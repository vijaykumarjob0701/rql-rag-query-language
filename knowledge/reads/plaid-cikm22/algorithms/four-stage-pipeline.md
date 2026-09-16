---
type: Algorithm
title: PLAID four-stage scoring pipeline (Fig 5)
tags: [plaid, pipeline, algorithm]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:05:00+01:00
---

# Four-stage PLAID pipeline `[Established mechanism]`

From Fig 5 + §4 (no numbered Algorithm environment in paper; stages are prose + figure).

| Stage | Name | Inputs | Filter / score | Output size (hyperparams) |
|-------|------|--------|----------------|---------------------------|
| 1 | Initial candidate generation | Centroids \(C\), query \(Q\) | \(S_{c,q}=CQ^\top\); top-`nprobe` centroids/token → inverted list of **passage IDs** | Unbounded initial set (no `ncandidates` hard cut) |
| 2 | Centroid interaction **with** pruning | Centroid scores, PIDs | Drop tokens with max centroid score \(< t_{cs}\); MaxSim on pruned \(\tilde{D}\) | TopK(**`ndocs`**) |
| 3 | Centroid interaction **without** pruning | Centroid scores, PIDs | Full bag-of-centroids MaxSim | TopK(**`ndocs/4`**) |
| 4 | Final ranking | Residuals + centroids | Decompress → exact MaxSim (Eq. 1) | TopK(**`k`**) |

## Default hyperparameter grid (Table 2, AUTHOR)

| \(k\) | `nprobe` | \(t_{cs}\) | `ndocs` |
|------|----------|--------------|---------|
| 10 | 1 | 0.5 | 256 |
| 100 | 2 | 0.45 | 1024 |
| 1000 | 4 | 0.4 | 4096 |

## RQL packaging `[hypothesis]`
Physical plan id `LATE_PLAID` / capability `late_plaid` exposes (`nprobe`, `t_cs`, `ndocs`, `k`) as costable knobs; must not silently drop Stage 4 exact MaxSim when the logical op asked for late-interaction scores.
