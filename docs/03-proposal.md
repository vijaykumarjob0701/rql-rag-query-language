# 03 — Proposal: RQL (Retrieval Query Language)

## Goals

1. **Declarative retrieval plans** for RAG: vector + lexical + metadata + fusion + rerank + multi-hop.  
2. **Backend-agnostic IR** that compiles to Pinecone/Qdrant/Weaviate/Milvus/pgvector/Redis/ES/Turbopuffer/Neo4j adapters.  
3. **Explicit filter strategy & ANN params** for reproducibility.  
4. **Planner** that can push filters, choose fusion depths, and budget rerankers.  
5. **Improve reliability first**, then latency, then accuracy (via better default plans + fewer silent empty results).

Non-goals (v1): full DDL standardization; replacing embedding model APIs; guaranteed identical recall across ANN implementations.

---

## Design choice: SQL extension vs DSL vs GraphQL

| Approach | Pros | Cons | Verdict for RQL |
|----------|------|------|-----------------|
| SQL extension | Familiar; works with BI; pgvector/TopK prove it | Awkward for multi-stage RAG & agents; joins tempt misuse of chunk tables | **Compile target & optional surface** |
| Custom DSL (RQL) | Stages/fusion/rerank are natural; CTE-like hops | New learning curve | **Primary language** |
| GraphQL | Nice for Weaviate-shaped schemas | Weak for ranking algebra & multi-backend | Adapter only |
| Cypher-like | Best for GraphRAG | Overfit to property graphs | Optional graph module |

**RQL** = SQL-inspired **retrieval DSL** with CTE-style multi-hop, compiling optionally *to* SQL dialects where rich engines exist.

---

## Grammar sketch (informative)

```ebnf
query          = [ with_list ] retrieve_stmt ;
with_list      = "WITH" cte ( "," cte )* ;
cte            = ident "AS" "(" retrieve_stmt ")" ;

retrieve_stmt  = "RETRIEVE" target
                 [ "EMBED" embed_spec ]
                 [ search_clause ]
                 [ "WHERE" bool_expr ]
                 [ "FILTER_MODE" ( "PUSHDOWN" | "ITERATIVE" | "POST" | "AUTO" ) ]
                 [ "FUSE" fuse_spec ]
                 [ "DIVERSIFY" diversify_spec ]
                 [ "RERANK" rerank_spec ]
                 [ "EXPAND" expand_spec ]
                 [ "ORDER BY" order_expr ]
                 [ "LIMIT" int ] [ "OFFSET" int ]
                 [ "OPTION" option_list ] ;

target         = ident [ "AS" ident ] ;   -- collection / table / namespace

embed_spec     = "MODEL" string [ "TEXT" ( string | param ) ] | "VECTOR" ( vector_lit | param ) ;

search_clause  = "SEARCH" search_part ( "AND" search_part | "OR" search_part )* ;
search_part    = dense_search | sparse_search | bm25_search | multi_vec_search ;

dense_search   = "DENSE" [ "ON" field ] [ "METRIC" metric ] [ "CANDIDATES" int ] ;
sparse_search  = "SPARSE" [ "ON" field ] [ "CANDIDATES" int ] ;
bm25_search    = "BM25" [ "ON" fields ] "QUERY" ( string | param ) [ "CANDIDATES" int ] ;
multi_vec_search = "COLBERT" [ "ON" field ] [ "CANDIDATES" int ] ;

fuse_spec      = ( "RRF" [ "K" number ] [ "WEIGHTS" num_list ]
                 | "LINEAR" "WEIGHTS" num_list
                 | "DBSF"
                 | "EXPR" score_expr ) ;

diversify_spec = "MMR" [ "LAMBDA" number ] | "PER" field "MAX" int ;
rerank_spec    = "MODEL" string [ "TOP" int ] ;
expand_spec    = "PARENT" field | "WINDOW" int "AROUND" field ;

bool_expr      = ... ;  -- AND/OR/NOT, comparisons, IN, CONTAINS, MATCH_PHRASE, ACL helpers
metric         = "cosine" | "dot" | "l2" | "ip" ;
```

---

## Example patterns (see also `/examples`)

### A. Classic RAG: dense + metadata ACL

```sql
RETRIEVE chunks
  EMBED MODEL 'text-embedding-3-large' TEXT $question
  SEARCH DENSE ON embedding METRIC cosine CANDIDATES 50
  WHERE tenant = $tenant AND acl_allows($user)
  FILTER_MODE AUTO
  LIMIT 8
  OPTION ef_search = 64;
```

### B. Hybrid BM25 + dense with RRF

```sql
RETRIEVE chunks
  EMBED MODEL 'text-embedding-3-large' TEXT $question
  SEARCH
    DENSE ON embedding CANDIDATES 40
    AND BM25 ON content QUERY $question CANDIDATES 40
  WHERE status = 'published' AND lang = 'en'
  FUSE RRF K 60
  RERANK MODEL 'bge-reranker-v2-m3' TOP 8
  LIMIT 8;
```

### C. Multi-query union

```sql
WITH
  q1 AS (
    RETRIEVE chunks EMBED TEXT $q_primary SEARCH DENSE CANDIDATES 20 LIMIT 20
  ),
  q2 AS (
    RETRIEVE chunks EMBED TEXT $q_alt SEARCH DENSE CANDIDATES 20 LIMIT 20
  )
RETRIEVE UNION(q1, q2)
  FUSE RRF K 60
  LIMIT 10;
```

### D. Parent expansion after chunk hit

```sql
RETRIEVE chunks
  EMBED TEXT $question
  SEARCH DENSE CANDIDATES 30
  WHERE doc_type = 'policy'
  EXPAND PARENT doc_id
  RERANK MODEL 'ce-mini' TOP 5
  LIMIT 5;
```

### E. Multi-hop (entity → evidence)

```sql
WITH entities AS (
  RETRIEVE kg_nodes
    EMBED TEXT $question
    SEARCH DENSE ON name_emb CANDIDATES 10
    WHERE type IN ('Person','Org')
    LIMIT 5
)
RETRIEVE chunks
  EMBED TEXT $question
  SEARCH DENSE CANDIDATES 40
  WHERE entity_id IN (SELECT id FROM entities)
  FILTER_MODE PUSHDOWN
  LIMIT 12;
```

### F. Graph hop (compiles to Neo4j Cypher SEARCH + MATCH when backend supports)

```sql
RETRIEVE Movie
  SEARCH DENSE ON embedding CANDIDATES 8
  WHERE release_year >= 1990
  THEN TRAVERSE ACTED_IN → Person LIMIT 20;
```

---

## Compilation to backends

```
RQL text → Parse AST → Normalize (types, defaults)
        → Logical plan (Search, Filter, Fuse, Rerank, Expand, Hop)
        → Planner (pushdown, depths, backend caps)
        → Physical plan per adapter
```

| Logical op | Qdrant | Pinecone | Weaviate | pgvector | Redis | ES | Turbopuffer | Neo4j |
|------------|--------|----------|----------|----------|-------|-----|-------------|-------|
| DENSE | query/prefetch | query/search | nearVector | ORDER BY dist | VSIM/KNN | knn | rank_by ANN | SEARCH VECTOR INDEX |
| BM25 | sparse/payload | sparse/text | bm25/hybrid | tsvector/pg_search | SEARCH | match | BM25 | full-text indexes |
| FUSE RRF | FusionQuery | app or sparse hybrid | hybrid fusionType | SQL CTE | FT.HYBRID | retriever.rrf | multi_query RRF | app |
| Filter PUSHDOWN | Filter + ACORN | metadata filter | where | WHERE | FILTER | filter | filters | WHERE in SEARCH |
| RERANK | app / inference | app | modules | app | app | inferencer | app | app |

Adapters emit **native** calls; unsupported ops fall back with warnings in `EXPLAIN`.

---

## Planner ideas

1. **Filter cardinality estimate** → choose PUSHDOWN vs overfetch+POST (avoid empty results).  
2. **Hybrid depth allocation** under latency SLO (e.g. 40/40 vs 100/20).  
3. **Rerank budget**: `min(candidates, latency_ms / cost_per_pair)`.  
4. **Namespace/tenant routing** before ANN.  
5. **Multi-hop scheduling**: parallel independent CTEs (cf. PlanRAG logical query trees, 2026).  
6. **EXPLAIN ANALYZE** fields: `candidates_scanned`, `filter_selectivity`, `fusion_method`, `rerank_n`, `backend`.

---

## Benefits (expected)

| Dimension | Mechanism | Caveat |
|-----------|-----------|--------|
| **Reliability** | Named plans, EXPLAIN, frozen options | Still need golden embeddings |
| **Speed** | Pushdown, server-side fusion, fewer round-trips | ANN approx ≠ exact |
| **Accuracy** | Default hybrid+rerank+parent-expand; multi-hop CTEs | Gains from better *plans*, not syntax magic |

## Risks

- **False portability:** same RQL, different recall across HNSW implementations.  
- **Spec bloat:** trying to encode every vendor quirk.  
- **Optimizer overclaim:** without stats, planner heuristics can hurt.  
- **Security:** ACL helpers must compile to enforceable server filters, not client-only.  
- **Adoption:** frameworks may ignore a standard unless adapters ship early.

## Feasibility verdict

**Feasible now** as an open IR + adapters (like Substrait for analytics, or Prisma for ORMs). Highest leverage: standardize **filters + hybrid fusion + multi-stage plans**, compile to existing engines, integrate with LangChain/LlamaIndex as a retriever backend. Full ANSI-style standardization can follow once 2–3 major vendors implement a common subset (or a popular middleware wins).
