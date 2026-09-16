---
type: Equation
title: PLAID centroid scores and approximate MaxSim
tags: [plaid, equation, centroid-interaction]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:05:00+01:00
---

# Equations — centroid interaction / pruning (PLAID §4)

**Source:** Santhanam et al., CIKM 2022 / arXiv:2205.09707, §4.1–4.3.

## Query–centroid scores (Eq. 2)
\[
S_{c,q} = C \cdot Q^{\top}
\]
Computed once per query; reused across all bag-of-centroids approximations.

## Approximate passage matrix (Eq. 3)
For candidate passage token centroid indices \(I\):
\[
\tilde{D} = \begin{bmatrix} S_{c,q}[I_1] \\ S_{c,q}[I_2] \\ \vdots \end{bmatrix}
\]

## Approximate MaxSim (Eq. 4)
\[
S_{\tilde{D}} = \sum_{i=1}^{|Q|} \max_{j=1}^{|\tilde{D}|} \tilde{D}_{i,j}
\]
Same MaxSim-sum shape as ColBERT; inputs are centroid score rows, not residual vectors.

## Centroid pruning predicate (Eq. 5)
Include token with centroid \(i\) in Stage-2 \(\tilde{D}\) iff
\[
\max_{j=1}^{|Q|} S_{c,q_{i,j}} \ge t_{cs}
\]

## Final score (Eq. 1 = ColBERT MaxSim)
Stage 4 decompresses residuals to \(D\) and applies standard MaxSim \(S_{q,d}\).

**RQL note:** Eqs. 2–5 are **[Established]** literature mechanisms for a physical `LATE_PLAID` plan. Operator naming / capability flags remain **[Hypothesis]**.
