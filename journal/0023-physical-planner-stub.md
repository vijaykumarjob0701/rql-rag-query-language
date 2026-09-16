# 0023 — LogicalPlan → PhysicalPlan planner stub

**Date:** 2026-09-16 ~23:59 IST (Europe/Dublin)  
**Type:** Hypothesis prototype (deterministic physical rules)  
**Status:** Capability-profile rule engine only — **not** Cascades costing; **no** fabricated latency/recall  
**Artifacts:** [`../experiments/harness/rql_planner/`](../experiments/harness/rql_planner/) · CLI [`../experiments/harness/plan_rql.py`](../experiments/harness/plan_rql.py) · test [`../experiments/harness/test_rql_planner.py`](../experiments/harness/test_rql_planner.py) · results [`../experiments/results/rql_planner/`](../experiments/results/rql_planner/) · profiles `rql_planner/profiles/{qdrant,elasticsearch,pgvector}.json`  
**Prior seed:** Toy parser (journal 0022) → “physical planner stub (Logical→Physical + FilterExec/ShimCast)”

---

## Context

Journal 0021 froze LogicalPlan / PhysicalPlan JSON Schema (`0.1.0-draft`). Journal 0022 produced four schema-valid LogicalPlans from toy RQL text. Layer 2 of the compile stack (“optimise LogicalPlan → PhysicalPlan with capability negotiation”) still lacked an executable stub.

## Question asked

Can a **tiny**, honest, deterministic rule engine turn those LogicalPlans into PhysicalPlans that validate against `schemas/physical-plan.schema.json`, using **docs-derived** vendor capability profiles (not live probes)?

## Where we looked

- In-repo: `schemas/physical-plan.schema.json`, `schemas/examples/*.physical.json`, `experiments/harness/test_filter_strategy_chooser.py`, `docs/09-vendor-api-matrix.md` (journal 0020), thesis §06 / §07, parser results under `experiments/results/rql_parser/`.
- No new external paper multimodal pass.

## What is Hypothesis vs Established

| Item | Label |
|------|--------|
| Planner packaging / rule wiring / profile JSON files | **Hypothesis** |
| FilterExec mode names + FANNS pruningStrategy map | **Hypothesis** packaging of **Established** survey vocabulary (journal 0019) |
| Vendor capability flags (`rrfNative`, `annIterator`, …) | **Established** as docs-only survey cells (journal 0020); profiles are Hypothesis encodings of those cells |
| RRF / MaxSim / iterative-scan *mechanisms* | **Established** in literature/docs; planner does not re-measure them |
| Latency / recall numbers | **Not claimed** (none fabricated) |

## Rules implemented

1. **Filter → FilterExec** — toy Stats inferred from opaque predicate (`aclHard`, label/range/complex heuristics) + profile `filterCaps`; chooser thresholds aligned with `test_filter_strategy_chooser.py` (ACL+iterator→`ITERATIVE`; ACL else→`PRE`; …). Optional FANNS `pruningStrategy` labels (SSP/VSP/VJP).
2. **Fuse_rrf → FusionExec** — `native=true` if `rrfNative`; else wrap `ShimCast client_rrf` around `native=false`.
3. **Fuse_linear → FusionExec** — native if `weightedFusionNative`; else `ShimCast client_linear`.
4. **Search_late → LateInteractExec** — `colbert` when `multiVectorLate` (or as fail-closed default); optional `--late-rewrite plaid|muvera` when profile advertises `latePlaid` / `fdeMips`.
5. **Search_dense / Search_bm25** → `AnnExec` / `Bm25Exec`.

Profiles: **qdrant**, **elasticsearch**, **pgvector** (minimum set).

## What we produced

1. Package `experiments/harness/rql_planner/` (`planner.py`, `filter_mode.py`, `profiles/`, CLI `__main__.py`).
2. CLI: `plan_rql.py plan … --profile … [--validate]` / `plan-batch` / `list-profiles`.
3. Test `test_rql_planner.py`: **4 logical × 3 profiles = 12/12 plan + validate**; rule assertions (native RRF vs shim; ACL modes; late variant).
4. Results under `experiments/results/rql_planner/` (`*.physical.json` + `plan_validate.txt`).
5. Thesis §06 / §07 (+ abstract/conclusion) cite the stub as Hypothesis.

## 1–5% seed

Once PhysicalPlan is schema-frozen and LogicalPlans exist, a **dozens-of-lines** capability-table + rewrite rules make “Logical → Physical” real for Filter/Fuse/Late — proving EXPLAIN/adapters can share trees without pretending cost-based optimisation is done.

## Uncertainty

- Selectivity inference from opaque `expr` strings is deliberately toy.
- Profiles omit Weaviate/Milvus/OpenSearch (easy to add later).
- `Union` / LTR / Condorcet barely stubbed; no budgets invent latency/recall.
- Adapter emission (backend JSON/SQL) still absent.

## Next questions

1. Deeper **Substrait / Apache Calcite** read for IR adjacency?  
2. Or **adapter emit stub** (PhysicalPlan → Qdrant Query JSON / ES retriever / pgvector SQL) without live CI calls?  
3. Extend profiles to Weaviate / Milvus / OpenSearch from docs/09.

## Anti-overclaim

Planner stub ≠ production optimizer. Schema validation ≠ retrieval quality. Capability profiles ≠ live probes. **No** fabricated ANN/RAG metrics. **No push** this entry.
