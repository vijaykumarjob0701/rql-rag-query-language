# Protocol 01 — FANNS microbench (HUMAN)

**Goal:** Reproduce *a* filtered-ANN recall–latency curve under controlled selectivity. Do **not** paste ACORN paper numbers.

## Steps
1. Choose library + version; write `ENV.txt`.
2. Use a licensed vector set (e.g. SIFT1M) + synthetic predicates at s ∈ {0.01, 0.05, 0.1, 0.5}.
3. Implement PRE / POST / (optional SUBGRAPH if available).
4. Sweep candidate depth; record recall@10, p50/p95 latency, QPS.
5. Store under `experiments/results/fanns/<run_id>/`.

## Acceptance
- `metrics.json` with schema `{selectivity, mode, recall_at_10, latency_p50_ms, latency_p95_ms, qps, n_queries}`
- Plan or command lines recorded; seed fixed.
