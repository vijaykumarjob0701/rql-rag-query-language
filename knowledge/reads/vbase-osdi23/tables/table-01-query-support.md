---
type: TableNote
title: "Table 1 — Online Similarity Query Support for Vectors"
status: provisional
---

# Table 1 — Query support matrix

**What it measures:** Systems × query classes S1 (single TopK), S2 (TopK+scalar filter), S3 (multi-column TopK), S4 (vector similarity / range filter).  
**Author point:** No prior listed system covers all online classes efficiently; some rely on exhaustive scan.  
**Honesty:** Cells paraphrased from extract; do not invent additional checkmarks.  
**RQL note `[hypothesis]`:** Capability negotiation should advertise which of S1–S4 / Join a backend adapter supports.
