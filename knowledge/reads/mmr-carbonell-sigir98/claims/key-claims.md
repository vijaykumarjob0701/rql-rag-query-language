---
type: Claims
title: MMR key claims (honesty-tagged)
tags: [mmr, claims]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:20:00+01:00
status: provisional
---

# Key claims

| Claim | Tag | Evidence |
|-------|-----|----------|
| MMR = Arg max of λ·Sim₁(Di,Q) − (1−λ)·max Sim₂(Di,Dj∈S) over Di∈R∖S | **Established** (formula) | §2 |
| λ=1 → standard relevance ranking; λ=0 → maximal diversity among R | **Established** (semantics) | §2 |
| Sim₁ and Sim₂ may be the same or different metrics | **Established** | §2 |
| Useful search strategy: small λ then larger λ after reformulation | **AUTHOR narrative / Provisional** | §2 (e.g. 0.3 then 0.7) |
| Pilot users prefer broader MMR ranking (80% chose MMR) | **AUTHOR-only / Provisional** | §3 n=5 — **not reproduced** |
| Passage MMR with cosine for single/multi-doc summarization | **Established** (use of formula) | §4 |
| SUMMAC highest-utility F=.73; Table 1 precision @ λ | **AUTHOR-only / Provisional** | §4 Table 1 — **not reproduced** |
| Clearest advantage = multi-document anti-redundancy | **AUTHOR narrative** | Abstract; §5 |
| RQL `DIVERSIFY MMR` / \(\mathrm{Diversify}_{mmr}\) syntax / defaults | **Hypothesis** | thesis §05; docs/08 |
| MMR ≡ channel fusion (RRF/linear) | **False / do not claim** | MMR reorders one set; fusion merges rankings |
