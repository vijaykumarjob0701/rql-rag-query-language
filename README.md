# RAG / Vector Query Languages — Research Package (2026-09-16)

## Executive summary

**Do vector databases have a query language like SQL / Redis commands / MongoDB QL?**  
**Partially yes — but there is no industry-standard equivalent.** Production systems expose *vendor-specific* interfaces: JSON/REST filter DSLs (Pinecone, Qdrant, Turbopuffer), GraphQL operators (Weaviate), boolean expression strings (Milvus), SQL extensions (pgvector, ClickHouse, DuckDB, SQL Server `VECTOR_SEARCH`, TopK SQL, VelesQL), Redis command dialects (`FT.SEARCH` / `FT.HYBRID`), Cypher `SEARCH` (Neo4j 2026.01+), and Vespa YQL. A few *dedicated* SQL-like languages exist as products or proposals (**TopK SQL**, **VelesQL**, **QQL** for Qdrant, O’Reilly’s hypothetical **VQL**), but none is a cross-vendor standard analogous to ANSI SQL.

**What exists today for vector + metadata in RAG?**  
Nearly every engine supports **ANN/kNN + metadata filters**, and most mature engines support **hybrid BM25/sparse + dense** with RRF or weighted fusion. RAG apps typically compose this in application code (LangChain/LlamaIndex): embed → top-k → filter → (optional) hybrid fuse → rerank → generate. Multi-hop / agentic / GraphRAG patterns live *above* the DB, not in a shared query language.

**Gaps:** no portable query language; filter semantics and filter-pushdown quality vary; limited joins/aggregations over chunks; hard to express multi-stage retrieval plans declaratively; weak reproducibility and cost-based planning for ANN+filter+hybrid+rerank pipelines.

**Feasibility of a dedicated RAG query language:** **Yes — feasible and useful**, especially as a *portable IR* that compiles to backend adapters with a planner for filter pushdown, hybrid fusion, and multi-hop plans. Expect gains in **reliability** (reproducible plans), **latency** (better pushdown / fewer round-trips), and **accuracy** (declarative hybrid + structured multi-hop) — not magic recall from syntax alone. Risks: semantic impedance across backends, ANN non-determinism, and premature standardization.

This package proposes **RQL (Retrieval Query Language)** — a SQL-inspired DSL for RAG retrieval plans. See [`docs/03-proposal.md`](docs/03-proposal.md).

---

## Motivation: accuracy, reliability, speed

| Dimension | Why a query language helps |
|-----------|----------------------------|
| **Accuracy** | Declares hybrid weights, fusion (RRF/linear), over-fetch + rerank, and multi-hop structure so teams stop hard-coding ad-hoc Python that silently drifts. |
| **Reliability** | Same RQL text → same logical plan → auditable EXPLAIN; reduces “works on Qdrant, broken on Pinecone” filter bugs. |
| **Speed** | Planner can push filters into ANN, choose pre- vs post-filter, fuse server-side when available, batch multi-queries, and avoid client round-trips. |

RAG efficiency is dominated by: embedding cost, ANN latency under filters, hybrid fusion, reranker tokens, and multi-hop loops. A language that *names* these stages lets optimizers and eval harnesses target them.

---

## Package contents

| Path | Contents |
|------|----------|
| [`docs/01-landscape.md`](docs/01-landscape.md) | Survey of vector DB query APIs with concrete examples |
| [`docs/02-gaps-and-needs.md`](docs/02-gaps-and-needs.md) | Gaps vs SQL / Redis / MongoDB |
| [`docs/03-proposal.md`](docs/03-proposal.md) | RQL goals, grammar sketch, compilation, planner (v1) |
| [`docs/04-related-work.md`](docs/04-related-work.md) | Papers, OSS, products (2024–2026) |
| [`docs/05-brainstorm-adjacent.md`](docs/05-brainstorm-adjacent.md) | **v2** Adjacent search angles (22) |
| [`docs/06-deep-literature.md`](docs/06-deep-literature.md) | **v2** 28 papers/systems from sideways search |
| [`docs/07-evolved-idea.md`](docs/07-evolved-idea.md) | **v2** Algebra, layers, steal-vs-invent map |
| [`docs/references.md`](docs/references.md) | All URLs used |
| [`NOTES-search-log.md`](NOTES-search-log.md) | Search queries + what each turned up |
| [`examples/`](examples/) | Example RQL queries (incl. v2 patterns 10–12) |

---



---

## Deep dive (v2) — adjacent research → evolved algebra

v1 answered “what query surfaces exist on vector DBs?” v2 asks the transformer-style question: **what adjacent fields already solved pieces of this problem?**

We brainstormed 22 sideways angles (classic IR QLs, PostGIS kNN+filter, array DBs, BlinkDB budgets, Calcite/Cascades, BigDAWG polystores, Substrait, Datalog, filtered ANN, ColBERT/MUVERA, GraphRAG, Lara/SystemDS, HyDE, provenance, VSS joins, learned FANNS planners, …), searched primary literature, and re-derived RQL as:

> a **retrieval algebra** over scored evidence + a **cost-based physical planner** for filter/ANN/fusion/late-interact strategies, compiled via **shims** to many backends — textual RQL is the frontend, not the product.

| Doc | What you’ll find |
|-----|------------------|
| [`docs/05-brainstorm-adjacent.md`](docs/05-brainstorm-adjacent.md) | Full angle list + steal vs invent |
| [`docs/06-deep-literature.md`](docs/06-deep-literature.md) | ≥28 annotated papers/systems |
| [`docs/07-evolved-idea.md`](docs/07-evolved-idea.md) | Genealogy, algebra, layers, roadmap |
| [`NOTES-search-log.md`](NOTES-search-log.md) | Transparent search process |

**Biggest shift:** filter strategy and approximate budgets are first-class (like attention was for sequence models); portable **plans** beat portable SQL skins.

## Quick answers

1. **Dedicated languages already?** Yes (emerging/non-standard): **TopK SQL**, **VelesQL**, **QQL**, O’Reilly **VQL** (hypothetical); also SQL/Cypher/GraphQL/YQL *extensions*, not a unified RAG standard.
2. **Dominant practice?** SDK/JSON: `query(vector, top_k, filter)` + app-side hybrid/rerank.
3. **Best near-SQL today for RAG?** pgvector (+ FTS), TopK SQL, SQL Server `VECTOR_SEARCH`, Redis `FT.HYBRID`, Neo4j Cypher `SEARCH`.
4. **Biggest gap?** Portable expression of *retrieval plans* (hybrid + filter + multi-stage + graph hop), not merely “nearest neighbors.”

*Research date: 2026-09-16 (Europe/Dublin).*
