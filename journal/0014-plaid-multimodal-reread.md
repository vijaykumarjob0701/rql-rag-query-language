# 0014 — PLAID multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~23:05 IST (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source  
**Source:** Santhanam, Khattab, Potts & Zaharia — *PLAID: An Efficient Engine for Late Interaction Retrieval* — CIKM ’22  
**URLs:** https://arxiv.org/abs/2205.09707 · https://arxiv.org/pdf/2205.09707.pdf · ACM DOI 10.1145/3511808.3557325 (pp. 1747–1756)  
**Local PDF:** `tooling/scripts/extract_out/plaid-2205.09707.pdf` (**10 pp**; arXiv v1 19 May 2022)  
**Extract dir:** `tooling/scripts/extract_out/plaid_2205/` (87 nodes / 87 edges; main Figs 1–8 are vector graphics — page PNGs under `page_renders/`)  
**OKF bundle:** [`../knowledge/reads/plaid-cikm22/`](../knowledge/reads/plaid-cikm22/)

---

## Context

ColBERT (0012) established MaxSim / late interaction. MUVERA (0013) established the FDE→MIPS→MaxSim-rerank rewrite for single-vector backends. PLAID is the **middle rung**: keep ColBERTv2 residual multi-vector semantics, accelerate with centroid interaction + multi-stage pruning.

## Question asked

What are PLAID’s centroid-interaction / pruning stages (formulas, pipeline, hyperparameters), which figures/tables ground the quality–latency claim, and what is safe **[Established]** for RQL’s ColBERT→PLAID→MUVERA ladder vs packaging **[Hypothesis]** / speedup tables **AUTHOR-only**?

## Where we looked

- Known arXiv `2205.09707` (bib `santhanam2022plaid`; docs/NOTES already cited)
- Venue confirmation: CIKM 2022 (reproducibility paper + Stanford ColBERT README)
- Local download + `extract_document.py` + `relate_components.py`
- Visual skim of `page_renders/page-01.png` … `page-10.png` (Figs 1–8, Tables 1–6)
- Full text §3 analysis + §4 PLAID (4.1–4.5) + §5 empirics

## Pass 1 — Skim

1. CIKM’22 / arXiv 10 pp: **PLAID** = Performance-optimized Late Interaction Driver for ColBERTv2.
2. Bottleneck of vanilla ColBERTv2: index gather + residual decompression on huge candidate sets (Fig 2a ~287 ms).
3. Core ideas: treat passages as **bags of centroid IDs**; **centroid interaction** ≈ MaxSim with centroid score lookups; **centroid pruning** via \(t_{cs}\); 4-stage funnel → residual MaxSim only on `ndocs/4` passages.
4. Empirics MS MARCO v1/v2, Wikipedia OpenQA, LoTTE; up to ~140M passages; AUTHOR speedups up to ~7× GPU / ~45× CPU.
5. Ablation (Fig 6): interaction, pruning, and fast kernels each contribute (AUTHOR).

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro; §2 Related (2.1 Neural IR, 2.2 Pruning); §3 ColBERTv2 analysis (3.1–3.4); §4 PLAID (4.1 Candidate gen, **4.2 Centroid interaction**, **4.3 Centroid pruning**, 4.4 Scoring, 4.5 Fast kernels); §5 Eval (5.1–5.4); §6 Conclusion |
| Figures | **Fig 1** late-interaction diagram (from ColBERT); **Fig 2** latency breakdown vanilla vs PLAID; **Fig 3** centroid-only recall of vanilla top-\(k\); **Fig 4** centroid-score eCDF; **Fig 5** **4-stage scoring pipeline**; **Fig 6** ablation speedups; **Fig 7** latency vs corpus size; **Fig 8** thread scaling |
| Tables | **Table 1** corpora + index GiB; **Table 2** hyperparams (`k`, `nprobe`, \(t_{cs}\), `ndocs`); **Tables 3–6** e2e quality+latency (MS MARCO v1, Wiki OpenQA, LoTTE, MS MARCO v2) |
| Algorithms | No numbered Alg.; pipeline = Fig 5 + §4 prose |
| Equations | **(1)** MaxSim \(S_{q,d}\) (ColBERT); **(2)** \(S_{c,q}=C\cdot Q^\top\); **(3)** \(\tilde{D}\) bag-of-centroid score rows; **(4)** MaxSim on \(\tilde{D}\); **(5)** prune predicate \(\max_j S_{c,q_{i,j}}\ge t_{cs}\) |

**Miss checklist:** all 10 pages opened as PNG; Fig 5 stages labeled; Tables 2–3 headers understood; extract XObjects decorative — **figures recovered via page renders**; ACM camera-ready page range recorded from secondary cites (verify before camera-ready bib).

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| Fig 2 + §3.2 | motivates | skip residual load for weak candidates | bottleneck = lookup/decompress |
| Fig 3 + §3.3 | grounds | centroid-only high recall @ \(10\cdot k\) | AUTHOR analysis |
| Fig 4 + §3.4 | motivates | \(t_{cs}\) pruning | heavy-tailed centroid scores |
| Eq. (2)–(4) + §4.2 | implements | centroid interaction ≈ MaxSim | ESTABLISHED mechanism |
| Eq. (5) + §4.3 | implements | centroid pruning | ESTABLISHED mechanism |
| Fig 5 | structures | Stages 1→2→3→4 funnel | ESTABLISHED pipeline |
| Table 2 | configures | `nprobe`, \(t_{cs}\), `ndocs` vs \(k\) | AUTHOR defaults |
| Tables 3–6 / Fig 6 | grounds | AUTHOR quality–latency / ablation | unreproduced |

## Pass 4 — Seed (1–5%)

**Observation:**

> PLAID accelerates ColBERTv2 late-interaction search by a **four-stage funnel** (Fig 5): (1) candidate generation from top-`nprobe` centroids per query token via a centroid→**passage-ID** inverted list; (2) **centroid interaction with pruning** — approximate MaxSim using precomputed \(S_{c,q}=C Q^\top\) rows, dropping tokens whose max centroid score \(< t_{cs}\), emit TopK(`ndocs`); (3) **centroid interaction without pruning**, emit TopK(`ndocs/4`); (4) residual decompression + **exact MaxSim** (Eq. 1) for final TopK(`k`). Centroid-only retrieval at depth \(\sim 10\cdot k\) recovers 99%+ of vanilla top-\(k\) on authors’ MS MARCO / LoTTE plots (Fig 3; AUTHOR). Authors report large latency wins (e.g. abstract up to 7× GPU / 45× CPU; Table 3 narrative ~6.8× / 45× at \(k=1000\)) — **AUTHOR numbers only**.

**Interpretation for RQL** (`[hypothesis]` packaging):

> Mark **centroid interaction (Eqs. 2–4), centroid pruning (Eq. 5), and the 4-stage residual MaxSim funnel (Fig 5)** as **[Established]** literature mechanisms filling the middle of the ColBERT→PLAID→MUVERA physical ladder for \(\mathrm{Search}_{late}\). Keep RQL names (`LATE_PLAID` / capability `late_plaid`) and compile policy as **[Hypothesis]**. Label all speedup/MRR/Success@k tables **AUTHOR-only / unreproduced**. Do not treat PLAID as an FDE/MIPS substitute — it still needs multi-vector residual storage; MUVERA remains the single-vector-ANN rewrite (0013).

**Evidence pointers:** Fig 2, 3, 5, 6; Eqs. (1)–(5); §4.1–4.5; Tables 2–3.

**Anti-overclaim:** unreproduced latencies/quality; Stage-4 MaxSim still required for reported quality; CPU padding-free MaxSim kernels ≠ GPU path; hyperparams are author grid not universal; paper builds on ColBERTv2 residuals (not vanilla ColBERT v1 storage).

**Uncertainty:** ACM proceedings page span (1747–1756 cited by reproducibility study — confirm against ACM DL before final bib); arXiv preprint pagination (10 pp) vs camera-ready.

## Pass 5 — Next queries

1. Optional: ColBERTv2 (Santhanam et al., NAACL’22) multimodal if residual-compression details needed beyond PLAID §3.1
2. **Bruch** linear / continuum-fusion multimodal for `Fuse_linear` sibling (do not rush a thin 0015)
3. Vendor multi-vector / late_interaction APIs vs PLAID stage semantics
4. Optional: PLAID reproducibility study (arXiv:2404.14989) as secondary — not required for Established mechanism label

## Promote?

- [x] Thesis: PLAID centroid interaction + pruning stages **[Established]**; rewrite ladder middle filled; speedup tables AUTHOR-only
- [x] OKF bundle under `knowledge/reads/plaid-cikm22/`
- [ ] Not inventing new MaxSim — Stage 4 still ColBERT Eq. (1) / ColBERT Eq. (3)
