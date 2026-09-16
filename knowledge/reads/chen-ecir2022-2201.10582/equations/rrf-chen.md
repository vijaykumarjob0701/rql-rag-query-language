---
type: Equation
title: Chen Eq. (1) — RRF hybrid fuse
tags: [chen, rrf, equation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Equation (1) — Reciprocal Rank Fusion

\[
\mathrm{RRF}(q,d,M)=\sum_{m\in M}\frac{1}{k+\pi_m(q,d)},\qquad k=60
\]

- \(\pi_m(q,d)\): rank of document \(d\) under model \(m\) for query \(q\)
- \(M\): set of lexical and/or deep retrieval models
- Follows Cormack et al. (SIGIR’09); used here as the **zero-shot** hybrid fuse

## Linear case study (§6; not Eq. numbered)

\[
s(d)=\alpha\, s_{\mathrm{BM25}}(d)+(1-\alpha)\, s_{\mathrm{NPR}}(d)
\]

with **min-max** score normalisation; \(\alpha\in\{0.1,\ldots,0.9\}\) grid-searched on OOD sets (not zero-shot).
