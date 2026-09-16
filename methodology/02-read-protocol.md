# 02 — Read Protocol (One Source)

**Date:** 2026-09-16 (Europe/Dublin)  
**Applies to:** one PDF / HTML primary source at a time.  
**Tools:** [`../tooling/`](../tooling/) extractors assist inventory; human/agent judgment owns relation and seed extraction.

---

## Pass overview

| Pass | Name | Goal | Timebox (guideline) |
|------|------|------|---------------------|
| 1 | Skim | Title, abstract, section map, conclusion — *no claims yet* | 5–15 min |
| 2 | Multimodal inventory | List every section, figure, table, algorithm, notable equation | 15–40 min |
| 3 | Relate components | Link figure↔caption↔body; table↔claim; algo↔named strategy | 20–45 min |
| 4 | Extract 1–5% seed | Structured notes only for what unlocks next work | 10–20 min |
| 5 | Next queries | Mutate search from the seed ([`01-search-strategy.md`](01-search-strategy.md)) | 5–10 min |

Do not skip Pass 2–3 for “short” papers. Short papers still hide meaning in one plot.

---

## Pass 1 — Skim

Checklist:

- [ ] Title + authors + venue/year (mark uncertainty)
- [ ] Abstract: problem, method noun phrases, claimed contribution
- [ ] Section headings only (build a mental TOC)
- [ ] Conclusion / limitations paragraph if present
- [ ] Related-work section: note *field names* and *system names* for later cite-chase (do not deep-read yet)

**Output:** 3–6 bullet “what this appears to be about.” No RQL algebra implications yet.

---

## Pass 2 — Multimodal inventory

Use tooling when available (`extract_document.py`) plus visual skim of the PDF.

Record in `inventory` (tool JSON or notes):

1. **Text / sections** — numbered headings; appendices  
2. **Figures** — id, page, caption text, type (architecture / curve / ablation / screenshot)  
3. **Tables** — id, page, caption, what rows/cols measure  
4. **Algorithms / listings** — id, name, page  
5. **Equations** — only if they define an operator or cost model  
6. **Statistical diagrams** — ROC, latency–recall, CDF, heatmaps — treat as first-class

### Miss checklist (mandatory)

Before leaving Pass 2, answer:

- [ ] Did we open every page that contains a figure or table?  
- [ ] Are figure captions captured (not just “Figure 3 exists”)?  
- [ ] Are table headers understood enough to know the metric?  
- [ ] Are appendix figures/tables included?  
- [ ] If extraction missed images, did we still *view* them in a PDF reader?

If any answer is no → remain in Pass 2.

---

## Pass 3 — Relate components

Build an explicit relationship list (tooling: `relate_components.py` heuristics + manual edges):

| Edge type | Example |
|-----------|---------|
| `introduces` | §3.2 paragraph → Figure 3 |
| `grounds` | Table 2 → claim “X beats Y at 95% recall” |
| `implements` | Algorithm 1 → “predicate subgraph traversal” |
| `qualifies` | Limitations § → Figure 5 failure regime |
| `cites-sideways` | Related work sentence → new field token |

Heuristic anchors in text: `Figure N`, `Fig. N`, `Table N`, `Algorithm N`, `Eq. N`.

**Output:** `relations` notes or `relations.json`. Prefer a small correct graph over a large guessed one.

---

## Pass 4 — Extract only the useful 1–5%

Use [`../tooling/scripts/notes_template.md`](../tooling/scripts/notes_template.md).

Include:

- Seed statement (1–3 sentences)  
- Evidence pointers (figure/table/section ids)  
- Confidence / uncertainty  
- What this does **not** justify (anti-overclaim)  
- Steal-vs-invent hint aligned with docs/05–07 *only as hypothesis*

Do **not** rewrite docs/07 here. Promotion rules live in [`03-preprocess-and-synthesis.md`](03-preprocess-and-synthesis.md).

---

## Pass 5 — Generate next queries from the seed

Produce 2–5 mutated queries (see mutation table in [`01-search-strategy.md`](01-search-strategy.md)).  
Log them in the journal entry for this source and optionally in `NOTES-search-log.md`.

---

## Definition of done (one source)

A source is “read” only when Passes 1–5 are complete and the miss checklist is checked. Abstract-only notes do **not** count.
