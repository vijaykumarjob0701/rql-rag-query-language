---
type: FigureNote
title: Fig 2 — classification of 17 FANNS algorithms under VSP/VJP/SJP/SSP
page: 7
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Fig 2 — A1–A17 classification `[Established taxonomy]`

**Caption:** “Classification of FANNS algorithms under the pruning-focused framework and interrelationships among them.”

**Layout (page-07 PNG):** Four columns VSP | VJP | SJP | SSP. Box style encodes index family (graph / IVF / general); fill encodes filter assumption (general / equality / range).

| Column | Algorithms (paper IDs) |
|--------|-------------------------|
| VSP | **A1** Post-Filtering family; **A2** VBase (refines A1) |
| VJP | **A3** AIRSHIP; **A4** ACORN; **A5** Faiss-IVF; **A6** CAPS; **A7** NHQ; **A8** HQANN; **A9** Filtered-DiskANN; **A10** SeRF; **A11** iRangeGraph |
| SSP | **A12** Pre-Filtering family |
| SJP | **A13** Milvus-Partition; **A14** HQI; **A15** MA-NSW; **A16** UNG; **A17** WST |

**Interrelationships (arrows):** A12 related to A1/A13/A15; within VJP: A3↔A4, A5↔A6, A7/A8→A9, A10→A11.

**RQL `[hypothesis]`:** Primary FilterExec anchors — A1→POST, A2→ITERATIVE, A4→SUBGRAPH, A9→SPECIALIZED, A12→PRE, A13/A14→PARTITION; §6.3 multi-algo → ROUTER/AUTO. NHQ/HQANN (A7–A8) are fusion-distance mechanisms, not FilterExec.
