# 0013 — MUVERA multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~22:57 IST (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source  
**Source:** Dhulipala, Hadian, Jayaram, Lee, Mirrokni — *MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings* — arXiv:2405.19504 (Google Research; preprint; NeurIPS’24 note in bib pending camera-ready verify)  
**URLs:** https://arxiv.org/abs/2405.19504 · https://arxiv.org/pdf/2405.19504.pdf  
**Local PDF:** `tooling/scripts/extract_out/muvera-2405.19504.pdf` (**26 pp**; arXiv v2 stamped 8 Jun 2026)  
**Extract dir:** `tooling/scripts/extract_out/muvera_2405/` (155 nodes / 109 edges; page PNGs under `page_renders/` all 26 pp)  
**OKF bundle:** [`../knowledge/reads/muvera-2405.19504/`](../knowledge/reads/muvera-2405.19504/)  
**Fallback note:** PDF **found** — Bruch continuum/fusion deferred (still open for Fuse_linear sibling).

---

## Context

ColBERT (0012) established MaxSim/late interaction. MUVERA is the Google Research reduction of **multi-vector Chamfer (= MaxSim-sum)** search to **single-vector MIPS** via Fixed Dimensional Encodings (FDEs), with optional Chamfer rerank — the natural RQL physical rewrite when a backend lacks native multi-vector search but has strong MIPS.

## Question asked

What is Chamfer vs ColBERT MaxSim, what are FDEs (construction + theorems), how does MUVERA’s two-stage pipeline contrast with PLAID’s multi-stage, and what is safe **[Established]** vs RQL rewrite packaging **[Hypothesis]**?

## Where we looked

- Known arXiv `2405.19504` (docs/06 §15)
- Local download + extract + relate
- Visual skim of `page_renders/page-01.png`…`page-26.png` (esp. Fig 1 PLAID vs MUVERA; Fig 2 FDE process; Figs 3–5 recall curves; Tables 1–4 appendix)
- Full text §1.1 Chamfer; §2 FDE; Theorems 2.1–2.2; §3 eval vs PLAID/SV heuristic; §4 conclusion

## Pass 1 — Skim

1. Multi-vector (ColBERT-family) retrieval is expensive vs single-vector MIPS.
2. MUVERA maps query/doc bags \(Q,P\) to FDEs \(F_q(Q), F_{doc}(P)\) s.t. \(\langle F_q(Q), F_{doc}(P)\rangle \approx \mathrm{CHAMFER}(Q,P)\).
3. \(\mathrm{CHAMFER}(Q,P)=\sum_{q\in Q}\max_{p\in P}\langle q,p\rangle\) — authors equate to ColBERT MaxSim.
4. Pipeline: build doc FDEs → MIPS (DiskANN) → Chamfer rerank top-\(K_c\) (Fig 1 vs PLAID 4-stage).
5. Theory: ε-approximations (Thm 2.1–2.2); empirics on BEIR vs PLAID / SV heuristic (AUTHOR).

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro (+1.1 Chamfer, 1.2 approach, 1.3 related); §2 FDEs (+2.1 theory); §3 Evaluation (3.1 offline FDE quality, 3.2 online/e2e); §4 Conclusion; appendices A–C (proofs, stats, ablations) |
| Figures | **Fig 1** MUVERA 2-step vs PLAID 4-stage; **Fig 2** FDE generation (SimHash partitions → blocks); **Fig 3** FDE recall vs dimension; **Fig 4** FDE vs brute Chamfer; **Fig 5** FDE vs SV heuristic; **Fig 6+** ball-carving / latency–recall (later pages) |
| Tables | **Table 1** FDE vs SV heuristic candidate counts; **Tables 2–4** variance / projection dims; dataset stats Fig 9 / appendix |
| Algorithms | Informal FDE construction (SimHash φ, fill_empty_clusters, repetitions, projections); MIPS via DiskANN; product quantization 32× |
| Equations | Chamfer def; FDE target \(\langle F_q(Q),F_{doc}(P)\rangle\approx\mathrm{CHAMFER}\); Thm 2.1–2.2 NCHAMFER ±ε |

**Miss checklist:** all 26 pages rendered; Fig 1–5 viewed; table captions understood (Recall@N, candidates, latency); appendix figures included in render set; extract table count inflated (85) — prefer visual + prose.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| §1.1 Chamfer | equates | ColBERT MaxSim-sum | same operator, different name |
| Fig 1 | contrasts | MUVERA 2-stage vs PLAID multi-stage | rewrite lineage |
| §2 + Fig 2 | introduces | FDE via SimHash partitions | core mechanism |
| Thm 2.1–2.2 | grounds | ε-approx + approx NNS | theory (not our proof check) |
| Fig 5 / Table 1 | grounds | AUTHOR: fewer candidates than SV heuristic | unreproduced |
| §3.2 | implements | DiskANN MIPS + Chamfer rerank + PQ | physical engine |
| PLAID cite [43] | cites-sideways | Santhanam PLAID | middle rewrite (unread) |

## Pass 4 — Seed (1–5%)

**Observation:**

> MUVERA reduces multi-vector retrieval under Chamfer similarity \(\sum_{q\in Q}\max_{p\in P}\langle q,p\rangle\) (ColBERT MaxSim) to single-vector MIPS by asymmetrically encoding bags into Fixed Dimensional Encodings whose inner product approximates Chamfer. Construction partitions space (SimHash / optional k-means), fills empty clusters, concatenates repetitions/projections to dimension \(d_{\mathrm{FDE}}=B\cdot d_{\mathrm{proj}}\cdot R_{\mathrm{reps}}\). Retrieval: MIPS over doc FDEs (authors: DiskANN) then **one** Chamfer/MaxSim rerank stage — simpler than PLAID’s multi-stage centroid pipeline. Authors prove ε-approximations (Thm 2.1–2.2) and report BEIR recall/latency gains vs PLAID and better candidate efficiency vs the SV heuristic — **AUTHOR numbers only**.

**Interpretation for RQL:**

> Treat Chamfer≡MaxSim-sum as already **[Established]** via ColBERT Eq. 3 + MUVERA §1.1 terminology bridge. Treat **FDE reduction + MIPS + MaxSim rerank** as **[Established]** literature mechanism for a physical rewrite, but RQL rule \(\mathrm{Search}_{late}\Rightarrow\mathrm{FDE\_ANN}+\mathrm{MAXSIM\_RERANK}\) (and ColBERT→PLAID→MUVERA ladder) as **[Hypothesis]** compile targets / capability negotiation. Do **not** cite author “10% recall / 90% latency” as our measurement.

**Evidence pointers:** §1.1 Chamfer; Fig 1–2; §2; Thm 2.1–2.2; Fig 5; §3.2 DiskANN+PQ.

**Anti-overclaim:** unreproduced BEIR/PLAID comparisons; FDE randomness (variance claimed small); NeurIPS venue stamp still provisional in bib; PLAID not multimodally re-read; not every MIPS backend equals DiskANN.

**Uncertainty:** arXiv v2 date stamp “8 Jun 2026” vs original May 2024 posting; camera-ready NeurIPS page numbers; exact default \((R_{\mathrm{reps}},k_{\mathrm{sim}},d_{\mathrm{proj}})\) for production.

## Pass 5 — Next queries

1. PLAID multimodal (centroid interaction stages) to firm middle rewrite
2. Bruch et al. arXiv:2210.11934 for Fuse_linear / CC (still open)
3. Vendor FDE / multi-vector support matrix for capability profiles
4. Optional: DESSERT / other MV retrieval cite-chase from MUVERA related work
5. Tiny harness: deterministic MaxSim on toy embeddings (optional; this session)

## Promote?

- [x] Thesis optimizer rewrite: late → FDE_ANN + MaxSim rerank **[Hypothesis]**; cite MUVERA mechanism
- [x] OKF `knowledge/reads/muvera-2405.19504/`
- [ ] Do not invent new FDE math in RQL
