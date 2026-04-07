# 5 Why Analysis (五次为什么)

**Category:** Definition (问题定义)

**Framework ID:** #12

**Source:** https://pmframe.works/framework-five-why

---

## Overview

连续追问五次「为什么」，每次的答案成为下一个问题的起点，直到找到问题的根本原因而非表面症状。由丰田汽车创始人丰田佐吉提出，后成为精益生产的核心工具。

**Creator:** 丰田佐吉 (Toyota)

**Origin:** 丰田生产系统 (TPS)

---

## Core Methodology

从一个具体、可观察的问题陈述出发，每一层「为什么」都指向上一层答案的根因，直到到达无法继续追溯的根本原因。

---

## Steps

1. **问题陈述** — 从具体、可观察的问题出发
2. **W1** — 为什么发生？→ 获得第一层原因
3. **W2** — 为什么那个原因导致问题？→ 追溯更深层原因
4. **W3** — 继续追问，验证每层答案是否为事实而非假设
5. **W4** — 停在「我们可以控制的根本原因」处
6. **W5** — 实施系统性解决方案

---

## Key Principles

- "大多数问题都有系统性根因，而不是随机发生的"
- 数字「5」不是规则 — 有时3次足够，有时需要7次
- 根本原因通常是流程缺失、规则不明或资源不足
- 不要用5 Why来归咎人

---

## Use Cases

- 生产或工程事故的根因分析
- 用户流失或满意度下降的诊断
- 功能Bug反复出现的系统分析
- 产品指标异常波动的溯源
- 客户投诉背后的服务流程问题
- 团队效率低下的流程瓶颈排查

---

## Famous Case: Toyota Welding Robot Incident

> "工厂缺少预防性维护标准流程（SOP）"

追溯路径：保险丝断裂 → 电路短路 → 轴承润滑不足 → 油泵损坏 → **过滤器长期堵塞，无人定期检查**

---

## Related Frameworks

- [根本原因分析（RCA）](Root-Cause-Analysis-RCA.md)
- [问题树](Issue-Tree.md)
- [冰山模型](Iceberg-Model.md)
- [马斯克五步法](Musk-Five-Steps.md)

---

## Skill Download

**File:** `skills/five-why.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Use when drilling down to the root cause of a problem
---

# 5 Whys

A simple root-cause analysis technique that asks "why" iteratively (typically five times) to peel back symptoms and reach the fundamental cause of a problem.

## Steps

1. **State the problem** — Write a clear, specific description of the problem you are investigating.
2. **Ask "Why does this happen?"** — Answer the first why with a direct, factual cause.
3. **Repeat "Why?"** — Take the answer from the previous step and ask why again. Continue for at least five rounds.
4. **Verify the chain** — Read the causal chain in reverse ("therefore...") to confirm each link is logical.
5. **Identify the root cause and countermeasure** — The final answer should point to a systemic cause you can act on. Define a corrective action.

## Output Format

A numbered chain: Problem statement, followed by Why 1 through Why 5 (each with answer), the identified root cause, and a proposed countermeasure or action item.
```

---

*Source: [PMFrame.works - Five Why](https://pmframe.works/framework-five-why)*
