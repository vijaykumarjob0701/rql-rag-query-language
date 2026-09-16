---
type: Figure
title: "Figure 1 — MRR@10 vs mean query latency (MS MARCO)"
tags: [colbert, figure]
status: provisional
---

# Figure 1

**Caption (paper):** Effectiveness (MRR@10) versus Mean Query Latency (log-scale) for representative ranking models on MS MARCO Ranking.

**What we saw (page-01 render):** Pareto plot placing BM25/neural matchers at low latency/lower MRR; BERT-base/large at high MRR and ~10^4–10^5 ms; ColBERT re-rank and full-retrieval near BERT quality at much lower latency.

**Use for RQL:** Motivates `Search_late` as a first-class leaf when quality–cost tradeoff matters — **not** a reproduced latency claim.
