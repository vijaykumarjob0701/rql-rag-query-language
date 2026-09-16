---
type: FigureNote
title: Figure 4 — FilterIntoJoinRule
page: 5
---

# Fig. 4 — FilterIntoJoinRule

(a) Filter above Join → (b) Filter pushed to the join input that owns the predicate (sales), enabling cheaper join and potential backend pushdown.

**Grounds:** rule-based semantic-preserving rewrites; same spirit as RQL FilterExec placement `[hypothesis]`.
