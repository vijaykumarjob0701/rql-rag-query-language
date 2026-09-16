---
type: Paper
title: "Precise Zero-Shot Dense Retrieval without Relevance Labels"
resource: https://doi.org/10.18653/v1/2023.acl-long.99
tags: [hyde, dense-retrieval, zero-shot, acl2023]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:10:00+01:00
status: provisional
---

# HyDE — Gao et al. (ACL 2023) `[venue-verified]`

**Authors:** Luyu Gao, Xueguang Ma, Jimmy Lin, Jamie Callan  
**Venue:** ACL 2023 (Volume 1: Long Papers), Toronto; pages 1762–1777; DOI 10.18653/v1/2023.acl-long.99; Anthology 2023.acl-long.99  
**Preprint read:** arXiv:2212.10496v1 (11 pp; 20 Dec 2022)  
**Local:** `tooling/scripts/extract_out/hyde-2212.10496.pdf`  
**Code:** https://github.com/texttron/hyde

## Abstract (paraphrase)

HyDE builds fully zero-shot dense retrieval without relevance labels by pivoting through **Hypothetical Document Embeddings**: an instruction-following LM (e.g. InstructGPT) generates a hypothetical answer document; an unsupervised contrastive encoder (e.g. Contriever) embeds it; real corpus documents are retrieved by vector similarity in document space. The encoder’s dense bottleneck filters hallucinated details. AUTHOR experiments claim large gains over Contriever across web search, BEIR, and Mr.TyDi languages (unreproduced here).

## Links
- Journal 0032; [claims](claims/key-claims.md); [HyDE→RQL strategy](strategies/hyde-rewrite-for-rql.md); [Eqs. 5–8](equations/hyde-query-vector.md).
