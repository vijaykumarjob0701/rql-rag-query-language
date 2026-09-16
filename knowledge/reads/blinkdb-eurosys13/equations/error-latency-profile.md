---
type: EquationNote
title: BlinkDB Error-Latency Profile (ELP) sketch
tags: [blinkdb, elp]
generated:
  by: grok-bot/executor
  at: 2026-09-17T00:55:00+01:00
status: provisional
---

# ELP (sketch)

For aggregates in Table 2, estimator variance scales ~1/n (hence std-error ~1/√n) in the number of matching sample rows n.

**Error profile:** given target std-error, solve for required n from Table 2; pick smallest sample resolution K expected to yield ≥ n matches.

**Latency profile:** assume query time scales ~linearly with rows read (after small pilot runs to fit rates); pick largest K still under time bound.

RQL analogy (Hypothesis): replace n with ANN candidate effort; replace std-error with a **recall proxy** — mapping is packaging, not a theorem from BlinkDB.
