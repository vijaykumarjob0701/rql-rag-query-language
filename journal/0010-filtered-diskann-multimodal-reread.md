# 0010 — Filtered-DiskANN multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~22:50 IST (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source (seed provisional for RQL algebra)  
**Source:** Gollapudi, Karia, Sivashankar, Krishnaswamy, Begwani, Raz, Lin, Zhang, Mahapatro, Srinivasan, Singh, Simhadri — *Filtered-DiskANN: Graph Algorithms for Approximate Nearest Neighbor Search with Filters* — WWW 2023 (Austin, TX)  
**URLs:** https://harsha-simhadri.org/pubs/Filtered-DiskANN23.pdf · DiskANN GitHub (implementation lineage)  
**Note:** **Not on arXiv** (confirmed earlier in NOTES); primary PDF is author-hosted WWW’23.  
**Local PDF:** `tooling/scripts/extract_out/filtered-diskann-www23.pdf` (11 pp)  
**Extract dir:** `tooling/scripts/extract_out/filtered_diskann_www23/` (14 figures assets; 88 nodes / 189 edges)  
**OKF bundle:** [`../knowledge/reads/filtered-diskann-www23/`](../knowledge/reads/filtered-diskann-www23/)

---

## Context

ACORN (`0006`) critiques specialized equality indices (incl. Filtered-DiskANN) for limited predicate forms; VBASE (`0009`) covers iterator/relational composition. This read grounds the **`SPECIALIZED`** physical mode with primary multimodal evidence.

## Question asked

What do FilteredVamana / StitchedVamana actually change in the **graph build** (not only search), which algorithms/figures show wins under low filter specificity, and what predicate class is in scope for RQL capability negotiation?

## Where we looked

- Local PDF download + extract/relate
- Full text: §1 drawbacks, §3–4 algorithms, §5 eval, §7 conclusions
- Visual: rendered Fig.1–3 page (QPS vs recall@10 × specificity percentiles on Turing/Prep/DANN)
- Caption inventory for Algs 1–5, Tables 1–4, Figs 1–11 (appendix Milvus/NHQ)

## Pass 1 — Skim

1. Filtered ANNS = ANN restricted to points matching query **labels** (date/price/lang-style metadata).
2. Critiques post-filter (must over-fetch under low specificity), per-label full indices (cost), and pre/inline methods that **do not rewrite the vector graph**.
3. Proposes **FilteredVamana** (streaming/incremental, geometry+labels in prune) and **StitchedVamana** (per-label Vamana then union+prune).
4. Targets ~thousands of filters, tens–hundreds labels/point; SSD-friendly DiskANN lineage; AUTHOR claims order-of-magnitude QPS at high recall@10.
5. Open problems: >several-thousand filters; complex SQL-like expressions; full dynamic deletes.

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro (1.1 filtered ANNS, 1.2 drawbacks, 1.3 results) → §2 Related → §3 FilteredVamana (3.1 FilteredGreedySearch, 3.2 build) → §4 StitchedVamana → §5 Evaluation → §6? (ads impact) → §7 Conclusions |
| Figures | Fig.1–3 main QPS–recall@10 grids (Turing/Prep/DANN × 100/75/50/25/1pc specificity); Fig.4 shuffled; Fig.5 unfiltered; Fig.6 28M scale; Fig.7–8 NHQ appendix; Fig.9–11 Milvus appendix |
| Tables | T1 datasets + specificity stats; T2 build times; T3–T4 improvement summaries |
| Algorithms | Alg.1 FilteredGreedySearch; Alg.2 FindMedoid; Alg.3 FilteredRobustPrune; Alg.4 FilteredVamana indexing; Alg.5 StitchedVamana indexing |

**Miss checklist:** main result page viewed; captions captured; T1 headers understood; appendix figures listed via captions (not every appendix raster deep-viewed — noted as residual uncertainty).

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| §1.2 | introduces | post vs pre vs inline failure modes | planner taxonomy |
| Alg.1 | implements | label-aware greedy search | only expand neighbors ∩ labels |
| Alg.3–4 | implements | FilteredVamana build | geometry **and** label-aware prune |
| Alg.5 | implements | StitchedVamana | per-label graphs ∪ prune |
| Fig.1–3 | grounds | low-specificity post-filter collapse | AUTHOR curves |
| §7 | qualifies | SQL-like filters / large \|F\| open | capability limits |

## Pass 4 — Seed (1–5%)

**Observation:**

> Efficient filtered ANNS often requires **changing index construction**, not only search: FilteredVamana / StitchedVamana build navigable graphs using both geometry and label sets, then search with FilteredGreedySearch that only expands label-matching neighbors. Empirically (authors), post-/inline baselines degrade sharply at low filter specificity while these graphs sustain high recall@10 at higher QPS on natural-label datasets. Scope in the paper is primarily **label / equality-style filters** (benchmark queries often singleton \(F_q\)); complex arbitrary predicates and very large filter vocabularies remain open.

**Interpretation for RQL** (`[hypothesis]`):

> `FilterExec=SPECIALIZED` is appropriate when the backend advertises Filtered-DiskANN-class indices **and** the predicate is (or rewrites to) supported label/equality forms with known cardinality. Outside that capability → fall back to `PRE`/`POST`/`SUBGRAPH`/`ITERATIVE`/`AUTO`. Do not treat Filtered-DiskANN as predicate-agnostic (that is ACORN’s claim space).

**Evidence pointers:** §1.2, Alg.1, Alg.3–5, Fig.1–3, Table 1, §7.

**Anti-overclaim:** unreproduced QPS; not a general SQL predicate engine; not automatic choice for ACL ranges/regex; RQL does not “include DiskANN.”

**Uncertainty:** full author-list formatting in bib; residual appendix figure depth; production DiskANN feature parity vs WWW’23 paper.

## Pass 5 — Next queries

1. Cormack et al. RRF SIGIR 2009 multimodal (short)  
2. FANNS survey Lin 2025 arXiv:2505.06501 taxonomy figures  
3. NHQ / HQI primary PDFs (ACORN related-work chase)  
4. DiskANN GitHub filtered query API vs Alg.1  
5. Selectivity×specificity cost models for AUTO planner

## Promote?

- [x] Thesis related-work + optimizer `SPECIALIZED` wording (hypothesis/provisional cleared to “read”)  
- [ ] Not settled algebra alone
