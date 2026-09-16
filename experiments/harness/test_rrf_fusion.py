#!/usr/bin/env python3
"""Deterministic Reciprocal Rank Fusion on fixed lists (Cormack et al. 2009 idea).

Reports only the computed ranking for this toy input — not an IR benchmark.
"""
from __future__ import annotations

from collections import defaultdict

def rrf(*rankings: list[str], k: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, doc in enumerate(ranking, start=1):
            scores[doc] += 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda x: (-x[1], x[0]))

def main() -> int:
    dense = ["D1", "D2", "D3", "D4"]
    bm25 = ["D3", "D1", "D5", "D2"]
    fused = rrf(dense, bm25, k=60)
    print("RRF unit test (k=60)")
    print("dense:", dense)
    print("bm25:", bm25)
    print("fused:")
    for doc, score in fused:
        print(f"  {doc}\t{score:.6f}")
    # Deterministic assertions
    assert fused[0][0] == "D1"
    assert fused[1][0] == "D3"
    print("OK: top-2 are D1, D3 as expected for this toy input")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
