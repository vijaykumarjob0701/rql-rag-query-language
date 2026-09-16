---
type: Strategy
title: Fuse_rrf implications for RQL
tags: [rrf, fuse, rql]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:55:00+01:00
---

# Strategy — \(\mathrm{Fuse}_{rrf}\) for RQL

## Established (steal)

- Formula \(\sum 1/(k+r(d))\); default \(k=60\); 1-based ranks.
- Rank-only fusion when dense/BM25/late scores are not calibrated.
- Portable across backends that already expose RRF (Qdrant, Milvus, ES/OS, Redis, Turbopuffer, SQL CTEs).

## Hypothesis (RQL packaging)

- Name the logical op \(\mathrm{Fuse}_{rrf}(k_{\mathrm{rrf}})\) in the evidence algebra.
- Compile to vendor fusion primitives or local fuse over channel-local rankings.
- Keep \(\mathrm{Fuse}_{linear}\) / learned fuse as siblings when scores are comparable (Bruch — not this paper).
- EXPLAIN must show \(k\) and input channel ranks, not opaque “hybrid=on”.

## Do not

- Copy Cormack MAP tables into RQL eval as reproduced.
- Claim RQL invents RRF.
- Silently drop channels that omit ranks.
