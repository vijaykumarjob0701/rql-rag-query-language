# 0019 — FANNS survey Lin et al. 2025 multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~23:35 IST (Europe/Dublin)  
**Type:** multimodal source read (filter-strategy / taxonomy seed)  
**Status:** Pass 1–5 complete for this source  
**Source:** Yanjun Lin, Kai Zhang, Zhenying He, Yinan Jing, X. Sean Wang — *Survey of Filtered Approximate Nearest Neighbor Search over the Vector-Scalar Hybrid Data* — arXiv:2505.06501v1 (cs.DB), 10 May 2025  
**URLs:** https://arxiv.org/abs/2505.06501 · PDF https://arxiv.org/pdf/2505.06501 · code https://github.com/lyj-fdu/FANNS  
**Local PDF:** `tooling/scripts/extract_out/fanns_lin2025_2505_06501.06501.pdf` (**25 pp**)  
**Extract dir:** `tooling/scripts/extract_out/fanns_lin2025_2505_06501/` (6 embedded XObjects; 3 table extracts; 47 nodes / 65 edges; `page_renders/page-01..25.png`)  
**OKF bundle:** [`../knowledge/reads/fanns_lin2025_2505_06501.06501/`](../knowledge/reads/fanns_lin2025_2505_06501.06501/)  
**Cite-chase of:** queued after Condorcet 0018; prior FilterExec seeds ACORN 0006 / VBASE 0009 / Filtered-DiskANN 0010

---

## Context

FilterExec modes in thesis §06 were grounded in three primary papers plus an informal PRE/POST folklore. The Lin et al. 2025 survey is the dedicated **FANNS taxonomy** pass: pruning-focused classification (VSP/VJP/SJP/SSP), 17 algorithm families (A1–A17), and a selectivity×distribution query-difficulty schema. Goal: map survey taxonomy → RQL FilterExec, labelling ESTABLISHED survey structure vs HYPOTHESIS RQL packaging; AUTHOR-only for any speedups.

## Question asked

What filter-strategy taxonomy do Figs 1–2 / A1–A17 establish, how do selectivity and ID/POD/OOD (Figs 3–6) inform planner signals, and how should RQL name PRE/POST/ITERATIVE/SUBGRAPH/SPECIALIZED/PARTITION/ROUTER/AUTO without inventing metrics?

## Where we looked

- WebSearch `arXiv 2505.06501 FANNS survey Lin` → title/authors verified
- `curl` arXiv PDF + `extract_document.py` + `relate_components.py`
- Visual skim of all 25 page PNGs (focus: Fig 1–2 taxonomy; Fig 3–6 difficulty; Table 1–2; Alg 1–2; §3 A1–A17; §6.3 multi-algorithm combo)

## Pass 1 — Skim

1. Formal hybrid dataset / hybrid query + recall@k / selectivity definitions (§2).
2. Critiques coarse pre/post/in-filtering taxonomy; proposes **pruning-focused** four strategies: **VSP, VJP, SJP, SSP**.
3. Classifies **17** algorithms A1–A17 (Fig 2): Post-Filtering, VBase, AIRSHIP, ACORN, Faiss-IVF, CAPS, NHQ, HQANN, Filtered-DiskANN, SeRF, iRangeGraph, Pre-Filtering, Milvus-Partition, HQI, MA-NSW, UNG, WST.
4. Hybrid datasets Table 2; query difficulty = **selectivity × distribution** (ID/POD/OOD; Figs 3–6).
5. Open: general filters, workload-aware partition, **combining multiple algorithms** (§6.3).
6. No universal winner implied; practitioner guidance via taxonomy + difficulty factors.

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro (C1–C3 problems) → §2 Preliminaries (Defs, Alg 1 IVF / Alg 2 Graph) → §3 Review FANNS (3.1 framework; 3.2 VSP; 3.3 VJP; 3.4 SSP; 3.5 SJP) → §4 Hybrid datasets → §5 Distribution factor → §6 Open questions → §7 Conclusion |
| Figures | **Fig 1** pruning-focused framework (VSP/VJP/SJP/SSP pipelines + selectivity thumbs); **Fig 2** A1–A17 classification + interrelationships (index type / filter class colouring); **Fig 3** oracle-partition recall vs nprobe/efSearch × ID/POD/OOD; **Fig 4** UMAP MNIST-8M vs MTG; **Fig 5** Mahalanobis histograms; **Fig 6** 3×3 selectivity×distribution query schema Q1–Q9 |
| Tables | **Table 1** notations; **Table 2** hybrid datasets D1–D9 |
| Algorithms | **Alg 1** Search on IVF; **Alg 2** Search on Graph (preliminaries — not FANNS-specific) |
| Families A1–A17 | See Pass 3 map |

**Miss checklist:** all 25 pages rendered and opened; Fig 1–6 captions + axes understood; Tables 1–2 headers understood; embedded XObjects only on pp. 7, 13, 16 (vector drawings elsewhere recovered via page PNGs); pdfplumber/pymupdf table extracts noisy on layout — Table 2 recovered via text+PNG.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| Fig 1 | introduces | VSP/VJP/SJP/SSP | ESTABLISHED survey taxonomy |
| Fig 2 | implements | A1–A17 placement | ESTABLISHED classification |
| A1 Post-Filtering | grounds | VSP → RQL POST | over-fetch \(K'\) |
| A2 VBase | grounds | VSP refinement → ITERATIVE | relaxed monotonicity (cross 0009) |
| A4 ACORN | grounds | VJP → SUBGRAPH | predicate subgraph |
| A9 Filtered-DiskANN | grounds | VJP → SPECIALIZED | equality subgraphs (cross 0010) |
| A12 Pre-Filtering | grounds | SSP → PRE | scan filtered subset |
| A13–A14 Milvus/HQI | grounds | SJP → PARTITION | workload partition + per-subset FANNS |
| A6 CAPS AFT | qualifies | partition *within* IVF clusters | PARTITION-adjacent |
| §6.3 | introduces | multi-algorithm dynamic select | ROUTER/AUTO literature direction |
| Fig 3–6 | grounds | selectivity × ID/POD/OOD difficulty | planner signals; AUTHOR empirics unreproduced |
| Table 2 | grounds | hybrid dataset catalogue | for HUMAN microbench |

## Pass 4 — Seed (1–5%)

**Observation:**

> Lin et al. (arXiv:2505.06501) replace coarse pre/post/in-filtering with a **pruning-focused** taxonomy: **VSP** (vector-only; Post-Filtering A1, VBase A2), **VJP** (vector-centric joint; ACORN/AIRSHIP/Filtered-DiskANN/… A3–A11), **SSP** (scalar-only; Pre-Filtering A12), **SJP** (scalar-centric joint; Milvus-Partition/HQI/MA-NSW/UNG/WST A13–A17). Fig 1 gives pipelines and selectivity regimes; Fig 2 places 17 algorithms. Query difficulty is **selectivity × distribution** (ID/POD/OOD; Figs 3–6). §6.3 states combining multiple FANNS algorithms with dynamic selection (selectivity cost models in ADBV/Milvus/VBase; ACORN→PRE at high selectivity) as a system-level direction.

**Interpretation for RQL:**

> Package FilterExec modes as **HYPOTHESIS** names over **ESTABLISHED** survey families:  
> `PRE`←SSP/A12; `POST`←VSP/A1; `ITERATIVE`←A2 VBase (also 0009); `SUBGRAPH`←VJP/A4 ACORN (0006); `SPECIALIZED`←VJP/A9 Filtered-DiskANN (+ SeRF/iRangeGraph class; 0010); `PARTITION`←SJP/A13–A14 (+ multi-subset SJP); `ROUTER`/`AUTO`←§6.3 multi-algorithm selection (Hypothesis packaging; cite survey open direction + prior routing papers in docs/06). Surface survey vocabulary in EXPLAIN (`pruning_strategy ∈ {VSP,VJP,SJP,SSP}`, selectivity, distribution factor). Do **not** invent speedups; AUTHOR Fig 3 curves unreproduced.

**Evidence pointers:** Fig 1–2; A1–A17 §3.2–3.5; Fig 3–6; Table 1–2; §6.3; cross journals 0006/0009/0010.

**Anti-overclaim:** unreproduced recall curves; survey ≠ endorsement that every A* maps 1:1 to a distinct RQL opcode; NHQ/HQANN fusion-distance (A7–A8) is **not** FilterExec (separate fusion/index packaging); ROUTER is survey *direction*, not a finished algorithm in this PDF.

**Uncertainty:** arXiv v1 only (no journal pagination); residual vector-drawing figure fidelity beyond page PNGs; exact A5 Faiss-IVF vs “skip non-matching during IVF scan” vs POST naming.

## Pass 5 — Next queries

1. **Vendor multi-vector / weighted-linear / hybrid API matrix** (Qdrant, ES, Weaviate, Milvus) — fusion + filter pushdown surface (queued)
2. Optional: query-aware FANNS routing paper (arXiv:2606.19898) multimodal for ROUTER empirics
3. Optional: SIEVE / Compass primary PDFs for PARTITION/ROUTER neighbours
4. Optional: HUMAN FANNS microbench protocol 01 using Table 2 dataset picks
5. Optional: NHQ/HQANN fusion-distance primary reads (not FilterExec)

## Promote?

- [x] Journal 0019 + OKF `knowledge/reads/fanns_lin2025_2505_06501.06501/`
- [x] Thesis: strengthen §06 FilterExec from survey; cite `lin2025fanns`; related-work paragraph
- [x] Meta: NOTES / CHANGELOG / docs/06 / docs/08 / docs/references / journal index
- [ ] Do not invent FANNS speedups or fake RAG metrics
- [ ] Do not push
