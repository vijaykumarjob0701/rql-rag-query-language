# 0016 — Bruch et al. fusion multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~23:25 IST (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source  
**Source:** Bruch, Gai, Ingber — *An Analysis of Fusion Functions for Hybrid Retrieval* — ACM TOIS (2023); arXiv:2210.11934v2 (4 May 2023)  
**URLs:** https://arxiv.org/abs/2210.11934 · https://arxiv.org/pdf/2210.11934 · DOI 10.1145/3596512 · Pinecone research page  
**Local PDF:** `tooling/scripts/extract_out/bruch-arxiv-2210.11934.pdf` (**36 pp**)  
**Extract dir:** `tooling/scripts/extract_out/bruch_2210/` (181 nodes / 283 edges; 81 figure XObjects; 13 tables; full `page_renders/page-01..36.png`)  
**OKF bundle:** [`../knowledge/reads/bruch-arxiv-2210.11934/`](../knowledge/reads/bruch-arxiv-2210.11934/)  
**Prior hand-off:** journal `0015` remains a seed note only (not a Pass 1–5).

---

## Context

After Cormack RRF (`0011`) established \(\mathrm{Fuse}_{rrf}\) and the ColBERT→PLAID→MUVERA ladder filled late-interaction (`0012`–`0014`), `0015` queued **Bruch** for a full multimodal pass on convex/linear fusion vs RRF — only if the PDF was rich enough. PDF found (36 pp TOIS/arXiv); inventory is dense (Figs 1–20 + Tables 1–8 + appendices A–D).

## Question asked

What does Bruch et al. establish about **convex combination (CC / TM2C2)** vs **RRF** (parameter sensitivity, normalization, sample efficiency, in-/out-of-domain), and what is safe to mark **[Established]** for \(\mathrm{Fuse}_{linear}\) / \(\mathrm{Fuse}_{ltr}\) sibling delineation vs RQL packaging **[Hypothesis]**?

## Where we looked

- WebSearch → arXiv:2210.11934 / DOI 10.1145/3596512 (ACM TOIS)
- `docs/06-deep-literature.md` §12 + `docs/references.md` #72
- Local download + `extract_document.py` + `relate_components.py`
- Visual skim of all 36 page PNGs (focus: Figs 1–3, 5–8, 11–12; Tables 1–4; §4–§7)
- Full text Eqs. (2)–(5), (7)–(8), (10); Conclusion

## Pass 1 — Skim

1. Hybrid retrieval = fuse lexical + semantic ranked lists / scores.
2. Main objects: **convex combination** \(f_{\mathrm{Convex}}=\alpha\,\phi_{\mathrm{Sem}}(f_{\mathrm{Sem}})+(1-\alpha)\,\phi_{\mathrm{Lex}}(f_{\mathrm{Lex}})\) and **RRF** \(1/(\eta+\pi_{\mathrm{Lex}})+1/(\eta+\pi_{\mathrm{Sem}})\).
3. Authors’ preferred practical CC: **TM2C2** = theoretical min–max normalization + convex combo; often \(\alpha\approx 0.8\) in-domain.
4. Claims vs prior (Chen et al.): RRF is **parameter-sensitive**; CC learning is largely **normalization-agnostic** among monotone \(\phi\); **CC beats RRF** in-domain and zero-shot OOD on their suite; CC is **sample-efficient** (<~5% train queries).
5. Desiderata (§6): monotonicity, homogeneity, boundedness, Lipschitz continuity / score-distribution preservation, interpretability/sample efficiency.
6. Appendices A–D: same fusion analysis on Splade/Tas-B/MiniLM pairings (generality beyond BM25+MiniLM).

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro; §2 Related; §3 Setup (notation, datasets Table 1, empirics); §4 CC analysis (4.1 suitability, 4.2 normalization); §5 RRF analysis (5.1 parameters, 5.2 Lipschitz / SRRF); §6 Discussion (desiderata); §7 Conclusion; Refs; Apps A–D |
| Figures | **Fig 1** Lex×Sem TMM score scatter (pos/neg) — complementarity; **Fig 2** \(f_{\mathrm{Convex}}\) heatmaps \(\alpha=0.6/0.8\); **Fig 3** NDCG vs \(\alpha\) under 6 normalizations; **Fig 4** relative expansion \(\lambda\); **Fig 5** \(\Delta\)NDCG TM2C2−RRF vs \(\alpha\); **Fig 6** reciprocal-rank scatters; **Fig 7–8** RRF \(\eta_{\mathrm{Lex}},\eta_{\mathrm{Sem}}\) heatmaps/effect; **Fig 9–10** SRRF vs RRF; **Fig 11** unnormalized CC vs pure Sem; **Fig 12** sample-efficiency curves TM2C2 vs parameterized RRF/RRF-CC; **Figs 13–20** appendix fusion pairs |
| Tables | **Table 1** datasets (MS MARCO, NQ, Quora in-domain; NFCorpus, HotpotQA, FEVER, SciFact, DBPedia, FiQA zero-shot); **Table 2** primary Recall/NDCG Lex/Sem/TM2C2(\(\alpha{=}0.8\))/RRF(\(\eta{=}60\))/Oracle; **Table 3** parameterized RRF; **Table 4** TM2C2 vs RRF vs SRRF; **Tables 5–8** appendix model pairs |
| Algorithms | None numbered; procedural: union set \(\mathrm{U}_k(q)\), fill missing scores, fuse, reorder |
| Equations | (2) \(\phi_{\mathrm{mm}}\); (3) \(f_{\mathrm{Convex}}\); (4) \(\phi_{\mathrm{tmm}}\); (5) \(\phi_{\mathrm{z}}\); (7)–(8) RRF / two-\(\eta\); (9) SRRF smooth approx; (10) RRF-CC |

**Miss checklist:** all 36 pages rendered and opened; figure captions + Table 2/4 headers understood (Recall/NDCG@1000, @100 on SciFact/NFCorpus); appendix Figs 13–20 + Tables 5–8 included as inventory (not every cell transcribed); extract table CSVs are lossy — recovered via page PNGs + full_text.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| Eq. (3)+(4) | introduces | TM2C2 | preferred CC instantiation |
| Fig 1 | grounds | Lex+Sem complementarity | AUTHOR visualization |
| Fig 3 | grounds | normalization largely reconstructible | AUTHOR; identity \(I\) bad |
| Table 2 + Fig 5 | grounds | TM2C2 > RRF(60) NDCG (their suite) | AUTHOR; disagree with Chen et al. |
| Eq. (8) + Fig 7 | grounds | RRF parametric / sensitive | AUTHOR |
| Fig 9–10 + Table 4 | grounds | smoother SRRF helps vs RRF | Lipschitz intuition |
| Fig 12 | grounds | TM2C2 sample-efficient | AUTHOR <~5% train |
| §6 | qualifies | fusion desiderata | design principles |
| §7 | cites-sideways | Chen et al. [5] disagreement | RRF-vs-CC literature conflict |

## Pass 4 — Seed (1–5%)

**Observation:**

> Bruch et al. analyze hybrid fusion as (i) a **convex combination of normalized channel scores** \(f_{\mathrm{Convex}}=\alpha\phi_{\mathrm{Sem}}(f_{\mathrm{Sem}})+(1-\alpha)\phi_{\mathrm{Lex}}(f_{\mathrm{Lex}})\) — especially **TM2C2** with theoretical min–max \(\phi_{\mathrm{tmm}}\) — versus (ii) **RRF** on ranks \(1/(\eta+\pi)\). On their BEIR-style suite they report TM2C2 (\(\alpha=0.8\) tuned in-domain) beating default RRF (\(\eta=60\)) on NDCG in-domain and zero-shot; argue RRF is multi-parameter and sensitive; argue monotone normalizations are largely interchangeable for CC (unlike raw unnormalized scores); and show \(\alpha\) tunes sample-efficiently. They also propose fusion **desiderata** (monotonicity, homogeneity, boundedness, Lipschitz/score-preservation, sample efficiency).

**Interpretation for RQL:**

> Mark **CC / linear score fusion formulas + normalization role + RRF-vs-CC delineation as literature mechanisms** **[Established]** for sibling operators \(\mathrm{Fuse}_{linear}(\alpha)\) (and \(\mathrm{Fuse}_{ltr}\) as the learned/multi-parameter end of the continuum). Keep Cormack \(\mathrm{Fuse}_{rrf}\) as the **rank-only portable default** when scores are incomparable **[Established]** (journal 0011). Treat **planner policy** “prefer linear/CC when calibrated scores + small labeled set exist; else RRF” as **[Hypothesis]**. Do **not** treat Bruch NDCG/Recall tables or “CC always beats RRF” as our reproduced RAG metrics **[Provisional / AUTHOR-only]** — their disagreement with Chen et al. is itself a literature signal.

**Evidence pointers:** Eqs. (2)–(5), (7)–(8), (10); Figs 1, 3, 5, 7, 12; Tables 2, 4; §6–§7.

**Anti-overclaim:** unreproduced BEIR numbers; not proof CC wins on every vendor hybrid stack; not a full LTR model (single \(\alpha\) ≠ LambdaMART); \(\alpha\in[0.6,0.8]\) is AUTHOR suggestion not sacred; appendices pairings still AUTHOR-only.

**Uncertainty:** exact TOIS volume/issue/pages (DOI verified; arXiv PDF used for pages); whether product “linear fusion” matches \(\phi_{\mathrm{tmm}}\) vs \(\phi_{\mathrm{mm}}\); Chen et al. [5] not re-read this turn.

## Pass 5 — Next queries

1. Chen et al. hybrid retrieval claim that RRF beats CC (cite-chase; resolve disagreement)
2. Montague–Aslam Condorcet Fuse CIKM 2002 (short multimodal if PDF short)
3. FANNS survey Lin 2025 arXiv:2505.06501 taxonomy figures
4. Vendor linear-fusion / weighted score APIs (Qdrant, ES, Milvus) vs Bruch \(\phi\)
5. Optional: tiny LTR / learned fuse literature pointer for \(\mathrm{Fuse}_{ltr}\) beyond single-\(\alpha\)

## Promote?

- [x] Thesis: strengthen Fuse_linear / Fuse_ltr vs Fuse_rrf with Established vs Hypothesis labels + related-work Bruch paragraph
- [x] OKF bundle `knowledge/reads/bruch-arxiv-2210.11934/`
- [x] Optional harness: weighted linear fusion on fixed toy scores (real output only)
- [ ] Do not invent RQL-specific fusion math beyond packaging
