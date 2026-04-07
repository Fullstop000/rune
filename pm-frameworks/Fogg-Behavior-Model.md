# Fogg Behavior Model (Fogg 行为模型)

**Category:** Growth (增长策略)

**Framework ID:** #70

**Source:** https://pmframe.works/framework-fogg-behavior-model

---

## Overview

B = MAP。行为发生的那一刻，动机（Motivation）、能力（Ability）和触发（Prompt）必须同时到位。

**Creator:** B.J. Fogg (Stanford)

---

## Core Concepts

| Element | Description |
|---------|-------------|
| **Motivation (M)** | 用户有多想完成这个行为？来源：快感/痛苦、希望/恐惧、社会认同/排斥 |
| **Ability (A)** | 用户完成这个行为有多简单？影响因素：时间成本、金钱成本、脑力消耗、体力消耗、与日常习惯偏差 |
| **Prompt (P)** | 用户在正确时刻被提醒了吗？三种触发类型：Spark（低动机时激励）、Facilitator（低能力时提供帮助）、Signal（高动机高能力只需信号） |

---

## Key Steps

1. 选定目标行为 (30分钟) — 定义具体可观察的行为
2. 评估当前 MAP 状态 (45分钟) — 动机、能力、触发三项评分
3. 设计能力干预 (设计 Sprint) — 缩小行为，降低门槛
4. 设计触发策略 (设计 Sprint) — 选择正确触发类型和时机
5. 测量并迭代 (2周周期) — 监控指标，持续优化

---

## Case Study: Duolingo Streak Feature Redesign (2017-2018)

**Problem:** 2016-2017严重留存危机，用户在3-4天后参与度下降

**MAP Diagnosis:**
- M: Decay — 初始热情消退，无可见进度
- A: Low — 10-15分钟课程对忙碌用户要求过高
- P: Failed — 在错误时间发送通用提醒

**Interventions:**
- A: 引入"5分钟微课程"
- M: Streak Counter使进度可见
- P: 基于用户行为数据的个性化推送通知

**Results:** +14% 30天留存率，DAU从15M增长到25M（18个月）

---

## Related Frameworks

- [Hook 上钩模型](Hook-Model.md)
- [用户旅程地图](User-Journey-Map.md)
- [Kano 模型](Kano-Model.md)

---

## Skill Download

**File:** `skills/fogg-behavior-model.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Diagnose why users are not taking a desired action using the B=MAP behavior model
---

# Fogg Behavior Model

Behavior happens when Motivation, Ability, and a Prompt converge at the same moment: B = MAP.

## Steps

1. Define the **target behavior** you want users to perform
2. Assess **Motivation** -- is the user motivated enough? (pleasure/pain, hope/fear, belonging/rejection)
3. Assess **Ability** -- is it easy enough? Audit time, money, effort, cognitive load, and social deviance
4. Assess **Prompt** -- is there a well-timed trigger? Check if it is noticeable and actionable
5. Identify which factor is the bottleneck (low motivation, low ability, or missing prompt)
6. Design interventions for the bottleneck -- simplify, motivate, or add prompts

## Output Format

**Target behavior:** [What you want users to do]

| Factor | Current State | Bottleneck? | Intervention |
|--------|-------------|------------|-------------|
| Motivation | [H/M/L] | [Yes/No] | [Action] |
| Ability | [H/M/L] | [Yes/No] | [Action] |
| Prompt | [Present/Absent] | [Yes/No] | [Action] |

**Primary fix:** [Simplify / Motivate / Prompt]
```

---

*Source: [PMFrame.works - Fogg Behavior Model](https://pmframe.works/framework-fogg-behavior-model)*
