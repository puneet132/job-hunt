# Job Hunt for ChatGPT

Setup takes about 15 minutes. You'll use three ChatGPT features:

| Part | Feature | Does what |
|---|---|---|
| A | Project (or Custom GPT) | Day-to-day: find jobs, tailor resume + email from a screenshot, rate your resume, answer questionnaires |
| B | Scheduled task | Daily digest of roles posted in the last 3 days |
| C | Gmail app (connector) | Reads LinkedIn / Naukri / Instahyre / Indeed alert emails; drafts application emails |

## Before you start
Copy `../shared/profile-template.md` to `profile.md` and fill it in. Keep it private.

## A. Project
1. Sidebar → **Projects → New project** → name it "Job Hunt".
2. Project settings → **Instructions** → paste all of [`instructions.txt`](instructions.txt).
3. **Add files:**
   - your filled-in `profile.md`
   - [`../shared/search-rules.md`](../shared/search-rules.md)
   - [`../shared/platforms-india.md`](../shared/platforms-india.md)
   - [`../shared/application-workflow.md`](../shared/application-workflow.md)
   - your master resume (PDF or DOCX)
4. Test it in a chat inside the project: "Find Product Owner jobs posted in the last 3 days in Gurugram", or send a job-post screenshot.

**Custom GPT instead?** Explore GPTs → Create → Configure: paste the same instructions and upload the same files as Knowledge. Use this if you want to share the assistant. Scheduled tasks can't run Custom GPTs.

## B. Daily digest
Scheduled tasks can't read Project files, so the prompt has to be self-contained.
1. Open [`../shared/daily-digest-prompt.md`](../shared/daily-digest-prompt.md), copy the prompt and fill in every `<…>`.
2. Paste it into a **normal chat** (not inside the Project) and send. If ChatGPT doesn't schedule it automatically, add: "Make this a scheduled task every day at 7:50 PM IST."
3. Turn on delivery: **Settings → Notifications → Tasks → Email and/or Push**.

Limits: Plus allows 5 active tasks; Free allows 3 and only flexible time windows.

## C. Connect Gmail
**Settings → Apps → Gmail → Connect.** Then set daily job alerts on LinkedIn, Naukri and Instahyre (see `../shared/platforms-india.md`) so there's something to read.

## Known limits
- Gmail drafts created by ChatGPT can't carry attachments; download the tailored resume and attach it yourself. Sending needs your approval each time.
- Live LinkedIn/Naukri search needs agent mode with you logged in; scheduled tasks rely on alert emails and public sites.
- Features and plan limits change; check OpenAI's help centre if a step looks different.
