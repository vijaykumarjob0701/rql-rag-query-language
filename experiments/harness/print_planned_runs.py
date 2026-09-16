#!/usr/bin/env python3
"""Print planned experiment tuples from example.yaml without inventing scores."""
from __future__ import annotations

import itertools
import re
import sys
from pathlib import Path

def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [x.strip().strip("'\"") for x in inner.split(",")]
    return [value.strip().strip("'\"")] if value else []

def load_config(path: Path) -> dict:
    """Parse our simple key: [a, b] config without requiring PyYAML."""
    data: dict[str, list[str]] = {
        "channels": [],
        "fuse": [],
        "filter_mode": [],
        "rerank": [],
        "baselines": [],
        "metrics": [],
    }
    for raw in path.read_text().splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip() or line.startswith(" ") or line.startswith("\t"):
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        if key in data:
            data[key] = parse_inline_list(val)
    return data

def main() -> int:
    cfg_path = Path(sys.argv[1] if len(sys.argv) > 1 else "configs/example.yaml")
    if not cfg_path.is_file():
        alt = Path("experiments") / cfg_path
        cfg_path = alt if alt.is_file() else cfg_path
    data = load_config(cfg_path)
    print(f"# Planned runs from {cfg_path} (NO SCORES)")
    print(f"# metrics: {', '.join(data['metrics'])}")
    n = 0
    for baseline, ch, fuse, fm, rr in itertools.product(
        data["baselines"] or ["sdk_glue"],
        data["channels"] or ["hybrid"],
        data["fuse"] or ["rrf"],
        data["filter_mode"] or ["AUTO"],
        data["rerank"] or ["off"],
    ):
        n += 1
        print(
            f"{n:03d} baseline={baseline} channels={ch} fuse={fuse} "
            f"filter_mode={fm} rerank={rr} score=NOT_RUN"
        )
    print(f"# total planned tuples: {n}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
