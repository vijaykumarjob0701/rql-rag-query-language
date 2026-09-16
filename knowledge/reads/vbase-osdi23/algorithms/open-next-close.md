---
type: AlgorithmNote
title: Open / Next / Close vector index adaptation
status: provisional
---

# Open / Next / Close (§4.2)

**ESTABLISHED-FOR-US (paper says):** VBASE re-architects HNSW / IVFFlat / SPANN to expose Volcano iterators instead of TopK-only RPCs.

| Index | Open (sketch) | Next (sketch) | State |
|-------|---------------|---------------|-------|
| HNSW | Search upper layers for entry | Return closest unvisited; expand neighbors into candidates | visited bitmap, current node, candidates |
| IVFFlat | Sort lists by centroid distance | Stream vectors from nearest lists | sorted lists + cursor |
| SPANN | (incorporated; billion-scale) | similar iterator adaptation | — |

**Operators:** OrderBy+limit TopK; scalar filter interleaved; distance range filter; Join via range-filter index join (§3.2, §4.2).  
**Code claim:** Authors cite ~200 LOC for HNSW adaptation; ~2k LOC PostgreSQL total — AUTHOR, not independently counted here.
