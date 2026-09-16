---
type: Strategy
title: Steal BlinkDB dual contracts → RQL budget options (Hypothesis packaging)
tags: [blinkdb, rql, budgets]
generated:
  by: grok-bot/executor
  at: 2026-09-17T00:55:00+01:00
status: provisional
---

# Strategy: AQP budgets for RQL

## Steal (Established idea)
- Make approximation **declarative** in the query: error/confidence **or** latency bound.
- Maintain a profile (ELP) relating “effort” (sample size / candidates / ef) to quality and latency; pick the cheapest effort that meets the declared bound.
- Return / EXPLAIN the quality proxy actually achieved.

## Invent / package (Hypothesis for RQL)
- Surface: `OPTION RECALL TARGET r LATENCY …` (examples/10-hyde-rewrite-budget.rql).
- IR: PhysicalPlan `budgets.recallTarget` / `budgets.latencyMs` (schema v0.1.0-draft).
- Bind to retrieval knobs: ANN `ef`/`nprobe`/candidates, FilterExec mode, rewrite/rerank depth — **not** to Hive stratified samples.
- EXPLAIN must say which knobs moved and that recallTarget is a **proxy**, not a measured guarantee.

## Do not steal naively
- Do not import Table 2 variance formulas as recall@k estimators.
- Do not claim confidence intervals on ANN results from this paper alone.
