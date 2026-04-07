# LTV-CAC Framework (LTV-CAC 框架)

**Category:** Growth (增长策略)

**Framework ID:** #65

**Source:** https://pmframe.works/framework-ltv-cac

---

## Overview

User Lifetime Value to Customer Acquisition Cost ratio is core growth health indicator—typically requires LTV/CAC ≥ 3.

---

## Formulas

| Metric | Formula |
|--------|---------|
| **LTV** | LTV = ARPU × (1 / Monthly Churn Rate) × Gross Margin |
| **CAC** | Total Sales + Marketing Spend / New Customers Acquired |
| **LTV:CAC** | LTV / CAC |
| **CAC Payback Period** | CAC / (ARPU × Gross Margin) |

---

## Benchmarks

| Ratio | Status |
|-------|--------|
| **< 1** | Losing money on each customer |
| **1-3** | Warning zone |
| **= 3** | Healthy (target) |
| **> 5** | Not investing enough in growth |

---

## Case Study: HubSpot (2011-2014)

- Started at 1.5:1 ratio (danger zone), reached 4.7:1 by IPO
- CAC payback period: 11 months
- Tactics: Inbound content marketing reduced CAC 60%; upsell to mid-market reduced churn from 5%+ to 1-2%

---

## Related Frameworks

- [AARRR Pirate Metrics](AARRR-Pirate-Metrics.md)
- [Growth Flywheel](Growth-Flywheel.md)
- [PMF Framework](Product-Market-Fit-PMF.md)
- [North Star Metric](North-Star-Metric.md)

---

## Skill Download

**File:** `skills/ltv-cac.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Evaluate unit economics by comparing Customer Lifetime Value to Customer Acquisition Cost
---

# LTV-CAC Framework

Assess business sustainability by calculating the ratio of what a customer is worth versus what it costs to acquire them.

## Steps

1. Calculate **CAC** -- total sales + marketing spend / number of new customers acquired
2. Calculate **CLV** -- average revenue per user x gross margin x average lifespan (months)
3. Compute **CLV:CAC ratio** (healthy target: 3:1 or higher)
4. Measure **CAC payback period** -- months to recover acquisition cost
5. Segment by channel, cohort, or plan to find the most efficient growth paths
6. Identify levers to improve: reduce CAC, increase ARPU, extend retention, or improve margins

## Output Format

| Metric | Value |
|--------|-------|
| CAC | $[X] |
| CLV | $[X] |
| CLV:CAC Ratio | [X]:1 |
| Payback Period | [X] months |
| Best Channel | [Channel] (CAC: $[X]) |

**Health check:** [Healthy / Warning / Unsustainable]
**Top lever:** [Recommended improvement area]
```

---

*Source: [PMFrame.works - LTV-CAC](https://pmframe.works/framework-ltv-cac)*
