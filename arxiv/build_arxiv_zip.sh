#!/usr/bin/env bash
# Pack a clean arXiv TeX source tree (no aux junk).
# Run from anywhere; resolves paths relative to this script.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
THESIS="$ROOT/thesis"
ARXIV="$ROOT/arxiv"
STAGE="$ARXIV/_stage_rql"
ZIP="$ARXIV/rql-arxiv-source.zip"
PDF_OUT="$ARXIV/rql-arxiv.pdf"

echo "[arxiv] research root: $ROOT"

if [[ ! -f "$THESIS/main.tex" ]]; then
  echo "ERROR: missing $THESIS/main.tex" >&2
  exit 1
fi

# Prefer an already-built PDF; rebuild if latexmk available and PDF missing/stale intent.
if [[ ! -f "$THESIS/main.pdf" ]]; then
  echo "[arxiv] main.pdf missing — attempting latexmk build"
  (cd "$THESIS" && latexmk -pdf -interaction=nonstopmode main.tex)
fi

# Ensure .bbl exists (arXiv often needs it).
if [[ ! -f "$THESIS/main.bbl" ]]; then
  echo "[arxiv] main.bbl missing — running bibtex pass"
  (cd "$THESIS" && pdflatex -interaction=nonstopmode main.tex >/dev/null \
    && bibtex main \
    && pdflatex -interaction=nonstopmode main.tex >/dev/null \
    && pdflatex -interaction=nonstopmode main.tex >/dev/null)
fi

rm -rf "$STAGE"
mkdir -p "$STAGE/sections" "$STAGE/figures"

# Core sources
cp "$THESIS/main.tex" "$STAGE/"
cp "$THESIS/references.bib" "$STAGE/"
cp "$THESIS/main.bbl" "$STAGE/"
cp "$ARXIV/00README.XXX" "$STAGE/"

# Sections + TikZ figures only (no tables/ junk placeholders)
cp "$THESIS"/sections/*.tex "$STAGE/sections/"
cp "$THESIS"/figures/*.tikz "$STAGE/figures/" 2>/dev/null || true

# Strip absolute paths / local-only noise if any future generated files appear
# (currently none).

rm -f "$ZIP"
(
  cd "$STAGE"
  # Zip contents at archive root (main.tex at top level) — arXiv expects this.
  zip -r -q "$ZIP" . \
    -x '*.aux' '*.log' '*.out' '*.fls' '*.fdb_latexmk' '*.blg' \
       '*.synctex.gz' '*.pdf' '*~' '*/.DS_Store'
)

cp -f "$THESIS/main.pdf" "$PDF_OUT"

echo "[arxiv] wrote $ZIP"
unzip -l "$ZIP" | sed -n '1,40p'
echo "[arxiv] wrote $PDF_OUT ($(pdfinfo "$PDF_OUT" 2>/dev/null | awk '/Pages/{print $2}') pages)"
echo "[arxiv] stage kept at $STAGE (safe to delete)"
