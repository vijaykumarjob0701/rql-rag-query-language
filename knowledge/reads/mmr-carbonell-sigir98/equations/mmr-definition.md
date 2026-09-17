---
type: EquationNote
title: Maximal Marginal Relevance definition (SIGIR’98 §2)
tags: [mmr, equations]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:20:00+01:00
status: provisional
---

# MMR definition (sketch)

\[
\mathrm{MMR} \stackrel{\mathrm{def}}{=}
\arg\max_{D_i \in R \setminus S}
\Big[
\lambda\,\mathrm{Sim}_1(D_i, Q)
-
(1-\lambda)\max_{D_j \in S}\mathrm{Sim}_2(D_i, D_j)
\Big]
\]

- \(R = \mathrm{IR}(C, Q, \theta)\): retrieved candidate list  
- \(S\): already selected subset of \(R\) (grows greedily)  
- \(\mathrm{Sim}_1\): query–document (or query–passage) similarity  
- \(\mathrm{Sim}_2\): document–document (or passage–passage) similarity (may ≠ Sim₁)  
- \(\lambda \in [0,1]\): relevance vs novelty; **λ=1** pure relevance; **λ=0** max diversity

RQL packaging (Hypothesis): \(\mathrm{Diversify}_{mmr}(\lambda)\) applies this greedy selection to an evidence relation \(E\), with Sim₁/Sim₂ chosen by plan attributes (e.g. score channel vs embedding cosine).
