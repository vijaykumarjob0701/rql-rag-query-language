---
type: Playbook
title: PLAID rewrite implications for RQL (hypothesis)
tags: [rql, hypothesis, plaid, rewrite, late-interact]
status: hypothesis
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:05:00+01:00
---

# PLAID middle rung for RQL `[hypothesis]`

## ColBERT → PLAID → MUVERA compile ladder

| Step | Physical form | Mechanism status | When |
|------|---------------|------------------|------|
| 1 | Native multi-vector MaxSim (ColBERT / ColBERTv2 index) | MaxSim **[Established]** (0012) | Capability `multi_vector` |
| 2 | **PLAID:** 4-stage centroid prune → residual MaxSim | Pipeline **[Established]** (0014); packaging **[Hypothesis]** | Capability `late_plaid` |
| 3 | **MUVERA:** FDE → MIPS → MaxSim/Chamfer rerank | FDE mechanism **[Established]** (0013) | Capability `fde_mips` / single-vector ANN only |
| fail | EXPLAIN + error | — | Neither multi-vector nor FDE |

## What PLAID contributes (vs ColBERT / MUVERA)
- **Keeps** multi-vector residual index + exact MaxSim at the end (unlike MUVERA’s FDE approximation for candidate gen).
- **Adds** cheap bag-of-centroids MaxSim + \(t_{cs}\) sparsification so residuals are loaded for ~`ndocs/4` passages only.
- Requires ColBERTv2-style **centroid+residual** compression layout — not a generic single-vector ANN rewrite.

## Cost vector hooks `[hypothesis]`
- `nprobe`, `t_cs`, `ndocs`, final `k`
- CPU vs GPU kernel availability (paper: padding-free MaxSim = CPU-only; LUT decompress = both)
- Inverted-list footprint (centroids→PIDs)

## Links
- Equations: [../equations/centroid-interaction.md](../equations/centroid-interaction.md)
- Pipeline: [../algorithms/four-stage-pipeline.md](../algorithms/four-stage-pipeline.md)
- ColBERT score: [../../colbert-sigir20/equations/maxsim-late-interaction.md](../../colbert-sigir20/equations/maxsim-late-interaction.md)
- MUVERA ladder sibling: [../../muvera-2405.19504/strategies/fde-rewrite-for-rql.md](../../muvera-2405.19504/strategies/fde-rewrite-for-rql.md)
