# Job Hunt

An AI job-search assistant for **Product Manager, Product Owner and delivery-side Business Analyst roles**, built for India and adaptable to other markets. One skill runs on **Claude and ChatGPT**, with a Gem version for **Gemini**.

## What it does
- **Starts from your resume.** It reads your resume, fills in your profile, and asks only what's missing (targets, CTC, notice period, cities), with tap-to-answer options.
- **Finds fresh openings:** only roles posted in the last 3 days, from Indeed, Weekday, company career pages and your LinkedIn / Naukri / Instahyre alert emails.
- **Judges fit by the job description, not the title.** "BA" roles that are really reporting or SAP configuration get dropped. Every role is rated Strong / Good / Stretch with a reason.
- **Groups roles by city in your order:** default Gurugram → Delhi NCR → Pune → Bengaluru → Hyderabad → Mumbai → Remote.
- **Fixes your resume.** It researches live postings, checks ATS parsing and credibility, interviews you to surface missing achievements, and rebuilds a one-page resume.
- **Applies from a screenshot:** a tailored resume (built by a script, so it looks the same every time) plus a 5–8 line email.
- **Sends a daily digest** on a schedule and keeps a tracker of what you've applied to.
- **Stays honest:** it uses only your real facts, never invents links or dates, and never sends anything without your OK.

## Install
| Platform | How | Guide |
|---|---|---|
| **Claude** | Upload [`job-hunt.skill`](job-hunt.skill) in Settings → Capabilities → Skills | [`claude/`](claude/) |
| **ChatGPT** (paid) | Upload [`job-hunt.skill`](job-hunt.skill) in Plugins → Skills | [`chatgpt/`](chatgpt/) |
| **ChatGPT** (Free/Go) | A Project with [`chatgpt/instructions.txt`](chatgpt/instructions.txt) and the reference files | [`chatgpt/`](chatgpt/) |
| **Gemini** | A Gem with [`gemini/gem-instructions.txt`](gemini/gem-instructions.txt) and the reference files | [`gemini/`](gemini/) |

Then say **"Help me with my job hunt"** and attach your resume.

## What's inside
```
job-hunt.skill               packaged skill (zip of skills/job-hunt) for Claude and ChatGPT
skills/job-hunt/
  SKILL.md                   entry point: routing and principles
  references/
    onboarding.md            resume first, then only the missing questions
    profile-template.md      the profile the assistant builds and relies on
    search-rules.md          roles, delivery-BA definition, cities, 3-day rule, filters, fit, output
    platforms-india.md       every relevant Indian job platform and how to reach it
    application-workflow.md  job post → tailored resume + short email
    resume-review.md         market research, ATS/credibility checks, discovery interview, rebuild
    resume-format.md         one layout everywhere; how to build the file
    compensation-india.md    CTC terms, typical hikes, answering salary questions
    tracker.md               keeping track of roles and applications
    daily-digest-prompt.md   self-contained prompt for scheduled digests
    quality-checklist.md     checks before any job list, resume or email
  scripts/build_resume.py    JSON → one-page ATS-friendly DOCX/PDF
  assets/                    resume example (JSON), LaTeX template, tracker CSV
chatgpt/                     setup guide + Project instructions (fallback)
gemini/                      setup guide + Gem instructions
evals/evals.json             test prompts for checking the skill's behaviour
```

## Other countries or roles
Swap `platforms-india.md` and `compensation-india.md` for your market, and set your roles and cities during onboarding.

## Privacy
Your profile (with CTC and contact details) stays in your own chats, memory or project files. Don't commit a filled-in `profile.md` to a public repo; `.gitignore` blocks it.

## License
MIT
