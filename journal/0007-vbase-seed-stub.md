# 0007 — VBASE seed stub (Pass 0 / queued)

**Date:** 2026-09-16 (Europe/Dublin)  
**Type:** next-seed stub (quality over quantity — **not** a completed multimodal read)  
**Status:** queued — Pass 1–5 **not** done  
**Target:** Zhang et al. — *VBASE: Unifying Online Vector Similarity Search and Relational Queries via Relaxed Monotonicity* (OSDI 2023)  
**URLs (from `docs/references.md`):**  
- https://www.microsoft.com/en-us/research/publication/vbase-unifying-online-vector-similarity-search-and-relational-queries-via-relaxed-monotonicity/  
- https://www.usenix.org/system/files/osdi23-zhang-qianxi_1.pdf  
- https://github.com/microsoft/MSVBASE  

---

## Context

ACORN Pass 1–5 (`0006`) surfaced **iterator-style** filtered search as a sibling physical mode (`ITERATIVE`) that we must not invent from abstracts. VBASE is the preferred second seed because provisional `docs/07` leans on “ANN as Open/Next iterator” for `VSIM JOIN`.

## Question to ask next

Does VBASE actually expose vector similarity as a **monotonic iterator** composable with relational operators, and which figures define the relaxed-monotonicity guarantee vs plain TopK RPC?

## Planned Pass 1–5 (not started)

1. Download PDF to `tooling/scripts/extract_out/`  
2. `extract_document.py` + `relate_components.py`  
3. Multimodal inventory (esp. system architecture + join/iterator figures)  
4. 1–5% seed only  
5. Next queries (likely Filtered-DiskANN or RRF classic)

## 1–5% seed

**None yet** — process placeholder only.

## Uncertainty

Everything about VBASE internals remains **unread** in this repo beyond secondary mentions in provisional docs.

## Next questions

1. Open VBASE PDF and complete Pass 1 skim bullets only in a follow-up journal entry (do not expand this stub into fake notes).
