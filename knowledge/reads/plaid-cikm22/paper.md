---
type: Paper
title: "PLAID: An Efficient Engine for Late Interaction Retrieval"
resource: https://arxiv.org/abs/2205.09707
tags: [plaid, cikm22, late-interaction, centroid-interaction, colbertv2]
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:05:00+01:00
status: provisional
---

# PLAID — Santhanam, Khattab, Potts, Zaharia (CIKM 2022) `[venue-verified]`

**Authors:** Keshav Santhanam*, Omar Khattab*, Christopher Potts, Matei Zaharia (*equal contribution; Stanford)  
**Venue:** CIKM ’22 (ACM); DOI [10.1145/3511808.3557325](https://doi.org/10.1145/3511808.3557325); pages 1747–1756 (camera-ready per reproducibility cites)  
**arXiv:** [2205.09707](https://arxiv.org/abs/2205.09707) v1, 19 May 2022 (local PDF = this preprint, **10 pages**)  
**Code:** https://github.com/stanford-futuredata/ColBERT (`fast_search` → merged to main)  
**Local:** `tooling/scripts/extract_out/plaid-2205.09707.pdf`

## Abstract (paraphrase)

PLAID (Performance-optimized Late Interaction Driver) accelerates ColBERTv2 late-interaction search without quality loss by treating each passage as a lightweight **bag of centroids**, applying **centroid interaction** and **centroid pruning** in a multi-stage pipeline, then residual decompression + exact MaxSim only on a tiny final set. Authors report up to **7× GPU / 45× CPU** latency reduction vs vanilla ColBERTv2 (AUTHOR numbers) at up to ~140M passages.

## Links
- Journal 0014; [claims](claims/key-claims.md); [equations](equations/centroid-interaction.md); [pipeline](algorithms/four-stage-pipeline.md); [RQL strategy](strategies/plaid-rewrite-for-rql.md).
