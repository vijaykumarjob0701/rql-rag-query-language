# Protocol 03 — Adapter smoke (HUMAN)

For each backend (pgvector docker, Qdrant docker, optional Pinecone):
1. Upsert ≤1k toy vectors + metadata ACL field.
2. Run equivalent RQL-or-SQL: dense top-k with ACL predicate.
3. Assert zero ACL violations on negative tests.
4. Write sanitized `smoke.json` (no secrets).
