#!/usr/bin/env python3
"""Alias entrypoint for rql_pipeline.py (E2E offline glue)."""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from rql_pipeline import main

if __name__ == "__main__":
    raise SystemExit(main())
