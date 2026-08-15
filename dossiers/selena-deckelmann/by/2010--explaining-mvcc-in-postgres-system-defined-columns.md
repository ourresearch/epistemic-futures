---
title: "Explaining MVCC in Postgres: system defined columns"
person: selena-deckelmann
section: by
type: blog-post
year: 2010
date: 2010-09-01
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2010/09/01/explaining-mvcc-in-postgres-system-defined-columns/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Explaining MVCC in Postgres: system defined columns

## Full text

[](http://www.chesnok.com/daily/wp-content/uploads/2010/09/Untitled.png)

I’m playing around with some diagrams for explaining MVCC that I’ll be posting here over the next few days. Not sure if I’ll end up giving up on slides and just use a whiteboard for the talk. I made an [illustrated shared buffers](http://www.slideshare.net/selenamarie/illustrated-buffer-cache) deck to go along with Greg Smith’s excellent talk on shared buffers a while back. This is the beginning of a talk that I hope will emulate that.

Here are my first few slides, showing the system-defined columns. The next few slides will describe optimizations PostgreSQL has for managing the side effects of our pessimistic rollback strategy, and reducing IO during vacuuming and index updates.
