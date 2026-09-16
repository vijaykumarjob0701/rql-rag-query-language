---
type: Playbook
title: Iterator ANN and VSIM JOIN implications for RQL (hypothesis)
status: hypothesis
tags: [rql, hypothesis, vbase, iterative, vsim-join]
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:48:00+01:00
---

# Iterator + VSIM JOIN implications `[hypothesis]`

Aligns with provisional [`docs/07-evolved-idea.md`](../../../../docs/07-evolved-idea.md) and ACORN strategy table.

| VBASE idea | Hypothesized RQL mapping |
|------------|--------------------------|
| Open/Next/Close ANN | Capability `ann_iterator`; physical `FilterExec=ITERATIVE` |
| Filter during traversal | Prefer over POST+blind over-fetch when iterator available |
| Distance range stop + RM | Physical range leaf / stop condition attributes |
| Vector Join via range index-join | Physical realization of logical `VSimJoin` when adapter supports it |
| Multi-column TopK / NRA-style | Future `Fuse` / multi-channel planner (unread depth) |

## Hard constraints

- ACL / tenant predicates: still mandatory server-side; RM early-stop must not drop required survivors — planner conservatism when stats missing.
- `EXPLAIN` should name `ITERATIVE` vs `POST`/`SUBGRAPH`/`SPECIALIZED`.

## Links

- Companion ACORN modes: [`../../acorn-2403.04871/strategies/filter-strategy-implications-for-rql.md`](../../acorn-2403.04871/strategies/filter-strategy-implications-for-rql.md)
- Filtered-DiskANN specialized: [`../../filtered-diskann-www23/strategies/specialized-label-graphs-for-rql.md`](../../filtered-diskann-www23/strategies/specialized-label-graphs-for-rql.md)
