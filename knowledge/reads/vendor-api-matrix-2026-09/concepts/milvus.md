---
type: Concept
title: Milvus — expr filter, hybrid_search, RRFRanker
vendor: milvus
tags: [expr, hybrid_search, rrf, weighted]
status: provisional
sources:
  - https://milvus.io/api-reference/pymilvus/v2.6.x/MilvusClient/Vector/hybrid_search.md
  - https://milvus.io/docs/v2.6.x/multi-vector-search.md
  - https://milvus.io/docs/reranking.md
---

# Milvus

**Filter DSL:** Boolean `expr` (alias `filter`) on each `AnnSearchRequest`.  
**Composition:** API docs say expression **applied before ANN** → treat as **PRE** (docs); internals **UNKNOWN** without smoke.  
**Hybrid:** `hybrid_search` over multiple ANN requests + ranker.  
**Fusion:** `RRFRanker` and `WeightedRanker` (documented).  
**EXPLAIN:** **UNKNOWN** (HTML guides often blocked to automated fetch; API used).  
**RQL map:** Clean compile target for multi-channel search + `Fuse_rrf` / weighted linear; verify expr semantics live (HUMAN P1).
