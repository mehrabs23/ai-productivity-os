# Project Breakdown & Task Creation Prompts

## Building a Personal Productivity System with AI — Prompt Library

---

### When to Use This Category

Use these prompts when translating goals into actionable work — specifically when you need to move from an abstract intention ("I want to launch a course") into concrete, database-ready tasks.

This category covers:
- Breaking goals → projects → milestones → tasks → subtasks
- Converting messy thinking into structured, Notion-ready entries
- Estimating effort and identifying blockers before they slow you down

### How to Use Any Prompt in This File

1. Fill in all `[SQUARE BRACKETS]` with your real context
2. Submit to ChatGPT
3. **Review and edit the output** — pay special attention to task effort estimates and blockers
4. Paste the structured output directly into your Notion Project or Task database

---

## Section 1: Brain Dump and Capture

---

### Prompt 2.1 — Brain Dump → Structured System Prompt

**Purpose:** Take a messy list of thoughts, tasks, ideas, and worries and convert it into a structured set of goals, projects, tasks, and priorities — ready to enter into Notion.

**When to use:** When you're feeling overwhelmed, scattered, or have a messy list of "things to do" with no clear structure. Also excellent as the very first prompt before starting Day 1.

---

```
You are an expert productivity system architect. I'm going to give you a brain dump — an unfiltered list of everything on my mind right now (tasks, worries, ideas, commitments, projects, and goals all mixed together).

Your job is to sort, classify, and structure this into a clean, actionable system I can immediately enter into my Notion workspace.

My brain dump:
[PASTE YOUR UNFILTERED LIST HERE — everything, in any order, in any format. Include the messy stuff.]

My context:
- My role / situation: [e.g., "freelance writer", "final-year student", "working parent with a side project"]
- Life areas I manage: [e.g., Work / Studies / Personal / Health / Content / Admin / Finance]
- My most important commitment right now: [THE THING THAT CANNOT SLIP]

Please process this into 4 clear sections:

**Section 1: Goals identified**
— Any items that represent a larger desired outcome (not a specific task). List as: Goal name → Rough success condition.

**Section 2: Projects identified**
— Bounded pieces of work with a deliverable. For each: Project name → Parent goal (if visible) → Estimated size (Small/Medium/Large).

**Section 3: Tasks identified**
— Specific atomic actions. For each: Task name (verb-first) → Parent project → Effort (S/M/L) → Priority (P1–P4).

**Section 4: Parking lot**
— Items that don't clearly fit into a task, project, or goal right now. Keep them named so I can decide on them consciously.

At the end: identify the single most important first action I should take tomorrow morning.
```

**Customisation notes:** This prompt gets dramatically better the longer and messier your brain dump is. Don't clean it up before pasting. The AI is good at finding structure in chaos.

---

## Section 2: Goal → Project → Task Hierarchy

---

### Prompt 2.2 — Goal → Projects Breakdown Prompt

**Purpose:** Given a well-defined goal, generate the candidate projects needed to achieve it.

**When to use:** Day 1, Session 3 — after defining your goals, to populate your Projects Database.

---

```
You are a project planning consultant. I need to identify the projects that form the work structure for this goal.

Goal: [PASTE YOUR GOAL AND OUTCOME STATEMENT]
Deadline: [DATE]
My context and constraints: [RESOURCES, TIME AVAILABLE, KEY CONSTRAINTS]

A project is a bounded piece of work — larger than a single task, smaller than the full goal — that produces a deliverable when complete.

Please:
1. List 3–6 candidate projects that together would achieve this goal
2. For each project:
   - Write a 1-sentence scope note: what it includes and what it explicitly excludes
   - Classify as: Critical (must do) / Important (should do) / Optional (nice to have)
   - Estimate size: Small (< 1 week) / Medium (1–4 weeks) / Large (1+ month)
3. Identify any dependencies: which projects cannot start until another is complete?
4. Flag any project that looks like a single task (too small to be a project) or the goal itself (too large)

My goal has these life areas: [WORK / PERSONAL / STUDY / CONTENT / HEALTH / ETC.]
```

---

### Prompt 2.3 — Project → Tasks Breakdown Prompt

**Purpose:** Given a project, generate a comprehensive, verb-first task list ready for Notion.

**When to use:** Day 1, Session 4 — when populating your Task Database for the first time.

---

```
You are a project analyst. I need a complete, implementation-ready task list for this project.

Project name: [PROJECT NAME]
Goal it serves: [PARENT GOAL]
Scope (what's in and out): [1–2 sentences]
Deadline: [DATE]
My role: [AM I DOING THIS ALONE OR WITH OTHERS? IF OTHERS, BRIEFLY WHO?]

Please generate a comprehensive task list. For each task:
1. Write a verb-first task name: Draft / Review / Build / Send / Decide / Research / Schedule / Finalise / Test...
2. Write a 1-sentence "definition of done" — what does complete look like for this specific task?
3. Estimate effort: Small (< 1 hour) / Medium (1–3 hours) / Large (3+ hours)
4. Flag if it is a blocker — other tasks cannot start until this one is done
5. Suggest a priority: P1 / P2 / P3 / P4

Target: 8–14 tasks. If any task would take more than 3 hours, split it. Tasks should be completable in a single work session.

After the task list:
- Identify the single task that would most unblock the rest of the project
- Flag any task where I'm likely to underestimate the effort required
```

---

### Prompt 2.4 — Milestone Generation Prompt

**Purpose:** Break a project into 3–5 meaningful checkpoints — named in past tense as completed states.

**When to use:** Day 2, Session 1 — when building your milestone map for bigger projects.

---

```
You are a project milestone architect. I need to break this project into meaningful, verifiable checkpoints.

Project: [PROJECT NAME]
Scope: [WHAT THIS PROJECT INCLUDES]
Start date: [DATE YOU BEGAN OR WILL BEGIN]
Target completion: [DEADLINE]

A milestone is a named, verifiable checkpoint — the moment you can say "this phase is done." It is NOT a task (too small) and NOT the full project (too large).

Please identify 3–5 milestones. For each:
1. Name it as a completed state, past tense: "Research phase complete" not "Do research"
2. Describe what must be true for this milestone to be verified as complete (1–2 sentences)
3. Suggest a realistic target date given the project timeline
4. List the 2–3 key tasks that must happen to reach this milestone
5. Name the output or deliverable this milestone produces (a document, a decision, a working prototype, etc.)

After the milestones:
- Flag any milestone that is actually a task (too small)
- Identify which milestone, if missed, would most seriously jeopardise the project
```

---

### Prompt 2.5 — Reverse Planning Prompt

**Purpose:** Starting from a project's end date, work backwards to assign realistic dates to each milestone.

**When to use:** Day 2, Session 1 — immediately after generating milestones for a project with a real deadline.

---

```
You are a project scheduling specialist. I need to sequence my milestones using reverse planning — working backwards from the completion date to ensure I'm on track.

Project: [PROJECT NAME]
Final completion deadline: [DATE — non-negotiable]
Today's date: [DATE]

Milestones (in approximate forward order):
1. [MILESTONE 1 NAME]
2. [MILESTONE 2 NAME]
3. [MILESTONE 3 NAME]
4. [MILESTONE 4 NAME — if applicable]
5. [MILESTONE 5 NAME — if applicable]

Please:
1. Assign a realistic target date to each milestone, working backwards from the final deadline. Allow appropriate time between milestones for the tasks required.
2. Flag any milestone pair where the gap looks dangerously short — where even minor delay would cascade.
3. State clearly what I should have completed or in-progress by TODAY to be on track.
4. Identify the most critical upcoming milestone — the one where a miss is hardest to recover from.
5. Recommend a "early warning date" — a date by which, if Milestone 2 isn't done, I should immediately renegotiate the deadline or reduce scope.
```

---

## Section 3: Task-Level Precision

---

### Prompt 2.6 — Task Splitting Prompt

**Purpose:** Break a large task (3+ hours) into 2–4 smaller, session-ready sub-tasks.

**When to use:** Whenever you add a task to Notion and realize it's too large to complete in one sitting. Also use during the weekly planning session when tasks seem to keep rolling over.

---

```
You are a task decomposition specialist. I have a task that is too large to complete in a single work session. Help me break it into smaller, sequentially completable sub-tasks.

Task: [TASK NAME AND BRIEF DESCRIPTION]
Project context: [WHICH PROJECT / GOAL IT BELONGS TO]
Current estimated effort: [HOW LONG YOU THINK IT WILL TAKE IN TOTAL]
Why it keeps not getting done: [OPTIONAL — if you know, this helps]

Please split this into 2–4 smaller tasks that:
1. Each take no more than 1–2 hours
2. Each have a clear, observable definition of done
3. Are sequenced — Task A produces output that feeds Task B
4. Can be done independently in a single focused session

Use verb-first names: Draft / Review / Finalise / Test / Send / Build / Decide / Research / Summarise

Also: identify which sub-task is the hardest to start — this is likely the one worth scheduling first.
```

---

### Prompt 2.7 — Effort Estimation Prompt

**Purpose:** Generate honest effort estimates for a set of tasks, including risk adjustments for underestimation.

**When to use:** When you have a task list but aren't sure if your estimates are realistic — especially before planning a week or committing to a deadline.

---

```
You are an experienced project estimator. I need realistic effort estimates for a list of tasks. I tend to underestimate, so please be honest about complexity and add buffer where needed.

Project: [PROJECT NAME]
My proficiency in this domain: [EXPERT / COMPETENT / LEARNING / BEGINNER]
Any external dependencies that could add delay: [E.g., "waiting on feedback", "need a tool I haven't used before"]

Tasks to estimate (paste your list):
[LIST TASKS — one per line, with any brief description that clarifies what is involved]

For each task:
1. Estimate effort in hours: Best case (everything goes smoothly) / Realistic case / Worst case
2. Flag any task where I'm likely to underestimate — and explain why
3. Rate confidence in my estimate: High / Medium / Low
4. Note if this task typically "expands" as you get into it (scope creep risk)

After the table:
5. Sum the realistic estimates and tell me: can this reasonably be done in [MY AVAILABLE HOURS PER WEEK = X hours/week] given [DEADLINE DATE]?
6. Identify the one task most likely to blow my timeline if I underestimated it.
```

---

### Prompt 2.8 — Notion-Ready Task Table Prompt

**Purpose:** Generate task output in a structured table format ready to paste into Notion as a CSV or markdown table.

**When to use:** When you have a completed verbal description of a project and want to generate a Notion-ready task list in one step — without having to manually reformat AI output.

---

```
You are a Notion workspace assistant. I need you to generate a task list in a structured markdown table format that I can paste directly into Notion or a CSV import.

Project: [PROJECT NAME]
Goal it serves: [PARENT GOAL]
Deadline: [DATE]
My life area for this project: [WORK / PERSONAL / STUDY / CONTENT / HEALTH / ADMIN]
Brief description of what needs to happen: [DESCRIBE THE PROJECT OR DELIVERABLE IN 2–4 SENTENCES]

Please generate a Notion-ready task table with these columns:

| Task Name | Area | Status | Priority | Due Date | Effort | Blocker? | Notes |

Rules:
- Task Name: verb-first (Draft / Review / Build / Send / Decide / Research / Finalise)
- Area: use the life area I provided
- Status: all start as "Inbox"
- Priority: P1 / P2 / P3 / P4
- Due Date: suggest based on the deadline — spread tasks across the available time
- Effort: Small / Medium / Large
- Blocker?: Yes / No
- Notes: Any critical dependency or definition-of-done detail

Aim for 8–14 tasks. Do not add tasks that aren't needed to complete the project.
```

---

## Section 4: Persona-Specific Prompts

---

### Prompt 2.9 — Brain Dump for Students

**When to use:** Use Prompt 2.1 above with this context block added.

---

```
[Use Prompt 2.1: "Brain Dump → Structured System Prompt". Add this student-specific context block:]

Student-specific context:
- Semester / term: [e.g., "Week 7 of Semester 2", "Dissertation month 2"]
- Academic obligations: [LIST UPCOMING DEADLINES — assignments, exams, presentations with dates]
- Non-academic commitments: [PART-TIME WORK, SOCIETIES, SPORT, VOLUNTEERING — with approximate hours]
- What I'm most anxious about right now (even if vague): [WRITE IT HONESTLY]

When sorting my brain dump, please distinguish clearly between:
- Fixed academic deadlines (cannot move)
- Self-imposed goals (I choose to pursue these)
- Things I've said yes to but should evaluate whether I should deprioritise
```

---

### Prompt 2.10 — Multi-Goal Project Mapping Prompt

**Purpose:** Given 2–4 active goals, identify projects that serve more than one goal simultaneously — reducing duplication and effort.

**When to use:** When you have multiple active goals and suspect they might share some of the same work. A powerful efficiency check before building out your full Projects Database.

---

```
You are a strategic project architect. I have multiple active goals and I want to identify projects that serve more than one goal simultaneously, so I can maximise efficiency.

My active goals:
Goal 1: [GOAL NAME + BRIEF OUTCOME]
Goal 2: [GOAL NAME + BRIEF OUTCOME]
Goal 3: [GOAL NAME + BRIEF OUTCOME]
(Add more if needed)

My context: [ROLE / SITUATION / KEY CONSTRAINTS]

Please:
1. Identify any projects or pieces of work that would advance more than one goal at once. Explain clearly which goals they serve and how.
2. For each overlapping project: rate the effort (Small / Medium / Large) and suggest whether to prioritise it above single-goal projects.
3. Identify any goal combinations that are likely to conflict — where doing one well makes it harder to do the other.
4. Suggest 1–2 "gateway projects" — early pieces of work that would build momentum for multiple goals simultaneously.
```

---

*Next file: [`prioritization_prompts.md`](prioritization_prompts.md)*
