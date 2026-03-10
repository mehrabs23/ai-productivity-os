# Day 3 Task Sheet — Workshop Handout

## Building a Personal Productivity System with AI

**Day:** Day 3  
**Theme:** Operationalizing Your Life OS — Dashboards, Workflow, Reminders, and Daily Check-ins  
**Your goal today:** Build a Life OS you can actually open and use tomorrow morning.

---

## Before You Start — Which Track Are You On?

> ### 🟢 Track A — Continuing from Days 1 & 2
> **Use this track if you have:**
> - Goals database with 2+ goals
> - Projects database with 1+ active projects
> - Tasks database with 10+ tasks and Due Dates set
> - Area / Life Domain property on your Task database
>
> **→ Start at Task 1 below. Skip the Track B callouts.**

> ### 🟡 Track B — Starting Fresh (Latecomer / No Prior Setup)
> **Use this track if you:**
> - Missed Days 1 and/or 2
> - Have a blank Notion workspace
> - Have incomplete task data (fewer than 5 tasks, no due dates set, no Area property)
>
> **→ Before doing ANYTHING on this sheet, complete the Minimum Setup Path:**
> [`templates/day_3_minimum_setup_path.md`](../../templates/day_3_minimum_setup_path.md)
> It takes 20–30 minutes and gives you exactly what you need to participate in all Day 3 activities.
> **Then return here and follow the Track B callouts in each task below.**
>
> ⚠️ You do NOT need Goals or Projects databases to participate today.
> One Tasks database with 8–10 tasks is enough for everything in Day 3.

---

## Task 1 — Audit and Triage (Session 1 — 15 min)

**Objective:** Ensure your Life OS has real data before you build on top of it.

**Estimated time:** 15 minutes

> **🟡 Track B:** You already completed this setup via the Minimum Setup Path. Proceed directly to Task 2.
> Quick confirmation: does your Tasks database have 8+ tasks, 2+ life areas, and at least 1 task with a due date in the past? If yes — you're ready.

### What to do (Track A)

1. Open your Task Database in Notion
2. Confirm you have tasks in at least 2 different life areas (work + at least one of: personal, studies, content, health, admin)
3. Look for tasks missing a Due Date — add a date to at least 5 of them now
4. Check if you have an "Area" or "Life Domain" property on your task database. If not, add a Select property with these options: Work / Studies / Personal / Content / Health / Admin / Finance
5. Assign Area values to your 10 most important tasks

### What success looks like
- 10+ tasks, at least 2 life areas represented, 5+ tasks with Due Dates, Area property exists

### Common mistakes
- Only having work tasks (your Life OS should represent your whole life)
- Tasks without dates (they can't power your reminder views)

---

## Task 2 — Build Your Life OS Kanban (Session 2 — 30 min)

**Objective:** Create a visual workflow board across all life areas using a unified set of status values.

**Estimated time:** 30 minutes

> **🟡 Track B:** Follow all steps exactly as written. Your minimum setup already has the correct 6 Status values. Start at Step 1.

### Your 6 Status Values (set these exactly)

| Status | What Goes Here |
|--------|---------------|
| Inbox | Captured but not yet processed |
| Planned | Acknowledged, not yet scheduled |
| This Week | Committed for this week |
| In Progress | Actively working on (max 3 at once) |
| Waiting / Blocked | Can't move — waiting on someone or something |
| Done | Completed |

### Step-by-Step

1. **Open your Task Database**
2. **Click "+ Add a view"** → choose **Board**
3. **Set "Group by" to:** Status
4. **Edit your Status property options** (via the property settings, not the view):
   - Remove any old options that don't match the 6 values above
   - Add the 6 values, assign different colors so each column is visually distinct
5. **Move your tasks** into the correct columns based on their real current state
   - Anything unscheduled = Inbox or Planned
   - Anything you're actively working on = In Progress (max 3!)
   - Anything blocked = Waiting / Blocked
6. **Create a filtered view called "Active":**
   - Click "Filter" on the board view
   - Add filter: Status ≠ Inbox
   - Add filter: Status ≠ Done
   - Rename the view: "Active Work"
7. **Add a WIP limit callout above the board:**
   - Press `/` → type "Callout" → select it
   - Write: "🎯 In Progress limit: 3. Adding a 4th? Something must move first."

### What success looks like
- Board view exists with 6 status columns in distinct colors
- Tasks from 2+ life areas visible on the board
- "Active Work" filtered view excludes Inbox and Done
- WIP callout visible above the board

### Common mistakes
- Only work tasks on the Kanban (your personal and study tasks should be here too)
- 5+ tasks in "In Progress" at once (this defeats the purpose — be honest about what's truly active)
- Forgetting to create the "Active" filtered view (the main board is too noisy without it)

### Stretch version
Create a second Board view grouped by "Area / Life Domain" — this shows you which life area has the most open work and which is neglected.

### Deliverable
Task Database Board view with 6 statuses, tasks from 2+ areas, "Active Work" filtered view, WIP callout.

---

## Task 3 — Build Your Life OS Dashboard (Session 3 — 40 min)

**Objective:** Build a single Notion page that shows your full life system at a glance.

**Estimated time:** 40 minutes

> **🟡 Track B:** Follow all steps exactly as written. When the steps refer to Goals or Projects databases:
> - Skip the "Active Projects" section — you don't have a Projects database yet
> - Skip any step asking you to link the Goals database
> - Everything else (Kanban, Today, Overdue, Due Soon, This Week, Completed Recently, Check-In, Weekly Status) works exactly the same with only a Tasks database
>
> Your dashboard will have all the core views and will work identically to Track A learners for all Day 3 activities.

### Required Dashboard Sections (build in this order)

| Section | Purpose |
|---------|---------|
| 📝 Daily Check-In (toggle) | First thing you see each day |
| 🎯 Today | Tasks due/prioritized for today |
| ⚠️ Overdue | Tasks where due date is past |
| 🔔 Due Soon | Tasks due in next 3 days |
| 📅 This Week | Tasks due within 7 days |
| 🗂️ Kanban — Active | Embedded board view |
| ✅ Completed Recently | Tasks done in last 7 days |
| 📊 Weekly Status | Progress summary for the week |

### Step-by-Step

**A. Create the page:**
1. In Notion, click "+ New page" in the sidebar
2. Name it: `[emoji] [Your Name]'s Life OS` (e.g., "🏠 Alex's Life OS")
3. Click the **•••** at the top → enable **"Full width"**
4. Click the smiley face icon area → add an emoji icon (e.g., 🏠 or 🧠)
5. Click "Add cover" → choose a cover from Notion's free library (or leave as solid color — add your own screenshot later)

**B. Add a header callout:**
1. Press `/` → type "Callout" → select
2. Write: `Life OS | [Today's date] | [Your main life areas]`
3. Give it a color that feels motivating (blue, purple, or teal recommended)

**C. Create column layout:**
1. Type a title: "🎯 Today" as a Heading 2
2. Below it, add a linked database: press `/` → "Linked view of database" → select your Task database
3. Rename the view "Today"
4. Filter: Due Date = Today — OR — Status = In Progress
5. Hide all properties except: Task Name, Status, Area
6. Hover to the right edge of that block until you see a blue line → drag another block to sit beside it (creates 2-column layout)

**D. Add remaining views (in each column or below):**
- **Overdue:** Link Task DB → Filter: Due Date before Today AND Status ≠ Done
- **Due Soon:** Link Task DB → Filter: Due Date next 3 days AND Status ≠ Done
- **This Week:** Link Task DB → Filter: Due Date within 7 days → Sort: Priority high→low
- **Active Kanban:** Link Task DB → Board view → use your "Active Work" filter
- **Completed Recently:** Link Task DB → Filter: Status = Done AND Date modified ≥ 7 days ago
- **Weekly Status:** Heading 2, then a text block with prompts (see Task 6 below)

**E. Set as home page:**
- Right-click your dashboard page in the sidebar → "Set as default page" (or pin it to the top)

### The 5-Second Test
Close Notion. Open it again. Navigate to your dashboard. Start a timer.  
**Can you see your top priority within 5 seconds?**  
If not: move the "Today" section higher. Remove one section that doesn't answer an urgent question.

### What success looks like
- Dashboard has icon, cover, full-width layout
- 5+ linked views, at least 2 columns
- Shows data from real tasks (not empty)
- Set as your Notion home

### Common mistakes
- Too many sections (more than 9 = scroll fatigue — pick the most useful)
- Table view for everything (mix list, gallery, board views for readability)
- Forgetting to apply filters (a linked database without a filter shows everything — too noisy)
- Aesthetics before data (choose a cover *after* the views are working)

### Stretch version
Add a "navigation bar" using buttons or text links at the very top of the page to jump to each section quickly.

### Deliverable
Life OS Dashboard: icon, cover, full-width, 5+ linked views in 2-column layout, set as Notion home.

---

## Task 4 — Set Up Reminder Views (Session 4 — 20 min)

**Objective:** Make your dashboard actively surface what's urgent and overdue.

**Estimated time:** 20 minutes

> **🟡 Track B:** If you used the Minimum Setup Path, the Reminder Date property already exists. Skip Step 2. Start at Step 3 — set 2 reminders on tasks you added.

### Step-by-Step

1. **Open your Task database** (the main database, not a view)
2. **Add "Reminder Date" property:**
   - Click "+ Add a property" → choose Date
   - Name it: "Reminder Date"
   - This is the date when you want to be reminded, *before* the due date
3. **Set at least 2 Notion reminders on real tasks:**
   - Open a task → click the Due Date field → click the date → toggle the reminder option
   - Set to "1 day before" or "2 days before"
   - Notion will send you a push notification (make sure Notion notifications are enabled)
4. **Verify your "Due Soon" view works:**
   - Open the Due Soon view → confirm it shows tasks due in the next 3 days
   - If it's empty: add due dates to tasks first (go back to Task 1)
5. **Verify your "Overdue" view works:**
   - Open the Overdue view → confirm it shows tasks where due date is in the past and Status ≠ Done
   - Sort by Due Date ascending (earliest overdue at top)
6. **Confirm both views are visible on your dashboard**

### What success looks like
- Reminder Date property exists on Task database
- 2+ tasks have Notion reminders set
- Due Soon view shows real upcoming tasks (not empty)
- Overdue view shows real overdue tasks (if any) or "0" if all dates are current

### Common mistakes
- Tasks have no Due Dates → views show nothing (add dates first)
- Due Soon shows 14+ days ahead (too wide — keep at 3–5 days max)
- Overdue view not sorted (hardest overdue tasks should be at the top)

### Stretch version
Add a third reminder view: "Reminder Date = Today" — tasks where your self-set Reminder Date is today.

### Deliverable
Reminder Date property added. 2+ Notion reminders set. Due Soon and Overdue views working and visible on dashboard.

---

## Task 5 — Create Your Daily Check-In Routine (Session 5 — 20 min)

**Objective:** Build a daily check-in ritual inside your Life OS Dashboard.

**Estimated time:** 20 minutes

### Step-by-Step

1. **Go to the top of your Life OS Dashboard**
2. **Add a toggle block:**
   - Press `/` → type "Toggle" → select "Toggle List"
   - Name it: `📝 Daily Check-In — [Today's Date]`
3. **Inside the toggle, add these 5 questions as text lines:**
   ```
   1. What are my top 3 priorities today?
   
   2. Is there anything overdue I need to handle first?
   
   3. Was there anything I avoided yesterday? Do I need to move it today?
   
   4. My energy level today: /5
   
   5. What would make today feel complete?
   ```
4. **Fill it in right now** (this is your first real check-in — do it for real, not as a test)
5. **Move the toggle above the "Today" view** (it should be the very first thing on the page)
6. **Optional:** If you prefer, create a separate "Daily Log" database instead of a toggle — Date, Priorities, Reflections, Energy

### What success looks like
- Check-in toggle is at the top of the dashboard (not buried below the fold)
- Questions are clear and quick to answer (under 5 minutes)
- You have filled it in for today

### Common mistakes
- Making the check-in a 20-question journal entry (it becomes a barrier instead of a ritual)
- Placing it below the fold (out of sight = out of habit)
- Not actually completing it today (this is a habit — it starts today)

### Stretch version
Create a standalone "Daily Log" database with: Date (Date), Top 3 (Text), Energy (Number 1–5), One Thing I Avoided (Text). Link it to the dashboard.

### Deliverable
Daily Check-In toggle at the top of your dashboard, filled in for today.

---

## Task 6 — Build Weekly Status Section (Session 6 — 20 min)

**Objective:** Add a Weekly Status section to your dashboard for progress visibility and weekly review preparation.

**Estimated time:** 20 minutes

### Step-by-Step

1. **Scroll to the bottom of your Life OS Dashboard**
2. **Add a Heading 2:** `📊 Week in Review`
3. **Add "Completed This Week" linked view:**
   - Link Task database
   - Filter: Status = Done AND (Date filter: within this week)
   - View: List (compact)
   - Rename: "✅ Completed This Week"
4. **Add a Weekly Status text block below the linked view:**
   ```
   **Week of:** 
   
   **Wins this week:**
   - 
   
   **Still in progress / carried over:**
   - 
   
   **What I'm re-prioritising:**
   - 
   
   **Focus for next week:**
   - 
   ```
5. **Fill in "Wins this week"** right now with anything you've completed since Monday
6. **Optional:** Add "Still Open from Last Week" = Overdue view (reuse the one you built in Task 4)

### What success looks like
- "Completed This Week" view shows real tasks from this week
- Weekly Status text template is filled in (at least partially)
- Someone reading this section could understand your week's progress in under 2 minutes

### Common mistakes
- Not filtering by "this week" (shows all completed tasks ever — misleading)
- Leaving the status template blank (the data alone doesn't tell the story)
- Making it too long (5 lines per section max — this is a summary, not a report)

### Stretch version
Add a "Next Week Focus" section below with 3 lines for next week's priorities — makes the weekly review transition smoother.

### Deliverable
Weekly Status section at bottom of dashboard with "Completed This Week" view and filled-in status template.

---

## Task 7 — Simulate Your First Day in the Life OS (Session 7 — 15 min)

**Objective:** Walk through your system as if it's tomorrow morning.

**Estimated time:** 15 minutes

### The Simulation Steps

Do this as if it's 8:30am tomorrow:

1. Open your dashboard (only the dashboard — no sidebar navigation)
2. Open your Daily Check-In toggle → fill in tomorrow's version
3. Scan "Today" → pick your #1 priority → open it
4. Glance at "Overdue" → anything to address before starting?
5. Check "Due Soon" → anything to move to "This Week" status?
6. Look at your Kanban Active view → is everything in the right column?
7. Capture one new task that comes to mind → make sure it lands in "Inbox" status

### Debrief (write or discuss):
- How long did the morning scan take?
- What felt natural? What felt awkward?
- What one layout change would make this faster?

### Deliverable
Completed the simulation. One layout change noted and applied.

---

## Day 3 End-of-Day Checklist

Use the detailed completion checklist in [`student_materials/day_3_completion_checklist.md`](../day_3_completion_checklist.md).

Quick summary:

- [ ] Life OS Kanban — 6 statuses, 2+ life areas, "Active Work" filtered view
- [ ] Life OS Dashboard — icon, cover, full-width, 5+ linked views
- [ ] Due Soon and Overdue views — working and visible in dashboard
- [ ] Reminders set on 2+ tasks
- [ ] Daily Check-In — built and completed for today
- [ ] Weekly Status — built and partially filled for this week
- [ ] Completed the Day-in-the-Life simulation
- [ ] Day 3 Daily Check-In reflection written

---

## Prompt References for Day 3

| Task | Prompt File | Prompt Name |
|------|------------|-------------|
| 1 (Triage) | `prompt_library/task_breakdown_prompts.md` | Task Breakdown Prompt |
| 2 (Kanban — Extension) | `prompt_library/system_optimization_prompts.md` | Kanban Design Prompt |
| 3 (Dashboard — Extension) | `prompt_library/system_optimization_prompts.md` | Dashboard UX Audit Prompt |
| 5 (Check-In — Extension) | `prompt_library/daily_planning_prompts.md` | Daily Check-In Design Prompt |
