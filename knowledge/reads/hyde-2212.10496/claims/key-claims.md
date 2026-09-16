---
type: Claims
title: HyDE key claims (honesty-tagged)
tags: [hyde, claims]
generated:
  by: grok-bot/executor
  at: 2026-09-17T01:10:00+01:00
status: provisional
---

# Key claims

| Claim | Tag | Evidence |
|-------|-----|----------|
| Zero-shot dense retrieval without relevance labels via hyp-doc pivot | **Established** (mechanism) | Abstract; §3.2; Fig 1 |
| InstructLM generates hypothetical document from query+INST; Contriever embeds; MIPS retrieves real docs | **Established** (mechanism) | Fig 1; Eqs. (4)–(7) |
| Dense encoder acts as lossy compressor / grounds hyp-doc to corpus | **Established** (mechanism narrative) | §3.2; abstract |
| Query vector ≈ mean of N generated-doc embeddings (± optional query emb) | **Established** (Eqs. 6–8) | §3.2 |
| No HyDE-specific training; shares Contriever embedding space | **Established** (setup) | §4.1; intro footnote |
| Outperforms Contriever; competitive with fine-tuned on DL/BEIR/Mr.TyDi | **AUTHOR-only / Provisional** | Tables 1–4 — **not reproduced** |
| RQL `REWRITE HYDE` syntax / planner costs | **Hypothesis** | thesis §05; examples/10 |
| HyDE ≡ generative doc-id retrieval (DSI-style) | **False / do not claim** | §2 delineation |
