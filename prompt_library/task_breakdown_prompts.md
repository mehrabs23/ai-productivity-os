# Task Breakdown Prompts

## Building a Personal Productivity System with AI — Prompt Library

---

## Prompt 1: Project Identification Prompt

**Purpose:** Given a goal, generate a list of candidate projects that together constitute the work needed to achieve it.

**When to use:** Day 1, Session 3 — when translating goals into projects.

---

```
I have the following goal:

Goal: [PASTE YOUR GOAL + OUTCOME STATEMENT]
Deadline: [DATE]

Please help me identify the projects I need to undertake to achieve this goal.

A project is a bounded piece of work — larger than a single task, smaller than the full goal — that produces a deliverable when complete.

Please:
1. List 3–6 candidate projects that together would move this goal towards completion
2. For each project, write a 1-sentence scope note describing what the project includes and excludes
3. Indicate whether each project is: Critical (must do) / Important (should do) / Optional (nice to have)
4. Note any dependencies between projects (e.g., Project B cannot start until Project A is complete)

My context (current resources, constraints, time available): [DESCRIBE YOUR SITUATION]
```

---

## Prompt 2: Project-to-Tasks Breakdown Prompt

**Purpose:** Given a project, generate a comprehensive list of tasks.

**When to use:** Day 1, Session 4 — when populating your Task Database.

---

```
I have the following project:

Project name: [PROJECT NAME]
Goal it serves: [PARENT GOAL]
Scope: [WHAT THIS PROJECT INCLUDES AND EXCLUDES — 1–2 sentences]
Deadline: [DATE]

Please generate a comprehensive list of tasks needed to complete this project.

For each task:
1. Write a verb-first task name (Draft, Review, Build, Send, Decide, Research, Schedule...)
2. Add a brief description of what "done" looks like for this task (1 sentence)
3. Estimate approximate effort: Small (< 1 hour), Medium (1–3 hours), Large (3+ hours)
4. Note any task that is a blocker — i.e., other tasks cannot start until this one is done

Aim for 8–14 tasks. Avoid tasks that are too large to complete in one work session. If a task would take more than one session, suggest splitting it.
```

---

## Prompt 3: Milestone Generation Prompt

**Purpose:** Break a project into 3–5 meaningful milestones — checkpoints that mark progress.

**When to use:** Day 2, Session 1 — when building your milestone map.

---

```
I have the following project:

Project: [PROJECT NAME]
Scope: [WHAT THIS PROJECT INCLUDES]
Start date: [DATE YOU BEGAN OR WILL BEGIN]
Target completion: [DEADLINE]

Please help me identify 3–5 milestones for this project.

A milestone is a named, verifiable checkpoint — the moment you can say "this phase is done." It is NOT a task (too small) and NOT the full project completion (too large).

For each milestone:
1. Name it as a completed state (e.g., "First draft of all case studies written" not "Write case studies")
2. Describe what must be true for this milestone to be considered complete (1–2 sentences)
3. Suggest a target date based on the project timeline
4. List the 2–3 key tasks that must happen for this milestone to be reached

Note: if any milestone is actually a task, flag it and suggest a better milestone to replace it.
```

---

## Prompt 4: Reverse Planning Prompt

**Purpose:** Starting from a project's end date, work backwards to assign target dates to each milestone.

**When to use:** Day 2, Session 1 — immediately after generating your milestones.

---

```
I have a project with the following milestones. Please help me sequence them using reverse planning — working backwards from the completion date.

Project: [PROJECT NAME]
Completion date: [DATE]

Milestones (in approximate order):
1. [MILESTONE 1 NAME]
2. [MILESTONE 2 NAME]
3. [MILESTONE 3 NAME]
4. [MILESTONE 4 NAME — if applicable]

For each milestone, suggest a realistic target date by working backwards from the completion date. Allow adequate time between milestones for the tasks required.

Also flag:
- Any milestone sequence that looks too compressed (not enough time between steps)
- Any milestone that should actually come before another milestone based on dependencies
- What I should have completed or in progress by [TODAY'S DATE] if I'm to stay on track
- Identify the most critical upcoming milestone — the one that, if missed, would jeopardize the whole timeline

*(Also listed in prioritization_prompts.md Prompt 3)*
```

---

## Prompt 5: Task Splitting Prompt

**Purpose:** Break a task that is too large into 2–3 actionable sub-tasks.

**When to use:** Any time during the course when you identify a task that will take more than one session.

---

```
I have a task that is too large to complete in one work session. Please help me split it.

Task: [TASK NAME AND BRIEF DESCRIPTION]
Project context: [WHICH PROJECT IT BELONGS TO]
Current estimated effort: [HOW LONG YOU THINK IT WILL TAKE]

Please split this task into 2–4 smaller tasks that:
1. Each take no more than 1–2 hours
2. Each have a clear definition of done
3. Can be sequenced (i.e., Task A produces an output that feeds Task B)
4. Are independently completable in a single work session

Use verb-first task names: Draft / Review / Finalise / Test / Send / Build / Decide / Research
```
