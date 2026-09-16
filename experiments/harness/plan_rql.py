#!/usr/bin/env python3
"""CLI wrapper: LogicalPlan JSON → PhysicalPlan JSON (Hypothesis planner stub).

Usage (from repo root):
  tooling/.venv/bin/python experiments/harness/plan_rql.py plan \\
      experiments/results/rql_parser/01-hybrid-rrf.logical.json \\
      --profile qdrant --validate
  tooling/.venv/bin/python experiments/harness/plan_rql.py plan-batch \\
      experiments/results/rql_parser/ \\
      --profiles qdrant,elasticsearch,pgvector \\
      --out-dir experiments/results/rql_planner/ --validate
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from rql_planner.__main__ import main

if __name__ == "__main__":
    raise SystemExit(main())
