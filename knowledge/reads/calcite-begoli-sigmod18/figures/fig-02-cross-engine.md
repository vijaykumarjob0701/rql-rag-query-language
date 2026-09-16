---
type: FigureNote
title: Figure 2 — Cross-engine optimization process
page: 4
---

# Fig. 2 — Query optimization across conventions

Example joining Splunk + MySQL with filter/group/sort. Scans start in backend conventions; join may move across Spark or into Splunk via ODBC lookup rules — calling convention as first-class physical property.

**Grounds:** multi-backend planning; adapter-specific pushdown.
