---
type: ClaimSet
title: MUVERA key claims (evidence-linked)
tags: [muvera, claims, fde]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:57:00+01:00
---

# Key claims

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Chamfer \(\sum_{q\in Q}\max_{p\in P}\langle q,p\rangle\) is the ColBERT-family late-interaction / MaxSim score.  
   Evidence: §1.1; bridges to ColBERT Eq. (3) (journal 0012)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (mechanism):** FDEs \(F_q(Q), F_{doc}(P)\) satisfy \(\langle F_q(Q), F_{doc}(P)\rangle \approx \mathrm{CHAMFER}(Q,P)\); built via space partition (SimHash), fill_empty_clusters, repetitions, projections.  
   Evidence: §2; Fig 2; [../equations/chamfer-and-fde.md](../equations/chamfer-and-fde.md)

3. **AUTHOR-CLAIM (theory stated; proof not re-derived here):** Theorems 2.1–2.2 give ε-approximations / approx Chamfer NNS with FDE dimension bounds.  
   Evidence: §2.1 — treat as author theorems, not our proof audit

4. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (pipeline):** Two-stage retrieval: MIPS over doc FDEs (DiskANN) → Chamfer/MaxSim rerank; contrasts PLAID multi-stage (Fig 1).  
   Evidence: Fig 1; §3.2

5. **AUTHOR-CLAIM (not reproduced):** FDEs match SV-heuristic recall with fewer candidates (Fig 5 / Table 1); BEIR e2e ~10% higher recall / ~90% lower latency vs PLAID on authors’ average.  
   Evidence: §3 — **do not cite as our measurement**

## Anti-claims

- Reproduced BEIR/PLAID numbers.
- That FDE rewrite is mandatory for all `Search_late` plans.
- That we multimodally validated PLAID internals (cite-only).
