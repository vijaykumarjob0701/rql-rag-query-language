---
type: Concept
title: Traits and calling convention
tags: [calcite, traits]
status: established
---

# Traits and calling convention

Calcite attaches **traits** to relational expressions to encode physical properties without splitting every operator into LogicalX vs PhysicalX classes. Changing a trait does not change the logical rows produced; it changes how/where the expression runs and thus cost.

**Calling convention** is the trait naming the engine (e.g. `jdbc-mysql`, `splunk`, `spark`, `enumerable`). Optimization moves subtrees across conventions via converters and adapter-specific rules (predicate/join pushdown examples in Fig. 2 / §5).

**RQL `[hypothesis]`:** `capabilities.*` on plans + FilterExec mode ads play a similar role to traits/conventions — capability negotiation rather than a full trait lattice.
