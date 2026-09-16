---
type: Concept
title: Adapters and pushdown
tags: [calcite, adapters]
status: established
---

# Adapters and pushdown

An adapter = model + SchemaFactory + Schema/Tables (+ optional rules). Minimal surface: table scan in the backend convention; richer adapters push Filter/Sort/Join into the engine. Missing ops fall back to **enumerable** iterators in-process.

Fig. 4 (`FilterIntoJoinRule`) shows classical pushdown preserving semantics while enabling backend filters.

**RQL `[hypothesis]`:** Vendor emit stubs + ShimCast mirror “push what you can; mark client work explicitly” — without claiming Calcite’s rule engine.
