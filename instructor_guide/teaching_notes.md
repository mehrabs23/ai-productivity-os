# Teaching Notes

## Building a Personal Productivity System with AI

---

### Core Pedagogical Philosophy

This course operates on three principles that should guide every instructional decision:

**1. Learners build with real data.**  
No fictional practice scenarios. Learners use their own goals, their own projects, their own hours. This means some learners will be uncomfortable — share too much, overthink their goals, or feel exposed when their attention budget reveals they've been avoiding something important. This discomfort is productive. Don't rush past it.

**2. AI is a thinking partner, not a shortcut.**  
In every prompt demonstration, show the review-and-edit step. Make it visible that the AI output is a first draft. If an AI output is wrong or generic, celebrate the imperfection as a teaching moment: "This is why we always edit. The AI doesn't know you yet. You do."

**3. Deliverables over activities.**  
Every session ends with something real that the learner has built. If you're running short on time, cut the discussion, not the build task. A learner who leaves with a complete system and incomplete discussion has learned more than one who discussed extensively but didn't build.

---

### Common Learner Challenges (and How to Handle Them)

#### "I don't know what my goals are"

This is the most common Day 1 blocker. Do not try to fix it with more explanation. Instead:
- Ask: "What do you spend time on that feels important but has no deadline?"
- Ask: "What outcome, if achieved 6 months from now, would make this year feel successful?"
- Suggest they start with one professional goal and one personal goal
- If still blocked: "Write down what you want to be different about your working life in 90 days. That's your goal."

#### "I have too many goals / projects / tasks"

This is a classic overload pattern. Reframe:
- "Having too many is fine — we just need to identify the active ones. Backlog the rest."
- Use the Prioritization and Overload Triage prompts early rather than waiting for Day 2

#### "My system feels fake because most of my work is reactive (meetings, requests, etc.)"

This is real, especially for team leads and freelancers. Acknowledge it directly:
- "Reactive work is real work. It goes in the Work Session Log. It counts."
- "The goal isn't to eliminate reactive work — it's to have clarity about what matters SO THAT reactive work doesn't crowd out your most important projects."
- Consider adding a "Reactive / Admin" category to the attention budget

#### "ChatGPT gave me a bad output"

This is a teaching moment, not a failure. Show the learner:
- The prompt might need more context — show them how to add specificity
- The output might be partially right — show them how to edit rather than reject
- Different AI models produce different results — GPT-4 often produces more nuanced outputs than GPT-3.5

#### "My Notion is a mess after Day 2"

Expected. By Day 2, some learners have three versions of the same database, orphaned tasks, and linked views that link to nothing.
- Suggest a 10-minute "clean-up session" at the start of Day 3
- The Dashboard session naturally consolidates the mess — let the UX audit do the heavy lifting

---

### Setting the Tone on Day 1

The first 15 minutes of Day 1 set the social contract for the course. Establish these norms explicitly:

1. **We build with real data.** "I'd like everyone to use their actual goals and projects today. If something feels too personal to share, you don't have to share it — but do put it in your system."

2. **We don't compare systems.** "Some of you will build beautiful Notion dashboards. Some will build functional but ugly ones. Both are valid. We are not competing."

3. **AI outputs are always reviewed and edited.** Make this visible every single time you demo — never copy-paste directly from ChatGPT without visibly editing at least one thing.

4. **The capstone is a conversation, not a performance.** "Day 4 ends with a 10-minute walkthrough. You will literally just show someone your Notion workspace and explain why you designed it that way."

---

### Day-Specific Notes

#### Day 1
- Allow 10–15 extra minutes if learners are setting up Notion for the first time
- Many learners will define goals too vaguely on first attempt — the Goal Design Prompt usually sharpens them on the second pass, no instruction needed
- The hardest thing about Day 1 is deciding which goals to include. Encourage: "Pick the 3 you're actually working on this quarter, not the 10 you care about in principle."

#### Day 2
- Reverse planning is often the most cognitively demanding session. Give learners extra time here.
- The attention budget comparison (ideal vs. actual) is the emotional core of the day. Let silence happen when learners see the gap. Don't rush to the next thing.
- Many learners will have zero work session log entries — help them estimate retroactively from calendar data or memory

#### Day 3

**Core Day 3 principle: Day 3 is about usability, not just structure.**

By the end of Day 3, learners must be able to use their system — not just admire it. The test: can a learner open Notion and know what to do next in under 10 seconds? If not, the dashboard is not working.

**The dashboard must support action, not just visibility.**

A dashboard with 12 sections and zero actionable decisions is a decoration, not a tool. Remind learners frequently:
- "Would you actually open this tomorrow morning?"
- "Can you take one action from this view right now?"

If the answer is no, simplify.

**Reminders reduce mental load.**

Many learners carry their task list in their heads because no system has reliably resurfaced things at the right moment. When teaching the Due Soon and Overdue views, frame reminders as cognitive offloading:
> "Every task you're worrying about remembering is borrowing CPU from your thinking. The system exists to carry those tasks — not your brain."

Explain that Notion's date-based reminder notifications only work when tasks have dates. This is why Task 1 (the audit) includes adding due dates.

**Kanban is a visual Life OS — not just corporate project management.**

Many learners will associate Kanban with Jira, Trello, or corporate sprints. Reframe deliberately:
> "This board has your dentist appointment, your essay draft, your side hustle idea, and your work deadline — all in one view. That's a Life OS board."

Point to the "Waiting / Blocked" column: "This column is where honest systems put things that can't move. Without it, blocked tasks hide inside 'In Progress' and never get done."

**Daily check-ins create daily intention.**

The check-in is the highest-leverage habit in the system. Without it, learners return to reactivity — opening email first, planning from inbox instead of priorities.

When introducing the check-in, make it feel like a ritual, not an admin task:
> "The check-in is 5 minutes. It replaces 30 minutes of confusion about what you're supposed to work on."

Have learners fill in their first check-in during class — not as a demo, but as real use.

**Weekly status views support clarity and accountability.**

Frame the weekly status as:
- A self-honesty check (what actually got done vs. what I planned)
- A communication tool (sharable with an accountability partner)
- A Day 4 input (the weekly review on Day 4 uses this section as its starting point)

**Common Day 3 misconceptions:**

| Misconception | Correction |
|--------------|-----------|
| "I need to make the dashboard look good first" | Function before aesthetics — build views, then polish |
| "Kanban is for work tasks only" | Personal, study, and admin tasks belong there too |
| "I don't need Due Dates if I know what's important" | Dates power all reminder views — without them, filters don't work |
| "The daily check-in is too simple to matter" | Simplicity is a feature — a 5-minute ritual beats a 30-minute one you skip |
| "More sections = more complete" | 6–8 sections is the sweet spot. More = scroll fatigue. |

**Common student confusion points:**

1. **Linked database vs. adding a new database:** Show the difference explicitly — "Linked View of Database pulls from your existing database. We're not creating new data here."
2. **Filter logic:** Keep to simple cases for beginners — don't combine AND/OR until basics are working.
3. **2-column layout collapsing:** "Normal in Notion — just drag the block back beside it. It takes practice."
4. **WIP limit:** "The limit makes you tell the truth. When everything is 'In Progress,' nothing actually is."

**How to redirect students stuck in aesthetic perfectionism:**

When a student is adjusting cover photos while their Due Soon view is empty:
1. Walk over and ask: "Does your Overdue view have any tasks in it?"
2. Redirect with warmth: "The aesthetics will matter when you open this tomorrow. The data needs to work first."

Suggested phrase to say to the whole room:
> "I'm noticing some of you are in dashboard-decoration mode — that's a great sign it feels like yours. But let's run the 5-second test together first. If it passes, decorate away."

#### Day 4
- The capstone is the most important session of the course. Give it adequate time.
- For learners who feel their system is "not good enough" to present: "An honest, incomplete system told with clarity is worth more than a perfect system you can't explain."
- The retrospective portion of the capstone is often the most revealing — reward honesty with enthusiasm

---

### Assessment Guidance

See [`/course_overview/assessment_and_capstone.md`](../course_overview/assessment_and_capstone.md) for full rubric guidance.

**Key grading principles:**
- Reward specificity over completeness (a well-defined goal is worth more than five vague ones)
- Reward honest retrospective over polished system design
- Don't penalise learners whose systems are functional but not beautifully designed
- Penalise learners who cannot explain *why* they designed their system the way they did
