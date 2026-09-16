# 0011 — Cormack et al. RRF multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~22:55 IST (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source  
**Source:** Cormack, Clarke, Büttcher — *Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods* — SIGIR 2009 (Boston), pp. 758–759  
**URLs:** https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf · ACM DOI 10.1145/1571941.1572114 · Google Research pubs page  
**Local PDF:** `tooling/scripts/extract_out/cormack-sigir09-rrf.pdf` (**2 pp**)  
**Extract dir:** `tooling/scripts/extract_out/rrf_cormack_sigir09/` (9 nodes / 6 edges; no XObject figures — tables are body text; page PNGs under `page_renders/`)  
**OKF bundle:** [`../knowledge/reads/rrf-cormack-sigir09/`](../knowledge/reads/rrf-cormack-sigir09/)

---

## Context

After ACORN / VBASE / Filtered-DiskANN grounded **FilterExec** physical modes (journals 0006, 0009, 0010), Pass 5 of 0010 queued the classic **RRF** paper as the next multimodal read. Product RAG stacks (Qdrant, Milvus, ES/OS, Redis, Turbopuffer, pgvector SQL CTEs) already ship RRF; this pass locks the **formula + prior-art status** for `Fuse_rrf` without inventing new fusion math.

## Question asked

What exactly does Cormack et al. define as RRF (score, \(k\), rank semantics), what evidence do Tables 1–3 give vs Condorcet / CombMNZ / LTR, and what is safe to mark **[Established]** for RQL vs what remains RQL-specific packaging?

## Where we looked

- WebSearch → author PDF `cormack.uwaterloo.ca/cormacksigir09-rrf.pdf`
- Local download + `extract_document.py` + `relate_components.py`
- Visual skim of rendered page-01 / page-02 PNGs (both pages; tables viewed)
- Full text §1 formula + pilots; §2 Discussion; references [1]–[6]

## Pass 1 — Skim

1. Short SIGIR’09 poster/short paper (2 pages): unsupervised **rank fusion** baseline that unexpectedly beat stronger methods.
2. Core formula: \(\mathrm{RRFscore}(d)=\sum_{r\in R} 1/(k+r(d))\) with **\(k=60\)** fixed after pilot (choice “not critical”).
3. Compares to **Condorcet Fuse** (pairwise majority) and **CombMNZ** (score-dependent + cutoff).
4. Empirics: Wumpus pilots (Table 1), TREC run fusion (Table 2), LETOR 3 meta-learner fusion (Table 3).
5. Discussion: rank-only (no score calibration), streaming/summable one ranking at a time, diversity conjecture vs Condorcet.

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Reciprocal Rank Fusion; §2 Discussion; References |
| Figures | **None** (confirmed visually + extract: 0 image XObjects) |
| Tables | **Table 1** pilot \(k\) sweep MAP on TREC 351–400 (30 Wumpus configs) + Best/Condorcet/CombMNZ; **Table 2** TREC Robust / 3 / 5 / 9 fusion MAPs; **Table 3** LETOR 3 RRF vs Condorcet/CombMNZ/ListNet/LGD/AdaRank/RankSVM/RankBoost |
| Algorithms | Informal score defs only (RRF, Condorcet relation, CombMNZ) — no numbered Alg. |
| Equations | RRF sum; CombMNZ product-of-hits × score sum |

**Miss checklist:** both pages opened and viewed as PNG; table captions + headers understood (MAP); no appendix; extract missed structured table files (tables are typeset in body — recovered via full_text + visual).

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| §1 formula | introduces | \(\mathrm{RRFscore}\), \(k=60\) | portable default |
| Table 1 | grounds | “\(k\) near-optimal, not critical” | AUTHOR MAP sweep |
| Table 2 | grounds | RRF ≥ Condorcet on listed TREC sets | AUTHOR; CombMNZ wins TREC 3 |
| Table 3 | grounds | RRF > listed LTR individuals; CombMNZ edges RRF (n.s.) | AUTHOR; meta-learner claim |
| §2 | qualifies | CombMNZ needs calibrated \(s_r\); higher variance | why rank-only fusion |
| §2 | cites-sideways | Montague–Aslam Condorcet (CIKM’02) | fusion lineage |

## Pass 4 — Seed (1–5%)

**Observation:**

> Reciprocal Rank Fusion ranks documents by \(\sum_r 1/(k+r(d))\) over input rankings. With \(k=60\) fixed after a pilot, the method is unsupervised, **score-free** (uses ranks only), and incrementally summable. On the authors’ TREC fusion and LETOR 3 experiments, RRF matched or beat Condorcet Fuse and often beat the best individual run / LTR baselines; CombMNZ occasionally edges RRF when scores are available. Authors report ~4–5% average MAP gains vs Condorcet/CombMNZ/best in their pilot+TREC suite (sign tests), and argue RRF harnesses ranking diversity better than majority Condorcet.

**Interpretation for RQL** (`[hypothesis]` only for packaging):

> Mark mathematical RRF + default \(k=60\) as **[Established]** IR prior art for logical operator \(\mathrm{Fuse}_{rrf}(k_{\mathrm{rrf}})\). Keep RQL *naming*, plan IR placement, and vendor compile targets as **[Hypothesis]**. Prefer RRF as the portable hybrid default when channel scores are incomparable; expose \(\mathrm{Fuse}_{linear}\) / learned fuse when calibrated scores exist (Bruch-style — separate read). Do **not** treat Cormack MAP tables as our reproduced RAG metrics.

**Evidence pointers:** §1 formula; Table 1–3; §2 Discussion; refs [4] Condorcet, CombMNZ lineage.

**Anti-overclaim:** unreproduced TREC/LETOR numbers; not proof RRF always beats linear/CC on modern dense+BM25 RAG; not a learned fuse; \(k=60\) is conventional not sacred; paper is 2 pp short form.

**Uncertainty:** exact ACM front-matter page layout vs author PDF; Buettcher spelling (Büttcher / Buettcher); whether product “RRF” implementations use 0- vs 1-based ranks (paper: rank permutation on \(1..|D|\)).

## Pass 5 — Next queries

1. Bruch et al. convex combination / learned linear fusion vs RRF (primary PDF multimodal)
2. FANNS survey Lin 2025 arXiv:2505.06501 taxonomy figures (short)
3. Montague & Aslam Condorcet Fuse CIKM 2002 (cite-chase)
4. Vendor RRF rank base (Qdrant / ES / Milvus) vs Cormack \(r(d)\ge 1\)
5. Optional ColBERT / MUVERA abstract+figures for \(\mathrm{Search}_{late}\) rewrite rules

## Promote?

- [x] Thesis related-work fusion subsection + algebra \(\mathrm{Fuse}_{rrf}\) **[Established]** wording + applications hybrid pattern
- [x] OKF bundle under `knowledge/reads/rrf-cormack-sigir09/`
- [ ] Not a new fusion algorithm — do not invent RQL-specific RRF math
