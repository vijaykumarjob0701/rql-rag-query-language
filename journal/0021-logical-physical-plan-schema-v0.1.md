# 0021 — LogicalPlan / PhysicalPlan JSON Schema v0.1.0-draft

**Date:** 2026-09-16 ~23:55 IST (Europe/Dublin)  
**Type:** Hypothesis IR freeze (draft schemas + validator)  
**Status:** Schemas frozen as **draft Hypothesis**; **not** a published standard  
**Artifacts:** [`../schemas/`](../schemas/) · harness [`../experiments/harness/validate_plans.py`](../experiments/harness/validate_plans.py) · results [`../experiments/results/plan_schema/validate.txt`](../experiments/results/plan_schema/validate.txt)  
**Prior seed:** Vendor matrix (journal 0020) → “freeze LogicalPlan / PhysicalPlan JSON Schema”

---

## Context

Journal 0020 established (docs-only) what major vector stores expose for filters, hybrid, RRF, late interaction, and EXPLAIN. Thesis §05/§06 already sketched evidence operators and FilterExec modes. The missing artifact was a **machine-checkable IR** so adapters, EXPLAIN, and eval harnesses share one tree shape — without overclaiming a standard.

## Question asked

Can we freeze draft JSON Schema (2020-12) for LogicalPlan and PhysicalPlan that encode docs/08 + thesis §05 operators, §06 FilterExec / late-interact physical nodes, optional capability flags aligned to the vendor matrix, and 3–5 valid examples — validated for real?

## Where we looked

- In-repo: `docs/08-algebra-sketch.md`, `docs/07-evolved-idea.md` (Ext), `docs/09-vendor-api-matrix.md`, thesis §05–§07, journal 0020.
- No new external paper multimodal pass this entry (schema freeze only).

## What we produced

1. **`schemas/logical-plan.schema.json`** — ops: `Search_dense` / `bm25` / `late`, `Filter`, `Union`, `Fuse_{rrf,linear,ltr,condorcet}`, `Diversify`, `Rerank`, `Expand`, `Rewrite`, `Traverse`, `VSimJoin`, `Ext`; optional `capabilities`.
2. **`schemas/physical-plan.schema.json`** — `FilterExec` modes PRE/POST/ITERATIVE/SUBGRAPH/SPECIALIZED/PARTITION/ROUTER/AUTO; `AnnExec`; `FusionExec`; `LateInteractExec` (`colbert`/`plaid`/`muvera`); `ShimCast`; optional recall/latency/ACL budgets.
3. **`schemas/examples/`** — hybrid RRF (logical+physical), filtered dense (logical+physical), late+PLAID rewrite, client RRF shim, MUVERA FDE ladder.
4. **`experiments/harness/validate_plans.py`** — `jsonschema` Draft202012Validator; all 8 example files **passed** (see `validate.txt`).
5. Thesis §05 / §07 cite this freeze as **Hypothesis IR**; PDF rebuild.

## 1–5% seed

**Capability-annotated plan trees** (not just op names) are the portable unit: the same LogicalPlan can compile to native `FusionExec` or explicit `ShimCast` depending on `rrfNative` / FilterExec ads from the vendor matrix — making “fail closed / EXPLAIN” enforceable in schema examples before any live adapter.

## Uncertainty

- Operator arity / Rewrite wiring (`then`) may need revision after a toy parser.
- Substrait/Calcite adjacency not yet encoded (extension functions / custom relations TBD).
- Predicate `expr` remains opaque strings (adapter-local); no portable filter DSL yet.
- Schemas are **Hypothesis** packaging; Established literature/docs facts are *cited by* labels, not certified by JSON Schema.

## Next questions

1. Deeper **Substrait / Apache Calcite** read for IR adjacency (relations, extensions, costing hooks)?  
2. Or first **toy RQL parser** → LogicalPlan JSON conforming to this schema?  
3. Skeleton adapter emitting PhysicalPlan only (pgvector SQL + Qdrant Query JSON) — no live CI calls.

## Anti-overclaim

Draft schemas ≠ industry standard. Validator pass ≠ retrieval quality. No fabricated ANN/RAG metrics. **No push** this entry.
