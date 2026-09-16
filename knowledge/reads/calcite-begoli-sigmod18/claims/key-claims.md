---
type: ClaimSet
title: Calcite key claims (paper-anchored)
tags: [calcite, claims]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-17T00:10:00+01:00
---

# Key claims

1. **ESTABLISHED-FOR-US:** Calcite deliberately omits storage, execution algorithms, and metadata repositories so it can mediate among applications and multiple processing engines via adapters.  
   Evidence: §3; [fig-01-architecture.md](../figures/fig-01-architecture.md)

2. **ESTABLISHED-FOR-US:** Internal IR is a **tree of relational operators**; entry via SQL parser/validator **or** programmatic RelBuilder / expression builder (non-SQL languages welcome).  
   Evidence: §3–§4; Pig→RelBuilder example

3. **ESTABLISHED-FOR-US:** Physical properties are modeled as **traits** (ordering, grouping, partitioning, **calling convention**); Calcite does **not** require separate logical vs physical operator entity classes.  
   Evidence: §4

4. **ESTABLISHED-FOR-US:** Adapters supply schemas/tables and planner rules that convert logical ops into backend **conventions**; **enumerable** convention provides iterator-based client operators when backends lack an op.  
   Evidence: §5; Fig. 2–3

5. **ESTABLISHED-FOR-US:** Cost-based planner uses dynamic programming **similar to Volcano**, registering expressions into equivalence sets via digests; also an exhaustive planner; engines pluggable; metadata providers supply cost/cardinality/selectivity.  
   Evidence: §6

6. **ESTABLISHED-FOR-US (related-work framing):** Calcite builds on Volcano (Graefe & McKenna 1993) and Cascades (Graefe 1995) ideas.  
   Evidence: §2 related work; Cascades PDF skimmed separately for vocabulary

## Anti-claims

- That RQL embeds Calcite or implements RelTraitDef / VolcanoPlanner.
- That journal 0023 capability profiles are a Cascades memo search.
- Any unreproduced Calcite benchmark numbers (paper is systems/architecture).
