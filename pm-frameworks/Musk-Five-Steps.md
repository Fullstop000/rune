# Musk Five Steps (马斯克五步法)

**Category:** Definition (问题定义)

**Framework ID:** #11

**Source:** https://pmframe.works/framework-musk-five-steps

---

## Overview

埃隆·马斯克在 SpaceX 与特斯拉工程实践中总结的设计原则：在优化或自动化任何事情之前，先质疑其存在的必要性，再不断精简。

> "大多数团队在优化不该存在的东西"

---

## Core Problem

工程师和产品团队有根深蒂固的惯性：拿到需求就开始想怎么实现、怎么优化，而很少问——这个需求本身应该存在吗？结果是他们不断优化错误的事情。

---

## The Five-Step Framework

| Step | Name | Core Principle |
|------|------|----------------|
| 01 | **质疑需求 (Question)** | 追溯需求的提出者，从源头质疑每一个需求 |
| 02 | **删除冗余 (Delete)** | 删除零件、步骤、功能。删除的东西中没有10%需要加回来，说明删得还不够 |
| 03 | **简化优化 (Simplify)** | 只在删除之后，对剩下的东西进行简化 |
| 04 | **加速执行 (Accelerate)** | 缩短周期、提高频率——此刻加速的是前三步验证过的正确事情 |
| 05 | **最后自动化 (Automate)** | 自动化是最后一步，对糟糕流程的自动化只会让糟糕发生得更快 |

> "跳过质疑直接进入执行，是最常见也是最昂贵的错误"

---

## Applicable Scenarios

1. 功能规划前的需求审查
2. 工程部署流程优化 (CI/CD)
3. 注册/激活流程精简
4. 产品路线图优先级过滤
5. 服务运营流程重新设计
6. 组织与会议流程精简

---

## Case Study: SpaceX Falcon 9 Merlin 发动机支架

| Stage | Before | After |
|-------|--------|-------|
| 零件数 | 83个独立零件 | 1个整体零件 |
| 制造周期 | 3周 | 3天 |
| 成本 | 基准 | **下降75%** |

### Five-Step Application Process

1. **质疑规格来源**：追溯发现原始规格复制自航空行业标准，但火箭不是飞机
2. **删除复杂几何**：为不必要规格存在的复杂形状被消除
3. **简化设计**：用更少材料和单一几何形态重新设计
4. **加速制造**：因为制造的东西变简单了
5. **自动化**：只在此时针对已简化的单一零件引入CNC自动化

---

## Usage Recommendations

1. 步骤顺序很重要——跳过质疑直接自动化是最常见的错误
2. 每个需求都有一个负责人——追溯到人，才能真正质疑它
3. "删除"不是妥协，而是最难的设计决策
4. 用这个框架审查产品路线图上每一个功能——通常缩减30-50%
5. 每个季度问一次："我们做的哪10%的事情根本不应该存在？"

---

## Related Frameworks

- [第一性原理](First-Principles.md) — 用第一性原理支撑每步的本质拆解
- [5 Why 分析](5-Why-Analysis.md) — 深挖各步骤中的问题根因
- [问题树](Issue-Tree.md) — 结构化拆解优化目标
- [根本原因分析](Root-Cause-Analysis-RCA.md) — 对识别的无效环节做根本原因分析

---

## Skill Download

**File:** `skills/musk-five-steps.md`

**Skill Content:**

```markdown
# Summary of Musk's Five-Step Process

This document outlines a framework for radical simplification through five sequential steps:

1. **Question requirements** - Challenge every assumption, especially those from experts
2. **Delete** - Remove unnecessary parts aggressively (aim for 10%+ restoration threshold)
3. **Simplify and optimize** - Only after deletion; don't optimize what shouldn't exist
4. **Accelerate** - Speed up only after steps 1-3 are complete
5. **Automate** - Last, never first; automating flaws locks them in
```

---

*Source: [PMFrame.works - Musk Five Steps](https://pmframe.works/framework-musk-five-steps)*
