---
type: Concept
title: pgvector — SQL WHERE, post-filter, iterative scans, app hybrid
vendor: pgvector
tags: [sql, postfilter, iterative-scan, explain]
status: provisional
sources:
  - https://github.com/pgvector/pgvector/blob/master/README.md
  - https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py
---

# pgvector

**Surface:** SQL.  
**Filter+ANN:** On approx indexes, filtering applied **after** index scan (**POST**); **iterative index scans** (≥0.8.0) rescind more of the index; partial indexes / partitioning optional.  
**Hybrid:** Compose with Postgres FTS; RRF example in pgvector-python — **not** built-in BM25/RRF operators.  
**EXPLAIN:** Full PostgreSQL `EXPLAIN` / `ANALYZE`.  
**RQL map:** Best **plan visibility**; FilterExec often POST+iterative or PRE via selective btree; `Fuse_rrf` usually **client/SQL CTE shim**.
