# Event Storming (事件风暴)

**Category:** Definition (问题定义)

**Framework ID:** #23

**Source:** https://pmframe.works/framework-event-storming

---

## Overview

DDD collaboration tool using "domain events" sticky notes to rapidly model complex business processes and identify system boundaries.

**Creator:** Alberto Brandolini

**Year:** 2012

---

## Process

1. **Brainstorm events** — Write domain events on orange stickies
2. **Arrange chronologically** — Timeline of events
3. **Add commands** — What triggers each event
4. **Add actors** — Who performs actions
5. **Identify aggregates** — Group related objects
6. **Find bounded contexts** — System boundaries

---

## When to Use

- Domain-driven design
- Business process modeling
- Team alignment on processes
- System architecture planning

---

## Related Frameworks

- [User Journey Map](User-Journey-Map.md)
- [Service Blueprint](Service-Blueprint.md)
- [Systems Thinking](Systems-Thinking.md)

---

## Skill Download

**File:** `skills/event-storming.md` (inferred from pattern)

---

## Skill Content

```markdown
---
description: Model a business domain collaboratively by mapping domain events, commands, and aggregates
---

# Event Storming

A workshop-based technique for discovering domain complexity by mapping events on a timeline, then layering commands, actors, and policies.

## Steps

1. **Chaotic exploration** -- everyone writes domain events (past tense verbs) on orange sticky notes
2. **Timeline ordering** -- arrange events left-to-right in chronological flow
3. **Add commands** -- identify what triggers each event (blue stickies)
4. **Add actors and systems** -- note who or what issues each command (yellow stickies)
5. **Identify aggregates and bounded contexts** -- group related events into clusters
6. **Surface hotspots** -- mark conflicts, unknowns, or bottlenecks with pink stickies

## Output Format

**Event Flow:** [Ordered list of domain events]
**Commands:** [Trigger -> Event mappings]
**Aggregates:** [Clustered event groups with names]
**Bounded Contexts:** [Context boundaries and relationships]
**Hotspots:** [Open questions and risks]
```

---

*Source: [PMFrame.works - Event Storming](https://pmframe.works/framework-event-storming)*
