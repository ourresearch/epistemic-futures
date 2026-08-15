---
title: "How I am publishing right now"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2026
date: "2026-05-28"
venue: "Data Leverage (Digital Garden / dataleverage.substack.com)"
authors: "Nicholas Vincent"
source_url: "https://nickmvincent.github.io/meta-notes/current-publishing-flow.html"
retrieved: "2026-08-13"
content: "full-text"
notes: "Dek: A rough map of my current local Markdown to Leaflet, Substack, and social-post workflow. Garden section: meta-notes. Mirrored on the Data Leverage Substack."
---

# How I am publishing right now

## Full text

[status: rough draft]

This post is just meant to briefly document the current state of my
blogging workflow.

The basic version is:

- I plan to now write the majority of my posts in Markdown on my local
machine (or, write in Docs/Word then convert to Markdown so I have a
plaintext copy of the content).

- I keep these Markdown files in the same source monorepo as my
personal website.

- I use a script (lightweight, mainly produced using Codex + GPT5.5.
-- fairly confident this can be reproduced and modified from any coding
agent quickly as needed) to sync those Markdown files to my Leaflet Data
Leverage publication.

- I use another script to produce a copy-pastable HTML version that I
can paste into Substack manually.

- I usually try to crosspost or announce the post on Twitter/X,
Bluesky, and LinkedIn.

- I am also starting to categorize posts into lanes: longer Data
Leverage posts, short focus posts, short reaction posts that stay in the
main Data Leverage publication, and these meta notes about
writing/blogging/process.

The monorepo has five main writing lanes:

- content/writing/drafts/ for private-ish local drafts
that I do not intend to publish directly.

- content/writing/posts/ for longer Data Leverage
pieces.

- content/writing/reaction-posts/ for short reaction
posts that should remain in the main Data Leverage publication. Each
begins with a reaction to: source link, like a standardized
quote tweet.

- content/writing/short-posts/ for short focus
posts.

- content/writing/notes/ for this meta-blog /
notes-on-writing track.

I keep track of publication routing in
state/digital-garden/publications.json. The shared content
index at state/digital-garden/content-index.json connects
the writing lanes to personal-site entries and scholarly references. In
practice, this means the repo knows about three Leaflet destinations:
the main Data Leverage publication, the focus short-posts publication,
and notesonnotes. Short reactions stay in the main Data Leverage lane
and are sorted separately only in the garden view. This is nice because
it lets the same local Markdown-first pattern apply across multiple
public surfaces without forcing every kind of writing to pretend to be
the same thing.

The main loop, when I am being disciplined, is something like
this:

- Write or edit a Markdown file locally.

- Run the local helpers that extract references, build backlinks,
render HTML, and build the little garden view.

- Check status to see what the repo thinks is changed,
publish-relevant, or stale.

- Dry-run the Leaflet sync.

- Commit and push, because the live publish path currently insists
that publish-relevant files are clean and pushed.

- Run the live Leaflet sync.

- Generate the Substack paste preview if the post is also going to
Substack.

- Manually paste into Substack, tweak anything weird, publish
there.

- Announce the post on the social sites, and ideally record those
announcements in the distribution ledger.

The social distribution step is the least automated part. Usually I
want some combination of:

- a Twitter/X post,

- a Bluesky post,

- a LinkedIn post,

- maybe some other targeted sharing if the post is relevant to a
particular community.

The repo has a content/writing/distribution.md ledger
and helper commands for recording mirrors and announcements. The idea is
that full mirrors, like Substack copies, can be marked stale if the
source Markdown changes after the recorded commit, while social
announcements are treated as "non-blocking".

The broader philosophy here is that I want the canonical version of a
post to be something I can edit locally, diff, render, cite from, and
move between platforms. I also want a relatively simple way to handle
versioning.

Source revision history

Selected Git commits that changed this source file.

- 542114960e 2026-08-03 - Add a dedicated reaction-post lane

- 9fb4674b8a 2026-07-12 - Migrate blog into digital presence monorepo

Source and AT Protocol record

Source path
content/writing/notes/2026-05-28-current-publishing-flow.md

AT Protocol URI
at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mni4e4yj5pgs

Local AT Protocol-shaped preview used to inspect the record before an exact public cache is refreshed.

{
"note": "Local AT Protocol-shaped preview. Run `make garden-refresh-atproto` to cache exact public records where available.",
"sourcePath": "content/writing/notes/2026-05-28-current-publishing-flow.md",
"uri": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.document/3mni4e4yj5pgs",
"value": {
"$type": "site.standard.document",
"title": "How I am publishing right now",
"description": "A rough map of my current local Markdown to Leaflet, Substack, and social-post workflow.",
"publishedAt": "2026-05-28",
"site": "at://did:plc:doxvahqvyhyqf32v7wz7p5xk/site.standard.publication/3mkin4i6dy22o",
"content": {
"$type": "at.markpub.markdown",
"text": "[status: rough draft]\n\nThis post is just meant to briefly document the current state of my blogging workflow.\n\nThe basic version is:\n\n- I plan to now write the majority of my posts in Markdown on my local machine (or, write in Docs/Word then convert to Markdown so I have a plaintext copy of the content).\n- I keep these Markdown files in the same source monorepo as my personal website.\n- I use a script (lightweight, mainly produced using Codex + GPT5.5. -- fairly confident this can be reproduced and modified from any coding agent quickly as needed) to sync those Markdown files to my Leaflet Data Leverage publication.\n- I use another script to produce a copy-pastable HTML version that I can paste into Substack manually.\n- I usually try to crosspost or announce the post on Twitter/X, Bluesky, and LinkedIn.\n- I am also starting to categorize posts into lanes: longer Data Leverage posts, short focus posts, short reaction posts that stay in the main Data Leverage publication, and these meta notes about writing/blogging/process.\n\nThe monorepo has five main writing lanes:\n\n- `content/writing/drafts/` for private-ish local drafts that I do not intend to publish directly.\n- `content/writing/posts/` for longer Data Leverage pieces.\n- `content/writing/reaction-posts/` for short reaction posts that should remain in the main Data Leverage publication. Each begins with a `reaction to:` source link, like a standardized quote tweet.\n- `content/writing/short-posts/` for short focus posts.\n- `content/writing/notes/` for this meta-blog / notes-on-writing track.\n\nI keep track of publication routing in `state/digital-garden/publications.json`. The shared content index at `state/digital-garden/content-index.json` connects the writing lanes to personal-site entries and scholarly references. In practice, this means the repo knows about three Leaflet destinations: the main Data Leverage publication, the focus short-posts publication, and notesonnotes. Short reactions stay in the main Data Leverage lane and are sorted separately only in the garden view. This is nice because it lets the same local Markdown-first pattern apply across multiple public surfaces without forcing every kind of writing to pretend to be the same thing.\n\nThe main loop, when I am being disciplined, is something like this:\n\n1. Write or edit a Markdown file locally.\n2. Run the local helpers that extract references, build backlinks, render HTML, and build the little garden view.\n3. Check status to see what the repo thinks is changed, publish-relevant, or stale.\n4. Dry-run the Leaflet sync.\n5. Commit and push, because the live publish path currently insists that publish-relevant files are clean and pushed.\n6. Run the live Leaflet sync.\n7. Generate the Substack paste preview if the post is also going to Substack.\n8. Manually paste into Substack, tweak anything weird, publish there.\n9. Announce the post on the social sites, and ideally record those announcements in the distribution ledger.\n\nThe social distribution step is the least automated part. Usually I want some combination of:\n\n- a Twitter/X post,\n- a Bluesky post,\n- a LinkedIn post,\n- maybe some other targeted sharing if the post is relevant to a particular community.\n\nThe repo has a `content/writing/distribution.md` ledger and helper commands for recording mirrors and announcements. The idea is that full mirrors, like Substack copies, can be marked stale if the source Markdown changes after the recorded commit, while social announcements are treated as \"non-blocking\".\n\nThe broader philosophy here is that I want the canonical version of a post to be something I can edit locally, diff, render, cite from, and move between platforms. I also want a relatively simple way to handle versioning.\n"
}
}
}
