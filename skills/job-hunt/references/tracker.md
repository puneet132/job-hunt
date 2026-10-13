# Application tracker

A tracker stops the same role from being sent twice and shows the user where each application stands. Use the best option the platform offers.

## Columns (same everywhere)
`date_added, posted_on, city, title, company, fit, family, link, source, status, reason, notes`
- `fit`: Strong / Good / Stretch
- `family`: product / delivery
- `status`: new / applied / interviewing / offer / rejected / skipped

`assets/tracker-template.csv` has the header row.

## Options, best first
1. **A live tracker page.** In Claude, if artifacts with a shared database are available, publish a small page that lists the roles grouped by city with Applied / Interviewing / Skip buttons, and have the daily digest add rows to its database. This works best because the user can update status from their phone.
2. **A connected spreadsheet** (Google Sheets or Excel through a connector). The digest appends rows; the user edits the status column.
3. **A CSV file.** The assistant updates `tracker.csv` each time and gives it back to the user, who re-uploads it next time.
4. **Nothing persistent.** Scheduled runs can't keep state, so ask the run to avoid repeating roles from its own earlier outputs, and accept that some repeats will slip through.

## When the user reports an update
"Applied to X", "Got an interview at Y", "Z is closed" → update the row's status, and stop listing closed roles. If a listed role turns out to be closed, remove it, find out why it slipped through (usually an unverified posting date), and tighten that check.
