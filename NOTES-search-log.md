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


## 2026-09-17 ~00:12 IST — E2E CLI + pause checklist

| Action | Result |
|--------|--------|
| `rql_pipeline.py` offline glue | parse→plan→emit; run folder under `experiments/results/e2e/smoke/` |
| Smoke `examples/toy` × 3 profiles | **12/12** schema-validated; `run_validate.txt` |
| Pause checklist | `experiments/PAUSE_CHECKLIST.md` + journal 0027 |
| Policy | No live DBs; no push; recommend human P0 before more seeds |

## 2026-09-16 ~23:50 IST — Vendor API matrix (docs-only)

| Action | Result |
|--------|--------|
| WebSearch/WebFetch Qdrant filtering + hybrid Query API | Filter DSL; prefetch+`rrf`/`dbsf`; weighted RRF ≥1.17; multivector rescore; leaf filter propagation note |
| WebFetch ES kNN filtered + RRF retriever + Profile | `knn.filter` during approx kNN; `retriever.rrf`; weights ≥9.2; Profile API |
| WebFetch OpenSearch hybrid RRF | `hybrid` + score-ranker RRF (`rank_constant` default 60); normalisation alternative |
| WebFetch Weaviate hybrid + filtering + multi-vector | `relativeScoreFusion`/`rankedFusion`; **pre-filtering**; ColBERT multi-vector ≥1.29 |
| WebFetch Milvus `hybrid_search` API (+ search for rankers) | `expr`/`filter` before ANN (API wording); `RRFRanker`/`WeightedRanker`; HTML guides often 403 |
| curl pgvector README | POST-filter on approx indexes; iterative scans ≥0.8.0; hybrid via FTS + external RRF example; SQL EXPLAIN |
| Optional Pinecone/Redis docs | Pinecone filter-before-rank + client RRF; Redis FT.SEARCH filter=>KNN with BATCHES/ADHOC_BF |
| Artifacts | `docs/09-vendor-api-matrix.md`; journal 0020; OKF vendor-api-matrix-2026-09; thesis §07 weave |
| Policy | No live clusters/credentials; UNKNOWN cells preserved |

**Next seed candidates:** freeze LogicalPlan JSON Schema (capability flags ↔ matrix); deeper Substrait/Calcite read; skeleton adapters emitting plans only (no live I/O in CI).

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

## 2026-09-16 evening IST — VBASE + Filtered-DiskANN multimodal execution

| Query / action | Result |
|----------------|--------|
| WebSearch `VBASE Unifying Online Vector Similarity Search … OSDI 2023 Zhang` | Confirmed USENIX OSDI’23 title/authors; PDF `osdi23-zhang-qianxi_1.pdf` (not a different “Ending the Anomaly” paper) |
| `curl` USENIX VBASE PDF | Saved `tooling/scripts/extract_out/vbase-osdi23-zhang.pdf` (20 pp) |
| `curl` Filtered-DiskANN PDF | Saved `tooling/scripts/extract_out/filtered-diskann-www23.pdf` (11 pp; author host, not arXiv) |
| `extract_document.py` + `relate_components.py` | `extract_out/vbase_osdi23/` (149 nodes / 306 edges); `extract_out/filtered_diskann_www23/` (88 / 189) |
| Pass 1–5 journals | `journal/0009-vbase-multimodal-reread.md`, `journal/0010-filtered-diskann-multimodal-reread.md` |
| OKF bundles | `knowledge/reads/vbase-osdi23/`, `knowledge/reads/filtered-diskann-www23/` |

Queued after VBASE/Filtered-DiskANN: Cormack RRF — **done in 0011**; still open: FANNS survey Lin 2025 figure pass; MSVBASE code API vs paper §4.2.

## 2026-09-16 ~22:55 IST — Cormack RRF multimodal execution

| Query / action | Result |
|----------------|--------|
| WebSearch `Cormack Clarke Buettcher SIGIR 2009 Reciprocal Rank Fusion PDF` | Author PDF https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf; ACM 10.1145/1571941.1572114 |
| `curl` author PDF | `tooling/scripts/extract_out/cormack-sigir09-rrf.pdf` (**2 pages**, 66196 bytes) |
| `extract_document.py` + `relate_components.py` | `extract_out/rrf_cormack_sigir09/` (9 nodes / 6 edges; tables in body text) |
| Page renders | `page_renders/page-01.png`, `page-02.png` — Tables 1–3 viewed |
| Pass 1–5 journal | `journal/0011-rrf-cormack-multimodal-reread.md` |
| OKF bundle | `knowledge/reads/rrf-cormack-sigir09/` |

Queued after RRF: ColBERT/MUVERA — **done in 0012/0013**; still open: PLAID multimodal; Bruch CC/linear multimodal; FANNS survey Lin 2025 figures; Montague–Aslam Condorcet.


## 2026-09-16 ~22:57 IST — ColBERT + MUVERA multimodal execution

| Query / action | Result |
|----------------|--------|
| `curl` arXiv PDF `2004.12832` | `tooling/scripts/extract_out/colbert-sigir20.pdf` (**10 pages**, 4918165 bytes) |
| `extract_document.py` + `relate_components.py` | `colbert_sigir20/` (78 nodes / 196 edges); Figs 1–3 via page renders (vector graphics) |
| Pass 1–5 journal | `journal/0012-colbert-multimodal-reread.md` |
| OKF bundle | `knowledge/reads/colbert-sigir20/` |
| `curl` arXiv PDF `2405.19504` | `tooling/scripts/extract_out/muvera-2405.19504.pdf` (**26 pages**, 2214748 bytes) — **not blocked** |
| Extract + relate | `muvera_2405/` (155 nodes / 109 edges); full page renders 01–26 |
| Pass 1–5 journal | `journal/0013-muvera-multimodal-reread.md` |
| OKF bundle | `knowledge/reads/muvera-2405.19504/` |
| MaxSim harness | `experiments/harness/test_maxsim_late.py` → `experiments/results/maxsim/unit_test.txt` |

Queued (still open): PLAID multimodal (middle rewrite); Bruch CC/linear multimodal; FANNS survey Lin 2025 figures; Montague–Aslam Condorcet; vendor multi-vector API matrix.

## 2026-09-16 ~23:05 IST — PLAID multimodal execution

| Query / action | Result |
|----------------|--------|
| WebSearch `PLAID Santhanam ColBERT Efficient Passage Search arXiv 2022` | arXiv:2205.09707; CIKM’22 DOI 10.1145/3511808.3557325; pp 1747–1756 |
| `curl` arXiv PDF | `tooling/scripts/extract_out/plaid-2205.09707.pdf` (**10 pages**) |
| `extract_document.py` + `relate_components.py` | `plaid_2205/` (87 nodes / 87 edges); page renders 01–10 |
| Pass 1–5 journal | `journal/0014-plaid-multimodal-reread.md` |
| OKF bundle | `knowledge/reads/plaid-cikm22/` |
| Thesis weave | Centroid interaction + 4-stage prune **Established**; AUTHOR speedups only; ladder middle filled |

Queued after PLAID: Bruch — **done in 0016**; still open: Chen et al.; FANNS survey Lin 2025 figures; Montague–Aslam Condorcet; vendor API matrix.

## 2026-09-16 ~23:25 IST — Bruch fusion multimodal execution

| Query / action | Result |
|----------------|--------|
| WebSearch `Bruch fusion hybrid retrieval continuum` + docs/06 §12 | arXiv:2210.11934; DOI 10.1145/3596512 (ACM TOIS) |
| `curl` arXiv PDF | `tooling/scripts/extract_out/bruch-arxiv-2210.11934.pdf` (**36 pages**) |
| `extract_document.py` + `relate_components.py` | `bruch_2210/` (181 nodes / 283 edges; 81 figs / 13 tables); page renders 01–36 |
| Pass 1–5 journal | `journal/0016-bruch-fusion-multimodal-reread.md` (0015 remains hand-off only) |
| OKF bundle | `knowledge/reads/bruch-arxiv-2210.11934/` |
| Thesis weave | Fuse_linear / Fuse_ltr vs Fuse_rrf Established-vs-Hypothesis; AUTHOR NDCG only |
| Linear harness | `experiments/harness/test_linear_fusion.py` → `experiments/results/linear_fusion/unit_test.txt` |

Queued (still open): Chen et al. RRF-vs-CC cite-chase; FANNS survey Lin 2025 figures; Montague–Aslam Condorcet; vendor multi-vector / linear-fusion API matrix.

## 2026-09-16 ~23:35 IST — Chen ECIR’22 cite-chase (Bruch [5]) multimodal

| Query / action | Result |
|----------------|--------|
| Bruch refs → [5] Tao Chen et al. ECIR 2022 | “Out-of-Domain Semantics to the Rescue! Zero-Shot Hybrid Retrieval Models” |
| WebSearch + arXiv PDF `2201.10582` | `tooling/scripts/extract_out/chen-ecir2022-2201.10582.pdf` (**16 pages**) |
| Springer DOI | 10.1007/978-3-030-99736-6_7; pp. 95–110 |
| `extract_document.py` + `relate_components.py` | `chen_ecir2022/` (47 nodes / 86 edges); page renders 01–16 |
| Pass 1–5 journal | `journal/0017-chen-ecir2022-multimodal-reread.md` |
| OKF bundle | `knowledge/reads/chen-ecir2022-2201.10582/` |
| Thesis weave | Fuse_rrf vs Fuse_linear preference subsection (Established disagreement → Hypothesis planner rule); Chen bib + related-work |

**Resolution (no new metrics):** Chen prefers RRF for zero-shot (best min-max linear underperforms RRF ~3% rel.\ Recall@1K on Robust04/TREC-COVID, AUTHOR Fig 2); Bruch prefers TM2C2 on NDCG. Conflict = setups (metric / linear form / labels / channels), not a single false paper.

Queued after Chen: Montague–Aslam Condorcet — **done in 0018**; still open: FANNS survey Lin 2025 figures; vendor multi-vector / linear-fusion API matrix.

## 2026-09-16 ~23:30 IST — Montague–Aslam Condorcet multimodal

| Query / action | Result |
|----------------|--------|
| WebSearch `Montague Aslam Condorcet fusion CIKM 2002 PDF` | Author PDF https://www.khoury.northeastern.edu/~jaa/IS4200.10X1/resources/condorcet.pdf; ACM DOI 10.1145/584792.584881; pp. 538–548 |
| `curl` author PDF | `tooling/scripts/extract_out/montague-aslam-cikm02-condorcet.pdf` (**11 pages**) |
| `extract_document.py` + `relate_components.py` | `montague_condorcet_cikm02/` (53 nodes / 44 edges); page renders 01–11 |
| Pass 1–5 journal | `journal/0018-montague-aslam-condorcet-multimodal-reread.md` |
| OKF bundle | `knowledge/reads/montague-aslam-cikm02-condorcet/` |
| Thesis weave | Fuse_condorcet sibling of Fuse_rrf; RRF remains portable default |

Queued after Condorcet: FANNS survey — **done in 0019**; still open: vendor multi-vector / linear-fusion API matrix; optional Condorcet harness.

## 2026-09-16 ~23:35 IST — FANNS survey Lin et al. 2025 multimodal (filter taxonomy)

| Query / action | Result |
|----------------|--------|
| WebSearch `arXiv 2505.06501 FANNS survey Lin` | Title/authors verified: Yanjun Lin, Kai Zhang, Zhenying He, Yinan Jing, X. Sean Wang — *Survey of Filtered Approximate Nearest Neighbor Search over the Vector-Scalar Hybrid Data* |
| `curl` arXiv PDF | `tooling/scripts/extract_out/fanns-lin2025-2505.06501.pdf` (**25 pages**) |
| `extract_document.py` + `relate_components.py` | `fanns_lin2025_2505_06501/` (6 embedded imgs; 3 table extracts; 47 nodes / 65 edges); page renders 01–25 |
| Pass 1–5 journal | `journal/0019-fanns-lin2025-multimodal-reread.md` |
| OKF bundle | `knowledge/reads/fanns-lin2025-2505.06501/` |
| Thesis weave | FilterExec ← VSP/VJP/SJP/SSP + A1–A17; add PARTITION/ROUTER; `lin2025fanns` bib; §03 related-work; abstract |

**Established (survey structure):** pruning taxonomy VSP/VJP/SJP/SSP; A1–A17 map (Figs 1–2); selectivity×distribution difficulty schema (Figs 3–6); §6.3 multi-algorithm combination as literature direction.

**AUTHOR-only:** Fig 3 oracle-partition recall curves — unreproduced.

**Hypothesis (RQL):** FilterExec packaging PRE/POST/ITERATIVE/SUBGRAPH/SPECIALIZED/PARTITION/ROUTER/AUTO.

Queued (still open): **vendor multi-vector / weighted-linear / hybrid API matrix** (Qdrant, ES, Weaviate, Milvus); optional query-aware FANNS routing paper; optional Condorcet harness.

## 2026-09-16 ~23:55 IST — LogicalPlan / PhysicalPlan schema freeze

| Query / action | Result |
|----------------|--------|
| In-repo synthesis (docs/08, thesis §05–§07, docs/09, journal 0020) | No new external multimodal paper pass |
| Author `schemas/logical-plan.schema.json` + `physical-plan.schema.json` | JSON Schema draft 2020-12; version `0.1.0-draft` Hypothesis IR |
| Examples under `schemas/examples/` | 8 files: hybrid RRF L/P, filtered dense L/P, late+PLAID L/P, client RRF shim P, MUVERA ladder P |
| `pip install jsonschema` in `tooling/.venv` + `validate_plans.py` | **All 8 examples passed** → `experiments/results/plan_schema/validate.txt` |
| Thesis weave | §05 LogicalPlan freeze; §07 PhysicalPlan freeze; abstract/conclusion; rebuild PDF |
| Journal | `0021-logical-physical-plan-schema-v0.1.md` |

**Honesty:** Draft schemas are **Hypothesis** packaging — not a published standard. Vendor matrix cells remain Established docs-only survey.

**Next seed (done in 0022):** toy RQL parser → LogicalPlan JSON.

## 2026-09-16 ~23:59 IST — Toy RQL parser → LogicalPlan

| Query / action | Result |
|----------------|--------|
| Implement `experiments/harness/rql_parser/` | Tiny RETRIEVE/SEARCH/WHERE/FUSE subset → LogicalPlan 0.1.0-draft |
| Schema-aligned `.rql` (4 files) | 01 hybrid RRF, 02 filtered dense, 03 late, 04 hybrid linear |
| `test_rql_parser.py` + jsonschema | **4/4 parse + validate**; EMBED negative reject |
| Results | `experiments/results/rql_parser/*.logical.json` + `parse_validate.txt` |
| Thesis weave | §05 toy frontend; §07 layer-1 prototype; abstract/conclusion; rebuild PDF |
| Journal | `0022-toy-rql-parser.md` |

**Honesty:** Grammar packaging is **Hypothesis**. Not a full SQL engine. No retrieval metrics.

**Next seed (done in 0023):** physical planner stub (Logical→Physical + FilterExec/ShimCast).

## 2026-09-16 ~23:59 IST — Physical planner stub (Logical→Physical)

| Query / action | Result |
|----------------|--------|
| Implement `experiments/harness/rql_planner/` | Deterministic Filter/Fuse/Late rules + capability profiles |
| Profiles (docs-derived) | `qdrant.json`, `elasticsearch.json`, `pgvector.json` (journal 0020 flags) |
| `test_rql_planner.py` + jsonschema | **12/12 plan + validate** (4 logical × 3 profiles) |
| Results | `experiments/results/rql_planner/*.physical.json` + `plan_validate.txt` |
| Thesis weave | §06 planner stub; §07 layer-2; abstract/conclusion; rebuild PDF |
| Journal | `0023-physical-planner-stub.md` |

**Honesty:** Planner packaging is **Hypothesis**. Profiles are docs-derived — **not** live probes. No latency/recall invented.

**Next seed (done in 0024):** adapter emit stub (PhysicalPlan → backend JSON/SQL, no live CI).

## 2026-09-17 ~00:00 IST — Adapter emit stub (PhysicalPlan → vendor sketches)

| Query / action | Result |
|----------------|--------|
| Implement `experiments/harness/rql_adapters/` | qdrant / elasticsearch / pgvector emit (strings/JSON/SQL only) |
| CLI `emit_rql.py` + `test_rql_adapters.py` | **6/6** hybrid-rrf + filtered-dense × 3 profiles |
| Results | `experiments/results/rql_adapters/*.emit.json` (+ `*.request.sql`) + `emit_validate.txt` |
| Thesis weave | §07 layer-3 emit stub; abstract/conclusion; rebuild PDF |
| Journal | `0024-adapter-emit-stub.md` |

**Honesty:** Emit packaging is **Hypothesis**. Docs-shaped sketches — **not** executed. No latency/recall invented. No live DB calls.

**Next seed (done in 0025):** deeper Substrait / Apache Calcite read for IR adjacency.

## 2026-09-17 ~00:10 IST — Substrait / Calcite IR adjacency

| Query / action | Result |
|----------------|--------|
| Fetch substrait.io (about, relations, extensions, serialization) | Portable plan IR; extension points; no hard logical/physical split |
| Download Calcite arXiv:1802.10233 (10 pp) + page PNGs | Figs 1–4; traits; adapters; Volcano-like planner |
| Skim Cascades Graefe 1995 (10 pp) | Tasks / memo / enforcers vocabulary |
| Journal + OKF | `0025`; `substrait-spec-2026-09/`; `calcite-begoli-sigmod18/` |
| Thesis weave | §03 + §07 adjacency; abstract/conclusion; bib Cascades; rebuild PDF |

**Honesty:** Established = Substrait/Calcite/Cascades source facts. RQL adjacency = **Hypothesis** (inspired-by). **No** Substrait wire compat claim. **No push.**

**Next seed candidates:** end-to-end CLI glue `rql→plan→emit` (no live DB); **or** pause checklist for human P0 (protocol 03 live smoke / decide Substrait Extension*Rel in-scope?).

## 2026-09-17 ~00:55 IST — BlinkDB AQP budgets (journal 0031)

| Query / action | Result |
|----------------|--------|
| `BlinkDB Agarwal EuroSys 2013 DOI` | ACM 10.1145/2465351.2465355; pages 29–42; authors Agarwal/Mozafari/Panda/Milner/Madden/Stoica |
| Fetch `https://arxiv.org/pdf/1203.5485.pdf` | 16 pp arXiv v2; extract `tooling/scripts/extract_out/blinkdb_1203/` + page_renders |
| Pass 1–5 | Dual ERROR/TIME + ELP Established; RQL RECALL/LATENCY Hypothesis packaging; ε≠recall@k |
| Thesis fold Colab synth | journals 0030; §09 + Appendix A honest labels |


## 2026-09-17 ~01:10 IST — HyDE (Gao et al.) multimodal Pass 1–5

| Query / action | Result |
|----------------|--------|
| `Gao Ma Lin Callan HyDE Precise Zero-Shot Dense Retrieval venue` | ACL 2023 Long Papers; Anthology 2023.acl-long.99; DOI 10.18653/v1/2023.acl-long.99; pp. 1762–1777 |
| Fetch `https://arxiv.org/pdf/2212.10496.pdf` | **11 pp** arXiv v1; extract `tooling/scripts/extract_out/hyde_2212/` + page_renders |
| Pass 1–5 | hyp-doc→Contriever→doc–doc MIPS **Established**; RQL `REWRITE HYDE` **Hypothesis**; Tables 1–4 AUTHOR-only |
| Journal / OKF | `0032-hyde-multimodal-reread.md`; `knowledge/reads/hyde-2212.10496/` |
| Thesis fold | §03/§05/§08 + abstract/conclusion; bib `gao2023hyde`; rebuild PDF |

**Honesty:** No reproduced IR metrics. No push. Next optional: toy parser `REWRITE HYDE` / WITH CTE; Multi-HyDE/DMQR; Asai instruction-aware.

