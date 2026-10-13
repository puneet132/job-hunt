# Job Hunt for Claude

The skill lives in [`../skills/job-hunt/`](../skills/job-hunt/). It's the same folder ChatGPT uses.

## Install
**Claude app (claude.ai, desktop, mobile)**
1. Download [`job-hunt.skill`](../job-hunt.skill) from the repo root.
2. **Settings → Capabilities → Skills → Upload skill**, then choose the file.

**Claude Code**
```bash
git clone https://github.com/puneet132/job-hunt.git
cp -r job-hunt/skills/job-hunt ~/.claude/skills/
```

## First use
Say "Help me with my job hunt" and attach your resume. Claude reads it, asks only what's missing (multiple choice where it can), and saves your profile. Then:
- "Today's openings": roles posted in the last 3 days, grouped by city
- (job-post screenshot): tailored one-page resume plus a short email, as a Gmail draft with the resume attached if Gmail is connected
- "Is my resume good enough?": market research, ATS check, discovery interview, rebuild
- "Send me openings every day at 7:50 PM": a scheduled task, plus a live tracker page where your plan supports artifacts

## Works best with
- **Gmail connector:** reads job-alert emails; creates drafts with the resume attached
- **Web search and fetch:** Weekday, company career pages
- **Code execution:** builds resume files with `scripts/build_resume.py`
- **An Indeed connector,** if your workspace has one
