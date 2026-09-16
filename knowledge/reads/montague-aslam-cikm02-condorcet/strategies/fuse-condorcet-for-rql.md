---
type: Strategy
title: Fuse_condorcet implications for RQL
tags: [condorcet, fuse, rql]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:30:00+01:00
---

# Strategy — \(\mathrm{Fuse}_{condorcet}\) for RQL

## Established (steal)

- Pairwise majority comparator over channel ranks (Alg 1); sort → fused ranking (Alg 3).
- Rank-only; no score calibration; \(O(nk\log n)\).
- Sibling of \(\mathrm{Fuse}_{rrf}\) in the **rank-only** quadrant of Fig 1 (vs CombMNZ score quadrant; vs weighted Condorcet when training exists).
- Known failure mode: correlated channels can dominate pairwise votes → optional dependence filter / weights.

## Hypothesis (RQL packaging)

- Name logical op \(\mathrm{Fuse}_{condorcet}\) (optionally \(\mathrm{Fuse}_{condorcet}^{w}\) with channel weights) in the evidence algebra as a **Fuse family sibling**, not a replacement for \(\mathrm{Fuse}_{rrf}\).
- Default portable fuse remains \(\mathrm{Fuse}_{rrf}(k{=}60)\) (Cormack; Chen zero-shot); offer Condorcet when planner/user wants **majoritarian** semantics or when evaluating Fuse-family A/B.
- EXPLAIN must show comparator = pairwise-majority, channel set, optional weights / dep-filter threshold.
- Dependence filtering (set-sim threshold) is a **pre-fuse channel prune** physical hint, not FilterExec ANN taxonomy.

## Do not

- Copy Montague MAP / sign-test tables into RQL eval as reproduced.
- Claim RQL invents Condorcet voting.
- Silently treat Condorcet as score fusion or as “better than RRF” universally (Cormack AUTHORS disagree on their suites).
