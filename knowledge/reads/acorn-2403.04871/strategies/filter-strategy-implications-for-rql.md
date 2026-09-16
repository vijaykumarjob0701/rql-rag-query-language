---
type: Playbook
title: Filter-strategy implications for RQL (hypothesis)
description: How ACORN’s taxonomy maps to hypothesized RQL physical FilterExec modes.
tags: [rql, hypothesis, fanns, filter-mode]
status: hypothesis
generated:
  by: grok-bot/executor
  at: 2026-09-16T12:14:00+01:00
---

# Filter-strategy implications for RQL `[hypothesis]`

**Not promoted** to settled algebra. Aligns with provisional [`docs/07-evolved-idea.md`](../../../../docs/07-evolved-idea.md).

| ACORN / literature strategy | Hypothesized RQL physical mode | When (sketch) |
|-----------------------------|--------------------------------|---------------|
| Pre-filtering | `FilterExec=PRE` | High selectivity survivors small enough for exact/scan |
| Post-filtering (+ overfetch) | `FilterExec=POST` | High selectivity, positive correlation, cheap overfetch |
| Predicate subgraph (ACORN) | `FilterExec=SUBGRAPH` | Backend capability present; low–mid selectivity / correlation risk |
| Specialized equality graph (Filtered-DiskANN) | `FilterExec=SPECIALIZED` | Known small equality predicate set + capable index |
| Iterator / relaxed scan (VBASE — *unread this step*) | `FilterExec=ITERATIVE` | Needs Open/Next integration — **seed only** |
| Unknown | `FilterExec=AUTO` | Cost model + stats; hard constraint: ACL predicates must not be client-side-only |

## Planner signals suggested by ACORN

From [fig-02-query-correlation.md](../figures/fig-02-query-correlation.md) and §3:

- **Selectivity \(s\)**
- **Dataset size \(n\)**
- **Query–predicate correlation** (positive / negative / none)

## Hard constraints (reliability-first)

- Mandatory ACL / tenant predicates: prefer server-side enforcement regardless of QPS.
- `EXPLAIN` must name which `FilterExec` was chosen and why (stats missing → conservative mode).

## Links

- Parent paper: [../paper.md](../paper.md)
- Neighbor selection physical variants: [../figures/fig-04-neighbor-selection.md](../figures/fig-04-neighbor-selection.md)
