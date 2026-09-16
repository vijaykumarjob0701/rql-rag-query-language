---
type: Figure
title: Fig 2 — RRF vs linear interpolation vs oracle
tags: [chen, fig2, rrf, interpolation]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:35:00+01:00
---

# Fig 2 — Hybrid vs interpolation (Robust04, TREC-COVID)

**Page:** 11 (arXiv PDF)  
**Caption:** “The comparisons of our hybrid model, oracle system and interpolation.”

**What it shows (AUTHOR):**
- X-axis: interpolation weight \(\alpha\)
- Y-axis: Recall@1K
- Bottom curve: min-max linear BM25+NPR (weight-sensitive)
- Solid line: RRF(BM25, NPR)
- Dashed: full RRF (Bo1 + docT5query + NPR)
- Dotted: oracle merge of relevant results (headroom)

**Author claim:** even best \(\alpha\) underperforms RRF(BM25, NPR) by ~3% relative on both datasets.

**Honesty:** curve values not digitised here; rely on §6 prose + visual skim of page PNG.
