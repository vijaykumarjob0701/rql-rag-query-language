---
type: ClaimSet
title: Chen ECIR’22 key claims (evidence-linked)
tags: [chen, claims, rrf, interpolation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Key claims

Legend: **AUTHOR-CLAIM** = stated by paper; **ESTABLISHED-FOR-US** = we verified the paper says it (not that we reproduced experiments).

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Zero-shot hybrid fuse of lexical + deep channels via **RRF**  
   \(\mathrm{RRF}(q,d,M)=\sum_m 1/(k+\pi_m(q,d))\) with \(k=60\).  
   Evidence: Eq. (1); §3.1; [../equations/rrf-chen.md](../equations/rrf-chen.md)

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US (mechanism):** Score **linear interpolation** is sensitive to score scales and \(\alpha\); needs normalisation + weight tuning that conflicts with zero-shot transfer.  
   Evidence: §3.1; §6

3. **AUTHOR-CLAIM (not reproduced):** On Robust04 and TREC-COVID, best-tuned min-max linear \(s=\alpha s_{\mathrm{BM25}}+(1-\alpha)s_{\mathrm{NPR}}\) underperforms RRF(BM25, NPR) by ~**3% relative Recall@1K**; larger gap vs full multi-channel RRF.  
   Evidence: Fig 2; §6 — **do not cite as our measurement**

4. **AUTHOR-CLAIM (not reproduced):** Hybrid RRF improves OOD Recall@1K vs deep and vs BM25 (authors’ averages 20.4% / 9.54% relative in abstract); Tables 3–4 detail per-dataset R@1K/MAP.  
   Evidence: Abstract; Tables 3–4 — AUTHOR-only

5. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Deep NPR deteriorates under large domain shift (TREC-COVID); lexical more robust; channels complementary (Fig 1).  
   Evidence: §5.1; Fig 1; Table 4 narrative

## Anti-claims

- That we reproduced Chen Recall/MAP tables or digitised Fig 2 peaks.
- That Chen’s linear baseline equals Bruch TM2C2 (\(\phi_{\mathrm{tmm}}\)).
- That “RRF always beats CC” universally — Bruch reports the opposite winner under NDCG + TM2C2.
- That first-stage Recall@1K equals end-to-end RAG answer quality.
