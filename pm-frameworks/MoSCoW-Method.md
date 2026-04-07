# MoSCoW Method (MoSCoW 方法)

**Category:** Execution (执行落地)

**Framework ID:** #48

**Source:** https://pmframe.works/framework-moscow

---

## Overview

将需求分为必须有、应该有、可以有、这次不做四类，快速在团队内建立优先级共识，避免功能范围蔓延。

**Creator:** Dai Clegg (Oracle UK)

**Year:** 1994

---

## The Four Categories

| Category | Definition | Target Ratio |
|----------|------------|--------------|
| **M - Must Have 必须有** | 没有它产品无法运作，MVP 的底线 | ~60% |
| **S - Should Have 应该有** | 重要但非绝对必要，可以延期 | ~20% |
| **C - Could Have 可以有** | 只有时间充裕才做，锦上添花 | ~10% |
| **W - Won't Have 这次不做** | 明确声明这次不做，但不代表永远不做 | ~10% |

---

## What It Solves

失败的 Sprint 和延期上线，最常见的根本原因是范围蔓延——那些看起来「只要加一下」的功能，不断积累。MoSCoW 强制团队回答核心问题：「如果这个功能没做，会怎样？」

---

## Key Recommendations

1. Must Have 超过 60% 是危险信号——必须重新讨论
2. 一定要让工程师参与 MoSCoW，而不只是 PM 和业务方
3. 明确定义「这次」的时间范围，否则每个讨论都会失焦
4. Won't Have 列表需要被定期回顾，但不是随时可以推翻
5. MoSCoW 的输出必须有利益相关者的签字认可，否则它没有约束力

---

## Case Study: UK Government Digital Service GOV.UK (2011-2013)

- 10个月从立项到上线（政府项目通常需要数年）
- 650+ 被整合替代的分散政府网站
- 2013 年度设计奖得主

---

## Related Frameworks

- [RICE 优先级模型](RICE-Prioritization.md)
- [ICE 评分模型](ICE-Scoring.md)
- [Impact Effort 矩阵](Impact-Effort-Matrix.md)
- [需求优先级四象限](Priority-Quadrant-Eisenhower-Matrix.md)
- [用户故事地图](User-Story-Map.md)

---

## Skill Download

**File:** `skills/moscow.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Categorize requirements as Must, Should, Could, or Won't have
---

# MoSCoW Method

Classify requirements into four priority buckets to reach consensus on scope. Use when negotiating scope with stakeholders or planning a release with limited resources.

## Steps

1. **List all requirements** — gather features, stories, or tasks for the release.
2. **Must Have** — requirements that are non-negotiable; without them the release fails.
3. **Should Have** — important but not critical; painful to leave out but the release still works.
4. **Could Have** — nice-to-have; include only if time and budget allow.
5. **Won't Have (this time)** — explicitly agreed to be out of scope for this release.
6. **Validate** — ensure Must Haves do not exceed ~60% of capacity; adjust if needed.

## Output Format

A four-column table (Must / Should / Could / Won't) listing each requirement, with a summary showing the percentage of effort allocated to each category.
```

---

*Source: [PMFrame.works - MoSCoW](https://pmframe.works/framework-moscow)*
