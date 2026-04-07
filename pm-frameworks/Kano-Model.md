# Kano Model (Kano 模型)

**Category:** Discovery (用户洞察)

**Framework ID:** #06

**Source:** https://pmframe.works/framework-kano-model

---

## Overview

The Kano Model helps teams prioritize features by classifying them into three categories based on how they impact user satisfaction. Not all features are equal—some are baseline requirements, others are performance drivers, and some are delightful surprises.

**Creator:** Noriaki Kano (狩野纪昭)

**Origin:** 1984 paper "Attractive Quality and Must-be Quality"

**Best For:** Feature planning periods, version iterations

**Duration:** 1 day questionnaire design, 3-5 days data analysis

---

## Core Methodology

The model uses a two-dimensional framework: feature implementation level versus user satisfaction. Features don't have a linear relationship with satisfaction—some provide diminishing returns while others create disproportionate impact.

---

## Three Feature Types

| Type | Description | Example |
|------|-------------|---------|
| **Must-be (必备型)** | Baseline expectations users assume you should have. Absence causes extreme dissatisfaction; presence doesn't generate additional satisfaction. | Phone calls work, app doesn't crash, login doesn't lose data |
| **Performance (期望型)** | Linear relationship between quality and satisfaction. Better performance = higher satisfaction. Useful for benchmarking against competitors. | Load speed, photo clarity, battery life |
| **Attractive (魅力型)** | Unexpected features that delight users. Absence doesn't cause dissatisfaction; presence creates positive surprise. Key weapon for competitive differentiation. May退化 become must-be over time. | WeChat red packets, original Siri, AirDrop |

---

## When to Use

- New feature prioritization decisions
- Competitive differentiation analysis
- User satisfaction diagnosis
- Version 0.x feature trade-offs
- High/low-end market customization
- User segmentation for differentiated needs

---

## Five Implementation Steps

1. **Collect features to evaluate** — Select 10-20 candidate features from backlog, describe each in user-perceivable terms

2. **Design Kano questionnaire** — Create positive question (How do you feel if product has this?) and negative question (How do you feel if product lacks this?) with options: Like / Should be / Neutral / Tolerable / Dislike

3. **Collect user feedback** — Gather minimum 30 valid responses (separate by segment if needed), use evaluation matrix to determine each response's category

4. **Draw classification matrix** — Count category proportions per feature, assign highest frequency as feature's Kano type, create overview visualization

5. **Develop differentiated strategy** — Must-be: ensure reliability; Performance: compare investment vs. competitors; Attractive: polish as differentiation highlight

---

## Case Study: Spotify Premium (2019-2020)

Spotify conducted Kano surveys with ~3,000 users across 60+ candidate features.

**Counterintuitive finding:** Users' most anticipated features weren't technically complex ones.

- Originally planned priority: High-definition audio (Performance type)
- Adjusted priority: Offline download stability (Must-be weakness—users leaving due to download failures) + Lyrics sync (Attractive type, low cost, high emotional value)

**Result:** After reprioritization, Premium renewal rate increased 11% over 6 months.

---

## Best Practices

**✓ Do:**
- Conduct separate surveys for different user segments—categories vary by user type
- Repeat analysis periodically—Attractive features can degrade to Must-be over time
- Combine with satisfaction coefficients (Better/Worse) for quantified priority scores
- Use concrete scenario descriptions in surveys, avoid abstract technical descriptions

**✗ Don't:**
- Use Kano results as sole decision basis—combine with development cost analysis
- Replace real surveys with internal discussions—team intuition often skews toward Attractive features
- Use sample sizes under 30—results become unreliable
- Ignore "Indifferent" features—they represent opportunities to cut costs

---

## Related Frameworks

- [User Interview Five Questions](User-Interview-Five-Questions.md) — Upstream input: interview validation of user perception assumptions
- [RICE Priority Model](RICE-Prioritization.md) — Downstream: converting demand categories into quantifiable priorities
- [MoSCoW Method](MoSCoW-Method.md) — Comparison: more intuitive must vs. optional layering approach
- [Priority Quadrant](Priority-Quadrant-Eisenhower-Matrix.md) — Downstream: mapping satisfaction tiers to priority matrix
- [Lean Canvas](Lean-Canvas.md) — Downstream: incorporating core demand insights into business model validation

---

## Skill Download

**File:** `skills/kano-model.md`

**Skill Content:**

```markdown
# Kano Model

Classify product features into categories based on how their presence or absence affects user satisfaction, guiding prioritization decisions.

## Steps

1. **List candidate features** — Gather all features or improvements under consideration.
2. **Design Kano questionnaire** — For each feature, ask two questions: "How would you feel if this feature were present?" and "How would you feel if it were absent?"
3. **Collect responses** — Survey target users using the functional/dysfunctional question pairs.
4. **Classify each feature** — Map responses to categories: Must-be (expected baseline), Performance (more is better), Delighter (unexpected wow), Indifferent, or Reverse.
5. **Prioritize** — Ensure all Must-be features are covered first, then invest in Performance features, and add Delighters for differentiation.

## Output Format

A table with columns: Feature, Category (Must-be / Performance / Delighter / Indifferent / Reverse), Evidence, and Priority recommendation.
```

---

*Source: [PMFrame.works - Kano Model](https://pmframe.works/framework-kano-model)*
