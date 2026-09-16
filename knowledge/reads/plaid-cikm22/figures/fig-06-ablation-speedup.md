---
type: Figure
title: "Figure 6 — Ablation speedups (AUTHOR)"
tags: [plaid, figure, ablation]
status: provisional
---

# Figure 6

Cumulative speedup vs vanilla ColBERTv2 on MS MARCO v1 sample:

| Stack | GPU (AUTHOR) | CPU 8-thread (AUTHOR) |
|-------|--------------|------------------------|
| + Centroid interaction | 3.7× | 4.2× |
| + Centroid pruning | 5.2× | 8.6× |
| + Fast decompress / kernels | 6.6× | 42.4× |

**Honesty:** AUTHOR-only; do not treat as RQL harness results.
