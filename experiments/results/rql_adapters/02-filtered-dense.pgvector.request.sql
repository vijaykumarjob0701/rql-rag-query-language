-- SKETCH ONLY — Hypothesis / approximate — not executed against a live DB. Docs-shaped emit from PhysicalPlan; live smoke = HUMAN_TODO.
-- vendor=pgvector label=Hypothesis approximate=true notExecuted=true
-- FilterExec mode=ITERATIVE: enable iterative index scans (pgvector ≥0.8.0) so POST-filter recovers recall; see docs/09 + journal 0020.
-- SET hnsw.iterative_scan = strict_order;  -- illustrative, not executed
SELECT id, embedding <=> $q_dense AS dist
FROM chunks
WHERE (tenant_id = 'acme' AND clearance >= 2) /* Hypothesis: opaque predicate pass-through */
ORDER BY embedding <=> $q_dense
LIMIT 20;
-- hnsw.ef_search = 100  -- session GUC hint, not executed
