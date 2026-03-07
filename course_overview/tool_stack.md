# Tool Stack

## Building a Personal Productivity System with AI

---

### Overview

This course uses a deliberately minimal, free, and widely accessible tool stack. Every tool in this list has a free tier that is sufficient for the entire course. No subscriptions, no premium accounts, and no technical setup are required.

---

### Core Tools

---

#### Notion

**Role in the course:** Primary workspace — databases, views, dashboard, kanban, streak tracker

**Why Notion:**
- Free tier includes unlimited personal pages and databases
- Flexible enough to build a goal-project-task hierarchy natively
- Dashboard and linked database views are genuinely useful (not toy examples)
- Learners are likely to continue using it after the course

**Features used:**
- Database pages (Goals, Projects, Tasks, Work Sessions)
- Linked database views and filters
- Kanban view
- Gallery, Table, List, Board, and Calendar views
- Relations and Rollups between databases
- Simple formulas for progress tracking
- Toggle lists and callout blocks for structured templates

**Free tier limitations (won't affect this course):**
- API integrations are not used
- Guest access and team features are not used
- Block storage limits only apply to very old free accounts

**Setup:** Create a free account at [notion.so](https://notion.so). No credit card required. Use the course Notion template (link distributed at course start).

---

#### ChatGPT

**Role in the course:** AI thinking partner — goal articulation, task breakdown, prioritization, planning, and reflection

**Why ChatGPT:**
- Free tier (GPT-3.5) is fully sufficient for all prompts in this course
- Widely recognized — most learners have already encountered it
- No API key or technical integration required — used entirely via chat UI
- The prompt library is designed to produce high-quality outputs with GPT-3.5

**How it is used:**
- Goal definition and success criteria generation
- Project-to-task decomposition
- Priority triage (overloaded task list analysis)
- Daily planning prompt
- End-of-day reflection companion
- System improvement suggestions
- Capstone retrospective prompt

**What it is NOT used for:**
- Coding or technical work
- Automated workflows or integrations
- Replacing learner judgment — all AI output is evaluated and edited by the learner

**Note on GPT-4:** Learners with a ChatGPT Plus subscription can use GPT-4 for all prompts. The course is designed and tested on GPT-3.5 to ensure accessibility.

**Setup:** Create a free account at [chat.openai.com](https://chat.openai.com). No credit card required.

---

#### Google Sheets (Optional, Day 2)

**Role in the course:** Supplementary attention budget and session log for learners who prefer spreadsheets

**Why included:**
- Some learners find tabular data more comfortable than Notion databases
- Provides an alternative for the Attention Budget and Work Session Log
- Templates are provided as CSV files in [`templates/`](../templates/)

**Features used:**
- Simple data tables
- Manual calculation rows
- Conditional formatting (optional)

**When used:**
- Day 2: Attention Budget and Work Session Log as alternatives to Notion
- The Notion version is the primary and recommended approach

**Setup:** Free with any Google account at [sheets.google.com](https://sheets.google.com).

---

### Future Extension Tools (Not Used in This Course)

The following tools will be used in the future Jupyter Notebook / Google Colab extension of this course. They are **not required** for the current 4-day version.

| Tool | Purpose | Status |
|------|---------|--------|
| **Google Colab** | Hosted Python notebooks for data analysis exercises | Future — see `colab_versions/README.md` |
| **Jupyter Notebook** | Local Python notebook alternative | Future — see `notebooks/README.md` |
| **Pandas** | Data processing for session log analysis | Future |
| **Matplotlib / Seaborn** | Visualisation for attention and session dashboards | Future |

---

### Tool Stack Philosophy

This course was designed with **minimum viable tooling** in mind. The deliberate constraints are:

1. **All free** — eliminates cost as a barrier to entry
2. **No code** — eliminates technical skill as a barrier to entry
3. **No integrations** — eliminates complexity and failure points
4. **Browser-based** — works on any operating system

The course acknowledges that many learners will eventually want to extend their system — connecting Notion to Zapier, building automation workflows, or using AI APIs directly. These are valid next steps, but they are **out of scope** for this course.

---

### Compatibility Notes

| Platform | Compatibility |
|----------|--------------|
| Windows | Fully supported |
| macOS | Fully supported |
| Linux | Fully supported |
| iOS / Android | Limited — Notion mobile app works, but dashboard building is easier on desktop |
| Chromebook | Fully supported (browser-based tools only) |

> **Recommendation:** Learners should use a desktop or laptop computer with a modern browser (Chrome, Firefox, Safari, or Edge) for the best experience.
