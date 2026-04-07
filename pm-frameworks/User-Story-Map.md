# User Story Map (用户故事地图)

**Category:** Execution (执行落地)

**Framework ID:** #46

**Source:** https://pmframe.works/framework-user-story-map

---

## Overview

A framework that organizes user stories into three layers ("User Activity → Task → Sub-task") with the horizontal axis showing the user journey and the vertical axis representing priority. Helps teams plan meaningful MVP boundaries through "horizontal slicing" rather than random feature cutting.

**Creator:** Jeff Patton

**Year:** 2005 (book published 2014)

---

## Three Layers

| Layer | Description |
|-------|-------------|
| **Layer 1 (Top): User Activities** | Major steps forming the "skeleton" |
| **Layer 2 (Middle): Tasks** | Specific operations to complete each activity |
| **Layer 3 (Bottom): Sub-tasks** | Edge cases, optimizations, details |

**Horizontal = time sequence; Vertical = priority** (Release Line separates versions)

---

## Key Principles

1. Tell the user story first, not from the feature list
2. Skeleton uses user language, not technical terms
3. Vertical slices must deliver complete user experience even if small
4. Each Release line should be an independently verifiable hypothesis
5. Keep the map updated as a living document

---

## Applicable Scenarios

- Define MVP feature boundaries
- New product scope planning
- Cross-team feature priority alignment
- Break large Epics into iterative releases
- Identify gaps and breakpoints in user experience
- Product refactor or redesign scope planning

---

## Case Study: Salesforce Sales Cloud (2013)

- 2-day story mapping workshop with real sales reps, managers, and engineering
- Found 40% of planned features corresponded to abandoned workflows
- Release 1 development cycle reduced from 8 months to 3 months
- Covered 60%+ of users' core daily operations

---

## Related Frameworks

- [Sprint Framework](Sprint-Framework.md) (downstream)
- [Shape Up](Shape-Up.md) (comparable)
- [Opportunity Solution Tree](Opportunity-Solution-Tree.md) (upstream)
- [NOW-NEXT-LATER Roadmap](NOW-NEXT-LATER-Roadmap.md) (downstream)

---

## Skill Download

**File:** `skills/user-story-map.md`

**Skill Content:**

```markdown
# User Story Mapping (Jeff Patton)

Arrange user stories along a horizontal activity backbone and slice vertically into releases. Use when planning what to build first and ensuring each release delivers a complete user journey.

## Steps

1. **Frame the journey** — identify the user persona and their end-to-end goal.
2. **Build the backbone** — list major user activities left to right in chronological order.
3. **Add tasks** — under each activity, list the specific tasks users perform.
4. **Add stories** — under each task, write user stories as vertical cards, ordered by priority (top = highest).
5. **Draw release slices** — draw horizontal lines to group stories into releases; each slice should deliver a walkable end-to-end experience.

## Output Format

A two-dimensional map: horizontal axis = activities and tasks (the backbone), vertical axis = stories ordered by priority, with horizontal lines marking release boundaries. Include a summary of what each release delivers.
```

---

*Source: [PMFrame.works - User Story Map](https://pmframe.works/framework-user-story-map)*
