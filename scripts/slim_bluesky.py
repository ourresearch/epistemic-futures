#!/usr/bin/env python3
"""Normalize raw Bluesky feed JSON into a compact, still-lossless-for-text form.

getAuthorFeed repeats the author's full profile (~850 bytes) on every post, and embeds
the *entire* parent and root post — including their authors — on every reply. For a
reply-heavy account that's most of the payload: Anil Dash's raw feed is 240 MB, over
GitHub's 100 MB file limit.

What we keep: the post's own record (text, createdAt, langs, facets, embeds), its uri/cid,
engagement counts, and labels. What we drop: the repeated author profile (written once to
_meta.json instead) and the full inlined parent/root objects (reduced to their URIs — the
parent's text is someone else's words, not this person's, and the URI preserves the link).

    python3 scripts/slim_bluesky.py                 # slim every timeline in place
    python3 scripts/slim_bluesky.py --check         # report sizes only
"""
import argparse, json, pathlib, sys


def slim(item):
    p = item.get("post", {}) or {}
    a = p.get("author", {}) or {}
    out = {
        "uri": p.get("uri"),
        "cid": p.get("cid"),
        "record": p.get("record"),
        "indexedAt": p.get("indexedAt"),
        "metrics": {
            k: p.get(k + "Count")
            for k in ("reply", "repost", "like", "quote", "bookmark")
            if p.get(k + "Count") is not None
        },
    }
    if p.get("labels"):
        out["labels"] = p["labels"]
    if a.get("did"):
        out["authorDid"] = a["did"]
    r = item.get("reply") or {}
    ctx = {}
    for side in ("parent", "root"):
        node = r.get(side) or {}
        if node.get("uri"):
            ctx[side] = node["uri"]
            who = (node.get("author") or {}).get("handle")
            if who:
                ctx[side + "Author"] = who
    if ctx:
        out["replyTo"] = ctx
    if item.get("reason"):  # repost marker
        out["reason"] = {"$type": item["reason"].get("$type")}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="dossiers")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    total_before = total_after = 0
    for f in sorted(pathlib.Path(args.root).glob("*/social/bluesky-timeline.jsonl")):
        before = f.stat().st_size
        items = []
        author = None
        with f.open() as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                raw = json.loads(line)
                if author is None:
                    author = (raw.get("post", {}) or {}).get("author")
                items.append(slim(raw))
        after_text = "".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items)
        total_before += before
        total_after += len(after_text.encode())
        pct = len(after_text.encode()) / max(before, 1)
        print(f"{f.parent.parent.name:<24} {before/1e6:>7.1f} MB -> {len(after_text.encode())/1e6:>6.1f} MB  ({pct:.0%})  {len(items):,} posts")
        if not args.check:
            f.write_text(after_text)
            if author:
                (f.parent / "bluesky-author.json").write_text(json.dumps(author, indent=1, ensure_ascii=False))
    print(f"\ntotal {total_before/1e6:.1f} MB -> {total_after/1e6:.1f} MB")


if __name__ == "__main__":
    main()
