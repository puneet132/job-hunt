# Application workflow: job post → tailored resume + short email

The candidate sends a screenshot or the text of a job post, often with a recruiter's email address. Handle it end to end. Most candidates don't want to read tailoring notes; they want the finished resume and email.

## Steps
1. **Read the post:** title, company, location, experience asked, must-have skills, recruiter email, any application questions. Screenshots crop and recruiters write badly — if the company name or the contact route is genuinely unreadable, ask one short question rather than guessing. Work around everything else.
2. **Check the tracker for this company and role** before spending anything on tailoring. Reposts through staffing agencies are the norm; a duplicate application reads as careless and the candidate only gets one impression. On a hit, say which application it was and when, and stop.
3. **Check fit** against the candidate profile — `references/fit-assessment.md` has the three verdicts and what counts as a mismatch.
   - Strong or partial fit → continue without asking.
   - Mismatch (a required credential they lack, far more years than they have, a posting not open to them at all) → two lines on why, then stop.
4. **Tailor the resume** from the candidate's master resume:
   - Mirror the job description's keywords in the summary, skills and bullets, only where they're true for the candidate.
   - Put the most relevant bullets first. For BA/delivery roles, lead with requirements, user stories, backlog and UAT outcomes; for PM roles, lead with business outcomes and product decisions.
   - Never add experience, tools, certifications or numbers that aren't in the profile, and respect the profile's honesty rules.
   - One page, ATS-friendly: single column, standard headings, no tables, graphics or text boxes.
   - Name the file `<First>_<Last>_<Role>_Resume.pdf` (or .docx).
   - If the posting wants something genuinely absent — "must have 3 years of Kubernetes" with no Kubernetes anywhere — don't quietly invent it and don't quietly drop it. Say it's missing in one line and let the candidate decide.
5. **Write the email** (style below).
6. **Deliver:** create a **draft** addressed to the recruiter with the tailored resume attached. Never send or submit without the candidate's explicit OK — they're the one applying, and they should see what goes out under their name. See **Attachments** below; it's the step that fails.
7. **Report back in three lines:** what the role is, the fit verdict, and that the draft is ready. Not the resume, not the tailoring rationale. Surface only what they'd want to stop you over — a duplicate, a missing must-have, an attachment that didn't land.

## Attachments: the step that fails

An email that says "resume attached" with nothing attached is worse than no email. It's the one outcome here that actively damages the candidate, and it happens often enough to treat as the main risk.

- **Shrink the file first.** Email tools carry attachments as base64 inside the request, and an oversized payload fails — sometimes silently. Run `scripts/shrink_docx.py` on every resume before attaching; it strips the parts a resume never needs and cuts roughly 40% with no visible change.

  ```bash
  python3 -I scripts/shrink_docx.py resume.docx resume_slim.docx
  ```

- **Verify before claiming.** Many email APIs won't report whether an attachment landed — `get_draft` often doesn't list attachments at all. If it can't be confirmed, say so: "draft's ready — check the paperclip before you send." Never write "resume attached" in the body on faith.
- **Always attach something.** If the tailored build fails for any reason, attach the master resume and say that's what happened. An application with a generic resume still works; one with no resume doesn't.
- **Don't substitute a cloud link.** A Drive or Dropbox link reads as friction to a recruiter and often gets stripped by corporate mail. If attaching genuinely can't be done, hand the candidate the file instead.

## Email style
- **Short:** 5–8 lines of body. Tight bullets, minimal prose.
- Human and specific, not templated. No long caveat or apology paragraphs.
- Subject: `Application: <Role> — <Name> (<x> yrs, <domain>)`
- Body:
  - One opening line naming the role and where it was seen.
  - 2–3 bullets with the most relevant proof points for this job description.
  - One line with notice period, and answers to any questions the post asked (current CTC, expected CTC, notice period, relocation).
  - A one-line close.
- Signature: `Name · Phone · LinkedIn`. Keep the LinkedIn reference short; long URLs often get expanded into redirect links.
- If the candidate falls short on a requirement, use one short clause at most, or leave it out.

## Example
> **Subject:** Application: Product Owner — Asha Rao (4 yrs, Fintech)
>
> Hi Priya,
>
> I'm applying for the Product Owner role at Acme Payments (seen on LinkedIn).
> - Launched a merchant onboarding flow that cut activation time by half
> - Run two-week sprints with a 12-person team; own the backlog and UAT sign-off
> - Wrote the PRDs for UPI AutoPay, now used by 40,000+ merchants
>
> Notice period: 30 days. Resume attached.
>
> Thanks,
> Asha Rao · +91-90000 00000 · LinkedIn

## Other requests the assistant should handle
- **"Rate my resume for this JD":** score out of 10, the 3–5 missing keywords that are true for the candidate, and exact bullet edits.
- **Application questions** (CTC, "why this company", questionnaires): first person, short, from the profile. Keep AI or technical claims honest.
- **Interview prep:** STAR stories built only from the profile's experience bullets.
