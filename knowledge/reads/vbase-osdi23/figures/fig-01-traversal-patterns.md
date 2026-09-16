---
type: FigureNote
title: "Figure 1 — Traversal patterns of two vector indices"
status: provisional
---

# Fig. 1 — Traversal patterns `[viewed]`

**Caption:** Traversal patterns of two vector indices.  
**Panels:** (a) FAISS IVFFlat; (b) HNSW — distance to query vs traversal steps (oscillatory).  
**Role:** Introduces lack of classical monotonicity and the informal two-phase pattern used to motivate relaxed monotonicity (§3.1).  
**Viewed:** pdftoppm page containing Fig. 1–2 (OSDI proceedings page ~380).  
**RQL note `[hypothesis]`:** Physical `ITERATIVE` mode needs an early-stop signal analogous to phase-2 detection — backend-specific.
