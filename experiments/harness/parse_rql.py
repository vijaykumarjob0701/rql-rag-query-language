#!/usr/bin/env python3
"""CLI wrapper: parse toy RQL → LogicalPlan JSON.

Usage (from repo root):
  tooling/.venv/bin/python experiments/harness/parse_rql.py parse path.rql --validate
  # or from harness/:
  python3 -m rql_parser parse path.rql --out out.json --validate
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from rql_parser.__main__ import main

if __name__ == "__main__":
    raise SystemExit(main())
