# Quality checklist: run before every output

These failures happened in real use. Check for them every time.

## Job lists
- [ ] Every role was posted within the last 3 days, and the posting date was actually read from the source, not assumed from an alert's send date.
- [ ] Every role has a working link copied from the source, with tracking parameters stripped. No "search the careers page" placeholders.
- [ ] The description was read for every role rated Strong or Good. Titles alone mislead (e.g. a "Product Manager" that's really pricing analytics).
- [ ] Years asked fit the rule. Roles needing far more experience were dropped, not rated Strong.
- [ ] No duplicates of roles already in the tracker. Job IDs on some boards change between searches, so compare company + title.
- [ ] Nothing estimated: experience or salary not in the posting shows "Not listed".
- [ ] Grouped by city in the user's order; Strong → Good → Stretch inside each city.

## Resumes
- [ ] One page; layout per `resume-format.md`.
- [ ] Every claim is in the profile; the honesty rules are respected.
- [ ] Text extraction shows titles and dates on clean, separate lines.
- [ ] Keywords from the job description are used only where they're true.

## Emails
- [ ] 5–8 lines of body, bullets, no caveat paragraphs.
- [ ] Answers any question the posting asked (CTC, notice period).
- [ ] Short LinkedIn reference in the signature.
- [ ] Resume attached, or the user told in one line to attach it.
- [ ] Not sent without the user's explicit OK.

## Scheduled runs
- [ ] The prompt is self-contained (scheduled runs often can't read uploaded files).
- [ ] After the first run, check its output against this list and tighten the prompt where it slipped.
