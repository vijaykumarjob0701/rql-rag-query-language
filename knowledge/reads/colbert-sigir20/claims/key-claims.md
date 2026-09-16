---
type: ClaimSet
title: ColBERT key claims (evidence-linked)
tags: [colbert, claims, maxsim]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Late interaction scores \(S_{q,d}=\sum_i\max_j E_{q_i}\cdot E_{d_j}^\top\) (MaxSim-sum; cosine via L2-normalized embeddings; squared L2 also evaluated).  
   Evidence: §3.1–3.3 Eq. (3); [../equations/maxsim-late-interaction.md](../equations/maxsim-late-interaction.md); [../figures/fig-02-matching-paradigms.md](../figures/fig-02-matching-paradigms.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Query and document encoders are independent; document bags \(E_d\) can be computed **offline**; interaction has no trainable parameters.  
   Evidence: §3.2–3.4; [../figures/fig-03-architecture.md](../figures/fig-03-architecture.md)

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (mechanism):** MaxSim is pruning-friendly → end-to-end retrieval via vector-similarity index (faiss IVFPQ) then exhaustive MaxSim refine.  
   Evidence: §3.6

4. **AUTHOR-CLAIM (not reproduced):** On MS MARCO re-ranking, ColBERT ≈ BERT_base MRR@10 at ~170× lower latency / ~14,000× fewer FLOPs vs BERT re-rankers (Table 1; Fig 1).  
   Evidence: Table 1 — **do not cite as our measurement**

5. **AUTHOR-CLAIM (not reproduced):** End-to-end ColBERT_L2 improves MRR/Recall vs BM25/doc2query/DeepCT/docTTTTTquery on authors’ setup (Table 2).  
   Evidence: Table 2

6. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (ablation narrative):** Late interaction, MaxSim (vs averages), and query augmentation ([mask] padding) are essential to reported effectiveness (§4.4).  
   Evidence: §4.4

## Anti-claims

- That we reproduced MS MARCO / TREC CAR metrics.
- That every vector DB implements multi-vector MaxSim natively.
- That faiss IVFPQ is the only admissible physical plan for `Search_late`.
