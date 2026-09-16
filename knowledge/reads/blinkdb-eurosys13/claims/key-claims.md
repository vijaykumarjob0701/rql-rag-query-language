---
type: Claims
title: BlinkDB key claims (honesty-tagged)
tags: [blinkdb, claims]
generated:
  by: grok-bot/executor
  at: 2026-09-17T00:55:00+01:00
status: provisional
---

# Key claims

| Claim | Tag | Evidence |
|-------|-----|----------|
| Dual query contracts: `ERROR WITHIN ε AT CONFIDENCE C` **or** `WITHIN T` (with reported relative error) | **Established** (mechanism / surface) | §2 examples p.3 |
| Offline multi-dim multi-res stratified (+ uniform) sample families; runtime picks family + resolution | **Established** (mechanism) | Fig 1–2; §3; §4 |
| ELP: pilot small samples → project error (~1/√n) and latency (~linear rows) to meet constraint | **Established** (mechanism) | §4.2; Table 2 |
| Closed-form variance for Avg/Count/Sum/Quantile | **Established** (AQP aggregates) | Table 2 |
| 17 TB / <2s / 2–10% error on 100-node cluster | **AUTHOR-only / Provisional** | Abstract; §6 — **not reproduced** |
| RQL `RECALL TARGET` / `LATENCY` ≡ BlinkDB ERROR/TIME | **False / do not claim** | Category error: ANN recall ≠ aggregate sampling error |
| RQL budgets packaging + planner binding | **Hypothesis** | thesis §06; schemas PhysicalPlan `budgets` |
