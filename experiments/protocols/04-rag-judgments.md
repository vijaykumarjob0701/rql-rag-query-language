# Protocol 04 — Judgments (HUMAN)

1. Fix a query set (≤100) and retrieved pools from competing plans.
2. Label relevance (human or declared LLM judge with prompt hash).
3. Compute nDCG@k only from those labels.
4. Store `labels.jsonl` + `meta.json` (annotator id / model id).
