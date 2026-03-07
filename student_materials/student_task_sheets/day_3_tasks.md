# Day 3 Task Sheet

## Building a Personal Productivity System with AI

**Date:** Day 3  
**Theme:** Dashboard — Kanban, Streaks & UX Audit  
**Your goal today:** Build a Master Dashboard that makes your entire productivity system navigable from a single page.

---

### Before You Start

Make sure you have from Days 1–2:
- [ ] Goals Database: 3+ goals
- [ ] Projects Database: 2+ projects with milestones
- [ ] Task Database: 10+ tasks with priority tiers
- [ ] Anti-To-Do Log: 5+ entries
- [ ] Work Session Log: 5+ sessions
- [ ] Attention Budget documented

If anything is missing, use the first 15 minutes to backfill it.

---

## Task 1A: Build Your Kanban Board (Session 1 — 35 min)

**Objective:** Set up a Kanban board view of your Task Database with meaningful workflow stages.

### Kanban Stage Reference

| Stage | What Goes Here |
|-------|---------------|
| Backlog | Captured tasks, not yet scheduled |
| This Week | Committed tasks for the current week |
| In Progress | Actively being worked on (max 3) |
| Blocked | Cannot move — waiting on external input |
| Done | Completed (archive or review weekly) |

You may rename or add stages to match your actual workflow.

### Step-by-Step

1. **Open your Task Database**
2. **Add a new view:** Click "+ Add a view" → select "Board"
3. **Group by:** Status property
4. **Edit Status options** to match your workflow stages:
   - Rename/add options to match the reference above (or your custom stages)
   - Assign emoji if helpful (e.g., 🔴 Blocked)
5. **Sort your tasks:** Drag each task card to the correct stage based on its real current status
6. **Add a WIP limit reminder:**
   - Create a Callout block above your Kanban view
   - Write: "⚠️ In Progress limit: 3 — if you're adding a 4th, something must move to Done first"
7. **Create a filtered Kanban view called "Active Work":**
   - Filter out Backlog (too noisy) and Done (use for review only)
   - This is your daily working view

### What to look at when you're done
- Is anything in Blocked? What would unblock it?
- Does In Progress have more than 3 cards? That's your WIP violation to resolve.
- Does Backlog look overwhelming? That's your signal for the overload triage prompt.

### Minimum Viable Task
- Task Database has a Board view with 4+ workflow stages
- Tasks are sorted into appropriate columns
- WIP limit reminder added
- "Active Work" filtered view created

### Extension Task
- Try grouping by Priority instead of Status — what does this reveal about how your work is distributed?
- Use the "Kanban Design Prompt" in [`prompt_library/system_optimization_prompts.md`](../../prompt_library/system_optimization_prompts.md) to get suggestions for custom stages specific to your work type

### Deliverable
Task Database in Board view with 4+ stages, tasks distributed, WIP limit visible.

---

## Task 2A: Build Your Master Dashboard (Session 2 — 35 min)

**Objective:** Create a single Notion page that aggregates your most important system views.

### Dashboard Sections (Minimum)

| Section | Source Database | Filter |
|---------|----------------|--------|
| Today's Focus | Tasks | Due = today OR Priority = Critical |
| This Week | Tasks | Due ≤ +7 days, sort Priority H→L |
| Active Projects | Projects | Status = Active |

### Step-by-Step

1. **Create a new Notion page** at the top level of your workspace
   - Name it: "🏠 [Your Name]'s Mission Control"
   - This is your new home page

2. **Add a header callout block:**
   - "Productivity Dashboard | Today: [today's date]"

3. **Create a 2-column layout** (drag content blocks side by side)

4. **Add "Today's Focus" linked database (Column 1, top):**
   - Click "+ Add linked database" → select your Task database
   - Rename the view: "Today's Focus"
   - Filter: Due Date = Today OR Priority = Critical
   - Show only: Task Name + Status (hide all other properties)

5. **Add "Active Projects" linked database (Column 1, below):**
   - Link to Projects database
   - Filter: Status = Active
   - View type: Gallery or List

6. **Add "This Week" linked database (Column 2):**
   - Link to Task database
   - Filter: Due Date ≤ +7 days
   - Sort: Priority high → low
   - View type: Table

7. **Add "Anti-To-Do: Today" linked database (Column 2, below):**
   - Link to Anti-To-Do database
   - Filter: Date = today

8. **Pin or favourite this page** so it's your Notion home

### The 5-Second Test
Open your dashboard from a new tab. Time yourself: can you find your most important task within 5 seconds?

### Minimum Viable Task
- Master Dashboard page titled and accessible
- At least 3 linked views created
- At least 2 sections in a 2-column layout
- Dashboard is set as your Notion home (pinned or favourited)

### Extension Task
- Add a "Quick Capture" toggle block at the top of your dashboard for fast inbox items
- Add an "Inbox" note section for things that need to be processed later
- Use the Dashboard UX Audit Prompt in [`prompt_library/system_optimization_prompts.md`](../../prompt_library/system_optimization_prompts.md) to get AI feedback on your layout

### Deliverable
Master Dashboard page with at least 3 linked views and functional layout.

---

## Task 3A: Build Your Streak Tracker (Session 3 — 30 min)

**Objective:** Track 2–3 daily process habits using a Notion database linked to your dashboard.

### What to Track (choose your 2–3)

Think: process habits, not outcome targets.

**Good streak habits:**
- ✅ Completed morning planning
- ✅ Updated Anti-To-Do (at least 1 entry)
- ✅ Logged at least 1 work session
- ✅ Completed end-of-day reflection
- ✅ Reviewed dashboard at day start

**Avoid tracking:**
- ❌ "Worked on Project A for 4 hours" (outcome, not process)
- ❌ "Completed 5 tasks" (outcome target — varies with life)

### Step-by-Step

1. **Create a "Streak Tracker" database in Notion:**
   - Properties: Date (Date) | Habit (Select) | Completed (Checkbox) | Notes (Text, optional)
   - Add your 2–3 habit options in the Habit Select property

2. **Add today's entries:**
   - One row per habit (e.g., if you track 3 habits, add 3 rows for today)
   - Check the Completed box for any habit you've already done today

3. **Create a Streak Tracker view:**
   - Filter: Date ≥ [today minus 14 days] (last 2 weeks)
   - Sort: Date descending
   - View type: Table

4. **Add your Streak Tracker to your Master Dashboard:**
   - Link the Streak Tracker database to your Mission Control page
   - Place it in a visible location (below the fold is fine)

5. **Backfill (optional but recommended):**
   - Add entries for the past 3 days with honest estimates (Did you do morning planning on Monday? Tuesday?)

### Minimum Viable Task
- Streak Tracker database created with 2–3 habits defined
- Today's entries added (one row per habit)
- Streak view linked to Master Dashboard

### Extension Task
- Backfill the last 5 days honestly
- Identify: which habit do you most consistently skip? What's getting in the way?
- Use the "Habit Design Prompt" in [`prompt_library/system_optimization_prompts.md`](../../prompt_library/system_optimization_prompts.md) to get suggestions for which habits to track based on your goals

### Deliverable
Streak Tracker with 2–3 habits, today's entries, and view linked to Master Dashboard.

---

## Task 4A: Dashboard UX Audit (Session 4 — 25 min)

**Objective:** Evaluate and improve your dashboard's usability using a structured self-audit and AI feedback.

### UX Audit Questions

Answer each question honestly before using AI feedback:

1. **Load Test:** Open your dashboard from a blank Notion screen. Time from click to "I know what to do today." Is it ≤ 5 seconds?

2. **Noise Check:** Is there any section you already know you'll ignore most days? _(Be honest — it's okay to remove something you added)_

3. **Click Count:** Pick a specific task. How many clicks does it take to open it from the dashboard? _(Target: ≤ 3 clicks)_

4. **Label Clarity:** Are all your linked views clearly named? Could someone else understand what each section is for without explanation?

5. **Emotional Check:** Does opening this dashboard feel like relief (clarity) or dread (overwhelm)?

### Step-by-Step

1. **Self-audit:** Answer the 5 questions above. Write your answers in a brief Notion note or directly in this task sheet.

2. **Run the Dashboard UX Audit Prompt:**
   - Open [`prompt_library/system_optimization_prompts.md`](../../prompt_library/system_optimization_prompts.md)
   - Use the "Dashboard UX Audit Prompt"
   - Describe your dashboard layout (section names, what they show, how they're arranged)
   - Submit to ChatGPT

3. **Implement at least 2 changes from the AI feedback:**
   - Remove a redundant section
   - Rename an unclear view
   - Reorder sections to surface the most important view first
   - Hide a property from a linked view that's adding noise

4. **Document your changes:**
   - Add a brief note to your dashboard (or a Callout block): "Updated [date] — removed [X], renamed [Y]"

### Minimum Viable Task
- Self-audit completed (5 questions answered, even briefly)
- At least 2 UX changes implemented based on AI feedback or your own audit

### Deliverable
Refined Master Dashboard with at least 2 documented UX improvements.

---

## Day 3 End-of-Day Checklist

- [ ] Kanban Board: 4+ stages, tasks sorted, WIP limit visible
- [ ] Master Dashboard: 3+ linked views in a 2-column layout
- [ ] Streak Tracker: 2–3 habits, today's entries, linked to dashboard
- [ ] Dashboard UX: 2+ improvements implemented
- [ ] Daily Check-In completed (see [`reflection_templates/daily_checkin.md`](../reflection_templates/daily_checkin.md))
- [ ] Reviewed capstone instructions for tomorrow (see [`capstone_instructions.md`](../capstone_instructions.md))

---

## Prompt References Used Today

| Task | Prompt File | Prompt Name |
|------|------------|-------------|
| 1A (Extension) | `system_optimization_prompts.md` | Kanban Design Prompt |
| 2A (Extension) | `system_optimization_prompts.md` | Dashboard UX Audit Prompt |
| 3A (Extension) | `system_optimization_prompts.md` | Habit Design Prompt |
| 4A | `system_optimization_prompts.md` | Dashboard UX Audit Prompt |
