---
title: "follow along as we rearchitect"
person: jason-priem
section: by
type: blog-post
year: 2012
date: 2012-03-29
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/20121763408/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# follow along as we rearchitect

## Full text

\

Total-impact has outgrown its baby teeth: we are rearchitecting the codebase.  The goal is a robust and scaleable framework that will take us through the next phase of rapid growth.

The new codebase will have a clean api, a webapp that uses the api directly, data storage at the item level, a history of metric values over time, and queues to facilitate timeliness and scalability.  It is being built from the ground up with good logging, error-handling, and documentation… aspects that aren’t always at the top of the hackathon agenda 🙂

The new codebase is written in Python rather than PHP.  This change wasn’t taken lightly: changing programming languages is a Classic Blunder after all.  That said, others have done it successfully, and Python appears to be [the favourite programming language at Hacker News](http://news.ycombinator.com/item?id=3746692), so we’re confident it is the right move.

Without further ado, here are [the new code repositories](https://github.com/total-impact) at GitHub.  Works in progress… stay tuned!
