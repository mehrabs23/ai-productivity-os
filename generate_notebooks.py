"""
Notebook generator for:
  "Building a Personal Productivity System with AI"

Run:  python3 generate_notebooks.py
Output: notebooks/ and colab_versions/ directories
"""

import json, os, pathlib

NOTEBOOKS_DIR = pathlib.Path("notebooks")
COLAB_DIR     = pathlib.Path("colab_versions")
NOTEBOOKS_DIR.mkdir(exist_ok=True)
COLAB_DIR.mkdir(exist_ok=True)


# ── helpers ────────────────────────────────────────────────────────────────

def md(source):
    return {"cell_type": "markdown", "metadata": {}, "source": source}

def code(source, outputs=None):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": outputs or [],
        "source": source,
    }

def nb(cells, title=""):
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"},
            "colab": {"name": title},
        },
        "cells": cells,
    }

def save(notebook, filename):
    for path in [NOTEBOOKS_DIR / filename, COLAB_DIR / filename]:
        with open(path, "w") as f:
            json.dump(notebook, f, indent=1)
    print(f"  ✓ {filename}")


# ══════════════════════════════════════════════════════════════════════════════
# DAY 1 — Foundation: Goals, Projects, Tasks
# ══════════════════════════════════════════════════════════════════════════════

def build_day1():
    cells = []

    # ── Title ─────────────────────────────────────────────────────────────
    cells.append(md("""\
# 🗂️ Day 1 — Foundation: Goals, Projects & Tasks
## Building a Personal Productivity System with AI

**Estimated duration:** 5 hours (with breaks)  
**Notebook role:** Interactive lab — run alongside your Notion workspace and ChatGPT tab.

---

### What you will do today
| Session | Outcome |
|---------|---------|
| Session 1 | Understand the Productivity OS model |
| Session 2 | Define 3–5 real goals with success criteria |
| Session 3 | Translate goals into active projects |
| Session 4 | Break projects into tasks |

> **How to use this notebook:**  Edit cells tagged with `# ✏️ YOUR INPUT` and run them.  
> All other cells are pre-built for you. You do not need to write code from scratch.

---
"""))

    # ── Setup ─────────────────────────────────────────────────────────────
    cells.append(md("## ⚙️ Setup — Run This First"))
    cells.append(code("""\
# Run this cell first — sets up display libraries
import pandas as pd
from IPython.display import display, Markdown

pd.set_option("display.max_colwidth", 80)
pd.set_option("display.max_rows", 50)
print("✅ Setup complete — you're ready to start Day 1.")
"""))

    # ── Section 1 ─────────────────────────────────────────────────────────
    cells.append(md("""\
---
## 📖 Session 1 — What Is a Productivity OS?
*Duration: ~60 minutes (teaching + activity)*

### Concept
Most people manage **tasks**. High performers manage **systems**.

A **Productivity Operating System** has three layers:

| Layer | What it is | Example |
|-------|-----------|---------|
| **Goals** | The outcomes you want | "Launch a newsletter with 500 subscribers by June" |
| **Projects** | Bounded work that serves a goal | "Build Beehiiv newsletter platform" |
| **Tasks** | Atomic actions inside a project | "Draft issue 1 outline" |

> Most people live at the Task layer and wonder why they feel busy but not productive.  
> This course installs all three layers — today.

### Why Notion + ChatGPT?
- **Notion** = relational database that links Goals → Projects → Tasks in one workspace  
- **ChatGPT** = structured thinking partner that helps articulate vague intentions precisely

*No coding required — this notebook helps you organise, visualise, and reflect on what you build in Notion.*

---
"""))

    cells.append(md("### 🎯 Activity 1A — Your Current Productivity State"))
    cells.append(code("""\
# ✏️ YOUR INPUT — edit the values below, then run the cell

my_name = "Alex"                  # Your name
org_score = 2                     # How organised do you feel right now? (1 = chaos, 5 = very organised)
biggest_frustration = "I lose track of what I'm supposed to be working on."

# ── Output ──
display(Markdown(f\"\"\"
### 👤 {my_name}'s Starting Point

| Question | Your Answer |
|----------|------------|
| Organisation score (1–5) | **{org_score} / 5** |
| Biggest frustration | *{biggest_frustration}* |

> Bookmark this. On Day 4 you'll compare against where you end up.
\"\"\"))
"""))

    # ── Section 2 ─────────────────────────────────────────────────────────
    cells.append(md("""\
---
## 🎯 Session 2 — Defining Your Goals with AI
*Duration: ~60 minutes*

### Concept
**A goal without success criteria is a wish.**

Well-formed goals are:
- **Outcome-focused** — describe what changes, not what you'll do
- **Time-bounded** — have a clear deadline
- **Measurable** — have observable success criteria you can verify

```
Goal formula = Outcome statement + Deadline + Success criteria (3–5 bullet points)
```

### ChatGPT Prompt Block
Copy the prompt below into ChatGPT, replacing everything in `[BRACKETS]`:

---
```
I want to define a personal goal more clearly. Here is my raw goal:

[PASTE YOUR RAW GOAL STATEMENT HERE]

Please:
1. Rewrite it as a specific outcome statement (what changes, not what I'll do)
2. Suggest 3–5 measurable success criteria
3. Identify 1–2 pitfalls that might prevent it
4. Ask 2–3 clarifying questions to sharpen the goal further

My context: [DESCRIBE YOUR SITUATION BRIEFLY]
```
---
> 📎 Full prompt versions: `prompt_library/goal_design_prompts.md` in the course repo
"""))

    cells.append(md("### 🎯 Activity 2A — Enter Your Goals"))
    cells.append(code("""\
# ✏️ YOUR INPUT — fill in your goals below
# Paste in what you got from ChatGPT (edited to be truly yours)

goals = [
    {
        "goal_name": "Launch a freelance UX business",
        "outcome": "Have 3 paying clients generating £3,000+/month by December 31st",
        "deadline": "2024-12-31",
        "success_criteria": "3 active clients / £3k MRR / 5 published case studies",
        "domain": "Career",
        "status": "Active",
    },
    {
        "goal_name": "Complete Figma Advanced Course",
        "outcome": "Finish all 8 modules and create 2 motion design portfolio pieces",
        "deadline": "2024-05-31",
        "success_criteria": "All modules done / 2 portfolio pieces published",
        "domain": "Learning",
        "status": "Active",
    },
    # Add more goals here — copy the block above and edit
]

# ── Display your goals table ──
df_goals = pd.DataFrame(goals)
display(Markdown("### 📋 Your Goals Database"))
display(df_goals[["goal_name", "domain", "deadline", "status"]])
display(Markdown("---"))
display(Markdown("**Full success criteria:**"))
for i, g in enumerate(goals, 1):
    display(Markdown(f"**Goal {i} — {g['goal_name']}**  \\n{g['outcome']}  \\n✅ {g['success_criteria']}"))
"""))

    cells.append(code("""\
# ── Goal quality check ──
display(Markdown("### ✅ Goal Quality Check"))
issues = []
for g in goals:
    if len(g["outcome"]) < 20:
        issues.append(f"⚠️  '{g['goal_name']}': outcome statement is very short — is it specific enough?")
    if len(g["success_criteria"].split("/")) < 2:
        issues.append(f"⚠️  '{g['goal_name']}': try to add at least 2–3 success criteria.")

if issues:
    for issue in issues:
        print(issue)
else:
    print("✅ All goals look well-formed. Copy them into your Notion Goals Database.")
print(f"\\nTotal goals defined: {len(goals)}")
"""))

    # ── Section 3 ─────────────────────────────────────────────────────────
    cells.append(md("""\
---
## 🗂️ Session 3 — Projects: Translating Goals into Work
*Duration: ~60 minutes*

### Concept
A **project** is a bounded piece of work that produces a deliverable when complete.

| | Goal | Project |
|--|------|---------|
| Duration | Months–years | Weeks–months |
| Done when | Outcome achieved | Deliverable produced |
| Example | Launch freelance business | Build and publish portfolio website |

### ChatGPT Prompt Block
```
I have the following goal: [PASTE GOAL + OUTCOME STATEMENT]

Please help me identify 3–6 projects I need to complete to achieve this goal.
For each project:
1. Write a 1-sentence scope note (what it includes / excludes)
2. Rate it: Critical / Important / Optional
3. Note any dependencies between projects

My context: [SITUATION + TIME AVAILABLE]
```
> 📎 Full prompts: `prompt_library/task_breakdown_prompts.md` — Prompt 1: Project Identification
"""))

    cells.append(md("### 🎯 Activity 3A — Enter Your Projects"))
    cells.append(code("""\
# ✏️ YOUR INPUT — define your projects (from ChatGPT output, edited)

projects = [
    {
        "project_name": "Build Portfolio Website",
        "linked_goal": "Launch a freelance UX business",
        "priority": "High",
        "deadline": "2024-03-15",
        "status": "Active",
        "scope_note": "Design, write, and publish 5 case studies + About page. Excludes testimonials.",
    },
    {
        "project_name": "Client Outreach Campaign",
        "linked_goal": "Launch a freelance UX business",
        "priority": "High",
        "deadline": "2024-04-01",
        "status": "Active",
        "scope_note": "Identify 20 leads, draft outreach messages, track replies. Excludes proposals.",
    },
    {
        "project_name": "Figma Modules 4–8",
        "linked_goal": "Complete Figma Advanced Course",
        "priority": "Medium",
        "deadline": "2024-05-31",
        "status": "Active",
        "scope_note": "Complete remaining 5 course modules and submit final project. Excludes publishing tutorials.",
    },
    # Add more projects here
]

df_proj = pd.DataFrame(projects)
display(Markdown("### 📋 Your Projects Database"))
display(df_proj[["project_name", "linked_goal", "priority", "deadline", "status"]])
"""))

    cells.append(code("""\
# ── Priority check ──
high = [p for p in projects if p["priority"] == "High"]
display(Markdown(f"### ⚡ Priority Summary\\n**High priority projects: {len(high)}**"))
for p in high:
    print(f"  🔴 {p['project_name']} — due {p['deadline']}")
if len(high) > 4:
    print("\\n⚠️  You have many High priority projects. Consider demoting 1–2 to Medium.")
else:
    print("\\n✅ Priority spread looks manageable.")
"""))

    # ── Section 4 ─────────────────────────────────────────────────────────
    cells.append(md("""\
---
## ✅ Session 4 — Tasks: The Atomic Unit of Progress
*Duration: ~60 minutes*

### Concept
A **task** is the smallest unit of action that moves a project forward.

**Good task formula:** `Verb + Object`  
Examples: *Draft homepage copy*, *Review client brief*, *Send invoice to Client A*

Rules for good tasks:
- Completable in one work session (< 2 hours)
- Has a clear "done" definition  
- Verb-first name

### ChatGPT Prompt Block
```
I have the following project: [PROJECT NAME]
Goal it serves: [GOAL]
Scope: [SCOPE NOTE]

Please generate 8–14 tasks needed to complete this project.
For each task:
1. Write a verb-first task name
2. Add a 1-sentence "done" definition
3. Estimate effort: Small (<1hr) / Medium (1–3hr) / Large (3hr+)
4. Note any tasks that are blockers
```
> 📎 Full prompts: `prompt_library/task_breakdown_prompts.md` — Prompt 2: Project-to-Tasks
"""))

    cells.append(md("### 🎯 Activity 4A — Enter Your Tasks"))
    cells.append(code("""\
# ✏️ YOUR INPUT — add your tasks here
# Tip: start with your most active project's tasks

tasks = [
    {"task_name": "Draft homepage case study copy",    "project": "Build Portfolio Website", "priority": "P1", "status": "Not Started", "effort": "Medium", "due": "2024-02-15"},
    {"task_name": "Review and finalise About page",    "project": "Build Portfolio Website", "priority": "P2", "status": "Not Started", "effort": "Small",  "due": "2024-02-16"},
    {"task_name": "Export 3 project images from Figma","project": "Build Portfolio Website", "priority": "P3", "status": "Not Started", "effort": "Small",  "due": "2024-02-20"},
    {"task_name": "Publish portfolio to live site",    "project": "Build Portfolio Website", "priority": "P2", "status": "Blocked",     "effort": "Medium", "due": "2024-03-01"},
    {"task_name": "Identify 20 outreach leads",        "project": "Client Outreach Campaign","priority": "P2", "status": "Not Started", "effort": "Medium", "due": "2024-02-20"},
    {"task_name": "Draft 3 outreach email templates",  "project": "Client Outreach Campaign","priority": "P2", "status": "Not Started", "effort": "Small",  "due": "2024-02-22"},
    {"task_name": "Complete Figma Module 4",           "project": "Figma Modules 4–8",       "priority": "P3", "status": "Not Started", "effort": "Large",  "due": "2024-03-15"},
    {"task_name": "Complete Figma Module 5",           "project": "Figma Modules 4–8",       "priority": "P3", "status": "Not Started", "effort": "Large",  "due": "2024-03-30"},
    # ✏️ Add at least 10 tasks total
]

df_tasks = pd.DataFrame(tasks)
display(Markdown("### ✅ Your Task Database"))
display(df_tasks[["task_name", "project", "priority", "effort", "status", "due"]])
print(f"\\nTotal tasks entered: {len(tasks)}")
"""))

    cells.append(code("""\
# ── System health snapshot ──
display(Markdown("### 🏥 Day 1 System Health Snapshot"))

total_goals    = len(goals)
total_projects = len(projects)
total_tasks    = len(tasks)
blocked_tasks  = len([t for t in tasks if t["status"] == "Blocked"])

health_data = {
    "Layer":  ["Goals", "Projects", "Tasks", "Blocked Tasks"],
    "Count":  [total_goals, total_projects, total_tasks, blocked_tasks],
    "Target": ["3–5", "2–4 active", "10+", "0–2"],
}
display(pd.DataFrame(health_data))

if total_tasks >= 10 and total_projects >= 2 and total_goals >= 2:
    print("\\n✅ Day 1 complete! Your system foundation is in place.")
    print("   Copy your tables into your Notion databases before tomorrow.")
else:
    print("\\n⚠️  Keep going — aim for 3+ goals, 2+ projects, and 10+ tasks.")
"""))

    # ── Reflection ────────────────────────────────────────────────────────
    cells.append(md("""\
---
## 📔 Day 1 Reflection
*Aligned with: `student_materials/reflection_templates/daily_checkin.md`*
"""))
    cells.append(code("""\
# ✏️ YOUR INPUT — complete your Day 1 reflection

reflection = {
    "what_i_built":    "Goals Database with 3 goals, Projects Database with 3 projects, 8 tasks entered.",
    "what_surprised":  "I had more vague goals than I thought — most needed significant sharpening.",
    "what_is_unclear": "How tightly should success criteria be defined? Can they evolve?",
    "tomorrow_focus":  "Set up milestones for my most important project.",
}

display(Markdown("### 📔 Day 1 Daily Check-In"))
for k, v in reflection.items():
    label = k.replace("_", " ").capitalize()
    display(Markdown(f"**{label}:** *{v}*"))

display(Markdown("---\\n> 💡 Save this notebook. On Day 4, you will reference this reflection during your retrospective."))
"""))

    cells.append(md("""\
---
## 🏁 Day 1 Deliverables Checklist

| Deliverable | Where it lives |
|-------------|---------------|
| Goals table (3+ goals with success criteria) | This notebook + Notion Goals Database |
| Projects table (2+ projects linked to goals) | This notebook + Notion Projects Database |
| Task table (10+ tasks linked to projects) | This notebook + Notion Task Database |
| Day 1 Reflection | Reflection cell above |

**Tomorrow:** Day 2 — Prioritization, Milestones, Reverse Planning, and Attention Budgeting.

> 📎 Repo references used today:
> - `prompt_library/goal_design_prompts.md`
> - `prompt_library/task_breakdown_prompts.md`
> - `templates/notion_blueprint.md`
> - `templates/task_template.csv`
> - `student_materials/student_task_sheets/day_1_tasks.md`
"""))

    return nb(cells, title="Day 1 — Foundation")


# ══════════════════════════════════════════════════════════════════════════════
# DAY 2 — Prioritization, Milestones, Reverse Planning, Attention Budget
# ══════════════════════════════════════════════════════════════════════════════

def build_day2():
    cells = []

    cells.append(md("""\
# 🎯 Day 2 — Prioritization, Milestones & Attention Budgeting
## Building a Personal Productivity System with AI

**Estimated duration:** 5 hours (with breaks)  
**Prerequisite:** Day 1 notebook complete — you have goals, projects, and tasks defined.

---

### What you will do today
| Session | Outcome |
|---------|---------|
| Session 1 | Map milestones and use reverse planning |
| Session 2 | Prioritize your task list using the P1–P4 framework |
| Session 3 | Build your Anti-To-Do log |
| Session 4 | Create your Attention Budget and compare ideal vs actual |

> **Tip:** Work from Day 1's task list. Copy it into this notebook's input cells.
---
"""))

    cells.append(md("## ⚙️ Setup"))
    cells.append(code("""\
import pandas as pd
from datetime import datetime, timedelta
from IPython.display import display, Markdown

pd.set_option("display.max_colwidth", 80)
today = datetime.today().date()
print(f"✅ Setup complete. Today is {today}.")
"""))

    # ── Session 1: Milestones ───────────────────────────────────────────────
    cells.append(md("""\
---
## 🗓️ Session 1 — Milestones & Reverse Planning
*Duration: ~60 minutes*

### Concept
A **milestone** is a named, verifiable checkpoint — the moment you can say *"this phase is done."*

| | Task | Milestone | Project |
|--|------|-----------|---------|
| Size | Smallest | Medium | Largest |
| Done when | Action complete | Phase complete | Deliverable produced |
| Example | "Draft About page" | "All case studies written and approved" | "Portfolio live" |

### Reverse Planning
Working backwards from a deadline:
1. Start at the completion date
2. Assign the last milestone a date 1–2 weeks before completion
3. Work backwards, leaving realistic gaps between each milestone

### ChatGPT Prompt Block
```
I have a project: [PROJECT NAME]
Milestones:
1. [MILESTONE 1]
2. [MILESTONE 2]
3. [MILESTONE 3]
Completion date: [DATE]

Please assign realistic target dates by working backwards.
Flag any milestone that looks too compressed.
Tell me what I should have done by [TODAY'S DATE] to stay on track.
```
> 📎 Repo prompt: `task_breakdown_prompts.md` — Prompt 3: Milestone Generation  
> 📎 Repo prompt: `prioritization_prompts.md` — Prompt 3: Reverse Planning (also in `task_breakdown_prompts.md` Prompt 4)
"""))

    cells.append(md("### 🎯 Activity 1A — Define Milestones for Your Key Project"))
    cells.append(code("""\
# ✏️ YOUR INPUT — define milestones for your most important project

project_name   = "Build Portfolio Website"
completion_date = "2024-03-15"   # YYYY-MM-DD

milestones = [
    {"milestone": "Outline and structure for all 5 case studies agreed",  "target_date": "2024-02-10", "status": "Done"},
    {"milestone": "All 5 case study drafts written",                      "target_date": "2024-02-24", "status": "In Progress"},
    {"milestone": "Images, design, and About page finalised",             "target_date": "2024-03-05", "status": "Not Started"},
    {"milestone": "Portfolio reviewed and feedback incorporated",          "target_date": "2024-03-10", "status": "Not Started"},
    {"milestone": "Portfolio live and URL shared",                        "target_date": "2024-03-15", "status": "Not Started"},
]

df_m = pd.DataFrame(milestones)
display(Markdown(f"### 📍 Milestone Map: {project_name}"))
display(df_m)

# ── Reverse planning check ──
end = datetime.strptime(completion_date, "%Y-%m-%d").date()
days_left = (end - today).days
print(f"\nCompletion date: {completion_date}")
print(f"Days remaining: {days_left}")
"""))

    cells.append(code("""\
# ── On-track check ──
display(Markdown("### 🔍 On-Track Analysis"))
for m in milestones:
    m_date = datetime.strptime(m["target_date"], "%Y-%m-%d").date()
    is_past = m_date < today
    is_done = m["status"] == "Done"
    if is_past and not is_done:
        print(f"⚠️  OVERDUE — '{m['milestone']}' was due {m['target_date']} and is {m['status']}")
    elif not is_past and m["status"] == "Not Started":
        days_until = (m_date - today).days
        print(f"📅 Upcoming in {days_until} days — '{m['milestone']}'")
    elif is_done:
        print(f"✅ Done — '{m['milestone']}'")
"""))

    # ── Session 2: Priority ─────────────────────────────────────────────────
    cells.append(md("""\
---
## ⚡ Session 2 — Task Prioritization
*Duration: ~60 minutes*

### Concept — The P1–P4 Framework

| Priority | Label | Meaning |
|----------|-------|---------|
| **P1** | Critical | Must be done today. Blocking others or zero-slack deadline. |
| **P2** | High | Must be done this week. Significant consequence if delayed. |
| **P3** | Medium | Important but not urgent. Can be done this week or next. |
| **P4** | Low | Low consequence if deferred. Do when time permits. |

> **Rule:** P1 should have **maximum 2 tasks** at any time. If you have 3+ P1 tasks, demote the least critical one.

### ChatGPT Prompt Block
```
Here is my current task list: [PASTE TASKS]

My context:
- Top 2 active projects: [PROJECTS]
- Deadlines this week: [DEADLINES]
- One task I've been avoiding: [TASK]

Categorise each task as P1/P2/P3/P4.
Important: P1 should have no more than 2 tasks. Flag if there are more.
```
> 📎 Repo prompt: `prompt_library/prioritization_prompts.md` — Prompt 1: Task Prioritization
"""))

    cells.append(md("### 🎯 Activity 2A — Prioritize Your Tasks"))
    cells.append(code("""\
# ✏️ YOUR INPUT — paste your tasks here with ChatGPT-suggested priorities (then edit)

tasks = [
    {"task_name": "Send Brand Guidelines v1 to Client A",     "project": "Client Work",          "priority": "P1", "due": "2024-02-14", "status": "In Progress"},
    {"task_name": "Draft homepage case study copy",            "project": "Portfolio Website",    "priority": "P1", "due": "2024-02-15", "status": "Not Started"},
    {"task_name": "Review and finalise About page",            "project": "Portfolio Website",    "priority": "P2", "due": "2024-02-16", "status": "Not Started"},
    {"task_name": "Identify 20 outreach leads",               "project": "Client Outreach",      "priority": "P2", "due": "2024-02-20", "status": "Not Started"},
    {"task_name": "Draft 3 outreach email templates",         "project": "Client Outreach",      "priority": "P2", "due": "2024-02-22", "status": "Not Started"},
    {"task_name": "Export 3 project images from Figma",       "project": "Portfolio Website",    "priority": "P3", "due": "2024-02-20", "status": "Not Started"},
    {"task_name": "Complete Figma Module 4",                  "project": "Figma Course",         "priority": "P3", "due": "2024-03-15", "status": "Not Started"},
    {"task_name": "Write February newsletter issue outline",  "project": "Newsletter",           "priority": "P3", "due": "2024-02-28", "status": "Not Started"},
    {"task_name": "File Q4 expenses",                         "project": "Admin",                "priority": "P4", "due": "2024-03-01", "status": "Not Started"},
]

df_tasks = pd.DataFrame(tasks)
for tier in ["P1", "P2", "P3", "P4"]:
    t = df_tasks[df_tasks["priority"] == tier]
    icon = {"P1": "🔴", "P2": "🟠", "P3": "🟡", "P4": "⚪"}[tier]
    label = {"P1": "Critical", "P2": "High", "P3": "Medium", "P4": "Low"}[tier]
    display(Markdown(f"**{icon} {tier} — {label} ({len(t)} tasks)**"))
    if len(t): display(t[["task_name", "project", "due"]])

if len(df_tasks[df_tasks["priority"] == "P1"]) > 2:
    print("⚠️  WARNING: More than 2 P1 tasks. Demote the least critical one to P2.")
else:
    print("✅ P1 count is within the 2-task limit.")
"""))

    # ── Session 3: Anti-To-Do ───────────────────────────────────────────────
    cells.append(md("""\
---
## ✅ Session 3 — The Anti-To-Do Log
*Duration: ~45 minutes*

### Concept
The **Anti-To-Do Log** is a record of what you *actually completed* — the opposite of a to-do list.

**Why it matters:**
- Most people underestimate how much they accomplish
- The Anti-To-Do log is the raw data source for your weekly review
- It's the antidote to feeling "unproductive" despite doing real work

**Entry format:** `[Action verb] + [what] + [why it counts]`  
Examples:
- *"Sent Brand Guidelines v1 to Client A — unblocks client feedback cycle"*
- *"Declined underpriced project from Client D — protected time for portfolio work"*
- *"Completed Figma Module 4 — 50% of course done"*

> 📎 See `student_materials/reflection_templates/daily_checkin.md` for the full check-in template
"""))

    cells.append(md("### 🎯 Activity 3A — Log Today's Anti-To-Do Entries"))
    cells.append(code("""\
# ✏️ YOUR INPUT — log everything you completed today (or this week)
# Use verb-first entries. Be specific. Include decisions and communications.

anti_todo = [
    {"date": str(today), "entry": "Sent Brand Guidelines draft to Client A — unblocks milestone",  "category": "Work"},
    {"date": str(today), "entry": "Reviewed and replied to 8 emails — inbox cleared",               "category": "Admin"},
    {"date": str(today), "entry": "Completed Day 1 notebook and entered data into Notion",          "category": "Learning"},
    # ✏️ Add your own entries here
]

df_anti = pd.DataFrame(anti_todo)
display(Markdown(f"### ✅ Anti-To-Do Log — {today}"))
display(df_anti)

print(f"\nEntries today: {len(anti_todo)}")
by_cat = df_anti.groupby("category").size()
display(Markdown("**By category:**"))
display(by_cat.to_frame("count"))
"""))

    # ── Session 4: Attention Budget ─────────────────────────────────────────
    cells.append(md("""\
---
## 💡 Session 4 — Attention Budget
*Duration: ~60 minutes*

### Concept
Your **Attention Budget** is the deliberate allocation of your focused work hours across domains of your life.

Most people discover (when they actually measure) that:
- **Admin** consumes 2–3x more time than intended
- **Strategic thinking** gets almost no protected time
- **Side projects** receive "whatever is left" — which is usually nothing

### How to measure
Use your **Work Session Log** (from `templates/work_session_log_template.csv`) to record:
- What you worked on
- How long you worked
- Which domain it belongs to

Then compare against your **ideal** allocation.

> 📎 Full prompt: `prompt_library/prioritization_prompts.md` — Prompt 4: Attention Budget Analysis
"""))

    cells.append(md("### 🎯 Activity 4A — Set Your Ideal Attention Budget"))
    cells.append(code("""\
# ✏️ YOUR INPUT — set your ideal allocation (must total 100%)

ideal_budget = {
    "Client Work / Main Job": 45,
    "Side Projects / Own Work": 25,
    "Learning": 15,
    "Admin & Email": 10,
    "Strategic Thinking": 5,
}

# ── Validate ──
total = sum(ideal_budget.values())
display(Markdown("### 💡 Your Ideal Attention Budget"))
df_ideal = pd.DataFrame(list(ideal_budget.items()), columns=["Domain", "Ideal (%)"])
display(df_ideal)
if total != 100:
    print(f"⚠️  Your allocations sum to {total}%. Please adjust to total exactly 100%.")
else:
    print("✅ Budget totals 100%. Looks good.")
"""))

    cells.append(md("### 🎯 Activity 4B — Log Actual Hours and Compare"))
    cells.append(code("""\
# ✏️ YOUR INPUT — log your actual work sessions from the past 3–5 days
# Format: (domain, hours_worked)
# Domain names must match exactly what you used in ideal_budget above

work_sessions = [
    ("Client Work / Main Job",     2.5),
    ("Client Work / Main Job",     3.0),
    ("Admin & Email",              1.0),
    ("Admin & Email",              1.5),
    ("Side Projects / Own Work",   0.5),
    ("Learning",                   0.0),
    ("Strategic Thinking",         0.0),
    # ✏️ Add more sessions from your work session log
]

# ── Calculate actual allocation ──
from collections import defaultdict
actual_hours = defaultdict(float)
for domain, hrs in work_sessions:
    actual_hours[domain] += hrs

total_hours = sum(actual_hours.values())
actual_pct = {d: round((h / total_hours) * 100, 1) for d, h in actual_hours.items()} if total_hours else {}

# ── Comparison table ──
rows = []
for domain, ideal_pct in ideal_budget.items():
    actual = actual_pct.get(domain, 0.0)
    gap = actual - ideal_pct
    flag = "⚠️ Over" if gap > 10 else ("📉 Under" if gap < -10 else "✅ OK")
    rows.append({"Domain": domain, "Ideal (%)": ideal_pct, "Actual (%)": actual, "Gap": gap, "Status": flag})

df_compare = pd.DataFrame(rows)
display(Markdown("### 📊 Ideal vs Actual Attention Allocation"))
display(df_compare)
display(Markdown(f"*Total hours logged: {total_hours:.1f}h across {len(work_sessions)} sessions*"))
"""))

    cells.append(code("""\
# ── Attention insight ──
display(Markdown("### 💬 Attention Budget Insight"))
over  = df_compare[df_compare["Gap"] >  10]
under = df_compare[df_compare["Gap"] < -10]

if len(over):
    print("🔴 Over-invested domains (consuming more than ideal):")
    for _, r in over.iterrows():
        print(f"   {r['Domain']}: {r['Actual (%)']}% vs {r['Ideal (%)']}% ideal (+{r['Gap']:.0f}%)")

if len(under):
    print("\\n📉 Under-invested domains (getting less than ideal):")
    for _, r in under.iterrows():
        print(f"   {r['Domain']}: {r['Actual (%)']}% vs {r['Ideal (%)']}% ideal ({r['Gap']:.0f}%)")

if not len(over) and not len(under):
    print("✅ Your actual allocation is close to ideal. Well balanced.")

print("\\n💡 ChatGPT prompt to go deeper:")
print("   → prompt_library/prioritization_prompts.md — Prompt 4: Attention Budget Analysis")
"""))

    # ── Reflection ─────────────────────────────────────────────────────────
    cells.append(md("---\n## 📔 Day 2 Reflection"))
    cells.append(code("""\
# ✏️ YOUR INPUT

reflection_d2 = {
    "biggest_priority_insight": "I had 4 P1 tasks — demoted 2. That forced an honest decision.",
    "attention_gap":            "Admin is eating 30% of my time vs 10% ideal.",
    "one_change_next_week":     "No email before 10am — protect morning for P1 tasks.",
    "tomorrow_focus":           "Build Kanban view in Notion and set up dashboard.",
}

display(Markdown("### 📔 Day 2 Daily Check-In"))
for k, v in reflection_d2.items():
    display(Markdown(f"**{k.replace('_',' ').capitalize()}:** *{v}*"))
"""))

    cells.append(md("""\
---
## 🏁 Day 2 Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| Milestone map for key project | ☐ |
| Prioritized task list (P1–P4) | ☐ |
| Anti-To-Do log (today's entries) | ☐ |
| Attention budget (ideal vs actual) | ☐ |

> 📎 Repo references today:
> - `prompt_library/prioritization_prompts.md`
> - `prompt_library/task_breakdown_prompts.md`
> - `templates/work_session_log_template.csv`
> - `templates/attention_budget_template.csv`
> - `student_materials/student_task_sheets/day_2_tasks.md`
"""))

    return nb(cells, title="Day 2 — Prioritization")


# ══════════════════════════════════════════════════════════════════════════════
# DAY 3 — Dashboard UX, Kanban, Streaks
# ══════════════════════════════════════════════════════════════════════════════

def build_day3():
    cells = []

    cells.append(md("""\
# 📊 Day 3 — Dashboard, Kanban & Streak Tracking
## Building a Personal Productivity System with AI

**Estimated duration:** 5 hours (with breaks)  
**Prerequisite:** Days 1 & 2 complete — goals, projects, tasks, and priorities defined.

---

### What you will do today
| Session | Outcome |
|---------|---------|
| Session 1 | Build a Kanban workflow view |
| Session 2 | Create dashboard-style summaries |
| Session 3 | Set up your Streak Tracker |
| Session 4 | Run the 5-second load test and dashboard UX audit |
---
"""))

    cells.append(md("## ⚙️ Setup"))
    cells.append(code("""\
import pandas as pd
from datetime import datetime, timedelta
from IPython.display import display, Markdown

pd.set_option("display.max_colwidth", 80)
today = datetime.today().date()
print(f"✅ Setup complete. Today is {today}.")
"""))

    # ── Session 1: Kanban ───────────────────────────────────────────────────
    cells.append(md("""\
---
## 🗂️ Session 1 — Kanban: Task Flow Made Visible
*Duration: ~60 minutes*

### Concept
A **Kanban board** makes work-in-progress visible by showing tasks as cards moving through workflow stages.

### Default stages for this course:
| Stage | What goes here | WIP Limit |
|-------|---------------|-----------|
| 📌 Backlog | All captured tasks, not yet committed | Unlimited |
| 📋 This Week | Tasks committed to for this week | 7–10 |
| ⚡ In Progress | Actively being worked on right now | **Max 3** |
| 🔴 Blocked | Cannot proceed — waiting on something external | — |
| ✅ Done | Completed this week | — |

> **WIP limit = 3** on "In Progress". This is a commitment, not a suggestion.  
> If you want to add a 4th, something must move to Done first.

> 📎 Full stage guide: `templates/kanban_structure.md`
"""))

    cells.append(md("""\
### 🎯 Activity 1A — Build Your Kanban View
> 📎 Extension prompt: `system_optimization_prompts.md` — Prompt 3: Kanban Design Prompt
"""))
    cells.append(code("""\
# ✏️ YOUR INPUT — assign statuses to your tasks

tasks = [
    {"task_name": "Send Brand Guidelines v1",           "project": "Client Work",       "priority": "P1", "status": "In Progress"},
    {"task_name": "Draft homepage case study copy",     "project": "Portfolio Website",  "priority": "P1", "status": "In Progress"},
    {"task_name": "Review and finalise About page",     "project": "Portfolio Website",  "priority": "P2", "status": "This Week"},
    {"task_name": "Identify 20 outreach leads",         "project": "Client Outreach",   "priority": "P2", "status": "This Week"},
    {"task_name": "Draft 3 outreach email templates",   "project": "Client Outreach",   "priority": "P2", "status": "This Week"},
    {"task_name": "Publish portfolio to live site",     "project": "Portfolio Website",  "priority": "P2", "status": "Blocked"},
    {"task_name": "Export 3 project images from Figma", "project": "Portfolio Website",  "priority": "P3", "status": "Backlog"},
    {"task_name": "Complete Figma Module 4",            "project": "Figma Course",       "priority": "P3", "status": "Backlog"},
    {"task_name": "Write February newsletter outline",  "project": "Newsletter",         "priority": "P3", "status": "Backlog"},
    {"task_name": "File Q4 expenses",                   "project": "Admin",              "priority": "P4", "status": "Backlog"},
]

stages = ["Backlog", "This Week", "In Progress", "Blocked", "Done"]
icons  = {"Backlog": "📌", "This Week": "📋", "In Progress": "⚡", "Blocked": "🔴", "Done": "✅"}

df = pd.DataFrame(tasks)
display(Markdown("## 🗂️ Your Kanban Board"))
for stage in stages:
    subset = df[df["status"] == stage]
    display(Markdown(f"### {icons[stage]} {stage} ({len(subset)} tasks)"))
    if len(subset):
        display(subset[["task_name", "project", "priority"]].reset_index(drop=True))

# WIP check
wip = df[df["status"] == "In Progress"]
if len(wip) > 3:
    print(f"\\n⚠️  WIP LIMIT EXCEEDED: {len(wip)} tasks In Progress (max 3). Move one to Done or Blocked.")
else:
    print(f"\\n✅ WIP is {len(wip)}/3 — within limit.")
"""))

    # ── Session 2: Dashboard Summary ────────────────────────────────────────
    cells.append(md("""\
---
## 📊 Session 2 — Dashboard Summary View
*Duration: ~60 minutes*

### Concept
Your **Master Dashboard** should answer one question above all others:  
**"What do I do right now?"**

It must pass the **5-second load test**: can you identify your single most important task within 5 seconds of opening it?

### The five dashboard sections (from `templates/dashboard_blueprint.md`)
1. 🎯 **Today's Focus** — tasks due today or Priority = P1
2. 🗂️ **Active Projects** — projects with Status = Active
3. 📅 **This Week** — tasks due within 7 days, sorted by priority
4. ✅ **Shipped Today** — Anti-To-Do entries for today
5. 🔥 **Today's Habits** — Streak Tracker entries for today
"""))

    cells.append(md("### 🎯 Activity 2A — Generate Your Dashboard Summary"))
    cells.append(code("""\
# ✏️ YOUR INPUT — paste your current data

projects = [
    {"project_name": "Build Portfolio Website",  "priority": "High",   "deadline": "2024-03-15", "status": "Active"},
    {"project_name": "Client Outreach Campaign", "priority": "High",   "deadline": "2024-04-01", "status": "Active"},
    {"project_name": "Figma Modules 4–8",        "priority": "Medium", "deadline": "2024-05-31", "status": "Active"},
]

anti_todo_today = [
    "Sent Brand Guidelines draft to Client A",
    "Cleared inbox — 12 emails processed",
    "Completed Day 2 notebook activities",
]

# ── Today's Focus ──
today_str = str(today)
todays_focus = [t for t in tasks if t["priority"] == "P1" or t.get("due") == today_str]
this_week    = [t for t in tasks if t["status"] in ["This Week", "In Progress"]]

display(Markdown("---"))
display(Markdown(f"# 🏠 Mission Control — {today}"))

display(Markdown("## 🎯 Today's Focus"))
if todays_focus:
    for t in todays_focus:
        display(Markdown(f"- **{t['priority']}** {t['task_name']} *(→ {t['project']})*"))
else:
    display(Markdown("*No P1 tasks — check your This Week column.*"))

display(Markdown("\\n## 🗂️ Active Projects"))
for p in projects:
    if p["status"] == "Active":
        display(Markdown(f"- **{p['priority']}** · {p['project_name']} · Due {p['deadline']}"))

display(Markdown("\\n## 📅 This Week"))
for t in this_week:
    display(Markdown(f"- [{t['status']}] {t['task_name']} — {t['priority']}"))

display(Markdown("\\n## ✅ Shipped Today"))
for entry in anti_todo_today:
    display(Markdown(f"- {entry}"))
"""))

    cells.append(code("""\
# ── 5-Second Load Test ──
display(Markdown("---\\n### ⏱️ 5-Second Load Test"))
p1 = [t for t in tasks if t["priority"] == "P1"]
if p1:
    first_p1 = p1[0]["task_name"]
    print(f"✅ Your #1 task is immediately identifiable: '{first_p1}'")
    print("   Test: Close this notebook. Reopen it. Find this task in < 5 seconds.")
else:
    print("⚠️  No P1 tasks defined. Your dashboard won't pass the load test.")
    print("   Go back to your task list and assign at least 1 P1 task.")
"""))

    # ── Session 3: Streak Tracker ────────────────────────────────────────────
    cells.append(md("""\
---
## 🔥 Session 3 — Streak Tracker & Habit Consistency
*Duration: ~45 minutes*

### Concept
The **Streak Tracker** records whether you completed a daily process habit on a given day.

**Track process habits, not outcome targets:**
- ✅ "Did I complete my morning planning?" — trackable
- ❌ "Did I earn £500 today?" — not a process habit

### How to choose 2–3 habits to track
From `templates/streak_tracker_structure.md`:

| Habit | Why |
|-------|-----|
| Morning Planning (15 min) | Sets direction before reactive work begins |
| Anti-To-Do update | Keeps completed work visible |
| End-of-Day Reflection | Closes the mental loop |
| Weekly Review | Prevents project drift |

> **Start with 2 habits only. Add a 3rd only after 3 weeks of consistency.**
"""))

    cells.append(md("""\
### 🎯 Activity 3A — Log Your Streak Data
> 📎 Extension prompt: `system_optimization_prompts.md` — Prompt 4: Habit Design Prompt
"""))
    cells.append(code("""\
# ✏️ YOUR INPUT
# habits = the 2–3 habits you are tracking
# For each day, fill in True/False for each habit

my_habits = ["Morning Planning", "Anti-To-Do Update"]

# Format: (date_string, habit_name, completed)
streak_log = [
    ("2024-02-12", "Morning Planning",    True),
    ("2024-02-12", "Anti-To-Do Update",   True),
    ("2024-02-13", "Morning Planning",    False),
    ("2024-02-13", "Anti-To-Do Update",   True),
    ("2024-02-14", "Morning Planning",    True),
    ("2024-02-14", "Anti-To-Do Update",   True),
    (str(today),   "Morning Planning",    True),
    (str(today),   "Anti-To-Do Update",   False),
    # ✏️ Add more entries as you go
]

df_streak = pd.DataFrame(streak_log, columns=["Date", "Habit", "Completed"])

display(Markdown("### 🔥 Your Streak Tracker"))
pivot = df_streak.pivot_table(index="Date", columns="Habit", values="Completed", aggfunc="first")
display(pivot.replace({True: "✅", False: "❌", None: "—"}))

# ── Streak counts ──
display(Markdown("\\n**Completion rates:**"))
for habit in my_habits:
    h_data = df_streak[df_streak["Habit"] == habit]
    rate = h_data["Completed"].mean() * 100
    print(f"  {habit}: {rate:.0f}% ({h_data['Completed'].sum()}/{len(h_data)} days)")
"""))

    # ── Session 4: UX Audit ─────────────────────────────────────────────────
    cells.append(md("""\
---
## 🔍 Session 4 — Dashboard UX Audit
*Duration: ~30 minutes*

### Concept
After building your dashboard, audit it for usability:

| Principle | Question |
|-----------|----------|
| Load test | Can you find your #1 task in < 5 seconds? |
| Signal-to-noise | Are there sections you always skip? |
| Click efficiency | Can you open a specific task in ≤ 3 clicks? |
| Label clarity | Are all section headings self-explanatory? |

### ChatGPT Prompt Block
```
My Notion dashboard sections:
[Describe each section — what database, what filter, what view type]

Please evaluate against:
1. Load test (5-second rule)
2. Signal-to-noise ratio
3. Click efficiency
4. Label clarity

Give me: keep / simplify / remove for each section, plus 2 improvements.
```
> 📎 Repo prompt: `prompt_library/system_optimization_prompts.md` — Prompt 2: Dashboard UX Audit
"""))

    cells.append(md("### 🎯 Activity 4A — Self-Audit Your Dashboard"))
    cells.append(code("""\
# ✏️ YOUR INPUT — score your Notion dashboard sections
# Rate each section: 1 = never use it, 5 = use it every session

dashboard_sections = [
    {"section": "Today's Focus",    "uses_daily": True,  "clarity": 5, "keep": "Yes"},
    {"section": "Active Projects",  "uses_daily": True,  "clarity": 4, "keep": "Yes"},
    {"section": "This Week",        "uses_daily": True,  "clarity": 5, "keep": "Yes"},
    {"section": "Shipped Today",    "uses_daily": False, "clarity": 3, "keep": "Simplify"},
    {"section": "Full Task Table",  "uses_daily": False, "clarity": 3, "keep": "Remove"},
    # ✏️ Add your own sections here
]

df_audit = pd.DataFrame(dashboard_sections)
display(Markdown("### 🔍 Dashboard Section Audit"))
display(df_audit)

keep    = df_audit[df_audit["keep"] == "Yes"]
simplify = df_audit[df_audit["keep"] == "Simplify"]
remove  = df_audit[df_audit["keep"] == "Remove"]

print(f"\\n✅ Keep: {len(keep)} sections")
print(f"🔧 Simplify: {len(simplify)} sections")
print(f"🗑️  Remove: {len(remove)} sections")

if len(remove):
    print("\\nSections to remove:")
    for _, r in remove.iterrows():
        print(f"  ✗ {r['section']}")
"""))

    # ── Reflection ─────────────────────────────────────────────────────────
    cells.append(md("---\n## 📔 Day 3 Reflection"))
    cells.append(code("""\
# ✏️ YOUR INPUT

reflection_d3 = {
    "kanban_insight":       "I realised I had 5 In Progress tasks. Cut to 3 — immediately felt clearer.",
    "dashboard_change":     "Removed the full task table from my dashboard. It was noise.",
    "streak_habit_1":       "Morning Planning",
    "streak_habit_2":       "Anti-To-Do Update",
    "tomorrow_focus":       "Day 4 — set up my daily planning ritual and run my first weekly review.",
}

display(Markdown("### 📔 Day 3 Daily Check-In"))
for k, v in reflection_d3.items():
    display(Markdown(f"**{k.replace('_',' ').capitalize()}:** *{v}*"))
"""))

    cells.append(md("""\
---
## 🏁 Day 3 Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| Kanban board populated and WIP within limit | ☐ |
| Dashboard summary generated in notebook | ☐ |
| Streak tracker set up with 2 habits | ☐ |
| Dashboard UX audit completed | ☐ |

> 📎 Repo references today:
> - `templates/kanban_structure.md`
> - `templates/dashboard_blueprint.md`
> - `templates/streak_tracker_structure.md`
> - `prompt_library/system_optimization_prompts.md`
> - `student_materials/student_task_sheets/day_3_tasks.md`
"""))

    return nb(cells, title="Day 3 — Dashboard & Tracking")


# ══════════════════════════════════════════════════════════════════════════════
# DAY 4 — AI Review, Daily Planning, Weekly Review, Capstone
# ══════════════════════════════════════════════════════════════════════════════

def build_day4():
    cells = []

    cells.append(md("""\
# 🤖 Day 4 — AI Review, Daily Planning & Capstone
## Building a Personal Productivity System with AI

**Estimated duration:** 5 hours (including capstone)  
**Prerequisite:** Days 1–3 complete.

---

### What you will do today
| Session | Outcome |
|---------|---------|
| Session 1 | Define your AI productivity assistant prompt |
| Session 2 | Run your first morning planning ritual |
| Session 3 | Complete your first weekly review |
| Session 4 | Run a system retrospective and capstone presentation |

> Today is the integration day. You will run the system end-to-end for the first time.
---
"""))

    cells.append(md("## ⚙️ Setup"))
    cells.append(code("""\
import pandas as pd
from datetime import datetime, timedelta
from IPython.display import display, Markdown

pd.set_option("display.max_colwidth", 100)
today = datetime.today().date()
print(f"✅ Setup complete. Today is {today} — Day 4.")
"""))

    # ── Session 1: AI Productivity Prompt ───────────────────────────────────
    cells.append(md("""\
---
## 🤖 Session 1 — Your AI Productivity Assistant Prompt
*Duration: ~45 minutes*

### Concept
By Day 4, you have built a complete productivity system. Now you build the **AI layer** that runs on top of it.

Your **AI productivity assistant prompt** is a standing context block you paste at the start of any ChatGPT session. It tells ChatGPT:
- Who you are
- What your active goals and projects are
- What your current priority is
- What kind of help you want

This transforms ChatGPT from a generic assistant into a personalised thinking partner that knows your system.

### The Daily Planning Ritual
Every morning (10–15 minutes):
1. Open Notion dashboard
2. Open ChatGPT
3. Paste your assistant prompt (with today's update)
4. Generate your daily plan
5. Edit and commit the plan to a Notion Daily Note

> 📎 Full prompts: `prompt_library/daily_planning_prompts.md`
"""))

    cells.append(md("""\
### 🎯 Activity 1A — Set Up Your AI Context + Run Your Morning Planning Session
"""))
    cells.append(code("""\
# ✏️ YOUR INPUT — fill in your personal context

my_name          = "Alex"
my_role          = "Freelance UX designer"
my_top_goal      = "Launch a freelance UX business with 3 paying clients by December 31st"
my_active_projects = [
    "Build Portfolio Website (due March 15)",
    "Client Outreach Campaign (due April 1)",
]
my_top_priority_today = "Draft homepage case study copy (P1 — blocked on client sign-off)"
my_available_hours = 5
my_energy_today    = 4   # 1–5
my_constraints     = "Client call at 2pm (1 hr). Hard stop at 6pm."
my_request         = "Help me plan my day and identify what to do first."

# ── Generate your standing prompt ──
lines = [
    "You are my AI productivity assistant. Here is my current context:",
    "",
    f"Name: {my_name}",
    f"Role: {my_role}",
    f"Top Goal: {my_top_goal}",
    "",
    "Active Projects:",
] + [f"- {p}" for p in my_active_projects] + [
    "",
    f"Top priority today: {my_top_priority_today}",
    f"Available hours today: {my_available_hours}",
    f"Energy level (1-5): {my_energy_today}",
    f"Constraints: {my_constraints}",
    "",
    f"Request: {my_request}",
]
assistant_prompt = "\\n".join(lines)

display(Markdown("### 🤖 Your AI Productivity Assistant Prompt"))
display(Markdown("*Copy this into ChatGPT at the start of each planning session:*"))
print(assistant_prompt)
print("\\n✅ Prompt built. Paste it into ChatGPT and run your morning planning session.")
"""))

    # ── Session 2: Daily Planning ────────────────────────────────────────────
    cells.append(md("""\
---
## ☀️ Session 2 — Morning Planning Ritual
*Duration: ~45 minutes*

### Concept
The morning planning ritual is the daily **trigger** that activates your system.

Without it, you open email first and plan reactively.  
With it, you open your dashboard first and plan intentionally.

**Ritual steps (10–15 min daily):**
1. Open Notion → Mission Control dashboard
2. Identify your P1 task for the day
3. Paste your AI assistant prompt into ChatGPT with today's context
4. Review and edit the AI-generated plan
5. Commit the plan to a Daily Note

> 📎 Prompt: `prompt_library/daily_planning_prompts.md` — Prompt 1: Morning Planning
"""))

    cells.append(md("### 🎯 Activity 2A — Generate and Record Your Daily Plan"))
    cells.append(code("""\
# ✏️ YOUR INPUT — record your daily plan (from ChatGPT output, edited)

daily_plan = [
    {"time": "09:00–11:00", "task": "Draft homepage case study copy",    "project": "Portfolio Website", "type": "Deep Work"},
    {"time": "11:00–11:30", "task": "Review and reply to 8 emails",      "project": "Admin",             "type": "Admin"},
    {"time": "11:30–12:00", "task": "Review About page copy",            "project": "Portfolio Website", "type": "Deep Work"},
    {"time": "12:00–13:00", "task": "Lunch / break",                     "project": "—",                 "type": "Break"},
    {"time": "13:00–14:00", "task": "Prepare client call notes",         "project": "Client Work",       "type": "Prep"},
    {"time": "14:00–15:00", "task": "Client call",                       "project": "Client Work",       "type": "Meeting"},
    {"time": "15:00–16:30", "task": "Identify 10 outreach leads",        "project": "Client Outreach",   "type": "Deep Work"},
    {"time": "16:30–17:00", "task": "Day 4 notebook — weekly review",    "project": "Course",            "type": "Learning"},
    {"time": "17:00–17:15", "task": "End-of-day reflection + Anti-To-Do","project": "Admin",             "type": "Ritual"},
]

df_plan = pd.DataFrame(daily_plan)
display(Markdown(f"### ☀️ Daily Plan — {today}"))
display(df_plan[["time", "task", "type"]])

deep = df_plan[df_plan["type"] == "Deep Work"]
admin = df_plan[df_plan["type"] == "Admin"]
print(f"\\nDeep Work blocks: {len(deep)}")
print(f"Admin blocks: {len(admin)}")
print(f"Total planned slots: {len(daily_plan)}")
"""))

    cells.append(md("### 🎯 Activity 2B — End-of-Day Reflection"))
    cells.append(code("""\
# ✏️ YOUR INPUT — complete at end of day (or simulate)

eod_reflection = {
    "planned_vs_completed":  "Completed 6 of 9 slots. Client call overran by 30 min.",
    "what_moved":            "Homepage case study drafted (P1 done!). Outreach leads partially done.",
    "what_didnt_move":       "About page — no time after client call overrun.",
    "focus_quality_1_10":    8,
    "take_to_tomorrow":      "Finish About page (30 min) + 10 more outreach leads.",
    "pattern_to_avoid":      "Scheduling P2 tasks immediately after a variable-length meeting.",
}

display(Markdown(f"### 🌙 End-of-Day Reflection — {today}"))
for k, v in eod_reflection.items():
    label = k.replace("_", " ").capitalize()
    display(Markdown(f"**{label}:** *{v}*"))

# ── Anti-To-Do for today ──
anti_todo = [
    "Drafted homepage case study copy (P1 complete)",
    "Held client call — agreed next milestone",
    "Identified 8 new outreach leads",
    "Completed Day 4 Session 1 + 2",
]
display(Markdown("\\n**✅ Anti-To-Do — shipped today:**"))
for entry in anti_todo:
    display(Markdown(f"- {entry}"))
"""))

    # ── Session 3: Weekly Review ────────────────────────────────────────────
    cells.append(md("""\
---
## 📋 Session 3 — Weekly Review
*Duration: ~60 minutes*

### Concept
The **weekly review** closes the loop on the week. It:
- Surfaces what you actually accomplished (vs. what you planned)
- Identifies the dominant pattern of the week
- Produces 3 concrete intentions for next week

**Six-step weekly review (from `student_materials/reflection_templates/weekly_review.md`):**
1. Clear the decks — close open loops
2. Review Anti-To-Do (what was shipped?)
3. Review projects (which moved, which stalled?)
4. Review attention budget (ideal vs actual)
5. Identify next week's top 3 intentions
6. Use ChatGPT to sense-check the plan

> 📎 Prompt: `prompt_library/review_prompts.md` — Prompt 1: Weekly Review
"""))

    cells.append(md("### 🎯 Activity 3A — Run Your Weekly Review"))
    cells.append(code("""\
# ✏️ YOUR INPUT — fill in your week's data

week_summary = {
    "week_of":      "2024-02-12 to 2024-02-16",
    "anti_todo_entries": [
        "Sent Brand Guidelines v1 to Client A",
        "Drafted homepage case study copy",
        "Reviewed About page copy",
        "Identified 8 outreach leads",
        "Processed 35+ emails",
        "Completed 3 course notebooks",
    ],
    "projects_moved":   ["Build Portfolio Website", "Client Work (Client A)"],
    "projects_stalled": ["Figma Modules 4–8"],
    "projects_blocked": ["Publish portfolio to live site"],
    "attention_ideal": {"Client Work": 45, "Own Work": 25, "Learning": 15, "Admin": 10, "Strategy": 5},
    "attention_actual": {"Client Work": 55, "Own Work": 18, "Learning": 10, "Admin": 15, "Strategy": 2},
    "next_week_intentions": [
        "Finish portfolio case studies and get sign-off",
        "Send first 5 outreach emails",
        "Resume Figma Module 4 (Thursday protected block)",
    ],
}

display(Markdown(f"### 📋 Weekly Review — Week of {week_summary['week_of']}"))

display(Markdown("\\n**✅ Shipped this week:**"))
for e in week_summary["anti_todo_entries"]:
    display(Markdown(f"- {e}"))

display(Markdown("\\n**Project health:**"))
for p in week_summary["projects_moved"]:    print(f"  🟢 Moved: {p}")
for p in week_summary["projects_stalled"]:  print(f"  🟡 Stalled: {p}")
for p in week_summary["projects_blocked"]:  print(f"  🔴 Blocked: {p}")
"""))

    cells.append(code("""\
# ── Attention budget week-over-week ──
display(Markdown("\\n**Attention Budget — Ideal vs Actual:**"))
rows = []
for domain in week_summary["attention_ideal"]:
    ideal  = week_summary["attention_ideal"][domain]
    actual = week_summary["attention_actual"].get(domain, 0)
    gap    = actual - ideal
    rows.append({"Domain": domain, "Ideal (%)": ideal, "Actual (%)": actual, "Gap": gap,
                 "Status": "⚠️ Drift" if abs(gap) > 8 else "✅ OK"})
display(pd.DataFrame(rows))

display(Markdown("\\n**Next week's top 3 intentions:**"))
for i, intention in enumerate(week_summary["next_week_intentions"], 1):
    display(Markdown(f"{i}. {intention}"))
"""))

    # ── Session 4: Retrospective + Capstone ─────────────────────────────────
    cells.append(md("""\
---
## 🔄 Session 4 — System Retrospective & Capstone
*Duration: ~90 minutes*

### Concept
The **system retrospective** evaluates your productivity OS itself — not just what you did, but how well your system is working.

It asks: *"What should I change about the system, not just my work?"*

**Seven-section retrospective (from `student_materials/reflection_templates/retrospective.md`):**
1. System component usage audit
2. Ritual consistency review
3. What's working
4. What's not working
5. One system change to implement now
6. Attention budget adjustment
7. Change log entry

> 📎 Prompt: `prompt_library/system_optimization_prompts.md` — Prompt 1: System Retrospective
"""))

    cells.append(md("### 🎯 Activity 4A — Run Your System Retrospective"))
    cells.append(code("""\
# ✏️ YOUR INPUT — evaluate each system component

components = [
    {"component": "Goals Database",        "usage": "Regular",   "keeping": "Yes",      "note": "3 goals, well-formed"},
    {"component": "Projects Database",     "usage": "Regular",   "keeping": "Yes",      "note": "3 active projects"},
    {"component": "Task Database",         "usage": "Regular",   "keeping": "Yes",      "note": "12 tasks, linked"},
    {"component": "Anti-To-Do Log",        "usage": "Regular",   "keeping": "Yes",      "note": "Updated daily — easy habit"},
    {"component": "Work Session Log",      "usage": "Sometimes", "keeping": "Simplify", "note": "Logging is slow — need shortcut"},
    {"component": "Attention Budget",      "usage": "Sometimes", "keeping": "Yes",      "note": "Useful but only reviewed weekly"},
    {"component": "Kanban Board",          "usage": "Regular",   "keeping": "Yes",      "note": "WIP limit working well"},
    {"component": "Master Dashboard",      "usage": "Regular",   "keeping": "Yes",      "note": "Removed 3 sections — better now"},
    {"component": "Streak Tracker",        "usage": "Sometimes", "keeping": "Yes",      "note": "2 habits tracked, on day 3"},
    {"component": "Daily Planning Ritual", "usage": "Regular",   "keeping": "Yes",      "note": "Takes 12 min — worth it"},
    {"component": "Weekly Review",         "usage": "Not using", "keeping": "Simplify", "note": "This is the first one"},
]

df_retro = pd.DataFrame(components)
display(Markdown("### 🔄 System Component Audit"))
display(df_retro[["component", "usage", "keeping", "note"]])

not_using = df_retro[df_retro["usage"] == "Not using"]
if len(not_using):
    print(f"\\n⚠️  {len(not_using)} components not in use — consider simplifying or removing:")
    for _, r in not_using.iterrows(): print(f"   → {r['component']}: {r['note']}")
"""))

    cells.append(md("### 🎯 Activity 4B — Capstone Summary Export"))
    cells.append(code("""\
# ✏️ YOUR INPUT — complete your capstone summary

capstone = {
    "name":             my_name,
    "date":             str(today),
    "system_version":   "1.0",
    "goals_count":      3,
    "projects_count":   3,
    "tasks_count":      12,
    "most_proud_of":    "Milestone map for Portfolio project — first time I can see the critical path clearly.",
    "biggest_change":   "I now know my actual attention allocation. Admin was 3x what I thought.",
    "one_thing_to_drop":"The Work Session Log in its current form — too slow. Will use a simpler version.",
    "one_thing_to_keep":"Morning Planning ritual — biggest ROI of the four days.",
    "capstone_statement": "I came in with vague ideas. I'm leaving with a structured, working system I'll actually use.",
    "next_30_days_commitment": "Run the weekly review every Friday for 4 consecutive weeks.",
}

display(Markdown(f"# 🎓 Capstone Summary — {capstone['name']}"))
display(Markdown(f"*System v{capstone['system_version']} · {capstone['date']}*"))
display(Markdown("---"))

display(Markdown(f"**System built:**  {capstone['goals_count']} goals · {capstone['projects_count']} projects · {capstone['tasks_count']} tasks"))
display(Markdown(f"\\n**Most proud of:** {capstone['most_proud_of']}"))
display(Markdown(f"\\n**Biggest insight:** {capstone['biggest_change']}"))
display(Markdown(f"\\n**Drop:** {capstone['one_thing_to_drop']}"))
display(Markdown(f"\\n**Keep:** {capstone['one_thing_to_keep']}"))
display(Markdown(f"\\n**Capstone statement:** *{capstone['capstone_statement']}*"))
display(Markdown(f"\\n**30-day commitment:** {capstone['next_30_days_commitment']}"))

display(Markdown("\\n---\\n## ✅ Course Complete"))
display(Markdown("> Your system is live. Your first weekly review is done. Your streak tracker is running.  \\n> The only thing left is to show up tomorrow morning and run the ritual."))
"""))

    # ── Reflection ─────────────────────────────────────────────────────────
    cells.append(md("---\n## 📔 Final Reflection — Looking Back to Day 1"))
    cells.append(code("""\
# ── Compare Day 1 starting state to now ──
display(Markdown("### 📔 Day 1 → Day 4: What Changed?"))

# ✏️ Fill in your Day 1 starting state (from your Day 1 notebook reflection cell)
day1_org_score       = 2
day1_frustration     = "I lose track of what I'm supposed to be working on."
day4_org_score       = 4
day4_assessment      = "I now have structure. I still have challenges, but I can see them clearly."

comparison = {
    "Metric":         ["Organisation score (1–5)", "Biggest challenge"],
    "Day 1 (start)":  [f"{day1_org_score}/5", day1_frustration],
    "Day 4 (today)":  [f"{day4_org_score}/5", day4_assessment],
}
display(pd.DataFrame(comparison))
print("\\nCongratulations on completing the course.")
print("Your system is live. Go build something meaningful with it.")
"""))

    cells.append(md("""\
---
## 🏁 Day 4 Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| AI productivity assistant prompt written | ☐ |
| Daily plan generated and logged | ☐ |
| End-of-day reflection completed | ☐ |
| Weekly review completed | ☐ |
| System retrospective run | ☐ |
| Capstone summary exported | ☐ |

---
## 📎 All Repo References Used Across 4 Days

| File | Used in |
|------|---------|
| `prompt_library/goal_design_prompts.md` | Day 1 |
| `prompt_library/task_breakdown_prompts.md` | Days 1, 2 |
| `prompt_library/prioritization_prompts.md` | Day 2 |
| `prompt_library/daily_planning_prompts.md` | Day 4 |
| `prompt_library/review_prompts.md` | Day 4 |
| `prompt_library/system_optimization_prompts.md` | Days 3, 4 |
| `templates/notion_blueprint.md` | Day 1 |
| `templates/kanban_structure.md` | Day 3 |
| `templates/dashboard_blueprint.md` | Day 3 |
| `templates/streak_tracker_structure.md` | Day 3 |
| `templates/task_template.csv` | Days 1, 2 |
| `templates/work_session_log_template.csv` | Day 2 |
| `templates/attention_budget_template.csv` | Day 2 |
| `student_materials/reflection_templates/daily_checkin.md` | Days 1–4 |
| `student_materials/reflection_templates/weekly_review.md` | Day 4 |
| `student_materials/reflection_templates/retrospective.md` | Day 4 |
"""))

    return nb(cells, title="Day 4 — AI Review & Capstone")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN — generate all notebooks
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("Building AI Productivity OS notebook package...\n")

    day1 = build_day1()
    save(day1, "day_1_foundation.ipynb")

    day2 = build_day2()
    save(day2, "day_2_prioritization.ipynb")

    day3 = build_day3()
    save(day3, "day_3_dashboard_and_tracking.ipynb")

    day4 = build_day4()
    save(day4, "day_4_ai_review_and_capstone.ipynb")

    print(f"""
✅ All notebooks generated!

Output locations:
  notebooks/
    ├── day_1_foundation.ipynb
    ├── day_2_prioritization.ipynb
    ├── day_3_dashboard_and_tracking.ipynb
    └── day_4_ai_review_and_capstone.ipynb
  colab_versions/  (identical — Colab-compatible as-is)
    └── same 4 files

Open in Jupyter:  jupyter notebook notebooks/
Open in Colab:    Upload any file from colab_versions/ to colab.research.google.com
""")

