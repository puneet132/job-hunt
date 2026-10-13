# Resume format

The same layout on every platform, so a tailored resume always looks like the master.

## Layout (ATS-friendly, one page)
1. Name (large), a headline line ("Product Owner | Product Manager · Domain"), then one contact line: phone · email · LinkedIn (short form) · city
2. Summary: 3–4 lines, bold optional, leading with the two strongest outcomes
3. Experience: for each role, "Title at Company" with dates right-aligned, one italic line of context (client, product, scope) with the city right-aligned, then 4–6 bullets
4. Projects (optional)
5. Skills: 3–4 labelled lines (e.g. Product · Analysis & Delivery · AI · Tools)
6. Education & Awards

Rules: single column, standard section names, no tables, icons, photos, text boxes or headers and footers. Dates as "Mon YYYY – Mon YYYY". File name `<First>_<Last>_<Role>_Resume.pdf`.

## Building the file
`scripts/build_resume.py` turns a JSON description of the resume into a DOCX, and into a PDF too if LibreOffice is installed. It needs `python-docx`, which is preinstalled in most code-running sandboxes (Claude's and ChatGPT's); otherwise run `pip install python-docx`.

```bash
python scripts/build_resume.py resume.json --out Jane_Doe_Product_Owner_Resume.docx --pdf
```

The JSON shape is in `assets/resume-example.json`. Fill it from the profile, tailor the wording for the job description, and build.

If the platform can't run code, write the resume in the same section order as plain text, and tell the user to paste it into their own Word or Google Docs template.

## Checks after building
- Exactly one page. If it overflows, shorten bullets before shrinking fonts below 10pt.
- Extract the text from the PDF (`pdftotext` or pdfminer). Titles and dates must come out cleanly, on their own lines, not run together.
- No claim that isn't in the profile.

## LaTeX alternative
`assets/resume-template.tex` is the same layout in LaTeX, for users who prefer Overleaf. Compile with XeLaTeX.
