# Streak Tracker Structure

## Building a Personal Productivity System with AI

---

### Overview

This document describes how to design, populate, and maintain your Streak Tracker — the habit consistency layer of your productivity system.

---

## What Is a Streak Tracker?

A streak tracker records whether you completed a daily process habit on a given day. It is not a tracker of outcomes ("did I earn £500 today?") — it is a tracker of processes ("did I run my morning planning routine today?").

**Why process habits, not outcome targets?**
- You cannot directly control whether you close a sale. You can control whether you made the calls.
- You cannot control whether you feel creative. You can control whether you sat down to write.
- Outcomes are variable. Processes are consistent. Track what you control.

---

## Database Structure

| Property | Type | Notes |
|----------|------|-------|
| Entry | Title | Use format: "[Habit] — [Date]" e.g., "Morning Planning — 12 Mar" |
| Date | Date | The specific date of this entry |
| Habit | Select | Your 2–3 habit options |
| Completed | Checkbox | ✅ if done, unchecked if missed |
| Notes | Text | Optional: what got in the way, or the minimal version you completed |

---

## Choosing Your 2–3 Habits

Use the following framework to select the right habits:

**High-leverage candidates:**

| Habit | Why it's worth tracking |
|-------|------------------------|
| Morning Planning | Sets direction before reactive work begins |
| Anti-To-Do Update | Keeps completed work visible; feeds weekly review |
| Session Log Update | Enables attention budget analysis |
| End-of-Day Reflection | Closes the mental loop; improves tomorrow |
| Dashboard Check | Keeps priorities top of mind |
| Weekly Review | Prevents project drift |

**Select habits that:**
- You can complete in 5–15 minutes
- Are currently inconsistent (not things you always do anyway)
- Feed other parts of your system (e.g., Morning Planning feeds the Daily Note)

**Start with 2. Add a 3rd only after 3 weeks of consistency.**

---

## Minimum Viable Version of Each Habit

For difficult days, define a minimal version that still counts:

| Habit | Full version | Minimal version (still counts) |
|-------|-------------|-------------------------------|
| Morning Planning | 15 min with ChatGPT + Daily Note | 5 min: open dashboard and name 1 priority |
| Anti-To-Do Update | 3+ entries with category | 1 entry — anything you completed |
| End-of-Day Reflection | Full Daily Check-In template | Write 1 sentence: "Today I ___" |
| Weekly Review | 6-step full review | 5-min pass: Anti-To-Do review + 3 next-week outcomes |

> **Rule:** Streaks maintained with minimal versions still count. The point is consistency, not perfection.

---

## View Setup in Notion

### View 1: Last 14 Days
- Filter: Date ≥ Today minus 14 days
- Sort: Date descending (most recent at top)
- Group by: Habit (to see each habit's streak at a glance)

### View 2: This Week
- Filter: Date ≥ start of current week
- View type: Table
- Good for embedding in your dashboard

### View 3: Full Archive
- No filter
- Sort: Date descending
- Used for monthly retrospective

---

## Monthly Habit Review

Include this in your monthly retrospective:

1. **Which habit had the highest completion rate?** ___ / ___ days
2. **Which habit had the lowest?** ___ / ___ days
3. **What made the low-completions happen?** Specific barrier pattern?
4. **Is the habit still relevant to your current goals?** If not, swap it.

---

## Red Flag Patterns

| Pattern | Interpretation |
|---------|---------------|
| Streak consistently breaks on Mondays | Monday is heavier than expected — adjust planning ritual |
| Streak breaks in same week each month | Pattern event (e.g., billing week, recurring calls) |
| All habits break simultaneously | Systemic overload — time to run an Overload Triage |
| Habit never gets completed | Wrong habit, or implementation intention missing — redesign |
