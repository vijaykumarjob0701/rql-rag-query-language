# References — URLs used in this research package

Research date: **2026-09-16**. Prefer primary product docs and dated 2024–2026 sources.

## Vector DB & search product docs

1. https://docs.pinecone.io/guides/search/filter-by-metadata  
2. https://docs.pinecone.io/reference/api/2025-10/data-plane/fetch_by_metadata  
3. https://docs.weaviate.io/weaviate/api/graphql/search-operators  
4. https://docs.weaviate.io/weaviate/search/filters  
5. https://docs.weaviate.io/weaviate/search/similarity  
6. https://docs.weaviate.io/weaviate/api/graphql/filters  
7. https://qdrant.tech/documentation/search/filtering/  
8. https://skills.qdrant.tech/api-reference/search/query-points.md  
9. https://milvus.io/api-reference/pymilvus/v2.6.x/MilvusClient/Vector/hybrid_search.md  
10. https://milvus.io/docs/v2.6.x/multi-vector-search.md  
11. https://milvus.io/docs/v2.6.x/rrf-ranker.md  
12. https://docs.trychroma.com/docs/querying-collections/query-and-get  
13. https://github.com/pgvector/pgvector  
14. https://supabase.com/docs/guides/ai/hybrid-search  
15. https://redis.io/docs/latest/commands/ft.hybrid/  
16. https://redis.io/docs/latest/develop/ai/search-and-query/vectors/  
17. https://redis.io/docs/latest/develop/whats-new/8-4/  
18. https://redis.io/blog/vector-indexes-in-redis/  
19. https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rrf.html  
20. https://www.elastic.co/guide/en/elasticsearch/reference/8.19/retriever.html  
21. https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/  
22. https://docs.lancedb.com/search/filtering  
23. https://docs.lancedb.com/tables  
24. https://lance.org/integrations/duckdb/sql/  
25. https://docs.vespa.ai/en/basics/querying.html.md  
26. https://turbopuffer.com/docs/query  
27. https://turbopuffer.com/docs/vector  
28. https://turbopuffer.com/docs/fts  
29. https://docs.datastax.com/en/astra-db-serverless/databases/vector-search.html  
30. https://neo4j.com/docs/cypher-manual/current/clauses/search/  
31. https://neo4j.com/blog/genai/vector-search-with-filters-in-neo4j-v2026-01-preview/  
32. https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-search-transact-sql?view=sql-server-ver17  
33. https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-distance-transact-sql?view=sql-server-ver17  
34. https://duckdb.org/docs/stable/extensions/vss.html  

## SQL-like / dedicated vector query languages

35. https://www.topk.io/blog/20260614-topk-sql  
36. https://github.com/topk-io/topk  
37. https://github.com/cyberlife-coder/VelesDB  
38. https://github.com/cyberlife-coder/VelesDB/blob/main/docs/VELESQL_SPEC.md  
39. https://github.com/pavanjava/qql  
40. https://github.com/anvai-labs/proximaDB  
41. https://www.oreilly.com/library/view/vector-databases/9781098177584/ch09.html  
42. https://www.oreilly.com/library/view/vector-databases/9781098177584/  

## Frameworks & RAG patterns

43. https://www.langchain.com/resources/langchain-vs-llamaindex  
44. https://dev.to/jamesli/rag-retrieval-performance-enhancement-practices-detailed-explanation-of-hybrid-retrieval-and-self-query-techniques-59ja  
45. https://developers.llamaindex.ai/  

## Academic (query planning / structured RAG)

46. https://arxiv.org/html/2607.00508 — PlanRAG logical query trees (2026)  
47. https://arxiv.org/html/2508.06105v1 — LogicRAG (2025)  
48. https://arxiv.org/html/2601.11255 — RT-RAG (2026)  
49. https://arxiv.org/pdf/2601.11024 — PruneRAG (2026)  

## Secondary / survey articles consulted

50. https://medium.com/data-science-collective/pinecone-vs-weaviate-vs-qdrant-vs-milvus-66d5bfbcc460  
51. https://markaicode.com/usecases/vector-database-for-semantic-search/  
52. https://www.instaclustr.com/education/vector-database/pgvector-hybrid-search-benefits-use-cases-and-quick-tutorial/  
53. https://learnbackend.com/guides/hybrid-search-postgres-bm25-pgvector/  
54. https://aimenta.ai/insights/apac-vector-database-extended-guide-vespa-lancedb-turbopuffer-2026  
55. https://tiger-data-docs.vercel.app/docs/build/examples/hybrid-search  

---

## Deep dive v2 — adjacent literature (added 2026-09-16)

### Filtered ANN / hybrid vector+predicate
56. https://arxiv.org/abs/2403.04871 — ACORN (Patel et al., 2024)  
57. https://harsha-simhadri.org/pubs/Filtered-DiskANN23.pdf — Filtered-DiskANN (Gollapudi et al., WWW 2023)  
58. https://github.com/microsoft/DiskANN — DiskANN / Filtered-DiskANN implementation  
59. https://arxiv.org/abs/2304.01926 — HQI / hybrid vector search in KGs (Mohoney et al., 2023)  
60. https://arxiv.org/abs/2308.15014 — CAPS partition index for filtered similarity (2023)  
61. https://arxiv.org/abs/2505.06501 — Survey of FANNS (Lin et al., 2025)  
62. https://arxiv.org/abs/2510.27141 — Compass general filtered search (2025)  
63. https://arxiv.org/abs/2507.11907 — SIEVE filtered vector search (2025)  
64. https://arxiv.org/abs/2602.17914 — Learning-based filtered-ANN query planning (2026)  
65. https://arxiv.org/abs/2606.19898 — Query-aware routing for FANNS (2026)  
66. https://www.microsoft.com/en-us/research/publication/vbase-unifying-online-vector-similarity-search-and-relational-queries-via-relaxed-monotonicity/ — VBASE (OSDI 2023)  
67. https://www.usenix.org/system/files/osdi23-zhang-qianxi_1.pdf — VBASE PDF  
68. https://github.com/microsoft/MSVBASE — MSVBASE code  
69. https://arxiv.org/abs/2507.21989 — Benchmarking FANNS on transformer embeddings (2025)  
70. https://arxiv.org/pdf/2508.16263 — Attribute filtering in ANN experimental study (2025)  

### Fusion / late interaction / rewriting
71. https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf — Reciprocal Rank Fusion (SIGIR 2009)  
72. https://arxiv.org/abs/2210.11934 — Bruch et al. fusion analysis (TOIS 2023; DOI 10.1145/3596512); multimodal journal 0016  
72b. https://arxiv.org/abs/2201.10582 — Chen et al. zero-shot hybrid / RRF vs linear interp (ECIR 2022; DOI 10.1007/978-3-030-99736-6_7); multimodal journal 0017
73. https://arxiv.org/abs/2004.12832 — ColBERT (2020)  
74. https://arxiv.org/abs/2205.09707 — PLAID late-interaction engine (2022)  
75. https://arxiv.org/abs/2405.19504 — MUVERA multi-vector via FDEs (2024)  
76. https://arxiv.org/abs/2212.10496 — HyDE (Gao et al., 2022)  
77. https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf — MMR (Carbonell & Goldstein, 1998)  
78. https://arxiv.org/abs/2411.13154 — DMQR-RAG multi-query rewriting (2024)  

### Classic IR languages & standards
79. http://lemurproject.org/lemur/IndriQueryLanguage.php — Indri query language  
80. https://sourceforge.net/p/lemur/wiki/Indri%20Query%20Language%20Reference/ — Indri QL reference  
81. https://galagosearch.org/retrieval.html — Galago retrieval / operator language  
82. https://www.loc.gov/standards/sru/cql/ — CQL Contextual Query Language  
83. https://www.loc.gov/standards/sru/ — SRU / CQL home  
84. https://lucene.apache.org/core/10_5_1/queryparser/org/apache/lucene/queryparser/classic/package-summary.html — Lucene QueryParser  
85. https://github.com/terrier-org/terrier-core/blob/5.x/doc/querylanguage.md — Terrier matchop language  

### Optimizers, federation, declarative compute
86. https://arxiv.org/abs/1802.10233 — Apache Calcite (2018)  
87. https://calcite.apache.org/ — Apache Calcite project  
88. https://sigmod.org/publications/sigmodRecord/1506/pdfs/04_vision_Duggan.pdf — BigDAWG polystore vision (2015)  
89. https://substrait.io/ — Substrait portable plan IR  
90. https://substrait.io/about/ — Substrait about / vision  
91. https://arxiv.org/abs/1203.5485 — BlinkDB (2012)  
92. https://arxiv.org/abs/1909.02976 — SystemDS (2019)  
93. https://arxiv.org/abs/1709.06416 — Weld (2017)  
94. https://arxiv.org/abs/1604.03607 — Lara key-value algebra (2016)  
95. https://arxiv.org/abs/1703.07342 — LaraDB (2017)  
96. https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-173.html — Dedalus (Alvaro et al.)  

### GraphRAG, joins, spatial/array/multimedia analogies
97. https://arxiv.org/abs/2408.08921 — GraphRAG survey (2024)  
98. https://arxiv.org/abs/2501.00309 — Retrieval-Augmented Generation with Graphs survey (2024/25)  
99. https://arxiv.org/abs/2508.18494 — DiskJoin (2025)  
100. https://arxiv.org/abs/2603.16360 — Fast approximate vector joins (2026)  
101. https://arxiv.org/abs/2512.09695 — Exqutor vector-augmented SQL optimizer (2025)  
102. https://postgis.net/docs/using_postgis_query.html — PostGIS spatial queries  
103. https://www.postgis.net/docs/manual-3.5/geometry_distance_knn.html — PostGIS `<->` kNN  
104. https://doc.rasdaman.org/04_ql-guide.html — Rasdaman rasql  
105. https://www.iso.org/standard/61195.html — MPEG-7 Part 12 Query Format (MPQF)  
106. https://arxiv.org/abs/2408.05109 — NL2SQL with LLMs survey (2024)  
