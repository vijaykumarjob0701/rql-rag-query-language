---
type: AlgorithmNote
title: "Algorithms 4–5 — FilteredVamana and StitchedVamana"
status: provisional
---

# Alg. 4 FilteredVamana

Incremental: insert points with FilteredGreedySearch candidates + FilteredRobustPrune (Alg. 3) using geometry **and** label-set conditions; streaming-friendly.

# Alg. 5 StitchedVamana

Batch: build per-label Vamana graphs, union edges, prune to degree bound. Authors report better search quality, slower/less incremental build than FilteredVamana.
