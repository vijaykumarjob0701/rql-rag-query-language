---
type: FigureNote
title: Figure 1 — Apache Calcite architecture
page: 3
---

# Fig. 1 — Architecture

Block diagram: JDBC client ↔ Calcite (SQL parser/validator **or** expressions builder → **operator expressions** → query optimizer with **pluggable rules** + **metadata providers**) ↔ external data processing systems / adapters.

**Grounds:** operator-tree IR; optimizer = rules + metadata + planner engines; storage omitted.
