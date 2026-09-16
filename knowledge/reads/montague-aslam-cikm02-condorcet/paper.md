---
type: Paper
title: "Condorcet Fusion for Improved Retrieval"
resource: https://www.khoury.northeastern.edu/~jaa/IS4200.10X1/resources/condorcet.pdf
tags: [condorcet, cikm02, fusion, montague, aslam]
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:30:00+01:00
status: provisional
---

# Condorcet-fuse — Montague & Aslam (CIKM 2002) `[venue-verified]`

**Authors:** Mark Montague, Javed A. Aslam (Dartmouth College)  
**Venue:** CIKM’02, November 4–9, 2002, McLean, Virginia, USA; ACM 1-58113-492-4/02/0011; pages 538–548 (ACM proceedings)  
**DOI:** [10.1145/584792.584881](https://doi.org/10.1145/584792.584881)  
**Local:** `tooling/scripts/extract_out/montague-aslam-cikm02-condorcet.pdf` (**11 pages**, author course host PDF)  
**Alt mirrors:** `https://www.ccs.neu.edu/home/jaa/CSG339.06F/resources/condorcet.pdf`

## Abstract (paraphrase)

Introduce **Condorcet-fuse**: adapt majoritarian Condorcet voting from Social Choice Theory to metasearch/data fusion. Graph-theoretic analysis yields a **sorting-based** algorithm (pairwise majority as comparator) that is efficient \(O(nk\log n)\) and effective on TREC. Authors report Condorcet-fuse often beats CombMNZ / rCombMNZ / Borda-fuse whether or not scores/training are available; weighted and dependence-filtered variants improve further.

## Links
- Journal 0018; [claims](claims/key-claims.md); [Fuse_condorcet strategy](strategies/fuse-condorcet-for-rql.md); [Alg 1/3](algorithms/condorcet-fuse.md); equation/comparator note.
