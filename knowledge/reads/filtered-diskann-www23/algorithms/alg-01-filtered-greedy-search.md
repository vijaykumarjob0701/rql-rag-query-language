---
type: AlgorithmNote
title: "Algorithm 1 — FilteredGreedySearch"
status: provisional
---

# Alg. 1 FilteredGreedySearch(\(S, x_q, k, L, F_q\))

Label-aware greedy search: maintain candidate list ≤ \(L\); expand only out-neighbors sharing a label with query filter set \(F_q\); start from per-label start nodes \(\mathrm{st}(f)\).  
Paper benchmarks often use singleton \(F_q\); algorithm allows \(|F_q|>1\).
