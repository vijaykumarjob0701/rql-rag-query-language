---
type: EquationNote
title: HyDE query-vector construction (Eqs. 5–8)
tags: [hyde, equations]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:10:00+01:00
status: provisional
---

# HyDE query vector (sketch)

Classical dual-encoder (Eq. 1): \(\mathrm{sim}(q,d)=\langle\mathrm{enc}_q(q),\mathrm{enc}_d(d)\rangle\).

HyDE sets \(f=\mathrm{enc}_d=\mathrm{enc}_{con}\) (contrastive) and builds the query vector from generated docs:

\[
\hat{\mathbf{v}}_{q} = \frac{1}{N}\sum_{k=1}^{N} f(\hat{d}_k),\quad \hat{d}_k\sim g(q,\mathrm{INST})
\]

Optional include query (Eq. 8):

\[
\hat{\mathbf{v}}_{q} = \frac{1}{N+1}\Big(\sum_{k=1}^{N} f(\hat{d}_k) + f(q)\Big)
\]

RQL packaging (Hypothesis): `REWRITE HYDE` materialises \(\{\hat{d}_k\}\) (or their embeddings); planner may choose N and whether to mix \(f(q)\).
