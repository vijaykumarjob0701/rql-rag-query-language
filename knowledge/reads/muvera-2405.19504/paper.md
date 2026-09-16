---
type: Paper
title: "MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings"
resource: https://arxiv.org/abs/2405.19504
tags: [muvera, fde, multi-vector, google-research]
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
status: provisional
---

# MUVERA — Dhulipala et al. (arXiv:2405.19504) `[arxiv-verified]`

**Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram (corr.), Jason Lee, Vahab Mirrokni (Google Research / DeepMind / UMD)  
**Version read:** arXiv 2405.19504v2 [cs.DS] (PDF stamp 8 Jun 2026); **26 pages**  
**Venue note:** Bib lists NeurIPS 2024 per Google Research pubs page — verify camera-ready before citing venue as final.  
**Local:** `tooling/scripts/extract_out/muvera-2405.19504.pdf`

## Abstract (paraphrase)

MUVERA reduces multi-vector similarity search to single-vector MIPS by mapping query/document embedding bags to Fixed Dimensional Encodings (FDEs) whose inner product approximates Chamfer (= MaxSim) similarity, with ε-approximation theorems, then optional Chamfer rerank. Authors report fewer candidates than the SV heuristic and favorable BEIR recall/latency vs PLAID — AUTHOR-only.

## Links
- Journal 0013; [claims](claims/key-claims.md); [equations](equations/chamfer-and-fde.md); [rewrite strategy](strategies/fde-rewrite-for-rql.md).
