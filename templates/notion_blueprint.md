# Notion Blueprint

## Building a Personal Productivity System with AI

---

### Overview

This document describes the complete Notion workspace architecture — every database, its properties, and its relationships. Use this as a reference when setting up your workspace from scratch or troubleshooting a broken relation.

---

## Database 1: Goals

**Purpose:** The highest-level layer of your system. Captures what you're working toward and defines success.

**View types to create:**
- Table (default)
- Gallery (by Status — for dashboard embedding)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Goal Name | Title | Active phrasing: "Launch a newsletter with 500 subscribers by June" |
| Outcome Statement | Text | 1–2 sentences on what changes in the world when this goal is achieved |
| Success Criteria | Text | 3–5 bullet points — observable, measurable |
| Status | Select | Active / Paused / Achieved / Archived |
| Domain | Select | Career / Learning / Financial / Health / Personal / Creative |
| Deadline | Date | Target completion date |
| Priority | Select | High / Medium / Low |
| Linked Projects | Relation | → Projects database (one Goal → many Projects) |

---

## Database 2: Projects

**Purpose:** Bounded units of work that serve goals. Each project produces a deliverable.

**View types to create:**
- Table (default)
- Filtered: Active Projects (Status = Active)
- Gallery (for dashboard: show Name + Priority + Status)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Project Name | Title | Action-oriented: "Build Content Pipeline" not "Content" |
| Linked Goal | Relation | → Goals database (many Projects → one Goal) |
| Status | Select | Planning / Active / On Hold / Complete / Archived |
| Priority | Select | High / Medium / Low |
| Deadline | Date | Target completion |
| Scope Note | Text | 1 sentence on what's included and excluded |
| Milestone Map | Toggle / Text | Nested toggle list with milestone checkpoints |
| Linked Tasks | Relation | → Tasks database (one Project → many Tasks) |

---

## Database 3: Tasks

**Purpose:** Atomic actions. Each task can be completed in one work session. Verb-first names.

**View types to create:**
- Table (default)
- Board (Kanban by Status)
- Filtered: This Week's Priorities (Due ≤ +7 days, sort: Priority)
- Filtered: Today's Focus (Due = today OR Priority = Critical)
- Filtered: Blocked (Status = Blocked)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Task Name | Title | Verb-first: Draft / Review / Send / Build / Decide / Research |
| Linked Project | Relation | → Projects database |
| Status | Select | Backlog / This Week / In Progress / Blocked / Done |
| Priority | Select | P1 – Critical / P2 – High / P3 – Medium / P4 – Low |
| Due Date | Date | Approximate is fine — update as needed |
| Effort | Select | Small (< 1hr) / Medium (1–3hr) / Large (3hr+) |
| Notes | Text | Blocker details, dependencies, or context |

---

## Database 4: Anti-To-Do Log

**Purpose:** Captures completed work, decisions, and problems solved — what you actually shipped.

**View types to create:**
- Table (default)
- Filtered: Today (Date = today) — for dashboard
- Filtered: This Week (Date ≥ start of week)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Entry | Title | [Action verb + what + why it counts] |
| Date | Date | The date this was completed |
| Category | Select | Work / Admin / Learning / Decision / Personal |
| Notes | Text | Optional: impact, who it helped, what it unblocked |

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
| Domain | Select | Matches your Attention Budget categories |
| Output | Text | 1-sentence description of what was produced |

---

## Database 6: Streak Tracker

**Purpose:** Tracks daily process habits for consistency.

**View types to create:**
- Table (default)
- Filtered: Last 14 Days (Date ≥ today minus 14 days, sort: Date descending)

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Entry | Title | Auto-populated: "[Habit] — [Date]" |
| Date | Date | The date of the habit |
| Habit | Select | Your 2–3 habit options (Morning Planning / Daily Check-In / etc.) |
| Completed | Checkbox | ✅ if done, unchecked if missed |
| Notes | Text | Optional: barrier, minimal version completed |

---

## Master Dashboard Page

**Page name:** 🏠 [Your Name]'s Mission Control

**Layout:** 2-column, with linked databases and callout blocks.

**Recommended sections:**

| Position | Section | Source | Filter |
|----------|---------|--------|--------|
| Column 1, Top | Today's Focus | Tasks | Due = today OR Priority = Critical |
| Column 1, Middle | Active Projects | Projects | Status = Active |
| Column 2, Top | This Week | Tasks | Due ≤ +7 days, sort Priority |
| Column 2, Middle | Anti-To-Do: Today | Anti-To-Do Log | Date = today |
| Below fold | Daily Habits | Streak Tracker | Date = today |

**Optional additions:**
- Callout block at top: "Dashboard updated [date] — System v[X]"
- Quick Capture toggle: free-text inbox for processing later
- Link to weekly review template

---

## Relation Map (Visual)

```
Goals ──────────────────────────────────────────────────────────────────┐
  │                                                                       │
  └──[ Linked Projects ]──► Projects ──────────────────────────────────┐  │
                              │                                          │  │
                              └──[ Linked Tasks ]──► Tasks              │  │
                                                       │                 │  │
                                                       └── Dashboard ◄──┘  │
                                                                           │
Anti-To-Do Log ──────────────────────────────────► Dashboard ◄────────────┘
Work Session Log ─────────────────────────────────► Attention Budget
Streak Tracker ───────────────────────────────────► Dashboard
```
