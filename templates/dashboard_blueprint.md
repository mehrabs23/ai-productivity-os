# Dashboard Blueprint

## Building a Personal Productivity System with AI

---

### Overview

This document provides a step-by-step guide to building your Master Dashboard in Notion — the "front page" of your productivity system.

Your dashboard should answer one question above all others: **"What do I do right now?"**

---

## Part 1: Create the Dashboard Page

1. Open Notion and navigate to your workspace home
2. Create a new page at the top level (not inside any database)
3. Name it: **🏠 [Your Name]'s Mission Control**
4. Add a header callout block at the top:
   > 📋 **Dashboard** | Week of [date] | System v1.0

---

## Part 2: Add Your Key Views

### View 1: Today's Focus

**Purpose:** Shows only the tasks that matter right now — today's deadlines and critical work.

**Setup steps:**
1. Click `/` → type "Linked view of database" → select your **Task Database**
2. Click "Filter" → Add filter: Due Date = Today **OR** Priority = Critical
3. Hide all properties except: Task Name + Status
4. Rename the view: **"🎯 Today's Focus"**
5. Set view type: Table (compact)

---

### View 2: Active Projects

**Purpose:** Shows your active projects at a glance with their priority and status.

**Setup steps:**
1. Add another linked database → select your **Projects Database**
2. Filter: Status = Active
3. Show properties: Name + Priority + Deadline
4. Rename: **"🗂️ Active Projects"**
5. Set view type: Gallery (shows cards) or List

---

### View 3: This Week

**Purpose:** Shows all tasks due within the next 7 days, sorted by priority.

**Setup steps:**
1. Add another linked database → select your **Task Database**
2. Filter: Due Date ≤ Today + 7 days
3. Sort: Priority → High to Low
4. Show properties: Name + Due Date + Priority + Status
5. Rename: **"📅 This Week"**
6. Set view type: Table

---

### View 4: Anti-To-Do — Today

**Purpose:** Reminds you what you've already shipped today — counteracts the feeling that nothing is getting done.

**Setup steps:**
1. Add another linked database → select your **Anti-To-Do Log**
2. Filter: Date = Today
3. Show properties: Entry + Category
4. Rename: **"✅ Shipped Today"**
5. Set view type: List (compact)

---

### View 5: Daily Habits

**Purpose:** Shows today's streak tracker entries — keep this visible to build end-of-day habit.

**Setup steps:**
1. Add another linked database → select your **Streak Tracker**
2. Filter: Date = Today
3. Show properties: Habit + Completed
4. Rename: **"🔥 Today's Habits"**
5. Set view type: Table (compact)

---

## Part 3: Layout and Design

### 2-Column Layout

Notion supports dragging blocks side by side to create columns.

**Recommended layout:**

| Column 1 | Column 2 |
|----------|----------|
| 🎯 Today's Focus | 📅 This Week |
| 🗂️ Active Projects | ✅ Shipped Today |
| (below fold) 🔥 Today's Habits | (below fold) Quick links |

To create columns: hover between two blocks until a blue divider appears, then drag one block beside the other.

---

## Part 4: The 5-Second Load Test

After your dashboard is set up, run this test:

1. Close Notion completely
2. Open Notion from the app icon
3. Navigate to your Mission Control page
4. Start timing from page load

**Target:** You can identify your single most important task within 5 seconds.

If you can't, identify which section is causing noise and either:
- Remove it
- Simplify the filter
- Move it below the fold (out of first-view)

---

## Part 5: Dashboard Maintenance

### Weekly (2 minutes, as part of weekly review)
- Update the header callout with the current week
- Check that linked views are showing the right data (filters still valid)
- Remove any section you haven't opened in the past week

### Monthly (with retrospective)
- Evaluate which views you actually use vs. ignore
- Remove ignored views
- Add new views only if they answer a question you're asking daily

---

## Quick Reference: Notion Linked View Tips

| Goal | How to do it |
|------|-------------|
| Show only active items | Add filter: Status = Active / Not Started / In Progress |
| Limit visible columns | Open view → "Properties" → toggle off unused fields |
| Set a default view | Click ••• on the view tab → "Set as default view" |
| Hide database title | Toggle "Show database title" off under view settings |
| Create narrow table columns | Drag column borders to resize |
