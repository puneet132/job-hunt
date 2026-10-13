# Onboarding: resume first, then only the missing questions

Run this the first time someone uses the skill, or whenever no filled-in profile exists. The goal is a complete, accurate profile (see `profile-template.md`) with as little typing as possible from the user.

## Step 1: ask for the resume
Open with one short message:
> "To get started, send me your current resume (PDF, Word or a photo). I'll read it and only ask about what's missing."

If they don't have one handy, accept a LinkedIn profile export, a pasted summary, or answers to the questions in Step 3.

## Step 2: extract everything you can
Read the resume and fill in the profile template yourself:
- Name, contact, city, headline
- Each role: title, company, dates, location, and every bullet that has an outcome or a number
- Education, certifications, awards, skills, tools, projects
- Total years of experience, worked out from the dates
- Domains (insurance, fintech, e-commerce, healthcare and so on), inferred from the companies and projects

Note anything unclear or risky as you go: unexplained gaps longer than 6 months, a title that doesn't match the bullets, round-number metrics with no context, a payroll employer that differs from the client.

## Step 3: ask only what the resume can't tell you
Batch the questions (at most 4 at a time) and offer options wherever possible, so the user can tap rather than type. If the platform has a multiple-choice question tool (for example AskUserQuestion in Claude), use it; otherwise show numbered options and accept short replies like "1b, 2a".

**Round 1: targets and numbers (always ask; these are never on a resume)**
1. Which roles are you targeting? (Product Manager / Product Owner · Business Analyst on the delivery side · both, PM first · something else)
2. Which cities, in order of preference? (Offer the main hubs for their country; for India: Gurugram, Delhi NCR, Pune, Bengaluru, Hyderabad, Mumbai, Remote.)
3. Current CTC, expected CTC, and the lowest you'd accept?
4. Notice period? (Immediate · 15 days · 30 days · 60 days · 90 days)

**Round 2: preferences (ask once)**
5. Job types you'll accept? (Full-time direct · vendor / third-party payroll · contract-to-hire · freelance; multi-select)
6. Work mode? (Remote · hybrid · on-site · any)
7. Shift? (Day shift only · flexible)
8. Open to relocating? (Yes, anywhere in the country · selected cities only · no)

**Round 3: fill the resume's gaps (only those that apply)**
- An unexplained gap: "What were you doing between <dates>?" (Studying / exam prep · freelancing · family · health · job search · other)
- A vague metric: "How was '<metric>' measured? Can you defend it in an interview?" (Tracked in a tool · business report · rough estimate, so drop it)
- A title mismatch: "What's your official designation on payroll, and what do you actually do day to day?"
- No numbers at all for a role: "What changed because of your work there?" Offer examples: users, revenue, time saved, error rate, releases shipped.

For a deeper discovery of achievements the resume doesn't show, use the interview rounds in `resume-review.md`.

## Step 4: confirm and save
Show the filled profile in a compact summary (one screen) and ask: "Anything wrong or missing?" Then save it so it isn't lost:
- **Claude:** save to memory if available, and keep it as `profile.md` in the project or skill workspace.
- **ChatGPT:** ask permission to save the key facts to memory, and give the user `profile.md` to upload into their Project so every chat has it.
- **Anywhere else:** give the user `profile.md` and ask them to keep it and re-attach it in future chats.

## Step 5: offer the next step
Pick the most useful one for them:
- "Want me to review your resume against what recruiters are asking for right now?" (`resume-review.md`)
- "Want today's openings posted in the last 3 days?" (`search-rules.md`)
- "Want a daily digest on a schedule?" (`daily-digest-prompt.md`)

## Rules
- Never ask for something the resume already answers.
- Never invent a profile fact to fill a gap; leave it blank and ask.
- Keep each message short; most people do this on their phone.
- Salary, phone and email are private. Use them only in the user's own applications.
