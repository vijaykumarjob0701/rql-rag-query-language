---
type: Concept
title: Logical vs physical is consumer convention
tags: [substrait, physical-plan]
status: established-docs
---

# Logical vs physical is consumer convention

Substrait physical_relations docs state there is **no true** logical/physical distinction in the specification. Operators such as HashJoin, Exchange, and Top-N are *conventionally* physical. A given consumer may treat a subset of operators as its physical plan.

**Implication for RQL `[hypothesis]`:** RQL’s explicit LogicalPlan vs PhysicalPlan JSON split is a **stricter packaging choice** than Substrait’s convention — inspired by the same need, not a Substrait requirement. Do not claim Substrait “requires” dual schemas.
