# 0012 — ColBERT multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~22:57 IST (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source  
**Source:** Khattab & Zaharia — *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT* — SIGIR ’20  
**URLs:** https://arxiv.org/abs/2004.12832 · https://arxiv.org/pdf/2004.12832.pdf · ACM DOI 10.1145/3397271.3401075  
**Local PDF:** `tooling/scripts/extract_out/colbert-sigir20.pdf` (**10 pp**; arXiv v2 4 Jun 2020)  
**Extract dir:** `tooling/scripts/extract_out/colbert_sigir20/` (78 nodes / 196 edges; 17 tiny XObject images — main Figs 1–3 are vector graphics; page PNGs under `page_renders/`)  
**OKF bundle:** [`../knowledge/reads/colbert-sigir20/`](../knowledge/reads/colbert-sigir20/)

---

## Context

After FilterExec (ACORN / VBASE / Filtered-DiskANN) and Fuse_rrf (Cormack), the algebra still had `Search_late` as a thin leaf. ColBERT is the primary source for **late interaction / MaxSim** as established IR mechanism; PLAID/MUVERA are later physical rewrites (MUVERA = journal 0013).

## Question asked

What exactly is late interaction and MaxSim (formula, similarity metrics, pruning story), which figures/tables ground the quality–cost claim, and what is safe to mark **[Established]** for RQL vs packaging/`Search_late` naming **[Hypothesis]**?

## Where we looked

- Known arXiv PDF `2004.12832` (docs/06 §13; bib already present)
- Local download + `extract_document.py` + `relate_components.py`
- Visual skim of rendered `page_renders/page-01.png` … `page-10.png` (all 10 pages; Figs 1–3 and Tables 1–2 viewed)
- Full text §3.1–3.6 (architecture, encoders, late interaction Eq. 3, indexing, re-rank, end-to-end faiss); §4 empirics

## Pass 1 — Skim

1. SIGIR’20 long paper (10 pp): BERT-based **late interaction** ranking bridging cross-encoder quality and representation-model cost.
2. Independent query/document encoders → bags of contextualized embeddings; relevance = **sum of MaxSim** over query embeddings vs document bag.
3. Document embeddings offline-indexable; interaction is pruning-friendly → re-rank **and** end-to-end retrieval via faiss IVFPQ.
4. Empirics on MS MARCO + TREC CAR; Fig 1 quality–latency Pareto; Tables 1–2 re-rank vs end-to-end.
5. Ablation (§4.4): late interaction / MaxSim / query augmentation matter for effectiveness.

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro; §2 Related; §3 ColBERT (3.1 Architecture, 3.2 Encoders, 3.3 Late Interaction, 3.4 Indexing, 3.5 Re-ranking, 3.6 End-to-end); §4 Eval (4.1–4.5); refs |
| Figures | **Fig 1** MRR@10 vs latency (log) on MS MARCO; **Fig 2** four matching paradigms (a representation / b interaction / c all-to-all BERT / **d late interaction + MaxSim**); **Fig 3** ColBERT architecture \(f_Q\), \(f_D\), MaxSim, Σ, offline indexing bracket |
| Tables | **Table 1** re-rank MS MARCO MRR@10 + latency + FLOPs; **Table 2** end-to-end MRR + Recall@50/200/1000 + latency; further ablations/space in §4.4–4.5 (viewed in page renders) |
| Algorithms | Informal procedures (offline index; two-stage e2e with faiss) — no numbered Alg. |
| Equations | (1)(2) encoder bags \(E_q, E_d\); **(3)** \(S_{q,d}=\sum_i \max_j E_{q_i}\cdot E_{d_j}^\top\) (cosine via L2-normalized dots; also evaluate squared L2) |

**Miss checklist:** all 10 pages opened as PNG; Fig 1–3 captions understood; Table 1–2 headers (MRR@10, latency ms, FLOPs, Recall@k) understood; extract XObjects are decorative (arrows/icons) — **figures recovered via page renders**; appendix: none beyond refs.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| Fig 2(d) + §3.1 | introduces | late interaction + MaxSim | paradigm vs (a)(b)(c) |
| Eq. (3) | implements | \(S_{q,d}\) MaxSim-sum | ESTABLISHED scoring |
| Fig 3 | grounds | offline \(f_D\) + online \(f_Q\) + MaxSim | indexing story |
| §3.6 | implements | faiss IVFPQ candidate gen → exhaustive MaxSim refine | e2e physical sketch |
| Table 1 | grounds | AUTHOR quality–cost vs BERT re-rankers | unreproduced here |
| Table 2 | grounds | AUTHOR e2e MRR/Recall vs BM25/doc2query/… | unreproduced |
| §4.4 | qualifies | MaxSim / query aug / late interact essential | ablation |

## Pass 4 — Seed (1–5%)

**Observation:**

> ColBERT encodes query and document into bags of contextualized BERT embeddings (\(E_q\), \(E_d\)), then scores relevance by **late interaction**: \(S_{q,d}=\sum_{i\in[|E_q|]}\max_{j\in[|E_d|]} E_{q_i}\cdot E_{d_j}^\top\) (Eq. 3; cosine via unit L2 norms; squared L2 also evaluated). Document bags are computed offline; MaxSim is cheap and pruning-friendly, enabling (i) fast re-ranking of BM25 candidates and (ii) end-to-end retrieval via vector-similarity indexes (authors use faiss IVFPQ) followed by exact MaxSim refinement. Authors report competitive MS MARCO MRR@10 vs BERT re-rankers at orders-of-magnitude lower latency/FLOPs (Tables 1–2; Fig 1) — **AUTHOR numbers only**.

**Interpretation for RQL** (`[hypothesis]` for packaging):

> Mark **MaxSim / late-interaction scoring (Eq. 3)** and the independent-encoder + offline document bag pattern as **[Established]** prior art for logical leaf \(\mathrm{Search}_{late}(q,k)\). Keep RQL naming (`SEARCH LATE_INTERACT` / `COLBERT`), plan IR placement, and compile targets as **[Hypothesis]**. Physical rewrite chain (ColBERT exhaustive/faiss → PLAID centroid prune → MUVERA FDE+MIPS) is **[Hypothesis]** compile policy (PLAID not multimodally read this pass; MUVERA = 0013). Do **not** treat ColBERT MRR/latency tables as our reproduced RAG metrics.

**Evidence pointers:** Fig 2(d), Fig 3; Eq. (3); §3.5–3.6; Tables 1–2; §4.4 ablation.

**Anti-overclaim:** unreproduced MS MARCO/TREC CAR numbers; not a claim every backend ships multi-vector; Eq. 3 uses sum-of-max — not average-of-max; faiss IVFPQ params are author config not universal; paper predates ColBERTv2/PLAID/MUVERA.

**Uncertainty:** ACM camera-ready pagination vs arXiv 10 pp; “CNN” in Eqs (1)(2) vs prose “linear layer” (author notation); exact ACM proceedings page range (DOI present).

## Pass 5 — Next queries

1. MUVERA FDE multimodal (queued as 0013) — rewrite \(\mathrm{Search}_{late}\Rightarrow\mathrm{FDE\_ANN}+\mathrm{MaxSim\_rerank}\)
2. PLAID (Santhanam et al., arXiv:2205.09707) centroid interaction + pruning — middle rewrite
3. ColBERTv2 (Santhanam et al.) denoised supervision / residual compression cite-chase
4. Vendor multi-vector / late_interaction APIs (Turbopuffer, TopK, Weaviate multi-vector) vs Eq. 3 semantics
5. Optional: Bruch still open for Fuse_linear sibling

## Promote?

- [x] Thesis: MaxSim/late interaction **[Established]**; `Search_late` leaf + ColBERT→PLAID→MUVERA rewrite **[Hypothesis]**
- [x] OKF bundle under `knowledge/reads/colbert-sigir20/`
- [ ] Not inventing a new MaxSim formula — do not alter Eq. 3
