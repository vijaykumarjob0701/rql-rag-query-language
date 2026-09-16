---
type: ClaimSet
title: ACORN key claims (evidence-linked)
description: Claims we are willing to cite carefully, with figure/section anchors.
tags: [acorn, claims]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T12:14:00+01:00
---

# Key claims

Label legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Pre-filtering scales poorly as \(|X_p|\) grows; post-filtering needs search-scope expansion and suffers under low selectivity or low query–predicate correlation.  
   Evidence: §1, §3.2; [fig-02-query-correlation.md](../figures/fig-02-query-correlation.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Specialized indices (e.g. Filtered-DiskANN) can outperform pre/post but constrain predicate cardinality (~1k) and equality-style operators.  
   Evidence: §1; related work §8

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Ideal hybrid performance with HNSW would be an **oracle partition** index over \(X_p\) with complexity scaling like \(O_s(\log s n + K)\), but building one index per predicate is impractical for unknown/high-cardinality predicates.  
   Evidence: §4; [fig-03-predicate-subgraph.md](../figures/fig-03-predicate-subgraph.md)

4. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** ACORN searches the **predicate subgraph** of a denser predicate-agnostic graph to approximate oracle-partition search.  
   Evidence: §5; Alg. 2; Fig. 3–4

5. **AUTHOR-CLAIM (not reproduced):** ACORN-γ achieves **2–1,000× higher QPS** at ~0.9 recall vs prior methods across evaluated datasets; ACORN-1 approximates with substantially lower TTI.  
   Evidence: abstract, §7, §9; [fig-07-08-recall-qps.md](../figures/fig-07-08-recall-qps.md) — **do not cite as our measurement**

## Anti-claims (what we refuse to assert)

- That every production vector DB should ship ACORN.
- That RQL runtime embeds ACORN.
- Any fabricated microbenchmark numbers.
