# 0026 — E2E pipeline CLI (offline glue)

**Date:** 2026-09-17 ~00:11 IST (Europe/Dublin)  
**Type:** Hypothesis prototype (CLI glue)  
**Status:** Offline E2E works — **not** live DB execution; live smoke remains **HUMAN_TODO**  
**Artifacts:** [`../experiments/harness/rql_pipeline.py`](../experiments/harness/rql_pipeline.py) · alias [`../experiments/harness/run_rql.py`](../experiments/harness/run_rql.py) · results [`../experiments/results/e2e/`](../experiments/results/e2e/) · validate log [`../experiments/results/e2e/run_validate.txt`](../experiments/results/e2e/run_validate.txt)  
**Prior seed:** journal 0025 Pass 5 → “E2E CLI glue: rql → parse → plan → emit”

---

## Context

Journals 0021–0024 froze schemas + parser + planner + emit as separate CLIs. Journal 0025 grounded Substrait/Calcite adjacency. Missing piece: one deterministic command that runs the full offline compile stack and writes a run folder.

## Question asked

Can a single script glue toy `.rql` → LogicalPlan → PhysicalPlan(profile) → vendor emit sketches for profiles `qdrant` / `elasticsearch` / `pgvector`, validate schemas, and write auditable artifacts — **without** live DB I/O?

## Where we looked

- In-repo: `rql_parser`, `rql_planner`, `rql_adapters`, `examples/toy/*.rql`, schemas 0.1.0-draft.
- No new paper pass; no live clusters.

## What we produced

1. CLI `experiments/harness/rql_pipeline.py` (+ `run_rql.py` alias).
2. Stages per `(toy, profile)`: parse → validate LogicalPlan → plan → validate PhysicalPlan → emit sketches (`notExecuted`).
3. Run folder `experiments/results/e2e/smoke/` with `manifest.json`, `index.json`, `summary.txt`, and per-stem/profile artifacts.
4. Aggregate log `experiments/results/e2e/run_validate.txt`.
5. Smoke: **4 toys × 3 profiles = 12/12 OK** with schema validation enabled.

## 1–5% seed

The compile stack is now **one offline command** — the prototype is end-to-end as files-on-disk, not four manual CLIs. Citation-ready eval still blocked on human P0 (FANNS microbench, datasets) and P1 live adapter smoke.

## Uncertainty

- Emit sketches for late/linear remain shallow (as in 0024).
- No cost model / Cascades search.
- No live verification of emitted JSON/SQL against real servers.

## Next questions

1. Human P0 pause checklist (journal 0027) — FANNS microbench + datasets.  
2. Protocol 03 live smoke (Vijay).  
3. Optional: more vendors from docs/09 (Weaviate/Milvus) as emit-only.

## Anti-overclaim

E2E ≠ live RAG/ANN bench. Schema-valid plans + sketches ≠ measured recall/latency. **No** live vector-DB network. **No** fabricated metrics. **No push** this entry.
