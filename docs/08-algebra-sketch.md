# 08 — RQL algebra sketch (markdown mirror)

**Date:** 2026-09-16 (Europe/Dublin)  
**Status:** `[hypothesis]` mirror of `thesis/sections/05-rql-algebra.tex` + filter modes from `06-optimizer.tex`  
**Honesty:** Not settled algebra. Grounding cites multimodal journals 0006 / 0009 / 0010 / **0011** (RRF) / **0012** (ColBERT MaxSim) / **0013** (MUVERA FDE). No fabricated metrics.

---

## Typed evidence relation

\[
E \subseteq Id \times Payload \times Score \times Channel \times Provenance \times Attr^*
\]

- Scores are **channel-local** until `Fuse`.
- Mandatory ACL attributes in `Attr` must remain enforceable in every physical plan `[hypothesis]`.

## Logical operators (kernel)

| Operator | Signature | Notes |
|----------|-----------|-------|
| `Search_dense(q,k)` | → E | ANN leaf |
| `Search_bm25(q,k)` | → E | Lexical leaf |
| `Search_late(q,k)` | → E | Late interaction / MaxSim-sum **[Established]** (ColBERT Eq. 3; journal 0012); RQL naming/compile **[Hypothesis]** |
| `Filter(P)` | E → E | Predicates / ACL |
| `Union` | E×E → E | Multi-query |
| `Fuse_rrf(k)` / `Fuse_linear` | E* → E | RRF formula + k=60 **[Established]** (Cormack SIGIR’09; journal 0011); RQL naming/compile **[Hypothesis]** |
| `Diversify_mmr` | E → E | |
| `Rerank_m` | E → E | |
| `Expand` | E → E | Parent/window |
| `Rewrite` | q → q* | HyDE / multi-query |
| `Traverse_h` | E → E | Bounded graph hop |
| `VSimJoin_θ` | E×E → E | Similarity join |

## Physical `FilterExec` modes

\[
FilterExec ∈ \{PRE, POST, ITERATIVE, SUBGRAPH, SPECIALIZED, AUTO\}
\]

| Mode | Literature seed | When (sketch) |
|------|-----------------|---------------|
| PRE | classical | Small survivor set |
| POST | ACORN critique | High selectivity / correlation; over-fetch |
| SUBGRAPH | ACORN | Predicate-agnostic denser graph capability |
| SPECIALIZED | Filtered-DiskANN | Label/equality graph capability |
| ITERATIVE | VBASE Open/Next + RM | Filter-during-traversal / join-friendly iterator |
| AUTO | planner | Stats + **never** drop ACL hard constraints |

## Rewrite examples `[hypothesis]`

1. Adverse selectivity/correlation → prefer SUBGRAPH / ITERATIVE / SPECIALIZED / over-fetch POST (by capability).
2. `VSimJoin` → iterator nested loops when `ann_iterator` available (VBASE-class).
3. Label predicates + FilteredVamana-class index → SPECIALIZED; else do not pretend.
4. **Hybrid fuse (RRF):** channel-local rankings → `Fuse_rrf(k=60)` when scores incomparable; linear/learned when calibrated `[hypothesis]`.
5. **Late-interact ladder:** `Search_late` → native MaxSim multi-vector (ColBERT) → PLAID-class centroid prune (cite-only) → MUVERA `FDE_ANN + MAXSIM_RERANK` (journal 0013); else fail closed / EXPLAIN — **never** silent dense cosine substitution.

## What this does **not** claim

- Reproduced ANN speedups from ACORN / VBASE / Filtered-DiskANN.
- Reproduced ColBERT MRR/latency or MUVERA BEIR/PLAID numbers.
- That every vendor implements multi-vector or FDE modes.
- That OKF packaging is part of the RQL runtime.
