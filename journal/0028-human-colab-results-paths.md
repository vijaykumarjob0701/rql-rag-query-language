# 0028 — Human + Colab paths for experiment results

**Date:** 2026-09-17 ~00:25 IST (Europe/Dublin)  
**Type:** Hand-off / reproducibility plumbing  
**Status:** Docs + Colab notebook + optional CPU smoke written; **no push**  
**Artifacts:**
- [`../experiments/HOW_TO_PROVIDE_RESULTS.md`](../experiments/HOW_TO_PROVIDE_RESULTS.md)
- [`../experiments/colab/fanns_microbench_colab.ipynb`](../experiments/colab/fanns_microbench_colab.ipynb)
- [`../experiments/colab/README.md`](../experiments/colab/README.md)
- [`../experiments/datasets/README.md`](../experiments/datasets/README.md) (+ `.gitignore`)
- [`../experiments/harness/fanns_synthetic_cpu.py`](../experiments/harness/fanns_synthetic_cpu.py)
- Smoke (optional): `experiments/results/fanns/synthetic_cpu_smoke_2026-09-17/` — **smoke / not P0**

**Prior:** journal 0027 pause / human P0 checklist

---

## Context

Offline compile stack is in-repo; citation-ready eval still needs human-owned FANNS / datasets / live adapters. Clear return paths (local, Colab zip, agent smoke) reduce friction without inventing P0 metrics.

## Question asked

How should Vijay (and agents, for tiny smoke only) deliver protocol artifacts into the listed git paths?

## What we added

| Path | Role |
|------|------|
| `HOW_TO_PROVIDE_RESULTS.md` | Preferred commit layout; metrics schema; Options A/B/C |
| `colab/fanns_microbench_colab.ipynb` | Synthetic PRE/POST on Colab; zip export; optional SIFT1M stub + license note |
| `harness/fanns_synthetic_cpu.py` | N=5k NumPy PRE/POST smoke → `results/fanns/synthetic_cpu_smoke_<date>/` |
| `datasets/README.md` | Digest/license template; `data/` gitignored |

## 1–5% seed

None for literature — process unlock: **Colab zip → `experiments/results/fanns/<run_id>/`** is an explicit human path alongside local runs.

## Uncertainty

Colab FAISS wheel availability varies by runtime; notebook falls back cpu→hnswlib. Synthetic recall/latency are real for the toy generator only.

## Anti-overclaim

Synthetic Colab / CPU smoke **≠** SIFT1M P0. No ACORN numbers pasted. **No push.**

## Next questions

1. Vijay runs Option A or B with licensed vectors for protocol 01.  
2. Fill `experiments/datasets/README.md` digests.  
3. Optional P1 adapter `smoke.json` under `results/adapters/<backend>/`.
