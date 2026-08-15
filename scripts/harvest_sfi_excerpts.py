#!/usr/bin/env python3
"""Harvest Krakauer-authored SFI Press chapter excerpts into the corpus."""
import html, json, pathlib, re, sys, time, urllib.request

HITS = json.load(open(sys.argv[1]))
OUT = pathlib.Path(sys.argv[2])

BOOK_BY_DOI_PREFIX = {
    "10.37911/9781947864023": ("History, Big History, & Metahistory", 2017),
    "10.37911/9781947864528": ("The Complex World: An Introduction to the Foundations of Complexity Science", 2024),
    "10.37911/9781947864542": ("Foundational Papers in Complexity Science", 2024),
    "10.37911/9781947864559": ("Foundational Papers in Complexity Science", 2024),
}
FALLBACK = {
    "whps-introduction": ("Worlds Hidden in Plain Sight", 2019),
    "16-transcience-disciplines-and-the-advance-of-plenary-knowledge": ("Worlds Hidden in Plain Sight", 2019),
    "21-complexity-worlds-hidden-in-plain-sight": ("Worlds Hidden in Plain Sight", 2019),
    "37-emergent-engineering-reframing-the-grand-challenge-for-the-21st-century": ("Worlds Hidden in Plain Sight", 2019),
    "preface-restoring-focus-at-a-planetary-scale": ("InterPlanetary Transmissions: Genesis", 2019),
    "foreword-the-quest-for-a-complex-unity": ("Emerging Syntheses in Science", 2019),
    "chapter-1-complex-economies-from-the-keynesian-orbit-to-the-darwinian-worm":
        ("The Economy as an Evolving Complex System IV", 2026),
}

def fetch(slug):
    req = urllib.request.Request(f"https://www.sfipress.org/{slug}",
                                 headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

def clean(h):
    body = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", h, flags=re.S)
    body = re.sub(r"</(p|div|h[1-6]|li|br)>", "\n\n", body)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", body))
    txt = re.sub(r"[ \t]+", " ", txt)
    txt = re.sub(r"\n\s*\n\s*", "\n\n", txt).strip()
    return txt

written = 0
for hit in HITS:
    slug = hit["slug"]
    try:
        raw = fetch(slug)
    except Exception as e:
        print(f"  SKIP {slug}: {e}")
        continue
    txt = clean(raw)

    title = (re.search(r"<title>(.*?)</title>", raw, re.S) or [None, slug])[1]
    title = html.unescape(title).replace("— SFI Press", "").strip()

    # Page layout: <nav chrome> Title  Book  pp. X–Y  DOI: ...  Author: ...  Excerpt  <body>
    parts = re.split(r"\bExcerpt\b", txt, maxsplit=1)
    excerpt = parts[1].strip() if len(parts) > 1 else ""
    # Trailing site furniture
    excerpt = re.split(r"\n\s*(?:Donate\b|News\b|Home\s+Books\b)", excerpt)[0].strip()
    if len(excerpt) < 400:
        print(f"  SKIP {slug}: excerpt too short ({len(excerpt)})")
        continue

    doi = hit.get("doi", "").rstrip(".")
    book, year = None, None
    for pref, (b, y) in BOOK_BY_DOI_PREFIX.items():
        if doi.startswith(pref):
            book, year = b, y
    if not book:
        book, year = FALLBACK.get(slug, (None, None))
    pages = (re.search(r"pp\.\s*([^\n]{0,24}?)\s*DOI", txt) or [None, ""])[1].strip()

    fname = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:70]
    path = OUT / f"{year or 'undated'}--sfipress-{fname}.md"
    fm = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        "person: david-krakauer",
        "section: by",
        "type: book-chapter",
        f"year: {year or ''}",
        f'venue: "SFI Press — {book}"' if book else 'venue: "SFI Press"',
        'authors: "David C. Krakauer"',
        f"source_url: https://www.sfipress.org/{slug}",
        "retrieved: 2026-08-13",
        "content: excerpt",
    ]
    if doi:
        fm.append(f"doi: {doi}")
    if pages:
        fm.append(f'pages: "{pages}"')
    fm.append('notes: "Opening excerpt published free on sfipress.org; the full chapter is '
              'not openly available (SFI Press gives ebooks in exchange for a donation). '
              'Harvested during the #774 SFI Press pass."')
    fm.append("---")
    path.write_text("\n".join(fm) + f"\n\n# {title}\n\n## Excerpt\n\n{excerpt}\n")
    written += 1
    print(f"  wrote {path.name} ({len(excerpt):,} chars)")
    time.sleep(0.2)

print(f"\n{written} files written")
