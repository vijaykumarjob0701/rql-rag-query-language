---
type: FigureNote
title: Figs 3–6 — selectivity × distribution (ID/POD/OOD) query difficulty
pages: [13, 16]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Figs 3–6 — Query difficulty schema `[Established framing; AUTHOR empirics]`

## Fig 3 (p.13) — Oracle partition performance
Recall@10 vs nprobe/efSearch on MNIST-8M and MTG with **oracle partition indices** (IVFFlat + HNSWFlat). Marker shape encodes distribution relation of query set: **ID / POD / OOD**.

**AUTHOR-only:** numeric curves unreproduced here.

## Fig 4 (p.13) — UMAP
MNIST-8M: digit-filtered subsets form separated clusters. MTG: rarity-filtered subsets heavily overlap.

## Fig 5 (p.13) — Mahalanobis histograms
Base–base vs query–base distance histograms per “x-y” hybrid query set; supports ID/POD/OOD narrative.

## Fig 6 (p.16) — Two-factor schema
3×3 grid **Q1–Q9**: rows = selectivity (unselective / medium / selective); columns = distribution (ID / POD / OOD). Blue = filter-passing base vectors; white = others; green star = query.

**RQL `[hypothesis]`:** Planner signals for AUTO/ROUTER — estimate **selectivity** *and* a **distribution/correlation** proxy (ACORN journal 0006 correlation; survey ID/POD/OOD). Prefer PRE when selective+cheap subset; avoid naive POST under selective+OOD; consider SUBGRAPH/SPECIALIZED/PARTITION when capability matches predicate class. Do not invent numeric thresholds from Fig 3.
