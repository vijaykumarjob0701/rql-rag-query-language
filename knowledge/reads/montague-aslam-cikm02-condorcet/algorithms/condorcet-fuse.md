---
type: Algorithm
title: Condorcet-fuse (Alg 1 + Alg 3)
tags: [condorcet, algorithm]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-16T23:30:00+01:00
---

# Algorithms 1 & 3 — Condorcet-fuse

## Algorithm 1 — Simple Majority Runoff
Compare two documents across \(k\) systems: increment/decrement a counter by which system ranks which higher; majority wins.

## Algorithm 2 — Theoretic Condorcet Metasearch (reference only)
Build full Condorcet graph over all pairs (\(O(n^2k)\)), then Hamiltonian path — impractical for large \(n\).

## Algorithm 3 — Condorcet-fuse
1. Create list \(L\) of all documents in the fusion pool  
2. \(\mathrm{Sort}(L)\) using Algorithm 1 as the comparison function  
3. Output the sorted list  

**Complexity (Theorem 4):** \(O(nk\log n)\) time, \(O(nk)\) space (ranks-per-doc representation).

**SCC note:** Within cyclic strongly connected components, QuickSort pivot choice affects local order; authors relate this to approximating Copeland-style degree rankings (§3.2.6).
