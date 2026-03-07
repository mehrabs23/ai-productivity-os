# Day 4 Task Sheet

## Building a Personal Productivity System with AI

**Date:** Day 4  
**Theme:** AI Review & Capstone  
**Your goal today:** Close the loop — establish your daily planning ritual, complete a weekly review and retrospective, and present your complete productivity system.

---

### Before You Start

Make sure you have all Day 1–3 deliverables:
- [ ] Goals, Projects, and Tasks databases populated
- [ ] Milestone map for at least 1 project
- [ ] Priority tiers applied to tasks
- [ ] Anti-To-Do Log and Work Session Log started
- [ ] Attention Budget documented
- [ ] Master Dashboard with Kanban and Streak Tracker
- [ ] Daily Check-Ins for Days 1–3 completed

**Reminder:** You are presenting your capstone today. Read [`capstone_instructions.md`](../capstone_instructions.md) if you haven't already.

---

## Task 1A: Run Your Daily AI Planning Session (Session 1 — 35 min)

**Objective:** Run a complete daily planning session using the structured prompt sequence. This is your first iteration of the ritual you'll use every working day going forward.

### The Daily Planning Sequence

1. **Open your Notion dashboard** — identify your top 3 priorities for today
2. **Note your context:** available hours, energy level (1–5), any key constraints (meetings, hard stops)
3. **Use the Daily Planning Prompt**
4. **Review and edit the output**
5. **Copy the finalised plan to a Notion Daily Note**
6. **Set a recurring calendar reminder**

### Step-by-Step

1. **Identify your top 3 priorities** by opening your Master Dashboard:
   - What is in "Today's Focus"?
   - What is due this week that hasn't moved to In Progress?
   - What is the single most important thing you could ship today?

2. **Note your planning context:**
   - Available focused hours today: ___
   - Energy level (1 = low, 5 = peak): ___
   - Any hard constraints (e.g., "I have a 2-hour call at 11am"): ___
   - The one thing I've been avoiding: ___

3. **Run the Daily Planning Prompt:**
   - Open [`prompt_library/daily_planning_prompts.md`](../../prompt_library/daily_planning_prompts.md)
   - Use the "Morning Planning Prompt" template
   - Fill in all placeholders with your real context
   - Submit to ChatGPT

4. **Review the AI output:**
   - Is the sequencing realistic given your energy pattern?
   - Is anything missing that you know you need to do?
   - Is the AI suggesting you do hard cognitive work during your lowest-energy period?
   - Edit until you'd actually commit to this plan

5. **Copy the finalised plan into a Notion Daily Note:**
   - Create a new page under a "Daily Notes" section called "[Today's Date] — Daily Plan"
   - Paste the plan
   - Add one line at the top: "Today I will feel good if I complete: [1 thing]"

6. **Set a recurring reminder:**
   - Calendar app → create recurring event: "Morning Planning (15 min)" — 8:30am or your preferred start time — every weekday

### Minimum Viable Task
- Top 3 priorities identified from dashboard
- Daily Planning Prompt run with real context
- AI output reviewed and edited
- Finalised plan copied to Notion Daily Note
- Recurring calendar reminder set

### Extension Task
- Try the "Energy-Aware Planning Prompt" variation — this asks ChatGPT to factor in your energy pattern when scheduling tasks
- Create a reusable Morning Planning template in Notion (a page template with the 5 input fields pre-filled)

### Deliverable
Completed Daily Note for today with a real, edited daily plan.

---

## Task 2A: Overload Triage + End-of-Day Reflection (Session 2 — 40 min)

**Objective:** Practice overload triage on your current task list, then complete your end-of-day reflection.

### Part A: Overload Triage (if your list has 10+ active tasks due this week)

1. **Copy your task list** (all tasks with due dates in the next 7 days) as a plain text list

2. **Run the Overload Triage Prompt:**
   - Open [`prompt_library/prioritization_prompts.md`](../../prompt_library/prioritization_prompts.md)
   - Use the "Overload Triage Prompt"
   - Include task list + your available hours this week + your top goals

3. **Review the AI triage output:**
   Each task should be classified as:
   - **Do Now** — must happen today/tomorrow, non-negotiable
   - **Schedule** — important, assign a specific future date
   - **Delegate** — could be done by someone else (note who)
   - **Drop** — remove from the list; low consequence

4. **Apply the decisions in Notion:**
   - Move "Schedule" tasks to new due dates
   - Archive "Drop" tasks (or mark as Cancelled)
   - Note "Delegate" tasks with a responsible party in the Notes field

5. **Document your triage decisions:**
   - Add a brief note in your Notion workspace: "Triage [date] — Dropped: X, Scheduled: Y, Delegated: Z"

### Part B: End-of-Day Reflection

1. Open the Daily Check-In template: [`reflection_templates/daily_checkin.md`](../reflection_templates/daily_checkin.md)
2. Complete all 6 questions honestly
3. Add at least 3 entries to your Anti-To-Do from today
4. Log today's work sessions in your Work Session Log

5. **Set a recurring end-of-day reminder:**
   - Calendar → recurring event: "End-of-Day Reflection (10 min)" — 5:30pm every weekday

### Minimum Viable Task

**Triage:**
- Run the Overload Triage Prompt (or document that your task count is manageable)
- Apply at least 2 triage decisions in Notion

**Reflection:**
- Day 4 Daily Check-In completed
- Anti-To-Do updated with 3+ entries
- Work Session Log updated

### Deliverable
Completed Day 4 Daily Check-In + triage decisions documented in Notion.

---

## Task 3A: Weekly Review + System Retrospective (Session 3 — 35 min)

**Objective:** Run your first complete weekly review and a system retrospective on your 4-day-old productivity OS.

### Part A: Weekly Review (20 min)

Use the 6-step weekly review sequence:

**Step 1 — Clear the decks** (5 min)  
Close all tabs except Notion. Mark your email as "read" or process to zero. You're doing a clean review.

**Step 2 — Review your Anti-To-Do** (3 min)  
Read through all entries from the past 4 days. What did you actually ship?

**Step 3 — Review open tasks** (4 min)  
Which tasks from this week are not done?  
- For each: Was it blocked externally, or was it avoided?
- Note the honest reason

**Step 4 — Review active projects** (4 min)  
Which projects moved forward? Which stalled?  
- For any stalled project: what is the specific blocker?

**Step 5 — Check attention allocation** (2 min)  
Look at your Work Session Log for the past 4 days. Which category got the most time? Does it match your ideal?

**Step 6 — Set next week's outcomes** (2 min)  
Write 3 outcomes for next week — specific, achievable:  
1. ___  
2. ___  
3. ___

Then run the Weekly Review Prompt:
- Open [`prompt_library/review_prompts.md`](../../prompt_library/review_prompts.md)
- Use the "Weekly Review Prompt"
- Input your anti-to-do entries, open tasks, and attention allocation
- Read the AI summary and any recommendations

### Part B: System Retrospective (15 min)

Answer these 4 questions in writing (a Notion note is fine):

1. **What parts of my system did I actually use this week?**  
   (List the specific databases, views, or rituals you engaged with)

2. **What parts did I set up but not use?**  
   (Be honest — there's always at least one)

3. **What is the weakest link in my current workflow?**  
   (The part most likely to break down in week 2)

4. **What is the one concrete change I will make to improve the system?**  
   (Must be specific: "I will add X" or "I will change Y from A to B")

Then run the retrospective prompt:
- Open [`prompt_library/system_optimization_prompts.md`](../../prompt_library/system_optimization_prompts.md)
- Use the "System Retrospective Prompt"
- Describe your system and what you used vs. ignored
- Read the AI's friction analysis

**Implement your one concrete change** in your Notion workspace now, before the capstone.

**Schedule your next retrospective:**
- Calendar → recurring every 4 weeks: "System Retrospective (20 min)"

### Minimum Viable Task
- All 6 weekly review steps completed
- 3 outcomes set for next week
- Written retrospective (4 questions answered)
- One concrete improvement implemented in Notion
- Next retrospective scheduled

### Deliverable
Completed Weekly Review note + Retrospective note with documented improvement in Notion.

---

## Before Your Capstone Presentation

Submit the following before the afternoon session:

- [ ] Notion link (view-only) OR screenshot of your workspace
- [ ] Capstone Written Walkthrough (6 questions, in [`capstone_instructions.md`](../capstone_instructions.md))
- [ ] At least one completed Weekly Review template

### 10-Minute Pre-Presentation Checklist Walkthrough

1. **Open your Master Dashboard** — run the 5-second load test
2. **Confirm your Goals Database** has 3+ goals with success criteria
3. **Confirm your Projects** have milestones and are linked to goals
4. **Confirm your Task Database** has priority tiers and a "This Week" view
5. **Confirm your Anti-To-Do** has real entries
6. **Confirm your Kanban** has tasks in multiple stages
7. **Confirm your Streak Tracker** is linked to the dashboard
8. **Confirm you have a Daily Note** from today's planning session
9. **Open your Retrospective note** — know the one thing you'd change

---

## Day 4 End-of-Day Checklist

- [ ] Daily planning session completed + stored in Notion Daily Note
- [ ] Recurring morning planning reminder set
- [ ] Overload triage completed (or confirmed not needed)
- [ ] End-of-day recurring reminder set
- [ ] Day 4 Daily Check-In completed
- [ ] Weekly Review completed (6 steps)
- [ ] System Retrospective completed (4 questions + 1 improvement implemented)
- [ ] Capstone materials submitted
- [ ] Capstone presentation delivered

---

## Prompt References Used Today

| Task | Prompt File | Prompt Name |
|------|------------|-------------|
| 1A | `daily_planning_prompts.md` | Morning Planning Prompt |
| 1A (Extension) | `daily_planning_prompts.md` | Energy-Aware Planning Prompt |
| 2A | `prioritization_prompts.md` | Overload Triage Prompt |
| 3A (Weekly Review) | `review_prompts.md` | Weekly Review Prompt |
| 3A (Retrospective) | `system_optimization_prompts.md` | System Retrospective Prompt |
