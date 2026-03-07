# System Optimization Prompts

## Building a Personal Productivity System with AI — Prompt Library

---

## Prompt 1: System Retrospective Prompt

**Purpose:** Analyse your productivity system's health — identify what's working, what's abandoned, and what one change would have the highest impact.

**When to use:** Day 4, Session 3 — and every 4 weeks thereafter as a maintenance ritual.

---

```
I'm doing a system retrospective on my personal productivity operating system. Please help me analyse it.

System components and usage (mark as: Using regularly / Sometimes / Not using):
- Goals Database: [STATUS]
- Projects Database: [STATUS]
- Task Database: [STATUS]
- Milestone Map: [STATUS]
- Anti-To-Do Log: [STATUS]
- Work Session Log: [STATUS]
- Attention Budget: [STATUS]
- Kanban Board: [STATUS]
- Master Dashboard: [STATUS]
- Streak Tracker: [STATUS]
- Daily Planning Routine: [STATUS]
- Weekly Review: [STATUS]

Rituals I'm maintaining consistently: [LIST]
Rituals I've dropped or am struggling with: [LIST]
My weakest link (the part most likely to degrade the whole system if ignored): [COMPONENT]

Time since system was last modified or improved: [DURATION]

Please:
1. Identify the 2–3 components that are underused and suggest whether each should be: kept and simplified / actively maintained / removed
2. Identify the single highest-leverage change that would improve my system's reliability
3. Flag any component that is likely causing friction rather than reducing it
4. Ask me one question that would help me make the most important decision about this system
```

---

## Prompt 2: Dashboard UX Audit Prompt

**Purpose:** Get structured feedback on your Notion dashboard's usability by describing its layout to ChatGPT.

**When to use:** Day 3, Session 4 — and any time you feel your dashboard needs a redesign.

---

```
I want to audit the usability of my personal productivity dashboard in Notion.

My dashboard layout:
[DESCRIBE YOUR DASHBOARD — list the sections from top to bottom, what database each section links to, and what filter/sort is applied]

Example format:
Section 1: "Today's Focus" — Task database, filtered by Due Date = today OR Priority = Critical
Section 2: "Active Projects" — Projects database, filtered by Status = Active
Section 3: "This Week" — Task database, filtered by Due ≤ 7 days, sorted by Priority

My sections:
[PASTE YOUR LAYOUT DESCRIPTION]

Current limitations or frustrations:
[DESCRIBE ANYTHING THAT FEELS SLOW, CONFUSING, OR NOISY]

Please evaluate my dashboard against these UX principles:
1. Load test: Can the most important information be found within 5 seconds?
2. Signal-to-noise ratio: Are there sections I'm likely to ignore?
3. Click efficiency: Can a specific task be opened in ≤ 3 clicks?
4. Label clarity: Are section names self-explanatory?

Please give me:
1. Your assessment of each section (keep / simplify / remove + reason)
2. Two specific changes that would most improve usability
3. One section you'd consider adding based on my system's apparent goals
```

---

## Prompt 3: Kanban Design Prompt

**Purpose:** Get suggestions for workflow stages that match your specific type of work.

**When to use:** Day 3, Session 1 — when designing your Kanban stages.

---

```
I'm designing a personal Kanban board and want workflow stages that match my actual work.

My work type: [DESCRIBE — e.g., "freelance UX designer with multiple clients", "student managing coursework and a side project", "team lead with meetings, strategic work, and personal projects"]

Current default stages I'm working from:
Backlog → This Week → In Progress → Blocked → Done

What doesn't fit well with the defaults above:
[DESCRIBE ANY STAGES THAT DON'T MATCH HOW YOUR WORK ACTUALLY FLOWS — e.g., "I have a review stage", "waiting for feedback is different from blocked", "I have a recurring admin queue"]

Please suggest:
1. A customised set of 4–6 stages for my Kanban, with a 1-sentence description of what goes in each stage
2. Any stage pairs that should be distinguished (e.g., "Blocked: External" vs. "Blocked: Internal")
3. How to decide when a task should move between stages — give me a clear decision rule for at least 3 transitions
```

---

## Prompt 4: Habit Design Prompt

**Purpose:** Identify the best 2–3 daily habits to track on your Streak Tracker, based on your goals.

**When to use:** Day 3, Session 3 — when setting up your Streak Tracker.

---

```
I want to set up a Streak Tracker to maintain daily consistency on 2–3 habits.

My current goals:
[LIST YOUR TOP 3 GOALS BRIEFLY]

My current system rituals:
[LIST WHAT YOU ALREADY DO — e.g., morning planning, daily check-in, session logging]

The rituals I want to be more consistent about:
[DESCRIBE — e.g., "I always skip the weekly review", "I start my day reactively instead of with planning"]

For my Streak Tracker, please suggest:
1. The 2–3 habits that would have the highest leverage on my goals (process habits only — not outcome targets)
2. A simple yes/no completion criterion for each habit (what does "done" look like?)
3. The minimum viable version of each habit for a difficult day (so I can maintain the streak even on hard days)
4. The one habit that, if I only tracked one thing, would be the most important

Remember: track processes, not outcomes. "Did I complete my morning planning?" rather than "Did I work 4 hours on Project X?"
```

---

## Prompt 5: System Improvement Idea Generation Prompt

**Purpose:** Generate a list of potential improvements for your productivity system — useful when you know something isn't working but aren't sure what to change.

**When to use:** During retrospectives, or any time your system feels stale.

---

```
I want to generate ideas for improving my productivity system.

Current system description:
[BRIEFLY DESCRIBE YOUR SYSTEM — which components you have, how you use them, which rituals you follow]

The symptoms I'm experiencing (even if I can't diagnose the cause):
[E.g., "I feel scattered in the morning", "I keep missing important tasks", "My dashboard has too much and I never open it", "I'm technically maintaining the system but it doesn't feel like it's helping"]

Constraints:
- I do not want to add complexity — simpler is better
- I'd prefer to modify what I have rather than add new tools
- Any change should take less than 30 minutes to implement

Please generate 5 specific, actionable improvement ideas. For each:
1. Name the intervention (what to do)
2. Describe precisely how to implement it in 2–3 steps
3. Describe what problem it solves
4. Rate it: Quick win (can implement today) / Medium effort (1–2 hours) / Major redesign
```
