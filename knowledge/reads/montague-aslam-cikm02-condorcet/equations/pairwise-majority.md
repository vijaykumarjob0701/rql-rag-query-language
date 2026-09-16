---
type: Equation
title: Pairwise majority runoff (Condorcet comparator)
tags: [condorcet, equation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:30:00+01:00
---

# Equation — pairwise majority (Alg 1)

**Source:** Montague & Aslam, CIKM 2002, Algorithm 1 / §3.2.

For documents \(d_1,d_2\) and \(k\) input rankings \(S_i\):

\[
\mathrm{count}(d_1,d_2)=\sum_{i=1}^{k}\mathrm{sign}\big(r_i(d_2)-r_i(d_1)\big)
\]

(with paper’s ++/−− formulation: +1 if \(S_i\) ranks \(d_1\) above \(d_2\), −1 otherwise).  
If \(\mathrm{count}>0\), prefer \(d_1\); else prefer \(d_2\).

**Condorcet graph:** edge \(x\to y\) iff \(x\) wins or ties the head-to-head vs \(y\).  
**Condorcet-fuse:** sort the candidate pool using the above as the comparison function (Alg 3) — yields a Condorcet path without materialising the full \(O(n^2k)\) graph.

**Weighted variant:** replace unweighted votes by sum of channel weights (e.g. per-system MAP) in the runoff (§3.2.7).

**RQL note:** Comparator + sort = **[Established]** prior art for \(\mathrm{Fuse}_{condorcet}\). Op name / compile / when-to-prefer vs RRF = `[hypothesis]`.
