# Prioritization & Workload Management Prompts

## Building a Personal Productivity System with AI — Prompt Library

---

### When to Use This Category

Use these prompts when you need to make hard choices: which tasks to do this week, which projects to invest in, what to defer, and how to balance competing demands on your time and attention.

Prioritization prompts help answer:
- "I have 30 tasks — which 5 matter most?"
- "I'm overloaded — what gets cut?"
- "I spent all week firefighting — what changed about my actual attention?"
- "I have two urgent things and can only do one — which one?"

### How to Use Any Prompt in This File

1. Fill in all `[SQUARE BRACKETS]` with your real context — the more honest, the more useful
2. Submit to ChatGPT
3. Prioritization outputs are recommendations, not rules. Review every recommendation against what you actually know.
4. Enter final priority decisions into your Notion Task Database

---

## Section 1: Task and Project Prioritization

---

### Prompt 3.1 — Task Prioritization Prompt

**Purpose:** Apply priority tiers to a full task list using structured, context-aware reasoning — not just urgency alone.

**When to use:** Day 2, Session 2 — when prioritizing your task list for the first time. Repeat at the start of each week.

---

```
You are a workload management specialist. I need help prioritizing my task list using a structured framework.

My current task list:
[PASTE YOUR FULL TASK LIST — one task per line. Include a rough due date or deadline if known.]

My context:
- My top 2 active projects: [PROJECT 1], [PROJECT 2]
- Hard deadlines this week: [LIST ANY NON-NEGOTIABLE DEADLINES]
- Fixed commitments already taking my time: [MEETINGS, CALLS, OBLIGATIONS with hours]
- One task I've been avoiding: [THE TASK YOU KEEP DEFERRING — be honest]
- My available productive hours this week (excluding obligations): [X hours]

Please categorise each task using these priority tiers:

P1 — Critical: Must be done today or tomorrow. Blocking others, or deadline = today/tomorrow.
P2 — High: Must be done this week. Significant consequence if delayed beyond 7 days.
P3 — Medium: Important but not urgent. Can slip 1–2 weeks without serious harm.
P4 — Low: Low consequence if deferred indefinitely. Do only when high-priority work is clear.

For each task:
1. Assign the tier
2. Write 1 sentence explaining the reasoning — especially if it's P1 or borderline P2/P3

Rules:
- P1 must have no more than 2–3 tasks. If your output shows 4+ P1 tasks, explicitly flag this and suggest which to demote and why.
- The avoided task must be assessed honestly, not automatically demoted.
```

---

### Prompt 3.2 — Impact vs. Effort Matrix Prompt

**Purpose:** Sort a list of tasks or projects into a 2×2 impact/effort grid — to identify quick wins, strategic bets, time sinks, and things to eliminate.

**When to use:** When kicking off a new week or quarter, or when you feel like you're working hard but not making meaningful progress. Also useful for project selection.

---

```
You are a strategic prioritization consultant. I want to map a list of tasks or projects onto an impact/effort matrix to make better resource decisions.

My list (tasks or projects):
[PASTE YOUR LIST — one item per line]

My context:
- What "high impact" means in my situation: [e.g., "progresses my main income goal", "reduces my biggest risk", "moves my most important goal forward by a meaningful amount"]
- My available time this week: [X hours]

Please place each item in one of 4 quadrants:
- Quick Wins (High Impact / Low Effort): Do these first — maximum return per hour
- Strategic Bets (High Impact / High Effort): Schedule focused time for these — they matter but require investment
- Time Sinks (Low Impact / High Effort): Challenge whether to do these at all; consider dropping or delegating
- Fill-In Work (Low Impact / Low Effort): Do only when there's no better use of time

After the matrix:
1. Identify my top 2 Quick Wins I should start with
2. Identify any item that is a Time Sink I should honestly consider removing from my list
3. Flag any Strategic Bet that I keep deferring — these are often the highest leverage and the most avoided
```

---

### Prompt 3.3 — Project Portfolio Ranking Prompt

**Purpose:** Given multiple active projects, decide which to invest in most heavily this week or this month.

**When to use:** When you have 3+ active projects and can't give all of them meaningful progress. Helps with conscious investment decisions at the project level.

---

```
You are a strategic portfolio advisor. I have multiple active projects and limited time. Help me decide how to allocate my attention across them.

My active projects:

Project 1: [NAME]
- Goal it serves: [PARENT GOAL]
- Current status: [ON TRACK / AT RISK / STALLED]
- Deadline: [DATE]
- Hours invested so far this week: [X]

Project 2: [NAME]
- Goal it serves: [PARENT GOAL]
- Current status: [ON TRACK / AT RISK / STALLED]
- Deadline: [DATE]
- Hours invested so far this week: [X]

Project 3: [NAME]
- Goal it serves: [PARENT GOAL]
- Current status: [ON TRACK / AT RISK / STALLED]
- Deadline: [DATE]
- Hours invested so far this week: [X]

(Add more projects as needed)

My available hours for project work this week: [X hours total]

Please:
1. Rank the projects by investment priority for this week — not which is most important ever, but which most needs focused hours RIGHT NOW
2. Suggest a rough hour allocation across projects for the week
3. Flag any project that is at risk of being neglected in a way that would be hard to recover from
4. Identify if any project should be explicitly paused or moved to "Planned" status to protect focus
```

---

## Section 2: Overload and Triage

---

### Prompt 3.4 — Overload Triage Prompt

**Purpose:** When you have more tasks than you can realistically complete this week, make explicit decisions about what to do, schedule, delegate, or drop.

**When to use:** Any time your task list feels overwhelming and paralysing. Also use at the start of any week where you can already see you've over-committed.

---

```
You are a workload triage specialist. I have more tasks than I can realistically complete this week and need help making explicit decisions.

My full task list for this week:
[LIST ALL TASKS WITH DUE DATES IF APPLICABLE — be exhaustive]

My constraints:
- Available productive hours this week: [X hours — honest estimate, after all obligations]
- Top goals that must progress this week: [GOAL 1, GOAL 2 — no more than 2]
- Anyone who is waiting on me for something: [IF APPLICABLE]

For each task, classify it as:
- Do Now: Must happen this week — non-negotiable (external deadline, someone is waiting, blocks something critical)
- Schedule: Important but can be moved — suggest a specific future date
- Delegate: Could be done by someone else — note who and whether I need to hand it off
- Drop: Low consequence to remove entirely — note the reason briefly

After the triage table:
1. Sum the estimated hours for "Do Now" tasks and compare to my available hours — flag if still over-committed
2. Identify the most painful deferral decision (the one hardest to accept) and explain clearly why it's the right call given the constraints
3. Ask me one question that would help me make the hardest remaining choice
```

---

### Prompt 3.5 — Low-Value Work Identifier Prompt

**Purpose:** Find tasks and activities in your current system that are consuming time without meaningfully serving your goals — and make a case for reducing or eliminating them.

**When to use:** During a weekly review or monthly retrospective, when something feels busy but not productive. Also good as a first step before accepting any new commitment.

---

```
You are a strategic efficiency advisor. I want to identify tasks and activities in my current work that have low impact relative to the time they consume.

My current regular activities and tasks (things I do weekly or frequently):
[LIST YOUR REGULAR ACTIVITIES — meetings, recurring tasks, daily habits, obligations, even things you "should" do]

My top goals: [LIST YOUR 2–3 MAIN ACTIVE GOALS]
What "high impact" means in my situation: [IN 1–2 SENTENCES]

For each activity or task:
1. Rate impact on my top goals: High / Medium / Low / None
2. Estimate time cost per week: [hours]
3. Flag as: Keep / Reduce / Eliminate / Delegate

Then:
4. Identify the one activity consuming the most time relative to the impact it produces
5. For each "Eliminate" recommendation, suggest what I should say or do to actually remove it — be practical
6. Identify any activity where the required effort could be cut by 50% without meaningfully reducing the impact (do less of it, not none of it)
```

---

## Section 3: Attention and Time Allocation

---

### Prompt 3.6 — Attention Budget Analysis Prompt

**Purpose:** Compare your intended focus allocation to your actual allocation and identify the largest gaps.

**When to use:** Day 2, Session 4 — after completing your Work Session Log for 3+ days. Repeat weekly.

---

```
You are an attention and focus strategist. Help me analyse the gap between where I intend to spend my focus and where it's actually going.

My ideal attention allocation (what I want to prioritise — totals 100%):
[DOMAIN 1]: [%]
[DOMAIN 2]: [%]
[DOMAIN 3]: [%]
[DOMAIN 4]: [%]
[Other]: [%]
Total: 100%

My actual allocation based on my Work Session Log for the past [X] days:
[DOMAIN 1]: [%]
[DOMAIN 2]: [%]
[DOMAIN 3]: [%]
[DOMAIN 4]: [%]
[Other]: [%]
Total: 100%

Context on why gaps exist: [ANY EXPLANATION — e.g., "unexpected client escalation", "admin is hard to avoid with team meetings", "creative work keeps getting pushed until evening when I'm tired"]

Please:
1. Identify the 2–3 largest gaps between ideal and actual
2. For each gap, suggest one structural change that would meaningfully close it (not just "do more of X")
3. Identify any domain receiving more time than my ideal — and suggest whether this warrants updating the ideal, or actively reducing the actual — and how
4. Ask me one question that would help me understand why the largest single gap persists week after week
```

---

### Prompt 3.7 — Priority Conflict Resolution Prompt

**Purpose:** When two high-priority tasks or projects compete for the same time slot, use structured reasoning to decide which to do first.

**When to use:** Any day — when you're stuck between two things that both feel genuinely urgent. Most useful when emotional weight is making the decision harder than it rationally needs to be.

---

```
You are a decision analyst. I'm stuck between two competing priorities and need structured reasoning to pick one. Do not give me a "do both" answer — I need to choose one to do first.

Option A: [TASK OR PROJECT NAME]
- Deadline: [DATE]
- What happens if delayed by 1 day: [CONSEQUENCE]
- What happens if delayed by 1 week: [CONSEQUENCE]
- Is anyone else blocked by this? [YES/NO — if yes, who and how seriously?]
- Effort to complete: [HOURS]

Option B: [TASK OR PROJECT NAME]
- Deadline: [DATE]
- What happens if delayed by 1 day: [CONSEQUENCE]
- What happens if delayed by 1 week: [CONSEQUENCE]
- Is anyone else blocked by this? [YES/NO — if yes, who and how seriously?]
- Effort to complete: [HOURS]

Please evaluate both options against:
1. Consequence severity: What is the worst realistic outcome of delaying each?
2. Reversibility: If delayed, how recoverable is the situation?
3. External dependencies: Is anyone else waiting? Is the cost to them significant?
4. Time to completion: If I start now, which could I finish faster and restore focus?

Output: A clear recommendation — do A first or do B first — with concise reasoning. Then, one sentence on what to do with the lower-priority item to make sure it doesn't fall through.
```

---

### Prompt 3.8 — Weekly Reset Prompt

**Purpose:** After a messy, derailed, or unproductive week, rebuild a clean and realistic plan for the coming week.

**When to use:** At the end of a bad week or the start of a recovery week. Also useful during a Monday planning session when you're feeling behind and overwhelmed.

---

```
You are a recovery-planning specialist. I've had a difficult week and need help resetting — not motivational advice, but a structured way to recover and build a realistic plan for the week ahead.

What happened last week (be honest):
- What I planned to do: [LIST YOUR INTENDED PRIORITIES]
- What I actually got done: [LIST HONESTLY]
- Why the week went off track: [THE REAL REASON — if known]
- What's now behind or overdue: [LIST]

This week's non-negotiables:
- Hard deadlines I cannot miss: [LIST WITH DATES]
- Key commitments already taking time: [MEETINGS, OBLIGATIONS]
- Available productive hours this week: [X hours — realistic]

Please give me:
1. An honest assessment of last week: what was the real output, without judgment?
2. A triage decision for everything that's overdue: Do Now / Schedule / Drop / Acknowledge but deprioritise
3. A realistic plan for this week: which 3–5 things would make it a genuinely good week, given the constraints?
4. One structural suggestion that might prevent the same kind of derailment this week
5. A clear "minimum viable week" — if everything else goes wrong again, what are the 1–2 things that absolutely must happen?
```

---

## Section 4: Persona Variants

---

### Prompt 3.9 — Prioritization for Freelancers

**When to use:** Use Prompt 3.1 above with this additional context block.

---

```
[Use Prompt 3.1: "Task Prioritization Prompt". Add this freelancer-specific context:]

Additional freelancer context:
- My current active clients: [CLIENT NAMES OR TYPES with rough hourly commitment each]
- Tasks that are billable vs. non-billable: [INDICATE FOR EACH TASK IF POSSIBLE]
- What non-client work I keep deferring: [OFTEN: own marketing, portfolio, skill-building]
- My income risk this week if client work slips: [LOW / MEDIUM / HIGH]

When prioritizing, please distinguish clearly between:
- Revenue-critical tasks (client work with deadlines)
- Business-building tasks (non-billable but strategic)
- Admin tasks (necessary but not leverage-building)

Suggest a split: what % of my week should go to each category given my current situation?
```

---

*Next file: [`daily_planning_prompts.md`](daily_planning_prompts.md)*
