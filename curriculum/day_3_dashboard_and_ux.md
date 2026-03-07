# Day 3: Dashboard & UX — Kanban, Visibility, and Streaks

## Building a Personal Productivity System with AI

---

### Day Goal

By the end of Day 3, every learner has a functional Master Dashboard in Notion that aggregates their goals, projects, tasks, and streaks into a single command centre they will actually want to open every morning.

### Transformation

**Before Day 3:** Learner has well-structured databases but has to navigate between them. The system exists but is not yet a dashboard.  
**After Day 3:** Learner has a visual, navigable productivity command centre — with a Kanban board, filtered task views, streak tracker, and a UX that reduces friction rather than creating it.

---

## Session Breakdown

| Session | Title | Duration | Focus |
|---------|-------|----------|-------|
| Opening | Day 3 Recap & Setup | 15 min | Check system health from Days 1–2 |
| Session 1 | Kanban Workflow Design | 60 min | Kanban stages, task movement |
| Break | — | 10 min | — |
| Session 2 | Master Dashboard Design | 60 min | Linked views, filters, layout |
| Break | — | 10 min | — |
| Session 3 | Streak Tracker & Consistency | 60 min | Habit tracking, streak logic |
| Lunch Break | — | 30 min | — |
| Session 4 | Dashboard UX Audit | 60 min | Usability self-audit, AI feedback, polish |
| Break | — | 10 min | — |
| Closing | Day 3 Wrap-Up | 30 min | Share-out, reflection, preview |
| **Total** | | **5 hours** | |

---

## Opening: Day 3 Recap (15 minutes)

### Instructor Actions
- Quick system health check: Does everyone have milestones, prioritized tasks, anti-to-do, and attention budget?
- Acknowledge: "Your system probably feels clunky to navigate right now. Today we fix that."
- Frame Day 3: "We're building the front-end of your system."

### Quick Demo Problem
Instructor opens a Notion workspace with 4 separate databases and no dashboard. 
"Try to find out what your three most important tasks for today are."  
Learners observe how many clicks it takes. Then: "By end of today, that's one view."

---

## Session 1: Kanban Workflow Design (60 minutes)

### Teaching Portion (20 minutes)

**Concept: What is a Kanban board?**

Kanban is a visual workflow management method originating from Toyota's manufacturing process. In personal productivity, it means displaying work as cards that move across stages from left to right — representing the lifecycle of a task from creation to completion.

**Why Kanban over a simple task list:**
- Provides spatial context — blocked work looks different from in-progress work
- Limits work-in-progress naturally (you feel uncomfortable when a column is overflowing)
- Makes flow visible — you can see if nothing is moving through "In Progress"

**The default Notion Kanban workflow (Board view):**
Each task card lives in a column corresponding to its Status property. Drag-and-drop moves tasks between stages.

**Recommended stages for this course:**

| Stage | What Goes Here |
|-------|---------------|
| **Backlog** | Tasks captured but not yet scheduled |
| **This Week** | Tasks committed to for the current week |
| **In Progress** | Tasks actively being worked on (ideally ≤3 at once) |
| **Blocked** | Tasks that cannot move forward without external input |
| **Done** | Completed tasks (can archive weekly) |

**Customising stages:**  
Learners should tailor stages to their own workflow. A writer might add "Draft" and "Editing". A student might add "Exam Prep" and "Submitted". The stage names should describe *real* states in the learner's workflow.

**WIP Limits:**  
A core Kanban principle: limit work in progress. For personal productivity, a good rule of thumb is: no more than 3 tasks in "In Progress" at any time. When a fourth task tries to move in, something must move to Done or Back to This Week.

### Demo (20 minutes)

**Instructor demonstrates with Alex's system:**

1. Opens the Task Database and switches to Board view (by Status)
2. Renames the status options to the five recommended stages
3. Moves several tasks into the appropriate columns based on actual status
4. Discusses the visual effect: "In Progress is full. Something is blocked. That's information."
5. Creates a WIP limit visual reminder: a Callout block above the Kanban that says "In Progress limit: 3"
6. Shows a filtered Kanban view: "Active Work" — filter out Backlog and Done

### Student Task 1A: Build Your Kanban Board (40 minutes)

**Minimum Viable Task:**
1. Open your Task Database and switch to Board view
2. Edit the Status property to include your preferred workflow stages (minimum: Backlog / This Week / In Progress / Blocked / Done)
3. Move existing tasks into the correct columns
4. Add a WIP limit note at the top of your board (Callout or Text block)
5. Create a filtered view of the Kanban: "Active Work" — exclude Backlog and Done

**Extension Task:**
- Add a second grouping option to the Kanban (Group by Priority OR by Project) and explore how different groupings reveal different patterns
- Use the Kanban Design Prompt to get AI suggestions for custom workflow stages specific to your type of work

**Deliverable:** Task Database in Board view with at least 4 stages, tasks distributed across columns

---

## Session 2: Master Dashboard Design (60 minutes)

### Teaching Portion (20 minutes)

**Concept: The Dashboard as Command Centre**

The Master Dashboard is a single Notion page that gives you a complete view of your system at a glance. It does not store new data — it **aggregates and filters** data from your existing databases into the most useful views.

**Design principles for a good productivity dashboard:**

1. **Signal, not noise:** Only show information you need to act on. Hide completed tasks, archived goals, and low-priority items by default.

2. **Navigation, not repetition:** Each view should answer a specific question. "What do I do today?" is different from "What is due this week?" Don't duplicate views unnecessarily.

3. **Visual hierarchy:** The most important information is at the top. Secondary context is below the fold.

4. **One click to action:** From the dashboard, you should be able to open any task or project in one click.

**Recommended dashboard sections:**

| Section | Content | Filter |
|---------|---------|--------|
| Today's Priorities | Task list | Due today OR P1 |
| This Week | Task list | Due within 7 days, sorted by priority |
| Active Projects | Project list | Status = Active |
| Streak Tracker | Habit database | Always visible |
| Quick Capture | Text block | A single text area for fast capture |
| Anti-To-Do (Today) | Filtered anti-to-do | Date = today |

**Notion Dashboard mechanics:**
- Use **Linked Database** (not embedded database) to pull data from existing databases
- Apply filters directly on the linked view — this doesn't change the source database
- Use **Gallery view** for projects (shows covers), **Table view** for tasks, **List view** for quick references

### Demo (20 minutes)

**Instructor builds Alex's Master Dashboard live:**

1. Creates a new Notion page called "🏠 Mission Control"
2. Adds a heading section and a two-column layout
3. Column 1: Adds linked database "Today's Focus" = filtered Task table (Due = today, Status ≠ Done)
4. Column 1 (below): Adds "Active Projects" = filtered Project gallery (Status = Active)
5. Column 2: Adds "This Week" = Task table (Due ≤ 7 days, sorted Priority High→Low)
6. Column 2 (below): Adds "Today's Anti-To-Do" (filtered by today's date)
7. Adds a Quick Capture toggle at the top for fast notes

### Student Task 2A: Build Your Master Dashboard (40 minutes)

**Minimum Viable Task:**
1. Create a new page in Notion: "🏠 [Your Name]'s Mission Control"
2. Add the following linked database views (at minimum):
   - Today's Priorities: Task database, filtered by Due = today or Priority = Critical
   - This Week: Task database, filtered by Due ≤ 7 days
   - Active Projects: Project database, filtered by Status = Active
3. Organise sections using Notion's column layout (2-column preferred)
4. Add your name and today's date as a callout at the top
5. Set this page as your Notion workspace home (pin it or set it as default)

**Extension Task:**
- Add an "Anti-To-Do: Today" section linked from your Anti-To-Do database
- Add a custom emoji or cover image to the dashboard page
- Use the Dashboard Design Prompt to get AI feedback on your layout choices

**Deliverable:** Master Dashboard page with at least 3 linked views and a functional layout

---

## Session 3: Streak Tracker & Consistency (60 minutes)

### Teaching Portion (20 minutes)

**Concept: Why Streaks Work**

A productivity system without a consistency mechanism degrades within weeks. Streaks provide:

1. **Visual commitment:** Seeing a visual chain of consecutive days on a routine makes breaking it feel costly
2. **Identity reinforcement:** "I am someone who reviews their tasks every morning" is more durable than "I want to review my tasks every morning"
3. **Minimum viable consistency:** A streak tracker doesn't care how much you did — only that you did *something*. This prevents perfectionism from becoming an obstacle to showing up.

**What to track:**
Streaks are most useful for **process habits** — things you do regardless of whether you're in the mood. Examples:
- Daily Morning Planning (complete daily planning session)
- End-of-Day Reflection (complete daily check-in)
- Work Session Logged (log at least 1 session per day)
- Anti-To-Do Updated (add at least 1 entry)

**What not to track:**  
Don't track outcome targets (e.g., "complete 5 tasks") as streaks. Outcome quantities vary with life circumstances. Process habits are the right level.

**Streak tracker structure in Notion:**
A simple database with:
- Habit name
- Date
- Completed (checkbox)
- Notes (optional)

A filtered view shows the current streak (consecutive days with Completed = true).

### Demo (20 minutes)

**Instructor builds Alex's Streak Tracker:**

1. Creates a "Streak Tracker" database with: Date, Habit (select), Completed (checkbox), Notes
2. Adds 3 habits: Morning Planning, End-of-Day Reflection, Session Logged
3. Backfills 5 days of fictional data
4. Creates a Streak Tracker view filtered to the last 14 days, sorted by Date descending
5. Shows how to add the Streak view to the Master Dashboard as a linked view
6. Uses a formula (optional, shown briefly): counts consecutive days of True in Completed field

### Student Task 3A: Build Your Streak Tracker (35 minutes)

**Minimum Viable Task:**
1. Create a "Streak Tracker" database in your Notion workspace with properties:
   - Date (Date)
   - Habit (Select — add 2–3 habits)
   - Completed (Checkbox)
   - Notes (Text, optional)
2. Define 2–3 habits to track (choose process habits, not outcome targets)
3. Add today's entries (one row per habit per day)
4. Create a view filtered to the last 14 days, sorted by Date descending
5. Add this view to your Master Dashboard

**Extension Task:**
- Backfill the streak tracker for the past 3 days (use honest estimates of whether you completed each habit)
- Use the Streak Design Prompt to get suggestions for which habits are worth tracking for your specific goals

**Deliverable:** Streak Tracker database with 2–3 habits, today's entries added, view linked in Dashboard

**Discussion Prompt:**
*"What's the daily process habit that, if you did it consistently, would have the biggest impact on your goals? What has stopped you from doing it consistently so far?"*

---

## Session 4: Dashboard UX Audit (60 minutes)

### Teaching Portion (15 minutes)

**Concept: UX for Personal Tools**

A tool's usability isn't just about aesthetics — it's about reducing friction. Friction is anything that makes it harder to start, continue, or return to a behaviour. A dashboard with too many sections, unclear labels, or too much noise is a friction machine.

**UX audit questions for your dashboard:**

1. **Load test:** Can you see the most important thing you need to do today within 5 seconds of opening the dashboard?
2. **Noise audit:** Is there any section you consistently ignore? Remove it or hide it.
3. **Click count:** Can you open a specific task in under 3 clicks from the dashboard?
4. **Label clarity:** Are all your linked views clearly named? Would someone else understand what each section is for?
5. **Emotional check:** Does opening this dashboard feel like relief or dread? Dread is a UX problem.

**AI feedback on dashboard design:**  
The Dashboard UX Audit Prompt helps learners describe their dashboard layout to ChatGPT and receive structured feedback on what to simplify, reorganise, or remove.

### Demo (10 minutes)

**Instructor runs the UX Audit Prompt on Alex's dashboard:**

1. Describes Alex's dashboard layout to ChatGPT using the audit prompt template
2. Receives 5 specific suggestions
3. Implements 2 of them live: removes a redundant section, renames an unclear view
4. Loads the dashboard again: "How does this feel different?"

### Student Task 4A: UX Audit Your Dashboard (30 minutes)

**Minimum Viable Task:**
1. Complete the load test on your dashboard — time yourself: can you find today's top priority in 5 seconds?
2. Run the Dashboard UX Audit Prompt with a description of your current layout
3. Implement at least 2 changes from the AI feedback
4. Add a "Last Updated" callout block with today's date

**Extension Task:**
- Add an "Inbox" section to your dashboard: an unfiltered Quick Capture box for anything that needs to be sorted later
- Ask a classmate to navigate your dashboard and report back: what was confusing? What was clear?

**Deliverable:** Refined Master Dashboard with at least 2 UX improvements documented in a brief note

---

## Closing: Day 3 Wrap-Up (30 minutes)

### Share-Out (15 minutes)
2–3 volunteers share their dashboard screen. Group gives one compliment and one improvement suggestion for each.

### Day 3 Reflection (10 minutes)
Learners complete the Day 3 Daily Check-In:
- What does your dashboard tell you about your current system state?
- What is still confusing or uncomfortable?
- What one change made the biggest visual difference?

### Preview of Day 4 (5 minutes)
Tomorrow we close the loop. Day 4 teaches the daily AI planning routine, the weekly review, the retrospective — and ends with the capstone presentation of your complete system.

---

## Day 3 Outputs and Deliverables

| Deliverable | Location |
|-------------|---------|
| Kanban Board (4+ stages, tasks populated) | Notion Task Database — Board view |
| Master Dashboard (3+ linked views) | Notion Master Dashboard page |
| Streak Tracker (2–3 habits, today's entries) | Notion Streak Tracker database |
| Dashboard UX improvements noted | Brief note or callout in dashboard |
| Day 3 Daily Check-In (completed) | Reflection template |

---

## Notebook Mapping

> See [`notebooks/README.md`](../notebooks/README.md) for planned notebook content.

**Planned notebook exercises for Day 3 (future):**
- `nb_05_streak_analysis.ipynb` — Visualise streak consistency over 30 days; identify drop patterns
- `nb_06_kanban_flow.ipynb` — Analyse task flow rates between stages; identify bottlenecks

---

## Repo Mapping

| Content Type | Location in Repo |
|-------------|-----------------|
| Day 3 student task sheet | [`student_materials/student_task_sheets/day_3_tasks.md`](../student_materials/student_task_sheets/day_3_tasks.md) |
| Dashboard blueprint | [`templates/dashboard_blueprint.md`](../templates/dashboard_blueprint.md) |
| Kanban structure template | [`templates/kanban_structure.md`](../templates/kanban_structure.md) |
| Streak tracker structure | [`templates/streak_tracker_structure.md`](../templates/streak_tracker_structure.md) |
| System optimisation prompts | [`prompt_library/system_optimization_prompts.md`](../prompt_library/system_optimization_prompts.md) |
