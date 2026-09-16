---
type: Playbook
title: Specialized label-graph implications for RQL (hypothesis)
status: hypothesis
---

# Specialized mode `[hypothesis]`

| Literature | RQL physical mode | When (sketch) |
|------------|-------------------|---------------|
| Filtered/Stitched Vamana | `FilterExec=SPECIALIZED` | Predicate ≈ label/equality set supported by index; cardinality in advertised limits |
| Post-filter baselines | `POST` | High specificity / cheap over-fetch |
| ACORN subgraph | `SUBGRAPH` | Predicate-agnostic backend |
| VBASE iterator | `ITERATIVE` | Open/Next + early-stop |

**Capability negotiation:** advertise `filtered_graph_labels=true`, max \|F\|, multi-label points, whether ranges/OR/AND beyond labels are supported (paper leaves complex SQL open).
