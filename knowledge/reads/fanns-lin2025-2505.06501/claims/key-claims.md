---
type: ClaimSet
title: FANNS survey key claims (evidence-linked)
tags: [fanns, claims, taxonomy]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (mechanism/taxonomy), not that we reproduced experiments.

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Coarse pre-/post-/in-filtering is insufficient; FANNS algorithms should be classified by **dominant pruning behaviour**: **VSP, VJP, SJP, SSP**.  
   Evidence: §3.1; Fig 1; [../figures/fig-01-pruning-framework.md](../figures/fig-01-pruning-framework.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Framework classifies **17** algorithms **A1–A17** with interrelationships (Fig 2): Post-Filtering, VBase, AIRSHIP, ACORN, Faiss-IVF, CAPS, NHQ, HQANN, Filtered-DiskANN, SeRF, iRangeGraph, Pre-Filtering, Milvus-Partition, HQI, MA-NSW, UNG, WST.  
   Evidence: §3.2–3.5; Fig 2; [../algorithms/a1-a17-families.md](../algorithms/a1-a17-families.md)

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (regime):** VSP suits **unselective** filters (weak on highly selective); SSP opposite; VJP/SJP aim at **varying** selectivity under restrictive assumptions / reliability caveats.  
   Evidence: Fig 1 thumbs; §3.2–3.5 prose

4. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Hybrid query difficulty needs **selectivity + distribution** (ID / POD / OOD), not selectivity alone; Figs 3–6 develop the schema.  
   Evidence: §5; Figs 3–6; [../figures/fig-03-06-query-difficulty.md](../figures/fig-03-06-query-difficulty.md)

5. **AUTHOR-CLAIM (not reproduced):** Oracle-partition IVF/HNSW recall curves on MNIST-8M / MTG show ID vs POD vs OOD gaps (Fig 3).  
   Evidence: Fig 3 — **do not cite as our measurement**

6. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (open direction):** §6.3 — combining multiple FANNS algorithms and **dynamically selecting** per hybrid query (selectivity cost models in ADBV/Milvus/VBase; ACORN→Pre-Filtering at high selectivity) is a promising system-level direction.  
   Evidence: §6.3

7. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Formal defs of hybrid dataset, hybrid query \(q=(f_s,f_v,v_q,k)\), selectivity, recall@k (Table 1 / §2).  
   Evidence: §2; Table 1

## Anti-claims

- That we reproduced Fig 3–6 empirics or any QPS/speedup tables (survey is primarily taxonomic; no fabricated RQL metrics).
- That VSP/VJP/SJP/SSP are RQL opcodes (they are survey strategies; FilterExec names are `[hypothesis]` packaging).
- That NHQ/HQANN fusion-distance is a FilterExec mode (index/fusion mechanism, not PRE/POST).
- That every backend implements SUBGRAPH/SPECIALIZED/PARTITION/ROUTER.
