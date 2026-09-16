---
type: Equation
title: Chamfer similarity and FDE approximation target
tags: [muvera, chamfer, fde, equation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
---

# Chamfer (= MaxSim-sum)

**Source:** MUVERA §1.1 (equated to ColBERT MaxSim).

\[
\mathrm{CHAMFER}(Q, P) = \sum_{q \in Q} \max_{p \in P} \langle q, p \rangle
\]

Same structural operator as ColBERT Eq. (3) with cosine implemented as inner product on (typically) normalized embeddings.

# FDE target

\[
\langle F_q(Q),\, F_{doc}(P) \rangle \approx \mathrm{CHAMFER}(Q, P)
\]

with \(d_{\mathrm{FDE}} = B \cdot d_{\mathrm{proj}} \cdot R_{\mathrm{reps}}\) (plus optional final projection). Partition \(\phi\) via SimHash (\(B=2^{k_{\mathrm{sim}}}\)) preferred over data-dependent k-means in authors’ Pareto study.

**RQL note:** Chamfer/MaxSim scoring **[Established]** (with ColBERT). Using FDE+MIPS as a physical rewrite of \(\mathrm{Search}_{late}\) is **[Hypothesis]** packaging.
