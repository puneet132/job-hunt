# Job Hunt for Claude

`job-hunt/` is a standard Agent Skill (a `SKILL.md` plus reference files). Claude loads it automatically when you ask for job openings, share a job post, or ask to tailor your resume.

## Install
**Claude app (claude.ai, desktop, mobile)**
1. Download `job-hunt.skill` from this repo's Releases page, or zip the `job-hunt/` folder yourself.
2. **Settings → Capabilities → Skills → Upload skill**, then choose the file.

**Claude Code**
```bash
git clone https://github.com/<owner>/job-hunt.git
cp -r job-hunt/claude/job-hunt ~/.claude/skills/
```

## First use
Start a chat with: "Set up my job hunt profile," and attach your resume. Claude fills in `profile-template.md` with you, then you can ask:
- "Today's openings": roles posted in the last 3 days, grouped by city
- (job-post screenshot): tailored one-page resume plus a short email, saved as a Gmail draft if Gmail is connected
- "Rate my resume for this JD"
- "Send me openings every day at 7:50 PM": creates a scheduled task where your Claude plan supports it

## Works best with
- **Gmail connector:** reads LinkedIn / Naukri / Instahyre / Indeed alert emails, and creates application drafts with the resume attached
- **Web search and fetch:** Weekday, company career pages
- **An Indeed connector,** if available in your Claude workspace
