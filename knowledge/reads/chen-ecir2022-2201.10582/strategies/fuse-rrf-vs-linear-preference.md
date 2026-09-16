---
type: Strategy
title: Fuse_rrf vs Fuse_linear preference (Chen×Bruch)
tags: [chen, bruch, fuse-rrf, fuse-linear, planner]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Strategy — when \(\mathrm{Fuse}_{rrf}\) vs \(\mathrm{Fuse}_{linear}\)

## Established (literature disagreement of setups)

| Axis | Chen et al. (ECIR’22) | Bruch et al. (TOIS’23) |
|------|------------------------|-------------------------|
| Preferred fuse (AUTHOR) | **RRF** (zero-shot) | **TM2C2** CC (tuned \(\alpha\)) |
| Linear form tested | min-max \(\alpha\)-interp BM25+NPR | \(\phi_{\mathrm{tmm}}\) + \(\alpha\) (TM2C2) |
| Primary metric | Recall@1K (+ MAP) | NDCG (+ Recall) |
| Labels for fuse weight | Avoid (zero-shot) | Small labeled set; sample-efficient |
| Claim vs other | best linear < RRF ~3% rel. R@1K (Fig 2) | TM2C2 > RRF(60) NDCG (Table 2 / Fig 5) |

Both papers are **correct about their own suites**; the conflict is not resolved by picking a side.

## Hypothesis (RQL planner rule)

1. Emit \(\mathrm{Fuse}_{rrf}(k{=}60)\) when channel scores are **incomparable / uncalibrated**, or when **no** (or vanishing) labeled queries exist for \(\alpha\) / \(\phi\) — Chen-style portability.
2. Emit \(\mathrm{Fuse}_{linear}(\alpha)\) with documented \(\phi\) (prefer TM2C2-class) when scores are **comparable** and a **small labeled set** can tune \(\alpha\) — Bruch-style.
3. Escalate \(\mathrm{Fuse}_{ltr}\) when query features / multi-channel weights justify learning beyond single \(\alpha\) (Chen §7 future work; continuum with Bruch).
4. EXPLAIN must surface fuse family, \(k\) or \(\alpha\)/\(\phi\), and channels.

## Do not

- Claim a universal empirical winner for RAG hybrids.
- Equate Chen’s linear baseline with Bruch TM2C2.
- Promote AUTHOR tables as our reproduced metrics.
