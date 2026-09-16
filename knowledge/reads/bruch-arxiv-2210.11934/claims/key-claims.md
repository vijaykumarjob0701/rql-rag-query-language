---
type: ClaimSet
title: Bruch fusion key claims (evidence-linked)
tags: [bruch, claims, fusion]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:25:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Convex combination of channel scores is
   \(f_{\mathrm{Convex}}=\alpha\phi_{\mathrm{Sem}}(f_{\mathrm{Sem}})+(1-\alpha)\phi_{\mathrm{Lex}}(f_{\mathrm{Lex}})\) with monotone normalizers \(\phi\) (min-max, theoretical min-max, z-score, …).  
   Evidence: Eqs. (2)–(5); [../equations/convex-combination.md](../equations/convex-combination.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Preferred practical form **TM2C2** uses theoretical min–max \(\phi_{\mathrm{tmm}}\); authors often use \(\alpha=0.8\) after in-domain validation; suggest \(\alpha\in[0.6,0.8]\).  
   Evidence: §4.2; §7; Table 2 setup

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (mechanism):** RRF rewritten with per-channel \(\eta_{\mathrm{Lex}},\eta_{\mathrm{Sem}}\) is parametric; default \(\eta=60\) is one point in a sensitive landscape.  
   Evidence: Eqs. (7)–(8); Figs 7–8; [../equations/rrf-bruch-parametric.md](../equations/rrf-bruch-parametric.md)

4. **AUTHOR-CLAIM (not reproduced):** On authors’ primary BM25+MiniLM suite, TM2C2 (\(\alpha=0.8\)) beats RRF(\(\eta=60\)) on NDCG in-domain and zero-shot (Table 2; Fig 5); disagrees with Chen et al. [5].  
   Evidence: Table 2; Fig 5; §7 — **do not cite as our measurement**

5. **AUTHOR-CLAIM (not reproduced):** Learning \(\alpha\) for TM2C2 is sample-efficient (Fig 12; often <~5% of training queries).  
   Evidence: Fig 12; §6–§7

6. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (design):** Fusion desiderata include monotonicity, homogeneity, boundedness, Lipschitz/score-distribution preservation, interpretability/sample efficiency.  
   Evidence: §6

## Anti-claims

- That we reproduced Bruch Recall/NDCG tables.
- That CC always dominates RRF on every modern RAG hybrid stack.
- That single-\(\alpha\) CC equals a full learned LTR stack (\(\mathrm{Fuse}_{ltr}\)).
- That Cormack’s RRF formula is wrong — Bruch critiques **default/parametric use in hybrid lexical–dense**, not the existence of RRF.
