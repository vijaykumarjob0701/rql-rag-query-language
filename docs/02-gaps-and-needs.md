# 02 — Gaps and Needs vs Traditional Query Languages

## What SQL / Redis / MongoDB give you that vector RAG mostly doesn’t

| Capability | Postgres SQL | Redis commands | MongoDB QL | Typical vector DB / RAG stack |
|------------|--------------|----------------|------------|-------------------------------|
| Standard language | ANSI-ish SQL | Documented command set | BSON query docs | **No cross-vendor standard** |
| Declarative filters | WHERE | Query syntax | Filter docs | Vendor JSON/`expr`/GraphQL — **incompatible** |
| Joins | First-class | Limited (app) | `$lookup` | Usually **none** across chunks/collections |
| Aggregations | GROUP BY, window | FT.AGGREGATE | Aggregation pipeline | Spotty (Turbopuffer, ES, Redis, SQL engines) |
| Query plans / EXPLAIN | Mature cost-based | INTROSPECT/PROFILE | explain | Rarely exposes ANN+filter cost model |
| Transactions | ACID | MULTI/Lua | Multi-doc (limited) | Often eventual; RAG rarely transactional |
| Reproducible scripts | `.sql` files | `.redis` scripts | mongosh | Python notebooks + SDK drift |
| Hybrid ranking | DIY SQL | `FT.HYBRID` | App | **Each vendor reinvents** RRF/alpha |
| Multi-step procedures | CTEs, procedures | Lua | Aggregation stages | **App agents / LangGraph** |

---

## Gap 1 — No standard query language

- Pinecone `$and` ≠ Qdrant `must` ≠ Milvus `expr` ≠ Weaviate `where` ≠ Turbopuffer `["And",…]`.
- Portability cost falls on frameworks (LangChain VectorStore abstractions leak; filters are the sharp edge).
- Hiring/docs: engineers learn N dialects; eval suites can’t share golden queries.

## Gap 2 — Vendor-specific filter semantics & pushdown

- **Pre-filter vs post-filter vs iterative filter** changes recall and latency dramatically (Qdrant ACORN, SQL Server iterative filtering, Neo4j in-index `WHERE` vs MATCH post-filter).
- Same logical predicate can silently return **empty** under post-filter + small `top_k` (classic RAG bug).
- Geo, nested arrays, nulls, and full-text-as-filter operators differ; no shared type system for metadata.

## Gap 3 — Limited joins / aggregations across chunks

RAG data is usually **denormalized chunks** (`doc_id`, `chunk_ix`, `text`, `embedding`, tags). Needs that hurt:

- “All chunks of the parent docs that matched” (parent-child / late chunking).
- Join chunk hits → entity table → related docs (GraphRAG-lite without a graph DB).
- Aggregate evidence per document, section, or tenant before generation.

SQL engines with vectors (pgvector, ClickHouse, DuckDB, SQL Server) handle this better; pure vector DBs force application joins.

## Gap 4 — Hard to express complex retrieval plans

Modern RAG is a **pipeline**, not a single kNN:

1. Query rewrite / multi-query  
2. Dense ANN ± sparse BM25  
3. Metadata ACL filters  
4. Fusion (RRF / linear / DBSF)  
5. Diversify / MMR  
6. Cross-encoder rerank  
7. Multi-hop / tool calls / graph traversal  

Today this is **imperative Python**. There is no widely adopted declarative form for:

```
HYBRID(dense, bm25) FILTER acl → OVERFETCH 50 → RERANK ce → LIMIT 8
THEN HOP entity_links → ANN …
```

Academic “query planning for RAG” (PlanRAG, LogicRAG, RT-RAG, PruneRAG — 2025–2026) operates on **NL → reasoning trees**, not on a shared IR against vector stores.

## Gap 5 — Reproducibility & observability

- ANN is approximate: `ef`, `nprobe`, quantization, and filter strategy change results.
- Few systems return a portable **logical plan + physical params** artifact for audits.
- Golden-set regression needs frozen embeddings, index build IDs, and query text — rarely packaged together.

## Gap 6 — Optimization / planning

Relational optimizers reason about selectivity and indexes. Vector RAG needs joint optimization of:

- Filter selectivity × ANN recall  
- Hybrid candidate depths  
- Rerank budget (latency/tokens)  
- Multi-hop branching factor  

Most stacks pick constants (`top_k=8`, `alpha=0.5`) by folklore.

## Gap 7 — Framework “query languages” are incomplete

- **LangChain SelfQueryRetriever**: NL → metadata filter + query — helpful, not a full retrieval QL; backend-specific translators.
- **LlamaIndex** query engines / `QueryFusionRetriever`: composition in Python objects, not a textual standard.
- **GraphQL for Weaviate**: powerful but Weaviate-bound.
- **Cypher + vectors**: excellent for GraphRAG on Neo4j; not a general vector-DB standard.

---

## What teams actually need (requirements for a RAG QL)

1. **Portable filters** with explicit pushdown hints (`PUSHDOWN | POSTFILTER | ITERATIVE`).  
2. **First-class hybrid** (dense, sparse, BM25, multi-vector/ColBERT) + named fusion.  
3. **Stages**: overfetch, diversify, rerank, expand-parent, multi-query union.  
4. **Structured multi-hop**: sequential/parallel subqueries with bindings (CTE-like).  
5. **EXPLAIN / COST** for ANN+filter+rerank.  
6. **Compile targets**: at least pgvector, Qdrant, Weaviate, Pinecone, ES, Redis, Turbopuffer.  
7. **Eval hooks**: attach dataset IDs, embedding model IDs, expected metrics.

Without these, “another SQL skin over one vendor” only helps that vendor’s DX — it does not fix the RAG ecosystem gap.
