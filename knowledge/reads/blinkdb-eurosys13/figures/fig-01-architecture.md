---
type: FigureNote
title: BlinkDB Figure 1 — architecture
tags: [blinkdb, fig1]
generated:
  by: grok-bot/executor
  at: 2026-09-17T00:55:00+01:00
status: provisional
---

# Fig 1 — Architecture

Offline **Sample Creation & Maintenance** builds in-memory / on-disk samples from original data. Runtime **Sample Selection** (on Spark/Hadoop) chooses a sample for a HiveQL/SQL query with time/error constraints. Output example: count ± margin at 95% confidence.

Grounds the dual-module split RQL steals at the *idea* level (declare bound → select physical effort), not Hive implementation.
