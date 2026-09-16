# 0017 — Chen et al. ECIR’22 multimodal re-read (Pass 1–5) — RRF-vs-CC cite-chase

**Date:** 2026-09-16 ~23:35 IST (Europe/Dublin)  
**Type:** multimodal source read (cite-chase from Bruch [5])  
**Status:** Pass 1–5 complete for this source  
**Source:** Chen, Zhang, Lu, Bendersky, Najork — *Out-of-Domain Semantics to the Rescue! Zero-Shot Hybrid Retrieval Models* — ECIR 2022 (LNCS), pp. 95–110  
**URLs:** https://arxiv.org/abs/2201.10582 · https://arxiv.org/pdf/2201.10582 · DOI [10.1007/978-3-030-99736-6_7](https://doi.org/10.1007/978-3-030-99736-6_7) · author PDF https://marc.najork.org/papers/ecir2022.pdf  
**Local PDF:** `tooling/scripts/extract_out/chen-ecir2022-2201.10582.pdf` (**16 pp**, arXiv v1)  
**Extract dir:** `tooling/scripts/extract_out/chen_ecir2022/` (47 nodes / 86 edges; 4 embedded figs; tables via pdfplumber+pymupdf; `page_renders/page-01..16.png`)  
**OKF bundle:** [`../knowledge/reads/chen-ecir2022-2201.10582/`](../knowledge/reads/chen-ecir2022-2201.10582/)  
**Cite-chase of:** Bruch et al. reference **[5]** (journal 0016)

---

## Context

Bruch (journal 0016) reported TM2C2 beating default RRF(\(\eta=60\)) on NDCG on their suite and explicitly **disagreed with Chen et al.** on RRF vs convex/linear score fusion. Goal this turn: identify and multimodal-read that Chen paper; resolve what the disagreement actually is (setup / metric / method), then write a thesis planner-policy subsection without inventing metrics.

## Question asked

What does Chen et al. claim about **RRF vs linear interpolation (CC)**, on what evidence, and how should RQL’s \(\mathrm{Fuse}_{rrf}\) vs \(\mathrm{Fuse}_{linear}\) preference be stated once both AUTHOR suites are in view?

## Where we looked

- Bruch bibliography [5] (pdftotext refs pp. 26–27 of arXiv:2210.11934)
- WebSearch → arXiv:2201.10582; Springer DOI 10.1007/978-3-030-99736-6_7; Najork author PDF
- `curl` arXiv PDF + `extract_document.py` + `relate_components.py`
- Visual skim of all 16 page PNGs (focus: Eq. 1; Fig 1–2; Tables 1–5; §3.1, §5.4, §6 Discussion)
- Cross-check with Bruch Table 2 / Fig 5 claims (journal 0016)

## Pass 1 — Skim

1. Zero-shot hybrid retrieval: train deep (NPR) on MS-MARCO; apply OOD without fine-tuning.
2. Lexical (BM25 ± Bo1 / docT5query) more robust under domain shift; deep deteriorates on large shift (esp. TREC-COVID).
3. Fuse channels with **RRF** (Cormack \(k=60\)) — **non-parametric**, rank-only — for zero-shot applicability.
4. Explicitly reject score **linear interpolation** for their zero-shot goal: sensitive to scales/weights; needs normalisation + \(\alpha\) tuning.
5. §6 case study: min-max normalised \(s=\alpha s_{\mathrm{BM25}}+(1-\alpha)s_{\mathrm{NPR}}\) even at best \(\alpha\) **underperforms** RRF(BM25, NPR) by ~**3% relative Recall@1K** on Robust04 and TREC-COVID (Fig 2).
6. Primary metric: **Recall@1K** (first-stage); also MAP. Not NDCG-focused like Bruch.

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro (typo “Introduciton”); §2 Related; §3 Method (3.1 hybrid/RRF, 3.2 lexical+expansions, 3.3 NPR deep); §4 Setup (datasets Table 1, lexical configs Table 2); §5 Evaluation (5.1 generalisation, 5.2 expansion, 5.3 complementarity, 5.4 hybrid); §6 Discussion (interpolation vs RRF; query-length Table 5); §7 Conclusion; References |
| Figures | **Fig 1** Venn unique relevant docs — Bo1 / docT5query / NPR (Robust04, TREC-COVID); **Fig 2** Recall@1K vs \(\alpha\) — interpolation curve vs RRF(BM25,NPR) solid vs full RRF dashed vs oracle dotted (Robust04, TREC-COVID) |
| Tables | **Table 1** five datasets (MS-MARCO pass/doc; ORCAS; Robust04; TREC-COVID); **Table 2** best lexical setups (index/query/fk/#expansions); **Table 3** in-domain R@1K/MAP BM25/Bo1/docT5/NPR/RRF variants; **Table 4** OOD same; **Table 5** ORCAS R@1K by query length |
| Algorithms | None numbered; RRF Eq. (1); sliding-window passage scoring for docs |
| Equations | **(1)** \(\mathrm{RRF}(q,d,M)=\sum_{m\in M} 1/(k+\pi_m(q,d))\), \(k=60\); linear case study \(s(d)=\alpha s_{\mathrm{BM25}}+(1-\alpha)s_{\mathrm{NPR}}\) (§6) |

**Miss checklist:** all 16 pages rendered and opened; Fig 1–2 captions + axes understood (Recall@1K vs \(\alpha\)); Tables 1–5 headers understood (R@1K / MAP); pdfplumber table CSVs lossy — recovered via page PNGs + pdftotext; embedded figure XObjects are four panel images on p.11 (Venn + curves).

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| Eq. (1) | implements | zero-shot hybrid fuse | Cormack RRF, \(k=60\) |
| §3.1 | qualifies | linear score interpolation | rejected for zero-shot (scale/weight sensitivity) |
| Fig 1 | grounds | channel complementarity | AUTHOR Venn |
| Tables 3–4 | grounds | RRF hybrids beat singles (R@1K) | AUTHOR; paired t-test claims |
| Fig 2 + §6 | grounds | best min-max linear \(\alpha\) < RRF(BM25,NPR) ~3% rel. | AUTHOR; **core of Bruch disagreement** |
| Table 5 | qualifies | NPR vs BM25 by query length | short→NPR; long→lexical |
| Bruch [5] cite | cites-sideways | this paper | Bruch claims opposite winner on NDCG/TM2C2 |

## Pass 4 — Seed (1–5%)

**Observation:**

> Chen et al. (ECIR’22) build a **zero-shot** hybrid of lexical (+expansion) and deep (NPR) channels fused by **RRF** (\(k=60\)). They argue score **linear interpolation** needs min-max normalisation and \(\alpha\) tuning that does not transfer zero-shot; on Robust04 and TREC-COVID their best-tuned min-max linear BM25+NPR still underperforms RRF(BM25, NPR) by about **3% relative Recall@1K** (Fig 2), with larger gaps vs full multi-channel RRF. Primary metric is first-stage **Recall@1K** (plus MAP), not NDCG.

**Interpretation for RQL (resolve Bruch disagreement):**

> The Chen↔Bruch “conflict” is an **ESTABLISHED literature disagreement of setups**, not a single false claim: (i) **metric** — Chen Recall@1K / MAP vs Bruch NDCG; (ii) **linear method** — Chen simple min-max \(\alpha\)-interp of BM25+NPR vs Bruch **TM2C2** (\(\phi_{\mathrm{tmm}}\) + \(\alpha\), often 0.8) against default RRF(60); (iii) **objective** — Chen optimises zero-shot / no labels vs Bruch shows \(\alpha\) is sample-efficient when a small labeled set exists; (iv) **channels/datasets** differ (NPR+expansions / Robust04–COVID vs MiniLM+BM25 / BEIR-style).  
> **Planner rule [Hypothesis]:** prefer \(\mathrm{Fuse}_{rrf}\) when scores incomparable or **no** calibrated labeled set (Chen-style zero-shot portability); prefer \(\mathrm{Fuse}_{linear}\) (TM2C2-class \(\phi\)) when comparable scores + small labels exist and early-precision/NDCG-style quality is the contract (Bruch-style); escalate \(\mathrm{Fuse}_{ltr}\) when multi-feature learning is justified. Do **not** declare a universal empirical winner.

**Evidence pointers:** Eq. (1); §3.1; Fig 2; Tables 3–4; §6; cross: Bruch Fig 5 / Table 2 / §7 (journal 0016).

**Anti-overclaim:** unreproduced Chen R@1K/MAP or Bruch NDCG; not “RRF always beats CC” or vice versa; Chen’s linear baseline ≠ Bruch TM2C2; first-stage recall ≠ RAG end-to-end answer quality.

**Uncertainty:** Springer proceedings pagination matches Bruch’s “95–110” (DOI chapter `_7`); arXiv PDF is **16 pp** preprint layout (not LNCS page images); NPR training details not re-implemented; exact Fig 2 numeric peaks read from curves + text (±3% relative) not digitised.

## Pass 5 — Next queries

1. Montague–Aslam Condorcet Fuse (Cormack’s pairwise-majority comparator) — short multimodal if PDF short
2. FANNS survey Lin 2025 taxonomy figures (still open from 0016 queue)
3. Vendor weighted-linear / hybrid APIs vs TM2C2 \(\phi\) (Qdrant, ES, Weaviate, Milvus)
4. Optional: Wang et al. / Gao et al. score-interpolation hybrids Chen cites as prior linear practice
5. Optional: per-query \(\alpha\) / query-length features → \(\mathrm{Fuse}_{ltr}\) literature pointer (Chen §6/§7 future work)

## Promote?

- [x] Journal 0017 + OKF `knowledge/reads/chen-ecir2022-2201.10582/`
- [x] Thesis: short \(\mathrm{Fuse}_{rrf}\) vs \(\mathrm{Fuse}_{linear}\) preference subsection (Established disagreement → Hypothesis planner rule)
- [x] Meta: NOTES / CHANGELOG / docs/06 / docs/references / journal index
- [ ] Do not invent fusion math or fake RAG metrics
