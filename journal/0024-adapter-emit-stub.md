# 0024 — PhysicalPlan → vendor adapter emit stub

**Date:** 2026-09-17 ~00:00 IST (Europe/Dublin)  
**Type:** Hypothesis prototype (docs-shaped request sketches)  
**Status:** Emit-only — **not** executed against live DBs; live smoke remains **HUMAN_TODO**  
**Artifacts:** [`../experiments/harness/rql_adapters/`](../experiments/harness/rql_adapters/) · CLI [`../experiments/harness/emit_rql.py`](../experiments/harness/emit_rql.py) · test [`../experiments/harness/test_rql_adapters.py`](../experiments/harness/test_rql_adapters.py) · results [`../experiments/results/rql_adapters/`](../experiments/results/rql_adapters/)  
**Prior seed:** Physical planner stub (journal 0023) → “adapter emit stub (PhysicalPlan → backend JSON/SQL, no live CI)”

---

## Context

Journal 0023 produced 12 schema-valid PhysicalPlans (4 logical × 3 docs-derived profiles). Layer 3 of the compile stack (“emit backend calls through adapters”) still lacked an executable stub. Protocol 03 (adapter smoke) remains a human task against real/local clusters.

## Question asked

Can a **tiny**, honest emitter turn PhysicalPlan JSON into **docs-shaped** vendor request artifacts (strings/JSON/SQL files only) for Qdrant / Elasticsearch / pgvector — without opening sockets or inventing smoke metrics?

## Where we looked

- In-repo: `experiments/results/rql_planner/*.physical.json`, `docs/09-vendor-api-matrix.md` (journal 0020), `knowledge/reads/vendor-api-matrix-2026-09/claims/adapter-surface.md`, thesis §07, planner package patterns.
- No new external paper multimodal pass; no live cluster calls.

## What is Hypothesis vs Established

| Item | Label |
|------|--------|
| Emit packaging / CLI / file layout | **Hypothesis** |
| Qdrant Query API `prefetch`+`fusion=rrf`, Filter JSON shape | **Established** docs surface (journal 0020); emit mapping is Hypothesis |
| ES `retriever.rrf`, `knn.filter` | **Established** docs surface; emit mapping Hypothesis |
| pgvector `<=>` + POST/iterative-scan behaviour | **Established** docs surface; SQL sketch Hypothesis |
| Opaque predicate → Filter DSL toy parse | **Hypothesis** (best-effort) |
| Latency / recall / smoke.json | **Not claimed** (none fabricated; not executed) |

## Emitters implemented

1. **qdrant** — Query API-shaped JSON: `nearest` (+ `filter`); hybrid → `prefetch` + `query.fusion=rrf` (client-shim plans mark `_client_rrf_required`).
2. **elasticsearch** — `retriever.rrf` (standard + knn) or `knn` + `filter` sketch.
3. **pgvector** — SQL sketch `ORDER BY embedding <=> … LIMIT`; `ITERATIVE` plans get iterative-scan comments/`SET` hints; ShimCast dual-branch + client-merge notes.

All artifacts carry `label=Hypothesis`, `approximate=true`, `notExecuted=true`, and a sketch banner.

## What we produced

1. Package `experiments/harness/rql_adapters/` (`emit.py`, CLI `__main__.py`, README).
2. CLI: `emit_rql.py emit | emit-batch | list-vendors`.
3. Test `test_rql_adapters.py`: **hybrid-rrf + filtered-dense × 3 profiles = 6/6** emit + assertions.
4. Results under `experiments/results/rql_adapters/` (`*.emit.json`, `*.request.sql`, `emit_validate.txt`, `emit_summary.txt`).
5. Thesis §07 (+ abstract/conclusion) cite emit stub as Hypothesis layer~3 sketch — **not** live smoke.

## 1–5% seed

Once PhysicalPlans exist, **dozens of lines** of docs-shaped emitters make “Physical → vendor request” real as **auditable sketches** — proving adapters can share the same trees without pretending CI ran against clusters.

## Uncertainty

- Filter DSL translation from opaque `expr` is deliberately toy.
- Late-interaction / linear-fusion emits are shallow stubs.
- Qdrant sparse/BM25 vector placeholders are illustrative.
- Weaviate / Milvus / OpenSearch emitters not yet added.
- **Live behaviour unverified** — HUMAN_TODO protocol 03.

## Next questions

1. Deeper **Substrait / Apache Calcite** read for IR adjacency?  
2. Extend emit to remaining physical stems (late, hybrid-linear) + more vendors from docs/09?  
3. Human live smoke (protocol 03) against local docker — **not** agent CI.

## Anti-overclaim

Emit stub ≠ working production adapter. Docs-shaped JSON/SQL ≠ verified API compatibility. **No** live network to vector DBs this entry. **No** fabricated ANN/RAG metrics. **No push** this entry.
