---
title: "Everyday Postgres: Describing an “ideal” Postgres Operational Environment"
person: selena-deckelmann
section: by
type: blog-post
year: 2014
date: 2014-01-30
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2014/01/30/everyday-postgres-describing-an-ideal-postgres-operational-environment/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Everyday Postgres: Describing an “ideal” Postgres Operational Environment

## Full text

I spent some time thinking about what things in the [Postgres](http://postgresql.org) environment (and specifically for [crash-stats.mozilla.com](http://crash-stats.mozilla.com)) make me happy, and which things bother me so much that I feel like something is pretty wrong until they are fixed or monitored.

[Here’s what I came up with](https://gist.github.com/selenamarie/8724731):

I’m planning to go through each of these items and talk about how we address them in the Web Engineering team, and that will include implementing some new things over the next couple of quarters that we haven’t had in the past.

One thing that didn’t surprise me about this list was how much documentation is needed to keep environments running smoothly. By smoothly, I mean that other people on the team can jump in and fix things, not just a single domain expert.

Sometimes docs come in the form of scripts or code. However, some prose and explanation of the thinking behind the way things works is often also necessary. I frequently underestimate how much domain knowledge I have that I really aught to be sharing for the sake of my team.
