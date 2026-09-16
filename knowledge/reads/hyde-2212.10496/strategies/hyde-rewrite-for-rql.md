---
type: Strategy
title: Steal HyDE hyp-doc pipeline → RQL Rewrite / REWRITE HYDE (Hypothesis packaging)
tags: [hyde, rql, rewrite]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:10:00+01:00
status: provisional
---

# Strategy: HyDE rewrite for RQL

## Steal (Established idea)
- Treat **LLM generation of a hypothetical document** as the relevance-bearing rewrite, not query–doc score learning.
- Embed hyp-doc(s) with the **same** unsupervised dense encoder as the corpus; retrieve by doc–doc similarity (MIPS).
- Optional: average N samples (± raw query embedding) before search (Eqs. 6–8).
- Task-specific **instruction** strings control generation form (Appendix A.1).

## Invent / package (Hypothesis for RQL)
- Surface: `REWRITE HYDE MODEL '…' TEXT $q AS hyp` inside `WITH` / CTE (examples/10-hyde-rewrite-budget.rql).
- Algebra: \(\mathrm{Rewrite}\) / \(\mathrm{Rewrite}_{hyde}: q \rightarrow q^*\) (or emb*) with explicit token/latency cost attributes.
- Feed hyp text into `EMBED` → `Search_dense`; compose with BlinkDB-inspired `OPTION RECALL|LATENCY` (journal 0031).
- EXPLAIN must show model, instruction, N samples, and that quality numbers are not claimed from this paper read.

## Do not steal naively
- Do not paste Tables 1–4 as RQL results.
- Do not require InstructGPT specifically — packaging is model-agnostic; mechanism assumes instruction-following NLG + contrastive encoder.
- Do not confuse with PLAID/MUVERA *physical* late-interaction rewrites (different stack).
