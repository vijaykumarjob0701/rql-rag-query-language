---
type: Concept
title: Weaviate — hybrid fusion, pre-filter, multi-vector
vendor: weaviate
tags: [hybrid, prefilter, colbert, graphql]
status: provisional
sources:
  - https://docs.weaviate.io/weaviate/concepts/search/hybrid-search
  - https://docs.weaviate.io/weaviate/concepts/filtering
  - https://docs.weaviate.io/weaviate/tutorials/multi-vector-embeddings
---

# Weaviate

**Surface:** GraphQL + clients.  
**Hybrid:** BM25 + vector; `alpha`; `fusionType` `relativeScoreFusion` (default ≥v1.24) or `rankedFusion`.  
**Filter+ANN:** Documented **pre-filtering** (allow-list); ACORN strategy default from v1.34.  
**Multi-vector:** ColBERT-style late interaction ≥v1.29.  
**EXPLAIN:** **UNKNOWN**.  
**RQL map:** Strong `Search_late` + hybrid; `rankedFusion` ≠ Cormack RRF API name but rank-based; score fusion ≈ weighted/normalized linear family.
