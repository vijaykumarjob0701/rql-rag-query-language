---
type: ClaimSet
title: VBASE key claims (evidence-linked)
tags: [vbase, claims]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:48:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Popular ANN indices (IVFFlat, HNSW) lack classical monotonicity; distance-vs-steps oscillates, motivating tentative TopK wrappers.  
   Evidence: §2.2, §3.1; [../figures/fig-01-traversal-patterns.md](../figures/fig-01-traversal-patterns.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Practical traversals show a **two-phase** pattern; **Relaxed Monotonicity** (Def. 1) compares neighbor-sphere radius \(R_q\) to window median \(M^s_q\).  
   Evidence: Eqs. 1–3; [../figures/fig-02-relaxed-monotonicity.md](../figures/fig-02-relaxed-monotonicity.md)

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Unified engine uses Volcano **Open / Next / Close**, adapting ANN internal traversal; terminate when operator condition ∧ RM check.  
   Evidence: §3.2, §4.2; [../algorithms/open-next-close.md](../algorithms/open-next-close.md)

4. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Enables S1–S4 online query classes and vector Join via distance range + index join; prior systems incomplete per Table 1.  
   Evidence: §2.1, Table 1; [../tables/table-01-query-support.md](../tables/table-01-query-support.md)

5. **AUTHOR-CLAIM (not reproduced):** Up to ~three orders-of-magnitude latency improvement on complex online queries; ~7000× on a join-style workload vs brute scan at high recall.  
   Evidence: abstract, §5, §7 — **do not cite as our measurement**

## Anti-claims

- That every vector DB implements VBASE.
- Fabricated microbench numbers.
- That RM early-stop is always ACL-safe without planner constraints.
