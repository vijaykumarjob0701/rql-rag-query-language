---
type: Paper
title: "The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries"
resource: https://doi.org/10.1145/290941.291025
tags: [mmr, diversity, sigir98, carbonell]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:20:00+01:00
status: provisional
---

# MMR — Carbonell & Goldstein (SIGIR 1998) `[venue-verified]`

**Authors:** Jaime Carbonell, Jade Goldstein (Language Technologies Institute, CMU)  
**Venue:** SIGIR ’98, Melbourne, Australia; pages 335–336; DOI 10.1145/290941.291025; ACM ISBN 1-58113-015-5  
**PDF read:** CMU author copy (2 pp) — https://www.cs.cmu.edu/~jgc/publication/MMR_DiversityBased_Reranking_SIGIR_1998.pdf  
**Local:** `tooling/scripts/extract_out/mmr-carbonell-sigir98.pdf` · bundle copy `MMR_DiversityBased_Reranking_SIGIR_1998.pdf`

## Abstract (paraphrase)

MMR combines query relevance with information novelty for document reordering and passage selection in summarization. A document has high *marginal relevance* if it is relevant to the query and minimally similar to already selected documents. Preliminary AUTHOR results claim some benefit for retrieval and single-document summarization, SUMMAC support for the latter, and clearest advantage for non-redundant multi-document summaries (unreproduced here).

## Links
- Journal 0033; [claims](claims/key-claims.md); [MMR→RQL strategy](strategies/diversify-mmr-for-rql.md); [MMR formula](equations/mmr-definition.md).
