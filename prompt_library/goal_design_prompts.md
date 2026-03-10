# Goal Design & Strategic Planning Prompts

## Building a Personal Productivity System with AI — Prompt Library

---

### When to Use This Category

Use these prompts at the beginning of your system build, when setting up or refining your Goals Database, or any time a goal feels vague, unmotivating, or unclear.

Goal design prompts help you move from **"I want to do more things"** → **"I have 3 well-defined goals with success criteria, feasibility checks, and a real roadmap."**

### How to Use Any Prompt in This File

1. Replace everything in `[SQUARE BRACKETS]` with your own real information
2. Submit to ChatGPT and read the full output
3. **Edit the output** — the AI gives you a first draft, not a final answer
4. Copy the refined version into your Notion Goals Database

> **Golden rule:** The more specific your input, the more useful the output.

---

## Section 1: Goal Clarification and Definition

---

### Prompt 1.1 — Goal Definition Prompt

**Purpose:** Transform a vague goal statement into a structured, measurable goal with a specific outcome and success criteria.

**When to use:** Day 1, Session 2 — when building your goals for the first time, or any time a goal feels fuzzy or hard to commit to.

---

```
You are acting as a strategic goal coach. Your job is to help me turn a rough goal statement into a well-defined, measurable goal I can actually track.

My raw goal statement:
[PASTE YOUR GOAL — it can be vague or half-formed, that's fine]

My context:
- My role / situation: [e.g., "freelance UX designer", "final-year student", "working full-time while building a side project"]
- Time I have available per week for this goal: [X hours/week]
- Rough deadline or timeframe: [e.g., "by end of Q2", "within 6 months", "no fixed date"]
- Any constraints I should factor in: [e.g., "limited budget", "no team", "family commitments on weekends"]

Please:
1. Rewrite my goal as a specific outcome statement — describe what is true in the world when this goal is achieved. Focus on outcomes, not activities.
2. Suggest 3–5 measurable success criteria — observable, specific statements that would confirm the goal is achieved. At least one must be quantitative (a number, date, or verifiable event).
3. Identify 2 potential obstacles that might prevent this goal from being achieved, based on how I've described it.
4. Ask me 2–3 clarifying questions that would help sharpen the goal further.

Format: clear headings for each section. No generic motivational filler.
```

**Customisation notes:** The more detail you put in "My context", the more tailored the output. Paste several raw goals at once if you want to compare which one the AI thinks is the most clearly defined.

---

### Prompt 1.2 — SMART Goal Conversion Prompt

**Purpose:** Convert an existing goal into strict SMART format — Specific, Measurable, Achievable, Relevant, Time-bound.

**When to use:** When you have a goal you believe in but it still feels hard to act on. Good for workshop exercises where you need a well-structured goal entry for Notion.

---

```
You are a performance coach specialising in goal-setting. I have a goal I believe is important but it's not well-structured. Please convert it into a strict SMART goal.

My goal as it currently stands:
[PASTE YOUR CURRENT GOAL STATEMENT]

For context:
- My situation: [BRIEF DESCRIPTION — role, major projects, time available]
- What prompted this goal: [WHY you want this — context helps SMART conversion be relevant]
- My deadline or target date: [DATE OR TIMEFRAME]

Please output:
1. Specific — One sentence: what exactly will be accomplished, and by whom?
2. Measurable — How will I know whether it's achieved? Name the metric(s).
3. Achievable — Is this realistic given my context? Flag any achievability risk.
4. Relevant — Why does this goal matter to my broader situation right now?
5. Time-bound — State the completion date or milestone schedule clearly.

Then:
6. Write the final SMART goal as one clean, complete statement I can paste into my Notion Goals Database.
7. Suggest 2-3 success criteria to track alongside it.
```

---

### Prompt 1.3 — Feasibility Check Prompt

**Purpose:** Surface-test a goal against your real constraints before committing to it. Prevents goals that look good on paper but will fail in practice.

**When to use:** After drafting a goal — before entering it into your Goals Database as "Active." Especially useful for ambitious goals or goals with external dependencies.

---

```
You are a critical thinking partner. I want you to stress-test a goal I'm considering committing to. Do not be encouraging — be analytically honest.

Goal: [GOAL NAME AND OUTCOME STATEMENT]
Deadline: [DATE]
My available time per week: [X hours/week]
Other active commitments I'm juggling: [LIST 2–4 ONGOING COMMITMENTS]

Please evaluate this goal against the following:

1. Time feasibility: Given my available hours per week, is there realistically enough time to reach this goal by the deadline? Show your rough estimate.
2. Dependency risk: Does this goal depend on other people's decisions, tools, or external outcomes I don't control? List them.
3. Conflict check: Based on my other commitments, is there a risk that this goal will compete heavily for the same time slot as something else?
4. Scope creep risk: Is the goal defined tightly enough to be completable, or is it likely to expand as I get into it?

Output:
- An honest feasibility verdict: Feasible / Feasible with adjustments / High risk
- The single most important change that would lower the biggest risk
- A suggested alternative formulation of the goal if it currently has a serious feasibility problem
```

---

### Prompt 1.4 — Goal Portfolio Review Prompt

**Purpose:** Review a set of goals as a portfolio — identify conflicts, gaps, and which to prioritise if you had to choose.

**When to use:** When you have 3+ goals and want to sense-check whether they're coherent, or during a retrospective when you're re-evaluating direction.

---

```
You are a strategic advisor reviewing my goal portfolio. I want honest, analytical feedback — not encouragement.

My active goals:
[LIST YOUR GOALS — one per line. Include a rough deadline and the life area each belongs to.]

My context:
- My role / situation: [BRIEF DESCRIPTION]
- Approximate available focused hours per week: [X hours]
- Life areas most important to me right now: [WORK / PERSONAL / STUDY / HEALTH / CREATIVE / ADMIN — list 2–3 top priorities]

For each goal:
1. Classify it as: Professional / Personal / Learning / Financial / Health / Creative / Admin
2. Rate its specificity (1 = vague, 3 = clearly measurable)
3. Flag it if it looks more like a project or a task (not a true goal-level outcome)

For the portfolio overall:
4. Identify any goals that appear to conflict with each other (time, attention, or resource conflicts)
5. Identify any important life area that is underrepresented among my goals
6. Recommend which 1–2 goals I should prioritise if I could actively pursue only 2
7. Flag any goal that is vague enough to be meaningless as a planning input

Output as a structured table + brief commentary.
```

---

### Prompt 1.5 — Goal Success Criteria Stress Test

**Purpose:** Challenge a goal's success criteria to ensure they're actually measurable, observable, and in your control.

**When to use:** After writing your first draft of success criteria — before entering them into Notion as your final version.

---

```
You are a measurement specialist. Please stress-test the success criteria for the following goal.

Goal: [GOAL NAME AND OUTCOME STATEMENT]
Success criteria:
- [CRITERION 1]
- [CRITERION 2]
- [CRITERION 3]
(Add more if needed)

For each criterion, evaluate:
1. Observable — Can someone else verify this without asking how I feel? (Yes / Partially / No)
2. Within my control — Does this depend primarily on my actions, or on other people's decisions / market conditions / luck? (Mostly mine / Mixed / Mostly external)
3. Calibrated difficulty — Is this criterion too easy, too hard, or appropriately challenging given the goal?
4. Lagging vs. leading — Is this a lagging indicator (outcome happened) or a leading one (activity happened)? Flag leading indicators that might not confirm the real goal is reached.

Then:
5. Rewrite any criterion that failed checks 1–3 above with a stronger version
6. Suggest one additional criterion that I may have missed — something that would make it harder to "game" the success conditions
```

---

## Section 2: Strategic Planning and Roadmapping

---

### Prompt 1.6 — Goal Narration Prompt

**Purpose:** Turn a structured goal into a short motivational narrative — useful for reconnecting with the "why" behind a goal.

**When to use:** Optional. Use to write a 1-paragraph "goal story" to pin to the top of your Goals Database or use as a Monday morning ritual.

---

```
You are a narrative coach. I want a short, grounded motivational statement for the following goal — not generic inspiration, but something specific to my situation.

Goal: [GOAL NAME]
Outcome statement: [WHAT CHANGES WHEN THIS GOAL IS ACHIEVED]
Deadline: [DATE]
Success criteria:
- [CRITERION 1]
- [CRITERION 2]
- [CRITERION 3]
Why this goal matters to me personally: [YOUR REASON — even 1 rough sentence helps]

Please write:
1. A 1-paragraph narrative (3–5 sentences) describing what my work and life look like once this goal is achieved. Use specific and concrete language — not "you'll feel fulfilled" but what concretely changes.
2. One sentence I can use as a "north star" summary — something short enough to put at the top of my Notion goal page.

Constraints:
- No generic motivational language ("you've got this", "the journey begins", etc.)
- No clichés
- Ground everything in the specific goal and context I've provided
- Make it honest — if the goal is hard or unglamorous, the narrative should acknowledge that
```

---

### Prompt 1.7 — Long-Term Roadmap Prompt

**Purpose:** Given a goal with a long horizon (3–12 months), generate a high-level roadmap of phases or milestones.

**When to use:** When setting up a long-horizon goal that will span multiple weeks or months. Use before building out individual projects.

---

```
You are a strategic planning consultant. I need to map out a realistic roadmap for a long-horizon goal.

Goal: [GOAL NAME AND OUTCOME STATEMENT]
Start date: [DATE I'M BEGINNING]
Target completion: [DEADLINE]
My context and constraints: [KEY CONSTRAINTS — time per week, budget, dependencies, other commitments]

Please create a high-level roadmap with 3–5 phases. For each phase:
1. Name it as a completed state (e.g., "Foundation built" not "Build foundation")
2. Describe what is true at the end of this phase — 1–2 sentences
3. Suggest a realistic target date for completing this phase
4. List the 2–3 most critical activities that define this phase
5. Name the most important output or deliverable this phase produces

After the roadmap:
6. Identify the phase most likely to take longer than estimated — and why
7. Identify the single highest-leverage action I could take in the first 7 days to build momentum
8. Flag any assumption embedded in this roadmap that I should validate early (before it becomes an expensive wrong turn)
```

---

## Section 3: Persona-Specific Goal Design Prompts

Use these variants when the standard prompts need persona-specific context built in.

---

### Prompt 1.8 — Goal Design for Students

**Purpose:** Design academic and personal goals within a semester structure, balancing coursework, exams, internships, and personal growth.

**When to use:** Use Prompt 1.1 as a base, but add this context block to get more relevant output.

---

```
[Use Prompt 1.1 above. Add the following context block to your input:]

Additional student context:
- Current semester: [e.g., "Year 2, Semester 2", "Final year dissertation semester"]
- Key academic deadlines this term: [EXAMS / ASSIGNMENTS / DISSERTATION CHAPTERS with dates]
- My capacity outside coursework: [Approx hours/week available for non-coursework goals]
- What I'm hoping to accomplish beyond academics this semester: [INTERNSHIP SEARCH / SIDE PROJECT / SKILL LEARNING / ETC.]

Please flag any goal that would be genuinely high-risk to add during exam periods.
```

---

### Prompt 1.9 — Goal Design for Freelancers

**Purpose:** Design goals within the reality of client work, income targets, and the need to balance delivery vs. business development vs. personal life.

---

```
[Use Prompt 1.1 above. Add the following context block:]

Additional freelancer context:
- My current client load: [NUMBER OF CLIENTS / PROJECTS, approximate hours/week]
- Income goal or constraint: [MONTHLY TARGET OR MINIMUM THRESHOLD]
- The goal I'm finding it hardest to move forward on: [OFTEN: own products, marketing, skill building — things that aren't billable]
- Time I realistically have for non-client work each week: [X hours]

Please distinguish between goals that serve immediate income and goals that serve long-term leverage (building something that earns without 1:1 time). Flag any goal where effort and reward are misaligned.
```

---

### Prompt 1.10 — Goal Design for Content Creators

**Purpose:** Design goals around content output, audience growth, and the challenge of balancing creation, distribution, strategy, and "the day job."

---

```
[Use Prompt 1.1 above. Add the following context block:]

Additional creator context:
- My platform(s): [YOUTUBE / NEWSLETTER / PODCAST / INSTAGRAM / ETC.]
- My current output cadence: [HOW OFTEN YOU PUBLISH — e.g., "1 video/month", "inconsistently"]
- My goal for audience or output: [SUBSCRIBERS / OPEN RATE / VIEWS / NUMBER OF PIECES]
- Time available for content creation per week: [X hours — be honest]
- The part of content creation I keep skipping or avoiding: [E.g., distribution, SEO, editing, strategy]

Please design goals that balance growth metrics (audience size) with process metrics (publishing consistency), and flag any goal where the metric can be "gamed" without real progress.
```

---

*Next file: [`task_breakdown_prompts.md`](task_breakdown_prompts.md)*
