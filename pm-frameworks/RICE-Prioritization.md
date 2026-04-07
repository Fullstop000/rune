# RICE Prioritization (RICE 优先级模型)

**Category:** Execution (执行落地)

**Framework ID:** #47

**Source:** https://pmframe.works/framework-rice

---

## Overview

RICE is a quantitative prioritization framework that transforms vague "feelings" into discussable numbers through four dimensions.

**Origin:** Intercom 产品团队

**Creator:** Sean McBride

**Year:** 2015年

**Core Formula:** R × I × C ÷ E = RICE Score

---

## Four Dimensions

| Dimension | Description | Scale |
|-----------|-------------|-------|
| **R (Reach)** | 触达量：每周期内受影响用户数 | Number |
| **I (Impact)** | 影响力：对核心指标的影响程度 | 0.25-3量表 |
| **C (Confidence)** | 信心值：对估算的确定程度 | 50%-100% |
| **E (Effort)** | 工作量：完成所需人月数（设计+工程+测试） | Person-months |

---

## What It Solves

优先级讨论常变成「谁嗓门大谁赢」，RICE让争论从「我觉得」转向「我的数据是」。

---

## When to Use

1. 季度规划时的功能优先级排序
2. 多产品线的资源分配决策
3. 团队对优先级有强烈分歧时
4. PM向工程团队解释排序逻辑
5. 评估是否值得投入技术债偿还
6. 新功能vs体验优化的取舍

---

## Usage Principles

1. 先对齐Reach的定义单位
2. Impact分数要和具体指标挂钩
3. Confidence低于50%时先做小实验
4. Effort用相对单位（人月）而非绝对天数
5. RICE分数是对话起点，不是终点

---

## Case Study: Intercom (2015)

将季度规划会议从3周压缩至4天，发现Reach估算差异最大（同一功能PM和销售估算可能相差10倍）。

---

## Related Frameworks

- [ICE评分模型](ICE-Scoring.md)
- [MoSCoW方法](MoSCoW-Method.md)
- [Impact Effort矩阵](Impact-Effort-Matrix.md)
- [需求优先级四象限](Priority-Quadrant-Eisenhower-Matrix.md)
- [Kano模型](Kano-Model.md)

---

## Skill Download

**File:** `skills/rice.md`

**Skill Content:**

```markdown
# RICE Prioritization

Score and rank features or initiatives using a consistent formula to remove bias from prioritization. Use when your backlog has many competing items and stakeholders disagree on order.

## Steps

1. **Reach** — estimate how many users/events this will affect in a given time period.
2. **Impact** — rate the expected effect per user (3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal).
3. **Confidence** — rate how certain you are about estimates (100% = high, 80% = medium, 50% = low).
4. **Effort** — estimate work required in person-months (or person-weeks).
5. **Calculate** — RICE Score = (Reach x Impact x Confidence) / Effort.
6. **Rank** — sort by score descending; review the top items for sanity.

## Output Format

A ranked table with columns: Feature, Reach, Impact, Confidence, Effort, RICE Score. Include a brief rationale for each estimate.
```

---

*Source: [PMFrame.works - RICE](https://pmframe.works/framework-rice)*
