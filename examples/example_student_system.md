# Example: University Student Productivity System

## Building a Personal Productivity System with AI — Example Systems

---

**Persona:** Sam, 20 — second-year Computer Science student, two part-time jobs (barista 12h/week, on-campus tutor 6h/week), involved in two student societies, applying for summer internships

**Goal:** Pass all modules with a 2:1 average, land a summer software engineering internship, and stop underperforming on coursework deadlines.

**Core problem:** Sam's life runs across 4 calendars, 2 Whatsapp groups, a University portal, and 3 different group chats. Nothing is in one place.

---

### What Sam Built

---

#### Goals Database

| Goal | Success Criteria |
|------|-----------------|
| Pass all Year 2 modules at 2:1 or above | Weighted average ≥ 60% across all 6 modules at end of semester |
| Land a summer software engineering internship | Received and accepted offer from a company in the target list by April 1 |
| Reduce coursework deadline misses | Zero late submissions in Semester 2. At most 1 request for extension in each module. |

*AI assisted with success criteria on goal 3: Sam's original goal was "be more organised" — the prompt reframed it as a specific, observable commitment.*

---

#### Projects Database

| Project | Linked Goal | Priority | Notes |
|---------|------------|---------|-------|
| Algorithms Module (COMP2073) | Pass modules at 2:1 | High | Midterm week 7. Coursework 1 due Week 9. Hardest module. |
| Internship Applications | Land SE internship | High | Target: 8 applications by March 1. CVs done. Prep needed. |
| Group Project (COMP2089) | Pass modules at 2:1 | Medium | 3-person group. Group meetings Monday evenings. |
| Databases Module | Pass modules at 2:1 | Medium | Assignment 1 due Week 8. Relatively comfortable material. |

---

#### Milestone Map: Algorithms Module

| Milestone | Target Date | Status |
|-----------|------------|--------|
| All lecture slides reviewed up to Week 5 | Week 5 Friday | ✅ Done |
| Revision notes for Sorting algorithms complete | Week 6 Friday | ✅ Done |
| Past exam questions (2019–2022) attempted | Week 7 Wednesday | 🟡 In Progress |
| Midterm completed | Week 7 Friday | ⬜ Not Started |
| Coursework 1 first draft written | Week 8 Friday | ⬜ Not Started |

**Reverse planning insight:**  
*"The midterm is Week 7 Friday. By Week 7 Wednesday I need to have done past papers — that means I need the revision notes done by Week 6. Working backwards, I can't wait until Week 7 to start revision."*

---

#### Internship Application Breakdown

**Sam's raw goal:** "Get a software internship"

**Task breakdown (from Task Breakdown Prompt):**

| Task | Priority | Status | Notes |
|------|---------|--------|-------|
| Research 20 companies hiring SE interns | P2 | Done | 20 on the list. 8 shortlisted. |
| Update CV (software-specific) | P1 | Done | Updated with GitHub projects |
| Write 3 cover letter templates | P2 | In Progress | Generic + Finance sector + Startup |
| Set up LinkedIn "Open to Work" | P3 | Done | Visible to recruiters only |
| Apply to 4 companies (Batch 1) | P1 | This Week | Deadline: own-set Feb 15 |
| Prepare for technical interviews | P2 | Backlog | LeetCode — 3 problems per week |
| Apply to 4 companies (Batch 2) | P2 | Backlog | Feb 28 target |

---

#### Sam's Attention Budget Challenge

| Domain | Ideal | Actual |
|--------|-------|--------|
| Academic work | 50% | 35% |
| Job applications | 25% | 10% |
| Part-time jobs | 15% | 30% |
| Societies / Social | 5% | 20% |
| Admin / Other | 5% | 5% |

**AI Insight:**  
*"You are spending twice as much time on part-time jobs and societies as you intended. Part-time work commitments may be non-negotiable, but social/society time at 20% vs 5% ideal represents 5+ hours per week that could be redirected to your highest-priority goals."*

**Sam's change:**  
> "I'm not reducing the jobs — I need the money. But I'm cutting society involvement from 2 active committees to 1. That's 3 hours per week back."

---

#### Kanban for Students

Sam adapted the Kanban stages for academic work:

| Stage | What it means |
|-------|--------------|
| Module Backlog | Topics/tasks not yet scheduled |
| This Week | Assigned to specific revision or coursework sessions |
| Active | Currently in a work session |
| Pending Review | Draft submitted / waiting on feedback |
| Done | Completed and filed |

---

#### Daily Planning for Exam Week

**Sam's morning planning prompt context:**
- Available hours today: 6 (9am–1pm and 3pm–5pm — barista shift at 5:30pm)
- Energy: 4/5 (slept well)
- Top priorities: Past paper timed attempt, Algorithms; Draft intro for Databases assignment; Apply to 2 internships
- Constraint: Can't do complex work during shift. 5pm hard stop.
- Thing I've been avoiding: The timed past paper (anxiety about results)

**AI-generated plan (excerpt):**  
> 9:00–11:00am — Algorithms past paper (2021) timed exam conditions. No notes.  
> 11:15–12:15pm — Review past paper answers; note gaps for further study.  
> 12:30–1:00pm — Databases intro draft — just write, don't edit  
> 3:00–4:30pm — Internship applications Batch 1 (2 companies — cover letters adapted from Template A)  
> 4:30–5:00pm — Email admin + pack bag for shift

**Sam's edit:** "The Databases intro is too short — I need at least 45 min not 30. Moving internship applications to Thursday."

---

#### Retrospective Takeaway

*"The system I built won't fix my time — I genuinely don't have more hours in the day. But what it fixed is my awareness. Before this course, I didn't know my actual allocation was 30% on part-time work. I thought it was 15%. That gap explains a lot."*

---

### Prompts Sam Used

1. **Goal Definition Prompt** → "Be more organised" became "Zero late submissions in Semester 2"
2. **Task Breakdown Prompt** → Internship applications broken into 8 specific tasks
3. **Reverse Planning Prompt** → Algorithms revision sequenced from midterm backwards
4. **Attention Budget Prompt** → Discovered society time was double target
5. **Prioritization Prompt** → Correctly identified LeetCode prep as P3, not P1 (midterm > interview prep right now)
6. **Daily Planning Prompt (Minimal Day version)** → Used on barista shift days to plan just 2 focused hours
