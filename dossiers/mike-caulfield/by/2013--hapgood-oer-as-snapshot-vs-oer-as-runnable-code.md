---
title: "OER as Snapshot vs. OER as \u201cRunnable Code\u201d"
person: mike-caulfield
section: by
type: blog-post
year: 2013
date: 2013-04-08
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2013/04/08/oer-as-snapshot-vs-oer-as-runnable-code/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# OER as Snapshot vs. OER as “Runnable Code”

## Full text

Today I was reading Pamela Fox’s blog post about discussions inside Coursera on [whether they want to open up their code](<http://blog.pamelafox.org/2013/03/source-snapshots.html>). It’s a thoughtful treatment of the subject, and contains I think a nice discussion of some of the hidden costs of going the open source route. It’s great to see engineers at Coursera thinking about this (see, I am not the anti-Coursera ravebot you all thought I was! I can be nice when I see good things! Show me good things!)

What Pamela ends up on is a desirable compromise — a halfway point between open and closed she calls the “source snapshot” approach:

> A “snapshot” is a dump of some part of our codebase, taken at a point in time and copied into a public repository. It may be an incomplete dump (missing dependencies or server-side, e.g.), it would not necessarily be runnable, and it would have no guarantees of being up-to-date or ever being updated in the future.

What’s fascinating is to think of these two models — open-sourcing and snapshotting — in terms of OER, and in particular OCW. Read that paragraph again, and you’ll realize that “Source Snapshot” defines what OpenCourseWare has largely been in the past. Materials from a course (but not all the materials), not runnable out of the box, with no expectation of updates or upkeep.

As Pamela points out, this is a good intermediate step:

> The snapshot would still be useful, for developers looking to see how we approached some aspect in the codebase, and also for us to refer to in talks and blog posts. It would also be a way for us to dip our toes into the open source waters, and to see what developers are most interested in. If a particular snapshot got a lot of attention, then maybe one day, when we felt we had the resources, we would turn it into an actual living open-source library and spend the time needed to nurture that community.

And again, we see the parallel here, where most _**institutional**_ reuse of OCW ends up influencing approach to course design without being directly reused. To get reuse, however, you need to go the extra mile.

We’ve talked about this before, of course. There’s this ancient post of mine on [Openess as Reuse vs. Openness as Transparency](<http://web.archive.org/web/20090413031817/http://mikecaulfield.com/2009/01/25/openness-as-reuse-and-openness-as-transparency/>), and Stian Haklev’s [amazing dissertation](<http://reganmian.net/top-level-courses/Haklev_Stian_201009_MA_thesis.pdf>) on the history and context of OCW in China makes an expanded version of this distinction central to its analysis (see the “Typology” on page seven for starters). Others have made similar distinctions.

But it’s useful, I think, to see it through this slightly different lens of “snapshots” vs. “open source”. To paraphrase Chris Kelty, an anthropologist of the Open Source community, such analogies are “[good to think with](<http://news.rice.edu/2008/07/10/the-way-i-see-it-burn-my-book-and-rip-and-mix-it-tooadding-your-two-cents-to-two-bits/>)” in that they provide new angles on old questions.

In this case, what the analogy allows us to ask is this: If we see open-source as a continuum from “source snapshot” to ‘true’ open source, what elements would we need to move from Point A to Point B?

This view sees transparency and reuse not as two seperate concerns, but as potential stages of a project’s development. That’s problematic but it’s also liberating, because the minute we see “OCW as open source” as built on top of “OCW as snapshot”, we see much of what makes the difference in software would also make the difference in OCW. To move OCW beyond the snapshot phase OCW would need to be:

  * More runnable. It should be usable, not just viewable. Real repurposable content shipped for immediate use in whatever wrapper (LMS, WordPress, EdX) it runs natively in. No more PDFs. No more quizzes as documents.
  * Dependency-free. It should contain everything it needs to run. No copyright redactions, no references to textbooks not included, no mentions of class activities that aren’t provided in the materials.
  * Community-supported. It would need a community around it, and a conscious (and funded!) effort by the original developer or developing institution to nurture that community through its initial stages.
  * Maintained and updated. It should have a community or institution that commits to the ongoing pruning and extension that such projects require so that they do not become empty husks of linkrot. (See [Dave Cormier’s post](<http://davecormier.com/edblog/2013/04/01/moocs-to-cultivate-networked-textbooks/>) for how that might work).

I think we’re getting there, slowly. But it’s hard, and the transition from “source snapshot” to “open source” is more resource intensive than many realize. Thinking about it in these terms helps us explain _why_ it is resource intensive, and under what circumstances that use of resources might be warranted. Again, not a perfect lens and not the only lens on this (not nearly), but one that I am finding useful at the moment.
