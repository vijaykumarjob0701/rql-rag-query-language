---
type: Playbook
title: FilterExec packaging from FANNS survey taxonomy
description: Map ESTABLISHED Lin et al. 2025 VSP/VJP/SJP/SSP (+ A1–A17) to hypothesized RQL FilterExec modes.
tags: [rql, hypothesis, fanns, filter-mode, taxonomy]
status: hypothesis
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# FilterExec from FANNS taxonomy `[hypothesis packaging]`

**Established (survey):** pruning strategies VSP / VJP / SJP / SSP; algorithm families A1–A17; difficulty = selectivity × distribution (ID/POD/OOD); §6.3 multi-algorithm combination as open system direction.

**Hypothesis (RQL):** physical mode names and planner policy. Cross-check ACORN/VBASE/Filtered-DiskANN OKFs (journals 0006/0009/0010).

| Survey anchor | FilterExec mode | When (sketch) |
|---------------|-----------------|---------------|
| SSP / A12 Pre-Filtering | `PRE` | High selectivity; survivor set scannable |
| VSP / A1 Post-Filtering | `POST` | Low selectivity / cheap over-fetch; watch empty-result risk |
| VSP / A2 VBase | `ITERATIVE` | Open/Next + relaxed monotonicity capability |
| VJP / A4 ACORN | `SUBGRAPH` | Predicate-subgraph / dense predicate-agnostic graph capability |
| VJP / A9 Filtered-DiskANN (+ A10–A11 class) | `SPECIALIZED` | Equality/range label graphs matching advertised predicates |
| SJP / A13–A14 (+ multi-subset SJP) | `PARTITION` | Workload-stable partitions / multi-subset indices |
| §6.3 combination + selectivity routers | `ROUTER` | Multiple FANNS implementations coexist; pick per query |
| Stats + capability negotiation | `AUTO` | Choose among advertised modes; **never** drop ACL hard constraints |

## EXPLAIN vocabulary (suggested)

- `pruning_strategy ∈ {VSP, VJP, SJP, SSP}` (survey)
- `filter_exec ∈ {PRE, POST, ITERATIVE, SUBGRAPH, SPECIALIZED, PARTITION, ROUTER, AUTO}` (RQL)
- `selectivity_hat`, optional `distribution_factor ∈ {ID, POD, OOD, unknown}`
- `fallback` chain when capability missing

## Hard constraints

- ACL / tenant predicates: server-side enforcement regardless of QPS.
- Missing SUBGRAPH/SPECIALIZED/PARTITION/ITERATIVE/ROUTER → documented fallback (often POST+overfetch or PRE), never pretend.

## Anti-overclaim

- No survey QPS copied as RQL results.
- Fig 1 thumbs ≠ calibrated cost model.
- NHQ/HQANN ≠ FilterExec.
