# Prioritization Prompts

## Building a Personal Productivity System with AI — Prompt Library

---

## Prompt 1: Task Prioritization Prompt

**Purpose:** Apply priority tiers to a full task list using structured reasoning.

**When to use:** Day 2, Session 2 — when prioritizing your task list for the first time, or at the start of each week.

---

```
I need help prioritizing my task list. Below is my current list of tasks.

[PASTE YOUR FULL TASK LIST — one task per line]

My context:
- Top 2 active projects: [PROJECT 1], [PROJECT 2]
- Deadlines this week: [LIST ANY HARD DEADLINES]
- Commitments already blocking my time: [MEETINGS, CALLS, OBLIGATIONS]
- One task I've been avoiding: [TASK YOU KEEP DEFERRING]

Please categorise each task using these priority tiers:

P1 — Critical: Must be done today. Blocking others or zero-slack deadline.
P2 — High: Must be done this week. Significant consequence if delayed.
P3 — Medium: Important but not urgent. Can be done this week or next.
P4 — Low: Low consequence if deferred. Do when time permits.

For each task:
1. Assign the tier
2. Write 1 sentence explaining the reasoning

Important: P1 should have no more than 2 tasks. If your output shows 3+ P1 tasks, flag this explicitly and suggest which one to demote.
```

---

## Prompt 2: Overload Triage Prompt

**Purpose:** When you have more tasks than you can realistically complete this week, make explicit decisions about what to do, schedule, delegate, or drop.

**When to use:** Day 2, Session 2 or Day 4, Session 2 — any time your task list feels overwhelming.

---

```
My task list for this week has more items than I can realistically complete. Help me triage it.

My task list:
[LIST ALL TASKS WITH DUE DATES IF APPLICABLE]

My available productive hours this week: [X hours]
My top goals that must progress this week: [GOAL 1, GOAL 2]

For each task, classify it as:
- Do Now: Must happen this week, non-negotiable
- Schedule: Important but can be moved to a specific future date (suggest a date)
- Delegate: Could be done by someone else — note who
- Drop: Low consequence to remove from the list entirely — note the reason

After the triage table, provide:
1. A summary of how many hours the "Do Now" tasks total (vs. my available hours)
2. A flag if the "Do Now" list still exceeds my available hours
3. One question that would help me make the hardest deferral decision
```

---

## Prompt 3: Reverse Planning Prompt

**Purpose:** Sequence project milestones by working backwards from an end goal or deadline.

*(Also listed in task_breakdown_prompts.md)*

**When to use:** Day 2, Session 1 — immediately after generating milestones.

---

```
I have a project with the following milestones. Please help me sequence them using reverse planning — working backwards from the completion date.

Project: [PROJECT NAME]
Completion date: [DATE]

Milestones:
1. [MILESTONE 1]
2. [MILESTONE 2]
3. [MILESTONE 3]
4. [MILESTONE 4 — if applicable]

Please:
1. Assign a realistic target date to each milestone, working backwards from the completion date
2. Flag any milestone sequence that looks too compressed
3. Tell me what I should have completed by [TODAY'S DATE] to stay on track
4. Identify the most critical upcoming milestone — the one that, if missed, would jeopardize the whole timeline
```

---

## Prompt 4: Attention Budget Analysis Prompt

**Purpose:** Compare your ideal attention allocation to your actual allocation and identify the largest gaps.

**When to use:** Day 2, Session 4 — after completing your Work Session Log for 3+ days.

---

```
Please help me analyse my attention budget — the allocation of my focused work time across different areas of my life.

My ideal attention allocation (what I want to prioritise):
[DOMAIN 1]: [%]
[DOMAIN 2]: [%]
[DOMAIN 3]: [%]
[DOMAIN 4]: [%]
[Other]: [%]
Total: 100%

My actual allocation based on my work session log for the past [X] days:
[DOMAIN 1]: [%]
[DOMAIN 2]: [%]
[DOMAIN 3]: [%]
[DOMAIN 4]: [%]
[Other]: [%]
Total: 100%

Notes on why gaps exist: [ANY CONTEXT — e.g., "I had an unexpected client project," "Admin is harder to avoid because of team meetings"]

Please:
1. Identify the 2–3 largest gaps between ideal and actual
2. For each gap, suggest one practical adjustment I could make to close it
3. Identify any domain that is getting more time than I listed as ideal — and suggest whether this warrants updating my ideal, or reducing the actual
4. Ask me one question that would help me understand why the largest gap persists
```

---

## Prompt 5: Priority Conflict Resolution Prompt

**Purpose:** When two high-priority tasks or projects compete for the same time slot, use structured reasoning to decide which to do first.

**When to use:** Any day — when you're stuck between two things that both feel genuinely urgent.

---

```
I am stuck between two competing priorities and need help deciding which to do first.

Option A: [TASK/PROJECT NAME]
- Deadline: [DATE]
- What happens if delayed by 1 day: [CONSEQUENCE]
- What happens if delayed by 1 week: [CONSEQUENCE]
- Is anyone else blocked by this? [YES/NO — if yes, who?]

Option B: [TASK/PROJECT NAME]
- Deadline: [DATE]
- What happens if delayed by 1 day: [CONSEQUENCE]
- What happens if delayed by 1 week: [CONSEQUENCE]
- Is anyone else blocked by this? [YES/NO — if yes, who?]

Please evaluate both options against these criteria:
1. Consequence severity (what happens if delayed)
2. Reversibility (can the delay be recovered from?)
3. External dependencies (is anyone waiting on this?)
4. Time required (which has a shorter time to completion?)

Give me a clear recommendation with reasoning — not a both/and answer. I need to do one first.
```
