# Job search rules

Read the candidate profile first: target roles, cities, salary floor and years of experience come from there. The defaults below apply when the profile is silent.

## Target roles
Default priority:
1. **Product roles:** Product Manager, Associate Product Manager, Product Owner.
2. **Delivery-side Business Analyst roles.** Judge by the work, not the title. It counts when the person works hand-in-hand with the development team to get the product built: requirement gathering with business or clients, writing user stories and acceptance criteria, backlog grooming and sprint ceremonies, tracking delivery, UAT and go-live.
   - Titles this appears under: Business Analyst, Senior Business Analyst, Techno-Functional / Functional Analyst, Implementation Consultant, Implementation Analyst, Business Consultant, Post-sales Business Analyst, Delivery Manager, Technical Project Manager, Scrum-oriented Project Manager, Product Analyst (only when it's requirements/backlog work).
   - Not a fit even if titled "BA" or "consultant": data/BI/reporting analyst, MIS/Excel analyst, financial/credit/pricing analyst, presales-only or sales consultant, SAP/Salesforce/ServiceNow/ERP configuration consultant, delivery heads managing 20+ engineers.

## Cities
Use the profile's order. Default for India: Gurugram → Delhi NCR (Delhi, Noida, Ghaziabad, Faridabad) → Pune → Bengaluru → Hyderabad → Mumbai / Navi Mumbai / Thane → Remote (India-open). Skip cities not on the list.

## The 3-day rule
Only show roles **posted in the last 3 days** (today plus the 3 days before). Most roles stop taking applications quickly, and stale listings waste applications.
- Use the date the source shows: Indeed "Posted on", Weekday or LinkedIn "x days ago", or the date in a Naukri job ID (the 6 digits before the last block: ...-071026... = 07 Oct 2026).
- If the posting date can't be confirmed, or is older than 3 days, leave the role out.
- An alert that re-sends an old listing doesn't make it new.

## Filters
- **Years asked vs the candidate's years (Y):** minimum asked ≤ Y+1 → can be Strong or Good; Y+2 to Y+3 → Stretch at best; more than Y+3 → drop.
- **Salary:** drop only if a listed salary's top end is clearly below the candidate's floor. Keep roles with no salary listed.
- Drop job types the candidate excludes (by default: contract-to-hire, freelance, part-time, internships, fresher roles).
- Fully on-site roles: include only if Strong (unless the profile accepts on-site), and label them "On-site".
- Drop staffing-agency reposts when the company's own posting is available.
- Read the full description before rating Strong or Good. The title alone isn't enough.
- Deep specialisms the candidate lacks → Stretch or drop.

## Fit rating
- **Strong:** target role family, years fit, and clear domain overlap or a near-exact match to the candidate's current work.
- **Good:** target role family and years fit, but a new domain or a slightly different level.
- **Stretch:** a senior title, years at the edge, a hard gap (e.g. a mandatory certification), or a non-preferred shift.
Always give a one-line reason.

## Links and data honesty
- Every role needs a working link copied from the source. Strip tracking parameters (LinkedIn: keep `linkedin.com/jobs/view/<id>/`; Naukri: drop everything after `?`). No link → leave the role out.
- Never estimate. If experience, salary or the work mode isn't in the posting, write "Not listed".

## Output format
Group by city in priority order, skipping empty cities. Inside each city: Strong, then Good, then Stretch; product roles before BA roles at the same fit.

Each role on one line:
`[Job title — Company](link) · Strong/Good/Stretch · work mode · posted date · experience asked · salary if listed · source · one-line reason`

If the posting asks application questions, add one short line with the answers to give (from the profile's numbers).

Start with "X new roles posted in the last 3 days". Cap at about 30 roles; fewer good roles beat padding. End with any source that couldn't be reached.
