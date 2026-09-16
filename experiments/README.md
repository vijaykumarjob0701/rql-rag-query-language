# Experiments — reproducibility stubs

**Date:** 2026-09-16 (Europe/Dublin)  
**Policy:** No fabricated metrics. This directory holds protocols, configs, and harness stubs. Report only runs you actually execute.

## Layout

```
experiments/
  README.md
  protocols/          # human-readable evaluation protocols
  configs/            # YAML run matrices
  harness/            # tiny runners (plan printer, unit tests)
  results/            # gitkeep; real outputs only when produced
```

## Quick start

```bash
cd experiments
python3 harness/print_planned_runs.py configs/example.yaml
python3 harness/test_rrf_fusion.py
```

## Status

| Component | Status |
|-----------|--------|
| Planned-run printer | works (no scores) |
| Deterministic RRF unit test | works (fixed lists) |
| ANN / RAG end-to-end benches | **not run** |

## Human hand-off

See [`HUMAN_TODOS.md`](HUMAN_TODOS.md) for benches Vijay must run (GPU ANN, datasets, DBs, judgments). Do not invent those results.
