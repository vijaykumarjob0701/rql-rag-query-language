# 06 — Deep Literature (Adjacent Searches)

**Research date:** 2026-09-16 (Europe/Dublin)  
**Method:** Adjacent-angle WebSearch + primary abs/PDF fetch (arxiv, LOC, SIGMOD Record, USENIX/MS pages).  
**Count:** **28** substantive papers/systems documented below (not vendor SDK fluff).  
**Uncertainty flagged** where venue/year inferred from arXiv date or secondary pages.

Companion: [`05-brainstorm-adjacent.md`](05-brainstorm-adjacent.md) · synthesis: [`07-evolved-idea.md`](07-evolved-idea.md).

---

## A. Filtered ANN / hybrid vector+predicate (physical algebra)

### 1. ACORN — Patel, Kraft, Guestrin, Zaharia (2024)
- **Venue/ID:** arXiv:2403.04871 (SIGMOD-era hybrid search; confirm venue on camera-ready)
- **URL:** https://arxiv.org/abs/2403.04871
- **Takeaway:** Predicate-agnostic hybrid search on HNSW via *predicate subgraph traversal* (emulating an ideal hybrid strategy without building one index per predicate). Contrasts with Filtered-DiskANN / HQANN-style equality-only / low-cardinality predicate sets. Directly motivates RQL’s `FILTER_MODE` beyond naive PRE/POST.
- **Implication for RQL:** Logical `WHERE` must compile to a **physical filter strategy** chosen by selectivity & predicate shape (equality vs arbitrary), not a single global default.

### 2. Filtered-DiskANN — Gollapudi et al. (2023, WWW)
- **URL:** https://harsha-simhadri.org/pubs/Filtered-DiskANN23.pdf · https://github.com/microsoft/DiskANN
- **Takeaway:** Label-aware Vamana graphs (FilteredVamana streaming, StitchedVamana batch) for equality/OR-style label filters with strong latency-recall; **not** general arbitrary predicates.
- **Implication for RQL:** Capability profiles: backends advertise supported filter classes; planner refuses or rewrites unsupported `WHERE` shapes.

### 3. HQI — Mohoney et al., “High-Throughput Vector Similarity Search in Knowledge Graphs” (2023)
- **Venue/ID:** arXiv:2304.01926
- **URL:** https://arxiv.org/abs/2304.01926
- **Takeaway:** Workload-aware Hybrid Query Index: qd-tree-like partitions using historical filters + vectors; per-leaf IVF with attribute bitmaps; batch matrix-mult optimizations for related-KG hybrid queries.
- **Implication for RQL:** Optional `OPTION workload_hint=…` / stats catalog; partition pruning as physical rewrite.

### 4. CAPS — Gupta et al. (2023)
- **Venue/ID:** arXiv:2308.15014
- **URL:** https://arxiv.org/abs/2308.15014
- **Takeaway:** Constrained ANN via **space partitions** (not graphs); competitive recall-latency with much smaller index than graph constrained search.
- **Implication for RQL:** Physical trait `IndexKind ∈ {HNSW, IVF, Partition, DiskANN}`; planner picks by size/latency SLO.

### 5. Survey of FANNS — Lin et al. (2025) — **multimodal Pass 1–5 done (journal 0019)**
- **Venue/ID:** arXiv:2505.06501v1 (cs.DB), 10 May 2025; **25 pp**
- **Authors:** Yanjun Lin, Kai Zhang, Zhenying He, Yinan Jing, X. Sean Wang (Fudan)
- **URL:** https://arxiv.org/abs/2505.06501 · code https://github.com/lyj-fdu/FANNS
- **OKF:** `knowledge/reads/fanns-lin2025-2505.06501/`
- **Takeaway (Established taxonomy):** Formalises hybrid dataset/query + metrics; **pruning-focused** taxonomy **VSP / VJP / SJP / SSP** classifying **A1–A17** (Figs 1–2), finer than pre/post/in-filtering. Query difficulty = **selectivity × distribution** (ID/POD/OOD; Figs 3–6). §6.3: combining multiple FANNS algorithms with dynamic selection is an open system direction.
- **Implication for RQL:** Map survey families → FilterExec (`PRE`←SSP/A12, `POST`←VSP/A1, `ITERATIVE`←A2 VBase, `SUBGRAPH`←VJP/ACORN, `SPECIALIZED`←Filtered-DiskANN class, `PARTITION`←SJP/Milvus-Partition/HQI, `ROUTER`/`AUTO`←§6.3). EXPLAIN should speak survey vocabulary (`pruning_strategy`, selectivity, distribution factor). **AUTHOR-only** for Fig 3 curves — unreproduced.

### 6. Compass — (2025)
- **Venue/ID:** arXiv:2510.27141
- **URL:** https://arxiv.org/abs/2510.27141
- **Takeaway:** General filtered search without a new specialized index: combine HNSW/IVF with B+-trees and a shared candidate queue for arbitrary conjunctions/disjunctions/ranges.
- **Implication for RQL:** Prefer compiling to **composable existing indexes** over requiring vendor-specific hybrid indexes.

### 7. SIEVE — (2025)
- **Venue/ID:** arXiv:2507.11907
- **URL:** https://arxiv.org/abs/2507.11907
- **Takeaway:** Collection of predicate-specific proximity indexes; router picks fastest index per query; large speedups vs single HNSW under hard predicates.
- **Implication for RQL:** Multi-index collections as physical option; `EXPLAIN` shows which specialized index was chosen.

### 8. Learning-based Filtered-ANN planning — Gan & Wang (2026)
- **Venue/ID:** arXiv:2602.17914
- **URL:** https://arxiv.org/abs/2602.17914
- **Takeaway:** Lightweight ML selects pre- vs post-filtering (and related plans) from dataset/query statistics; generic to backend ANN.
- **Implication for RQL:** `FILTER_MODE AUTO` becomes a **learned physical policy**, not a heuristic constant.

### 9. Query-aware routing for FANNS — (2026)
- **Venue/ID:** arXiv:2606.19898
- **URL:** https://arxiv.org/abs/2606.19898
- **Takeaway:** No single filtered-ANN method dominates even within one dataset; per-query routing over ACORN/UNG/SIEVE-class methods using predicted recall + offline QPS tables.
- **Implication for RQL:** Physical planner = **router**; logical plan stays stable across backends.

### 10. VBASE — Zhang et al. (OSDI 2023)
- **URL:** https://www.microsoft.com/en-us/research/publication/vbase-unifying-online-vector-similarity-search-and-relational-queries-via-relaxed-monotonicity/ · PDF: https://www.usenix.org/system/files/osdi23-zhang-qianxi_1.pdf · code: https://github.com/microsoft/MSVBASE
- **Takeaway:** “Relaxed monotonicity” — incremental Open/Next/Close traversal continues until enough tuples satisfy relational predicates, then final sort; unifies ANN with SQL filters/joins/analytics far beyond TopK-only APIs.
- **Implication for RQL:** Treat ANN as an **iterator** in a relational plan (not a one-shot TopK RPC); enables `VSIM JOIN` and iterative filter as first-class.

---

## B. Fusion, late interaction, rewriting (logical operators)

### 11. Reciprocal Rank Fusion — Cormack, Clarke, Büttcher (SIGIR 2009)
- **URL:** https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf
- **Takeaway:** Rank-only fusion `Σ 1/(k+rank)` (often k=60); strong metasearch baseline without score calibration.
- **Implication for RQL:** `FUSE RRF` is historically grounded; keep as default portable fusion.


### 11b. Condorcet-fuse — Montague & Aslam (CIKM 2002)
- **Venue/ID:** CIKM’02; DOI 10.1145/584792.584881; pp. 538–548
- **URL:** https://www.khoury.northeastern.edu/~jaa/IS4200.10X1/resources/condorcet.pdf · https://doi.org/10.1145/584792.584881
- **Takeaway:** Majoritarian fusion: sort document pool with pairwise majority runoff comparator (Alg 1+3), \(O(nk\log n)\), ranks only. Fig 1 taxonomy (ranks×training). AUTHORS report TREC MAP wins vs CombMNZ/rCombMNZ/Borda (unreproduced); dependence filtering for correlated runs. Multimodal Pass 1–5: journal `0018`; OKF `knowledge/reads/montague-aslam-cikm02-condorcet/`.
- **Implication for RQL:** `Fuse_condorcet` as Fuse-family sibling of `Fuse_rrf` (both rank-only); keep RRF as portable default (Cormack AUTHORS prefer RRF on their suites).

### 12. Analysis of fusion for hybrid retrieval — Bruch et al. (TOIS 2023 / arXiv:2210.11934)
- **Venue/ID:** arXiv:2210.11934; DOI 10.1145/3596512 (ACM TOIS)
- **URL:** https://arxiv.org/abs/2210.11934
- **Takeaway:** Convex combination (CC/TM2C2) of normalised lexical+semantic scores; RRF parameter-sensitive; CC sample-efficient; AUTHORS report CC > RRF on their suite (unreproduced here). Multimodal Pass 1–5: journal `0016`; OKF `knowledge/reads/bruch-arxiv-2210.11934/`.
- **Implication for RQL:** First-class `Fuse_linear` / `Fuse_ltr` alongside `Fuse_rrf`; don’t overfit product defaults to RRF-only.

### 12b. Zero-shot hybrid / RRF vs linear interp — Chen et al. (ECIR 2022 / arXiv:2201.10582)
- **Venue/ID:** ECIR 2022 LNCS; DOI 10.1007/978-3-030-99736-6_7; pp. 95–110; arXiv:2201.10582
- **URL:** https://arxiv.org/abs/2201.10582
- **Takeaway:** Zero-shot lexical+deep hybrid via **RRF** (\(k=60\)); argue score linear interpolation needs min-max + \(\alpha\) tuning that fights zero-shot; AUTHORS report best-tuned BM25+NPR linear still ~3% relative Recall@1K behind RRF(BM25,NPR) on Robust04 & TREC-COVID (Fig 2; unreproduced here). Multimodal Pass 1–5: journal `0017`; OKF `knowledge/reads/chen-ecir2022-2201.10582/`.
- **Implication for RQL:** Cite-chase of Bruch [5]: RRF-vs-CC “disagreement” is a **setup conflict** (Recall@1K zero-shot RRF vs NDCG TM2C2). Planner preference among Fuse_rrf / Fuse_linear is **Hypothesis** grounded in Established mechanisms.

### 13. ColBERT — Khattab & Zaharia (2020)
- **Venue/ID:** arXiv:2004.12832
- **URL:** https://arxiv.org/abs/2004.12832
- **Takeaway:** Late interaction / MaxSim over token embeddings — accuracy of deep interaction with cheaper retrieval than full cross-encoders.
- **Implication for RQL:** `SEARCH LATE_INTERACT` / `COLBERT` as a leaf, not an afterthought.

### 14. PLAID — Santhanam et al. (2022)
- **Venue/ID:** arXiv:2205.09707
- **URL:** https://arxiv.org/abs/2205.09707
- **Takeaway:** Centroid interaction + pruning engine making ColBERTv2 production-latency viable.
- **Implication for RQL:** Physical rewrite: late-interact → centroid prune → exact MaxSim (like hash join variants).

### 15. MUVERA — Dhulipala et al. (2024)
- **Venue/ID:** arXiv:2405.19504
- **URL:** https://arxiv.org/abs/2405.19504
- **Takeaway:** Fixed-dimensional encodings reduce multi-vector retrieval to single-vector MIPS with approximation guarantees; then MaxSim rerank.
- **Implication for RQL:** Optional rewrite `LATE_INTERACT ⇒ FDE_ANN + MAXSIM_RERANK`.

### 16. HyDE — Gao, Ma, Lin, Callan (ACL 2023) — **multimodal Pass 1–5 done (journal 0032)**
- **Venue/ID:** ACL 2023 Long Papers, pp. 1762–1777; DOI 10.18653/v1/2023.acl-long.99; arXiv:2212.10496
- **URL:** https://aclanthology.org/2023.acl-long.99/ · https://arxiv.org/abs/2212.10496
- **OKF:** `knowledge/reads/hyde-2212.10496/`
- **Takeaway (Established mechanism):** InstructLM generates hypothetical document(s) → unsupervised Contriever/mContriever embeds → MIPS in doc–doc space (Eqs. 4–8; Fig 1). No HyDE-specific training; query–doc scores not explicitly modeled.
- **AUTHOR-only:** Tables 1–4 DL/BEIR/Mr.TyDi — unreproduced.
- **Implication for RQL (Hypothesis packaging):** `REWRITE HYDE` / algebra `Rewrite_hyde` as costed plan node feeding `EMBED`/`Search_dense` (examples/10); multi-sample mean optional.

### 17. MMR — Carbonell & Goldstein (SIGIR 1998) — **multimodal Pass 1–5 done (journal 0033)**
- **Venue/ID:** SIGIR 1998, pp. 335–336; DOI 10.1145/290941.291025
- **URL:** https://www.cs.cmu.edu/~jgc/publication/MMR_DiversityBased_Reranking_SIGIR_1998.pdf · https://doi.org/10.1145/290941.291025
- **OKF:** `knowledge/reads/mmr-carbonell-sigir98/`
- **Takeaway (Established formula):** MMR def = Arg max_{Di ∈ R∖S} [λ Sim₁(Di,Q) − (1−λ) max_{Dj ∈ S} Sim₂(Di,Dj)]; λ=1 relevance-only; λ=0 max diversity.
- **AUTHOR-only:** Table 1 sentence precision; SUMMAC F=.73; n=5 pilot — unreproduced.
- **Implication for RQL (Hypothesis packaging):** `DIVERSIFY MMR` / algebra `Diversify_mmr(λ)` as post-retrieve/post-fuse diversity node (not a Fuse op).

---

## C. Classic IR & standards (language design ancestors)

### 18. Indri / Galago structured query languages
- **URLs:** http://lemurproject.org/lemur/IndriQueryLanguage.php · https://galagosearch.org/retrieval.html
- **Takeaway:** Everything-is-an-operator IR: `#combine`, `#weight`, `#wand`, `#odN`/`#uwN`, `#filreq`/`#filrej`, field restriction; Galago makes ranking functions query-language parameters.
- **Implication for RQL:** Prefer **composable scored operators** over SQL-only SELECT lists for ranking algebra.

### 19. CQL — Contextual Query Language (Library of Congress / SRU)
- **URL:** https://www.loc.gov/standards/sru/cql/
- **Takeaway:** Human-readable portable IR language with context sets and conformance profiles — bridges “Google-simple” and “SQL-powerful.”
- **Implication for RQL:** Ship **capability profiles** (Base, Hybrid, GraphHop, LateInteract) like CQL context sets.

### 20. Lucene QueryParser / Terrier matchop
- **URLs:** https://lucene.apache.org/core/10_5_1/queryparser/ · https://github.com/terrier-org/terrier-core/blob/5.x/doc/querylanguage.md
- **Takeaway:** Production lexical QL (Boolean, proximity, boosts) vs research matchop (`#band`, `#uwN`, weighting models).
- **Implication for RQL:** `BM25` leaf should accept Lucene-like query strings as optional sugar over structured ops.

---

## D. Optimizers, federation, declarative compute (plan IR)

### 21. Apache Calcite — Begoli et al. (2018)
- **Venue/ID:** arXiv:1802.10233 / SIGMOD’18
- **URL:** https://arxiv.org/abs/1802.10233
- **OKF:** `knowledge/reads/calcite-begoli-sigmod18/` · journal **0025**
- **Takeaway (Established):** Embeddable algebra+optimizer; traits/calling convention; adapters + enumerable fallback; Volcano-like cost-based planner (Cascades vocabulary via Graefe 1995).
- **Implication for RQL:** Planner as Calcite-*inspired* capability negotiation — **not** a Calcite embed (Hypothesis packaging).

### 22. BigDAWG polystore — Duggan et al. (SIGMOD Record 2015)
- **URL:** https://sigmod.org/publications/sigmodRecord/1506/pdfs/04_vision_Duggan.pdf
- **Takeaway:** Islands (data model + QL + engines), shims, SCOPE/CAST across models; black-box performance monitoring for engine choice.
- **Implication for RQL:** Each vector backend is a **shim** under a Retrieval Island; cross-engine plans use CAST (e.g., ANN hits → graph traverse).

### 23. Substrait
- **URL:** https://substrait.io/ · about · extensions · physical_relations
- **OKF:** `knowledge/reads/substrait-spec-2026-09/` · journal **0025**
- **Takeaway (Established):** Portable serialized plans (not SQL text); extension relations/functions; **no** hard logical/physical split in the spec (conventional).
- **Implication for RQL:** Long-term interchange *may* emit/embed Substrait extensions — today RQL JSON is Substrait-*inspired* Hypothesis IR only (do not claim wire compatibility).

### 24. BlinkDB — Agarwal et al. (EuroSys 2013) — **multimodal Pass 1–5 done (journal 0031)**
- **Venue/ID:** EuroSys ’13 pp. 29–42; DOI 10.1145/2465351.2465355; preprint arXiv:1203.5485v2 (16 pp read)
- **Authors:** Sameer Agarwal, Barzan Mozafari, Aurojit Panda, Henry Milner, Samuel Madden, Ion Stoica
- **URL:** https://doi.org/10.1145/2465351.2465355 · https://arxiv.org/abs/1203.5485
- **OKF:** `knowledge/reads/blinkdb-eurosys13/`
- **Takeaway (Established):** Dual declarative contracts (`ERROR WITHIN ε AT CONFIDENCE C` **or** `WITHIN T`); multi-resolution stratified samples; **ELP** selects sample size; Table 2 closed-form aggregate variances. AUTHOR 17TB/<2s/2–10% unreproduced.
- **Implication for RQL (Hypothesis packaging):** `OPTION RECALL TARGET` / `LATENCY` + PhysicalPlan `budgets.*` steal contract+ELP doctrine for retrieval effort knobs. **Delineation:** do **not** equate BlinkDB aggregate ε with ANN recall@k.

### 25. SystemDS — Boehm et al. (2019)
- **Venue/ID:** arXiv:1909.02976
- **URL:** https://arxiv.org/abs/1909.02976
- **Takeaway:** Declarative ML across the data-science lifecycle with compilation to distributed/federated runtimes.
- **Implication for RQL:** Retrieval plans as compileable DAGs with cost models, not notebook scripts.

### 26. Weld — Palkar et al. (2017)
- **Venue/ID:** arXiv:1709.06416
- **URL:** https://arxiv.org/abs/1709.06416
- **Takeaway:** Cross-library IR that fuses data-parallel work and kills materialization between stages.
- **Implication for RQL:** Fuse embed→ANN→filter→rerank without dumping full candidate payloads to the client.

### 27. Lara / LaraDB — Hutchison, Howe, Suciu (2016–2017)
- **Venue/ID:** arXiv:1604.03607 · arXiv:1703.07342
- **URL:** https://arxiv.org/abs/1604.03607
- **Takeaway:** Unify relational + linear algebra via associative tables and three ops: **join, union, ext**.
- **Implication for RQL:** Minimal kernel: scored relations + join (incl. VSIM), union (multi-query), ext (rewrite/expand/traverse).

---

## E. GraphRAG, joins, vector-SQL optimizers

### 28a. GraphRAG surveys — (2024–2025)
- **URLs:** https://arxiv.org/abs/2408.08921 · https://arxiv.org/abs/2501.00309
- **Takeaway:** Graph indexing → graph-guided retrieval → graph-enhanced generation; hybrid vector+structure is the norm; Cypher remains the practical graph surface.
- **Implication for RQL:** `TRAVERSE` / path patterns compile to Cypher when available; otherwise entity-table joins.

### 28b. DiskJoin / approximate vector joins — (2025–2026)
- **URLs:** https://arxiv.org/abs/2508.18494 · https://arxiv.org/abs/2603.16360
- **Takeaway:** Threshold vector similarity join as a batch primitive (distinct from online VSS); work sharing & merged indexes.
- **Implication for RQL:** `VSIM JOIN … ON distance < θ` for entity linking / multi-corpus matching.

### 28c. Exqutor — (2025)
- **Venue/ID:** arXiv:2512.09695
- **URL:** https://arxiv.org/abs/2512.09695
- **Takeaway:** Vector-augmented analytical SQL suffers from bad ANN cardinality estimates; Exqutor uses exact-cardinality-style probes with vector indexes during optimization.
- **Implication for RQL:** Planner may run **cheap cardinality probes** (or learned estimators) before choosing filter order.

### 28d. Dedalus — Alvaro et al. (UC Berkeley, 2009–2011)
- **URL:** https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-173.html
- **Takeaway:** Datalog + time for distributed mutable state / recursion with safety checks.
- **Implication for RQL:** Bounded recursive multi-hop (`WITH RECURSIVE … MAX_HOPS n`) with stratified safety.

---

## Coverage matrix (angle → sources)

| Angle (from doc 05) | Sources used |
|---------------------|--------------|
| Classic IR QLs | 18, 20 |
| CQL | 19 |
| Spatial analogy | (PostGIS docs — see search log; informs planner vocab) |
| Array DBs | SciDB/Rasdaman docs in search log |
| SQL/MM / MPEG-7 | ISO MPQF references in search log |
| AQP | 24 |
| Cascades/Calcite | 21 |
| Polystores | 22 |
| Substrait | 23 |
| Datalog | 28d |
| Filtered ANN | 1–10 |
| Learned FANNS planners | 8, 9, 28c |
| Hybrid fusion | 11, 12 |
| ColBERT/late interact | 13–15 |
| GraphRAG | 28a |
| Declarative ML | 25–27 |
| Query rewriting | 16 |
| Provenance/EXPLAIN | ProvSQL lineage literature (search log; motivates § in doc 07) |
| Vector joins | 28b |
| VBASE iterator model | 10 |

---

## What we deliberately did *not* treat as “new RQL languages”

TopK SQL, VelesQL, QQL, O’Reilly VQL — already covered in v1 [`04-related-work.md`](04-related-work.md). This deep dive asks what algebra those skins should compile to.
