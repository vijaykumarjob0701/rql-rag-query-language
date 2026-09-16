# 0001 — Initial question

**When:** 2026-09-16 (Europe/Dublin) — project inception  
**Status:** Settled as the motivating question (answers evolve; the question stays)

---

## Context

Starting a research package on whether vector / RAG systems have (or need) a query language analogous to SQL, Redis commands, or MongoDB QL.

## Question asked

1. Do vector databases have a query language like SQL / Redis / MongoDB?  
2. What exists today for vector + metadata retrieval in RAG pipelines?  
3. What gaps remain vs mature query languages?  
4. Is a dedicated **RAG / retrieval query language** feasible — and would it help **accuracy**, **reliability**, and **speed/efficiency**?

## Goals (user intent)

| Dimension | Intent |
|-----------|--------|
| **Accuracy** | Better hybrid fusion, over-fetch+rerank, multi-hop structure — less silent drift in ad-hoc Python |
| **Reliability** | Reproducible plans; fewer “works on vendor A, broken on B” filter bugs; auditable EXPLAIN |
| **Speed / efficiency** | Filter pushdown, fewer round-trips, server-side fusion when available, cost-aware ANN params |

Secondary interest: portable expression of *retrieval plans*, not merely “nearest neighbors + JSON filter.”

## Where we looked

Not yet — this entry records the question before search.

## What we read

N/A (question framing).

## 1–5% seed

The useful framing seed: optimize for **named retrieval stages** (embed → ANN → filter → hybrid fuse → rerank → multi-hop), because those dominate RAG quality and cost — a language that *names* stages enables planners and eval harnesses.

## Uncertainty

- Whether a textual DSL or a portable plan IR matters more  
- How much vendor semantic impedance blocks portability  
- ANN nondeterminism vs reproducibility goals  

## Next questions

- What do production vector DBs actually expose today? (→ landscape pass)  
- Are there dedicated VQL / TopK / SQL-extension efforts already?
