# RQL Deep Research — Search Log

**Research date:** 2026-09-16 (Europe/Dublin)  
**Method:** Read existing package → brainstorm 22 adjacent angles → WebSearch batches → curl arXiv abs / WebFetch PDFs → synthesize docs 05–07.

## Status
- [x] Read existing package (README, docs/01–04, references, examples)
- [x] Brainstorm → `docs/05-brainstorm-adjacent.md`
- [x] Searches (this log)
- [x] Deep literature → `docs/06-deep-literature.md` (28 sources)
- [x] Evolved idea → `docs/07-evolved-idea.md`
- [x] Update README + references + examples 10–12

---

## Search queries and what they turned up

### Batch 1 — Filtered ANN, joins, AQP, classic IR, ColBERT, fusion, optimizers

| Query | Notable hits |
|-------|----------------|
| `site:arxiv.org filtered ANN ACORN HQI IVF PQ metadata filter vector search` | ACORN 2403.04871; FANNS benchmarks 2507.21989; attribute filtering study 2508.16263; pg filter-agnostic study 2603.23710 |
| `site:arxiv.org vector similarity join approximate VSS join SIGMOD VLDB` | DiskJoin 2508.18494; approx vector joins / soft work sharing 2603.16360; dynamic similarity joins 2105.01818 |
| `site:arxiv.org approximate query processing BlinkDB AQP sampling query language` | BlinkDB 1203.5485; MISS sample sizes; BlazeIt FrameQL |
| `Indri Galago query language operators IndriQL structured query retrieval` | Indri QL refs (Lemur); Galago operator language docs |
| `CQL Contextual Query Language SRU Library of Congress information retrieval` | LOC CQL/SRU standards pages |
| `site:arxiv.org ColBERT late interaction multi-vector retrieval operator PLAID` | ColBERT 2004.12832; ColBERTv2; PLAID 2205.09707 |
| `site:arxiv.org hybrid search reciprocal rank fusion CombSUM learning to rank operators retrieval` | Hybrid/zero-shot fusion papers; calibrated graph-vector fusion 2603.28886; LTR multi-channel |
| `Apache Calcite Cascades Volcano cost-based optimizer query planning survey` | Calcite arXiv 1802.10233; VolcanoPlanner javadocs |

### Batch 2 — Datalog, polystores, declarative ML, HyDE, spatial, array, multimedia, GraphRAG

| Query | Notable hits |
|-------|----------------|
| `site:arxiv.org Datalog Dedalus recursive query multi-hop knowledge graph retrieval` | Vadalog; SparqLog; MARS KGQA; spreading activation multi-hop |
| `BigDAWG polystore Garlic federated query mediation survey` | BigDAWG SIGMOD Record PDF; Garlic; NSF polystore survey |
| `site:arxiv.org SystemDS Weld Tensor Query Language Lara declarative machine learning algebra` | SystemDS 1909.02976; Weld 1709.06416; Lara 1604.03607 / LaraDB 1703.07342 |
| `site:arxiv.org HyDE Hypothetical Document Embeddings query rewriting multi-query RAG algebra` | HyDE 2212.10496; DMQR-RAG 2411.13154; Multi-HyDE; QDC compress 2603.21024 |
| `PostGIS spatial query language R-tree filter pushdown kNN spatial SQL analogy` | PostGIS query docs; `<->` kNN; GiST Index Cond / recheck |
| `SciDB TileDB Rasdaman array database query language AFL AFL++` | SciDB AFL/AQL; rasql; TileDB storage API (not QL) |
| `SQL/MM multimedia MPEG-7 query language content-based retrieval standard` | ISO/IEC 15938-12 MPQF; SQL/MM SIGMOD Record note |
| `site:arxiv.org GraphRAG formal graph retrieval augmented generation vector Cypher` | GraphRAG surveys 2408.08921, 2501.00309; GraphRAFT; practical GraphRAG |

### Batch 3 — Provenance, learned indexes, Substrait, NL2SQL, Filtered-DiskANN, VBASE, RRF, Lucene

| Query | Notable hits |
|-------|----------------|
| `site:arxiv.org provenance EXPLAIN query plan retrieval information retrieval why-provenance` | ProvSQL; LineageX; OneProvenance; “Queries that Explain their Work” |
| `site:arxiv.org learned index ANN … learned query optimizer vector database` | Learning-based filtered-ANN planning 2602.17914; query-aware routing 2606.19898; Exqutor 2512.09695 |
| `Substrait query plan IR cross-engine portable analytics intermediate representation` | substrait.io vision (“plans not SQL”) |
| `site:arxiv.org text-to-SQL survey 2024 2025 NL2SQL retrieval plan generation RAG` | NL2SQL LLM surveys 2408.05109, 2407.15186 |
| `Filtered-DiskANN Gollapudi predicate filtering vector index Microsoft` | WWW 2023 PDF on harsha-simhadri.org; DiskANN GitHub workflows |
| `site:arxiv.org VBASE bridging vector similarity search relational predicates Zhang` | OSDI’23 VBASE; MS Research page; MSVBASE GitHub (abs search also surfaced CHASE/AkasicDB/Exqutor/BoomHQ) |
| `Cormack Reciprocal Rank Fusion SIGIR CombSUM CombMNZ data fusion IR` | Cormack SIGIR’09 PDF; Montague score normalization; Bruch fusion analysis |
| `Apache Lucene query parser syntax Terrier query language matching models` | Lucene 10.x QueryParser; Terrier matchop docs |

### Batch 4 — Follow-ups

| Query | Notable hits |
|-------|----------------|
| `site:arxiv.org MUVERA multi-vector retrieval Google ColBERT MaxSim` | MUVERA 2405.19504 |
| `site:arxiv.org HQI hybrid query index filtered vector search Mohoney` | Confirmed 2304.01926 HQI paper |
| `Dedalus Datalog temporal logic Alvaro distributed programming recursive queries` | EECS-2009-173 Dedalus tech report |
| `Carbonell Goldstein Maximal Marginal Relevance MMR SIGIR diversity retrieval` | MMR 1998 PDF (CMU) |
| `Filtered-DiskANN "Filtered Approximate Nearest Neighbor Search" Gollapudi arxiv` | Confirmed **not** on arXiv; WWW’23 PDF URL |
| `VBASE Unifying Online Vector Similarity Search … OSDI` | USENIX + MSR + PDF links |
| `Lara A Framework for Unified Linear and Relational Algebra … Hutchison arxiv` | 1604.03607 / 1703.07342 |
| `site:arxiv.org Compass General Filtered Search SIEVE Effective Filtered Vector Search 2025` | Compass 2510.27141; SIEVE 2507.11907 |

---

## Primary fetches (successful)

| Resource | Method | Outcome |
|----------|--------|---------|
| Multiple `https://arxiv.org/abs/…` | `curl` | Abstracts extracted for ACORN, FANNS survey, learning planner, Exqutor, MUVERA, HyDE, ColBERT, PLAID, fusion analysis, HQI, DiskJoin, vector joins, Compass, SIEVE, routing, BlinkDB, Calcite, SystemDS, Weld, Lara, GraphRAG surveys |
| https://substrait.io/about/ | WebFetch | Portable plan IR vision captured |
| https://www.loc.gov/standards/sru/cql/ | WebFetch | CQL design goals |
| https://sigmod.org/.../04_vision_Duggan.pdf | WebFetch | Full BigDAWG polystore paper text |
| https://arxiv.org/html/2403.04871 | WebFetch | Timed out → fell back to abs via curl |
| Several arXiv HTML pages | WebFetch | Timed out → abs curl worked |
| USENIX VBASE presentation page | WebFetch | Cloudflare challenge; used MSR + PDF URL instead |

---

## Negative / sparse results (expected)

- Direct “vector query language standard” still thin — confirms need for adjacent search.
- AFL++ is **not** SciDB AFL (search noise); ignored.
- CAPS appeared when searching Filtered-DiskANN on arXiv (different paper); corrected via author PDF.

---

## Deliverables written

| Path | Role |
|------|------|
| `docs/05-brainstorm-adjacent.md` | 22 angles |
| `docs/06-deep-literature.md` | 28 annotated sources |
| `docs/07-evolved-idea.md` | Algebra + thesis |
| `docs/references.md` | URLs 56–106 appended |
| `README.md` | Deep dive (v2) section |
| `examples/10-hyde-rewrite-budget.rql` | HyDE + budgets |
| `examples/11-vsim-join-entities.rql` | VSIM JOIN |
| `examples/12-fuse-learned-explain.rql` | Learned fuse + late interact |
| `NOTES-search-log.md` | This file |

**Did not push to GitHub** (per instructions).

## 2026-09-16 (Europe/Dublin) — ACORN Pass 5 next-query log (not all executed)

Queued mutations from journal 0006 (for later execution, not claimed as completed searches in this step):
1. Filtered-DiskANN FilteredVamana StitchedVamana equality predicate cardinality
2. VBASE relaxed monotonicity OSDI 2023 vector similarity iterator join
3. Cormack Clarke Buettcher reciprocal rank fusion SIGIR 2009
4. FANNS filtered approximate nearest neighbor survey Lin 2025 arXiv:2505.06501
5. filtered ANN query planning selectivity correlation cost model 2026

Verified during thesis bib cleanup: MUVERA authors via https://arxiv.org/abs/2405.19504 (Dhulipala, Hadian, Jayaram, Lee, Mirrokni).
