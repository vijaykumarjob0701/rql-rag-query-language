---
type: Figure
title: "Figure 4 — ACORN neighbor selection strategies"
description: Filter vs compression-based heuristic vs neighbor expansion during search.
tags: [acorn, figure, physical-ops]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T12:14:00+01:00
---

# Figure 4

**Caption:** Diagram of ACORN’s neighbor selection strategies. Blue nodes pass the query predicate. Subfigures include filter over expanded neighbors, compression heuristic, and neighbor expansion.

**Links:** Implements search described with [../algorithms/alg-02-acorn-search-layer.md](../algorithms/alg-02-acorn-search-layer.md).

**RQL `[hypothesis]`:** These are *intra-operator* physical variants under `FilterExec=SUBGRAPH`, not separate logical algebra ops.
