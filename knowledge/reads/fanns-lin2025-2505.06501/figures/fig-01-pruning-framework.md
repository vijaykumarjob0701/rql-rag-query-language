---
type: FigureNote
title: Fig 1 — pruning-focused FANNS framework (VSP/VJP/SJP/SSP)
page: 7
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Fig 1 — Pruning-focused framework `[Established taxonomy]`

**Caption (paper):** “The proposed pruning-focused framework for classifying FANNS algorithms”

**Visual (page-07 PNG):** Four rows from vector-pruning-dominant (top) to scalar-pruning-dominant (bottom):

| Strategy | Pipeline (schematic) | Selectivity thumbs (AUTHOR schematic) |
|----------|----------------------|----------------------------------------|
| **VSP** — vector-solely / “ANNS with result filtering” | Dataset → ANNS → \(K'\)-NN → exact filter → filtered \(K\)-NN | Good for **low** selectivity; poor for **high** |
| **VJP** — vector-centric joint / “ANNS with traversal filtering” | Dataset → ANNS+traversal filter → filtered \(K\)-NN | Aimed at **varying** selectivity; restrictive assumptions |
| **SJP** — scalar-centric joint | Dataset → coarse filter → partially filtered subsets → FANNS → merge | Varying selectivity; restrictive assumptions / workload need |
| **SSP** — scalar-solely | Dataset → exact filter → filtered subset → scan → filtered \(K\)-NN | Good for **high** selectivity; poor for **low** |

**RQL `[hypothesis]`:** Fig 1 is the ESTABLISHED survey vocabulary to expose in EXPLAIN (`pruning_strategy`). Map to FilterExec in [../strategies/filterexec-from-fanns-taxonomy.md](../strategies/filterexec-from-fanns-taxonomy.md). Do not treat thumbs as measured SLOs.
