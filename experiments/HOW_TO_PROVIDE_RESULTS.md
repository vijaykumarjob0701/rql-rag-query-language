# How to provide experiment results

**Date:** 2026-09-17 (Europe/Dublin)  
**Audience:** Vijay (local / Colab) and agents (CPU-only smoke only)  
**Policy:** Commit **digests + metrics + ENV + plans** — not multi-GB binaries. Do **not** paste ACORN (or any paper) numbers into `metrics.json`.

Preferred path: run a protocol → write artifacts into the listed folders → commit/PR. Large vector files stay local (gitignored); record URLs, licenses, and digests instead.

---

## Exact folders

| Kind | Path | What to commit |
|------|------|----------------|
| **FANNS microbench** | `experiments/results/fanns/<run_id>/` | `metrics.json`, `ENV.txt`, `plans/` (commands or plan JSON), optional short `README.md` |
| **Datasets** | `experiments/datasets/README.md` | URLs, licenses, digests, local path notes; optional `experiments/datasets/.gitignore` so `data/` stays out of git |
| **Adapter smoke** | `experiments/results/adapters/<backend>/smoke.json` | Sanitized latency/OK smoke only — **never** API keys |

Example FANNS layout:

```
experiments/results/fanns/<run_id>/
  ENV.txt
  metrics.json          # preferred aggregated form
  metrics.jsonl         # optional per-row log (also fine)
  plans/                # command lines, index build notes, seed
  README.md             # optional: one paragraph on hardware / caveats
```

`<run_id>` should be unique and descriptive, e.g. `sift1m_faiss_ivf_2026-09-17` or `colab_synth_50k_<timestamp>`.

---

## `metrics.json` schema (protocol 01)

From [`protocols/01-fanns-microbench.md`](protocols/01-fanns-microbench.md). Each row (object in an array, or one object per line in `metrics.jsonl`) must include:

```json
{
  "selectivity": 0.05,
  "mode": "PRE",
  "recall_at_10": 0.0,
  "latency_p50_ms": 0.0,
  "latency_p95_ms": 0.0,
  "qps": 0.0,
  "n_queries": 0
}
```

| Field | Meaning |
|-------|---------|
| `selectivity` | Fraction of points matching the predicate (e.g. `0.01`, `0.05`, `0.1`, `0.5`) |
| `mode` | `PRE` (filter then search subset) or `POST` (ANN then filter); optional `SUBGRAPH` if available |
| `recall_at_10` | Recall@10 vs ground truth **under the same predicate** |
| `latency_p50_ms` / `latency_p95_ms` | Query latency percentiles in milliseconds |
| `qps` | Queries per second (steady-state) |
| `n_queries` | Number of queries in the measurement |

Also record in `ENV.txt`: library + version, CPU/GPU, OS, seed, dataset id, index params. Fix the random seed.

Aggregated form (recommended for git):

```json
{
  "run_id": "…",
  "label": "P0 | smoke",
  "rows": [ { "selectivity": 0.01, "mode": "POST", "…" : "…" } ]
}
```

---

## Option A — Local machine

1. Follow [`protocols/01-fanns-microbench.md`](protocols/01-fanns-microbench.md) (FANNS) and/or [`02-datasets.md`](protocols/02-datasets.md) / [`03-adapter-smoke.md`](protocols/03-adapter-smoke.md).
2. Use a licensed vector set (e.g. SIFT1M) for **P0**; synthetic predicates at \(s \in \{0.01, 0.05, 0.1, 0.5\}\).
3. Write outputs under the exact folders above.
4. Update `experiments/datasets/README.md` with digests/licenses; keep binaries under a gitignored `data/` path.
5. Commit metrics + ENV + plans only; open a PR. Do not force multi-GB blobs into git without an explicit LFS decision.

---

## Option B — Google Colab

1. Open [`colab/fanns_microbench_colab.ipynb`](colab/fanns_microbench_colab.ipynb) (see [`colab/README.md`](colab/README.md)).
2. Runtime: CPU is fine for the **synthetic** path; GPU optional (`faiss-gpu` with fallback to `faiss-cpu`).
3. Run all cells. The notebook writes `/content/rql_fanns_<run_id>/` with `ENV.txt`, `metrics.json` (and/or `metrics.jsonl`), `README.md`, and `plans/`.
4. Final cell zips the folder — **Download** the zip from Colab.
5. On your machine:

```bash
cd /path/to/rag-vector-query-lang
unzip ~/Downloads/rql_fanns_<run_id>.zip -d experiments/results/fanns/
# ensure files land at experiments/results/fanns/<run_id>/{metrics.json,ENV.txt,...}
git add experiments/results/fanns/<run_id>
git commit -m "results: FANNS Colab run <run_id>"
git push   # you push; agents do not
```

6. Optional SIFT1M cell: only after you accept the dataset license; still do not commit the raw vectors.

Synthetic Colab runs are useful for plumbing and PRE/POST shape checks. They are **not** a substitute for SIFT1M (or equivalent) **P0**.

---

## Option C — Agent CPU-only synthetic microbench (smoke)

Separate, agent-safe path:

- Script: [`harness/fanns_synthetic_cpu.py`](harness/fanns_synthetic_cpu.py)
- Tiny \(N \approx 5\text{k}\), CPU, synthetic vectors + predicates
- Writes `experiments/results/fanns/synthetic_cpu_smoke_<date>/`

**Label clearly: smoke / not P0.** Does not replace protocol-01 SIFT1M (or other licensed large-set) runs. Do not cite these numbers as paper evaluation results.

```bash
# from repo root
tooling/.venv/bin/python experiments/harness/fanns_synthetic_cpu.py
```

---

## What not to do

- Do not invent or copy paper tables (ACORN, FANNS survey curves, etc.) into `metrics.json`.
- Do not commit API keys or cluster credentials with adapter `smoke.json`.
- Do not commit multi-GB `.fvecs` / shards; digests + metrics only.
- Do not treat Option C (or Colab synthetic-only) as closing HUMAN_TODOS P0.
