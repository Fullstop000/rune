# Issue Tree (问题树)

**Category:** Definition (问题定义)

**Framework ID:** #15

**Source:** https://pmframe.works/framework-issue-tree

---

## Overview

Issue Tree is a core analytical tool from McKinsey and top consulting firms. Based on the MECE Principle (Mutually Exclusive, Collectively Exhaustive), it decomposes complex problems into a structured tree of sub-problems.

---

## Two Core Tree Types

| Type | Question | Purpose |
|------|----------|---------|
| **Diagnostic Tree (Why)** | "Why did this happen?" | Identifies root causes |
| **Solution Tree (How)** | "How do we achieve this?" | Identifies paths |

---

## Common Mistakes

- Overlapping branches violating MECE
- Skipping intermediate layers
- Mixing Why and How trees
- Using trees as decoration without data verification
- Failing completeness checks

---

## Applicable Scenarios

- Strategic consulting analysis
- Product growth diagnosis
- Technical debt prioritization
- Cross-department root cause alignment
- Investor pitch frameworks
- Quarterly OKR alignment

---

## Case Study: McKinsey × Major US Retailer (2010s)

- **Problem:** Two-year profit decline; management assumed high customer acquisition costs
- **Key finding:** Old customers' basket size dropped 23%, not new customer issues
- **Result:** Solution shifted to bundle sales and personalization; cost was 1/5 of original plan

---

## Related Frameworks

- [5 Why Analysis](5-Why-Analysis.md)
- [Root Cause Analysis](Root-Cause-Analysis-RCA.md)
- [First Principles](First-Principles.md)
- [Musk's Five Steps](Musk-Five-Steps.md)

---

## Skill Download

**File:** `skills/issue-tree.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Use when decomposing a complex problem into mutually exclusive, collectively exhaustive parts
---

# Issue Tree (McKinsey)

Break down a complex problem into a MECE (Mutually Exclusive, Collectively Exhaustive) tree structure so every sub-problem is distinct and no part of the problem is missed.

## Steps

1. **Define the core question** — Frame the problem as a single, clear question at the top of the tree.
2. **Create the first split** — Divide into 2-4 branches that are mutually exclusive (no overlap) and collectively exhaustive (no gaps).
3. **Decompose each branch** — Break each branch into further sub-questions, maintaining MECE at every level.
4. **Go 2-3 levels deep** — Continue until each leaf node is specific enough to be analyzed or answered directly.
5. **Prioritize branches** — Assess which branches have the highest impact or are most uncertain, and focus effort there.

## Output Format

A hierarchical tree diagram (or indented outline) with the core question at the root, 2-3 levels of MECE branches, and priority markers on the most important branches.
```

---

*Source: [PMFrame.works - Issue Tree](https://pmframe.works/framework-issue-tree)*
