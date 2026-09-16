---
type: Paper
title: "Out-of-Domain Semantics to the Rescue! Zero-Shot Hybrid Retrieval Models"
resource: https://arxiv.org/abs/2201.10582
tags: [chen, ecir2022, hybrid, rrf, zero-shot]
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
status: provisional
---

# Zero-shot hybrid retrieval — Chen et al. (ECIR 2022) `[venue-verified DOI]`

**Authors:** Tao Chen, Mingyang Zhang, Jing Lu, Michael Bendersky, Marc Najork (Google Research)  
**Venue:** ECIR 2022, LNCS; DOI [10.1007/978-3-030-99736-6_7](https://doi.org/10.1007/978-3-030-99736-6_7); proceedings pp. **95–110**  
**arXiv:** 2201.10582v1 (25 Jan 2022) — local PDF used for page inventory (**16 pp** preprint layout)  
**Local:** `tooling/scripts/extract_out/chen-ecir2022-2201.10582.pdf`  
**Also:** https://marc.najork.org/papers/ecir2022.pdf  
**Bruch cite:** Bruch et al. reference **[5]** (journal 0016)

## Abstract (paraphrase)

Deep (BERT-style) retrievers beat lexical models in-domain but deteriorate under domain shift in zero-shot transfer; lexical models are more robust. Authors propose a non-parametric hybrid that fuses lexical (+expansion) and deep (NPR) rankings via **RRF**, reporting large relative Recall@1K gains vs deep alone and solid gains vs BM25 on three OOD sets.

## Links
- Journal 0017; [claims](claims/key-claims.md); [preference strategy](strategies/fuse-rrf-vs-linear-preference.md); [Eq. 1](equations/rrf-chen.md).
