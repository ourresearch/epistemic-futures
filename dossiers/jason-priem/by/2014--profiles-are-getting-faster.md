---
title: "Profiles are getting faster"
person: jason-priem
section: by
type: blog-post
year: 2014
date: 2014-01-14
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/profiles-are-getting-faster/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Profiles are getting faster

## Full text

\
Our mantra here is to ship features quickly and optimize ’em later. And after spending a lot of frustrated time waiting for profiles to load (especially very large profiles), we decided it was officially “later” and set out to improve profile loading times last week.

We ended up moving a lot of the rendering code from Javascript to Python, where it’s both faster and more maintainable, and doing some caching. The result: profiles like [Heather’s](http://impactstory.org/HeatherPiwowar) are now loading around five seconds faster; bigger profiles will see even larger improvements. The difference is especially pronounced when you switch back and forth between viewing the profile and zooming in to individual products: the return trip is now almost instant, which we’re really happy about.

There’s still a lot of room to improve loading times, especially on the first profile load, but we’re going to wait on this for now, at least until we get [feedback](http://feedback.impactstory.org) requesting faster loads. That means we’ll be able to turn our attention to shipping new features…we’ve got some coming up next week we can’t wait to show y’all!
