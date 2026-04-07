# Wizard of Oz Test (Wizard of Oz 测试)

**Category:** Validation (验证测试)

**Framework ID:** #36

**Source:** https://pmframe.works/framework-wizard-of-oz

---

## Overview

Before technology is implemented, a real person operates behind the scenes playing the system role, letting users believe they are interacting with a real product. Validates at extremely low cost whether users will actually use the feature and how they will use it.

---

## Core Problem Solved

Traditional user interviews ask "would you use this feature if it existed?" But people's responses to hypothetical questions often differ greatly from real behavior — 70% say "will use," only 20% actually do.

---

## Front Stage vs Back Stage

| Layer | Description |
|-------|-------------|
| **Front Stage (User sees)** | A "real, usable" product interface; system "instantly" responds |
| **Back Stage (User doesn't know)** | An operator receives commands via intercom or instant messaging; operator manually selects responses in real-time |

---

## Three Typical Test Setups

| Setup | Description |
|-------|-------------|
| Voice Assistant Testing | User speaks → Operator hears, manually inputs "AI response" → Screen displays as if AI generated |
| AI Recommendation Feature | User browses → Operator sees user behavior, manually selects "recommended content" → Displayed as "AI recommendations" |
| Smart Customer Service Bot | User types question in chat → Operator (real rep) responds in real-time → User believes they're talking to a bot |

---

## Key Success Factors

1. **Confidentiality is crucial** — if users suspect human intervention, results are distorted
2. **Operators need sufficient practice** — ensure response speed and quality
3. **Observe user "abandonment behavior"** — when do they stop trying? This is the most important data
4. **Suitable for validating "will users use it"** — rather than "do users like it"
5. **Post-test debrief interview** — user reactions after learning the truth are also valuable data

---

## Case Study: IBM Speech Recognition Research (1984)

**Setup:** Users believed they were interacting with "IBM's new speech recognition computer"; skilled typists in adjacent room typed "system responses" in real-time

**Key User Behaviors Discovered:**
1. Users naturally used complete grammatical sentences, not keyword commands
2. When system made errors, users instinctively "tried rephrasing" rather than repeating louder
3. Users quickly formed mental models of system "capability boundaries"
4. Frustration spiked sharply when response delay exceeded 3 seconds

**Impact:** These 1984 insights directly influenced IBM ViaVoice interface design 10 years later

---

## Related Frameworks

- [Five User Testing Laws](Usability-Testing-Five-Users.md) (downstream validation)
- [Lean Startup MVP](Lean-Startup-MVP.md) (downstream)
- [Assumption Validation Board](Assumption-Validation-Board.md) (complementary)

---

## Skill Download

**File:** `skills/wizard-of-oz.md`

**Skill Content:**

```markdown
# Wizard of Oz Test

Validate a product concept by manually simulating functionality behind the scenes.

## When to Use

Test whether users want a product by having humans secretly perform the work that technology would eventually do. Use when building the real thing is expensive and you need to validate demand or UX before investing in engineering.

## Steps

1. **Define the interaction** — specify what the user sees and does.
2. **Design the facade** — build a realistic-looking front end (UI, chatbot, form).
3. **Set up the backstage** — define the manual process, assign operators, create scripts/playbooks.
4. **Run the test** — let real users interact while operators fulfill requests manually in real time.
5. **Measure and learn** — track usage, satisfaction, willingness to pay, and time-to-serve.

## Output Format

A test plan describing the facade design, backstage operations playbook, success metrics with targets, test results summary, and a go/no-go recommendation with supporting data.
```

---

*Source: [PMFrame.works - Wizard of Oz](https://pmframe.works/framework-wizard-of-oz)*
