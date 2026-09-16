# 07 — Evolved Idea: RQL after Deep Adjacent Research

**Research date:** 2026-09-16 (Europe/Dublin)  
**Inputs:** v1 proposal ([`03-proposal.md`](03-proposal.md)) + brainstorm ([`05`](05-brainstorm-adjacent.md)) + literature ([`06`](06-deep-literature.md)).

---

## Genealogy (attention → transformer style)

| Stage | Field insight | What it becomes in RQL |
|-------|---------------|------------------------|
| 1 | Classical IR: ranking is an **operator algebra** (Indri `#combine`/`#weight`, RRF, MMR) | Scored relations + Fuse/Diversify ops |
| 2 | Spatial SQL: kNN + predicate needs **lossy index + recheck + EXPLAIN** (PostGIS/GiST) | Filter strategies + EXPLAIN traits |
| 3 | Filtered ANN 2023–2026: PRE/POST/ITERATIVE/predicate-subgraph/partition/router — **no universal winner** | Physical `FilterExec` chosen per query |
| 4 | VBASE: ANN as **iterator**, not TopK RPC | Open/Next plans; VSIM JOIN |
| 5 | Polystore + Substrait: portable **plan IR + shims**, not one SQL dialect | RQL text → LogicalPlan → PhysicalPlan → adapters |
| 6 | ColBERT/MUVERA: late interaction has **rewrites** (FDE, centroid prune) | `LATE_INTERACT` leaf + rewrite rules |
| 7 | HyDE/multi-query: rewrites are **plan nodes** with token cost | `REWRITE` / `HYDE` / `DECOMPOSE` — HyDE mechanism Established (0032); packaging Hypothesis |
| 8 | BlinkDB: declare **error/latency budgets** for approximate answers (**Pass 1–5 done**, journal **0031**) | `RECALL` / `LATENCY` options (Hypothesis packaging; ε≠recall@k) |
| 9 | Lara: tiny kernel (join ∪ union ∪ ext) unifies relational + linear | Minimal RQL algebra |
| 10 | GraphRAG + Datalog: multi-hop is **bounded recursion** | `TRAVERSE` / `WITH RECURSIVE` |

**Thesis shift:** v1 framed RQL as “SQL-inspired DSL for RAG pipelines.” v2 frames RQL as a **retrieval algebra + cost-based physical planner** whose textual DSL is only a frontend — analogous to how SQL fronts relational algebra, and how Substrait fronts engines.

---

## Evolved thesis (one paragraph)

**RQL is a portable intermediate representation for retrieval plans:** a small algebra over *scored multisets of evidence* (chunks, entities, paths) with leaves for dense, sparse/BM25, and late-interaction search; combinators for filter, fuse, diversify, rewrite, expand, traverse, and vector-similarity join; and a Cascades/Calcite-style optimizer that maps each logical plan onto backend-specific physical strategies (filter pushdown vs ACORN-like traversal vs iterative VBASE-style scan, RRF vs learned linear fusion, ColBERT vs MUVERA rewrite) under explicit recall/latency/ACL constraints — compiling via polystore-like shims to Pinecone/Qdrant/pgvector/Redis/ES/Neo4j/etc., with EXPLAIN provenance so RAG systems stop being unreproducible Python glue.

---

## Algebra (logical layer)

### Domain

- **Evidence relation** `E(id, payload, score, channel, provenance…)` — multiset of scored items.
- **Channels** ∈ {`dense`, `bm25`, `sparse`, `late_interact`, `graph`, `rewrite`, …}.
- Scores are **channel-local** until a Fuse op.

### Core operators (Lara-inspired kernel + IR)

| Op | Signature (informal) | Inspiration |
|----|----------------------|-------------|
| `Search_dense(q, k, metric)` | → E | ANN leaf |
| `Search_bm25(q, k)` | → E | Lexical leaf |
| `Search_late(q, k)` | → E | ColBERT/MaxSim |
| `Filter(P)` | E → E | Predicates / ACL |
| `Union` | E×E → E | Multi-query |
| `Fuse_rrf(k)` / `Fuse_linear(w)` / `Fuse_ltr(model)` | E* → E | Cormack RRF; Bruch CC; LTR |
| `Diversify_mmr(λ)` | E → E | Carbonell MMR |
| `Rerank(model, n)` | E → E | Cross-encoder |
| `Expand_parent` / `Expand_window` | E → E | Parent-child RAG |
| `Rewrite_hyde` / `Rewrite_multi` | q → q* or emb* | HyDE **[Established mech.** journal 0032**]** / DMQR **[Provisional]**; RQL packaging **[Hypothesis]** |
| `Traverse(pattern)` | E → E | GraphRAG / Cypher |
| `VSimJoin(θ)` | E×E → E | DiskJoin / SimJoin |
| `Ext(f)` | E → E | Generic map/flatmap (Lara ext) |

**Composability rule:** Anything that returns evidence can feed Fuse/Filter/Rerank. Rewrites feed Search. Traverse/VSimJoin bind identifiers for subsequent Filter pushdown.

### Layers

```
Textual RQL  ──parse──►  LogicalPlan (ops above)
                              │
                     Cascades/Volcano rewrites
                     (push Filter, choose Fuse,
                      rewrite LateInteract→FDE,
                      bound recursion, inject ACL)
                              │
                              ▼
                         PhysicalPlan
              FilterExec{PRE|POST|ITER|SUBGRAPH|AUTO}
              AnnExec{HNSW|IVF|DiskANN|…; ef,nprobe}
              FusionExec, RerankExec, ShimCast
                              │
                     adapters / BigDAWG-style shims
                              ▼
              Qdrant | pgvector | Pinecone | Neo4j | …
```

---

## Inspiration map (steal vs invent)

| Steal | From | Invent / specialize |
|-------|------|---------------------|
| Operator composability | Indri/Galago | Dense/late-interact leaves |
| Context sets / profiles | CQL | Hybrid / GraphHop / LateInteract profiles |
| Index Cond + recheck vocabulary | PostGIS/GiST | Recall-aware cost units |
| Island + shim + CAST | BigDAWG | Retrieval island semantics |
| Portable plan IR doctrine | Substrait | Evidence relation types & ANN traits |
| Logical/physical + rules | Calcite/Cascades | FANNS physical operators |
| Error/latency budgets | BlinkDB | `RECALL TARGET` ↔ ef/candidates |
| join ∪ union ∪ ext kernel | Lara | Score/channel attributes |
| Predicate-agnostic traversal | ACORN | Declarative `FILTER_MODE` |
| Label-aware graphs | Filtered-DiskANN | Capability negotiation |
| Iterator ANN | VBASE | RQL Open/Next execution model |
| Rank fusion theory | RRF + CC analysis | Named Fuse ops + LEARNED |
| Late-interact engines | ColBERT/PLAID/MUVERA | Rewrite rules in planner |
| Hypothetical docs | HyDE | `REWRITE` cost in planner |
| Bounded recursion | Dedalus/Datalog | `MAX_HOPS` + stratified RAG rules |
| Cross-lib fusion | Weld | Client-side materialization bans |
| Cardinality probes | Exqutor | ANN probe during planning |
| Query routing | 2026 FANNS routers | `FILTER_MODE AUTO` policy |

---

## Refined language surface (delta from v1)

v1 grammar stays valid. Additions motivated by research:

```text
-- Budgets (BlinkDB-inspired)
OPTION RECALL TARGET 0.92 LATENCY 80ms

-- Explicit physical hints (still optional; AUTO preferred)
FILTER_MODE AUTO | PUSHDOWN | POST | ITERATIVE | SUBGRAPH

-- Late interaction + rewrite
REWRITE HYDE MODEL 'gpt-…' AS hyp
SEARCH LATE_INTERACT ON token_vectors CANDIDATES 200
  -- planner may rewrite to FDE_ANN + MAXSIM

-- Vector similarity join (entity linking)
VSIM JOIN entities ON chunks.emb <=> entities.emb < 0.25

-- Bounded multi-hop
WITH RECURSIVE hop AS ( … ) MAX_HOPS 3

-- Provenance
EXPLAIN (LOGICAL, PHYSICAL, PROVENANCE)
```

Capability negotiation (CQL-inspired):

```text
PROFILE hybrid_v1;     -- requires BM25+dense+RRF
PROFILE graph_hop_v1;  -- requires Traverse or equivalent CAST
PROFILE late_v1;       -- requires multi-vector or MUVERA rewrite
```

---

## Planner (what “cost” means for retrieval)

Unlike relational selectivity alone, RQL cost is a **vector of**:

1. **Recall proxy** (ef, nprobe, candidate depth, filter strategy risk of empty results)
2. **Latency** (ANN, fusion, rerank tokens, LLM rewrite tokens, network RTTs)
3. **ACL safety** (must push mandatory predicates server-side — hard constraint)
4. **Dollar/token budget** (embeddings + rerankers + HyDE)

**Rules (examples):**

- Low selectivity + POST → rewrite to ITERATIVE (VBASE) or SUBGRAPH (ACORN) or overfetch×1/selectivity.
- `LATE_INTERACT` + backend without multi-vector → MUVERA-style FDE rewrite if extension present; else warn.
- Independent CTEs → parallel schedule (PlanRAG-adjacent, but over RQL IR).
- No single FANNS winner → `AUTO` consults router model + offline QPS/recall table (2026 routing papers).

---

## Five “aha” insights (deepening RQL)

1. **Filter strategy is the attention mechanism of vector RAG.** The literature shows PRE/POST/ITERATIVE/SUBGRAPH/PARTITION/ROUTER are first-class physical ops; treating `WHERE` as a boolean bolted onto TopK is why production RAG gets empty results. RQL’s job is to *name and plan* these strategies.

2. **Portable SQL text is the wrong abstraction; portable plans are right.** Substrait/BigDAWG teach: standardize the IR and shims. TopK/VelesQL skins are useful frontends, not the endgame.

3. **ANN should be an iterator in a larger algebra (VBASE), enabling joins — not only TopK.** Parent expansion, entity linking, and multi-corpus RAG need `VSIM JOIN` / incremental scan, not only `LIMIT k`.

4. **Fusion and late interaction are algebraic, with proven rewrites.** RRF vs learned linear (Bruch), ColBERT→PLAID→MUVERA show the planner needs rewrite rules, not hard-coded product fusion.

5. **Declare recall/latency like BlinkDB declares error bars.** Approximate systems need approximate *contracts*. Hidden `ef=64` folklore should become explicit options tied to EXPLAIN.

---

## What not to invent

- Another vendor JSON filter dialect.
- Guarantees of identical recall across HNSW libraries.
- Full multimedia MPEG-7 MPQF (too heavy; steal QueryByExample ideas only).
- Unbounded Datalog recursion in online RAG (always bound hops/latency).

---

## Research → engineering roadmap

| Phase | Deliverable |
|-------|-------------|
| P0 | Spec LogicalPlan JSON/protobuf (Substrait-inspired) + textual RQL parser |
| P1 | Adapters: pgvector, Qdrant, one JSON-API store; EXPLAIN LOGICAL/PHYSICAL |
| P2 | Filter planner (selectivity stats + AUTO router); Fuse RRF/LINEAR |
| P3 | Rewrite ops (multi-query, HyDE); LateInteract + optional FDE rewrite |
| P4 | Traverse shim to Neo4j; VSIM JOIN for entity tables |
| P5 | Learned cost model; provenance export for eval harnesses |

---

## Relationship to v1 package

- v1 landscape/gaps/proposal remain valid as product survey + initial syntax.
- v2 **deepens the compiler story**: algebra, physical FANNS ops, polystore shims, budgets, provenance.
- Examples added: rewrite+budget, vsim join, explain/provenance patterns (see `/examples`).
