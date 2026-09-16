---
type: Playbook
title: MUVERA FDE rewrite implications for RQL (hypothesis)
tags: [rql, hypothesis, muvera, fde, rewrite]
status: hypothesis
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
---

# FDE rewrite for RQL `[hypothesis]`

## Suggested compile ladder for `Search_late`

| Step | Physical form | When |
|------|---------------|------|
| 1 | Native multi-vector MaxSim (ColBERT-class index) | Adapter capability `multi_vector` |
| 2 | PLAID-class centroid prune → MaxSim | Capability `late_plaid` (cite-only until multimodal) |
| 3 | **MUVERA:** build/query FDEs via MIPS → `MAXSIM_RERANK` | Capability `fde_mips` / strong single-vector ANN only |
| fail | EXPLAIN + error | No multi-vector and no FDE extension |

## Cost vector hooks

- FDE dim / PQ bytes (authors: 32× PQ on large FDEs)
- Candidate depth \(K_c\) before Chamfer rerank
- Rerank Chamfer cost \(\propto |Q|\cdot|P|\) per candidate

## Links
- ColBERT established score: [../../colbert-sigir20/equations/maxsim-late-interaction.md](../../colbert-sigir20/equations/maxsim-late-interaction.md)
- Fig 1: [../figures/fig-01-muvera-vs-plaid.md](../figures/fig-01-muvera-vs-plaid.md)
