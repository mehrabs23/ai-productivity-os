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

> **Day 3 theme:** Operationalizing the Life OS — show students how the system becomes usable every day, not just structured.

---

### Demo 3.0 — Day 3 Frame-Setting (Opening, 5 min)

**What to say:**

> "Days 1 and 2 built the engine — your goals, projects, tasks, and prioritization. Today we build the dashboard and the daily driving habit. By the end of today, you'll have one page you open every morning instead of juggling three apps and a sticky note."

**Key reframe:** This is a **Life OS** — not a work PM tool. Alex's dashboard will show tasks from client work, newsletter, personal life, and admin. Show learners that multi-area visibility is the point.

**What to click first:**
- Open Alex's current Notion workspace, showing fragmented databases with no dashboard
- "Here's what Alex has right now — great foundations, but try to figure out what matters most today. Ready? Go."
- Pause for 10 seconds. Let learners observe the friction.
- "Today we fix that."

---

### Demo 3.1 — Life OS Workflow and Kanban Build (Session 2, 20 min)

**What the instructor should show first:**
- Open Alex's Task Database in Table view
- Show the old Status options (the messy ones from Days 1–2) — "We're going to standardize this"

**Step-by-step click sequence:**
1. Click the "Status" column header → "Edit property"
2. Remove all existing options by clicking "×" on each
3. Add the 6 standard Life OS statuses: **Inbox → Planned → This Week → In Progress → Waiting / Blocked → Done**
4. Assign distinct colors: Inbox (grey), Planned (blue), This Week (yellow), In Progress (purple), Waiting (orange), Done (green)
5. Click "Done", then "+ Add view" → select "Board"
6. Confirm grouping is "Status"
7. Drag several of Alex's tasks into correct columns:
   - Inbox: "Research dentist options", "Find recipe ideas for dinner"
   - This Week: "Deliver Client A brief", "Newsletter draft"
   - In Progress: "Portfolio page 3" (only 1 — maintain WIP)
   - Waiting: "Client B payment — awaiting invoice approval"
8. Press `/` above the board → "Callout" → type: "🎯 In Progress limit: 3. If adding a 4th, something must move to Done or Planned first."
9. "+ Add view" → name it "Active Work" → filter: Status ≠ Inbox AND Status ≠ Done

**What to say when introducing Life OS workflow:**
> "One workflow for everything. Your dentist appointment research sits next to your client brief. Your newsletter draft sits next to your personal goal to learn a language. This is what makes it a Life OS — everything flows through the same system."

**Where students commonly get stuck:**
- Editing the Status property (vs. trying to change it in the view) — show the distinction clearly
- Accidentally deleting Status options they still need
- Not creating the filtered "Active" view (leaving Inbox clutter visible)

**How to keep pace:**
- Demo takes 20 minutes max. Move directly to student task time after.
- If students have Notion loading issues, let them work from the blueprint: [`templates/day_3_life_os_dashboard_build_guide.md`](../templates/day_3_life_os_dashboard_build_guide.md)

---

### Demo 3.2 — Life OS Dashboard Build (Session 3, 20 min)

**What the instructor should show first:**
- Open a blank Notion page
- "I'm going to build this in front of you in real time, in the order you'll build it."

**Step-by-step click sequence:**
1. Create page → name: "🏠 Alex's Life OS"
2. Click **•••** top-right → enable **"Full width"**
3. Click the emoji space → choose 🏠
4. Click "Add cover" → select from Notion's free image library → pick something calm and professional
   - *(Note to instructor: recommend learners add their own original screenshot of their workspace here after class)*
5. Press `/` → "Callout" → write: `Life OS | Week of [date] | Work · Newsletter · Personal · Admin`
6. Add a Heading 2: "🎯 Today"
7. Press `/` → "Linked view of database" → select Task Database
8. Rename view: "Today" → Filter: Due Date = Today **OR** Status = In Progress → Properties: show Name, Status, Area only
9. Hover right edge of the "Today" block → drag another block alongside it → creates 2-column layout
10. In Column 2: Add linked database "⚠️ Overdue" → Filter: Due before Today AND Status ≠ Done → sort Due Date ascending
11. Below "Today" in Column 1: Add "📅 This Week" → Due ≤ today + 7 days, Status ≠ Done, sort Priority
12. Below "Overdue" in Column 2: Add "🔔 Due Soon" → Due within next 3 days AND Status ≠ Done
13. Below the 2-column section: Add "🗂️ Active Work" Kanban — Board view, Status ≠ Inbox, Status ≠ Done
14. Below that: "✅ Completed Recently" → Status = Done, last edited within 7 days

**How to transition from dashboard aesthetics to actual usefulness:**
> "I know some of you want to spend 30 minutes choosing the perfect cover photo. I've been there. But here's my rule: your dashboard earns its right to look good after it earns its right to be useful. Let's get the data right first. You can make it pretty tonight."

**Where students commonly get stuck:**
- Linked database showing "No results" — check that filters are correct and that tasks have Due Dates
- Column layout collapsing — usually from clicking elsewhere during drag; retry slowly
- Setting wrong view type on the kanban section (must be Board, not Table)

---

### Demo 3.3 — Reminder Views and Due-Date Setup (Session 4, 10 min)

**What the instructor should show first:**
- Open any task in Alex's Task Database that has no Due Date
- "This task is invisible to every filter. Let's fix that."

**Step-by-step click sequence:**
1. Open the task → click "Due Date" field → set a date 2 days from now
2. Click the date again → scroll to see the reminder dropdown → enable "1 day before"
3. Close the task → show it appearing in "Due Soon" on the dashboard
4. Open Task Database → click "+ Add a property" → choose Date → name it "Reminder Date"
5. Show 2 existing tasks with Due Dates → add a Reminder Date (e.g., 2 days before Due Date)
6. Show the "Overdue" view → confirm it's catching Alex's past-due tasks

**What to say about reminders:**
> "Your Due Soon and Overdue views ARE your reminder system. The goal is to make the system do the worrying so your brain doesn't have to. But reminders only work when tasks have dates — so make sure your important tasks all have a Due Date."

---

### Demo 3.4 — Daily Check-In Routine (Session 5, 10 min)

**What the instructor should show first:**
- Scroll to the top of Alex's Life OS dashboard
- "This is where the daily ritual lives — and it has to be at the top, not the bottom."

**Step-by-step click sequence:**
1. Press `/` → "Toggle List" → name: `📝 Daily Check-In — [Today's date]`
2. Open the toggle → add 5 lines:
   ```
   1. Top 3 priorities today:
   2. Anything overdue to address first?
   3. What did I avoid yesterday?
   4. Energy level today: /5
   5. What would make today feel complete?
   ```
3. Fill in each question live for Alex's fictional context
4. Collapse the toggle → "The page stays clean. The data is there."
5. Say to learners: "You'll fill this in during class today for your own system. That's your first real check-in."

**What to say about daily check-ins:**
> "The check-in is not a task. It's a ritual. It's the moment you go from reactive to intentional. The difference between opening Instagram and opening your Life OS is this 5 minutes of deliberate attention."

---

### Demo 3.5 — Weekly Status View (Session 6, 10 min)

**What the instructor should show first:**
- Scroll to the bottom of Alex's dashboard
- "This section answers a different question from 'what do I do today.' It answers: 'how is my week actually going?'"

**Step-by-step click sequence:**
1. Add a Heading 2: "📊 Week in Review"
2. Add linked database: Task DB → rename "✅ Completed This Week" → Filter: Status = Done, date filter: this week → view: List
3. Below it, add a text block:
   ```
   Week of: [date]
   Wins this week:
   -
   Still in progress / carried over:
   -
   What I'm re-prioritising:
   -
   Focus for next week:
   -
   ```
4. Fill in "Wins" for Alex's week using fictional data: "Delivered Client A brief, published newsletter"
5. "This section feeds directly into the weekly review we'll do on Day 4. You're building the source now."

**How to keep pace:**
- Each demo is standalone — if time is tight, combine 3.3 and 3.4 into one 15-minute block
- Leave 20 minutes at minimum for the "Simulate a Real Day" exercise — it's the payoff session

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
