---
type: Playbook
title: Late-interaction implications for RQL (hypothesis)
tags: [rql, hypothesis, late-interact, maxsim]
status: hypothesis
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
---

# Late-interaction implications for RQL `[hypothesis]`

| Literature mechanism | Hypothesized RQL piece | Status |
|----------------------|------------------------|--------|
| MaxSim-sum score Eq. (3) | Semantics of `Search_late` / channel `late` | Scoring **[Established]**; op name **[Hypothesis]** |
| Offline doc bags + online query encode | Indexing contract / adapter capability `multi_vector` | **[Hypothesis]** |
| faiss IVFPQ → exact MaxSim (§3.6) | Physical `LATE_EXACT` / `LATE_IVF_CANDIDATE` | **[Hypothesis]** |
| PLAID centroid interaction (0014) | Physical `LATE_PLAID` | **[Hypothesis]** cite-only |
| MUVERA FDE→MIPS→MaxSim rerank (0013) | Rewrite `Search_late ⇒ FDE_ANN + MAXSIM_RERANK` | **[Hypothesis]** |

## Hard constraints

- Do not silently substitute single-vector dense cosine for MaxSim when the logical plan asked for late interaction — either execute multi-vector, apply an advertised rewrite (FDE), or fail/EXPLAIN.
- ACL/filter operators remain orthogonal; filtering multi-vector hits still needs FilterExec capability negotiation.

## Links
- Parent: [../paper.md](../paper.md)
- Equation: [../equations/maxsim-late-interaction.md](../equations/maxsim-late-interaction.md)
- MUVERA sibling: [../../muvera-2405.19504/](../../muvera-2405.19504/)
