# Demo Flow

## Building a Personal Productivity System with AI

---

### Overview

This file provides the instructor with a structured script for every live demonstration across all 4 days. Each demo uses the fictional persona **"Alex Chen"** — a 31-year-old freelance UX designer working with 4 clients, running a side project (a UX newsletter), and trying to learn Figma advanced skills.

**Alex's system at a glance:**
- Goals: 3 active (grow freelance revenue, launch newsletter, learn advanced Figma)
- Projects: 5 active (Portfolio rebuild, Client A deliverable, Newsletter launch, Figma course, Admin cleanup)
- Tasks: ~25 tasks distributed across projects
- Current challenge: Too much client work, newsletter is stalling, learning is basically zero

Use Alex consistently across all demos. Learners will begin to feel familiar with Alex's situation and will apply patterns from Alex's system to their own without being told to.

---

## Day 1 Demos

---

### Demo 1.1 — Notion Template Tour (Session 1, 15 min)

**Goal:** Show learners what they're working with and demystify Notion's relational database structure.

**Steps:**
1. Open the duplicated Notion template
2. Navigate to the Goals database — show the table view with blank rows
3. "This is where we're headed: a Goals-Projects-Tasks stack, all linked"
4. Click into a blank Goal entry — show the properties panel (Goal Name, Outcome, Deadline, Success Criteria, Status)
5. Navigate to Projects database — show the "Linked to Goal" relation property
6. Navigate to Tasks database — show the "Linked to Project" relation property
7. "Notice how these three databases talk to each other. This is the foundation."

**Key demo move:** Click on a relation field and show how it pulls from the other database. This is the "aha moment" for most learners who've only used Notion as a notes app.

---

### Demo 1.2 — Goal Design Prompt (Session 2, 15 min)

**Goal:** Show learners the prompting process from raw intention → structured goal → Notion entry.

**Alex's raw goal for this demo:** "I want to make more money from freelancing"

**Steps:**
1. Open ChatGPT in a side tab
2. Open the Goal Design prompt template from the prompt library
3. Read it aloud: "I'm going to fill in the placeholder with Alex's raw goal statement"
4. Submit the prompt
5. Read the output — highlight the success criteria section
6. "Here's where I disagree with the AI: it suggested a 20% revenue increase. Alex has a specific target — I'm changing this to £4,000 MRR"
7. Edit the output (type a follow-up message: "The revenue target should be £4,000 MRR not a 20% increase. Revise.")
8. Copy the revised goal → paste into Notion Goals Database
9. Fill in the remaining properties: Deadline = December 31, Status = Active, Domain = Career

**Critical facilitator move:** Make the disagreement and edit visible. Say out loud: "I'm not just accepting this — I'm making it mine."

---

### Demo 1.3 — Project Creation (Session 3, 15 min)

**Goal:** Show how a goal translates into multiple projects.

**Alex's goal for this demo:** "Launch a UX newsletter with 500 subscribers by June"

**Steps:**
1. Open ChatGPT with the Business/Project Breakdown prompt
2. Input Alex's goal
3. Review output: 6 candidate projects emerge (branding, platform setup, content pipeline, distribution strategy, partnership outreach, analytics setup)
4. "Alex can't realistically run all 6 now. We're going to pick 3 active ones."
5. Select: Platform Setup, Content Pipeline, Distribution
6. Enter each into the Projects database:
   - Project name
   - Link to Goal: "Launch newsletter..."
   - Status: Active
   - Priority: High (Content), Medium (Platform), Low (Distribution)
   - Deadline: each 2–4 weeks before goal deadline
   - Scope note: 1-sentence description of what's included and excluded

---

### Demo 1.4 — Task Breakdown Prompt (Session 4, 10 min)

**Goal:** Show how a project becomes a task list.

**Alex's project for this demo:** "Content Pipeline — UX Newsletter"

**Steps:**
1. Use the Task Breakdown Prompt with Alex's project
2. ChatGPT returns 11 tasks
3. "I'm going to cut 3 that are too small, and I'm missing one critical task — I'll add it."
4. Enter 8 final tasks into the database
5. Show the relation link: each task → linked to "Content Pipeline" project
6. Apply basic properties: status = Not Started, priority guesses, due dates approximate

---

## Day 2 Demos

---

### Demo 2.1 — Milestone Map (Session 1, 20 min)

**Alex's project for this demo:** "Portfolio Rebuild"

**Steps:**
1. Use the Milestone Generation Prompt with the project description
2. ChatGPT generates 5 milestones — note that one is actually a task, not a milestone
3. "This one — 'Create a Figma mockup for the homepage' — that's a task. Let me replace it with a real milestone: 'Design phase complete for all 5 pages'"
4. Edit and enter 4 milestones in the project's milestone section (toggle list)
5. Run the Reverse Planning Prompt: "Given my launch date of March 1st, work backwards and assign realistic target dates for each milestone"
6. Assign dates to each milestone
7. "Notice: Milestone 2 and Milestone 3 both fall in the same week. I have a conflict. I either delay one project or extend the timeline."

---

### Demo 2.2 — Prioritization Prompt (Session 2, 15 min)

**Alex's task list for this demo:** 12 tasks of varying urgency

**Steps:**
1. Copy all tasks from Notion as a plain text list
2. Use the Prioritization Prompt
3. Review output — the AI suggests 4 P1 tasks
4. "Four P1 tasks? That can't be right. Let me look at these..."
5. Challenge two: "This is P2, not P1 — it's important but I have 3 weeks, not 3 days"
6. Update: 1 P1, 3 P2, 5 P3, 3 P4
7. Update the Notion Task database
8. Create filtered view: "This Week's Priorities" — Priority P1 or P2, Due Date ≤ 7 days, sort by due date

---

### Demo 2.3 — Work Session Log (Session 4, 15 min)

**Steps:**
1. Create Work Session Log database: Date, Project/Domain, Duration, Output
2. Enter 4 fictional sessions from Alex's recent 2 days:
   - "Client A deliverable, 2h → wrote project brief v1"
   - "Email / Admin, 1.5h → responded to 8 emails, updated invoice"
   - "Newsletter, 0.5h → brainstormed 3 article ideas"
   - "Client B call, 1h → discovery session notes"
3. "Now let's calculate the actual percentages:
   - Client work: 60% | Admin: 30% | Newsletter: 10% | Learning: 0%"
4. Run Attention Budget Analysis Prompt: input ideal (40/10/25/25) vs actual (60/30/10/0)
5. AI output: "Your administrative overhead is consuming 3x your target allocation. Learning has zero actual time."

---

## Day 3 Demos

---

### Demo 3.1 — Kanban Board (Session 1, 20 min)

**Steps:**
1. Open Alex's Task database → switch to Board view
2. Edit Status options: Backlog → This Week → In Progress → Blocked → Done
3. Move Alex's tasks into appropriate columns: 8 Backlog, 3 This Week, 1 In Progress, 1 Blocked, 2 Done
4. Add a WIP limit callout above the board: "⚠️ In Progress limit: 3"
5. Create filtered view: "Active Work" — exclude Backlog and Done

**Visual emphasis:** Show the "Blocked" column. "Notice there's one task here — it's blocked because Alex is waiting on a client response. This is information. Without a Kanban, that task just sits invisibly on a list."

---

### Demo 3.2 — Master Dashboard (Session 2, 20 min)

**Steps:**
1. Create new page: "🏠 Alex's Mission Control"
2. Add a title callout: "Dashboard as of [today's date] — Alex, UX Designer"
3. Add 2-column layout
4. Column 1, Section 1: Linked database "Today's Focus" — Task table, filter: Due = today OR Priority = Critical, hide all properties except Task Name and Status
5. Column 1, Section 2: Linked database "Active Projects" — Project gallery, filter: Status = Active, show: Name + Priority
6. Column 2, Section 1: Linked database "This Week" — Task table, filter: Due within 7 days, sort Priority H→L
7. Column 2, Section 2: Anti-To-Do Today — filter by date = today
8. "Now open the dashboard. One page. Everything visible. This is the front page of Alex's day."

---

### Demo 3.3 — Streak Tracker (Session 3, 20 min)

**Steps:**
1. Create Streak Tracker database: Date (Date), Habit (Select), Completed (Checkbox), Notes (Text)
2. Add habits: Morning Planning, End-of-Day Reflection, Session Logged
3. Add entries for past 5 days (fictional but realistic — 2 missed reflection days)
4. Create view: last 14 days, sorted by Date descending
5. Link view to the Master Dashboard as "Daily Habits"

---

## Day 4 Demos

---

### Demo 4.1 — Daily Planning Session (Session 1, 20 min)

**Alex's scenario:** Monday morning, 9am, available for 6 hours, medium energy, 3 priorities from dashboard.

**Steps:**
1. Read Alex's priorities from the Notion dashboard: P1 = Client A feedback doc, P2 = Newsletter draft, P2 = Portfolio page 3
2. Open the Daily Planning Prompt: fill in context (6h available, medium energy, priorities)
3. Submit
4. Review output: AI suggests a time-blocked sequence (Client A: 9–11am, Newsletter: 11:30–1pm, Portfolio: 2–4pm, Buffer/Admin: 4–5pm)
5. Edit: "I have a team call at 10am that wasn't in my context. Let me adjust."
6. Copy finalised plan into a Notion Daily Note
7. "This took 12 minutes. Alex's day is structured before he opens a single email."

---

### Demo 4.2 — Weekly Review (Session 3, 20 min)

**Alex's fictional week data:** 6 completed tasks (from anti-to-do), 4 incomplete tasks, attention allocation (admin 35%, client 40%, newsletter 15%, learning 10%)

**Steps:**
1. Open weekly review template
2. Complete the 6-step sequence:
   - Step 1: Inboxes cleared (fictional: yes)
   - Step 2: Anti-to-do review: 6 items shipped this week
   - Step 3: Open tasks: 4 incomplete, 2 were genuinely blocked (external), 2 were avoided
   - Step 4: Projects: Portfolio moved, Newsletter stalled (no publishing this week)
   - Step 5: Attention: admin 35% vs ideal 10% — too high again
   - Step 6: Next week: 3 outcomes defined
3. Run the Weekly Review Prompt — AI generates a summary and recommends: "Protect Tuesday afternoon for newsletter work"
4. Enter next week outcomes in Notion: "Publish newsletter issue 1 | Complete portfolio page 4 | Block 3 hours for admin only"

---

### Demo 4.3 — System Retrospective (Session 3, Within Step 3)

**Steps:**
1. Answer the 4 retrospective questions for Alex:
   - Used: Task database, Kanban, Anti-To-Do, Work Session Log
   - Abandoned: Streak Tracker (missed 3 days), Milestone map (didn't update)
   - Weakest link: Anti-To-Do — only used on days when things got done, not when things got blocked
   - One change: Set a daily 5:30pm reminder to update Anti-To-Do and tick off streaks
2. Run the System Retrospective Prompt
3. AI identifies: "Milestone map is not being updated — this is a leading indicator of project drift"
4. Proposed system change: Add milestone review to weekly review step 4
