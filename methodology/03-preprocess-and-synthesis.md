# 03 — Preprocess and Synthesis

**Date:** 2026-09-16 (Europe/Dublin)  
**Purpose:** Normalize what survives Pass 4; compare across sources; keep uncertainty; decide when (if ever) to promote into docs/07.

---

## Normalize notes

Each source gets one notes file (copy from `tooling/scripts/notes_template.md`), stored preferably as:

```
notes/YYYY-MM-DD-<short-slug>.md
```

(or under `journal/` when the note is itself a thinking step — see [`../journal/README.md`](../journal/README.md)).

### Required fields

| Field | Rule |
|-------|------|
| `source` | Title, authors, year/venue, URLs |
| `read_status` | `skimmed` \| `inventory` \| `related` \| `seeded` \| `complete` |
| `modalities_seen` | text / figures / tables / algorithms (checkbox list) |
| `seed` | The 1–5% insight in plain language |
| `evidence` | Pointers into the PDF (fig/table/§) |
| `uncertainty` | Explicit list |
| `next_queries` | 2–5 mutated searches |
| `rql_hypothesis` | Optional, labeled **hypothesis** — not a claim |

### Normalization rules

1. Quote sparingly; prefer paraphrase + location pointers.  
2. Separate **observation** (what the paper shows) from **interpretation** (what it might mean for RQL).  
3. Keep units and metrics as stated (recall@k, QPS, selectivity) — do not silently convert.  
4. If tooling extraction was partial, record `extraction_gaps`.

---

## Compare across papers

Maintain a lightweight comparison sheet (markdown table or CSV) with columns such as:

- problem framing (hybrid ANN? fusion? plan IR?)  
- logical operators named  
- physical strategies named  
- filter predicate class supported  
- evaluation metrics + datasets  
- contradictions vs peers  

Comparison happens **after** ≥2 sources have `read_status: complete` under the protocol — not after abstract dumps.

When two papers disagree:

1. Record both claims with evidence pointers.  
2. Prefer primary figures/tables over secondary blog summaries.  
3. Open contradiction search (funnel stage 5) before picking a side.

---

## Keeping uncertainty

Use tags in notes and journal:

- `[inferred-venue]`  
- `[arxiv-only]`  
- `[secondary-source]`  
- `[extraction-partial]`  
- `[hypothesis]`  

Never delete uncertainty when editing docs/06 or docs/07; resolve it with a re-read or mark `unresolved`.

---

## When to promote into docs/07

Promote an idea into [`../docs/07-evolved-idea.md`](../docs/07-evolved-idea.md) **only if all** hold:

1. At least one primary source read through Pass 5 (multimodal).  
2. Seed is supported by figure/table/algorithm evidence, not abstract alone.  
3. Cross-check: no unrebutted contradiction in the comparison sheet *or* contradiction is explicitly discussed.  
4. The change is framed as steal/specialize from named prior art, not a free invention.  
5. A journal entry records the promotion decision and the evidence.

Until then, keep ideas in notes/journal as `[hypothesis]`.

### What not to promote

- New operator names invented for elegance alone  
- Planner policies without a physical taxonomy cite  
- Claims that all backends can honor identical recall  

---

## Relationship to docs/06

docs/06 remains a **provisional catalog**. Slow-path re-reads may:

- demote entries (abstract-only → needs re-read)  
- enrich entries with figure/table seeds  
- split “takeaway” vs “implication” more carefully  

Prefer journal + notes for incremental truth; batch-edit docs/06 only after several completed protocols.
