---
type: Concept
title: RQL ↔ Calcite adjacency (Hypothesis)
tags: [rql, calcite, hypothesis]
status: hypothesis
---

# RQL ↔ Calcite adjacency `[hypothesis]`

| Steal | Leave |
|-------|-------|
| Algebra tree as IR; frontend optional | Shipping Calcite inside RQL |
| Adapter / convention pushdown | RelOptRule Java API |
| Explicit fallback when backend lacks op (enumerable ↔ ShimCast) | Claiming cost-based DP today |
| Pluggable metadata/cost later | Invented selectivity models without measurement |

Integrity: **inspired-by**, not “RQL is Calcite for vectors.”
