---
type: EquationNote
title: Hybrid query and selectivity (survey §2)
status: provisional
---

# Hybrid query & selectivity `[Established defs]`

**Hybrid query (Def paraphrase):** \(q = (f_s, f_v, v_q, k)\) with scalar predicate \(f_s\), similarity \(f_v\), query vector \(v_q\), result size \(k\).

**Filtered subset:** \(D_{f_s} = \{p \in D \mid f_s(p.s)=1\}\).

**Selectivity (Def 8 paraphrase):** fraction of points satisfying \(f_s\) (paper discusses proportion retained / related formulations — use paper wording in citations; do not invent a second formula).

**Recall@k:** standard overlap with exact filtered \(k\)-NN.

Planner note `[hypothesis]`: expose estimated selectivity (+ distribution factor when available) in EXPLAIN beside chosen FilterExec.
