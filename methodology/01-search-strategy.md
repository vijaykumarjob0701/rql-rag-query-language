# 01 — Search Strategy (Brainstorm)

**Date:** 2026-09-16 (Europe/Dublin)  
**Inputs:** Adjacent angles in [`../docs/05-brainstorm-adjacent.md`](../docs/05-brainstorm-adjacent.md); existing provisional cites in [`../docs/06-deep-literature.md`](../docs/06-deep-literature.md).  
**Constraint:** This doc defines *how and where to search*. It does not add new literature claims.

---

## WHERE to search

Primary academic surfaces:

| Surface | Why | How to use |
|---------|-----|------------|
| **arXiv** | Fastest primary PDFs (cs.DB, cs.IR, cs.LG, cs.AI) | `abs` → `pdf`; cite-chase via References; category filters |
| **Semantic Scholar** | Citation graph, “influential citations”, PDF links | Seed paper → citing / cited; sort by citation influence |
| **OpenReview** | ICLR/NeurIPS/ICML reviews and rebuttals | Catch critiques of filtered-ANN / retrieval claims |
| **ACL Anthology** | IR/NLP retrieval (ColBERT lineage, HyDE-adjacent, RAG eval) | Venue + year facets; PDF always |
| **DB proceedings** | VLDB, SIGMOD, SIGIR, CIKM, WWW, ICDE | Definitive filtered-ANN / hybrid / join papers |
| **Google Scholar** | Broad recall + “Cited by” | Use after a seed; watch duplicates / versions |
| **Google web** | Eng blogs, slides, standards | `filetype:pdf`, `site:`, quoted operator names |
| **GitHub topics** | Implementations behind papers | topics: `vector-search`, `hnsw`, `ann-benchmarks`, `colbert` |
| **Vendor eng blogs** | Pinecone, Qdrant, Weaviate, Milvus, Redis, Elastic, Neo4j, Vespa | Physical semantics / filter pushdown reality checks — not standards |
| **Standards bodies** | LOC CQL/SRU; ISO SQL/MM; MPEG-7 MPQF; Substrait | Existence proofs for portable IR / plan IR |

Secondary / careful:

- USENIX, MSDN/Azure, AWS architecture blogs (for production filter+ANN behavior)
- Survey arXiv numbers already logged in docs/06 — re-enter via cite-chasing, not re-dumping

---

## WHAT to search — query families

Map each family to angles in docs/05. Prefer **operator / planner vocabulary** over product names.

### Family A — Classical IR algebras
- `#combine` `#weight` Indri Galago operator algebra  
- rank fusion RRF CombSUM CombMNZ  
- CQL SRU “context set” library query language  

### Family B — Spatial / multimedia analogy
- PostGIS kNN `<->` GiST “Index Cond” recheck  
- SQL/MM MPEG-7 MPQF QueryByMedia  

### Family C — Approximate / budgeted query
- BlinkDB “ERROR WITHIN” approximate query processing  
- recall target latency budget ANN  

### Family D — Planner / portable plans
- Cascades Volcano Calcite traits cost factory  
- BigDAWG polystore CAST shim island  
- Substrait plan IR (not SQL text)  

### Family E — Filtered ANN physical algebra
- filtered ANN pre-filter post-filter iterative  
- predicate subgraph ACORN DiskANN label filter  
- FANNS survey selectivity hybrid query  

### Family F — Late interaction & hybrid leaves
- ColBERT PLAID MaxSim MUVERA FDE  
- hybrid dense sparse BM25 fusion learned  

### Family G — Graph + rewrite + joins
- GraphRAG Cypher SEARCH vector  
- HyDE query rewrite multi-query DMQR  
- vector similarity join threshold DiskJoin  

### Family H — Provenance / ACL
- ProvSQL why-provenance ranking  
- ACL filter pushdown mandatory predicate  

### Family I — Contradiction / negative space
- “filtered ANN fails” selectivity hard predicates  
- ANN nondeterminism reproducibility RAG  
- “no free lunch” hybrid index  

---

## Staged funnel

```
1. BROAD          product-agnostic operator / planner queries
        │
        ▼
2. ADJACENT       sideways fields from docs/05 (spatial, AQP, polystore…)
        │
        ▼
3. CITE-CHASING   References + “Cited by” from 1–2 seed PDFs
        │
        ▼
4. AUTHOR/VENUE   same authors’ follow-ons; SIGMOD/VLDB/SIGIR special sessions
        │
        ▼
5. CONTRADICTION  failure cases, rebuttals, OpenReview critiques
```

Rules:

- Do not stay in stage 1 after the first useful PDF.  
- Stage 3 usually yields the highest-quality 1–5% seeds.  
- Stage 5 prevents over-fitting the RQL thesis to flattering papers.

---

## Query mutation when a 5% insight appears

When Pass 4 of the read protocol yields a seed, **rewrite the query**, do not append keywords blindly.

| Seed type | Mutation pattern |
|-----------|------------------|
| New operator name (`#filreq`, `MaxSim`, `CAST`) | Quote the token; search token + field (“MaxSim ColBERT PLAID”) |
| Taxonomy row (PRE/POST/ITERATIVE) | Search each row label + “filtered ANN” separately |
| Venue/year surprise | Search venue proceedings TOC for that year + “vector” / “hybrid” |
| Negative result in a figure | Search “limitations of X” / OpenReview paper id |
| Citation in related work | Jump to that paper as new seed (cite-chase) |
| Capability claim (“equality labels only”) | Contradiction search: “arbitrary predicates” + same index family |

Keep a short mutation log (query → seed → next query). Prefer updating [`../NOTES-search-log.md`](../NOTES-search-log.md) with mutations over growing docs/06.

---

## Selection criteria (what to open as PDF)

Open a PDF if **any** hold:

1. Defines operators / algebra / plan nodes relevant to retrieval  
2. Compares physical strategies with figures/tables (not only prose)  
3. Names a portable IR / shim / EXPLAIN concept  
4. Contradicts a provisional docs/07 assumption  

Defer / skip:

- Pure vendor SDK tutorials without planner content  
- Embedding-model papers with no retrieval plan angle  
- Duplicate arXiv versions when a camera-ready is available  

---

## Output of search (before deep read)

For each candidate, record only:

- title, authors, year/venue (flag uncertainty)  
- URL (abs + pdf)  
- which query family / mutation produced it  
- why it might contain a seed (one sentence)  

Stop collecting when you have **2–3** candidates ready for the read protocol — not dozens.
