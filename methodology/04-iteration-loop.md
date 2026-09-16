# 04 — Iteration Loop

**Date:** 2026-09-16 (Europe/Dublin)  
**Purpose:** The repetitive cycle until something concrete emerges — and clear stop criteria.

---

## Loop diagram

```
                    ┌─────────────────────────┐
                    │  Search strategy / mutate│
                    │  (01)                    │
                    └───────────┬─────────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │  Select 1 source (max 3) │
                    └───────────┬─────────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │  Read protocol Pass 1–5  │
                    │  (02) + tooling extract  │
                    └───────────┬─────────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │  Normalize note + journal│
                    │  entry (03)              │
                    └───────────┬─────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
        New seed?         Contradiction?     Dead end?
              │                 │                 │
              ▼                 ▼                 ▼
        Mutate queries    Funnel stage 5     Park + pick
        (stay in loop)    then re-enter      different angle
              │                 │                 │
              └────────────┬────┴─────────────────┘
                           │
                           ▼
                Enough convergent seeds?
                     │           │
                    yes          no
                     │           │
                     ▼           └──► continue loop
            Promote carefully
            to docs/07 (03 rules)
                     │
                     ▼
                   STOP / pause
```

---

## Cadence recommendations

| Mode | Batch size | Goal |
|------|------------|------|
| Opening | 1 source | Prove the protocol + tooling |
| Steady | 2–3 sources | Compare seeds |
| Synthesis pause | 0 new PDFs | Update comparison sheet; maybe docs/07 |

Avoid “read ten abstracts” days. Prefer one complete protocol.

---

## Stop criteria (pause the literature loop)

Stop or pause when **any** of these hold:

1. **Convergent seeds:** ≥3 independent sources support the same operator/planner vocabulary you would steal.  
2. **Actionable gap:** You can state a concrete experiment or grammar question that literature will not answer (needs prototype).  
3. **Diminishing mutations:** New papers only repeat the same seed without new figures/taxonomies.  
4. **Time-box:** A planned slow-path window ends; journal the state honestly.  
5. **Blocker:** Tooling/extraction systematically fails on the corpus — fix tooling before more reading.

Stop criteria for **promoting to docs/07** are stricter (see [`03-preprocess-and-synthesis.md`](03-preprocess-and-synthesis.md)).

---

## Exit artifacts

When pausing, leave:

1. Journal entries up to date (chronological thinking)  
2. Notes with seeds + next queries for unfinished threads  
3. Comparison sheet snapshot  
4. Explicit list: `promoted` / `hypothesis` / `parked`

Do not exit by dumping more unread citations into docs/06.
