# Day 1 Task Sheet

## Building a Personal Productivity System with AI

**Date:** Day 1  
**Theme:** Foundation — Goals, Projects, and Tasks  
**Your goal today:** Set up your Notion workspace and populate it with real goals, projects, and tasks.

---

### Before You Start

Make sure you have:
- [ ] Notion account created and template duplicated
- [ ] ChatGPT account open in a separate tab
- [ ] Your task sheet open alongside your Notion workspace
- [ ] A rough sense of your top 2–3 goals before the session starts (can be vague — you'll refine them)

---

## Task 1A: Workspace Setup (Session 1 — 25 min)

**Objective:** Understand and confirm your Notion workspace structure.

### Minimum Viable Task
1. Open your duplicated Notion template
2. Navigate to each of the three databases and confirm you can see them:
   - [ ] Goals Database
   - [ ] Projects Database
   - [ ] Tasks Database
3. Click into the Goals database and review the property list (Goal Name, Outcome, Deadline, Success Criteria, Status)
4. Write your answer to this question in any note or scratch document:

> *"What is the single biggest outcome I want from my work or life right now?"*

This is your starting point. It doesn't need to be perfect — it's the raw material for Task 2A.

### Extension Task
- Switch the Task Database to Board view and explore it
- Add one custom property to the Goals database that feels personally relevant (e.g., "Domain" with tags like Career / Health / Learning)

### Deliverable
Screenshot or brief description of your Notion workspace showing all three databases visible.

---

## Task 2A: Define Your Goals (Session 2 — 45 min)

**Objective:** Enter 3–5 real, specific goals into your Goals Database using the Goal Design Prompt.

### Step-by-Step

1. **Write your raw goals** — list 3–5 goals in your own words. They can be vague at this stage.

2. **Run the Goal Design Prompt** for your most important goal:
   - Open [`prompt_library/goal_design_prompts.md`](../../prompt_library/goal_design_prompts.md)
   - Copy the "Goal Definition Prompt" template
   - Fill in `[YOUR RAW GOAL STATEMENT]` with your raw goal
   - Paste into ChatGPT and submit
   - Read the output

3. **Edit the output:**
   - Select the success criteria that resonate (delete ones that don't)
   - Change anything the AI got wrong about your specific situation
   - Add anything the AI missed

4. **Enter the goal into Notion:**
   - Goal name (concise, active phrasing)
   - Outcome statement (1–2 sentences)
   - Deadline (specific date, even if approximate)
   - Success criteria (3–5 bullet points)
   - Status: Active

5. **Repeat for 2–4 more goals** (you can skip the AI prompt if you already know what you want)

### Minimum Viable Task
- At least **3 goals** in the database
- Each goal has: deadline + at least 3 success criteria
- You have edited at least one AI-generated output

### Extension Task
- For your most important goal, write a 1-paragraph "goal story": the narrative version of why this goal matters to you right now

### Pair Share Check
After completing this task, share your most important goal with one other person in the room and ask:  
*"Does my success criteria tell you when I've won?"*

### Deliverable
Goals Database with at least 3 goals, each with a deadline and success criteria filled in.

---

## Task 3A: Build Your Projects Database (Session 3 — 40 min)

**Objective:** Create at least 2 active projects linked to your goals.

### Step-by-Step

1. **For each goal**, ask: "What is the primary piece of work I need to undertake to achieve this goal?"  
   That's a project.

2. **Use the Task Breakdown Prompt (project-level version)**:
   - Open [`prompt_library/task_breakdown_prompts.md`](../../prompt_library/task_breakdown_prompts.md)
   - Use the "Project Identification Prompt"
   - Input your goal and ask ChatGPT to generate 3–5 candidate projects
   - Select 1–2 that are most relevant in the next 3 months

3. **Enter each project into the Projects Database:**
   - Project name
   - Linked goal (click the relation property → select from Goals Database)
   - Status: Active
   - Priority: High / Medium / Low
   - Deadline (approximate — even a month is fine)
   - Scope note: 1 sentence on what this project includes and excludes

### Minimum Viable Task
- At least **2 active projects** in the database
- Each linked to a goal
- Each has a scope note distinguishing what it includes from what it excludes

### Extension Task
- Use ChatGPT to identify which single project, if completed, would have the greatest impact on your goals. Write a 2-sentence justification.

### Deliverable
Projects Database with at least 2 active projects, each linked to a goal.

---

## Task 4A: Build Your Task Database (Session 4 — 30 min)

**Objective:** Create at least 10 tasks across your projects.

### Step-by-Step

1. **Pick your most active project**
2. **Use the Task Breakdown Prompt**:
   - Open [`prompt_library/task_breakdown_prompts.md`](../../prompt_library/task_breakdown_prompts.md)
   - Use the "Project-to-Tasks Breakdown Prompt"
   - Input your project name and scope
   - ChatGPT returns 10–12 candidate tasks

3. **Edit the task list:**
   - Remove tasks that are too small or irrelevant
   - Split tasks that are too large (if it takes more than one session, split it)
   - Add any tasks the AI missed

4. **Enter tasks into the Task Database:**
   - Task name (start with a verb: Draft, Review, Send, Build, Decide)
   - Linked project (select from Projects Database)
   - Status: Not Started
   - Priority: your initial guess (you'll refine this tomorrow)
   - Due date: approximate is fine

5. **Repeat for at least one more project** (to reach 10+ total tasks)

### Minimum Viable Task
- At least **10 tasks** in the database
- Tasks distributed across at least 2 projects
- Each task linked to a project

### Extension Task
- Create a filter on the Task Database called "This Week" — show only tasks with due dates within the next 7 days, sorted by priority

### Deliverable
Task Database with at least 10 tasks, linked to at least 2 projects.

---

## Day 1 End-of-Day Checklist

- [ ] Goals Database: 3+ goals with deadlines and success criteria
- [ ] Projects Database: 2+ active projects linked to goals
- [ ] Task Database: 10+ tasks linked to projects
- [ ] Pair share completed (shared at least one goal)
- [ ] Daily Check-In completed (see [`reflection_templates/daily_checkin.md`](../reflection_templates/daily_checkin.md))

---

## Prompt References Used Today

| Task | Prompt File | Prompt Name |
|------|------------|-------------|
| 2A | `goal_design_prompts.md` | Goal Definition Prompt |
| 3A | `task_breakdown_prompts.md` | Project Identification Prompt |
| 4A | `task_breakdown_prompts.md` | Project-to-Tasks Breakdown Prompt |
