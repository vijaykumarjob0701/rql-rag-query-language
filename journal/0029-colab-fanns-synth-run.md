# 0029 — Colab FANNS synthetic microbench (agent-run)

**Date:** 2026-09-17 ~00:38 IST (Europe/Dublin)  
**Type:** empirical smoke via Google Colab  
**Status:** results in-repo; **not P0**

## What happened

User signed into Google on the box browser. Agent uploaded `experiments/colab/fanns_microbench_colab.ipynb` to Colab and Runtime → Run all on **T4 GPU**.

- **Colab URL:** https://colab.research.google.com/drive/1FH33zBXZezHLS3cSAR5nJQdELxX29s_A
- **Backend:** faiss-gpu 1.15.1
- **Dataset:** synthetic Gaussian N=50000 d=128 seed=42 (SIFT1M skipped)
- **Artifacts:** `experiments/results/fanns/colab_synth_20260916_233628/`

## Labels

- **[Reproduced here]:** PRE vs POST latency/QPS shape on this synthetic setup (see `metrics.json`).
- **Not P0:** licensed large vector set + GT kNN still required per protocol 01 / PAUSE_CHECKLIST.
- Do **not** treat recall@10=1.0 on synthetic easy predicates as paper-ready ANN quality.

## Links registry

`experiments/colab/LINKS.md` updated.
