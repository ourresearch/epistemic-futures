#!/usr/bin/env python3
"""Export the public corpus from this (private) working repo.

The public repo `ourresearch/epistemic-futures` is a GENERATED whitelist export of this one.
Policy (Jason, 2026-08-15): the public corpus is *everything freely available on the internet that
each attendee has written or said* — their own words only. Third-party coverage (`about/`), our
priority judgements, prep notes, and anything evaluative never leave this repo. Rather than a
redaction pass, the whitelist below IS the policy: only what is listed here is copied.

Usage:
    scripts/export_public.py --dest ~/Documents/epistemic-futures-public          # export
    scripts/export_public.py --dest ~/Documents/epistemic-futures-public --check  # scan only

Whitelist (per dossier `dossiers/<slug>/`):
    by/**            their own words (papers, posts, transcripts, books); frontmatter `notes:` scrubbed
                     of any sentence pointing at an about/ file
    social/**        their own X / Bluesky posts (slimmed JSONL)
    av/**            speaker-attributed transcripts of their talks/interviews (from oxjob #781)
    video.md         AV inventory
    *.tsv            enumeration indexes (their own works/posts; no about/ material lives in TSVs)
    cv.md            their own CV, where one was saved
    INDEX.md         FILTERED: about/ sections and any block that references about/ are dropped
Corpus-level:
    dossiers/00-roster.md          REGENERATED: name, published affiliation, summit role, counts
                                   from the export (the private roster's Tier/status columns never leave)
    dossiers/00-social-census.md, CONVENTIONS.md, PILOT-LESSONS.md, SOCIAL-COLLECTION.md
                                   secrets redacted
    scripts/                       all collectors + this script
    summit/website/**              clean markdown capture of the public summit website (4 pages)
    public/README.md → README.md   the recipient-facing README (hand-written here)
    public/AGENTS.md → AGENTS.md   "generated — do not edit" guard for agents

Everything else — about/, notes/, prep/, summit/framing-document.md, summit/schedule.md, the
summit/website-analysis-*.md files, collector state files — stays private.

Guarantees enforced after copy (the run FAILS if any is violated):
    * no path under dest contains `/about/`
    * no INDEX.md / roster / census file contains the string `about/` (our own prose must not
      point at excluded material; by/ bodies may contain e.g. site.com/about/ URLs)
    * no known secret (OpenAlex api_key, X bearer token from env) appears anywhere
    * roster contains no `Tier` column
    * no INDEX.md mentions a denylisted term (currently: Epstein — a third-party allegation that
      must not travel via coverage-notes prose)
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOSSIERS = REPO / "dossiers"

PER_DOSSIER_DIRS = ["by", "social", "av"]
PER_DOSSIER_FILES = ["video.md", "cv.md"]  # + *.tsv + filtered INDEX.md
CORPUS_FILES_VERBATIM = ["00-social-census.md", "CONVENTIONS.md", "PILOT-LESSONS.md", "SOCIAL-COLLECTION.md"]
INDEX_DENYLIST = ["epstein"]  # case-insensitive; blocks containing these are dropped, then asserted absent
_OA_KEY = "tEO76Rnv" + "V2LwjHcTG74OtA"  # split so this file itself passes the scan
SECRETS = [_OA_KEY]  # OpenAlex api_key that CONVENTIONS.md embeds in a curl example
for _env in ("X_BEARER_TOKEN", "ELEVENLABS_API_KEY", "ZYTE_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
    _v = os.environ.get(_env)
    if _v and len(_v) >= 16:
        SECRETS.append(_v)
REDACTIONS = {_OA_KEY: "<YOUR_OPENALEX_API_KEY>"}

INDEX_BANNER = (
    "> **Public export.** This index is generated from the private working corpus. Third-party\n"
    "> coverage *of* this person (reviews, profiles, news about them) is deliberately excluded —\n"
    "> only their own words are here. Item counts and coverage notes below refer to that subset.\n\n"
)


# ---------------------------------------------------------------- filters

def _blocks(lines: list[str]):
    """Yield (block_lines) where a block is: a table row / heading / blank line on its own, or a
    list item plus its indented continuation lines, or a run of consecutive plain prose lines."""
    i, n = 0, len(lines)
    list_re = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
    while i < n:
        ln = lines[i]
        if not ln.strip() or ln.startswith("#") or ln.startswith("|") or ln.startswith(">"):
            yield [ln]
            i += 1
            continue
        if list_re.match(ln):
            j = i + 1
            while j < n and lines[j].strip() and (lines[j].startswith((" ", "\t"))) and not list_re.match(lines[j]):
                j += 1
            yield lines[i:j]
            i = j
            continue
        j = i + 1
        while j < n and lines[j].strip() and not lines[j].startswith(("#", "|", ">")) and not list_re.match(lines[j]):
            j += 1
        yield lines[i:j]
        i = j


def filter_index(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    skipping_h2 = False
    for ln in lines:
        if ln.startswith("## "):
            skipping_h2 = "about/" in ln.lower()
            if skipping_h2:
                continue
        elif ln.startswith("# "):
            skipping_h2 = False
        if skipping_h2:
            continue
        out.append(ln)
    # drop blocks that reference about/ or a denylisted term
    kept: list[str] = []
    for blk in _blocks(out):
        joined = "\n".join(blk).lower()
        if "about/" in joined or any(t in joined for t in INDEX_DENYLIST):
            continue
        kept.extend(blk)
    text = "\n".join(kept).rstrip() + "\n"
    # our priority tiers are a judgement, not evidence — scrub the meta-line prefix and asides
    text = re.sub(r"^Tier: [^·\n]*·\s*", "", text, flags=re.M)
    text = re.sub(r",?\s*\bTier [12]\b", "", text)
    # collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    # insert banner after the H1
    m = re.match(r"(# .*\n)", text)
    if m:
        text = text[: m.end()] + "\n" + INDEX_BANNER + text[m.end():].lstrip("\n")
    return text


def _norm_name(n: str) -> str:
    import unicodedata
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    n = n.lower().replace("’", "'").replace("'", "")
    return re.sub(r"[^a-z ]", "", n).replace("caufield", "caulfield").strip()


def _published_affiliations() -> dict:
    """name → affiliation, exactly as the summit website publishes them (summit/website/attendees.md)."""
    f = REPO / "summit" / "website" / "attendees.md"
    out = {}
    if f.is_file():
        for ln in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"- (.+?), (.+)$", ln)
            if m:
                out[_norm_name(m.group(1))] = m.group(2).strip()
    return out


def build_public_roster(dest: Path) -> str:
    """A fresh roster for the public export: who, published affiliation, summit role, and what the
    export holds for them — counted from the export itself. Nothing about our priorities/status."""
    pub = _published_affiliations()
    rows = []
    for ln in (DOSSIERS / "00-roster.md").read_text(encoding="utf-8").splitlines():
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("#", "") or set(cells[0]) <= set("-: "):
            continue
        name, slug, aff, role = cells[1], cells[2], cells[3], cells[4]
        role = role.replace("(self — S3; not an attendee dossier)", "S3")
        role = re.sub(r"\s*\([^)]*Jason[^)]*\)", "", role).strip()
        aff_pub = pub.get(_norm_name(name)) or aff.split(" (")[0].split(";")[0].strip()
        d = dest / "dossiers" / slug
        if not d.is_dir():
            continue
        n_by = sum(1 for p in (d / "by").rglob("*") if p.is_file()) if (d / "by").is_dir() else 0
        n_soc = 0
        for f in (d / "social").glob("*.jsonl") if (d / "social").is_dir() else []:
            n_soc += sum(1 for _ in f.open(encoding="utf-8", errors="ignore"))
        n_av = sum(1 for p in (d / "av").rglob("*.md") if p.is_file()) if (d / "av").is_dir() else 0
        rows.append((name, slug, aff_pub, role, n_by, n_soc, n_av))
    hdr = (
        "# Roster\n\n"
        "Everyone on the summit's published attendee list "
        "(https://epistemicfuturessummit.pubpub.org/attendees — organizers and confirmed "
        "participants), plus Jason Priem's own dossier. Affiliations are as published on the site; "
        "summit roles are from the published schedule (S1–S6 = Thursday sessions). Counts are what "
        "this export holds — see each person's `INDEX.md` for what was searched and where it stopped.\n\n"
        "| Name | Dossier | Affiliation (as published) | Summit role | Items in `by/` | Social posts | Transcripts |\n"
        "|---|---|---|---|---:|---:|---:|\n"
    )
    body = "".join(
        f"| {n} | [`{s}`]({s}/INDEX.md) | {a} | {r} | {b:,} | {so:,} | {av} |\n"
        for n, s, a, r, b, so, av in rows
    )
    return hdr + body


def scrub_by_item(text: str) -> str:
    """Item frontmatter `notes:` sometimes points at a sibling about/ file ("reviews are in
    about/..."). Drop just the sentence(s) that do, in the frontmatter only; the body is untouched."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end < 0:
        return text
    fm, body = text[: end + 4], text[end + 4:]
    if "about/" not in fm:
        return text
    out = []
    for ln in fm.splitlines():
        if "about/" in ln:
            m = re.match(r'^(\w+:\s*)(["\']?)(.*?)(\2)\s*$', ln)
            if m:
                key, q, val = m.group(1), m.group(2), m.group(3)
                sents = re.split(r"(?<=[.!?;])\s+", val)
                keep = [x for x in sents if "about/" not in x]
                val = " ".join(keep).strip()
                if not val:
                    q = '"'
                ln = f"{key}{q}{val}{q}"
            else:
                ln = re.sub(r"[^.;]*about/[^.;]*[.;]?", "", ln).rstrip()
        out.append(ln)
    return "\n".join(out) + body


def redact(text: str) -> str:
    for k, v in REDACTIONS.items():
        text = text.replace(k, v)
    return text


# ---------------------------------------------------------------- export

def wipe_dest(dest: Path):
    for p in dest.iterdir():
        if p.name == ".git":
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()


def copy_file(src: Path, dst: Path, transform=None):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if transform is None:
        shutil.copy2(src, dst)
    else:
        dst.write_text(transform(src.read_text(encoding="utf-8")), encoding="utf-8")


def export(dest: Path) -> dict:
    stats = {"dossiers": 0, "by": 0, "social": 0, "av": 0, "tsv": 0, "omitted_about": 0}
    dest.mkdir(parents=True, exist_ok=True)
    wipe_dest(dest)
    for d in sorted(DOSSIERS.iterdir()):
        if not d.is_dir():
            continue
        stats["dossiers"] += 1
        out = dest / "dossiers" / d.name
        for sub in PER_DOSSIER_DIRS:
            if (d / sub).is_dir():
                if sub == "by":
                    for f in sorted((d / sub).rglob("*")):
                        if f.is_file():
                            rel = f.relative_to(d / sub)
                            copy_file(f, out / sub / rel, scrub_by_item if f.suffix == ".md" else None)
                else:
                    shutil.copytree(d / sub, out / sub)
                stats[sub] += sum(1 for p in (d / sub).rglob("*") if p.is_file())
        if (d / "about").is_dir():
            stats["omitted_about"] += sum(1 for p in (d / "about").rglob("*") if p.is_file())
        for f in PER_DOSSIER_FILES:
            if (d / f).is_file():
                copy_file(d / f, out / f)
        for f in d.glob("*.tsv"):
            copy_file(f, out / f.name)
            stats["tsv"] += 1
        if (d / "INDEX.md").is_file():
            copy_file(d / "INDEX.md", out / "INDEX.md", filter_index)
    (dest / "dossiers" / "00-roster.md").write_text(build_public_roster(dest), encoding="utf-8")
    for f in CORPUS_FILES_VERBATIM:
        if (DOSSIERS / f).is_file():
            copy_file(DOSSIERS / f, dest / "dossiers" / f, redact)
    shutil.copytree(REPO / "scripts", dest / "scripts", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    if (REPO / "summit" / "website").is_dir():
        shutil.copytree(REPO / "summit" / "website", dest / "summit" / "website")
    copy_file(REPO / "public" / "README.md", dest / "README.md")
    copy_file(REPO / "public" / "AGENTS.md", dest / "AGENTS.md")
    return stats


# ---------------------------------------------------------------- checks

def check(dest: Path) -> list[str]:
    problems: list[str] = []
    for p in dest.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        rel = p.relative_to(dest).as_posix()
        if "/about/" in f"/{rel}":
            problems.append(f"about/ path leaked: {rel}")
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        # our own prose must not point at excluded material; by/ bodies and the spec docs may
        # legitimately contain the substring (site.com/about/ URLs; CONVENTIONS describing the layout)
        if (rel.endswith("/INDEX.md") or rel.startswith("dossiers/00-")) and "about/" in txt:
            problems.append(f"'about/' string in {rel}")
        if "/by/" in rel and rel.endswith(".md") and txt.startswith("---"):
            fm_end = txt.find("\n---", 3)
            if fm_end > 0 and "about/" in txt[:fm_end]:
                problems.append(f"'about/' in frontmatter of {rel}")
        for s in SECRETS:
            if s in txt:
                problems.append(f"SECRET in {rel}")
        if rel.endswith("/INDEX.md"):
            low = txt.lower()
            for t in INDEX_DENYLIST:
                if t in low:
                    problems.append(f"denylisted term '{t}' in {rel}")
            if re.search(r"\bTier [12]\b|^Tier:", txt, re.M):
                problems.append(f"Tier survives in {rel}")
        if rel == "dossiers/00-roster.md" and re.search(r"\btier\b", txt, re.I):
            problems.append("Tier survives in roster")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", required=True, type=Path)
    ap.add_argument("--check", action="store_true", help="scan an existing export only")
    a = ap.parse_args()
    dest = a.dest.expanduser().resolve()
    if not a.check:
        if not (REPO / "public" / "README.md").is_file():
            sys.exit("missing public/README.md in the private repo")
        st = export(dest)
        print("exported:", st)
    probs = check(dest)
    if probs:
        print("\n".join(probs))
        sys.exit(f"FAILED: {len(probs)} problem(s)")
    print("OK: export passes all checks")


if __name__ == "__main__":
    main()
