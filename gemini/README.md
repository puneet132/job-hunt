# Job Hunt for Gemini

Gemini doesn't load skill folders, so it runs as a **Gem** with the same rules uploaded as knowledge.

## A. Create the Gem
1. Gemini app → **Gems → New Gem** → name it "Job Hunt".
2. **Instructions:** paste all of [`gem-instructions.txt`](gem-instructions.txt).
3. **Knowledge:** upload these files from [`../skills/job-hunt/references/`](../skills/job-hunt/references/): `onboarding.md`, `search-rules.md`, `platforms-india.md`, `application-workflow.md`, `resume-review.md`, `resume-format.md`, `quality-checklist.md`, `compensation-india.md`. Gems take a limited number of files, so if you hit the cap, merge the smaller ones.
4. Start a chat with the Gem and attach your resume. It runs onboarding and asks only what's missing.
5. When it gives you `profile.md`, edit the Gem and add it to Knowledge.

## B. Daily digest (scheduled action)
1. Ask the Gem: "Fill in the daily digest prompt from my profile."
2. Paste the result into a normal Gemini chat and ask: "Schedule this every day at 7:50 PM IST." Manage it under **Settings → Scheduled actions**.

Scheduled actions depend on your plan and region. If the option isn't there, run the prompt manually or use the Claude or ChatGPT version for scheduling.

## C. Connect Google apps
Gemini app → **Apps** → turn on **Gmail**, **Google Drive** and **Google Docs**. Set daily job alerts on LinkedIn, Naukri and Instahyre so Gemini has alerts to read.

## Known limits
- No code execution for the resume builder in Gems. Gemini writes the tailored resume in the same section order, and you paste it into your Google Docs template.
- Sending applications with attachments is a manual step.
- Live LinkedIn/Naukri search isn't possible; Gemini relies on alert emails and public sites.
- Features change; if a step looks different, check Google's Gemini help centre.
