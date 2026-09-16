---
type: AlgorithmNote
title: A1–A17 FANNS algorithm families (survey §3)
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# A1–A17 families `[Established survey classification]`

Preliminary Algs 1–2 (IVF / graph search) are ANNS baselines, not FANNS families.

| ID | Name | Pruning class | Mechanism gist | Hypothesized FilterExec |
|----|------|---------------|----------------|-------------------------|
| A1 | Post-Filtering family | VSP | Top-\(K'\) ANN then filter; \(K'\) guess / grow | **POST** |
| A2 | VBase | VSP (refined) | Filter-aware result update + relaxed monotonicity stop | **ITERATIVE** |
| A3 | AIRSHIP | VJP | Probabilistic expand satisfied/unsatisfied neighbors | SUBGRAPH-adjacent |
| A4 | ACORN | VJP | Traverse **predicate subgraph** only | **SUBGRAPH** |
| A5 | Faiss-IVF | VJP | Skip non-matching while scanning inverted lists | POST/scan hybrid |
| A6 | CAPS | VJP | Attribute frequency tree per IVF cluster | PARTITION-adjacent |
| A7 | NHQ | VJP | Fusion vector + fusion distance → plain ANN | *not FilterExec* (fusion index) |
| A8 | HQANN | VJP | NHQ-like alternate fusion distance | *not FilterExec* |
| A9 | Filtered-DiskANN | VJP | Stitched/Filtered Vamana; equality subgraphs | **SPECIALIZED** |
| A10 | SeRF | VJP | Range-specific subgraph overlay | SPECIALIZED (range) |
| A11 | iRangeGraph | VJP | Segment-tree of range subgraphs | SPECIALIZED (range) |
| A12 | Pre-Filtering family | SSP | Exact filter then brute scan (opt. PQ) | **PRE** |
| A13 | Milvus-Partition | SJP | Workload scalar partition + per-subset FANNS | **PARTITION** |
| A14 | HQI | SJP | Filter-based multi-layer qd-tree partitions | **PARTITION** |
| A15 | MA-NSW | SJP | NSW per scalar-tuple containment | PARTITION/SPECIALIZED |
| A16 | UNG | SJP | Prefix-tree-linked subset graphs | PARTITION/SPECIALIZED |
| A17 | WST | SJP | Window/segment tree + several search methods | PARTITION/SPECIALIZED |

**§6.3 combination:** dynamic choice among families (cost-model selectivity; ACORN→A12 when highly selective) → **ROUTER** / **AUTO** `[hypothesis]`.
