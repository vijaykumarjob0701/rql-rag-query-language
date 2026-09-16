---
type: Equation
title: Convex combination (CC / TM2C2)
tags: [bruch, equation, fuse-linear]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:25:00+01:00
---

# Equation — \(f_{\mathrm{Convex}}\) / TM2C2

**Source:** Bruch et al., Eqs. (2)–(5).

Min-max over union set \(\mathrm{U}_k(q)\):
\[
\phi_{\mathrm{mm}}(f_o(q,d)) = \frac{f_o(q,d) - m_q}{M_q - m_q}
\]

Theoretical min-max (TM2C2 when both channels use \(\phi_{\mathrm{tmm}}\)):
\[
\phi_{\mathrm{tmm}}(f_o(q,d)) = \frac{f_o(q,d) - \inf f_o(q,\cdot)}{M_q - \inf f_o(q,\cdot)}
\]
(e.g. BM25 \(\inf=0\); cosine \(\inf=-1\)).

Convex combination:
\[
f_{\mathrm{Convex}}(q,d) = \alpha\,\phi_{\mathrm{Sem}}(f_{\mathrm{Sem}}(q,d)) + (1-\alpha)\,\phi_{\mathrm{Lex}}(f_{\mathrm{Lex}}(q,d)),\quad 0\le\alpha\le 1
\]

z-score alternative: \(\phi_z=(f-\mu)/\sigma\) (Eq. 5).

**RQL note:** Formula + role of normalization are **[Established]** literature for \(\mathrm{Fuse}_{linear}(\alpha)\). Default \(\alpha\) / choice of \(\phi\) / planner policy remain **[Hypothesis]**.
