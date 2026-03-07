# Kanban Structure

## Building a Personal Productivity System with AI

---

### Overview

This document describes the default Kanban workflow stages and the decision rules for moving tasks between stages.

---

## Default Workflow Stages

| Stage | Emoji | What Goes Here |
|-------|-------|---------------|
| Backlog | 📌 | All captured tasks not yet committed to a specific week |
| This Week | 📋 | Tasks you've committed to completing this week |
| In Progress | ⚡ | Actively being worked on — WIP LIMIT: 3 |
| Blocked | 🔴 | Cannot move forward — waiting on something external |
| Done | ✅ | Completed this week (archive weekly) |

---

## WIP Limit

**Maximum tasks in "In Progress" at any time: 3**

This is a commitment, not a suggestion. If you want to add a 4th In Progress task, something must move to Done first.

If nothing is ready to be marked Done, it means you are multitasking — which is the problem the Kanban is designed to reveal.

---

## Stage Transition Rules

Use these decision rules to decide when a task moves between stages:

| From | To | Decision Rule |
|------|----|---------------|
| Backlog → This Week | "I commit to completing this task before Friday" |
| This Week → In Progress | "I am actively working on this right now (in this session)" |
| In Progress → Blocked | "I cannot proceed without input from someone else or an external event" |
| Blocked → In Progress | "The blocker has been resolved — I can continue" |
| In Progress → Done | "The task is complete. Nothing more needs to be done on this task." |
| Done → Archived | "End-of-week review: move Done tasks to an archive view" |

---

## Customising Your Stages

Your work may need different stage names. Common customisations:

### For creative or writing work:
| Stage | What it means |
|-------|--------------|
| Backlog | Not started |
| Drafting | Active writing in progress |
| Review | Draft complete, pending review or feedback |
| Editing | Feedback received, revisions underway |
| Published / Done | Live or submitted |

### For client / project work:
| Stage | What it means |
|-------|--------------|
| Backlog | Captured |
| Scoped | Defined and ready to start |
| In Progress | Actively working |
| Awaiting Client | Done by me, waiting on client input |
| Delivered | Submitted / handed over |

### For learning / study:
| Stage | What it means |
|-------|--------------|
| To Learn | Topics queued |
| Active Study | Currently studying |
| Practising | Applying / testing knowledge |
| Review | Spaced repetition pending |
| Complete | Mastered / tested |

---

## Weekly Kanban Maintenance (5 min)

Do this at the start of each week:

1. **Archive Done column:** Move last week's Done tasks to an archived view (filter: Status = Done AND Due < this week)
2. **Review Backlog:** Move 3–7 tasks from Backlog into This Week — only what you genuinely commit to
3. **Review Blocked:** For each Blocked task — has the blocker resolved? If yes, move to In Progress or This Week. If no, add a note with the remaining dependency.
4. **Check WIP:** Is In Progress at 3 or fewer? If more, something moved without being tracked — fix it.
