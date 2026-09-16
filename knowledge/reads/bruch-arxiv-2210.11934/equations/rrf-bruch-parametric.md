---
type: Equation
title: Parametric RRF (Bruch view)
tags: [bruch, equation, rrf]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:25:00+01:00
---

# Equation — RRF as used by Bruch

**Source:** Bruch et al., Eqs. (7)–(8), (10); lineage Cormack et al. (journal 0011).

Two-channel default form:
\[
f_{\mathrm{RRF}}(q,d)=\frac{1}{\eta+\pi_{\mathrm{Lex}}(q,d)}+\frac{1}{\eta+\pi_{\mathrm{Sem}}(q,d)}
\]

Per-channel parameters:
\[
f_{\mathrm{RRF}}(q,d)=\frac{1}{\eta_{\mathrm{Lex}}+\pi_{\mathrm{Lex}}}+\frac{1}{\eta_{\mathrm{Sem}}+\pi_{\mathrm{Sem}}}
\]

RRF-CC (Eq. 10): weighted mix of reciprocal-rank terms with \(\alpha,\eta_{\mathrm{Lex}},\eta_{\mathrm{Sem}}\).

**RQL note:** Does **not** replace Cormack formula as \(\mathrm{Fuse}_{rrf}\) definition. Supports **[Established]** claim that hybrid RRF use is parameter-sensitive; keeps rank-only portable default \(k/\eta=60\) from Cormack.
