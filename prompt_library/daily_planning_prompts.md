# Daily Planning & Execution Prompts

## Building a Personal Productivity System with AI — Prompt Library

---

### When to Use This Category

Use these prompts every working morning and whenever your plan gets disrupted mid-day. Daily planning prompts are the operational layer of your Life OS — they turn your goal and task structure into a real schedule for today.

The goal of daily planning is not to fill every hour. It's to answer: **"Given everything I know right now, what should I do next — and in what order?"**

### How to Use Any Prompt in This File

1. Open your Notion dashboard **before** opening email, Slack, or social media
2. Check your Overdue view, Due Soon view, and Today view
3. Fill in the prompt with what you see in Notion
4. Use ChatGPT output as a schedule suggestion — edit it to fit your actual situation
5. Commit your top 3 priorities and time blocks to your daily planning toggle

**Recommended ritual:** 10 minutes max. If planning is taking longer than 15 minutes, use the Minimal Day Prompt (Prompt 4.3) instead.

---

## Section 1: Core Daily Planning Prompts

---

### Prompt 4.1 — Morning Planning Prompt

**Purpose:** Generate a structured, realistic daily plan from your current context and priorities.

**When to use:** Every working morning, ideally within the first 20–30 minutes of starting work. Your primary daily planning tool.

---

```
You are my daily planning partner. Help me structure my work day with intention and realism.

Today's date: [DATE]
Day of the week: [MONDAY / TUESDAY / WED / THURS / FRIDAY / SAT / SUN]
Available productive hours today: [X hours — exclude obligations below]
Energy level right now (1 = very low, 5 = peak focus): [1–5]

Fixed constraints today (meetings, obligations, hard stops):
- [TIME: WHAT — e.g., "10am–11am: Team standup", "3pm: School pickup"]
- [TIME: WHAT]
- [TIME: WHAT — add more as needed]

From my Notion dashboard, my top priorities today are:
1. [PRIORITY 1 — task name + why it's the top priority today]
2. [PRIORITY 2 — task name + why]
3. [PRIORITY 3 — task name + why]

One thing I've been avoiding that might need to happen today:
[TASK OR ACTION — be honest. If nothing, write "nothing I'm aware of"]

Please create a realistic time-blocked daily plan that:
1. Assigns my top priorities to specific time slots, working around my fixed constraints
2. Places the most cognitively demanding work in my highest-energy period
3. Groups similar tasks to reduce context-switching where possible
4. Includes at least one buffer block (20–30 min) for unexpected things
5. Does NOT over-schedule — I should have breathing room

Format: a clean time-block schedule. At the end, add:
- One assumption built into this plan that I should verify
- One thing I should NOT attempt today given the above constraints

```

---

### Prompt 4.2 — Energy-Aware Planning Prompt

**Purpose:** An enhanced daily plan that explicitly matches task types to your energy patterns throughout the day.

**When to use:** When you're deciding how to sequence tasks — especially when you know you have both deep-focus work and lighter admin/communication tasks on the same day.

---

```
You are a performance planning coach. I want to build a daily plan that matches my task types to my actual energy pattern.

My typical energy pattern today:
- Morning [TIME–TIME]: [HIGH / MEDIUM / LOW focus capacity] — [Any note, e.g., "best for writing and deep analysis"]
- Mid-morning / Late morning [TIME–TIME]: [HIGH / MEDIUM / LOW]
- Midday [TIME–TIME]: [HIGH / MEDIUM / LOW] — [Any note]
- Afternoon [TIME–TIME]: [HIGH / MEDIUM / LOW]
- Evening [TIME–TIME, if applicable]: [HIGH / MEDIUM / LOW]

Today's date: [DATE]
Available hours after obligations: [X hours]

Fixed constraints and meetings:
[LIST WITH TIMES]

Tasks I need to do today:
[LIST YOUR TASKS WITH ESTIMATED DURATION — e.g., "Draft newsletter intro — 45 min"]

Please create a time-blocked plan that:
1. Places deep, creative, or high-complexity work in my highest-energy periods
2. Places calls, meetings, admin, and email in lower-energy periods
3. Places review tasks and lighter work in transition periods (before or after meetings)
4. Respects my fixed obligations

After the schedule:
- Name the task I should absolutely NOT do during my lowest-energy window
- If I only complete 60% of today's plan, which tasks should survive? (my "minimum viable day")
```

---

### Prompt 4.3 — Minimal Day Planning Prompt

**Purpose:** Create a minimum viable plan for days where time, energy, or focus is limited. Protects the most important thing when everything else is hard.

**When to use:** When you're overwhelmed, exhausted, sick, or having a difficult personal day. Also use when you have only 1–2 hours of real working time available.

---

```
You are a triage planning assistant. I'm having a minimal-capacity day and need a realistic, low-pressure plan that protects the most important thing without setting me up for failure.

I have approximately [X] productive hours available today.

The single most important thing I must move forward today is:
[ONE TASK OR OUTCOME — not a list]

Secondary items (only if the above is genuinely complete and I have time left):
[TASK 2 — optional]
[TASK 3 — optional, lower priority than Task 2]

Things I am explicitly deciding NOT to do today (so I don't feel guilty about them):
[LIST — helps make conscious decisions, not passive failures]

Please give me:
1. A simple time structure for today — just 2–3 blocks, not a detailed minute-by-minute plan
2. A suggested start time and duration for my most important task
3. One sentence framing I can use to define success for today: "Today is a good day if I..."
4. One thing that might make even this minimal plan fail — and what to do if that happens
```

---

## Section 2: Focus and Execution Prompts

---

### Prompt 4.4 — Focus Block Design Prompt

**Purpose:** Identify and design deep focus blocks within a day crowded with meetings — protecting time for your most cognitively demanding work.

**When to use:** On meeting-heavy days. Use the night before or first thing in the morning when you can see your calendar.

---

```
You are a focus architecture specialist. I have a meeting-heavy day and need to carve out protected deep-work time for my most important cognitive task.

Today's meeting and obligation schedule:
[LIST EVERY FIXED COMMITMENT WITH START TIME AND DURATION — e.g., "10am: team call 45 min", "1pm: client review 60 min"]

The deep work task I most need to progress today:
[TASK NAME + WHY IT REQUIRES FOCUSED, UNINTERRUPTED TIME]
Estimated time this task needs: [X hours / X minutes]

My realistic energy pattern today: [BRIEF DESCRIPTION — e.g., "peak 8–10am, low after 3pm"]

Please:
1. Identify the best available focus block(s) in my schedule today — prioritising time before my first meeting
2. Recommend whether to use one larger block or two shorter blocks, and justify why
3. Suggest what to do in the 5 minutes before the block starts to get into deep work mode quickly
4. Identify if there is no viable focus block today — and if so, suggest what to protect tomorrow morning instead
5. Name one thing I should turn off or close during this block to maximise the quality of focus
```

---

### Prompt 4.5 — Deadline-First Scheduling Prompt

**Purpose:** Generate a task schedule for a day where one hard deadline must be met — by working time allocations backwards from the deadline.

**When to use:** When a specific deadline is dominating the day and you need to ensure everything supporting it is sequenced correctly.

---

```
You are a deadline management specialist. I have a hard deadline today and need to build my schedule backwards from it.

Today's date: [DATE]
The hard deadline: [TASK OR DELIVERABLE] must be complete by [TIME/DATE]
What "complete" means for this deadline: [DESCRIBE WHAT DONE LOOKS LIKE — the output, the action, the sent file, etc.]

Tasks I still need to do to hit this deadline:
[LIST THE REMAINING TASKS IN APPROXIMATE SEQUENCE — e.g., "Finish draft", "Review and edit", "Add references", "Format and export", "Send"]

My available working time today: [START TIME – END TIME, minus any obligations]
Obligations that interrupt my working time: [LIST WITH TIMES]

Please:
1. Work backwards from the deadline and assign time slots to each remaining task
2. Flag if the current task list and timeline make the deadline risky — and explain why
3. Identify the single task I must NOT skip or rush if I want a quality output
4. Suggest what to do if I get to [TIME — e.g., 2pm] and the plan has already slipped
```

---

### Prompt 4.6 — Next Physical Action Prompt

**Purpose:** When you're stuck and unable to start a task, identify the single next concrete action — small enough to be undeniable.

**When to use:** Any time you have a task on your list but can't seem to begin it. Excellent for breaking through avoidance and paralysis.

---

```
You are a Getting Things Done specialist. I'm stuck on a task and can't seem to start. Help me identify the single next physical action — concrete enough that there's no reason not to do it right now.

The task I'm stuck on: [TASK NAME AND BRIEF DESCRIPTION]
Why I think I'm not starting: [IF YOU KNOW — avoidance, unclear what to do first, waiting on something, too large, etc. If you don't know, say "I don't know."]
What I've already done on this task (if anything): [DESCRIBE PROGRESS SO FAR, OR "NOTHING YET"]
What I need to have at the end: [THE OUTPUT OR DEFINITION OF DONE]

Please:
1. Define the single next physical action — one concrete step I can take in the next 5–30 minutes. Not "work on X" — something specific like "open Google Doc and write the first line of the introduction" or "send one-paragraph email to [person] asking for [specific information]."
2. If there are multiple possible next actions, show me the 2–3 best starting points and let me choose.
3. If I'm stuck because of a genuine blocker (waiting on someone, missing information), name it clearly and suggest the one action to unblock it.
4. One sentence: "The only way to fail the next action is to..."
```

---

### Prompt 4.7 — Context-Switch Recovery Prompt

**Purpose:** After an unexpected interruption, recalibrate your plan for the remaining hours of the day.

**When to use:** Mid-day, when an unexpected event has disrupted your plan and you need to decide what still happens today vs. what moves to tomorrow.

---

```
You are a day-recovery specialist. My planned flow has been disrupted and I need to recalibrate realistically — not optimistically.

Time now: [CURRENT TIME]
Hours remaining in my work day: [X hours]

What disrupted the plan:
[DESCRIBE — e.g., "urgent client call ran 2 hours longer than expected", "had to handle a personal situation", "got pulled into an unplanned meeting"]

What I had planned to do today (that I haven't done yet):
[LIST YOUR REMAINING PLANNED TASKS]

What is still genuinely non-negotiable today:
[HARD DEADLINE ITEMS OR EXTERNAL DEPENDENCIES — if none, write "none"]

Please give me:
1. A revised plan for the remaining [X] hours — realistic, not heroic
2. A clear statement of what I'm consciously moving to tomorrow (so I'm choosing, not failing)
3. One sentence: "Given what happened today, a realistic and honest finishing state for today is..."
4. One flag: if there's a risk that something in my "tomorrow" list will create a problem if left until tomorrow — tell me now
```

---

---

*Next file: [`review_prompts.md`](review_prompts.md)*
