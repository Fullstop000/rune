# ICE Scoring (ICE 评分模型)

**Category:** Execution (执行落地)

**Framework ID:** #51

**Source:** https://pmframe.works/framework-ice

---

## Overview

A prioritization framework for growth experiments and feature ideas using three dimensions: Impact × Confidence × Ease. Scores range from 1-1000, enabling teams to rank 15+ ideas in 30 minutes.

**Creator:** Sean Ellis (GrowthHackers)

**Year:** Early 2010s

---

## The Three Dimensions

| Dimension | Description | Score Meaning |
|-----------|-------------|---------------|
| **I - Impact** | Effect on core metrics (DAU, conversion, revenue) | 10 = game-changing, 1 = negligible |
| **C - Confidence** | Evidence supporting the hypothesis | 10 = substantial data, 1 = pure guess |
| **E - Ease** | Implementation difficulty (time, resources, dependencies) | 10 = days, 1 = months |

**Formula:** ICE Score = I × C × E

---

## Key Insight

"AI recommendation engine rebuild" might score Impact=10, but Confidence=4, Ease=2 = score of 80. A simpler idea might score 648 despite sounding less impressive.

---

## Related Frameworks

- [RICE](RICE-Prioritization.md) - Adds Reach dimension for more comprehensive scoring
- [MoSCoW](MoSCoW-Method.md) - Categorization complement for team communication
- [Impact/Effort Matrix](Impact-Effort-Matrix.md) - Visual mapping of ICE results
- [Priority Quadrant](Priority-Quadrant-Eisenhower-Matrix.md) - Four-quadrant visualization for discussions

---

## Skill Download

**File:** `skills/ice.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Score and rank experiments or feature ideas by Impact, Confidence, and Ease
---

# ICE Scoring

Prioritize experiments by scoring each on three dimensions (1-10) and multiplying to get a composite rank.

## Steps

1. List all candidate experiments or feature ideas
2. Score **Impact** (1-10): How much will this move the target metric if it works?
3. Score **Confidence** (1-10): How sure are you it will work, based on evidence?
4. Score **Ease** (1-10): How quickly and cheaply can you run this experiment?
5. Calculate ICE = Impact x Confidence x Ease for each item
6. Rank by ICE score and select the top experiments to run

## Output Format

| Experiment | Impact | Confidence | Ease | ICE Score |
|-----------|--------|-----------|------|-----------|
| [Idea 1] | [1-10] | [1-10] | [1-10] | [Score] |
| [Idea 2] | [1-10] | [1-10] | [1-10] | [Score] |

**Selected for next sprint:** [Top N experiments]
```

---

*Source: [PMFrame.works - ICE Scoring](https://pmframe.works/framework-ice)*
