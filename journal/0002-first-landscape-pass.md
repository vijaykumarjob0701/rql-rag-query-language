# 0002 — First landscape pass (v1)

**When:** 2026-09-16 (Europe/Dublin)  
**Artifacts:** [`../docs/01-landscape.md`](../docs/01-landscape.md), [`../docs/02-gaps-and-needs.md`](../docs/02-gaps-and-needs.md), [`../docs/03-proposal.md`](../docs/03-proposal.md), [`../docs/04-related-work.md`](../docs/04-related-work.md)

---

## Context

Direct answer to 0001: survey what exists on the market and in emerging proposals, then sketch an RQL v1.

## Question asked

What query surfaces do vector DBs and RAG stacks expose *today*, and what gaps remain vs SQL/Redis/Mongo?

## Where we looked

**Direct / product-centric search** (not yet adjacent-field):

- Vendor docs: Pinecone, Qdrant, Weaviate, Milvus, Turbopuffer, pgvector, ClickHouse, DuckDB, SQL Server `VECTOR_SEARCH`, Redis `FT.SEARCH` / `FT.HYBRID`, Neo4j Cypher `SEARCH`, Vespa YQL  
- Emerging language names: TopK SQL, VelesQL, QQL, O’Reilly hypothetical VQL  
- App-layer composition: LangChain / LlamaIndex retrieval patterns  

Query style was mostly “vector database query language”, “metadata filter ANN”, “hybrid search RRF” — i.e. **straight at the product**.

## What we found (summary)

- **Partial yes:** many engines have *vendor-specific* DSLs (JSON filters, GraphQL operators, boolean strings, SQL extensions, Redis commands, YQL, Cypher SEARCH).  
- **No industry standard** analogous to ANSI SQL for retrieval plans.  
- Dominant practice remains SDK: `query(vector, top_k, filter)` + app-side hybrid/rerank.  
- Gaps: portable plans, inconsistent filter pushdown, weak multi-stage declarative structure, limited joins/aggregations over chunks, weak cost-based planning.

v1 proposal: SQL-inspired **RQL** DSL compiling to backend adapters ([`../docs/03-proposal.md`](../docs/03-proposal.md)).

## What we read

Mostly documentation pages and secondary descriptions — **not** a multimodal paper protocol. Adequate for landscape; insufficient for algebra genealogy.

## 1–5% seed

Portable **retrieval plans** matter more than another JSON filter skin. But v1 still framed the product as a textual SQL-like DSL first.

## Limits of direct search

| Limit | Consequence |
|-------|-------------|
| Product docs emphasize APIs, not algebras | Missed classical IR operator lineage |
| Little cite-chasing into DB/IR venues | Filtered-ANN physical taxonomy under-sampled |
| Abstract/blog level on “related work” | Risk of inventing syntax without stealing vocabulary |
| No figure/table protocol | Latency–recall / planner diagrams not used as seeds |

## Uncertainty

- Whether SQL familiarity is the right frontend vs plan-IR-first  
- Which gaps are language problems vs index/engine problems  

## Next questions

- What adjacent fields already solved pieces (IR QLs, spatial kNN+filter, polystores, AQP, Cascades)? → brainstorm + deep dive (0003)
