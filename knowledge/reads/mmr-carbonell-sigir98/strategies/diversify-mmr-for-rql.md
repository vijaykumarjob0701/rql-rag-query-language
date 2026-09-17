---
type: Strategy
title: Steal MMR formula → RQL Diversify_mmr / DIVERSIFY MMR (Hypothesis packaging)
tags: [mmr, rql, diversify]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:20:00+01:00
status: provisional
---

# Strategy: MMR diversify for RQL

## Steal (Established idea)
- Greedy incremental selection maximizing **marginal relevance** = relevance − redundancy.
- Single scalar **λ** trades pure relevance (1) vs pure diversity (0).
- Allow distinct Sim₁ (to query) and Sim₂ (to selected set); cosine is the paper’s summarization default.
- Place after a retrieved set R exists — reorder / select subset, do not replace retrieval itself.

## Invent / package (Hypothesis for RQL)
- Surface: `DIVERSIFY MMR` with optional `λ=…` (and future Sim hints) as a plan node on evidence `E`.
- Algebra: \(\mathrm{Diversify}_{mmr}(\lambda): E \rightarrow E\).
- Typical compose: `Search_*` / `Fuse_*` → `Diversify_mmr` → optional `Rerank` / `Expand`.
- EXPLAIN must show λ, Sim choices, and that Table 1 / SUMMAC numbers are not claimed from this read.

## Do not steal naively
- Do not paste Table 1 or SUMMAC F=.73 as RQL results.
- Do not confuse with `Fuse_rrf` / `Fuse_condorcet` / `Fuse_linear` (multi-channel merge ≠ within-list diversity).
- Do not claim a universal default λ — paper suggests task-dependent (explore ~0.3, focus ~0.7).
