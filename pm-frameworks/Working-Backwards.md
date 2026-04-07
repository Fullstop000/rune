# Working Backwards (反向工作法)

**Category:** Definition (问题定义)

**Framework ID:** #22

**Source:** https://pmframe.works/framework-working-backwards

---

## Overview

Amazon's product development method requiring teams to write a press release and FAQ for a hypothetical shipped product *before* writing any code. If you can't clearly articulate customer value, it's not worth building.

**Creator:** Jeff Bezos (Amazon)

**Year:** 2004 (mandated internally)

---

## Two Core Documents

### 1. Press Release Template

| Element | Description |
|---------|-------------|
| Headline | One-sentence problem/solution statement |
| Subheadline | Specific customer benefit, not feature lists |
| Problem | Real customer pain in relatable scenarios |
| Solution | User experience focus, not technical specs |
| Customer Quote | Authentic sounding (not marketing speak) |
| Team Quote | Product philosophy explanation |
| Call to Action | Clear next steps for users |

### 2. FAQ Components

| Type | Description |
|------|-------------|
| External FAQ | Purchase decision questions (differentiation, pricing, security) |
| Internal FAQ | Feasibility questions (tech requirements, timeline, scalability) |

---

## Key Rule

5-10 revision rounds are normal. If it feels "good enough" early, it isn't ready.

---

## Case Study: Amazon Kindle (2006-2007)

| Press Release Claim | Hidden Requirement | Solution |
|---|---|---|
| "Wireless delivery" | Sprint network protocol (nonexistent) | Negotiated Whispernet, Amazon subsidized data |
| "Any book, 60 seconds" | Publisher rights (none signed) | 18 months of publisher negotiations |
| "No monthly fees" | Business model to cover costs | $399 hardware + content revenue model |

---

## Applicable Scenarios

- New product value validation before engineering resources
- Major feature alignment across teams
- Preventing feature creep
- Executive presentations
- Cross-team early alignment
- B2B product value definition

---

## Related Frameworks

- [CIRCLES 方法](CIRCLES-Method.md)
- [DACI 决策框架](DACI-Decision-Framework.md)
- [Lean Canvas](Lean-Canvas.md)
- [OGSM 战略规划](OGSM-Strategic-Planning.md)
- [Shape Up](Shape-Up.md)

---

## Skill Download

**File:** `skills/working-backwards.md` (inferred from pattern)

---

## Skill Content

```markdown
# Working Backwards (Amazon)

Define a product concept by writing the press release and FAQ first, then deriving requirements.

Start with the ideal customer experience by drafting a future press release, then work backward to define what must be built.

## Steps

1. Write a **press release** announcing the finished product (1 page max)
2. Draft **FAQs** -- external (customer questions) and internal (stakeholder questions)
3. Define the **customer experience** by writing user narratives or mockups
4. Identify the **hardest problems** that must be solved to deliver this experience
5. Derive **requirements and milestones** from the press release promises

## Output Format

**Press Release:**
- Headline: [Attention-grabbing title]
- Subheadline: [Target customer + key benefit]
- Problem: [Current pain point]
- Solution: [How the product solves it]
- Quote: [Fictional leader quote]
- Call to Action: [How customers get started]

**Key Requirements:** [Bulleted list derived from PR]
**Open Questions:** [Hardest unsolved problems]
```

---

*Source: [PMFrame.works - Working Backwards](https://pmframe.works/framework-working-backwards)*
