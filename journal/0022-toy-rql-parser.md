# 0022 — Toy RQL text → LogicalPlan parser

**Date:** 2026-09-16 ~23:59 IST (Europe/Dublin)  
**Type:** Hypothesis prototype (textual frontend)  
**Status:** Minimal subset only — **not** a full SQL engine  
**Artifacts:** [`../experiments/harness/rql_parser/`](../experiments/harness/rql_parser/) · CLI [`../experiments/harness/parse_rql.py`](../experiments/harness/parse_rql.py) · test [`../experiments/harness/test_rql_parser.py`](../experiments/harness/test_rql_parser.py) · results [`../experiments/results/rql_parser/`](../experiments/results/rql_parser/) · schema-aligned `.rql` under [`../schemas/examples/`](../schemas/examples/)  
**Prior seed:** Schema freeze (journal 0021) → “toy RQL parser → LogicalPlan JSON”

---

## Context

Journal 0021 froze draft LogicalPlan / PhysicalPlan JSON Schema (`0.1.0-draft`) with validated hand-written examples. Layer 1 of the compile stack (“parse textual RQL → LogicalPlan”) still lacked an executable frontend. Full aspirational `examples/*.rql` (EMBED, WITH, RERANK, …) remain out of scope.

## Question asked

Can a **tiny** honest grammar map schema-aligned RQL text to LogicalPlan JSON that passes `jsonschema` against `schemas/logical-plan.schema.json`?

## Where we looked

- In-repo: `schemas/logical-plan.schema.json`, `schemas/examples/*.logical.json`, `docs/03-proposal.md` grammar sketch, `examples/*.rql` (aspirational), journal 0021.
- No new external paper multimodal pass.

## What grammar is Hypothesis vs implemented

| Item | Label |
|------|--------|
| Full docs/03 / examples/*.rql surface (EMBED, CTE, RERANK, …) | **Hypothesis** sketch — **not** implemented |
| Toy EBNF in `rql_parser/grammar.md` | **Hypothesis** packaging of a subset |
| Mapping SEARCH/FILTER/FUSE → LogicalPlan ops | **Hypothesis** IR packaging (schema 0021) |
| RRF / MaxSim / linear-fusion *mechanisms* named by ops | **Established** in literature (cited elsewhere); parser does not re-prove them |

### Implemented (toy)

`RETRIEVE` · `SEARCH` {`DENSE`,`BM25`,`LATE`,`COLBERT`} · `ON` · `METRIC` · `K`/`CANDIDATES` · `QUERY` · `VECTOR_REF` · `WHERE` (opaque predicate) · `ACL_HARD` · `FUSE RRF [K n]` · `FUSE LINEAR WEIGHTS (…)` · optional `LIMIT` (meta-only when `k` already set) · `--` comments.

### Explicitly rejected

`EMBED`, `WITH`, `RERANK`, `DIVERSIFY`, `EXPAND`, `REWRITE`, `TRAVERSE`, `VSIM`, `FILTER_MODE`, `OPTION`, `UNION`, `EXPLAIN`, LTR/Condorcet/DBSF fuse, nested subqueries.

## What we produced

1. Package `experiments/harness/rql_parser/` (`parser.py`, `grammar.md`, `__main__.py`).
2. CLI: `python experiments/harness/parse_rql.py parse path.rql [--out …] [--validate]` or `python -m rql_parser parse …` from `experiments/harness/`.
3. Schema-aligned `.rql`: `01-hybrid-rrf`, `02-filtered-dense`, `03-late`, `04-hybrid-linear` (+ mirrors under `examples/toy/`).
4. Test `test_rql_parser.py`: **4/4 parse + validate**; negative EMBED rejection; outputs under `experiments/results/rql_parser/`.
5. Thesis §05 / §07 (+ abstract/conclusion) cite the prototype as Hypothesis.

## 1–5% seed

Once LogicalPlan is schema-frozen, a **dozens-of-lines** recursive-descent frontend is enough to make “text → IR” real for SEARCH/FILTER/FUSE — proving the IR is frontend-agnostic without pretending the aspirational RAG DSL is done.

## Uncertainty

- Predicate `expr` remains opaque (no portable filter AST).
- `LIMIT` has no LogicalPlan op — outer limit is meta-only when candidate `k` is set.
- `ON field` is accepted but not yet a first-class schema field (collection comes from `RETRIEVE`).
- Full `examples/*.rql` still fail by design.

## Next questions

1. Deeper **Substrait / Apache Calcite** read for IR adjacency?  
2. Or **physical planner stub** (LogicalPlan → PhysicalPlan with FilterExec mode / ShimCast from capability flags)?  
3. Skeleton adapters emitting backend JSON/SQL only (no live CI calls).

## Anti-overclaim

Toy parser ≠ production RQL. Schema validation ≠ retrieval quality. **No** fabricated ANN/RAG metrics. **No push** this entry.
