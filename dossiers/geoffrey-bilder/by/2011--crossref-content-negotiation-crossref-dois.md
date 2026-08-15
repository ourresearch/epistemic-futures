---
title: "Content Negotiation for Crossref DOIs"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2011
date: 2011-04-19
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/content-negotiation-for-crossref-dois/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/bj8hs-6m856."
---

# Content Negotiation for Crossref DOIs

## Full text

**2 minute read.**

## Content Negotiation for Crossref DOIs

So does anybody remember the posting [DOIs and Linked Data: Some Concrete Proposals](/blog/dois-and-linked-data-some-concrete-proposals/)?

Well, we went with option “D.”

From now on, DOIs, *expressed as [HTTP URI](http://en.wikipedia.org/wiki/Uniform_Resource_Identifier)s*, can be used with [content-negotiation](http://en.wikipedia.org/wiki/Content_negotiation).

Let’s get straight to the point. If you have [curl](http://curl.haxx.se/) installed, you can start playing with content-negotiation and Crossref DOIs right away:

> curl -D - -L -H   “Accept: application/rdf+xml” “`http://dx.doi.org/10.1126/science.1157784`” 
>
> curl -D - -L -H   “Accept: text/turtle” “`http://dx.doi.org/10.1126/science.1157784`”
>
> curl -D - -L -H   “Accept: application/atom+xml” “`http://dx.doi.org/10.1126/science.1157784`”

Or if you are already using Crossref’s “[unixref](https://www.crossref.org/schema/unixref1.1.xsd)” format:

> curl -D - -L -H “Accept: application/unixref+xml” “`http://dx.doi.org/10.1126/science.1157784&`#8221; 

This will work with over 46 million Crossref DOIs as of today, but the beauty of the setup is that from now on, any [DOI registration agency](http://www.doi.org/registration_agencies.html) can enable content negotiation for their constituencies as well. [DataCite](http://datacite.org/)- we’re looking at you 😉 .

It also means that, as registration agency members (Crossref publishers, for instance) start providing more complete and richer representations of their content, we can simply redirect content-negotiated requests directly to them.

We expect that that this development will round-out Crossref’s efforts to support standard APIs including [OpenURL](https://support.crossref.org/hc/en-us/articles/214880143) and [OAI\_PMH](https://support.crossref.org/hc/en-us/articles/213679866) and we look forward to seeing DOIs increasingly used in [linked data](http://en.wikipedia.org/wiki/Linked_Data) applications.

Finally, Crossref would just like to thank the [IDF](http://www.doi.org/foundation/bios.html) and [CNRI](http://www.cnri.reston.va.us/) for their hard work on this as well as [Tony Hammond](http://www.linkedin.com/in/tonyhammond) and [Leigh Dodds](http://www.ldodds.com/) for their valuable advice and persistent goading.
