---
type: Table
title: "Table 3 — MS MARCO v1 end-to-end (AUTHOR)"
tags: [plaid, table, author-only]
status: provisional
---

# Table 3 — in-domain MS MARCO v1 (**AUTHOR numbers — unreproduced**)

Selected rows (see page-07 render for full table):

| System | MRR@10 | R@100 | R@1k | Latency 8-CPU / GPU (ms) |
|--------|--------|-------|------|---------------------------|
| Vanilla ColBERTv2 (p=4, c=2^16) | 39.7 | 91.4 | 98.3 | 4568.5 / 259.6 |
| PLAID ColBERTv2 (k=10) | 39.4 | — | — | 31.5 / 11.5 |
| PLAID ColBERTv2 (k=100) | 39.8 | 90.6 | — | 52.9 / 20.2 |
| PLAID ColBERTv2 (k=1000) | 39.8 | 91.3 | 97.5 | 101.3 / 38.4 |

Narrative speedup at matched quality (\(k=1000\)): **~6.8× GPU / ~45× CPU** vs vanilla (AUTHOR). **Do not cite as our measurement.**
