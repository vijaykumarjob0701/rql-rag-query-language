---
type: Concept
title: Qdrant Query API — filters, RRF/DBSF, multivector
vendor: qdrant
tags: [filter, rrf, hybrid, multivector]
status: provisional
sources:
  - https://qdrant.tech/documentation/concepts/filtering/
  - https://qdrant.tech/documentation/search/hybrid-queries/
---

# Qdrant

**Filter DSL:** JSON `Filter` with `must` / `should` / `must_not` and field conditions (match, range, geo, …).  
**Hybrid:** Query API `prefetch` + fusion (`rrf`, `dbsf`); nested prefetch for multi-stage / ColBERT rescore.  
**RRF:** First-class; `k` configurable ≥1.16; **weights** ≥1.17.  
**Filter+ANN:** Filters on query; docs/PR emphasize propagating filters to leaf prefetches to avoid post-filter merge. Exact graph algorithm class: **UNKNOWN**.  
**EXPLAIN:** **UNKNOWN** in reviewed docs.  
**RQL map:** Strong native target for `Fuse_rrf`, multi-stage `Search_late` rescore, formula-ish custom scoring.
