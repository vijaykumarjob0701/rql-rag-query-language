# 04 — Related Work (papers, OSS, products; prefer 2024–2026)

## A. Dedicated / proposed vector query languages

| Work | Date | Type | Summary |
|------|------|------|---------|
| [O’Reilly *Vector Databases*, Ch. 9 “Vector Query Language” (VQL)](https://www.oreilly.com/library/view/vector-databases/9781098177584/ch09.html) | Book listed Apr 2026 | Hypothetical SQL-inspired VQL | Explicitly **not implemented**; calls for community/standards effort |
| [TopK SQL](https://www.topk.io/blog/20260614-topk-sql) | 2026-06-14 | Product SQL dialect | Postgres wire protocol; `semantic_similarity`, `bm25_score`, `vector_distance`, hybrid scoring in SELECT |
| [VelesQL (VelesDB)](https://github.com/cyberlife-coder/VelesDB/blob/main/docs/VELESQL_SPEC.md) | Spec updated 2026-06 | OSS SQL-like | `NEAR`, `SPARSE_NEAR`, `NEAR_FUSED`, `USING FUSION`, graph `MATCH`, JOINs |
| [QQL for Qdrant](https://github.com/pavanjava/qql) | Ongoing OSS | Thin SQL→Qdrant | SEARCH/SELECT/RECOMMEND, hybrid, WHERE, RERANK |
| [ProximaDB SQL extensions](https://github.com/anvai-labs/proximaDB) | 2026 (v0.2) | Early multi-model DB | pgvector-compatible ops; GRAPH_QUERY / DOCUMENT_QUERY |

## B. SQL / relational engines with vectors

| Work | Notes |
|------|-------|
| [pgvector](https://github.com/pgvector/pgvector) | De-facto SQL vector extension |
| [Supabase hybrid search](https://supabase.com/docs/guides/ai/hybrid-search) | SQL function: FTS + pgvector + RRF |
| [SQL Server VECTOR_SEARCH](https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-search-transact-sql?view=sql-server-ver17) | 2025/Azure; iterative filtering on latest DiskANN indexes |
| [DuckDB VSS](https://duckdb.org/docs/stable/extensions/vss.html) | In-process SQL ANN |
| [Lance + DuckDB SQL](https://lance.org/integrations/duckdb/sql/) | `lance_vector_search` UDF-style |
| ClickHouse ANN / distance SQL | Analytical SQL + vectors |

## C. Search / vector products with rich query surfaces

| Product | Query surface | Hybrid |
|---------|---------------|--------|
| [Weaviate GraphQL operators](https://docs.weaviate.io/weaviate/api/graphql/search-operators) | nearVector, bm25, hybrid | Native alpha / fusionType |
| [Qdrant Query API](https://qdrant.tech/documentation/concepts/search/) | prefetch + fusion | RRF, DBSF |
| [Pinecone metadata filters](https://docs.pinecone.io/guides/search/filter-by-metadata) | JSON `$` operators + text-match | Sparse/dense paths |
| [Redis FT.HYBRID](https://redis.io/docs/latest/commands/ft.hybrid/) | Since 8.4.0 | SEARCH + VSIM, RRF/LINEAR |
| [Elasticsearch RRF retriever](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rrf.html) | Retriever DSL | BM25 + knn |
| [OpenSearch hybrid RRF](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/) | Pipelines / hybrid query | From ~2.19 |
| [Turbopuffer query](https://turbopuffer.com/docs/query) | rank_by + filters + multi_query | RRF rerank_by |
| [Vespa YQL](https://docs.vespa.ai/en/querying.html) | nearestNeighbor + ranking | Ranking profiles |
| [Neo4j Cypher SEARCH](https://neo4j.com/docs/cypher-manual/current/clauses/search/) | 2026.01+ | In-index filters; hybrid via separate FT |
| [Milvus hybrid_search / RRF](https://milvus.io/docs/rrf-ranker.md) | Multi AnnSearchRequest | RRFRanker |

## D. Framework-level “query” abstractions (not full languages)

| Project | Role |
|---------|------|
| LangChain `SelfQueryRetriever` | NL → structured metadata filter + query |
| LlamaIndex `QueryFusionRetriever` / query engines | Multi-retriever fusion in Python |
| LangGraph / agentic RAG patterns | Imperative multi-step retrieval |
| Microsoft GraphRAG | Graph index + community summaries (pipeline, not QL) |

## E. Academic: query planning / structured retrieval for RAG (2024–2026)

| Paper | Venue/ID | Idea |
|-------|----------|------|
| [PlanRAG: When RAG Meets Query Planning (Logical Query Trees)](https://arxiv.org/html/2607.00508) | arXiv 2607.00508 (2026) | NL ERP → atomic queries → cost-based logical query trees; DB-planning analogy |
| [LogicRAG: Adaptive Reasoning Structures](https://arxiv.org/html/2508.06105v1) | arXiv 2508.06105 (2025) | Inference-time DAG of subproblems; topological retrieval; no pre-built graph |
| [RT-RAG: Reasoning in Trees](https://arxiv.org/html/2601.11255) | arXiv 2601.11255 (2026) | Consensus reasoning trees; bottom-up rewrite for multi-hop QA |
| [PruneRAG: Confidence-Guided Query Decomposition Trees](https://arxiv.org/pdf/2601.11024) | arXiv 2601.11024 (2026) | Decomposition tree + confidence pruning + parallel branches |
| Earlier PlanRAG / decision-focused RAG (2024) | Various | Planning for decision QA (distinct from 2026 LQT paper) |

**Note:** These papers plan **natural-language reasoning**, not a portable vector-store IR. They motivate RQL’s multi-hop CTEs and cost model, but do not replace product query APIs.

## F. Historical / adjacent query languages

- **SPARQL** — RDF graphs; vector extensions experimental, not RAG-standard.  
- **AQL (ArangoDB)** — multi-model; vectors via functions/indexes.  
- **Cypher** — now first-class vector `SEARCH` (Neo4j 2026).  
- **Elasticsearch Query DSL / SQL** — long-standing search QL with knn bolted on.  
- **MongoDB query language + Atlas Vector Search** — MQL filters + vector stage in aggregation.

## G. Takeaways for this research

1. **2026 is the year SQL-shaped vector search went mainstream** (TopK SQL, SQL Server iterative filtering, Neo4j SEARCH, Redis FT.HYBRID) — still **not one standard**.  
2. Academic energy is in **NL query planning trees**, complementary to a **declarative RQL IR**.  
3. Best near-term path: middleware IR (this proposal’s RQL) + adapters, informed by TopK/VelesQL syntax experiments and PlanRAG-style cost models.
