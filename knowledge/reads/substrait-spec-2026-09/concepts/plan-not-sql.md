---
type: Concept
title: Plans not SQL text
tags: [substrait, doctrine]
status: established-docs
---

# Plans not SQL text

Substrait’s stated motivation: SQL is human-friendly but insufficiently detailed and poorly suited as an interchange format between parsers, optimizers, and engines. Modern stacks already lower SQL to query/execution plans; Substrait standardizes that layer so engines can exchange semantics without N×N dialect bridges.

**RQL adjacency `[hypothesis]`:** RQL textual DSL is a frontend; the portable unit is LogicalPlan/PhysicalPlan — same doctrine, different domain (retrieval evidence algebra).
