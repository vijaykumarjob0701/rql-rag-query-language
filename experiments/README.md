# Experiments — reproducibility stubs

**Date:** 2026-09-17 (Europe/Dublin)  
**Policy:** No fabricated metrics. This directory holds protocols, configs, and harness stubs. Report only runs you actually execute.

## Layout

```
experiments/
  README.md
  HOW_TO_PROVIDE_RESULTS.md  # human+Colab return paths
  HUMAN_TODOS.md / PAUSE_CHECKLIST.md
  protocols/          # human-readable evaluation protocols
  configs/            # YAML run matrices
  harness/            # tiny runners + optional fanns_synthetic_cpu.py
  colab/              # Colab notebook for FANNS microbench export
  datasets/           # README digests; data/ gitignored
  results/            # real outputs only when produced (incl. fanns/)
```

## Quick start

```bash
cd experiments
python3 harness/print_planned_runs.py configs/example.yaml
python3 harness/test_rrf_fusion.py
python3 harness/test_maxsim_late.py
# schema validation (needs jsonschema; use ../tooling/.venv if needed)
../tooling/.venv/bin/python harness/validate_plans.py
../tooling/.venv/bin/python harness/test_rql_parser.py
../tooling/.venv/bin/python harness/parse_rql.py parse ../schemas/examples/01-hybrid-rrf.rql --validate
../tooling/.venv/bin/python harness/test_rql_planner.py
../tooling/.venv/bin/python harness/plan_rql.py plan results/rql_parser/01-hybrid-rrf.logical.json --profile qdrant --validate
../tooling/.venv/bin/python harness/test_rql_adapters.py
../tooling/.venv/bin/python harness/emit_rql.py emit-batch results/rql_planner/ --stems 01-hybrid-rrf,02-filtered-dense --out-dir results/rql_adapters/
../tooling/.venv/bin/python harness/rql_pipeline.py --inputs ../examples/toy --validate --run-id smoke
```

## Status

| Component | Status |
|-----------|--------|
| Planned-run printer | works (no scores) |
| Deterministic RRF unit test | works (fixed lists) |
| Deterministic MaxSim unit test | works (fixed toy embeddings; ColBERT Eq.3) |
| Plan schema validator | works (jsonschema; schemas/examples → results/plan_schema/validate.txt) |
| Toy RQL → LogicalPlan parser | works (Hypothesis subset; schemas/examples/*.rql → results/rql_parser/) |
| Logical→Physical planner stub | works (Hypothesis rules; 4×3 profiles → results/rql_planner/; schema-valid) |
| Physical→vendor adapter emit stub | works (Hypothesis sketches; hybrid-rrf+filtered-dense×3 → results/rql_adapters/; **not executed**) |
| Offline E2E pipeline CLI | works (Hypothesis; examples/toy × 3 profiles → results/e2e/; **12/12**; **not executed**) |
| Pause / human P0 checklist | `PAUSE_CHECKLIST.md` (what blocks citation-ready) |
| Human+Colab result paths | `HOW_TO_PROVIDE_RESULTS.md` + `colab/` (journal 0028) |
| Synthetic FANNS CPU smoke | optional `harness/fanns_synthetic_cpu.py` — **smoke / not P0** |
| ANN / RAG end-to-end benches (P0) | **not run** (human / Colab with licensed data) |

## Human hand-off

See [`PAUSE_CHECKLIST.md`](PAUSE_CHECKLIST.md), [`HUMAN_TODOS.md`](HUMAN_TODOS.md), and [`HOW_TO_PROVIDE_RESULTS.md`](HOW_TO_PROVIDE_RESULTS.md) (incl. **Colab** Option B). Do not invent P0 results; synthetic smoke ≠ SIFT1M P0.
