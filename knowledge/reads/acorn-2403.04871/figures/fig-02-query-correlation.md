---
type: Figure
title: "Figure 2 — Predicate clustering and query correlation"
description: Three regimes — no clustering; positive correlation; negative correlation.
tags: [acorn, figure, selectivity, correlation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T12:14:00+01:00
---

# Figure 2

**Caption:** Schematic of datasets with no predicate clustering; predicate clustering + positive query correlation; clustering + negative correlation. Dark blue = pass predicate; gray = fail; green = query.

**Why it matters:** Grounds the claim that post-filtering’s cost depends on correlation, not only selectivity.

**RQL `[hypothesis]`:** Cost model inputs should include a correlation/empty-result risk feature, not selectivity alone. See [../strategies/filter-strategy-implications-for-rql.md](../strategies/filter-strategy-implications-for-rql.md).
