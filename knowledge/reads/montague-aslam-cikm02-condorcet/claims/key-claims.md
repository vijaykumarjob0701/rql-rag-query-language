---
type: ClaimSet
title: Condorcet-fuse key claims (evidence-linked)
tags: [condorcet, claims]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:30:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Condorcet-fuse ranks documents by sorting with a **pairwise majority runoff** comparator (Alg 1) — ranks only; no raw scores required.  
   Evidence: Alg 1–3; §3.2.5; [../algorithms/condorcet-fuse.md](../algorithms/condorcet-fuse.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Complexity \(O(nk\log n)\) via QuickSort/MergeSort with Alg 1 as comparison (Theorem 4); theoretic full graph is \(O(n^2k)\).  
   Evidence: §3.2.5; Theorem 4; page 5

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Fig 1 taxonomy: metasearch methods classified by **ranks-only vs scores** × **no-training vs training** — Condorcet-fuse sits ranks-only / no-training; Weighted Condorcet-fuse is ranks-only / training.  
   Evidence: [../figures/fig-01-metasearch-taxonomy.md](../figures/fig-01-metasearch-taxonomy.md)

4. **AUTHOR-CLAIM (not reproduced):** On TREC 3/5/9 + Vogt, Condorcet-fuse outperforms rCombMNZ and Borda-fuse; outperforms CombMNZ on 3 of 4 datasets even without scores; sign tests in Table 2.  
   Evidence: Fig 4; Table 2; §4.3 / §5 — **do not cite as our measurement**

5. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (failure mode):** Condorcet majority is sensitive to **dependent/similar input runs** (TREC 9 Justsystem cluster; Table 3–4); dependence filtering (sim threshold 0.66) and MAP-based weights mitigate (Fig 5).  
   Evidence: §4.3.1; Tables 3–4; Fig 5

6. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (lineage):** Condorcet = majoritarian class; Borda-fuse = positional class (prior Aslam–Montague SIGIR’01). Cormack RRF (journal 0011) later compares against Condorcet Fuse.  
   Evidence: §2–§3; Cormack title/abstract

## Anti-claims

- That we reproduced TREC MAP or Table 2 sign tests.
- That Condorcet should displace \(\mathrm{Fuse}_{rrf}\) as RQL default (Cormack AUTHORS later prefer RRF).
- That Condorcet uses relevance scores (it does not; CombMNZ does).
- That Hamiltonian / SCC machinery must be materialised at runtime (efficient form is sort-with-comparator).
