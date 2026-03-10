# Notion Blueprint — Life OS Architecture

## Building a Personal Productivity System with AI

---

### Overview

This document describes the complete Notion workspace architecture for your Life OS — every database, its properties, and how they connect. This is your reference when setting up from scratch, adding Day 3 components, or troubleshooting a broken relation.

**Day 3 additions are marked with ✨** for easy identification.

---

## Database 1: Goals

**Purpose:** The highest-level layer. Captures what you're working toward across all life areas.

**View types to create:**
- Table (default)
- Gallery (by Status — for dashboard embedding)
- Filtered: Active (Status = Active)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Goal Name | Title | Active phrasing: "Launch a newsletter with 500 subscribers by June" |
| Outcome Statement | Text | 1–2 sentences on what changes in your life when this is achieved |
| Success Criteria | Text | 3–5 observable, measurable bullet points |
| Status | Select | Active / Paused / Achieved / Archived |
| Area / Life Domain ✨ | Select | Work / Studies / Personal / Content / Health / Admin / Finance |
| Deadline | Date | Target completion date |
| Priority | Select | High / Medium / Low |
| Linked Projects | Relation | → Projects database |

---

## Database 2: Projects

**Purpose:** Bounded units of work that serve goals. Each project produces a deliverable.

**View types to create:**
- Table (default)
- Filtered: Active Projects (Status = Active)
- Gallery (for dashboard: Name + Priority + Status)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Project Name | Title | Action-oriented: "Build Content Pipeline" not "Content" |
| Linked Goal | Relation | → Goals database |
| Status | Select | Planning / Active / On Hold / Complete / Archived |
| Area / Life Domain ✨ | Select | Matches task Area/Life Domain property |
| Priority | Select | High / Medium / Low |
| Deadline | Date | Target completion |
| Scope Note | Text | 1 sentence on what's included and excluded |
| Milestone Map | Toggle / Text | Nested toggle list with milestone checkpoints |
| Linked Tasks | Relation | → Tasks database |

---

## Database 3: Tasks ✨ (Day 3 Expanded)

**Purpose:** Atomic actions. Each task can be completed in one work session. Verb-first names.

**View types to create:**
- Table (default)
- Board — Kanban by Status ✨ (Day 3)
- Filtered: Active Work (Status ≠ Inbox, Status ≠ Done) ✨
- Filtered: Today (Due = today OR Status = In Progress) ✨
- Filtered: This Week (Due ≤ +7 days, sort: Priority)
- Filtered: Due Soon (Due within next 3 days, Status ≠ Done) ✨
- Filtered: Overdue (Due before today, Status ≠ Done) ✨
- Filtered: Completed Recently (Status = Done, last 7 days) ✨

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Task Name | Title | Verb-first: Draft / Review / Send / Build / Decide / Research |
| Area / Life Domain ✨ | Select | Work / Studies / Personal / Content / Health / Admin / Finance |
| Status ✨ | Select | **Inbox / Planned / This Week / In Progress / Waiting / Done** (Life OS workflow) |
| Priority | Select | P1 – Critical / P2 – High / P3 – Medium / P4 – Low |
| Due Date ✨ | Date | Set for all actionable tasks — required for reminder views |
| Reminder Date ✨ | Date | Date to be reminded — before the due date (e.g., 2 days earlier) |
| Linked Project | Relation | → Projects database |
| Notes | Text | Blocker details, dependencies, or context |
| Effort | Select | Small (< 1hr) / Medium (1–3hr) / Large (3hr+) |

### Unified Life OS Workflow Status Values ✨

> Use these status values **consistently** across all tasks in all life areas. Do not use different statuses for work vs. personal tasks.

| Status | Purpose | When to Use |
|--------|---------|------------|
| **Inbox** | Captured, not yet assessed | Anything you just captured or haven't committed to yet |
| **Planned** | Assessed, not yet scheduled | Real task, but no specific week committed |
| **This Week** | Committed to the current week | Moved here intentionally — you plan to do it this week |
| **In Progress** | Actively working on it | Limit to 3 tasks at once (WIP limit) |
| **Waiting / Blocked** | Waiting on someone or something | External dependency — cannot proceed without it |
| **Done** | Completed | Archive or review weekly |

---

## Database 4: Anti-To-Do Log

**Purpose:** Captures completed work, decisions, and problems solved — what you actually shipped.

**View types to create:**
- Table (default)
- Filtered: Today (Date = today)
- Filtered: This Week (Date ≥ start of week)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Entry | Title | [Action verb + what + why it counts] |
| Date | Date | The date this was completed |
| Category | Select | Work / Admin / Learning / Decision / Personal / Content |
| Notes | Text | Impact, who it helped, what it unblocked |

---

## Database 5: Work Session Log

**Purpose:** Records focused work blocks for attention budget analysis.

**View types to create:**
- Table (default)
- Filtered: This Week (Date ≥ start of week)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Session | Title | [Project/Domain + brief descriptor] |
| Date | Date | Session date |
| Duration (hrs) | Number | Decimal fine: 1.5 = 90 minutes |
| Area / Domain | Select | Matches Area/Life Domain — Work / Studies / Personal / etc. |
| Output | Text | 1-sentence description of what was produced |

---

## Database 6: Daily Check-In Log ✨ (New — Day 3)

**Purpose:** Records daily intentions and reflections. Feeds into weekly review patterns.

**Note:** This database is optional — many learners use the toggle block approach on the dashboard instead. Create this database if you want a persistent, searchable log.

**View types to create:**
- Table (default)
- Filtered: This Week (Date ≥ start of week)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Date | Title (as date string) | "Monday 10 March" — makes the log scannable |
| Top 3 Priorities | Text | Brief list of today's priorities |
| Overdue Review | Text | Any overdue tasks I'm addressing today |
| Avoided Yesterday | Text | Honest: what did I put off? |
| Energy Level | Number (1–5) | 1 = burnt out, 5 = high |
| Would Make Today Complete | Text | One clear finish line for today |

---

## Database 7: Streak / Routine Tracker

**Purpose:** Tracks daily process habits for consistency across the system.

**View types to create:**
- Table (default)
- Filtered: Last 14 Days (Date ≥ today minus 14 days, sort: Date descending)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Entry | Title | Auto-populated: "[Habit] — [Date]" |
| Date | Date | The date of the habit |
| Habit | Select | Your 2–3 habit options (Morning Check-In / Daily Review / etc.) |
| Completed | Checkbox | ✅ if done, unchecked if missed |
| Notes | Text | Optional: minimum-viable version if fully done felt impossible |

---

## Life OS Dashboard Page ✨ (Day 3 Core)

**Page name:** [Your emoji] [Your Name]'s Life OS  
**Layout:** Full-width, 2-column, with linked databases, callout, and toggle blocks.

### Recommended Section Order

| Position | Section | Source Database | Filter |
|----------|---------|----------------|--------|
| Top (full-width) | 📝 Daily Check-In | — (toggle) | None |
| Column 1, Top | 🎯 Today | Tasks | Due = today OR Status = In Progress |
| Column 1, Middle | 📅 This Week | Tasks | Due ≤ +7 days, sort Priority |
| Column 2, Top | ⚠️ Overdue | Tasks | Due < today AND Status ≠ Done |
| Column 2, Middle | 🔔 Due Soon | Tasks | Due within 3 days AND Status ≠ Done |
| Below fold (full-width) | 🗂️ Kanban — Active | Tasks | Board — Status ≠ Inbox, Status ≠ Done |
| Below fold | 🏷️ Active Areas | Goals/Projects | Status = Active |
| Below fold | ✅ Completed Recently | Tasks | Status = Done, last 7 days |
| Bottom | 📊 Weekly Status | Tasks + Text | Status = Done, this week + written summary |

**Optional additions:**
- Habits/Routines linked view (3 habits max — keep lightweight)
- Quick Links (short list of external URLs or Notion pages you visit daily)
- Quick Capture toggle (free-text inbox for ideas to process later)

---

## Relation Map (Full Life OS)

```
Goals ─────────────────────────────────────────────────────────┐
  │                                                               │
  └──[ Linked Projects ]──► Projects ────────────────────────┐   │
                              │                                │   │
                              └──[ Linked Tasks ]──► Tasks    │   │
                                                      │        │   │
                    ┌── Due Soon view (filter) ───────┘        │   │
                    ├── Overdue view (filter) ─────────────────┤   │
                    ├── Today view (filter) ──────────────────►│   │
                    └── Kanban / Board view ──────────────── Dashboard ◄──┘
Anti-To-Do Log ───────────────────────────────────────────► Dashboard
Work Session Log ──────────────────────────────────────────> Attention Budget
Daily Check-In Log ─────────────────────────────────────── Dashboard (toggle)
Streak / Routine Tracker ──────────────────────────────────> Dashboard (optional)
```

---

## Property Naming Reference

Use these exact names for maximum consistency across your system.

| Property | Database | Type | Purpose |
|----------|---------|------|---------|
| Task Name | Tasks | Title | Task label |
| Area / Life Domain | Tasks, Goals, Projects | Select | Life area categorisation |
| Status | Tasks | Select | Workflow stage (6 values) |
| Priority | Tasks, Projects | Select | Urgency/importance tier |
| Due Date | Tasks | Date | When it must be done |
| Reminder Date | Tasks | Date | When to be reminded (before due date) |
| Linked Project | Tasks | Relation | Task → Project link |
| Notes | Tasks | Text | Context, blockers, dependencies |
| Effort | Tasks | Select | Time estimate category |
