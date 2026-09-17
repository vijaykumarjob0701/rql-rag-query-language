# 0033 — MMR multimodal re-read (Pass 1–5): Diversify_mmr / DIVERSIFY MMR

**Date:** 2026-09-17 ~01:20 IST (Europe/Dublin)  
**Type:** multimodal source read (diversity reranking / anti-redundancy)  
**Status:** Pass 1–5 complete for this source  
**Source:** Carbonell & Goldstein — *The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries* — SIGIR 1998, pp. 335–336  
**URLs:** CMU PDF [MMR_DiversityBased_Reranking_SIGIR_1998.pdf](https://www.cs.cmu.edu/~jgc/publication/MMR_DiversityBased_Reranking_SIGIR_1998.pdf) · DOI [10.1145/290941.291025](https://doi.org/10.1145/290941.291025) · ACM DL · DBLP CarbonellG98  
**Local PDF:** `tooling/scripts/extract_out/mmr-carbonell-sigir98.pdf` (**2 pp**; also `knowledge/reads/mmr-carbonell-sigir98/MMR_DiversityBased_Reranking_SIGIR_1998.pdf`)  
**Extract dir:** `tooling/scripts/extract_out/mmr_carbonell_sigir98/` (0 XObject figures; Table 1 recovered via text+page PNG; `page_renders/page-01..02.png`)  
**OKF bundle:** [`../knowledge/reads/mmr-carbonell-sigir98/`](../knowledge/reads/mmr-carbonell-sigir98/)  
**Cite-chase of:** provisional `Diversify_mmr` / `DIVERSIFY MMR` in docs/05–08, thesis §05 Diversify row; sibling to HyDE rewrite pass (0032)

---

## Context

RQL’s evolved algebra already lists `Diversify_mmr(λ)` as a post-retrieve diversity op citing Carbonell MMR, but without a multimodal Pass 1–5 the formula was only historically named. After HyDE grounded rewrite (0032), the next clean seed was MMR so we can label the **λ-parameterized maximal marginal relevance** formula Established while keeping RQL surface packaging Hypothesis — and explicitly **not** treating AUTHOR Table 1 / SUMMAC F-scores as our metrics.

## Question asked

What exact MMR definition (Arg max over relevance−novelty with λ), λ extremes, and summarization/reorder uses does Carbonell & Goldstein establish, and how should RQL name `Diversify_mmr` / `DIVERSIFY MMR` without fake metrics?

## Where we looked

- WebSearch `Carbonell Goldstein MMR SIGIR 1998 The Use of MMR Diversity-Based Reranking PDF` → CMU PDF; DOI 10.1145/290941.291025; SIGIR’98 pp. 335–336
- `curl` CMU PDF + `extract_document.py` + `relate_components.py` + full page PNG skim (both pages)
- Focus: §2 MMR def / formula; §3 pilot reorder; §4 summarization + Table 1; §5 conclusion; refs [1]–[6]

## Pass 1 — Skim

1. Combines **query relevance** with **information novelty** for retrieval reorder and passage summarization.
2. Method noun: **Maximal Marginal Relevance (MMR)** — linear combination of Sim₁(Di,Q) and −max Sim₂(Di,Dj∈S).
3. Tunable λ ∈ [0,1]: λ=1 → pure relevance order; λ=0 → maximal diversity among R; intermediate → tradeoff.
4. Clearest AUTHOR narrative advantage: **multi-document** non-redundant summaries (vs single-doc / plain retrieval).
5. Short paper (2 pp SIGIR poster/short); pilot n=5 users; SUMMAC F=.73 AUTHOR claim; Table 1 sentence precision.
6. Related field tokens: SMART, TIPSTER, SUMMAC, Luhn abstracts, Kupiec trainable summarizer.

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro → §2 Maximal Marginal Relevance (formula) → §3 Document Reordering (pilot) → §4 Summarization (SUMMAC + Table 1) → §5 Concluding Remarks → References |
| Figures | **None** (no paper figures / no XObjects) |
| Tables | **Table 1** (p.2): Sentence Precision — Document Percentage × λ vs TREC+CMU / CMU Relevant columns; Lead Sentences baselines — **AUTHOR-only** |
| Algorithms / math | **MMR def** (§2): Arg max_{Di∈R∖S} [ λ Sim₁(Di,Q) − (1−λ) max_{Dj∈S} Sim₂(Di,Dj) ] |
| Other | Cosine used as Sim for passage MMR in §4; suggested search strategy λ≈0.3 then λ≈0.7 after reformulation |

**Miss checklist:** both page PNGs opened; Table 1 headers/metrics understood from PNG+text; no appendix; no figures to miss; AUTHOR precision/F-score **not** treated as ours.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| §2 MMR def | introduces | λ-relevance–novelty linear combo | ESTABLISHED formula |
| λ=1 / λ=0 | qualifies | pure relevance vs maximal diversity extremes | ESTABLISHED semantics |
| §3 pilot | grounds | user preference for broad/interesting (MMR) | AUTHOR n=5 — unreproduced |
| §4 + cosine | implements | passage MMR for single/multi-doc summaries | ESTABLISHED use case |
| Table 1 | grounds | AUTHOR sentence precision @ 10%/25% × λ | unreproduced; no sig. Δ claimed |
| SUMMAC F=.73 | grounds | AUTHOR query-relevant summary utility | unreproduced; authors note non-definitive |
| §5 | qualifies | strongest story = multi-doc anti-redundancy | narrative |

## Pass 4 — Seed (1–5%)

**Observation:**

> Carbonell & Goldstein (SIGIR’98) define **Maximal Marginal Relevance** as the incremental selection  
> \(\mathrm{MMR} \stackrel{\mathrm{def}}{=} \arg\max_{D_i\in R\setminus S}\big[\lambda\,\mathrm{Sim}_1(D_i,Q)-(1-\lambda)\max_{D_j\in S}\mathrm{Sim}_2(D_i,D_j)\big]\),  
> with λ∈[0,1] trading relevance (λ→1) against novelty/diversity (λ→0). Sim₁ and Sim₂ may differ. This is Established literature mechanism for diversity-aware reranking and anti-redundant passage selection — not a claim about RQL syntax or our measured IR/summary quality.

**Interpretation for RQL:**

> Package surface `DIVERSIFY MMR` / algebra \(\mathrm{Diversify}_{mmr}(\lambda)\) as **Hypothesis packaging** of that Established formula: a post-retrieve (or post-fuse) plan node that greedily reorders an evidence list E under λ and chosen Sim₁/Sim₂ (often cosine / embedding similarity).  
> **Hard delineation:** AUTHOR Table 1 precision and SUMMAC F=.73 stay AUTHOR-only; do **not** invent RQL MMR gains; do **not** equate MMR with fusion (RRF/Condorcet/linear) — MMR diversifies *within* one ranked set; fusion merges *channels*.  
> Established: MMR formula + λ extremes + relevance–novelty intent. Hypothesis: RQL names, default λ, Sim choices, planner placement after Search/Fuse, and adapter execution.

**Evidence pointers:** §2 formula; λ=0/1 paragraph; §4 cosine passage use; Table 1 AUTHOR-only; §5 multi-doc claim.

**Anti-overclaim:** unreproduced precision/F/user-study %; n=5 pilot; SUMMAC params varied across systems (authors say indicative); 2-page short paper ≠ full empirical monograph; no claim we implement MMR in adapters yet.

**Uncertainty:** Exact Sim₁/Sim₂ in the reorder pilot unspecified beyond “standard ranking”; Table 1 column construction (TREC∪CMU vs CMU-only) partially compressed in OCR; ACM camera-ready vs CMU PDF line breaks.

## Pass 5 — Next queries

1. Optional: toy RQL grammar + LogicalPlan node for `DIVERSIFY MMR λ=…` (low-risk engineering)
2. Optional: modern neural MMR / embedding-Sim₂ variants if packaging needs depth
3. Optional: xQuAD / IA-Select / other diversity baselines for cite-chase contrast (not required for formula grounding)
4. Optional: Hellerstein OLA (queued from 0031) if AQP refine-vs-contract still needed
5. Human P0 FANNS / live adapter smoke remains blocked on Vijay (unchanged)

## Promote?

- [x] Journal 0033 + OKF `knowledge/reads/mmr-carbonell-sigir98/`
- [x] Thesis: brief §03 related-work MMR paragraph; §05 Diversify Established+Hypothesis; light abstract/apps/bib
- [x] Meta: NOTES / CHANGELOG / docs/06 / docs/07 / docs/08 / docs/references / journal index / knowledge README
- [ ] Do not invent MMR IR/summary metrics or treat Table 1 as ours
- [ ] Do not push
