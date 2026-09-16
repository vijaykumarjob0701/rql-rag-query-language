---
type: Figure
title: "Figure 5 — PLAID scoring pipeline"
tags: [plaid, figure, pipeline]
status: provisional
---

# Figure 5

Four boxes: Stage 1 candidate generation (`nprobe`) → Stage 2 centroid interaction **with** prune (`t_cs`, TopK `ndocs`) → Stage 3 centroid interaction **without** prune (TopK `ndocs/4`) → Stage 4 residual decompress + MaxSim (TopK `k`).

**Use for RQL:** Canonical physical plan sketch for `LATE_PLAID` — see [../algorithms/four-stage-pipeline.md](../algorithms/four-stage-pipeline.md).
