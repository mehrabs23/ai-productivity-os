# Day 1: Foundation — Goals, Projects, and Tasks

## Building a Personal Productivity System with AI

---

### Day Goal

By the end of Day 1, every learner has a working Notion workspace containing their real goals, active projects, and current tasks — all structured, linked, and ready to use tomorrow morning.

### Transformation

**Before Day 1:** Learner has vague intentions, scattered notes, and no reliable system.  
**After Day 1:** Learner has a structured digital workspace with a Goals Database, Projects Database, and Task Database — all populated with their own real data.

---

## Session Breakdown

| Session | Title | Duration | Focus |
|---------|-------|----------|-------|
| Opening | Day 1 Kickoff | 15 min | Course intro, workspace setup |
| Session 1 | What Is a Productivity OS? | 60 min | Mental model, tool setup |
| Break | — | 10 min | — |
| Session 2 | Defining Your Goals with AI | 60 min | Goal design, success criteria |
| Break | 10 min | — | — |
| Session 3 | Projects: Translating Goals into Work | 60 min | Project database setup |
| Lunch Break | — | 30 min | — |
| Session 4 | Tasks: The Atomic Unit of Progress | 60 min | Task database, linking, AI breakdown |
| Break | 10 min | — | — |
| Closing | Day 1 Wrap-Up | 30 min | Share-out, reflection, preview |
| **Total** | | **5 hours** | |

---

## Opening: Day 1 Kickoff (15 minutes)

### Instructor Actions
- Welcome learners and introduce course arc
- Confirm everyone has created a Notion account and ChatGPT account
- Share the Notion template link — instruct learners to duplicate it into their workspace
- Quick poll: "On a scale of 1–5, how organised do you feel right now?"

### Learner Actions
- Duplicate the course Notion template
- Open ChatGPT in a separate tab
- Introduce themselves in the course chat (name + one word describing their current productivity state)

---

## Session 1: What Is a Productivity Operating System? (60 minutes)

### Teaching Portion (15 minutes)

**Concept:** Most people manage tasks. Exceptional performers manage systems.

A **Productivity Operating System (Productivity OS)** is the combination of:
- A **structure** for capturing and organising work (databases, categories, relationships)
- A **process** for deciding what to do next (daily planning, prioritization)
- A **ritual** for reviewing and improving (daily check-ins, weekly reviews, retrospectives)

This course builds all three, in that order.

**The three levels of work:**
1. **Goals** — What you want to achieve (outcomes)
2. **Projects** — The work you undertake to achieve goals (deliverables)
3. **Tasks** — The specific actions that move projects forward (actions)

Most people live at the task level. This course installs the full stack.

**Why use Notion?**  
Notion is not just a note-taking app. It is a relational database engine disguised as a notebook. This means we can build a Goals-Projects-Tasks structure where everything is linked — not siloed in separate apps.

**Why use ChatGPT?**  
Most people know what they want to achieve, but struggle to articulate it with enough specificity to act on. ChatGPT is used as a structured thinking partner — it asks the right questions, proposes frameworks, and produces first drafts that learners then edit and own.

### Demo (15 minutes)

**Instructor builds live (using fictional persona "Alex", a freelance UX designer):**

1. Shows the three-database Notion structure in the duplicated template
2. Opens ChatGPT and explains the tab setup (Notion + ChatGPT side by side)
3. Shows the difference between a vague goal ("Get fit") and a specific goal ("Run a 5km in under 30 minutes by September 1st")
4. Demonstrates how a vague goal maps to a vague project — and how this breaks everything downstream

### Student Task 1A: Workspace Setup (30 minutes)

**Minimum Viable Task:**
- Confirm Notion template is duplicated and accessible
- Explore all three databases (Goals, Projects, Tasks) — understand the property structure
- Write 1–2 sentences answering: *"What is the single biggest outcome I want from my life right now?"*

**Extension Task:**
- Explore Notion's Views panel and switch the Task database from Table to Board view
- Add one personal property to the Goals database (e.g., "Domain" with options like Career, Health, Learning)

**Deliverable:** Screenshot or description of your Notion workspace with the three databases visible

---

## Session 2: Defining Your Goals with AI (60 minutes)

### Teaching Portion (15 minutes)

**Concept:** A goal without success criteria is a wish.

Most people define goals in one of two broken ways:
- Too vague: "I want to be healthier"
- Too tactical: "I want to run Monday, Wednesday, Friday"

The sweet spot is a goal that is:
- **Outcome-focused** (what changes in the world, not what you'll do)
- **Time-bounded** (has a deadline)
- **Measurable** (has observable success criteria)
- **Yours** (not what you think you should want)

**The goal design framework used in this course:**

```
Goal = [Outcome statement] + [Deadline] + [Success criteria]
```

**Example:**  
*"Launch a freelance UX design business with 3 paying clients by December 31st.  
Success = 3 active retainer or project clients, £3,000+ monthly recurring revenue, a portfolio of 5 published case studies."*

**Why AI helps here:**  
Articulating goals clearly is hard. ChatGPT does not define your goals for you — it helps you clarify what you actually want by asking targeted questions and reflecting your words back with more precision.

### Demo (15 minutes)

**Instructor demonstrates the Goal Design Prompt (from [`prompt_library/goal_design_prompts.md`](../prompt_library/goal_design_prompts.md)) using Alex's fictional goal:**

1. Inputs the goal design prompt into ChatGPT with Alex's raw goal statement
2. Reviews ChatGPT's output — success criteria, potential obstacles, clarifying questions
3. Edits the output to match what Alex actually wants (not just accepting the AI's first draft)
4. Enters the final goal into the Notion Goals Database with all properties filled

### Student Task 2A: Define Your Goals (45 minutes)

**Minimum Viable Task:**
1. Identify your top 3–5 goals (mix of professional, learning, and personal if applicable)
2. Use the Goal Design Prompt from the prompt library (paste into ChatGPT, replace the placeholder with your raw goal)
3. Review, edit, and personalise the AI output
4. Enter each goal into the Notion Goals Database with:
   - Goal name
   - Outcome statement (1–2 sentences)
   - Deadline
   - Success criteria (3–5 bullet points)
   - Status (Active)
   - Domain tag (optional: Career / Learning / Health / Creative / Financial)

**Extension Task:**
- Use the AI-generated clarifying questions to write a 1-paragraph "goal story" for your most important goal — the narrative version of why this matters

**Deliverable:** Goals Database with at least 3 goals, each with success criteria filled in

**Pair Share (5 min, at end):**  
Share your most important goal with one other learner. Ask each other: *"Does the success criteria actually tell you when you've won?"*

---

## Session 3: Projects — Translating Goals into Work (60 minutes)

### Teaching Portion (15 minutes)

**Concept:** A project is a bounded piece of work that, when complete, moves you closer to a goal.

**The difference between goals and projects:**

| | Goal | Project |
|--|------|---------|
| **Duration** | Months to years | Weeks to months |
| **Definition of done** | Achievement of an outcome | Completion of a deliverable |
| **Example** | Launch freelance business | Build and publish portfolio website |

One goal can have many projects. One project can serve one goal.

**Project properties in this course's system:**
- Project name
- Linked goal
- Status (Active / Paused / Completed / Backlog)
- Priority (High / Medium / Low)
- Deadline
- Description / scope note
- Progress percentage (calculated later via rollup)

**Using AI for project breakdown:**  
Given a goal, ChatGPT can generate a list of projects that together constitute the work needed to achieve that goal. The learner's job is to evaluate whether these projects are realistic, whether any are missing, and whether any are redundant.

### Demo (15 minutes)

**Instructor demonstrates live with Alex's goal:**

1. Uses the Task Breakdown Prompt (adapted for project-level) with Alex's goal
2. Reviews the AI output — 5 candidate projects
3. Selects 2 projects that are most relevant right now
4. Enters them into the Notion Projects Database, linking each to the goal
5. Shows how the linked database relation works (Goals ↔ Projects)

### Student Task 3A: Build Your Projects Database (45 minutes)

**Minimum Viable Task:**
1. For each of your goals, use the Task Breakdown Prompt (project-level version) to generate candidate projects
2. Select 2–4 active projects per goal (focus on what is realistic for the next 3 months)
3. Enter each project into the Projects Database with:
   - Project name
   - Linked goal (select from Goals Database)
   - Status (Active)
   - Priority
   - Deadline (approximate)
   - 1-paragraph scope note (what does this project include and exclude?)

**Extension Task:**
- Use ChatGPT to identify the single most important project across all your goals — the one that would have the greatest impact if completed. Write a 2-sentence justification.

**Deliverable:** Projects Database with at least 2 active projects, each linked to a goal and with a scope note

---

## Session 4: Tasks — The Atomic Unit of Progress (60 minutes)

### Teaching Portion (15 minutes)

**Concept:** A task is the smallest unit of action that moves a project forward.

**What makes a good task:**
- It has a clear definition of done ("done" is not "worked on", it is "finished")
- It can be completed in one work session (ideally under 2 hours)
- It is assigned to one person (in this case, you)
- It has a due date or is date-stamped

**The task decomposition problem:**  
Most people either define tasks too broadly ("Build the website") or too narrowly ("Fix the button colour"). The right granularity is: *"Draft the About page copy and add to the Notion project page"* — specific enough to start, broad enough to be meaningful.

**Task properties in this course's system:**
- Task name
- Linked project
- Status (Not Started / In Progress / Done / Blocked)
- Priority (High / Medium / Low)
- Due date
- Estimated time (hours)
- Actual time (filled in after completion)
- Notes

**Why AI is useful here:**  
Given a project, ChatGPT can generate a first-pass list of tasks — usually more comprehensive than what any person would create in their head. The learner evaluates, prunes, and personalises.

### Demo (10 minutes)

**Instructor demonstrates the Task Breakdown Prompt with Alex's first project:**

1. Uses the Project-to-Tasks Breakdown Prompt from the library
2. Receives 10–12 candidate tasks from ChatGPT
3. Removes 3 that are irrelevant, combines 2 that are too small, and adds 1 that was missed
4. Enters the final 8 tasks into the Task Database, linked to the project

### Student Task 4A: Build Your Task Database (35 minutes)

**Minimum Viable Task:**
1. Pick your most active project
2. Use the Task Breakdown Prompt to generate candidate tasks
3. Edit, prune, and personalise the AI-generated list
4. Enter at least 10 tasks total (across all projects) into the Task Database with:
   - Task name (verb + noun format: "Draft", "Review", "Send", "Build")
   - Linked project
   - Status (Not Started by default)
   - Priority
   - Due date (even approximate)

**Extension Task:**
- Set up a filter view in the Task Database called "This Week" — filter by due date within 7 days, sorted by priority

**Deliverable:** Task Database with at least 10 tasks, distributed across at least 2 projects

---

## Closing: Day 1 Wrap-Up (30 minutes)

### Share-Out (15 minutes)
2–3 volunteers share their screen and walk the group through one goal and its associated project. Group gives one piece of feedback each.

### Day 1 Reflection (10 minutes)
Learners complete the Daily Check-In template for Day 1:
- What did you build today?
- What surprised you about your goals or projects?
- What feels uncomfortable or unclear?
- What is the one thing you want to build on tomorrow?

(Template: [`student_materials/reflection_templates/daily_checkin.md`](../student_materials/reflection_templates/daily_checkin.md))

### Preview of Day 2 (5 minutes)
Tomorrow we move from *what you want to do* to *deciding what to do first*. Day 2 introduces milestone thinking, reverse planning, the anti-to-do list, and attention budgeting.

---

## Day 1 Outputs and Deliverables

| Deliverable | Location |
|-------------|---------|
| Goals Database (3+ goals with success criteria) | Notion workspace |
| Projects Database (2+ projects linked to goals) | Notion workspace |
| Task Database (10+ tasks linked to projects) | Notion workspace |
| Day 1 Daily Check-In (completed) | Reflection template |

---

## Notebook Mapping

> This curriculum references future notebook content that has not yet been built.  
> See [`notebooks/README.md`](../notebooks/README.md) for planned notebook content.

**Planned notebook exercises for Day 1 (future):**
- `nb_01_goal_analysis.ipynb` — Analyse goal phrasing patterns; visualise goal-project-task hierarchy
- `nb_02_task_breakdown_experiment.ipynb` — Compare AI task breakdown outputs for different prompt formulations

---

## Repo Mapping

| Content Type | Location in Repo |
|-------------|-----------------|
| Full student task sheet | [`student_materials/student_task_sheets/day_1_tasks.md`](../student_materials/student_task_sheets/day_1_tasks.md) |
| Goal design prompts | [`prompt_library/goal_design_prompts.md`](../prompt_library/goal_design_prompts.md) |
| Task breakdown prompts | [`prompt_library/task_breakdown_prompts.md`](../prompt_library/task_breakdown_prompts.md) |
| Notion blueprint | [`templates/notion_blueprint.md`](../templates/notion_blueprint.md) |
| CSV task template | [`templates/task_template.csv`](../templates/task_template.csv) |
| Example persona systems | [`examples/`](../examples/) |
| Daily check-in template | [`student_materials/reflection_templates/daily_checkin.md`](../student_materials/reflection_templates/daily_checkin.md) |
