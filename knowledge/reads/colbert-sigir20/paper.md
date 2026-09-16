---
type: Paper
title: "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT"
resource: https://arxiv.org/abs/2004.12832
tags: [colbert, sigir20, late-interaction, maxsim]
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
status: provisional
---

# ColBERT — Khattab & Zaharia (SIGIR 2020) `[venue-verified]`

**Authors:** Omar Khattab, Matei Zaharia (Stanford University)  
**Venue:** SIGIR ’20, July 25–30, 2020; ACM DOI 10.1145/3397271.3401075  
**arXiv:** 2004.12832v2 [cs.IR] 4 Jun 2020  
**Local:** `tooling/scripts/extract_out/colbert-sigir20.pdf` (**10 pages**)

## Abstract (paraphrase)

ColBERT adapts BERT for efficient passage retrieval via **late interaction**: independent query/document encoders produce bags of contextualized embeddings; relevance is a cheap MaxSim-based interaction that supports offline document indexing and pruning-friendly end-to-end retrieval. Authors report effectiveness competitive with BERT re-rankers at far lower latency/FLOPs on MS MARCO and TREC CAR.

## Links
- Journal 0012; [claims](claims/key-claims.md); [MaxSim equation](equations/maxsim-late-interaction.md); [RQL strategy](strategies/late-interact-for-rql.md).
