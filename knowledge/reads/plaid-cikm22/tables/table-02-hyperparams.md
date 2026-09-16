---
type: Table
title: "Table 2 — PLAID hyperparameter configuration"
tags: [plaid, table]
status: provisional
---

# Table 2 (AUTHOR config)

| k | nprobe | t_cs | ndocs |
|---|--------|------|-------|
| 10 | 1 | 0.5 | 256 |
| 100 | 2 | 0.45 | 1024 |
| 1000 | 4 | 0.4 | 4096 |

Stage 3 always emits `ndocs/4` candidates (author heuristic, §4.3 / §5.1).
