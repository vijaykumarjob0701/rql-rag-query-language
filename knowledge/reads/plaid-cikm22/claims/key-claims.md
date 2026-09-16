---
type: ClaimSet
title: PLAID key claims (evidence-linked)
tags: [plaid, claims, centroid-interaction]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:05:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper states it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (mechanism):** PLAID scores with a **4-stage pipeline** (Fig 5): (1) candidate generation via top-`nprobe` centroids per query token → passage IDs; (2) **centroid interaction with pruning** (`t_cs`) → TopK(`ndocs`); (3) **centroid interaction without pruning** → TopK(`ndocs/4`); (4) residual decompression + exact MaxSim → TopK(`k`).  
   Evidence: §4; Fig 5; [../algorithms/four-stage-pipeline.md](../algorithms/four-stage-pipeline.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (mechanism):** **Centroid interaction** approximates MaxSim by substituting each passage token embedding with its nearest centroid ID and looking up precomputed query–centroid scores \(S_{c,q}=C Q^\top\) (Eq. 2–4).  
   Evidence: §4.2 Eqs. (2)–(4); [../equations/centroid-interaction.md](../equations/centroid-interaction.md)

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (mechanism):** **Centroid pruning** drops tokens whose max query–centroid score \(< t_{cs}\) before building the approximate bag (Eq. 5); used in Stage 2 only.  
   Evidence: §4.3 Eq. (5); Fig 4 motivation (heavy-tailed centroid scores)

4. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (motivation):** Centroid-only retrieval at depth \(10\cdot k\) recovers **99%+** of vanilla ColBERTv2’s top-\(k\) passages (in-domain MS MARCO v1 and OOD LoTTE pooled) — AUTHOR Fig 3 analysis.  
   Evidence: §3.3 Fig 3 — **analysis claim, unreproduced**

5. **AUTHOR-CLAIM (not reproduced):** vs vanilla ColBERTv2, PLAID reports up to **~7× GPU / ~45× CPU** latency cut at matched quality (abstract; Table 3 \(k=1000\) narrative: 6.8× GPU / 45× CPU on MS MARCO v1).  
   Evidence: Abstract; §5.2 Table 3 — **do not cite as our measurement**

6. **AUTHOR-CLAIM (not reproduced):** Ablation Fig 6 — GPU cumulative ~3.7× (centroid interaction) → 5.2× (+pruning) → 6.6× (+fast decompression); CPU ~4.2× → 8.6× → 42.4× (+fast kernels).  
   Evidence: §5.3 Fig 6 — AUTHOR-only

7. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (engineering):** Inverted list maps centroids→**passage IDs** (not embedding IDs); padding-free MaxSim C++ kernels (CPU); LUT residual decompression (CPU+CUDA).  
   Evidence: §4.1, §4.5

## Anti-claims
- That we reproduced MS MARCO / Wikipedia / LoTTE / MS MARCO v2 latencies or quality.
- That every multi-vector backend ships PLAID’s 4 stages.
- That PLAID replaces MaxSim semantics — Stage 4 still uses ColBERT Eq. (1) MaxSim on residuals.
