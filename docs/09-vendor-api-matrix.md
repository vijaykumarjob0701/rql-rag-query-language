# 09 — Vendor hybrid / filter / fusion API matrix (docs-only)

**Survey date:** 2026-09-16 (Europe/Dublin)  
**Method:** Official public docs via WebSearch + WebFetch / raw GitHub README. **No** live DB clusters, **no** credentials, **no** smoke calls.  
**Honesty:** Cells are **Established** only when the cited page states the capability. Ambiguous composition or undocumented EXPLAIN → **UNKNOWN**. Do not invent APIs.  
**Companion journal:** [`../journal/0020-vendor-hybrid-api-matrix.md`](../journal/0020-vendor-hybrid-api-matrix.md)  
**OKF bundle:** [`../knowledge/reads/vendor-api-matrix-2026-09/`](../knowledge/reads/vendor-api-matrix-2026-09/)

**Thesis citation label:** *Established adapter surface survey (docs-only, Sep 2026)*.

---

## Column legend

| Column | Meaning |
|--------|---------|
| Metadata filter DSL | How predicates are expressed |
| Filter+ANN composition | PRE / POST / in-graph / iterative / UNKNOWN (docs wording) |
| Hybrid / BM25+dense | Native hybrid or app-side only |
| RRF / weighted fusion | First-class fusion primitives |
| Multi-vector / late interaction | Named multi-vector, ColBERT/MaxSim, etc. |
| Query surface | REST/JSON, GraphQL, SQL, expr, FT commands |
| EXPLAIN / plan visibility | Documented plan/profile/explain |

---

## Master matrix

| Vendor | Metadata filter DSL | Filter+ANN composition | Hybrid / BM25+dense | RRF or weighted fusion | Multi-vector / late interaction | Query surface | EXPLAIN / plan |
|--------|---------------------|------------------------|---------------------|------------------------|---------------------------------|---------------|----------------|
| **Qdrant** | JSON `Filter`: `must` / `should` / `must_not` + field conditions ([filtering](https://qdrant.tech/documentation/concepts/filtering/)) | Filter on Query API; docs + PR describe **propagating filters to leaf/prefetch** to avoid post-filter merge ([hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/); [PR #4427](https://github.com/qdrant/qdrant/pull/4427)). Exact PRE vs in-graph algorithm: **UNKNOWN** without runtime | Prefetch dense+sparse then fuse ([hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/)); BM25 via sparse/BM25 models in tutorials | **`rrf`** (param `k` ≥1.16; **weights** ≥1.17) + **`dbsf`**; formula queries for custom score ([hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/)) | Multi-vector / ColBERT rescore via nested prefetch ([hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/); [multivectors tutorial](https://qdrant.tech/documentation/tutorials-search-engineering/using-multivector-representations/)) | REST/gRPC **Query API** JSON | **UNKNOWN** first-class EXPLAIN in reviewed docs |
| **Elasticsearch** | Query DSL / retriever `filter` ([RRF retriever](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrievers/rrf-retriever); [kNN](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/knn-search.html)) | **`knn.filter` applied during approximate kNN** so *k* matches survive (contrasts post-filter) ([kNN filtered](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/knn-search.html)) | Hybrid via **`rrf` retriever** (standard/BM25 + knn) or `query`+`knn` score sum with boosts ([hybrid search](https://www.elastic.co/docs/solutions/search/hybrid-search); [RRF](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrievers/rrf-retriever)) | **`retriever.rrf`**: `rank_constant` (default 60), `rank_window_size`; **per-retriever weights** (Stack ≥9.2) | Nested `dense_vector` for passage vectors; not ColBERT MaxSim-as-a-service in reviewed pages → late-interaction native: **UNKNOWN**/partial | REST JSON (`_search`, retrievers) | **Profile API** for search timing ([profile](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/search-profile)); kNN-specific plan tree: **UNKNOWN** |
| **OpenSearch** | Query DSL inside `hybrid.queries` + filters | Filter+k-NN composition details: **UNKNOWN** in RRF page alone (use k-NN + bool docs separately) | **`hybrid` query** + search pipeline ([hybrid](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/)) | **`score-ranker-processor` / RRF** (`rank_constant` default 60; weights sum to 1.0) **or** normalization processor (arithmetic/geometric/harmonic mean) ([RRF](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/)) | Multi-vector late interaction: **UNKNOWN** in reviewed hybrid/RRF pages | REST JSON + search pipelines | Hybrid **score explanation** processors / `explain` patterns documented on RRF page; full physical EXPLAIN: **UNKNOWN** |
| **Weaviate** | GraphQL `where` / client `filters` ([filters](https://docs.weaviate.io/weaviate/search/filters); [filtering concepts](https://docs.weaviate.io/weaviate/concepts/filtering)) | **Pre-filtering** (allow-list before/during HNSW); ACORN strategy default from v1.34 ([filtering concepts](https://docs.weaviate.io/weaviate/concepts/filtering)) | Native **`hybrid`**: BM25 + vector; `alpha`; `fusionType` `relativeScoreFusion` (default ≥v1.24) \| `rankedFusion` ([hybrid concepts](https://docs.weaviate.io/weaviate/concepts/search/hybrid-search)) | Rank-based fusion ≈ RRF-like (`rankedFusion`); score fusion (`relativeScoreFusion`); **not** Cormack-named RRF API | **Multi-vector / ColBERT** (≥v1.29) with MaxSim-style late interaction ([multi-vector tutorial](https://docs.weaviate.io/weaviate/tutorials/multi-vector-embeddings)) | GraphQL + gRPC/clients | **UNKNOWN** EXPLAIN in reviewed docs |
| **Milvus** | Boolean **`expr`** / `filter` alias on ANN requests ([hybrid_search API](https://milvus.io/api-reference/pymilvus/v2.6.x/MilvusClient/Vector/hybrid_search.md)) | API text: expr/filter **“applied before the ANN search”** → document as **PRE** (docs); engine internals **UNKNOWN** without runtime | **`hybrid_search`**: multiple `AnnSearchRequest` then ranker ([API](https://milvus.io/api-reference/pymilvus/v2.6.x/MilvusClient/Vector/hybrid_search.md); [multi-vector search](https://milvus.io/docs/v2.6.x/multi-vector-search.md)) | **`RRFRanker`** / **`WeightedRanker`** (docs + API) | Multiple vector fields / hybrid multi-path; ColBERT-native MaxSim field: **UNKNOWN** in reviewed API pages | SDK + REST JSON; `expr` strings | **UNKNOWN** EXPLAIN in reviewed pages (site fetch partially blocked) |
| **pgvector** | SQL `WHERE` ([README Filtering](https://github.com/pgvector/pgvector/blob/master/README.md)) | Approx indexes: filter **after** index scan (**POST**); **iterative index scans** (≥0.8.0) to recover recall; partial indexes / partitions optional ([README](https://github.com/pgvector/pgvector/blob/master/README.md)) | App-side: Postgres FTS (`tsvector`/`ts_rank`) + vector; example RRF in pgvector-python ([Hybrid Search](https://github.com/pgvector/pgvector/blob/master/README.md)) — **not** built-in BM25 | No first-class `RRF()` SQL; RRF example external | No first-class multi-vector MaxSim type in README | **SQL** | **PostgreSQL `EXPLAIN` / `EXPLAIN ANALYZE`** (engine-native) |
| **Pinecone** *(optional)* | Metadata filter JSON (`$eq`, `$in`, …) + text-match filters ([filter by metadata](https://docs.pinecone.io/guides/search/filter-by-metadata)) | Docs: metadata filtering **narrows candidate pool before ranking** ([hybrid overview](https://docs.pinecone.io/guides/search/hybrid-search)) | Dense+sparse single index; or client RRF of separate searches; text-match-then-dense ([hybrid](https://docs.pinecone.io/guides/search/hybrid-search)) | **Client-side RRF** documented; server-side dense+sparse combo via scaled vectors | Late interaction: **UNKNOWN** in reviewed pages | REST/JSON SDK | **UNKNOWN** |
| **Redis** *(optional)* | `FT.SEARCH` primary filter query before `KNN` ([vectors](https://redis.io/docs/latest/develop/ai/search-and-query/vectors/)) | Hybrid filter modes `BATCHES` / `ADHOC_BF` (auto or override) — neither pure PRE nor pure POST ([how filtering works](https://redis.io/docs/latest/develop/ai/search-and-query/vectors/)) | Keyword + vector in one `FT.SEARCH`; hybrid rank features evolve — verify version | First-class RRF in reviewed vector concepts page: **UNKNOWN** | Multi-vector late interaction: **UNKNOWN** | `FT.*` commands / query syntax | **UNKNOWN** / limited vs SQL EXPLAIN |

---

## Per-vendor source bookmarks (citable)

### Qdrant
- Filtering: https://qdrant.tech/documentation/concepts/filtering/
- Hybrid / multi-stage Query API: https://qdrant.tech/documentation/search/hybrid-queries/
- Multivectors / late interaction tutorial: https://qdrant.tech/documentation/tutorials-search-engineering/using-multivector-representations/
- Filter propagation PR (supporting note): https://github.com/qdrant/qdrant/pull/4427

### Elasticsearch
- kNN search + filtered kNN: https://www.elastic.co/guide/en/elasticsearch/reference/8.19/knn-search.html
- RRF retriever: https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrievers/rrf-retriever
- Hybrid search overview: https://www.elastic.co/docs/solutions/search/hybrid-search
- Profile API: https://www.elastic.co/docs/reference/elasticsearch/rest-apis/search-profile

### OpenSearch
- Hybrid search: https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/
- RRF: https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/

### Weaviate
- Hybrid search concepts: https://docs.weaviate.io/weaviate/concepts/search/hybrid-search
- Filtering concepts (pre-filter): https://docs.weaviate.io/weaviate/concepts/filtering
- Multi-vector embeddings: https://docs.weaviate.io/weaviate/tutorials/multi-vector-embeddings
- GraphQL search operators (repo): https://github.com/weaviate/docs/blob/main/docs/weaviate/api/graphql/search-operators.md

### Milvus
- `hybrid_search` API: https://milvus.io/api-reference/pymilvus/v2.6.x/MilvusClient/Vector/hybrid_search.md
- Multi-vector hybrid search guide: https://milvus.io/docs/v2.6.x/multi-vector-search.md
- Reranking overview: https://milvus.io/docs/reranking.md

### pgvector
- README (filtering, iterative scans, hybrid): https://github.com/pgvector/pgvector/blob/master/README.md
- RRF example (Python): https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py

### Pinecone / Redis (optional)
- Pinecone filter: https://docs.pinecone.io/guides/search/filter-by-metadata
- Pinecone hybrid: https://docs.pinecone.io/guides/search/hybrid-search
- Redis vectors: https://redis.io/docs/latest/develop/ai/search-and-query/vectors/

---

## Implications for RQL adapters (summary)

| RQL logical op | Portability note |
|----------------|------------------|
| `Filter` ∘ `Search_dense` | Map to vendor PRE (Weaviate/ES knn.filter/Milvus expr-before) vs POST+iterative (pgvector) vs hybrid BATCHES (Redis) vs Qdrant leaf-propagated filter — **capability negotiation required** |
| `Fuse_rrf` | Native: Qdrant `rrf`, ES `rrf` retriever, OpenSearch score-ranker, Milvus `RRFRanker`; Weaviate `rankedFusion` (related, not identical API); pgvector/Pinecone often **client shim** |
| `Fuse_linear` | Milvus `WeightedRanker`; Weaviate `relativeScoreFusion`+`alpha`; ES boosts / weighted RRF; Qdrant DBSF or formula — **not one shared semantics** |
| `Search_late` | Strong native: Qdrant multivector rescore, Weaviate multi-vector; else MUVERA/PLAID-style rewrite hypothesis |
| `Explain` | Only pgvector (SQL) and ES Profile / OS hybrid explain are clearly documented among core five — RQL EXPLAIN will often be **adapter-synthesized** |

Live smoke verification remains **HUMAN P1** (`experiments/protocols/03-adapter-smoke.md`).
