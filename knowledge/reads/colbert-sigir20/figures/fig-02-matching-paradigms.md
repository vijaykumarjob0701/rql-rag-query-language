---
type: Figure
title: "Figure 2 — Query–document matching paradigms"
tags: [colbert, figure, maxsim]
status: provisional
---

# Figure 2

**(a)** Representation-based (single vectors + similarity)  
**(b)** Early interaction matrix models (DRMM/KNRM/…)  
**(c)** All-to-all deep interaction (BERT cross-encoder)  
**(d)** **Late interaction (ColBERT):** bags of embeddings + per-query-embedding **MaxSim** + Σ

**Use for RQL:** Canonical diagram for why late interaction is neither pure dense ANN nor cross-encoder rerank.
