# 05 — Adjacent Angles Brainstorm (Deep Dive v2)

**Research date:** 2026-09-16 (Europe/Dublin)  
**Goal:** Evolve RQL by searching *sideways* — not “query language for vector DB” alone — the way transformers came from deep learning → attention → “Attention is All You Need.”

This list drove the literature sweep in [`06-deep-literature.md`](06-deep-literature.md) and the redesign in [`07-evolved-idea.md`](07-evolved-idea.md). Process log: [`../NOTES-search-log.md`](../NOTES-search-log.md).

---

## Why adjacent search?

v1 surveyed vendor APIs and emerging VQL/TopK/VelesQL skins. That answers “what exists.” It does **not** answer “what algebra should RQL *be*?” The missing pieces live in classical IR, spatial/array DBs, AQP, federated polystores, filtered-ANN theory, late interaction, declarative ML, and cost-based optimizers — fields that already solved analogous problems under different names.

---

## Brainstorm list (22 angles)

| # | Angle | Why it matters for RQL | Steal vs invent |
|---|-------|------------------------|-----------------|
| 1 | **Classic IR QLs** (INQUERY, Indri, Galago, Terrier matchop, Lucene QP) | Proven operator algebras for belief combination (`#combine`, `#weight`, `#wand`), proximity, filters (`#filreq`), and field restriction — closer to ranking than SQL | **Steal** operator taxonomy & composability; invent dense/sparse/ColBERT leaves |
| 2 | **CQL / SRU** (Library of Congress Contextual Query Language) | Portable human-readable IR language with context sets — existence proof that IR can standardize without becoming SQL | **Steal** context-set / profile idea for backend capability negotiation |
| 3 | **Spatial QL / PostGIS / R-trees / GiST** | kNN (`<->`) + predicate is the closest SQL analogy to ANN + filter; lossy index filter + recheck; EXPLAIN of Index Cond vs Filter | **Steal** planner vocabulary (Index Cond / recheck / best-first); invent recall-aware costs |
| 4 | **Array databases** (SciDB AFL/AQL, Rasdaman rasql, TileDB) | Multidimensional operators, chunking, functional algebras (AFL) as compile targets | **Steal** functional IR style for plan DAGs; invent embedding-space ops |
| 5 | **SQL/MM + MPEG-7 MPQF** | Standards for content-based multimedia retrieval (QueryByMedia, QueryByDescription, ROI, relevance feedback) | **Steal** query-by-example / feedback operators; avoid over-standardizing early |
| 6 | **AQP / BlinkDB / BlazeIt FrameQL** | Declarative **error/latency budgets** (`ERROR WITHIN ε`, time bounds) — ANN is already approximate | **Steal** first-class `RECALL TARGET` / `LATENCY BUDGET` syntax; invent ANN-specific error semantics |
| 7 | **Cascades / Volcano / Apache Calcite** | Logical→physical rewrite, traits, cost factories, adapters over heterogeneous sources | **Steal** planner architecture wholesale for RQL→backend adapters |
| 8 | **Polystores** (BigDAWG islands/SCOPE/CAST, Garlic wrappers) | Multi-model federation with shims — exact pattern for compiling one RQL to Qdrant + pgvector + Neo4j | **Steal** island / shim / CAST; invent retrieval-island semantics |
| 9 | **Substrait** | Open serialized relational plan IR (not SQL text) for cross-engine portability | **Steal** “portable plan, not portable SQL” doctrine; invent retrieval relation types |
| 10 | **Datalog / Dedalus / Vadalog** | Recursive multi-hop, fixpoint, temporal/distributed logic — formal home for GraphRAG hops | **Steal** recursive CTE / RULE sugar; invent retrieval-stratified recursion limits |
| 11 | **Text-to-SQL / NL→plan** | Schema linking + plan generation + verify — maps to NL→RQL with EXPLAIN verification | **Steal** generate-then-verify loop; RQL as safer target than free SQL |
| 12 | **Filtered ANN** (ACORN, Filtered-DiskANN, HQI, CAPS, Compass, SIEVE, FANNS surveys) | Core physical algebra: pre / post / iterative / predicate-subgraph / partition-bitmap | **Steal** `FILTER_MODE` taxonomy & selectivity-aware planning; invent declarative mapping |
| 13 | **Learning-based filtered-ANN planners** (2026 routing papers) | ML chooses pre vs post vs specialized index per query | **Steal** as physical planner policy; keep logical RQL stable |
| 14 | **Hybrid fusion** (RRF, CombSUM/CombMNZ, convex combination, LTR) | Fusion is an **algebraic operator**, not a product feature | **Steal** named fusion ops + learnable weights; invent calibrated multi-channel fuse |
| 15 | **ColBERT / PLAID / MUVERA** | Late interaction as first-class search leaf + physical rewrite (FDE→MIPS, centroid prune) | **Steal** `LATE_INTERACT` / `MAXSIM` ops + rewrite rules |
| 16 | **Graph + vector** (GraphRAG surveys, Cypher SEARCH, hybrid KG+ANN) | Traverse + embed as one plan language | **Steal** `TRAVERSE` / path patterns; invent bindings to chunk ids |
| 17 | **Declarative ML** (SystemDS, Weld IR, Lara algebra) | Unify linear algebra + relational; fuse across library boundaries | **Steal** small operator kernel (join/union/ext); invent retrieval-score as first-class attribute |
| 18 | **Query rewriting for RAG** (HyDE, multi-query, DMQR) | Rewrites as plan nodes: `REWRITE`, `HYDE`, `DECOMPOSE` before search | **Steal** as CTE-producing ops; invent cost of LLM rewrite tokens |
| 19 | **Provenance / EXPLAIN** (ProvSQL, why-provenance, plan lineage) | Auditable RAG: which rewrite, which channel, which filter path produced a chunk | **Steal** why-provenance on fused ranks; invent ANN nondeterminism markers |
| 20 | **ACL / constraint pushdown** | Security predicates must be server-enforced, not client-side cosmetic filters | **Steal** mandatory pushdown class + policy as typed predicates |
| 21 | **Vector similarity joins** (DiskJoin, SimJoin, threshold VSS joins) | Chunk↔entity, multi-corpus, cross-encoder candidate generation | **Steal** `VSIM JOIN` / threshold join; invent RAG-oriented join shapes |
| 22 | **Learned indexes / vector-augmented SQL optimizers** (Exqutor, etc.) | Cardinality of ANN is the hard meta-problem for planning | **Steal** exact/approx cardinality probes during planning |

---

## Genealogy sketch (pre-synthesis)

```
Classical IR operators (#combine, #filreq, RRF, MMR)
        + Spatial kNN planner vocabulary (GiST/PostGIS)
        + Filtered-ANN physical strategies (ACORN / DiskANN / Compass)
        + Polystore shims (BigDAWG) + Substrait-style plan IR
        + Late interaction leaves (ColBERT/MUVERA)
        + Recursive hop (Datalog) + rewrite ops (HyDE)
                    ↓
              RQL v2 algebra
     (logical retrieval plan → physical ANN plan)
```

This is the “attention → transformer” move: **compose known operators under a retrieval-specific algebra**, rather than inventing another JSON filter DSL.

---

## Explicit non-angles (parked)

- Full ANSI SQL standardization of embeddings (vendors already diverge on ANN).
- Guaranteeing identical recall across HNSW implementations (impossible; expose params instead).
- Replacing embedding model APIs (out of scope for a retrieval QL).

