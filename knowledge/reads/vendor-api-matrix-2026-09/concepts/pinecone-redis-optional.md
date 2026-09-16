---
type: Concept
title: Pinecone & Redis (optional quick rows)
vendor: pinecone-redis
tags: [optional, hybrid, filter]
status: provisional
sources:
  - https://docs.pinecone.io/guides/search/hybrid-search
  - https://docs.pinecone.io/guides/search/filter-by-metadata
  - https://redis.io/docs/latest/develop/ai/search-and-query/vectors/
---

# Pinecone / Redis (optional)

**Pinecone:** Metadata filters (+ text-match); docs say filters **narrow candidates before ranking**; hybrid via dense+sparse, text-match-then-dense, or **client RRF**. Server RRF: not first-class in reviewed overview. EXPLAIN **UNKNOWN**.  

**Redis:** `FT.SEARCH` with `primary_filter_query=>[KNN …]`; filter modes `BATCHES` / `ADHOC_BF` (auto). First-class RRF / late interaction: **UNKNOWN** in reviewed vector concepts page.  

**RQL map:** Optional adapters; prefer core five for MVP capability matrix.
