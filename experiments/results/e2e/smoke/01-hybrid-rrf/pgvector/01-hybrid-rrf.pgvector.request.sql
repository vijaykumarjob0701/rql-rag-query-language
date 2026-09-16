-- SKETCH ONLY — Hypothesis / approximate — not executed against a live DB. Docs-shaped emit from PhysicalPlan; live smoke = HUMAN_TODO.
-- vendor=pgvector label=Hypothesis approximate=true notExecuted=true
-- FusionExec: pgvector has no native RRF/weighted fuse — family=rrf native=False.
-- ShimCast shim=client_rrf expensive=True aclUnsafe=False — client merges ranked lists.
-- --- branch 0: AnnExec ---
SELECT id, embedding <=> $q_dense AS dist
FROM chunks
WHERE TRUE /* no predicate */
ORDER BY embedding <=> $q_dense
LIMIT 50;
-- hnsw.ef_search = 100  -- session GUC hint, not executed
-- --- branch 1: Bm25Exec ---
SELECT id, ts_rank(tsv, plainto_tsquery('english', 'portable retrieval IR for RAG')) AS rank
FROM chunks
WHERE TRUE /* no predicate */
  AND tsv @@ plainto_tsquery('english', 'portable retrieval IR for RAG')
ORDER BY rank DESC
LIMIT 50;
-- BM25/FTS via Postgres tsvector — not native BM25 engine
