# Job Hunt for Gemini

You'll use three Gemini features:

| Part | Feature | Does what |
|---|---|---|
| A | Gem (custom Gemini) | Day-to-day: find jobs, tailor resume + email from a screenshot, rate your resume, answer questionnaires |
| B | Scheduled action | Daily digest of roles posted in the last 3 days |
| C | Google Workspace apps (Gmail, Docs, Drive) | Reads job-alert emails; puts tailored resumes into Google Docs |

## Before you start
Copy `../shared/profile-template.md` to `profile.md` and fill it in. Keep it private.

## A. Create the Gem
1. In the Gemini app: **Gems → New Gem** (Gem manager) → name it "Job Hunt".
2. **Instructions:** paste all of [`gem-instructions.txt`](gem-instructions.txt).
3. **Knowledge:** upload
   - your filled-in `profile.md`
   - [`../shared/search-rules.md`](../shared/search-rules.md)
   - [`../shared/platforms-india.md`](../shared/platforms-india.md)
   - [`../shared/application-workflow.md`](../shared/application-workflow.md)
   - your master resume
4. Save, then test: "Find Product Owner jobs posted in the last 3 days in Gurugram", or upload a job-post screenshot.

## B. Daily digest (scheduled action)
1. Open [`../shared/daily-digest-prompt.md`](../shared/daily-digest-prompt.md), copy the prompt and fill in every `<…>`.
2. Paste it into a normal Gemini chat and ask Gemini to schedule it daily at your time ("Schedule this every day at 7:50 PM IST"). Manage it later from **Settings → Scheduled actions**.
3. Results arrive as Gemini notifications (and in the scheduled action's chat).

Scheduled actions are limited to certain plans and regions, and Google changes this often. If you don't see the option, run the digest prompt manually or use the Claude or ChatGPT version for scheduling.

## C. Connect Google apps
Gemini app → **Apps / Extensions** → turn on **Gmail**, **Google Drive** and **Google Docs**. Then set daily job alerts on LinkedIn, Naukri and Instahyre (see `../shared/platforms-india.md`) so Gemini has alerts to read.

## Known limits
- Gemini can read Gmail and help draft replies, but sending applications with attachments is still a manual step: copy the email, attach the resume, send.
- Live LinkedIn/Naukri search isn't possible; Gemini relies on alert emails and public sites.
- Features and plan limits change; check Google's Gemini help centre if a step looks different.
