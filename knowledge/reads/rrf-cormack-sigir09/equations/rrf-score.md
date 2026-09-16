---
type: Equation
title: RRF score definition
tags: [rrf, equation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:55:00+01:00
---

# Equation — RRFscore

**Source:** Cormack et al., SIGIR 2009, §1.

\[
\mathrm{RRFscore}(d \in D) = \sum_{r \in R} \frac{1}{k + r(d)}
\]

- \(D\): documents to rank  
- \(R\): set of rankings (permutations on \(1..|D|\))  
- \(r(d)\): rank of \(d\) in ranking \(r\) (1 = best)  
- \(k\): constant; authors fixed **\(k=60\)** after pilot (Table 1); choice “not critical”

**Also defined for comparison:** Condorcet pairwise majority; CombMNZ (needs scores \(s_r\) and cutoff \(c\)).

**RQL note:** This formula is **[Established]** prior art. Default \(k_{\mathrm{rrf}}=60\) matches the paper and common vendor defaults; still allow override in plans `[hypothesis]`.
