# Example RQL queries

These files illustrate **RQL (Retrieval Query Language)** patterns from [`../docs/03-proposal.md`](../docs/03-proposal.md). They are **not executable** against a live engine until an RQL compiler/adapters exist; they document intent and compile targets.

| File | RAG pattern |
|------|-------------|
| `01-dense-metadata.rql` | Dense + metadata/ACL |
| `02-hybrid-rrf.rql` | BM25 + dense + RRF + rerank |
| `03-hybrid-linear-weights.rql` | Weighted hybrid + diversification |
| `04-multi-query.rql` | Multi-query / HyDE-style union |
| `05-parent-expand.rql` | Parent document expansion |
| `06-multihop-entity.rql` | Entity hop → chunks |
| `07-graphrag-traverse.rql` | Vector seed + graph traverse |
| `08-acl-phrase-filter.rql` | Phrase/text-match + ACL |
| `09-colbert-late-interaction.rql` | Multi-vector / ColBERT |

Parameters like `$question`, `$tenant` are bound by the host application at compile/execute time.

## Deep dive v2 examples (2026-09-16)

| File | Pattern |
|------|---------|
| `10-hyde-rewrite-budget.rql` | `REWRITE HYDE` + recall/latency budgets |
| `11-vsim-join-entities.rql` | `VSIM JOIN` chunk↔entity threshold join |
| `12-fuse-learned-explain.rql` | Learned linear fusion + late interact + EXPLAIN |

See `docs/07-evolved-idea.md` for the algebra these illustrate.
