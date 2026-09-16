# 0020 — Vendor hybrid / filter / fusion API matrix (docs-only)

**Date:** 2026-09-16 ~23:50 IST (Europe/Dublin)  
**Type:** Established adapter surface survey (docs-only)  
**Status:** Matrix v1 frozen for thesis citation; **no** live cluster verification  
**Artifacts:** [`../docs/09-vendor-api-matrix.md`](../docs/09-vendor-api-matrix.md) · OKF [`../knowledge/reads/vendor-api-matrix-2026-09/`](../knowledge/reads/vendor-api-matrix-2026-09/)  
**Prior seed:** FANNS FilterExec taxonomy (journal 0019)

---

## Context

After grounding FilterExec modes in Lin et al. FANNS (0019) and fusion/late-interaction literature (0011–0018), RQL still needed a **docs-only map of what each major vector store actually exposes** for filters, hybrid/BM25+dense, RRF/weighted fusion, multi-vector, query surface, and EXPLAIN — so compilation/adapters (thesis §07) cite **Established** surfaces rather than folklore.

## Question asked

For Qdrant, Elasticsearch/OpenSearch, Weaviate, Milvus, and pgvector (plus optional Pinecone/Redis), what do **official public docs** state about: metadata filter DSL; filter+ANN composition (PRE/POST/UNKNOWN); hybrid/BM25+dense; RRF or weighted fusion; multi-vector/late interaction; query language surface; EXPLAIN/plan visibility?

## Where we looked

WebSearch + WebFetch / `curl` of official docs only (no credentials, no DB calls):

| Vendor | Primary URLs fetched or raw-read |
|--------|----------------------------------|
| Qdrant | https://qdrant.tech/documentation/concepts/filtering/ · https://qdrant.tech/documentation/search/hybrid-queries/ |
| Elasticsearch | https://www.elastic.co/guide/en/elasticsearch/reference/8.19/knn-search.html · https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrievers/rrf-retriever · profile API docs |
| OpenSearch | https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/ · hybrid index page |
| Weaviate | https://docs.weaviate.io/weaviate/concepts/search/hybrid-search · https://docs.weaviate.io/weaviate/concepts/filtering · multi-vector tutorial |
| Milvus | https://milvus.io/api-reference/pymilvus/v2.6.x/MilvusClient/Vector/hybrid_search.md (HTML docs often 403 to fetchers) |
| pgvector | https://raw.githubusercontent.com/pgvector/pgvector/master/README.md (Filtering, Iterative Index Scans, Hybrid Search) |
| Pinecone / Redis | https://docs.pinecone.io/guides/search/hybrid-search · https://docs.pinecone.io/guides/search/filter-by-metadata · https://redis.io/docs/latest/develop/ai/search-and-query/vectors/ |

## What we established (docs wording)

1. **Filter+ANN is not one mode across vendors:** Weaviate documents **pre-filtering**; Elasticsearch documents **`knn.filter` during approx kNN** (vs post-filter pitfalls); pgvector documents **post-filter on approx indexes** + **iterative scans** (≥0.8.0); Milvus API text says expr/filter **before ANN**; Redis documents hybrid **BATCHES / ADHOC_BF**; Qdrant documents Query filters and leaf-propagation to avoid post-filter merge (algorithmic PRE vs in-graph still **UNKNOWN** without runtime).
2. **RRF is widely but inconsistently native:** Qdrant `rrf` (+ weighted ≥1.17), ES `retriever.rrf`, OpenSearch score-ranker RRF, Milvus `RRFRanker`; Weaviate `rankedFusion` is rank-based fusion (related); pgvector/Pinecone often **client RRF**.
3. **Weighted / score fusion differs:** Milvus `WeightedRanker`; Weaviate `relativeScoreFusion`+`alpha`; Qdrant `dbsf` / formula; ES boosts / weighted RRF — **not interchangeable semantics**.
4. **Late interaction:** Qdrant multivector rescore and Weaviate multi-vector/ColBERT are documented; others **UNKNOWN** or nested-vector only.
5. **EXPLAIN:** PostgreSQL `EXPLAIN` (pgvector) and ES Profile / OpenSearch hybrid score explanation are the clear docs hits; others **UNKNOWN** → RQL EXPLAIN often adapter-synthesized.

## Gaps / UNKNOWN (do not invent)

- Exact Qdrant HNSW filter algorithm class (allow-list vs ACORN-like) beyond “propagate to leaves.”
- OpenSearch filter+k-NN composition without consulting separate k-NN pages.
- Milvus HTML guide pages intermittently blocked to automated fetchers — API reference used; live smoke still needed.
- Whether Pinecone/Redis ship first-class server RRF in all product tiers (docs emphasize client RRF or keyword∩vector patterns).
- No vendor claimed identical recall under portable plans.

## Implications for RQL adapters

- Capability negotiation must encode **FilterExec mode offered by backend** (PRE / POST+iterative / hybrid-batches / leaf-propagated / UNKNOWN).
- `Fuse_rrf` compiles to native ops where present, else **explicit client shim** (marked expensive; ACL-unsafe if scores leave trust boundary).
- `Fuse_linear` needs per-vendor score-normalization story (Weaviate relativeScoreFusion ≠ Milvus WeightedRanker ≠ Bruch TM2C2).
- `Search_late` prefers Qdrant/Weaviate native paths; else ColBERT→PLAID→MUVERA rewrite ladder (hypothesis packaging).
- Thesis §07 should cite this matrix as **Established adapter surface survey (docs-only, Sep 2026)**; Hypothesis: RQL LogicalPlan compiles through these shims.

## Human follow-up

**P1:** Live adapter smoke per `experiments/protocols/03-adapter-smoke.md` — Vijay runs against real/local clusters; agents must not fake results or use production credentials in-repo.

## Next seed (suggested)

1. Freeze **LogicalPlan / PhysicalPlan JSON Schema** (operators, capability flags mirroring this matrix).  
2. Deeper **Substrait / Apache Calcite** read for IR adjacency.  
3. Or first **skeleton adapter** (e.g. pgvector SQL + Qdrant Query JSON) emitting plans only (no live calls in CI).

## Anti-overclaim

Docs ≠ measured recall/latency. Matrix is a **surface survey**, not a bake-off. No fabricated API features.
