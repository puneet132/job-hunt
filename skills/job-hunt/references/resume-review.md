# Resume review and rebuild

Use this when the user asks whether their resume is good enough, gets no callbacks, or wants it rebuilt for a target role.

## 1. Research what the market asks for
Before judging the resume, pull 6–10 current job descriptions for the user's top target role in their top city (job board search plus `get details` / open the posting). Tally how many ask for each of these:
- ownership of outcomes, not just delivery
- product metrics (activation, adoption, conversion, retention, NPS)
- customer discovery (interviews, focus groups, field research)
- technical depth (APIs, integrations, architecture)
- AI / LLM product experience
- hands-on data (SQL, Power BI, analytics tools)
- domain depth for the user's sector
- roadmap, strategy and trade-off decisions
- business impact (revenue, cost, conversion)
- certifications (e.g. PSPO, CSPO, CBAP)

Show the user a short table: requirement · how many of N postings ask for it · how their resume covers it today.

## 2. Check why it may be getting filtered out
Run these checks and report only what fails:
- **ATS parsing:** extract the text the way an ATS would (e.g. `pdftotext` or pdfminer on the PDF). Job titles and dates must come out as separate, readable lines. Tables, columns, text boxes, icons and headers or footers often scramble.
- **Headline vs history:** a "Product Manager" headline over a history of BA titles gets rejected in seconds. The headline should be what they are now, pointing at where they're going (e.g. "Product Owner | Product Manager").
- **Designation honesty:** the title shown must survive a background check. If the payroll title differs, show "Payroll title (Actual role)", e.g. "Business Consultant (Product Owner)".
- **Gaps:** any unexplained gap over 6 months needs one line.
- **Metrics:** round percentages with no context ("40% improvement") read as invented. Every number should be something the user can explain in 20 seconds.
- **Filler:** buzzword lists ("growth-first thinking", "synergy") and 30-item keyword blocks read as AI-written. Cut them.
- **Length:** one page up to about 8 years of experience.
- **Expected CTC:** if the jump from current to expected is well above typical hikes for their market (in India, roughly 30–40% for a switch), say so plainly. It often matters more than the resume.

## 3. Discovery interview (find what's missing)
Most resumes leave out the person's best evidence. Ask in short rounds of up to 4 questions, with options where possible (use a multiple-choice tool if the platform has one). Skip anything the resume already answers.

**Round 1: foundation**
- Education details worth showing (grade, notable projects)? Anything in gap years?
- At each employer: designation at joining and leaving, roughly how many projects, typical team size?

**Round 2: current role, the strongest story**
- What products or modules do you own end to end? Any launched for the first time at the company?
- What changed because of them? Before vs after: time, users, revenue, cost, errors, adoption.
- How many users or customers? Over what period?
- Which systems or teams did you integrate with? How hands-on were you with APIs (wrote specs · reviewed and tested · business requirements only)?
- How much did you decide what got built (prioritised the backlog · pushed back or cut scope · proposed features · executed what business decided)?
- Who do you work with (CXO/VP · sales or channel heads · vendors · compliance/ops/security)?
- Release cadence, and any quality result you can defend (e.g. no requirement-related production defects)?

**Round 3: previous roles**
- Best one or two projects: client type, what you owned, outcome in numbers.
- Presales: how many pitches, how many won, deal size if known?

**Round 4: craft**
- Discovery methods you've actually used (interviews, shadowing, workshops, surveys, benchmarking)?
- Analytics tools used hands-on (Power BI, Mixpanel/Amplitude/GA, SQL you write yourself, Excel)?
- A/B tests: ran one yourself, or supported someone else's?
- Defined event tracking or a metrics plan before a launch?

**Round 5: AI and side projects**
- AI features you've written requirements for, tested or shipped? Measured results?
- Side projects: what, who uses them, any numbers?

**Round 6: extras**
- Certifications done or in progress? Awards? Mentoring, process improvements, internal tools?

Record every answer in the profile, including the honesty rules (numbers that were estimates, things they only supported).

## 4. Rebuild
- Lead the summary with their two strongest outcomes.
- Bullets: what you did, how, and the result. Put the number first where there is one.
- Remove or soften anything they can't defend. Add the evidence the interview surfaced.
- Keep one master resume that covers both product and delivery-BA keywords, and tailor it per application (see `application-workflow.md`).
- Build the file with `scripts/build_resume.py` (see `resume-format.md`), then re-run the ATS parsing check on the output.

## 5. Report back
In a few lines: what changed, what you removed and why, and the 2–3 things still worth doing (e.g. a certification, a referral at their current client, a realistic CTC ask).
