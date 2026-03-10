# Dashboard Blueprint — Life OS Design Guide

## Building a Personal Productivity System with AI

---

### Overview

This document is a comprehensive design guide for building your **Life OS Dashboard** in Notion — the operational layer that makes your entire Life OS usable every day.

Your dashboard does not store new data. It **aggregates and surfaces** information from your existing databases through linked views with smart filters. The question it must always answer: **"What matters most right now — across all areas of my life?"**

---

## Part 1: Purpose and Philosophy

### What a Life OS Dashboard Is For

| Purpose | What It Means |
|---------|--------------|
| **Show what matters today** | Surface the most critical tasks across all life areas |
| **Warn before things break** | Overdue and Due Soon views catch what you're about to miss |
| **Create daily intention** | Check-in section forces deliberate prioritisation each morning |
| **Provide progress visibility** | Completed and Weekly Status sections confirm forward movement |
| **Enable weekly review** | Weekly Status section feeds directly into the Day 4 review |

### What a Dashboard Is NOT For

- Storing new data (use your databases for that)
- Showing everything (use filters to reduce noise to signal)
- Being beautiful before being useful (function first, aesthetics second)

---

## Part 2: Required Dashboard Sections

Build these sections in the order listed. Each depends on the previous.

### Section 1: Daily Check-In (Top of Page — Always Visible)

**Purpose:** Creates daily intention before any task-switching begins.

**Type:** Toggle block

**What it contains:**
- What are my top 3 priorities today?
- Is there anything overdue I need to handle first?
- What did I avoid yesterday?
- Energy level today (1–5)
- What would make today feel complete?

**Filter:** None — this is a freeform text section, not a linked database.

**Guidance:** Keep this at the very top of the page. If it's below the fold, it will be skipped.

---

### Section 2: Today

**Purpose:** Shows only what matters right now — tasks due today or currently in progress.

**Source database:** Tasks  
**View type:** List or Gallery (compact)  
**Filter:** Due Date = Today **OR** Status = In Progress  
**Properties shown:** Task Name, Status, Area only (hide everything else)  
**Sort:** Priority high to low

**What you should see at a glance:** 3–7 tasks. If you see more than 10, tighten your filter.

---

### Section 3: Overdue

**Purpose:** Surfaces tasks where the due date has already passed — forces an honest reckoning.

**Source database:** Tasks  
**View type:** List (compact)  
**Filter:** Due Date before Today **AND** Status ≠ Done  
**Properties shown:** Task Name, Due Date, Area, Status  
**Sort:** Due Date ascending (earliest overdue at top)

**Guidance:** If this section is consistently full, the problem is not the system — it's over-scheduling.

---

### Section 4: Due Soon

**Purpose:** Shows tasks approaching in the next 3–5 days before they become overdue.

**Source database:** Tasks  
**View type:** List (compact)  
**Filter:** Due Date within next 3 days **AND** Status ≠ Done  
**Properties shown:** Task Name, Due Date, Area, Priority  
**Sort:** Due Date ascending

**Guidance:** 3-day window is ideal. 7-day window shows too much and creates noise.

---

### Section 5: This Week

**Purpose:** Broader view of all tasks due within the next 7 days.

**Source database:** Tasks  
**View type:** Table  
**Filter:** Due Date within next 7 days **AND** Status ≠ Done  
**Properties shown:** Task Name, Due Date, Priority, Status, Area  
**Sort:** Priority high to low, then Due Date ascending

---

### Section 6: Active Projects / Areas

**Purpose:** Shows all currently active projects or life areas so you don't lose track of your bigger commitments.

**Source database:** Goals or Projects  
**View type:** Gallery or List  
**Filter:** Status = Active  
**Properties shown:** Name, Area/Domain, Priority, Deadline  
**Sort:** Priority descending

---

### Section 7: Kanban — Active Workflow

**Purpose:** Shows the board view of current active tasks as a visual workflow.

**Source database:** Tasks  
**View type:** Board (grouped by Status)  
**Filter:** Status ≠ Inbox **AND** Status ≠ Done  
**Properties shown:** Task Name, Area, Priority  
**Columns:** Planned / This Week / In Progress / Waiting / Blocked

**Guidance:** Embed this below the fold — it's rich context but not the first thing you should see in a morning scan.

---

### Section 8: Completed Recently

**Purpose:** Shows tasks completed in the last 7 days — builds momentum visibility and prevents the feeling that nothing is getting done.

**Source database:** Tasks  
**View type:** List (compact)  
**Filter:** Status = Done **AND** Last Edited date within last 7 days  
**Properties shown:** Task Name, Area, Completion Date  
**Sort:** Date descending (most recent first)

---

### Section 9: Capture / Inbox

**Purpose:** Quick-entry point for new tasks or ideas without switching pages.

**Options:**
- A **text toggle** for quick capture notes (fastest, no database)
- A **linked Inbox view** of your Task database filtered to Status = Inbox

**Guidance:** This should feel lightweight. Heavy inbox management belongs in a dedicated triage session.

---

### Section 10: Weekly Status

**Purpose:** End-of-week progress summary that feeds Day 4's weekly review.

**Components:**
- "Completed This Week" linked view (Status = Done, filtered by current week)
- A text block with structured prompts:
  - Week of:
  - Wins:
  - Still in progress / carried:
  - What I'm re-prioritising:
  - Focus for next week:

---

## Part 3: Optional Sections

Add these only if they serve a real question you ask regularly.

| Section | When to Add | How to Keep It Lightweight |
|---------|------------|---------------------------|
| **Habits / Routines** | If you track daily habits | Limit to 3 habits max; use checkbox list or tiny database |
| **Appointments** | If you have recurring meetings | Embed your calendar or link to Notion calendar view |
| **Notes / Scratchpad** | If you capture ideas daily | One toggle block only — process it weekly |
| **Quick Links** | If you navigate often to external pages | Simple Notion bookmarks or a short list of URLs |
| **Quick Actions** | If Notion supports buttons in your plan | Button to add task, add note, open check-in |

---

## Part 4: Recommended Dashboard Layout

### 2-Column Structure

| Column 1 (Left) | Column 2 (Right) |
|-----------------|-----------------|
| 📝 Daily Check-In (toggle, full width across top) | |
| 🎯 Today | ⚠️ Overdue |
| 📅 This Week | 🔔 Due Soon |
| 🗂️ Active Projects / Areas | ✅ Completed Recently |

**Below the fold (full width):**
- 🗂️ Kanban — Active Workflow
- 📊 Weekly Status section
- (Optional) Habits / Capture / Quick Links

---

## Part 5: Design Principles and Avoiding Clutter

### Rules That Keep Your Dashboard Useful

1. **Maximum 8–10 sections total.** More than 10 means scroll-fatigue; the page stops being a dashboard and starts being a maze.

2. **Every section must answer a question.** Before adding a section, state the question it answers. "What's due today?" is good. "What does all my data look like?" is not.

3. **Run the 5-Second Test.** After any change, close Notion and reopen. Can you see today's most important task within 5 seconds? If not, reorganize.

4. **Vary view types.** Using Table for every section creates visual monotony. Mix List, Gallery, and Board to make sections scannable at different granularities.

5. **Show only relevant properties.** Every column you don't need in a linked view adds cognitive load. Hide it.

6. **Review your dashboard monthly.** Delete any section you haven't actively used in the past 2 weeks. If you open a dashboard page and always skip a section, the section is wrong for you.

---

## Part 6: Beginner-Friendly Build Notes

### How to Add a Linked Database in Notion

1. Press `/` on a new line
2. Type "Linked view of database" → press Enter
3. In the search box, type the name of your database → click it
4. A default table view will appear
5. Click "+ Add a view" to add Board, List, Gallery, etc.
6. Click "Filter" to narrow the results

### How to Create Columns in Notion

1. Type two separate blocks (e.g., two headings or two linked databases)
2. Hover between them until a blue line appears on the right edge
3. Drag one block to sit beside the other
4. Adjust column width by dragging the divider

### How to Hide Properties in a View

1. Click the linked database view → click "•••" → "Properties"
2. Toggle off any property you don't need to see in that specific view
3. This does NOT delete the property — it's just hidden in this view

---

## Part 7: Reminder-Ready Views

Your "Due Soon" and "Overdue" views **are your reminder system**. To make them effective:

- Ensure every task you care about has a **Due Date** property set
- Keep "Due Soon" at 3 days maximum — not 5, not 7
- Keep "Overdue" sorted with the oldest at the top (most urgent first)
- Add a **Reminder Date** property for tasks where you need a heads-up before the due date

> **Best practice:** Reminders are for tasks that are important but not urgent — where the due date might sneak up on you. Don't add reminders to every task; reminders for everything = effective reminders for nothing.
