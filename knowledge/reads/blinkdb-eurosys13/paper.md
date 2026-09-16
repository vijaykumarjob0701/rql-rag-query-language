---
type: Paper
title: "BlinkDB: Queries with Bounded Errors and Bounded Response Times on Very Large Data"
resource: https://doi.org/10.1145/2465351.2465355
tags: [blinkdb, aqp, eurosys13]
generated:
  by: grok-bot/executor
  at: 2026-09-17T00:55:00+01:00
status: provisional
---

# BlinkDB — Agarwal et al. (EuroSys 2013) `[venue-verified]`

**Authors (ACM/dblp):** Sameer Agarwal, Barzan Mozafari, Aurojit Panda, Henry Milner, Samuel Madden, Ion Stoica  
**Venue:** EuroSys ’13, Prague; ACM; pages 29–42; DOI 10.1145/2465351.2465355  
**Preprint read:** arXiv:1203.5485v2 (16 pp; author list on this PDF omits Milner)  
**Local:** `tooling/scripts/extract_out/blinkdb-1203.5485.pdf`

## Abstract (paraphrase)

BlinkDB is a parallel approximate SQL engine that runs aggregation queries on precomputed multi-dimensional, multi-resolution samples and lets users declare either error+confidence or response-time constraints. A runtime Error-Latency Profile selects sample size; answers include statistical error bars. AUTHOR experiments claim interactive latency on multi-TB Conviva/TPC-H workloads (unreproduced here).

## Links
- Journal 0031; [claims](claims/key-claims.md); [AQP→RQL strategy](strategies/aqp-budgets-for-rql.md); [ELP note](equations/error-latency-profile.md).
