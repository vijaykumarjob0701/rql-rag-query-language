# 0008 — HUMAN_TODO hand-off (no fake benches)

**Date:** 2026-09-16 (Europe/Dublin)  
**Type:** process / integrity  
**Status:** locked in

## Context

Parent/user addendum: anything beyond agent capability (GPU ANN, paid APIs, large datasets, production clusters, human judgments) must **not** be fabricated. Create clear HUMAN_TODO items for Vijay to run in this same GitHub repo and push.

## What we did

Created [`../experiments/HUMAN_TODOS.md`](../experiments/HUMAN_TODOS.md) with P0–P2 items, protocols `01`–`04`, expected artifact paths, and “what to push back”.

Linked from thesis §Evaluation and Appendix A (reproducibility).

## 1–5% seed

Integrity rule operationalised: **agent-run ≠ human-run**. Citation-ready eval waits on P0 FANNS microbench + dataset digests.

## Next questions

1. After Vijay lands one FANNS `metrics.json`, wire a results table into `thesis/sections/09` labelled REPRODUCED.
2. Continue VBASE Pass 1–5 (still queued in `0007`).
