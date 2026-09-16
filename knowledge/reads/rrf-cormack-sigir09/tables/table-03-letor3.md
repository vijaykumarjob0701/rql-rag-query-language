---
type: TableNote
title: Table 3 — LETOR 3 fusion vs LTR
tags: [rrf, table3, letor]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T22:55:00+01:00
---

# Table 3 — LETOR 3 (AUTHOR MAP + diffs)

**Corpus:** 583,850 document–query pairs (seven sets combined for analysis).

| method | MAP (AUTHOR CI) | MAP_RRF − MAP | p (AUTHOR) |
|--------|-----------------|---------------|------------|
| RRF | 0.6051 (0.58–0.63) | — | — |
| Condorcet | 0.5917 | 0.0134 | .004 |
| CombMNZ | 0.6107 | −0.0056 | .2 |
| ListNet | 0.5846 | 0.0205 | .001 |
| LGD | 0.5837 | 0.0214 | .003 |
| AdaRank-MAP | 0.5778 | 0.0273 | .000 |
| RankSVM | 0.5737 | 0.0314 | .000 |
| RankBoost | 0.5622 | 0.0429 | .000 |

**Paper claim:** fusing LETOR baselines yields a meta-learner matching/exceeding reported individuals; CombMNZ slightly edges RRF (not significant).

**Anti-overclaim:** not our RAG eval; modern dense+BM25 may differ (see Bruch-style linear fuse as separate hypothesis).
