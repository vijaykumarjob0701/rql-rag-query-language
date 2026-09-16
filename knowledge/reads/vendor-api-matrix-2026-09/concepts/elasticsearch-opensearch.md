---
type: Concept
title: Elasticsearch / OpenSearch — knn filter, hybrid, RRF
vendor: elasticsearch-opensearch
tags: [knn, rrf, hybrid, profile]
status: provisional
sources:
  - https://www.elastic.co/guide/en/elasticsearch/reference/8.19/knn-search.html
  - https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrievers/rrf-retriever
  - https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/
---

# Elasticsearch / OpenSearch

**ES filter+ANN:** `knn.filter` applied **during** approximate kNN (docs contrast with post-filter under-returning *k*).  
**ES hybrid:** `retriever.rrf` combining standard/BM25 and knn; or query+knn score sum with boosts.  
**ES RRF:** `rank_constant` (default 60), `rank_window_size`; per-retriever **weights** (Stack ≥9.2).  
**ES plan visibility:** Profile API (timing); kNN-specific EXPLAIN tree **UNKNOWN**.  
**OpenSearch hybrid:** `hybrid` query + search pipeline; RRF via score-ranker (`rank_constant` default 60, weights sum 1.0) **or** normalization+mean combiners.  
**OS explain:** Hybrid score explanation processors documented; full physical plan **UNKNOWN**.  
**RQL map:** Native `Fuse_rrf`; FilterExec ≈ in-search filtered knn (ES); capability flags differ ES vs OS pipelines.
