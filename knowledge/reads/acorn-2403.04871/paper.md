---
type: Paper
title: "ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data"
description: Primary paper concept for the ACORN multimodal read.
resource: https://arxiv.org/abs/2403.04871
tags: [acorn, hybrid-search, hnsw, filtered-ann, arxiv]
generated:
  by: grok-bot/executor
  at: 2026-09-16T12:14:00+01:00
status: provisional
sources:
  - url: https://arxiv.org/abs/2403.04871
    note: abs page
  - url: https://arxiv.org/pdf/2403.04871.pdf
    note: PDF v1 dated 7 Mar 2024
---

# ACORN (Patel et al., 2024) `[arxiv-only]`

**Authors:** Liana Patel, Peter Kraft, Carlos Guestrin, Matei Zaharia  
**arXiv:** 2403.04871v1 [cs.IR] 7 Mar 2024  

## Abstract (paraphrase, not verbatim dump)

Applications need joint search over embeddings and structured attributes. Existing hybrid methods either perform poorly or only support restricted predicates (e.g. small equality sets). ACORN extends HNSW with **predicate subgraph traversal** and a **predicate-agnostic** denser construction (ACORN-γ for search efficiency; ACORN-1 for lower build cost). Authors report state-of-the-art throughput at fixed recall across prior low-cardinality benchmarks and harder high-cardinality multimodal workloads.

## Links in this bundle

- Key claims: [claims/key-claims.md](claims/key-claims.md)
- Predicate subgraph figure: [figures/fig-03-predicate-subgraph.md](figures/fig-03-predicate-subgraph.md)
- RQL filter-strategy implications: [strategies/filter-strategy-implications-for-rql.md](strategies/filter-strategy-implications-for-rql.md)
- Journal write-up: [../../../journal/0006-acorn-multimodal-reread.md](../../../journal/0006-acorn-multimodal-reread.md)

## Extraction honesty

Local inventory lists 30 embedded rasters; many paper figures are vector drawings. Tables did not extract to CSV. Prefer captions + body citations over automated table dumps.
