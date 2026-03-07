# Day 2 Task Sheet

## Building a Personal Productivity System with AI

**Date:** Day 2  
**Theme:** Prioritization — Milestones, Reverse Planning, and Attention  
**Your goal today:** Transform your flat task list into a structured priority system with a milestone map, prioritized tasks, an anti-to-do list, and a work session log.

---

### Before You Start

Make sure you have from Day 1:
- [ ] Goals Database with 3+ goals
- [ ] Projects Database with 2+ projects linked to goals
- [ ] Task Database with 10+ tasks linked to projects
- [ ] Daily Check-In from Day 1 completed

If any of these are incomplete, spend the first 15 minutes of Day 2 completing them.

---

## Task 1A: Build Your Milestone Map (Session 1 — 35 min)

**Objective:** Break at least one project into 3+ milestones using reverse planning.

### Step-by-Step

1. **Select your most active project**

2. **Use the Milestone Generation Prompt:**
   - Open [`prompt_library/task_breakdown_prompts.md`](../../prompt_library/task_breakdown_prompts.md)
   - Use the "Milestone Generation Prompt"
   - Copy your project name and scope note into the template
   - Submit to ChatGPT
   - Read the candidate milestones

3. **Edit the milestones:**
   - Check: Are these milestones or tasks? (A milestone is a checkpoint, not an action. "Design phase complete" = milestone. "Create wireframes" = task.)
   - Remove task-level items
   - Add any missing checkpoint moments
   - Aim for 3–5 milestones per project

4. **Apply reverse planning:**
   - Use the "Reverse Planning Prompt" from [`prompt_library/prioritization_prompts.md`](../../prompt_library/prioritization_prompts.md)
   - Input: project end date + milestone list
   - ChatGPT will sequence milestones and suggest target dates
   - Adjust dates based on your real constraints

5. **Record milestones in your Notion project:**
   - Create a toggle list inside the project page titled "Milestone Map"
   - For each milestone: Name | Target Date | Status (Not Started)
   - Check: do any milestone dates conflict with other project milestones this week?

### Minimum Viable Task
- **1 project** with 3+ milestones
- Each milestone has a target date
- You've used the reverse planning approach (worked from end date backwards)

### Extension Task
- Repeat milestone mapping for a second project
- Use ChatGPT to identify whether any milestones across your two projects fall in the same week, and propose a resolution

### Deliverable
At least 1 project with a milestone map (3+ milestones) and reverse-planned dates in your Notion workspace.

---

## Task 2A: Prioritize Your Task List (Session 2 — 45 min)

**Objective:** Apply priority tiers to your entire task list using the AI prioritization prompt.

### Priority Tier Reference

| Tier | Label | Meaning |
|------|-------|---------|
| P1 | Critical | Must be done today — zero slack |
| P2 | High | Must be done this week |
| P3 | Medium | Important but not urgent |
| P4 | Low | Can wait; low consequence if deferred |

> ⚠️ **Rule:** P1 should have at most 1–2 tasks. If you have 5+ P1 tasks, something is wrong with your priority logic — not your task list.

### Step-by-Step

1. **Export your task list:** Copy all task names from your Notion database as a plain text list

2. **Run the Prioritization Prompt:**
   - Open [`prompt_library/prioritization_prompts.md`](../../prompt_library/prioritization_prompts.md)
   - Use the "Task Prioritization Prompt"
   - Include your task list and context (current deadlines, top 2 projects, one thing you've been avoiding)
   - Submit to ChatGPT

3. **Review the AI output critically:**
   - Does the P1 category have fewer than 3 tasks? If not, challenge each one.
   - Identify any task you would categorise differently and explain why (even to yourself)
   - Note: you are the final decision-maker — the AI provides a starting point

4. **Apply priority tiers in Notion:**
   - Update the Priority field for each task in your Task Database
   - Hint: use the Notion filter/sort so you can review each tier together

5. **Create a "This Week's Priorities" view:**
   - New view in Task Database
   - Filter: Due Date ≤ 7 days from today
   - Sort: Priority P1 → P4

### Over-Triage Step (if your list has 10+ tasks due this week)
- Use the "Overload Triage Prompt" from [`prompt_library/prioritization_prompts.md`](../../prompt_library/prioritization_prompts.md)
- Classify each task: Do Now / Schedule / Delegate / Drop
- Apply the decisions — update due dates, archive dropped tasks

### Minimum Viable Task
- Priority tier applied to **all tasks** in the database
- P1 has ≤ 2 tasks
- "This Week's Priorities" filtered view created

### Extension Task
- Create an additional view: "Blocked Tasks" — filter by Status = Blocked
- Identify who/what is blocking each item and note it in the task

### Deliverable
Task Database with priority tiers applied + "This Week's Priorities" view functional.

---

## Task 3A: Start Your Anti-To-Do List (Session 3 — 30 min)

**Objective:** Create an Anti-To-Do database and add at least 5 real entries from recent days.

### What goes on the Anti-To-Do?
- Tasks you completed (even small ones)
- Decisions you made
- Problems you solved that weren't on any list
- Things you said no to
- Conversations, calls, or reviews you completed
- Work sessions you finished

### Step-by-Step

1. **Create the Anti-To-Do section in Notion:**
   - Create a new page called "Anti-To-Do Log" or embed a database called "Anti-To-Do"
   - Properties: Date (Date) | Entry (Text) | Category (Select: Work / Admin / Learning / Decision / Personal)

2. **Add entries — 5 minimum — from the past 3 real days of your life:**
   - Use the format: [Action verb + what] + [why it counts / what it produced]
   - Examples:
     - "Reviewed and sent the Q3 client report (Email) — delivered 2 days early"
     - "Decided to stop pursuing Client X — freed up 5 hours/week"
     - "Debugged and fixed the broken API integration — unblocked the whole sprint"

3. **Add at least 1 entry per session of this course so far**

4. **Optional — run the Anti-To-Do Summary Prompt:**
   - Open [`prompt_library/review_prompts.md`](../../prompt_library/review_prompts.md)
   - Paste your entries and generate a "What I shipped this week" statement

### Minimum Viable Task
- Anti-To-Do section created with 5+ real entries
- Entries use the [action + why it counts] format

### Deliverable
Anti-To-Do Log with at least 5 entries from recent days.

---

## Task 4A: Set Your Attention Budget (Session 4 — 40 min)

**Objective:** Set up your Work Session Log, define your ideal attention allocation, and compare it to your actual behaviour.

### Step-by-Step

**Part 1: Work Session Log**

1. Create a "Work Session Log" database in Notion  
   Properties: Date | Project/Domain | Duration (hours) | Output Notes

2. Backfill at least **5 sessions** from the past 3 days (use calendar or memory — estimates are fine)
   - Examples: "Client A deliverable, 2h — wrote project brief v1"
   - Include admin sessions (meetings, email, admin) honestly

**Part 2: Calculate Actual Allocation**

3. Tally your session log by domain/project (work out the total hours and percentage per category)

**Part 3: Define Ideal Allocation**

4. Write your ideal attention allocation (%) across your main domains
   - Tip: All percentages must sum to 100%
   - Example: Client Work 40% | Learning 20% | Admin 15% | Side Project 15% | Other 10%

**Part 4: Compare and Analyse**

5. Use the "Attention Budget Analysis Prompt" from [`prompt_library/prioritization_prompts.md`](../../prompt_library/prioritization_prompts.md)
   - Input: your ideal vs. actual percentages + brief notes on why gaps exist
   - Read the AI's observations
   - Identify the single largest gap: what is over-consuming your attention?

### Minimum Viable Task
- Work Session Log with 5+ backfilled sessions
- Ideal attention allocation defined
- Actual allocation calculated (even roughly)
- Largest gap identified in writing

### Deliverable
Work Session Log + written comparison of ideal vs. actual attention allocation.

---

## Day 2 End-of-Day Checklist

- [ ] Milestone map: 1+ project with 3+ milestones and reverse-planned dates
- [ ] Priority tiers: all tasks have a P1–P4 tier assigned
- [ ] "This Week's Priorities" view created in Task Database
- [ ] Anti-To-Do Log: 5+ entries
- [ ] Work Session Log: 5+ backfilled sessions
- [ ] Attention Budget: ideal vs. actual comparison documented
- [ ] Daily Check-In completed (see [`reflection_templates/daily_checkin.md`](../reflection_templates/daily_checkin.md))

---

## Prompt References Used Today

| Task | Prompt File | Prompt Name |
|------|------------|-------------|
| 1A | `task_breakdown_prompts.md` | Milestone Generation Prompt |
| 1A | `prioritization_prompts.md` | Reverse Planning Prompt |
| 2A | `prioritization_prompts.md` | Task Prioritization Prompt |
| 2A (if needed) | `prioritization_prompts.md` | Overload Triage Prompt |
| 3A (optional) | `review_prompts.md` | Anti-To-Do Summary Prompt |
| 4A | `prioritization_prompts.md` | Attention Budget Analysis Prompt |
