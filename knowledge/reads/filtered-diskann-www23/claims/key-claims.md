---
type: ClaimSet
title: Filtered-DiskANN key claims
status: provisional
---

# Key claims

1. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Post-filtering collapses under low label specificity; building one full index per label is often too costly; many systems only change search, not the vector graph. Evidence: §1.2.

2. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** FilteredVamana / StitchedVamana use **geometry and labels** when adding/pruning edges; search uses FilteredGreedySearch (only expand label-matching neighbors). Evidence: Alg.1, Alg.3–5.

3. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Designed for ~\(10^3\) filters and multi-label points with index size near unfiltered graphs. Evidence: §1.3.

4. **AUTHOR-CLAIM (not reproduced):** Order-of-magnitude (or more) efficiency vs baselines; high recall@10 even at very low specificity on evaluated datasets. Evidence: Fig.1–3, abstract — **not our numbers**.

5. **AUTHOR-CLAIM / ESTABLISHED-FOR-US:** Open problems include larger filter vocabularies, complex SQL-like predicates, full dynamic deletes. Evidence: §7.
