---
type: FigureNote
title: Substrait docs structure map (no PDF figure)
tags: [substrait, inventory]
---

# Spec map (Pass 2 stand-in)

Substrait’s primary artifacts are **HTML specification pages**, not a single camera-ready PDF. For multimodal protocol fidelity we inventory the section graph:

```
Home / About
  └─ Spec
       ├─ Types / Type variations / User-defined types
       ├─ Relations
       │    ├─ Basics (Emit, Hints, Constraints, distribution, orderedness)
       │    ├─ Logical relations (Read, Filter, Project, Join, Aggregate, …)
       │    ├─ Physical relations (HashJoin, Exchange, TopN, …)  ← conventional
       │    └─ User-defined / Embedded (pending / designed)
       ├─ Extensions (YAML + Advanced + Extension*Rel)
       └─ Serialization (binary Plan, text)
```

No raster “Figure N” in the project docs for this pass; relation to Calcite Fig.1 is conceptual (parser → plan → engines), not a shared figure.
