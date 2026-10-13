#!/usr/bin/env python3
"""Shrink a .docx so it attaches reliably.

    python3 -I shrink_docx.py resume.docx resume_slim.docx

Why this exists
---------------
Email tools carry attachments as base64 inside the request. An oversized
payload fails, and the failure is often silent: the draft gets created, the
attachment doesn't, and the body still says "resume attached". That is the
worst outcome of an automated application — worse than no email at all.

A .docx is a ZIP of XML parts and a resume needs very few of them. This drops
the optional ones (theme, footnotes, endnotes, comments, font table, extended
and custom document properties), cleans the relationship and content-type
entries that pointed at them, and recompresses at maximum deflate. Typically
~40% smaller with no visible change; Word, Pages, LibreOffice, Google Docs and
ATS parsers all read the result normally.

Stdlib only. Run it on every resume before attaching.
"""

import os
import re
import sys
import zipfile

# Parts a resume never needs. Dropping a part means dropping every reference to
# it too, or Word reports the file as corrupt.
DROP_PREFIXES = (
    # python-docx's default template carries these two and they dominate the
    # file: a legacy Word 2010 style part and a document thumbnail.
    "word/stylesWithEffects.xml",
    "docProps/thumbnail.jpeg",
    "docProps/thumbnail.jpg",
    "word/theme/",
    "word/footnotes.xml",
    "word/endnotes.xml",
    "word/comments.xml",
    "word/fontTable.xml",
    "word/_rels/footnotes.xml.rels",
    "word/_rels/endnotes.xml.rels",
    "word/_rels/comments.xml.rels",
    "word/_rels/fontTable.xml.rels",
    "docProps/app.xml",
    "docProps/custom.xml",
)

# "stylesWithEffects" is matched in full so it can never catch word/styles.xml,
# which the document genuinely needs.
REL_RE = re.compile(
    rb"<Relationship[^>]*?(stylesWithEffects|thumbnail|theme|footnotes|endnotes"
    rb"|comments|fontTable|docProps/app\.xml|docProps/custom\.xml)[^>]*?/>",
    re.I,
)
CT_RE = re.compile(
    rb"<Override[^>]*?(stylesWithEffects|thumbnail|theme|footnotes|endnotes"
    rb"|comments|fontTable|custom-properties|extended-properties)[^>]*?/>",
    re.I,
)
# The thumbnail is also declared as a Default extension entry.
CT_DEFAULT_RE = re.compile(rb'<Default[^>]*?Extension="jpeg"[^>]*?/>', re.I)


def shrink(src, dst):
    with zipfile.ZipFile(src) as zin:
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zout:
            for item in zin.infolist():
                name = item.filename
                if name.endswith("/"):
                    continue
                if any(name.startswith(p) for p in DROP_PREFIXES):
                    continue
                data = zin.read(name)
                if name.endswith(".rels"):
                    data = REL_RE.sub(b"", data)
                elif name == "[Content_Types].xml":
                    data = CT_DEFAULT_RE.sub(b"", CT_RE.sub(b"", data))
                zout.writestr(name, data, zipfile.ZIP_DEFLATED, compresslevel=9)


def main():
    if len(sys.argv) != 3:
        print("usage: python3 -I shrink_docx.py <in.docx> <out.docx>", file=sys.stderr)
        return 1
    src, dst = sys.argv[1], sys.argv[2]
    if os.path.abspath(src) == os.path.abspath(dst):
        print("refusing to overwrite the source in place", file=sys.stderr)
        return 1

    shrink(src, dst)

    before, after = os.path.getsize(src), os.path.getsize(dst)
    # base64 inflates by 4/3, and that encoded size is what actually gets sent.
    print(
        f"{before:,} -> {after:,} bytes "
        f"({100 - after * 100 // max(before, 1)}% smaller; "
        f"~{after * 4 // 3:,} bytes base64)"
    )
    if after * 4 // 3 > 200_000:
        print(
            "warning: still large for an inline attachment — trim the resume to "
            "one page, or expect the attachment step to fail",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
