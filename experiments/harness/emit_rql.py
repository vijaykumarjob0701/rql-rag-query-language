#!/usr/bin/env python3
"""CLI wrapper: PhysicalPlan JSON → vendor request sketches (Hypothesis; not executed).

Usage (from repo root):
  tooling/.venv/bin/python experiments/harness/emit_rql.py list-vendors
  tooling/.venv/bin/python experiments/harness/emit_rql.py emit \\
      experiments/results/rql_planner/01-hybrid-rrf.qdrant.physical.json
  tooling/.venv/bin/python experiments/harness/emit_rql.py emit-batch \\
      experiments/results/rql_planner/ \\
      --stems 01-hybrid-rrf,02-filtered-dense \\
      --out-dir experiments/results/rql_adapters/
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from rql_adapters.__main__ import main

if __name__ == "__main__":
    raise SystemExit(main())
