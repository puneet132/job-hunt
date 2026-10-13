# Daily digest prompt

A self-contained prompt for a scheduled task (Claude, ChatGPT or Gemini). Scheduled runs often can't read uploaded files, so everything needed is in the prompt. Replace each `<…>` before saving.

```text
Every day at <time, e.g. 7:50 PM IST>, find new job openings for me and send a short digest.

ABOUT ME
<2–4 lines: current title, years of experience, 2–3 strongest outcomes with numbers, domains.>
Current CTC <x> LPA, expected <x–y> LPA (minimum <x>), notice <x> days. <Shift>. <Relocation / remote preference>.

ROLES (priority order)
1. Product Manager, Associate Product Manager, Product Owner.
2. Delivery-side BA roles: the job is working with the development team to get the product built (requirement gathering, user stories, backlog grooming, sprint tracking, UAT, go-live). Titles include Business Analyst, Senior BA, Techno-Functional Analyst, Implementation Consultant/Analyst, Business Consultant, Post-sales BA, Delivery Manager, Technical Project Manager. Judge by the description. NOT a fit: data/BI/MIS analyst, finance/credit analyst, presales-only or sales consultant, SAP/Salesforce/ServiceNow configuration.

CITIES (priority order): <e.g. Gurugram; Delhi NCR; Pune; Bengaluru; Hyderabad; Mumbai/Navi Mumbai>; then India-open Remote. Ignore other cities.

RULES
- ONLY roles posted in the last 3 days. If the posting date can't be confirmed, leave it out. Old listings re-sent in alerts don't count.
- Years asked: up to <my years + 1> OK; <my years + 2 to + 3> = Stretch; more = drop.
- Drop: listed salary clearly below <floor> LPA, contract-to-hire, freelance, internships, fresher roles, staffing reposts when the company posting exists.
- Every role needs a real link copied from the source (LinkedIn: linkedin.com/jobs/view/<id>/; Naukri: remove everything after "?"). No link = leave it out.
- Never guess experience, salary or dates. If missing, write "Not listed".
- Don't repeat roles sent in earlier runs.

WHERE TO LOOK
1. My email (if connected): job-alert emails from the last 3 days from LinkedIn, Naukri, Instahyre, Indeed, iimjobs, Hirist, Cutshort, Wellfound, Foundit, Glassdoor, Talent500. Read-only.
2. Web: Indeed India; Weekday (weekday.works/jobs/product-manager-jobs-in-india, /product-owner-jobs-in-india, /business-analyst-jobs-in-india); career pages of <your target companies>, rotating through them.

RATING
Strong = target role, years fit, domain overlap with my work. Good = target role and years fit, new domain. Stretch = senior title, years at the edge, a hard gap, or a non-preferred shift.

OUTPUT (short; I read it on my phone)
First line: "X new roles posted in the last 3 days".
One section per city in the order above (skip empty ones). Inside each: Strong, Good, Stretch; product roles before BA roles.
Each role on one line: [Title — Company](link) · Strong/Good/Stretch · work mode · posted · exp asked · salary if listed · source · one-line reason.
Max 30 roles. If little is new, say so in one line. Last line: any source that couldn't be reached.
```
