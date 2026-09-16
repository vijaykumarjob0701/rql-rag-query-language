---
type: Strategy
title: Fuse_linear / Fuse_ltr implications for RQL
tags: [bruch, fuse-linear, fuse-ltr, rql]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:25:00+01:00
---

# Strategy — \(\mathrm{Fuse}_{linear}\) / \(\mathrm{Fuse}_{ltr}\) for RQL

## Established (steal)

- Linear/convex score fusion \(f=\alpha\phi(s_{\mathrm{sem}})+(1-\alpha)\phi(s_{\mathrm{lex}})\) with monotone normalization (Bruch Eqs. 2–5).
- RRF remains the **rank-only** sibling when scores are incomparable (Cormack; journal 0011).
- Literature delineation: CC preserves calibrated score geometry better than rank-only RRF (Bruch §5–§6 desiderata / Lipschitz discussion) — as **mechanism**, not as our metric win.

## Hypothesis (RQL packaging)

- Name \(\mathrm{Fuse}_{linear}(\alpha)\) (and optional \(\phi\) / norm mode) in the evidence algebra.
- Name \(\mathrm{Fuse}_{ltr}(\mathrm{model})\) for multi-feature / learned rankers beyond single \(\alpha\).
- Planner policy: prefer RRF when channels lack calibrated comparable scores; prefer linear/CC when scores + small labeled set exist; escalate to LTR when features justify it.
- EXPLAIN must show \(\alpha\), \(\phi\), and input channels — not opaque `hybrid=on`.

## Do not

- Copy Bruch Table 2/4 NDCG into RQL eval as reproduced.
- Claim RQL invents convex combination or TM2C2.
- Silently apply linear fuse on incomparable raw scores without documenting normalization.
