# 0005 — Correction: Google OKF, not LangExtract

**Date:** 2026-09-16 (Europe/Dublin)  
**Type:** correction / clarification  
**Status:** locked in

## What we got wrong

In `0004` and `tooling/python-libraries.md` we guessed the user’s “recent Google library for relating entities / images” was **LangExtract**.

## User correction

> The google one was **OKF**.

## What OKF actually is

**Open Knowledge Format (OKF)** — Google Cloud’s open, vendor-neutral format for knowledge as:

- a directory of **markdown concept files** + **YAML frontmatter**
- **graph-shaped** relationships via normal markdown links (not only folder hierarchy)
- optional interactive **HTML visualizer** (concepts as nodes, links as edges; ER/schema views for tables)

Primary sources:

- https://github.com/GoogleCloudPlatform/open-knowledge-format
- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
- Knowledge Catalog OKF tree: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf

## Why this matters for RQL research

OKF is less “another PDF OCR lib” and more a **target representation** for careful multimodal reading:

- Paper → extract inventory (text / figures / tables)
- Promote the useful 1–5% into **linked concepts** (claim, figure, table, operator, filter strategy…)
- Relationships stay explicit and reviewable by a human on GitHub
- Visualizer can show how we connected components — matches the journal goal

LangExtract remains optional for span-grounded extraction; it is **not** what the user meant.

## 1–5% seed → next move

Prefer emitting research notes / paper digests as **OKF-shaped bundles** under something like `knowledge/` or `reads/<paper-id>/okf/` in later journal steps — after Pass 1–5 on a real paper (e.g. ACORN).

## Files updated

- `tooling/python-libraries.md`
- this journal entry + note on `0004`
- `CHANGELOG.md`
