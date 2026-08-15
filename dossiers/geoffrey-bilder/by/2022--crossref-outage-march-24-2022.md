---
title: "Outage of March 24, 2022"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2022
date: 2022-03-24
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/outage-of-march-24-2022/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/q39ba-n3564."
---

# Outage of March 24, 2022

## Full text

**2 minute read.**

## Outage of March 24, 2022

So here I am, apologizing again. Have I mentioned that I hate computers?

We had [a large data center outage](https://status.crossref.org/incidents/gwxd1yqdw304). It lasted 17 hours. It meant that pretty much all Crossref services were unavailable - our main website, our content registration system, our reports, our APIs. 17 hours was a long time for us - but it was also an inconvenient time for numerous members, service providers, integrators, and users. We apologise for this.

Like the [outage last October](https://doi.org/10.64000/sen6x-c2c16), the issue was related to the data center that we are trying to leave. However, unlike last time, our single nearby network admin wasn’t in surgery at the time. Tim was alerted in the early hours of his morning and was able get up and immediately investigate.

Despite having both secondary and tertiary backup connections, neither activated appropriately.

The problem was with incomplete BGP (Border Gateway Protocol) settings on our primary connection’s network provider’s side. We never noticed this because our backup connection had the correct and complete BGP settings. But our backup circuit went down (we don’t know why yet), and when the router with complete settings went down, only the router with the incomplete settings was available and so everything went down.

We hadn’t yet fully configured the tertiary connection to cut over automatically. This meant cutting over to the tertiary during the outage would have required manual and potentially error-prone reconfiguration. Not something we wanted to do in a hurry with a sleep-deprived network admin.

It’s not an excuse at all. But we are currently down two people in our infrastructure group. One of our infrastructure staff recently left for a startup, and we are already hiring a new third position. In short, our one-long-suffering sysadmin had to field this all by himself. But hey - [we are hiring a Head of Infrastructure](/jobs/2022-03-15-head-of-infrastructure/), and if you are interested you can now see the work you’d have cut out for you!

So things are back up and we’ve resolved the incident but we are carefully and cautiously monitoring. We will further analyze what went wrong and post an update when we have a clearer picture.

I apologize for the downstream pain this outage will have inevitably caused. We realize that many people will now be scrambling to clean things up after this lengthy outage.

More when I have it… but for now I’ll mostly be curled up in a ball.
