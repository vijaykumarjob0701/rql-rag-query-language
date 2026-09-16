#!/usr/bin/env python3
"""FANNS synthetic CPU smoke — PRE/POST filtered search (NOT P0).

Tiny N≈5k microbench for plumbing metrics.json / ENV.txt layout.
Label: smoke / not P0. Does not substitute for SIFT1M protocol-01 runs.
Uses NumPy only (no FAISS required).
"""
from __future__ import annotations

import argparse
import json
import platform
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT_PARENT = REPO_ROOT / "experiments" / "results" / "fanns"

SELECTIVITIES = (0.01, 0.05, 0.1, 0.5)
K = 10
SEED = 42


def _now_dublin_label() -> str:
    # Europe/Dublin ≈ UTC+1 in September (IST) without requiring zoneinfo.
    from datetime import timedelta
    dublin = datetime.now(timezone.utc) + timedelta(hours=1)
    return dublin.strftime("%Y-%m-%d")


def l2_normalize(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x, axis=1, keepdims=True)
    n = np.maximum(n, 1e-12)
    return x / n


def brute_topk(db: np.ndarray, queries: np.ndarray, k: int) -> np.ndarray:
    """Return (nq, k) indices of nearest neighbors (L2 on normalized → IP)."""
    # db, queries: float32 unit vectors; maximize IP == minimize L2
    sims = queries @ db.T  # (nq, n)
    # argpartition for speed
    k = min(k, db.shape[0])
    part = np.argpartition(-sims, kth=k - 1, axis=1)[:, :k]
    # sort within top-k
    rows = np.arange(queries.shape[0])[:, None]
    top_sims = sims[rows, part]
    order = np.argsort(-top_sims, axis=1)
    return part[rows, order]


def recall_at_k(pred: np.ndarray, truth: np.ndarray) -> float:
    """Mean recall@k; pred/truth shape (nq, k)."""
    nq, k = pred.shape
    hits = 0
    for i in range(nq):
        hits += len(set(pred[i].tolist()) & set(truth[i].tolist()))
    return hits / (nq * k)


def filtered_gt(
    db: np.ndarray, queries: np.ndarray, mask: np.ndarray, k: int
) -> np.ndarray:
    """Brute GT restricted to mask (True = keep)."""
    ids = np.flatnonzero(mask)
    if ids.size == 0:
        return np.full((queries.shape[0], k), -1, dtype=np.int64)
    sub = db[ids]
    local = brute_topk(sub, queries, min(k, sub.shape[0]))
    # map back; pad if subset smaller than k
    out = np.full((queries.shape[0], k), -1, dtype=np.int64)
    mapped = ids[local]
    out[:, : mapped.shape[1]] = mapped
    return out


def post_filter_search(
    db: np.ndarray,
    queries: np.ndarray,
    mask: np.ndarray,
    k: int,
    candidate_mult: int = 50,
) -> tuple[np.ndarray, list[float]]:
    """POST: ANN (brute full) with oversized candidate list, then filter."""
    n = db.shape[0]
    cand_k = min(n, max(k * candidate_mult, k))
    times = []
    out = np.full((queries.shape[0], k), -1, dtype=np.int64)
    for i in range(queries.shape[0]):
        t0 = time.perf_counter()
        cands = brute_topk(db, queries[i : i + 1], cand_k)[0]
        kept = [int(c) for c in cands if mask[c]]
        if len(kept) < k:
            # fill remaining from masked universe by brute on subset (still POST-ish fallback)
            ids = np.flatnonzero(mask)
            if ids.size:
                sub_rank = brute_topk(db[ids], queries[i : i + 1], min(k, ids.size))[0]
                for j in ids[sub_rank]:
                    if int(j) not in kept:
                        kept.append(int(j))
                    if len(kept) >= k:
                        break
        out[i, : min(k, len(kept))] = kept[:k]
        times.append((time.perf_counter() - t0) * 1000.0)
    return out, times


def pre_filter_search(
    db: np.ndarray, queries: np.ndarray, mask: np.ndarray, k: int
) -> tuple[np.ndarray, list[float]]:
    """PRE: filter ids then brute on subset."""
    ids = np.flatnonzero(mask)
    times = []
    out = np.full((queries.shape[0], k), -1, dtype=np.int64)
    if ids.size == 0:
        return out, [0.0] * queries.shape[0]
    sub = db[ids]
    for i in range(queries.shape[0]):
        t0 = time.perf_counter()
        local = brute_topk(sub, queries[i : i + 1], min(k, sub.shape[0]))[0]
        out[i, : local.shape[0]] = ids[local]
        times.append((time.perf_counter() - t0) * 1000.0)
    return out, times


def percentile(xs: list[float], p: float) -> float:
    if not xs:
        return 0.0
    return float(np.percentile(np.asarray(xs, dtype=np.float64), p))


def run(
    n: int = 5000,
    d: int = 128,
    nq: int = 50,
    out_dir: Path | None = None,
) -> Path:
    rng = np.random.default_rng(SEED)
    run_id = f"synthetic_cpu_smoke_{_now_dublin_label()}"
    out = out_dir or (DEFAULT_OUT_PARENT / run_id)
    out.mkdir(parents=True, exist_ok=True)
    (out / "plans").mkdir(exist_ok=True)

    db = l2_normalize(rng.standard_normal((n, d), dtype=np.float64).astype(np.float32))
    queries = l2_normalize(
        rng.standard_normal((nq, d), dtype=np.float64).astype(np.float32)
    )
    # Independent Bernoulli predicates per selectivity (fixed seed stream)
    labels = rng.random(n)

    rows = []
    for s in SELECTIVITIES:
        mask = labels < s
        # ensure at least k matches for tiny s
        if mask.sum() < K:
            need = K - int(mask.sum())
            zeros = np.flatnonzero(~mask)
            take = zeros[:need]
            mask[take] = True
        gt = filtered_gt(db, queries, mask, K)

        for mode, fn in (("PRE", pre_filter_search), ("POST", post_filter_search)):
            if mode == "PRE":
                pred, times = fn(db, queries, mask, K)
            else:
                pred, times = fn(db, queries, mask, K, candidate_mult=50)
            rec = recall_at_k(pred, gt)
            p50 = percentile(times, 50)
            p95 = percentile(times, 95)
            mean_ms = statistics.mean(times) if times else 0.0
            qps = (1000.0 / mean_ms) if mean_ms > 0 else 0.0
            rows.append(
                {
                    "selectivity": s,
                    "mode": mode,
                    "recall_at_10": round(rec, 6),
                    "latency_p50_ms": round(p50, 4),
                    "latency_p95_ms": round(p95, 4),
                    "qps": round(qps, 4),
                    "n_queries": nq,
                }
            )

    metrics = {
        "run_id": run_id,
        "label": "smoke / not P0",
        "warning": (
            "Synthetic CPU smoke only. Not a substitute for SIFT1M (or other "
            "licensed large-set) protocol-01 P0 evaluation. Do not cite as paper results."
        ),
        "dataset": f"synthetic_gaussian N={n} d={d} seed={SEED}",
        "rows": rows,
    }
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    with (out / "metrics.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    env_lines = [
        f"run_id={run_id}",
        "label=smoke / not P0",
        f"date_ist≈{_now_dublin_label()} (Europe/Dublin)",
        f"python={sys.version.split()[0]}",
        f"numpy={np.__version__}",
        "ann_backend=numpy_brute (no faiss)",
        f"platform={platform.platform()}",
        f"processor={platform.processor() or 'unknown'}",
        f"n={n} d={d} n_queries={nq} k={K} seed={SEED}",
        f"selectivities={list(SELECTIVITIES)}",
        "modes=PRE,POST",
    ]
    (out / "ENV.txt").write_text("\n".join(env_lines) + "\n", encoding="utf-8")

    plan = {
        "command": "tooling/.venv/bin/python experiments/harness/fanns_synthetic_cpu.py",
        "seed": SEED,
        "n": n,
        "d": d,
        "n_queries": nq,
        "k": K,
        "selectivities": list(SELECTIVITIES),
        "modes": ["PRE", "POST"],
        "post_candidate_mult": 50,
        "note": "smoke / not P0",
    }
    (out / "plans" / "run.json").write_text(
        json.dumps(plan, indent=2) + "\n", encoding="utf-8"
    )
    (out / "README.md").write_text(
        "\n".join(
            [
                f"# {run_id}",
                "",
                "**Label: smoke / not P0.**",
                "",
                "Tiny synthetic PRE/POST filtered search on CPU (NumPy brute).",
                "Generated by `experiments/harness/fanns_synthetic_cpu.py`.",
                "Do **not** treat these metrics as citation-ready FANNS evaluation.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n", type=int, default=5000)
    ap.add_argument("--d", type=int, default=128)
    ap.add_argument("--nq", type=int, default=50)
    ap.add_argument("--out-dir", type=Path, default=None)
    args = ap.parse_args()
    out = run(n=args.n, d=args.d, nq=args.nq, out_dir=args.out_dir)
    print(f"Wrote smoke results under {out}")
    print("LABEL: smoke / not P0 — not a substitute for SIFT1M P0")


if __name__ == "__main__":
    main()
