---
title: "Problems with dx.doi.org on January 20th 2015- what we know."
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2015
date: 2015-01-21
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/problems-with-dx.doi.org-on-january-20th-2015-what-we-know./"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/a0rsr-7xr47."
---

# Problems with dx.doi.org on January 20th 2015- what we know.

## Full text

**4 minute read.**

## Problems with dx.doi.org on January 20th 2015- what we know.

[Hell’s teeth](http://www.urbandictionary.com/define.php?term=Hells%20Teeth).

So today (January 20th, 2015) the DOI HTTP resolver at dx.doi.org started to fail intermittently around the world. The doi.org domain is managed by [CNRI](http://www.cnri.reston.va.us/) on behalf of the [International DOI Foundation](http://www.doi.org/). This means that the problem affected all DOI registration agencies including Crossref, [DataCite](https://www.datacite.org/), [mEDRA](https://www.medra.org/) etc. This also means that more popularly known end-user services like [FigShare](http://figshare.com/) and [Zenodo](https://zenodo.org/) were affected. The problem has been fixed, but the fix will take some time to propagate throughout the DNS system. You can monitor the progress here:

<https://www.whatsmydns.net/#A/doi.org>

Now for the embarrassing stuff…

At first lots of people were speculating that the problem had to do with somebody forgetting to renew the dx.doi.org domain name. Our information from CNRI was that the problem had to do with a mistaken change to a DNS record and that the domain name wasn’t the issue. We corrected people who were reporting that domain name renewal as the cause, but eventually we learned that it was actually true. We have had it confirmed that the problem originated with CNRI manually renewing the domain name at the last minute. Ugh. CNRI will issue a statement soon. We’ll link to it as soon as they do. UPDATE (Jan 21st): CNRI has sent Crossref a statement. They do not have it on their site yet, so we have can included it [below](#cnri).

In the mean time, if you are having trouble resolving DOIs, a neat trick to know is that you can do so using the Handle system directly. For example:

<http://hdl.handle.net/10.5555/12345678>

Crossref will, of course, also analyse what occurred, and issue a public report as well. Obviously, this report will include an analysis of how the outage effected DOI referrals to our members.

The amazingly cool thing is that everybody online has been very supportive and has helped us to diagnose the problem. Some have even said that the event underscores a point we often make about so-called “persistent-identifiers”- which is that they are not magic technology; the “persistence” is the result of a social contract. We like to say that Crossref DOIs are as persistent as Crossref staff. Well, to that phrase we have to add “and IDF staff” and “CNRI staff” and “ICANN staff”. It is [turtles all the way down](http://en.wikipedia.org/wiki/Turtles_all_the_way_down).

We don’t want to dismiss this event as an inevitable consequence of interdependent systems.And we don’t want to pass the buck. We need to learn something practical from this. How can we guard against this type of problem in the future? Again, people following this issue on Twitter have already been helping with suggestions and ideas. Can we crowd-source the monitoring of persistent identifier SLAs? Could we leverage Wikipedia, Wikidata or something similar to monitor critical identifiers and other infrastructure like purls, DOIs, handles, PMIDs, perma.cc, etc? Should we be looking at designating special exceptions to the normal rules governing DNS names? Do we need to distribute the risk more? Or is it enough *cough* to simply ensure that somebody, somewhere in the dependency chain had enabled DNS protection and auto-renewal for critical infrastructure DNS names?

Truly, we are humbled. For all the redundancy built into our systems (multiple servers, multiple hosting sites, Raid drives, redundant power), we were undone by a simple administrative task. Crossref, IDF and CNRI- we all feel [a bit crap](http://www.urbandictionary.com/define.php?term=a%20bit%20crap). But we’ll get back. We’ll fix things. And we’ll let you know how we do it.

We will update this space as we know more. We will also keep people updated on twitter on @CrossrefNews. And we will report back in detail as soon as we can.

---

### CNRI Statement

`"The doi.org domain name was inadvertently allowed to expire for a brief period this morning (Jan 20). It was reinstated shortly after 9am this morning as soon as the relevant CNRI employee learned of it. A reminder email sent earlier this month to renew the registration was apparently missed. We sincerely apologize for any difficulties this may have caused. The domain name has since been placed on automatic renewal, which should prevent any repeat of this event."`
