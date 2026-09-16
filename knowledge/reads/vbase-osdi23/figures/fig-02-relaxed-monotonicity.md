---
type: FigureNote
title: "Figure 2 — Relaxed Monotonicity intuition"
status: provisional
---

# Fig. 2 — RM intuition `[viewed]`

**Caption (paper):** Illustration of Relaxed Monotonicity’s intuition (neighbor sphere of \(q\) with radius \(R_q\); traversal window; median \(M^s_q\)).  
**Equations:** (1) \(R_q=\mathrm{Max}(\mathrm{TopE}(\{\mathrm{Distance}(q,v_j)\}))\); (2) \(M^s_q=\mathrm{Median}\) over window \(w\); (3) Def.1 \(\exists s\,\forall t\ge s: M^t_q \ge R_q\).  
**Role:** Formal early-stop predicate for iterator ANN.  
**RQL note `[hypothesis]`:** Optimizer may expose RM hyperparameters (\(E\), \(w\)) as physical hints — not part of logical algebra.
