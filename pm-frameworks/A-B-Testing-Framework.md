# A/B Testing Framework (A/B 测试框架)

**Category:** Validation (验证测试)

**Framework ID:** #34

**Source:** https://pmframe.works/framework-ab-testing

---

## Overview

The most rigorous product validation tool — hands product decisions over to data, not opinions. Tells you which version is "actually" better, not "feels" better.

**Core Mechanism:** Randomly divide traffic into two groups — one sees Version A, one sees Version B — and measure which performs better on key metrics.

---

## Seven-Step Process

| Step | Name | Description |
|------|------|-------------|
| 01 | Hypothesis | Clearly state what you believe will improve which metric |
| 02 | Design Variant | Change only one variable, keep everything else identical |
| 03 | Random Split | 50% users see A, 50% see B, eliminate selection bias |
| 04 | Run Experiment | Wait until reaching expected sample size, don't stop mid-way |
| 05 | Collect Data | Record key metric changes, including negative signals |
| 06 | Statistical Analysis | Calculate p-value, confirm 95% confidence level |
| 07 | Decision | Roll out winning version, or learn from failure |

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| Control Group | Existing version, baseline |
| Variant | New version changing one variable |
| Sample Size | At least 1,000 conversions per variant |
| Statistical Significance | 95% confidence = p < 0.05 |
| P-value | Probability result came from luck |
| Effect Size | How much the metric actually moved |

---

## Case Studies

**Google - 41 Blue Shades Test (2000):** Tested 41 different blue shades for toolbar links; winning blue generated ~$200M additional ad revenue annually. Ran 7,000+ A/B tests in 2011.

**Amazon - Remove Mandatory Registration (2004):** Changed mandatory registration to optional "guest checkout"; purchases increased 45%, generating ~$300M additional revenue in first year.

---

## Common Mistakes

1. Testing before sufficient sample size
2. Stopping early when results look good (p-hacking)
3. Changing multiple variables simultaneously
4. Ignoring novelty effects
5. Global winners may be losers for specific user groups

---

## Related Frameworks

- [North Star Metric Framework](North-Star-Metric.md) (validation tool)
- [HEART Framework](HEART-Framework.md) (upstream)
- [Validated Learning Loop](Validated-Learning-Loop.md) (downstream)
- [Task Completion Rate Testing](Task-Completion-Rate-Test.md) (complementary)
- [AARRR 海盗指标](AARRR-Pirate-Metrics.md) (upstream)

---

## Skill Download

**File:** `skills/ab-testing.md`

**Skill Content:**

```markdown
# A/B Testing Framework

Compare two variants with statistical rigor to determine which performs better. Use when you have enough traffic and need data-driven evidence before shipping a change.

## Steps

1. **Hypothesis** — state what you expect to change and why (e.g., "Changing CTA color to green will increase click-through by 10%").
2. **Metric** — define the primary metric and any guardrail metrics.
3. **Variant design** — create control (A) and treatment (B); change only one variable.
4. **Sample size** — calculate required sample size for desired statistical power (typically 80%) and significance (p < 0.05).
5. **Run** — randomly assign users, run until sample size is reached; do not peek early.
6. **Analyze** — compute statistical significance, effect size, and check guardrail metrics.

## Output Format

A test plan document with hypothesis, metrics, variant descriptions, sample size calculation, run duration estimate, and a results summary table with confidence intervals.
```

---

*Source: [PMFrame.works - A/B Testing](https://pmframe.works/framework-ab-testing)*
