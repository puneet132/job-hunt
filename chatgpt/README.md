# Job Hunt for ChatGPT

## Option 1 (recommended): install the skill (paid plans)
ChatGPT supports the same Agent Skills format Claude uses, so the whole skill (onboarding, resume review, resume builder script, job search rules, quality checks) works as-is.

1. Download [`job-hunt.skill`](../job-hunt.skill) from the repo root. It's a zip; don't unzip it.
2. In the ChatGPT app: **Plugins → Skills → Create → Upload from your computer** → choose the file.
3. In a chat (Work mode), type `@job-hunt`, or just say "Help me with my job hunt" and attach your resume.

On Enterprise and Edu plans an admin has to turn Skills on first. **Codex users** (all plans, including Free): unzip the file and put the `job-hunt` folder in `~/.agents/skills/`, then type `$job-hunt`.

## Option 2: Project (Free or Go plans, or if you can't upload skills)
1. **Projects → New project** → "Job Hunt".
2. Project settings → **Instructions** → paste all of [`instructions.txt`](instructions.txt).
3. **Add files** from [`../skills/job-hunt/references/`](../skills/job-hunt/references/): `onboarding.md`, `search-rules.md`, `platforms-india.md`, `application-workflow.md`, `resume-review.md`, `resume-format.md`, `quality-checklist.md`, `compensation-india.md`, plus `../skills/job-hunt/scripts/build_resume.py` and `../skills/job-hunt/assets/resume-example.json`.
4. Start a chat in the project and attach your resume. It runs onboarding and asks only what's missing.
5. When onboarding gives you `profile.md`, add it to the project's files so every chat knows you.

A **Custom GPT** works the same way (Create → Configure: same instructions, same files as Knowledge) if you want to share it.

## Daily digest (both options)
Scheduled tasks can't use skills or project files, so the digest prompt has to stand alone.
1. Ask the assistant: "Fill in the daily digest prompt from my profile." It completes [`daily-digest-prompt.md`](../skills/job-hunt/references/daily-digest-prompt.md) for you.
2. Paste the result into a **normal chat** and add: "Make this a scheduled task every day at 7:50 PM IST."
3. **Settings → Notifications → Tasks:** turn on Email and/or Push.

## Connect Gmail
**Settings → Apps → Gmail → Connect.** The assistant can then read LinkedIn / Naukri / Instahyre / Indeed alert emails and draft applications. Set daily alerts on those sites (see `platforms-india.md`) so there's something to read.

## Known limits
- ChatGPT's Gmail drafts can't carry attachments; download the tailored resume and attach it yourself. Sending needs your approval each time.
- No live tracker page. Use a Google Sheet, or the CSV tracker in `tracker.md`.
- Live LinkedIn/Naukri search needs agent mode with you logged in; scheduled tasks rely on alert emails and public sites.
- Features and plan limits change; if a step looks different, check OpenAI's help centre.
