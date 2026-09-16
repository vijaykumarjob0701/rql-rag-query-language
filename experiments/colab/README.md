# Colab — FANNS microbench helpers

**Date:** 2026-09-17 (Europe/Dublin)

## Notebook

| File | Purpose |
|------|---------|
| [`fanns_microbench_colab.ipynb`](fanns_microbench_colab.ipynb) | Synthetic PRE/POST filtered ANN on Colab (faiss-cpu / optional GPU); optional SIFT1M cell with license note |

## How to return results

1. Run the notebook → zip downloads from `/content/rql_fanns_<run_id>/`.
2. Unzip into the repo at `experiments/results/fanns/<run_id>/`.
3. Commit `metrics.json`, `ENV.txt`, `plans/` (not multi-GB vectors).
4. Full instructions: [`../HOW_TO_PROVIDE_RESULTS.md`](../HOW_TO_PROVIDE_RESULTS.md) (Option B).

## Important

- Synthetic Colab runs validate plumbing and PRE/POST shape — **not** a substitute for licensed SIFT1M (or equivalent) **P0**.
- Do **not** paste ACORN or other paper numbers into metrics.
- Protocol: [`../protocols/01-fanns-microbench.md`](../protocols/01-fanns-microbench.md).
