# Job Hunt

An AI job-search assistant for **Product Manager, Product Owner and delivery-side Business Analyst roles in India**. It runs on **Claude, ChatGPT or Gemini**.

## What it does
- **Finds fresh openings:** only roles posted in the last 3 days, from Indeed, Weekday, company career pages, and the LinkedIn / Naukri / Instahyre alert emails in your inbox.
- **Filters by fit:** judges each role by its description, not its title, so "Business Analyst" postings that are really Excel reporting or SAP configuration are dropped. Rates every role Strong / Good / Stretch with a one-line reason.
- **Groups by city in your order:** default Gurugram → Delhi NCR → Pune → Bengaluru → Hyderabad → Mumbai → Remote.
- **Applies from a screenshot:** send a job post and get a tailored one-page ATS-friendly resume plus a 5–8 line application email.
- **Sends a daily digest** on a schedule.
- **Stays honest:** it only uses facts from your profile, never invents links, dates, salaries or experience, and never sends anything without your OK.

## Pick your assistant
| Platform | Folder | What you set up |
|---|---|---|
| Claude | [`claude/`](claude/) | Install the `job-hunt` skill |
| ChatGPT | [`chatgpt/`](chatgpt/) | A Project (or Custom GPT) + a scheduled task |
| Gemini | [`gemini/`](gemini/) | A Gem + a scheduled action |

Each folder's README has step-by-step setup (about 15 minutes).

## Shared knowledge files
All three platforms use the same rules, in [`shared/`](shared/):
| File | Purpose |
|---|---|
| `profile-template.md` | Your profile: facts, numbers, targets, honesty rules. Fill in once and keep private. |
| `search-rules.md` | Target roles, delivery-BA definition, city order, 3-day rule, filters, fit rating, output format |
| `platforms-india.md` | Every relevant Indian job platform and how the assistant reaches it |
| `application-workflow.md` | Job post → tailored resume + short email, with an example |
| `daily-digest-prompt.md` | Self-contained prompt for scheduled daily digests |

The Claude skill bundles copies of these in `claude/job-hunt/references/`.

## Customising
- **Other roles or cities:** edit the targets in your profile; `search-rules.md` follows the profile.
- **Other countries:** replace `platforms-india.md` with your market's job boards and update the city list.

## Privacy
Your filled-in `profile.md` contains salary and contact details. Keep it out of public repos (`profile.md` is in `.gitignore`).

## License
MIT
