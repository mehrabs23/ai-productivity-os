# Day 3 Life OS Dashboard Build Guide

## Building a Personal Productivity System with AI

**Purpose:** A step-by-step, beginner-safe guide to building the Day 3 Life OS Dashboard in Notion. Follow this guide in order. Each section builds on the previous one.

---

## Before You Start — Which Track Are You On?

> ### 🟢 Track A — Continuing from Days 1 & 2
> **You have:** Goals database, Projects database, Tasks database from Days 1–2, plus Area / Life Domain property and at least 5 tasks with Due Dates.
>
> ✅ Proceed directly to **Section A: Page Setup** below.

> ### 🟡 Track B — Starting Fresh (Latecomer / No Prior Setup)
> **You have:** A blank Notion workspace OR an incomplete setup (no Goals/Projects database, fewer than 5 tasks, no Due Dates or Area property).
>
> **→ Before opening this guide, complete the Minimum Setup Path first:**
> [`templates/day_3_minimum_setup_path.md`](day_3_minimum_setup_path.md)
>
> It takes 20–30 minutes. When you return, follow the instructions in this guide exactly — **except Section C (Goals/Projects/Active Areas), which is marked optional for Track B**.
>
> ⚠️ You do NOT need Goals or Projects databases to complete Day 3. One Tasks database with 8–10 real tasks is enough for all Day 3 views and activities.

---

## Section A: Page Setup

### Purpose
Create the container for your Life OS Dashboard. This is the single most important page in your Notion workspace.

### Exact Steps

**A1. Create the page**
1. In Notion, click "+ New page" in the left sidebar
2. The page opens with a blank title field
3. Type your dashboard name (see naming guidance below)

**A2. Name your dashboard**
- Format: `[emoji] [Your Name]'s Life OS`
- Examples: `🏠 Alex's Life OS`, `🎓 Sam's Life OS`, `🧠 Priya's Creator OS`
- Choose a name that feels personal — you will open this every day

**A3. Enable full-width layout**
1. Click **•••** in the top-right corner of the page
2. Toggle on **"Full width"**
3. The page will expand to fill the screen — much better for dashboards

**A4. Add an icon**
1. Hover over the page title
2. Click "Add icon" that appears above the title
3. Choose an emoji that represents your system (e.g., 🏠 🧠 🎯 ✨)
4. Click the emoji to change it at any time

**A5. Add a cover**
1. Hover over the title area
2. Click "Add cover"
3. Notion will show a random image — click "Change cover" to choose
4. Select from Notion's gallery (Artworks, Colors, or Gradients are recommended for dashboards)

> **⚠️ Screenshot note:** Add your own original cover or screenshot later from your real workspace. Do not use covers from external tutorials. A solid color (Light Gray or Soft Blue) is perfectly fine for now.

### Example Setup
- Icon: 🏠
- Cover: Notion gallery → Gradients → Soft blue gradient
- Name: "🏠 Alex's Life OS"

### Common Mistakes
- Not enabling full-width (page looks cramped — hard to build columns)
- Spending too long on the cover before data is in the views
- Using a screenshot from someone else's workspace (use your own)

### What Success Looks Like
A full-width page with an icon, a cover, and a clear, personal title — ready to receive content.

---

## Section B: Main Tasks / Workflow Database

### Purpose
Set up or update your Task database with the unified Life OS workflow before linking it to the dashboard. The views you create here are what the dashboard will surface.

### B1. Standardize the Status Property

**Why:** All dashboard views filter by Status. If your statuses are inconsistent, your filters won't work.

**Steps:**
1. Open your Task database (not a view, the actual database page)
2. Click the "Status" column header → "Edit property"
3. Delete any existing options that don't match the 6 Life OS values
4. Add these 6 status values with the following colors:
   - **Inbox** → Grey
   - **Planned** → Blue
   - **This Week** → Yellow
   - **In Progress** → Purple
   - **Waiting / Blocked** → Orange
   - **Done** → Green

**Common mistakes:**
- Editing status options in the view instead of the property (won't affect other views)
- Using different names (e.g., "Backlog" instead of "Inbox") — stick to the 6 values for consistency

### B2. Add Reminder Date Property

**Steps:**
1. In your Task database, click "+ Add a property"
2. Choose "Date" type
3. Name it exactly: `Reminder Date`
4. Optional: add a description "Reminded before due date"

### B3. Confirm Area / Life Domain Property

1. Check if "Area" or "Life Domain" property exists on Tasks
2. If not: click "+ Add a property" → Select → name it: `Area / Life Domain`
3. Add values: Work / Studies / Personal / Content / Health / Admin / Finance

### B4. Build the Kanban (Board View)

1. In the Task database, click "+ Add a view"
2. Select "Board"
3. Confirm grouping is "Status"
4. This is your base Kanban view

### B5. Create "Active Work" Filtered Kanban View

1. In the Board view, click "Filter"
2. Add filter: Status does not equal "Inbox"
3. Add second filter: Status does not equal "Done"
4. Rename the view: "Active Work"
5. This is the Kanban view you'll embed in the dashboard

### B6. Create "Today" View

1. Click "+ Add a view" → choose "List"
2. Rename it: "Today"
3. Click "Filter" → Add filter: Due Date → "is" → "today"
4. Add OR filter: Status = "In Progress"
5. Sort: Priority high to low
6. Properties: show Task Name, Status, Area only (hide everything else)

### B7. Create "This Week" View

1. Click "+ Add a view" → choose "Table"
2. Rename it: "This Week"
3. Filter: Due Date → "is within" → "the next 7 days"
4. Add filter: Status → "is not" → "Done"
5. Sort: Priority high to low, Due Date ascending
6. Properties: show Task Name, Due Date, Priority, Status, Area

### B8. Create "Due Soon" View

1. Click "+ Add a view" → choose "List"
2. Rename it: "Due Soon"
3. Filter: Due Date → "is within" → "the next 3 days"
4. Add filter: Status → "is not" → "Done"
5. Sort: Due Date ascending
6. Properties: show Task Name, Due Date, Area, Priority

**Why 3 days?** 3 days gives you time to act before things become overdue. 7 days shows too much and becomes noise.

### B9. Create "Overdue" View

1. Click "+ Add a view" → choose "List"
2. Rename it: "Overdue"
3. Filter: Due Date → "is before" → "today"
4. Add filter: Status → "is not" → "Done"
5. Sort: Due Date ascending (earliest overdue at top)
6. Properties: show Task Name, Due Date, Status, Area

**Common mistakes:**
- Not adding the Status ≠ Done filter (completed tasks show as overdue even after finishing)
- Sorting descending instead of ascending (hides the most urgent overdue tasks)

### B10. Create "Completed Recently" View

1. Click "+ Add a view" → choose "List"
2. Rename it: "Completed Recently"
3. Filter: Status = "Done"
4. Add filter: Last Edited → "is within" → "the past 7 days"
5. Sort: Last Edited descending
6. Properties: show Task Name, Area

### What Success Looks Like
Your Task database has:
- 6 standardized Status values with colors
- Reminder Date property exists
- Area / Life Domain property exists
- 6 named filtered views ready for embedding in the dashboard

---

## Section C: Goals / Projects / Active Areas *(Track A — Optional for Track B)*

### Purpose
Surface your active commitments across all life areas so you don't lose track of bigger-picture work.

> **🟡 Track B:** Skip this section. You don't have a Projects or Goals database yet. This section is for learners who completed Days 1–2. You can add these databases after the session using the Day 1–2 materials.

### Steps (Track A only)

**C1. Create a filtered "Active Projects" view in your Projects database:**
1. Open your Projects database
2. Click "+ Add a view" → choose "Gallery" or "List"
3. Filter: Status = "Active"
4. Sort: Priority high to low
5. Properties: show Name, Area, Priority, Deadline
6. Rename: "Active Projects"

**C2. (Optional) Create an "Active Goals" view:**
1. Open your Goals database
2. Click "+ Add a view" → choose "Gallery"
3. Filter: Status = "Active"
4. Properties: Name, Area, Deadline, Priority
5. Rename: "Active Goals"

### What Students Should See
When they look at the Active Projects/Areas section of the dashboard, they should see 2–6 cards representing real active commitments across different life areas — not a list of everything they've ever thought about doing.

### Common Mistakes
- Showing "Archived" or "Paused" items (add the Status = Active filter)
- Showing too many cards (if more than 8 show up, tighten the filter — are they really all active?)

---

## Section D: Habits and Routines

### Purpose
Keep habits and routines visible on the dashboard without over-engineering them. A lightweight habit section creates accountability without becoming a tracking burden.

### How to Keep It Lightweight

**Option 1: Simple checkbox list (simplest)**
- Add a toggle block to the dashboard: "🔄 Today's Routines"
- Inside: 3–5 checkboxes with habit names
- Manual check each day; uncheck at start of each new day
- ⚠️ Limitation: not persistent across days

**Option 2: Linked Streak Tracker database (recommended)**
- Maintain a separate Streak Tracker database (Date, Habit, Completed checkbox)
- Link it to the dashboard: filter Date = today
- Shows today's habits in a compact view
- Takes 2 minutes to fill in each day

### What NOT to Overbuild
- Do not create a habit database with 15 properties before you've tracked anything
- Do not add habits for things you haven't actually decided to do daily
- Do not put habits above the fold if they take attention away from your tasks

**Recommendation:** Start with a checkbox toggle. Graduate to the database once the habit is established (usually 2–4 weeks).

---

## Section E: Dashboard Layout

### Purpose
Arrange the sections so the most important information is visible within 5 seconds of opening the page.

### Recommended Section Order

**Top of page (always visible without scrolling):**
1. 📝 Daily Check-In toggle
2. [Left column] 🎯 Today
3. [Right column] ⚠️ Overdue

**Second visible area (one scroll):**
4. [Left column] 📅 This Week
5. [Right column] 🔔 Due Soon

**Below the fold:**
6. 🗂️ Kanban — Active Workflow (full-width)
7. 🏷️ Active Projects / Areas
8. ✅ Completed Recently
9. 📊 Weekly Status section

**Optional (bottom):**
- Habits / Routines
- Quick Links
- Capture / Inbox toggle

### How to Create Columns

1. Add two separate blocks (e.g., two linked databases)
2. Hover between them until a grey divider appears on the right edge
3. Click and drag one block to sit beside the other
4. A blue column divider will confirm 2-column layout
5. Adjust column width by dragging the column divider left or right

**If columns don't form:** Try clicking elsewhere first, then retry the drag slowly.

### Sidebar / Navigation Ideas
- Add a "📌 Quick Links" section at the very top with text links to frequently visited databases
- Use Notion's sidebar (left panel) to bookmark the dashboard for one-click access
- Set the dashboard as your Notion Home (Settings → Workspace → Set dashboard page as Home)

### How to Keep the Page Readable
- Maximum 8–10 sections total
- Use Heading 2 for section titles (not Heading 1 — those take up too much space)
- Use "Compact" mode on linked databases where possible (less padding)
- Hide database titles on linked views by toggling them off (this reduces visual clutter)

---

## Section F: Daily Check-In

### Purpose
Create a daily ritual section at the very top of the dashboard that takes under 5 minutes and sets intention before any tasks are opened.

### Option 1: Toggle Block (Recommended for Beginners)

**Steps:**
1. Place cursor at the very top of the dashboard, above all other sections
2. Press `/` → type "Toggle" → select "Toggle List"
3. Name it: `📝 Daily Check-In — [Today's Date]`
4. Open the toggle (click the triangle)
5. Inside, add these lines:
   ```
   1. Top 3 priorities today:
   
   2. Overdue items to address first?
   
   3. What did I avoid yesterday that shows up today?
   
   4. Energy level today: /5
   
   5. What would make today feel complete?
   ```
6. Fill it in right now — this is your first real check-in

**Each day:** Open the toggle, update the date in the name, answer the 5 questions.

### Option 2: Daily Log Database (For persistent record)

**Create a database with:**
- Date (Title formatted as date string)
- Top 3 Priorities (Text)
- Overdue Review (Text)
- Avoided Yesterday (Text)
- Energy Level (Number 1–5)
- Would Make Today Complete (Text)

**Link to dashboard:** Filter Date = today, view = List (1 visible row)

### Questions to Include (Recommended Set)

| Question | Why It Matters |
|----------|---------------|
| Top 3 priorities | Forces prioritisation before action |
| Overdue review | Surfaces forgotten obligations before new work begins |
| What I avoided | Creates honest self-awareness about avoidance patterns |
| Energy level | Helps match task difficulty to actual capacity |
| What would make today feel complete | Creates a clear finish line |

### How to Make It Quick and Useful
- Answer in bullets, not paragraphs (2–3 words per line is enough)
- Aim for 3–5 minutes maximum
- Do not skip it even on "obvious" days — the habit is more important than the answers

---

## Section G: Weekly Status

### Purpose
Surface week-level progress for self-reflection and (optional) sharing with an accountability partner. This also feeds directly into the Day 4 weekly review.

### What It Should Contain

**Part 1:** "Completed This Week" linked database view
- Task DB, filter: Status = Done, Date modified this week
- View: List (compact), show Task Name and Area

**Part 2:** Written weekly status template (text block)
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

### What It Should Surface
- Real completed work (not imagined or planned)
- Honest acknowledgment of what moved and what didn't
- A clear intention for the coming week

### How It Supports Day 4 Review
On Day 4, learners run a weekly review using this section as the starting point. The "Completed This Week" view becomes the evidence base. The filled-in text block becomes the review summary.

---

## Section H: Quick Actions

### Purpose
Optional. Reduce friction for the most common tasks: adding new tasks, notes, or ideas.

### Examples

**Button to add a new task (Notion button block):**
1. Press `/` → type "Button" → select "Button"
2. Label: "+ Add Task"
3. Action: "Insert blocks" → Table row → select Tasks database
4. Click the button → opens a new task directly in Inbox

**Shortcut links:**
- Plain text links to frequently used databases: `[Open Task Database](link to your tasks page)`
- Formatted as a row at the top of the page

**Capture toggle:**
1. Press `/` → "Toggle" → name: "💡 Capture / Inbox"
2. Inside: a simple text block for free-form capture
3. Process weekly: convert captured ideas into real tasks

---

## Section I: Reminder Setup

### Purpose
Configure due dates and reminder triggers so the system surfaces urgency before it becomes a crisis.

### Due Date Setup

For every task you care about completing on time:
1. Open the task
2. Click the "Due Date" property
3. Enter the date the task should be done
4. Press Enter to confirm

**Best practice:** Add due dates to tasks when you create them, not after. A task without a date is invisible to all your reminder views.

### Reminder Date Setup

1. Open a task with a due date
2. Click the "Reminder Date" property
3. Set a date 2–3 days before the Due Date
4. This is your personal lead time — when you want to *start thinking* about the task

### Notion's Built-In Date Reminders

1. Open a task → click the Due Date value
2. In the date picker, scroll down to the "Reminder" dropdown
3. Select: "30 minutes before", "1 day before", "2 days before", or "1 week before"
4. Click "Confirm"
5. Notion will push a notification (desktop or mobile, depending on your Notion app settings)

### Due Soon View Best Practices

- Keep the window at **3 days** (not 5, not 7 — keeps it focused)
- Sort by Due Date ascending (nearest deadline first)
- Show only: Task Name, Due Date, Area, Priority

### Overdue View Best Practices

- Sort by Due Date ascending (oldest overdue at top — most urgent)
- Check this view **first** at the start of each day session
- If a task is chronically overdue: either schedule it deliberately or delete it — don't leave it sitting overdue indefinitely

### Avoiding Reminder Fatigue

| ✅ Good Reminder Use | ❌ Reminder Fatigue |
|---------------------|-------------------|
| Set on important tasks that might be forgotten | Every single task has a reminder |
| Set 1–3 days before deadline | Reminders set day-of (too late to act) |
| Reviewed and cleared after the task is done | Ignored because there are too many |

---

## Section J: Screenshot Guidance

### Purpose
This guide intentionally avoids using third-party screenshots. All visual documentation for this course should come from the instructor's own Notion workspace, captured after the system is built.

### Where to Capture Screenshots

All Day 3 screenshots should be captured after completing the full dashboard build. See the full plan at:
[`assets/screenshots/day_3/README.md`](../assets/screenshots/day_3/README.md)

### How to Name Screenshots

Use this naming convention:
`day3_[section]_[description].png`

Examples:
- `day3_dashboard_overview.png`
- `day3_kanban_board.png`
- `day3_daily_checkin_filled.png`
- `day3_due_soon_view.png`

### What Each Screenshot Should Show

Each screenshot should show a **real, populated workspace** — not a blank template. Tasks should have real names (fictional is fine), real due dates, and real status values. The screenshot communicates "this is what a working system looks like," not "this is a demo."

### Recommendation for Instructors

1. Complete the full Day 3 build in your own Notion workspace
2. Populate it with fictional but realistic data (use the Alex Chen persona)
3. Capture screenshots in order (follow the sequence in `assets/screenshots/day_3/README.md`)
4. Place screenshots in the `assets/screenshots/day_3/` folder
5. **Do not use screenshots from third-party YouTube videos, blog posts, or Notion tutorials**

---

## Build Completion Checklist

Use this to verify the full build before class:

- [ ] Page created with icon, cover, full-width layout, and personal name
- [ ] Status property has 6 unified values with distinct colours
- [ ] Reminder Date property added to Task database
- [ ] Area / Life Domain property exists on Task database
- [ ] "Active Work" filtered Kanban view created
- [ ] "Today" filtered view created (Due = today OR Status = In Progress)
- [ ] "This Week" filtered view created
- [ ] "Due Soon" view created (next 3 days, Status ≠ Done)
- [ ] "Overdue" view created (Due before today, Status ≠ Done)
- [ ] "Completed Recently" view created
- [ ] Dashboard has 2-column layout with Today + Overdue visible above fold
- [ ] Daily Check-In toggle at the very top
- [ ] Kanban view embedded below fold
- [ ] Weekly Status section at the bottom
- [ ] Page set as Notion home
- [ ] 5-Second Test passed (most important task visible in < 5 seconds)
