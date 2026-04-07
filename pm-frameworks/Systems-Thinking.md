# Systems Thinking (系统思维)

**Category:** Systems Thinking (系统思维)

**Framework ID:** #72

**Source:** https://pmframe.works/framework-systems-thinking

---

## Overview

不把问题孤立分析，而是看清各元素间的相互作用、反馈回路和涌现行为，找到真正能撬动系统的杠杆点

**Origin:** Donella Meadows, MIT System Dynamics

---

## Core Methodology - Causal Loop Diagram (CLD)

| Loop Type | Description |
|-----------|-------------|
| **Reinforcing Loops (R)** | Self-amplifying (e.g., word-of-mouth → new users → social proof → more spread) |
| **Balancing Loops (B)** | Self-regulating (e.g., user growth → infrastructure strain → performance decline → churn) |

**Three Elements:**
- **Stocks** (accumulations)
- **Flows** (rates of change)
- **Delays** (time between cause and effect)

---

## Donella Meadows Leverage Points (High to Low)

1. Change system goals and paradigms
2. Change feedback loop structure
3. Change delay duration in loops
4. Adjust flow parameters (lowest leverage)

---

## Case Study: Twitter/X Double Loop Dilemma

- **Enhancement loop:** Celebrity joins → fans flood → higher visibility → more celebrities
- **Balancing loop:** More celebrities → platform visibility → hate speech influx → safety decline → celebrities leave
- **Conclusion:** Leverage point is platform safety culture, not feature improvements

---

## Common Pitfalls

1. Drawing loop diagrams but not using for decisions
2. Ignoring delays in feedback loops
3. Treating correlation as causation in diagrams
4. Models too complex (>10-15 nodes)
5. Using systems thinking as pure analysis not action tool
6. Not identifying leverage point hierarchy before optimizing

---

## Related Frameworks

- [冰山模型](Iceberg-Model.md)
- [系统基模](Systems-Archetypes.md)
- [Cynefin框架](Cynefin-Framework.md)
- [约束理论](Theory-of-Constraints.md)
- [Wardley地图](Wardley-Mapping.md)

---

## Skill Download

**File:** `skills/systems-thinking.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Map feedback loops, delays, and leverage points to understand complex system behavior
---

# Systems Thinking

Understand why a system behaves the way it does by mapping its feedback loops, stocks, flows, and delays.

## Steps

1. Define the **system boundary** -- what is inside and outside the analysis?
2. Identify **stocks** (accumulations) and **flows** (rates of change)
3. Map **reinforcing loops** (R) -- virtuous or vicious cycles that amplify change
4. Map **balancing loops** (B) -- stabilizing forces that resist change
5. Identify **delays** -- where time lags cause oscillation or overshoot
6. Find **leverage points** -- where a small intervention produces outsized impact

## Output Format

**System boundary:** [What is in scope]

**Causal loop diagram:**
- R1: [Variable A] -> [Variable B] -> [Variable A] (reinforcing)
- B1: [Variable C] -> [Variable D] -> [Variable C] (balancing)

**Key delays:** [Where and how long]
**Leverage points:** [Ranked by impact]
**Recommended intervention:** [Action at highest leverage point]
```

---

*Source: [PMFrame.works - Systems Thinking](https://pmframe.works/framework-systems-thinking)*
