# 08 — RQL algebra sketch (markdown mirror)

**Date:** 2026-09-16 (Europe/Dublin)  
**Status:** `[hypothesis]` mirror of `thesis/sections/05-rql-algebra.tex` + filter modes from `06-optimizer.tex`  
**Honesty:** Not settled algebra. Grounding cites multimodal journals 0006 / 0009 / 0010 / **0011** (RRF) / **0012** (ColBERT MaxSim) / **0013** (MUVERA FDE) / **0014** (PLAID centroid interaction) / **0016** (Bruch CC/TM2C2). No fabricated metrics.

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
| `Fuse_rrf(k)` | E* → E | RRF formula + k=60 **[Established]** (Cormack SIGIR’09; journal 0011); RQL naming/compile **[Hypothesis]** |
| `Fuse_condorcet` | E* → E | Pairwise-majority sort **[Established]** (Montague–Aslam CIKM’02; journal 0018); RQL naming/compile **[Hypothesis]** |
| `Fuse_linear(α)` / `Fuse_ltr` | E* → E | CC/TM2C2 normalised convex combo **[Established]** mechanism (Bruch TOIS/arXiv:2210.11934; journal 0016); LTR + RQL packaging/policy **[Hypothesis]**; AUTHOR NDCG **[Provisional]** |
| `Diversify_mmr` | E → E | |
| `Rerank_m` | E → E | |
| `Expand` | E → E | Parent/window |
| `Rewrite` | q → q* | HyDE / multi-query |
| `Traverse_h` | E → E | Bounded graph hop |
| `VSimJoin_θ` | E×E → E | Similarity join |

## Physical `FilterExec` modes

\[
FilterExec ∈ \{PRE, POST, ITERATIVE, SUBGRAPH, SPECIALIZED, PARTITION, ROUTER, AUTO\}
\]

| Mode | Literature seed | When (sketch) |
|------|-----------------|---------------|
| PRE | FANNS SSP / A12 (Lin 2025 survey) | Small survivor set / high selectivity |
| POST | FANNS VSP / A1 | Low selectivity / cheap over-fetch |
| SUBGRAPH | FANNS VJP / ACORN A4 | Predicate-subgraph capability |
| SPECIALIZED | FANNS VJP / Filtered-DiskANN A9 | Label/equality (or range) graph capability |
| ITERATIVE | FANNS A2 VBase + VBASE Open/Next | Filter-during-traversal / join-friendly iterator |
| PARTITION | FANNS SJP / Milvus-Partition·HQI A13–A14 | Workload-stable partitions / multi-subset indices |
| ROUTER | FANNS §6.3 multi-algorithm combo | Per-query choose among advertised FANNS impls |
| AUTO | planner | Stats (selectivity × distribution) + **never** drop ACL hard constraints |

## Rewrite examples `[hypothesis]`

1. Adverse selectivity/correlation → prefer SUBGRAPH / ITERATIVE / SPECIALIZED / PARTITION / ROUTER / over-fetch POST (by capability; Lin 2025 taxonomy).
2. `VSimJoin` → iterator nested loops when `ann_iterator` available (VBASE-class).
3. Label predicates + FilteredVamana-class index → SPECIALIZED; else do not pretend.
4. **Hybrid fuse:** channel-local rankings → `Fuse_rrf(k=60)` when scores incomparable **[Established]**; optional `Fuse_condorcet` majoritarian sibling **[Established]** mechanism (journal 0018) / **[Hypothesis]** when-to-use; `Fuse_linear(α)` (Bruch CC/TM2C2) when calibrated scores exist **[Established]** mechanism / **[Hypothesis]** policy; `Fuse_ltr` when multi-feature LTR justified `[hypothesis]`.
5. **Late-interact ladder:** `Search_late` → native MaxSim multi-vector (ColBERT, 0012) → PLAID centroid interaction + multi-stage prune → residual MaxSim (journal **0014**, mechanism **[Established]**; AUTHOR speedups only) → MUVERA `FDE_ANN + MAXSIM_RERANK` (journal 0013); else fail closed / EXPLAIN — **never** silent dense cosine substitution.

## What this does **not** claim

- Reproduced ANN speedups from ACORN / VBASE / Filtered-DiskANN / FANNS survey Fig 3.
- Reproduced ColBERT MRR/latency, PLAID GPU/CPU speedups (Tables 3–6 / Fig 6), or MUVERA BEIR/PLAID numbers.
- That every vendor implements multi-vector or FDE modes.
- That OKF packaging is part of the RQL runtime.
