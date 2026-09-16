---
type: Equation
title: ColBERT MaxSim late-interaction score
tags: [colbert, maxsim, equation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
---

# Equation — \(S_{q,d}\) (MaxSim late interaction)

**Source:** Khattab & Zaharia, SIGIR 2020, §3.3 Eq. (3).

\[
S_{q,d} := \sum_{i \in [|E_q|]} \max_{j \in [|E_d|]} E_{q_i} \cdot E_{d_j}^{\top}
\]

- \(E_q\): bag of contextualized query embeddings (length \(N_q\), often 32; includes query-augmentation `[mask]` pads)  
- \(E_d\): bag of contextualized document embeddings (punctuation filtered)  
- Embeddings are **L2-normalized** so the dot product equals **cosine** similarity  
- Authors also evaluate **squared L2** as the vector similarity inside MaxSim (esp. end-to-end faiss path)

**Encoder sketches (Eqs. 1–2):** BERT + linear projection (“CNN” in paper notation) + Normalize; documents additionally Filter punctuation.

**RQL note:** This scoring definition is **[Established]** prior art for logical \(\mathrm{Search}_{late}\). Default physical realization (exhaustive MaxSim vs faiss candidate gen vs PLAID vs MUVERA FDE) is capability-dependent **[Hypothesis]**.
