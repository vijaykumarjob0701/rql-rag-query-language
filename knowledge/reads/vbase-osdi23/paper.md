---
type: Paper
title: "VBASE: Unifying Online Vector Similarity Search and Relational Queries via Relaxed Monotonicity"
description: Primary paper concept for the VBASE multimodal read (OSDI 2023).
resource: https://www.usenix.org/system/files/osdi23-zhang-qianxi_1.pdf
tags: [vbase, osdi, postgresql, hnsw, iterator, relaxed-monotonicity]
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:48:00+01:00
status: provisional
sources:
  - url: https://www.usenix.org/conference/osdi23/presentation/zhang-qianxi
    note: USENIX presentation page
  - url: https://www.usenix.org/system/files/osdi23-zhang-qianxi_1.pdf
    note: Camera PDF (20 pp)
  - url: https://github.com/microsoft/MSVBASE
    note: Open-source lineage (code not deeply read this pass)
---

# VBASE (Zhang et al., OSDI 2023) `[venue-verified]`

**Authors:** Qianxi Zhang, Shuotao Xu, Qi Chen, Guoxin Sui, Jiadong Xie, Zhizhen Cai, Yaoqi Chen, Yinxuan He, Yuqing Yang, Fan Yang, Mao Yang, Lidong Zhou (Microsoft Research Asia + affiliations)  
**Venue:** 17th USENIX OSDI, July 2023, Boston; proceedings pp. 377–395  

## Abstract (paraphrase)

High-dimensional vector indices lack classical monotonicity, pushing systems toward TopK-only tentative indices with hard-to-predict \(K\). VBASE identifies **relaxed monotonicity**, builds a unified Volcano-style engine over scalar and vector indices via **`Next`**, and claims much higher efficiency on complex online vector+relational queries while preserving TopK semantics (with an equivalence argument). Also enables analytical similarity queries (e.g. vector join) prior systems lack.

## Links in this bundle

- Claims: [claims/key-claims.md](claims/key-claims.md)
- Iterator / VSIM JOIN implications: [strategies/iterator-and-vsimjoin-for-rql.md](strategies/iterator-and-vsimjoin-for-rql.md)
- Journal: [../../../journal/0009-vbase-multimodal-reread.md](../../../journal/0009-vbase-multimodal-reread.md)

## Extraction honesty

Embedded rasters ≠ all paper figures; several XObjects unusable. Prefer captions + body + pdftoppm page views.
