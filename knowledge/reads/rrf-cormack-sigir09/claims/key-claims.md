---
type: ClaimSet
title: RRF key claims (evidence-linked)
tags: [rrf, claims]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:55:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** RRF score is \(\sum_r 1/(k+r(d))\) with \(k=60\) fixed after pilot.  
   Evidence: §1; [../equations/rrf-score.md](../equations/rrf-score.md); [../tables/table-01-pilot-k.md](../tables/table-01-pilot-k.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** RRF uses **ranks only** (no need for comparable raw scores), unlike CombMNZ.  
   Evidence: §1–§2

3. **AUTHOR-CLAIM (not reproduced):** On authors’ pilots + TREC fusion sets, RRF beats Condorcet / often CombMNZ / often best individual by ~4–5% MAP on average; sign tests reported.  
   Evidence: Tables 1–2; §1 — **do not cite as our measurement**

4. **AUTHOR-CLAIM (not reproduced):** On LETOR 3, RRF fusion of baseline LTR rankings beats individuals and Condorcet; CombMNZ slightly higher (n.s.).  
   Evidence: Table 3

5. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (engineering):** RRF needs no global pairwise vote matrix; ranks can be summed one system at a time.  
   Evidence: §2

## Anti-claims

- That we reproduced TREC/LETOR MAP.
- That RRF always dominates learned linear / CC fusion on modern hybrid RAG.
- That \(k=60\) is theoretically optimal for all corpora.
