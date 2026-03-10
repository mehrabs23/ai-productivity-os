# Day 2: Prioritization — Milestones, Reverse Planning, and Attention

## Building a Personal Productivity System with AI

---

### Day Goal

By the end of Day 2, every learner has transformed their flat task list into a structured priority system — with milestones, reverse-planned timelines, a clear picture of where their attention actually goes, and an honest anti-to-do list.

### Transformation

**Before Day 2:** Learner has a list of tasks and projects, but no sense of sequence, priority, or effort allocation.  
**After Day 2:** Learner has a milestone map, prioritized tasks, a tracked attention budget, and a work session log — giving them a clear view of where they intend to focus and where they are actually spending time.

---

## Session Breakdown

| Session | Title | Duration | Focus |
|---------|-------|----------|-------|
| Opening | Day 2 Recap & Setup | 15 min | System check, Day 1 review |
| Session 1 | Milestone Thinking & Reverse Planning | 60 min | Breaking projects into milestones |
| Break | — | 10 min | — |
| Session 2 | Task Prioritization with AI | 60 min | Priority tiers, AI triage |
| Break | — | 10 min | — |
| Session 3 | The Anti-To-Do List | 60 min | Capturing done work, combating to-do guilt |
| Lunch Break | — | 30 min | — |
| Session 4 | Attention Budgeting | 60 min | Session logging, ideal vs. actual allocation |
| Break | — | 10 min | — |
| Closing | Day 2 Wrap-Up | 30 min | Share-out, reflection, preview |
| **Total** | | **5 hours** | |

---

## Opening: Day 2 Recap (15 minutes)

### Instructor Actions
- Quick show of hands: Who has a complete Goals + Projects + Tasks database?
- Address common Day 1 issues (too many tasks, goals too vague, can't decide on priorities)
- Frame Day 2: "Now that we have a system, let's make it smart"

### Quick Pair Check
- Open your Notion workspace
- Count your tasks: How many are actually "High Priority"? (Most learners will find they marked everything High)
- This lands the core problem Day 2 solves

---

## Session 1: Milestone Thinking & Reverse Planning (60 minutes)

### Teaching Portion (20 minutes)

**Concept 1: What is a milestone?**

A milestone is a **named, verifiable checkpoint** within a project. It is not a task (too small) and not the project itself (too large). It is the moment you can point to and say: "We passed this threshold."

| Level | Example |
|-------|---------|
| Goal | "Launch freelance UX business with 3 clients" |
| Project | "Build and publish portfolio website" |
| **Milestone** | "First draft of all 5 case studies written" |
| **Milestone** | "Portfolio site live at custom domain" |
| Task | "Write case study for Project A" |

**Why milestones matter:**  
Without milestones, a project is a blob of work with a single due date. Problems don't surface until they are urgent. With milestones, problems surface early, when there's still time to adapt.

**Concept 2: Reverse Planning**

Forward planning starts from today and asks: "What can I do next?" This leads to optimistic, front-loaded plans that fall apart as reality intervenes.

**Reverse planning** starts from the end state and asks: "What must be true for this to happen?" Then: "What must be true before that?" Then: "What must be true before that?" Working backwards reveals the critical path and the dependencies between milestones.

**The reverse planning sequence:**
1. Define the project end state (what "done" looks like)
2. Identify the final milestone before project completion
3. Work backwards 3–5 steps to reach the current state
4. Each step is a milestone with a defined deadline
5. Check: Is this realistic? Do any milestones conflict with other projects?

### Demo (20 minutes)

**Instructor demonstrates with Alex's portfolio project:**

1. Uses the Milestone Thinking Prompt from the prompt library
2. ChatGPT generates 5 candidate milestones for "Build and publish portfolio website"
3. Instructor critiques the output — some milestones are too small (task-level), one is missing
4. Edits and enters 4 milestones into a Milestones view in the Projects database
5. Uses reverse planning prompt to sequence them from end to current date
6. Enters target dates and shows the milestone map view in Notion

### Student Task 1A: Build Your Milestone Map (40 minutes)

**Minimum Viable Task:**
1. Select your most active project
2. Use the Milestone Generation Prompt (from prompt library) with your project description
3. Review and edit the AI-generated milestones — remove, add, merge as needed
4. Create milestone entries in the Milestones section of your project (using a toggle list or sub-page)
5. Use the Reverse Planning Prompt to sequence them
6. Assign a target date to each milestone
7. Check: Are these dates realistic? Do any fall in the same week as other project milestones?

**Minimum milestone structure per milestone:**
- Name (e.g., "First draft of all case studies written")
- Target date
- Key task(s) required
- Status (Not Started / In Progress / Done)

**Extension Task:**
- Repeat milestone mapping for a second project
- Identify if any milestones across projects conflict — use ChatGPT to help propose a resolution

**Deliverable:** At least 1 project with a milestone map (3+ milestones) and reverse-planned dates

---

## Session 2: Task Prioritization with AI (60 minutes)

### Teaching Portion (20 minutes)

**Concept: The Priority Illusion**

Most people prioritize tasks by urgency or by how loud the requester is. This produces work that feels important but isn't — and consistently deprioritizes work that genuinely matters.

**The four priority tiers used in this course:**

| Tier | Label | Definition |
|------|-------|-----------|
| P1 | **Critical** | Must be done today; blocking others or has zero-slack deadline |
| P2 | **High** | Must be done this week; significant consequence if delayed |
| P3 | **Medium** | Should be done this sprint; important but not urgent |
| P4 | **Low** | Can be done when time permits; no significant consequence if deferred |

**The key insight:**  
The P1 category should almost always be **empty or have only one item**. If you have five P1 tasks, something is wrong — either your deadlines are unrealistic, or you haven't made real priority decisions.

**Using AI for prioritization:**  
ChatGPT is used to analyse a task list and apply the priority tier logic. The learner provides their task list, context about deadlines and goals, and the AI produces a prioritized version with reasoning. The learner then overrides any disagreements.

**The overload triage prompt:**  
When a task list is too long — more tasks than can realistically be done this week — the overload triage prompt helps learners identify what to defer, delegate, or drop. It forces explicit tradeoff decisions rather than passive accumulation.

### Demo (15 minutes)

**Instructor demonstrates the Prioritization Prompt with Alex's task list:**

1. Copies all tasks from the Notion Task Database into the prompt template
2. Runs the prioritization prompt in ChatGPT
3. Reviews the output — AI assigns tiers and provides one-line reasoning for each
4. Instructor demonstrates the override process: "I disagree with this P2 — it's P1 because of this client relationship"
5. Updates the Priority field in the Notion database
6. Shows the filtered view "P1 Tasks" — filters Task Database by Priority = Critical

### Student Task 2A: Prioritize Your Tasks (45 minutes)

**Minimum Viable Task:**
1. Copy your task list (from Notion) into the Prioritization Prompt template
2. Add context: your current deadlines, your top 2 active projects, and one thing you've been avoiding
3. Run the prompt and review the output
4. Apply the tier labels to your Notion Task Database (update the Priority property)
5. Create a filtered view called "This Week's Priorities" — filter: Due Date ≤ +7 days, Sort: Priority High → Low

**Extension Task:**
- If you have more than 10 tasks due this week, run the Overload Triage Prompt
- Identify at least 2 tasks to defer, and 1 task to drop entirely
- Update the task statuses accordingly

**Deliverable:** Task Database with priority tiers assigned, plus a "This Week's Priorities" filtered view

---

## Session 3: The Anti-To-Do List (60 minutes)

### Teaching Portion (20 minutes)

**Concept: The To-Do List Problem**

Traditional to-do lists only show what you haven't done yet. This creates a psychological burden: the list is always negative. It shows only unfinished work, never finished work. This conditions learners to feel perpetually behind.

**The Anti-To-Do List:**  
The anti-to-do list is a running log of **what you have actually done** — tasks completed, deliverables shipped, conversations had, decisions made, problems solved. Things go on the anti-to-do list *after* they're done, not before.

**Why this matters:**
1. **Progress visibility:** You can see that you've actually done significant work, even on days that felt wasted
2. **Counters perfectionism:** The anti-to-do gives credit to imperfect but useful work
3. **Inputs the weekly review:** At end of week, the anti-to-do is the raw material for "what actually happened this week"
4. **Psychological safety:** Learners feel less guilty about tasks they chose NOT to do, because they can see what they chose to do instead

**What belongs on the anti-to-do list:**
- Completed tasks (even small ones)
- Work sessions you finished
- Decisions you made
- Things you said no to
- Problems you solved that weren't on any list

**Two-line rule:** Each anti-to-do entry is 1–2 lines: what was done, and why it mattered (or why it counted).

### Demo (15 minutes)

**Instructor builds Alex's Anti-To-Do for the current fictional day:**

1. Creates an Anti-To-Do database in Notion (simple: Date, Entry, Category)
2. Populates 5 entries from Alex's fictional morning: client call notes, revised scope doc, finally sent that email, decided to defer feature X, resolved a billing question
3. Shows how the Anti-To-Do becomes the source of the daily reflection question: "What actually moved?"
4. Shows how to use the Anti-To-Do Prompt to generate a weekly accomplishment summary

### Student Task 3A: Start Your Anti-To-Do List (45 minutes)

**Minimum Viable Task:**
1. Create an Anti-To-Do section in your Notion workspace (dedicated database or embedded sub-page)
2. Properties needed: Date, Entry (text), Category (select: Work / Learning / Admin / Personal / Decision)
3. Add at least 5 entries from the past 3 days of your real life — things you did that never appeared on any to-do list
4. Add one entry per session you've completed so far in this course

**Extension Task:**
- Use the Anti-To-Do Summary Prompt to generate a "What I accomplished this week" statement from your entries
- This is the same prompt you will use every Friday for your weekly review

**Deliverable:** Anti-To-Do section with at least 5 real entries from recent days

**Discussion Prompt:**
*"Did anything surprise you when you started listing what you'd actually done? What work do you do that never appears on a to-do list?"*

---

## Session 4: Attention Budgeting (60 minutes)

### Teaching Portion (20 minutes)

**Concept 1: Attention is not the same as time**

You have 8 working hours in a day, but you do not have 8 hours of **attention**. Research consistently shows that deep, focused work — the kind that produces the most valuable output — is typically available in blocks of 1–2 hours, 2–4 times per day.

**Attention budgeting** is the practice of deliberately allocating your limited focused attention across your commitments, rather than letting it be claimed by whoever asks loudest.

**Concept 2: Ideal vs. Actual Allocation**

The attention budget has two sides:
- **Ideal allocation:** What percentage of your focused time *should* go to each domain?
- **Actual allocation:** What percentage *does* go to each domain, based on your work session log?

Most people are shocked when they compare the two.

**Example attention budget:**

| Domain | Ideal % | Actual % (last week) | Gap |
|--------|---------|---------------------|-----|
| Client Project A | 35% | 20% | −15% |
| Personal Project B | 25% | 5% | −20% |
| Admin (email, meetings) | 10% | 40% | +30% |
| Learning | 20% | 10% | −10% |
| Other | 10% | 25% | +15% |

This comparison is often the most confronting moment of the course. It shows, with data, that intentions and action are misaligned.

**Concept 3: Work Session Log**

The work session log is a simple record of each focused work block:
- Date
- Project / Domain
- Duration (hours)
- Output (what was produced)

After one week, this log provides the raw data for the actual attention allocation.

### Demo (15 minutes)

**Instructor demonstrates with Alex:**

1. Creates the Work Session Log database in Notion using the template structure
2. Enters 4 fictional sessions from Alex's past 2 days
3. Shows how to calculate the actual % per project from the log
4. Opens ChatGPT and uses the Attention Budget Analysis Prompt
5. Enters Alex's ideal vs actual allocations and reviews the AI's observations and recommendations
6. Discusses: "What would Alex need to change to close the gap?"

### Student Task 4A: Set Your Attention Budget (45 minutes)

**Minimum Viable Task:**
1. Set up the Work Session Log in your Notion workspace (or use the provided CSV template as a Google Sheet)
   - Properties: Date, Project/Domain, Duration (hours), Output Notes
2. Backfill at least 5 sessions from the past 3 days (real sessions, even rough estimates)
3. Calculate (manually or with ChatGPT's help) your actual percentage per domain for the past week
4. Define your ideal attention allocation — what should the percentages be?
5. Compare ideal vs. actual, note the biggest gap
6. Use the Attention Budget Analysis Prompt to generate observations and proposed adjustments

**Extension Task:**
- Create a simple weekly budget rule: "I will not let admin exceed 20% of my focused hours"
- Enter this as a "Budget Constraint" property on your Attention Budget note
- Identify one recurring commitment that consistently violates your budget

**Deliverable:** Work Session Log with at least 5 entries + written comparison of ideal vs. actual allocation

---

## Closing: Day 2 Wrap-Up (30 minutes)

### Share-Out (15 minutes)
2–3 volunteers share:
- Their biggest priority surprise (what they thought was P1 that actually wasn't)
- The gap they found in their attention budget

### Day 2 Reflection (10 minutes)
Learners complete the Day 2 Daily Check-In:
- What structure did you add to your system today?
- What did you realise about how you've been spending your time?
- What is one decision you made about where to focus this week?

### Preview of Day 3 (5 minutes)
Tomorrow we move from a system in databases to a **system you can see and navigate**. Day 3 builds the Kanban board, the Master Dashboard, and the streak tracker.

---

## Day 2 Outputs and Deliverables

| Deliverable | Location |
|-------------|---------|
| Milestone map (1+ project, 3+ milestones) | Notion workspace |
| Prioritized task list with "This Week" view | Notion Task Database |
| Anti-To-Do List (5+ entries) | Notion workspace |
| Work Session Log (5+ backfilled entries) | Notion / Google Sheets |
| Attention Budget (ideal vs. actual) | Written or Notion note |
| Day 2 Daily Check-In (completed) | Reflection template |

---

## Notebook Mapping

> This day's activities are supported by **optional interactive notebooks** for deeper analysis.
> See [`notebooks/day_2_prioritization.ipynb`](../notebooks/day_2_prioritization.ipynb) or the [Colab version](../colab_versions/day_2_prioritization.ipynb).

**Available notebook exercises for Day 2:**
- `nb_03_session_log_analysis.ipynb` — Import CSV session log and compute actual allocation percentages
- `nb_04_priority_statistics.ipynb` — Analyse priority distribution and identify overloaded task lists

---

## Repo Mapping

| Content Type | Location in Repo |
|-------------|-----------------|
| Day 2 student task sheet | [`student_materials/student_task_sheets/day_2_tasks.md`](../student_materials/student_task_sheets/day_2_tasks.md) |
| Prioritization prompts | [`prompt_library/prioritization_prompts.md`](../prompt_library/prioritization_prompts.md) |
| Task breakdown prompts | [`prompt_library/task_breakdown_prompts.md`](../prompt_library/task_breakdown_prompts.md) |
| Work session log template | [`templates/work_session_log_template.csv`](../templates/work_session_log_template.csv) |
| Attention budget template | [`templates/attention_budget_template.csv`](../templates/attention_budget_template.csv) |
| Project template | [`templates/project_template.csv`](../templates/project_template.csv) |
