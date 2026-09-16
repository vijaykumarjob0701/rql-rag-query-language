# 01 — Landscape: Vector DB Query Interfaces (as of 2026-09-16)

Vector databases do **not** share one query language. They cluster into five interface families:

1. **JSON / REST / gRPC filter DSLs** — Pinecone, Qdrant, Chroma, Turbopuffer, Astra Data API  
2. **GraphQL search operators** — Weaviate  
3. **Expression / boolean filter strings** — Milvus (`expr`), some Cassandra/Astra CQL paths  
4. **SQL or SQL-like dialects** — pgvector, ClickHouse, DuckDB VSS, LanceDB (+ DuckDB), SQL Server, TopK SQL, VelesQL, QQL  
5. **Domain languages** — Redis `FT.*`, Elasticsearch/OpenSearch DSL, Vespa YQL, Neo4j Cypher `SEARCH`

Below: concrete patterns for **vector similarity + metadata filters** (+ hybrid where available).

---

## 1. Pinecone — JSON metadata filter + query/search API

**Interface:** REST/gRPC SDK; MongoDB-style operators (`$eq`, `$in`, `$and`, …).  
**Hybrid:** dense + sparse / integrated embedding search; text-match filter operators on schema-enabled indexes (`$match_phrase`, `$match_all`, `$match_any`).

```python
index.query(
    vector=query_vec,
    top_k=3,
    filter={"category": {"$eq": "digestive system"}},
    include_metadata=True,
)
```

```json
{
  "query": {
    "inputs": {"text": "Disease prevention"},
    "top_k": 3,
    "filter": {
      "$and": [
        {"body": {"$match_all": "federal reserve"}},
        {"category": {"$eq": "finance"}},
        {"year": {"$gte": 2024}}
      ]
    }
  }
}
```

Docs: https://docs.pinecone.io/guides/search/filter-by-metadata

---

## 2. Weaviate — GraphQL + client query builders

**Interface:** GraphQL `Get { Class(nearVector|nearText|bm25|hybrid, where) }`; Python v4 filters.  
**Hybrid:** native `hybrid` with `alpha`, `fusionType` (`rankedFusion` | `relativeScoreFusion`).

```graphql
{
  Get {
    Article(
      hybrid: { query: "how to fish", alpha: 0.5 }
      where: { path: ["wordCount"], operator: LessThan, valueInt: 1000 }
      limit: 5
    ) {
      title
      summary
      _additional { score }
    }
  }
}
```

Docs: https://docs.weaviate.io/weaviate/api/graphql/search-operators · https://docs.weaviate.io/weaviate/search/filters

---

## 3. Qdrant — Filter DSL + unified Query API

**Interface:** REST/gRPC; `Filter` with `must` / `should` / `must_not`; `query_points` with `prefetch` + fusion (`rrf`, `dbsf`).  
**No first-class SQL** in-product; community **QQL** wraps SQL-like statements over the Python client.

```python
client.query_points(
    collection_name="docs",
    prefetch=[
        models.Prefetch(query=sparse_vec, using="sparse", limit=20),
        models.Prefetch(query=dense_vec, using="dense", limit=20),
    ],
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    query_filter=models.Filter(
        must=[models.FieldCondition(key="tenant", match=models.MatchValue(value="acme"))]
    ),
)
```

Docs: https://qdrant.tech/documentation/concepts/filtering/ · https://api.qdrant.tech/  
QQL: https://github.com/pavanjava/qql

---

## 4. Milvus / Zilliz — `expr` boolean expressions + `hybrid_search`

**Interface:** SDK/`expr` strings (e.g. `category == "tech" && year > 2020`); `AnnSearchRequest` list + `RRFRanker` / weighted ranker.

```python
from pymilvus import AnnSearchRequest, RRFRanker
req1 = AnnSearchRequest(data=[dense], anns_field="dense", param={"metric_type": "IP"}, limit=10,
                        expr='category == "tech"')
req2 = AnnSearchRequest(data=[sparse], anns_field="sparse", param={"metric_type": "IP"}, limit=10,
                        expr='category == "tech"')
client.hybrid_search(collection_name="col", reqs=[req1, req2], ranker=RRFRanker(k=60), limit=10)
```

Docs: https://milvus.io/docs · https://milvus.io/docs/rrf-ranker.md

---

## 5. Chroma — Python `query` / `where` / `where_document`

**Interface:** Embedded/client API (NumPy-like), not a textual QL.

```python
collection.query(
    query_embeddings=[emb],
    n_results=5,
    where={"source": "handbook"},
    where_document={"$contains": "vacation policy"},
)
```

Docs: https://docs.trychroma.com/docs/querying-collections/query-and-get

---

## 6. pgvector (PostgreSQL) — true SQL

**Interface:** SQL operators `<->` (L2), `<=>` (cosine), `<#>` (inner product); combine with `tsvector` / BM25 extensions for hybrid via CTEs + RRF in SQL.

```sql
SELECT id, content,
  COALESCE(1.0/(60 + sem.rank), 0) + COALESCE(1.0/(60 + lex.rank), 0) AS rrf
FROM ... -- semantic CTE + full-text CTE FULL OUTER JOIN
ORDER BY rrf DESC LIMIT 20;
```

Docs: https://github.com/pgvector/pgvector · Supabase hybrid: https://supabase.com/docs/guides/ai/hybrid-search

---

## 7. Redis — RediSearch / `FT.SEARCH` + `FT.HYBRID` (8.4+)

**Interface:** Redis command dialect (not SQL). Vector KNN in query string; `FT.HYBRID` fuses `SEARCH` + `VSIM` with RRF or LINEAR.

```
FT.SEARCH idx "(*)=>[KNN 10 @embedding $vec AS score]" PARAMS 2 vec <blob> SORTBY score DIALECT 2

FT.HYBRID products-idx
  SEARCH "laptop"
  VSIM @description_vector $query_vec KNN 2 K 10
  COMBINE RRF 4 WINDOW 50 CONSTANT 60
  PARAMS 2 query_vec <blob>
```

Docs: https://redis.io/docs/latest/commands/ft.hybrid/ · https://redis.io/docs/latest/develop/ai/search-and-query/vectors/

---

## 8. Elasticsearch / OpenSearch — Query DSL + retrievers

**Interface:** JSON Query DSL; ES 8.x+ `retriever` API with nested `standard` + `knn` under `rrf`.

```json
{
  "retriever": {
    "rrf": {
      "retrievers": [
        {"standard": {"query": {"match": {"text": "shoes"}}}},
        {"knn": {"field": "vector", "query_vector": [1.25, 2, 3.5], "k": 50, "num_candidates": 100}}
      ],
      "rank_constant": 20,
      "rank_window_size": 50
    }
  }
}
```

Docs: https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rrf.html · OpenSearch RRF: https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/

---

## 9. LanceDB — Python/JS builder + SQL via DuckDB/Lance

**Interface:** `table.search(vec).where("price > 20").limit(10)`; SQL UDF-style `lance_vector_search(...)` in DuckDB integration.

Docs: https://docs.lancedb.com/search/filtering · https://lance.org/integrations/duckdb/sql/

---

## 10. Vespa — YQL (Yahoo Query Language)

**Interface:** SQL-like YQL with `nearestNeighbor`, ranking profiles, filters in one query POST.

```
select * from sources * where {targetHits:10}nearestNeighbor(embedding, q) and category contains "tech"
```

Docs: https://docs.vespa.ai/en/querying.html

---

## 11. Turbopuffer — JSON `rank_by` + tuple filters + multi_query RRF

**Interface:** REST; filters as nested arrays (`["And", [...]]`); `rank_by: ["vector","ANN", vec]` or BM25; hybrid via `multi_query` + `rerank_by: ["RRF"]`.

```python
ns.query(
    rank_by=("vector", "ANN", query_vec),
    filters=("And", (("public", "Eq", True), ("timestamp", "Gte", dt))),
    limit=10,
)
ns.multi_query(
    queries=[
        {"rank_by": ("vector", "ANN", qv), "limit": 10},
        {"rank_by": ("content", "BM25", "quick fox"), "limit": 10},
    ],
    rerank_by=("RRF",),
)
```

Docs: https://turbopuffer.com/docs/query

---

## 12. Astra DB / Cassandra — Data API + CQL ANN

**Interface:** Document Data API (JSON filters + vector sort) and CQL `ORDER BY ... ANN OF` / vector search APIs depending on deployment.

Docs: https://docs.datastax.com/en/astra-db-serverless/databases/vector-search.html

---

## 13. Neo4j — Cypher `SEARCH` (2026.01+)

**Interface:** Cypher 25 `MATCH ... SEARCH node IN (VECTOR INDEX ... FOR $vec [WHERE ...] LIMIT k) SCORE AS score`. Prefer **in-index** `WHERE` inside `SEARCH` over post-filters.

```cypher
MATCH (movie:Movie)
  SEARCH movie IN (
    VECTOR INDEX moviePlots
    FOR $queryEmbedding
    WHERE movie.releaseDate > date('1990')
    LIMIT 4
  ) SCORE AS similarityScore
RETURN movie.title, similarityScore
```

Docs: https://neo4j.com/docs/cypher-manual/current/clauses/search/

---

## 14. ClickHouse — SQL distance functions + ANN indexes

```sql
SELECT id, cosineDistance(embedding, {qv:Array(Float32)}) AS dist
FROM docs
WHERE tenant = 'acme'
ORDER BY dist ASC
LIMIT 10;
```

Docs: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/annindexes (product docs evolve; confirm current ANN index names).

---

## 15. DuckDB VSS — SQL extension

```sql
SELECT * FROM docs
ORDER BY array_cosine_similarity(embedding, ?) DESC
LIMIT 10;
-- + MATCH_BM25 / FTS extension for hybrid in SQL
```

Docs: https://duckdb.org/docs/stable/extensions/vss.html

---

## 16. SQL Server 2025 / Azure SQL — `VECTOR_SEARCH`

```sql
SELECT TOP (5) WITH APPROXIMATE t.id, t.title, r.distance
FROM VECTOR_SEARCH(
        TABLE = dbo.articles AS t,
        COLUMN = content_vector,
        SIMILAR_TO = @qv,
        METRIC = 'cosine'
    ) AS r
WHERE t.category = 'Technology' AND t.published = 1  -- iterative filtering on latest indexes
ORDER BY r.distance;
```

Docs: https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-search-transact-sql?view=sql-server-ver17

---

## 17. Dedicated / emerging vector SQL dialects

| Name | Status | Notes |
|------|--------|-------|
| **TopK SQL** | Product (Jun 2026) | Postgres wire protocol; `semantic_similarity`, `bm25_score`, `vector_distance`, hybrid in one SELECT | https://www.topk.io/blog/20260614-topk-sql |
| **VelesQL** | OSS (VelesDB) | `NEAR` / `SPARSE_NEAR` / `NEAR_FUSED`, `USING FUSION`, MATCH graph | https://github.com/cyberlife-coder/VelesDB |
| **QQL** | OSS wrapper | SQL-like over Qdrant client | https://github.com/pavanjava/qql |
| **O’Reilly VQL** | Hypothetical (book Apr 2026) | Community proposal, not an implementation | https://www.oreilly.com/library/view/vector-databases/9781098177584/ch09.html |
| **ProximaDB SQL** | Early OSS | pgvector-compatible ops + GRAPH_QUERY / DOCUMENT_QUERY | https://github.com/anvai-labs/proximaDB |

---

## Comparison cheat sheet

| System | Primary QL shape | Metadata filter | Hybrid BM25+vector | Joins / multi-hop in-engine |
|--------|------------------|-----------------|--------------------|-----------------------------|
| Pinecone | JSON | Yes (`$…`) | Sparse/dense + text-match | Limited |
| Weaviate | GraphQL | `where` | Native hybrid | Cross-refs (discouraged at scale) |
| Qdrant | JSON Filter + Query | Yes | Prefetch + RRF/DBSF | Payload only |
| Milvus | `expr` + SDK | Yes | `hybrid_search` | Limited |
| Chroma | Python kwargs | `where` | App-side / evolving | No |
| pgvector | SQL | SQL WHERE | SQL CTE/RRF | Full SQL |
| Redis | FT commands | Query syntax | `FT.HYBRID` | Aggregations via FT |
| ES/OS | JSON DSL | Rich | Retriever RRF / pipelines | Limited joins |
| Turbopuffer | JSON rank_by | Tuple filters | multi_query RRF | Aggregations |
| Neo4j | Cypher SEARCH | In-index WHERE | App / hybrid patterns | **Graph hops** |
| TopK SQL | SQL dialect | WHERE | In-SELECT scores | Product-dependent |
| Vespa | YQL | Yes | Ranking profiles | Document model |

**Takeaway:** Combining vector similarity + metadata is **universally supported**; a **portable declarative language** for full RAG plans is **not**.
