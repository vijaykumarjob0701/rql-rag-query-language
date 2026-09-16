# 0018 — Montague & Aslam Condorcet-fuse multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~23:30 IST (Europe/Dublin)  
**Type:** multimodal source read (cite-chase from Cormack RRF / Chen queue)  
**Status:** Pass 1–5 complete for this source  
**Source:** Montague & Aslam — *Condorcet Fusion for Improved Retrieval* — CIKM 2002, pp. 538–548  
**URLs:** DOI [10.1145/584792.584881](https://doi.org/10.1145/584792.584881) · author PDF https://www.khoury.northeastern.edu/~jaa/IS4200.10X1/resources/condorcet.pdf · mirror https://www.ccs.neu.edu/home/jaa/CSG339.06F/resources/condorcet.pdf  
**Local PDF:** `tooling/scripts/extract_out/montague-aslam-cikm02-condorcet.pdf` (**11 pp**)  
**Extract dir:** `tooling/scripts/extract_out/montague_condorcet_cikm02/` (53 nodes / 44 edges; 7 embedded figs; page tables via visual; `page_renders/page-01..11.png`)  
**OKF bundle:** [`../knowledge/reads/montague-aslam-cikm02-condorcet/`](../knowledge/reads/montague-aslam-cikm02-condorcet/)  
**Cite-chase of:** Cormack SIGIR’09 Condorcet comparator (journal 0011); queued after Chen 0017

---

## Context

After RRF (0011), Bruch linear (0016), and Chen RRF-vs-linear (0017), the Fuse family still lacked the **majoritarian** classic Cormack compares against. Prefer Condorcet over FANNS this turn because the author PDF is findable and short (11 pp), completing the rank-fusion lineage before the filtered-ANN survey figure pass.

## Question asked

What exactly is Condorcet-fuse (algorithm, complexity, taxonomy vs CombMNZ/Borda), what evidence do Figs/Tables give, and how should RQL name it as a \(\mathrm{Fuse}\) sibling without inventing metrics or displacing \(\mathrm{Fuse}_{rrf}\)?

## Where we looked

- WebSearch `Montague Aslam Condorcet fusion CIKM 2002 PDF`
- Author course hosts (Khoury NEU / CCS NEU); ACM DOI 10.1145/584792.584881
- `curl` PDF + `extract_document.py` + `relate_components.py`
- Visual skim of all 11 page PNGs (focus: Fig 1–5; Alg 1–3; Tables 1–4; §3.2, §4.3.1, §5)

## Pass 1 — Skim

1. Metasearch / data fusion via **Condorcet** majoritarian voting (Social Choice Theory).
2. Condorcet graph + Hamiltonian / Condorcet path; voting paradox → SCCs.
3. Efficient **Condorcet-fuse**: sort with pairwise majority comparator — \(O(nk\log n)\).
4. Rank-only by default; optional **weighted** Condorcet (training/MAP weights); no native use of raw relevance scores.
5. TREC 3/5/9 + Vogt; compare CombMNZ, rCombMNZ, Borda-fuse; dependence filtering for correlated runs.
6. Conclusion: beats rCombMNZ/Borda; beats CombMNZ on 3/4 sets even without scores (AUTHOR).

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro (external vs internal; data-fusion scope); §2 Related (CombSum/MNZ, Borda-fuse, linear score combo); §3 Condorcet model (3.1 social choice; 3.2 metasearch: graph, paradox, SCCs, paths, Condorcet-fuse efficiency, within-SCC, weighted, scores); §4 Experiments (setup Table 1; train/test; procedure; results; 4.3.1 dependence filtering); §5 Conclusion; §6 References |
| Figures | **Fig 1** ranks×training taxonomy; **Fig 2** external vs internal architecture; **Fig 3** voting-paradox cycle; **Fig 4** MAP curves 4 datasets × random / best-to-worst; **Fig 5** weighted + dependence-filtered variants |
| Tables | **Table 1** datasets (#sys, MAP stats); **Table 2** sign-test grid (p.9); **Table 3** TREC 9 top-5 runs; **Table 4** avg pairwise set-sim |
| Algorithms | **Alg 1** Simple Majority Runoff; **Alg 2** Theoretic Condorcet Metasearch; **Alg 3** Condorcet-fuse (sort w/ Alg 1) |
| Equations / theorems | Condorcet graph edge def; Theorems 1–4 (Hamiltonian path; SCC order; QuickSort→path; \(O(nk\log n)\)); \(\mathrm{sim}=|A\cap B|/|A\cup B|\) |

**Miss checklist:** all 11 pages rendered and opened; Fig 1–5 captions + axes understood (Fig 4 MAP); Tables 1–4 headers understood; pdfplumber “tables” on p.1 are layout noise — real tables recovered via page PNGs + pdftotext; embedded XObjects include ACM logo + figure graphics.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| Alg 1 | implements | pairwise majority comparator | ranks only |
| Alg 3 | implements | Condorcet-fuse | sort w/ Alg 1 |
| Fig 1 | introduces | Fuse taxonomy | ranks/scores × train/no-train |
| Fig 3 | qualifies | need for path/SCC story | cycles |
| Fig 4 | grounds | AUTHOR MAP wins vs CombMNZ/Borda | unreproduced |
| Table 2 | grounds | sign-test claims | AUTHOR |
| Tables 3–4 + §4.3.1 | qualifies | dependence failure mode | Justsystem majority |
| Fig 5 | grounds | weights + dep-filter help | AUTHOR |
| Cormack 0011 | cites-sideways | this paper as Condorcet Fuse baseline | RRF later preferred by Cormack AUTHORS |

## Pass 4 — Seed (1–5%)

**Observation:**

> Montague & Aslam (CIKM’02) define **Condorcet-fuse**: fuse \(k\) rankings by sorting the document pool with a **pairwise majority runoff** comparator (Alg 1+3), \(O(nk\log n)\), ranks only. Fig 1 places it in the ranks-only / no-training cell beside Borda-fuse and rCombMNZ (vs CombMNZ on the score axis; weighted Condorcet when training exists). AUTHORS report strong TREC MAP vs CombMNZ/rCombMNZ/Borda (Fig 4 / Table 2; unreproduced here), and show majority voting is brittle to **correlated channels** (TREC 9 Justsystem cluster) unless dependence-filtered or weighted (Fig 5; sim threshold 0.66).

**Interpretation for RQL:**

> Package \(\mathrm{Fuse}_{condorcet}\) as a **Fuse family sibling** of \(\mathrm{Fuse}_{rrf}\) (both rank-only), not a default replacement. Prefer \(\mathrm{Fuse}_{rrf}(k{=}60)\) as the portable default (Cormack; Chen zero-shot); offer Condorcet when majoritarian pairwise semantics are desired or for Fuse-family A/B. Optional \(\mathrm{Fuse}_{condorcet}^{w}\) + pre-fuse dependence prune are physical/policy hints. Do **not** treat Fig 1 as FANNS FilterExec taxonomy — it is a **fusion-input** taxonomy.

**Evidence pointers:** Alg 1–3; Fig 1, 4, 5; Tables 1–4; §3.2.5–§3.2.7; §4.3.1; §5; cross: Cormack journal 0011.

**Anti-overclaim:** unreproduced MAP/sign tests; not “Condorcet beats RRF” (Cormack AUTHORS claim the opposite on their suites); Condorcet ≠ score CC/TM2C2; dependence filter ≠ ANN predicate FilterExec.

**Uncertainty:** ACM proceedings pagination 538–548 from DOI record (author PDF is 11-page letter layout, not ACM page images); within-SCC QuickSort nondeterminism not characterised for RAG; no Condorcet unit harness this turn.

## Pass 5 — Next queries

1. FANNS survey Lin et al. 2025 (arXiv:2505.06501) figure/table inventory for **filter-strategy taxonomy** → optimizer FilterExec (still open)
2. Vendor multi-vector / weighted-linear / hybrid API matrix (Qdrant, ES, Weaviate, Milvus)
3. Optional: property-test harness for pairwise-majority sort (toy lists; no IR metrics)
4. Optional: Aslam–Montague SIGIR’01 Borda-fuse / Models for metasearch (positional sibling)
5. Optional: Copeland / other Condorcet extensions for within-SCC policy

## Promote?

- [x] Journal 0018 + OKF `knowledge/reads/montague-aslam-cikm02-condorcet/`
- [x] Thesis: \(\mathrm{Fuse}_{condorcet}\) as Fuse family sibling (Established mechanism; prefer-RRF default Hypothesis)
- [x] Meta: NOTES / CHANGELOG / docs/06 / docs/references / journal index
- [ ] Do not invent fusion math or fake RAG metrics
- [ ] Do not push
