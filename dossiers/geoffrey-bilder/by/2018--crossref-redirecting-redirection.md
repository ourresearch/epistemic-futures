---
title: "Redirecting redirection"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2018
date: 2018-04-24
venue: "Crossref blog"
authors: "Geoffrey Bilder, Jonathan Rees, Henry Thompson"
source_url: "https://www.crossref.org/blog/redirecting-redirection/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/nyrp9-pak70. Co-authored (3 bylines)."
---

# Redirecting redirection

## Full text

**10 minute read.**

## Redirecting redirection

Crossref has decided to change the HTTP redirect code used by our DOIs from `303` back to the more commonly used `302`. Our implementation of 303 redirects back in 2010 was based on recommended best practice for supporting linked data identifiers. Unfortunately, very few other parties have adopted this practice.

What’s more, because using a 303 redirect is still unusual, it tends to throw [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization) tools into a [tizzy](http://www.dictionary.com/browse/tizzy?s=t)- and we spend a lot of time fielding SEO questions from our members about our use of 303s.

## TL;DR

At this point, we need to emphasise that we have never seen our use of 303s actually affect page rankings. But at the same time, use of 303 redirects has not had wider uptake. Maintaining this quixotic behaviour just isn’t worth the effort. We hope that, in the future, we can use other techniques (e.g. [signposting](https://signposting.org/) & [cite-as](https://datatracker.ietf.org/doc/draft-vandesompel-citeas/)) to achieve some of the things that 303 was supposed to do.

Note that these changes **will not affect users or machines using DOIs**. The change should be entirely transparent.

Below we provide some background to our decision and after that we provide some detailed technical notes from [Jonathan Rees](https://orcid.org/0000-0001-7694-8250) and [Henry Thompson](https://orcid.org/0000-0001-5490-1347) who have been very kind in helping to provide Crossref technical guidance on how we can help DOIs best support linked open data and adhere to HTTP best practice.

## Background

Back in 2010, Crossref, DataCite (and later, several other RAs) responded to [concerns that DOIs were not “linked-data friendly.”](https://doi.org/10.64000/x2spb-3d247) There were three problems with DOIs at that time:

1. It was not clear that DOIs could be used and expressed as HTTP URIs.
2. There was no standard way to ask a DOI to return a machine-readable representation of the data.
3. It wasn’t always clear if the DOI resolved to “the thing” (e.g. an article) or “something about the thing” (e.g. a landing page).

On the advice of several people in the linked data community, [we proposed some options for fixing this](https://doi.org/10.64000/8f0n4-64m15). And we finally settled on:

1. Recommending that Crossref DOIs be expressed and displayed as HTTP ([now HTTPS](https://doi.org/10.13003/5jchdy)) URIs. This made it clear that DOIs could be used with HTTP applications.
2. Enabling DOI registration agencies to support content negotiation. This allowed RAs to support providing machine-readable representations of the data associated with a DOI.
3. Changing the underlying redirect code from the normal 302 to 303. This was designed to clarify what, at the time, was true- that most DOIs resolved to a landing page, not the article itself.

By any practical measure, machine use of DOIs has exploded since we made these decisions back in 2010. Crossref’s APIs and content negotiation handle over 800 million requests for machine readable data a month. Our sibling organisation, [DataCite](https://www.datacite.org), has also seen a huge growth in machine use of DOIs. Many applications, from bibliographic management tools, to authoring systems and CRIS systems, make use of machine actionable DOIs all the time. So clearly our work to promote DOIs as machine actionable identifiers is working, but we are certain that our current use of 303 redirects has nothing to do with this growth.

First of all, as we said, very few parties have actually subscribed to the notion of using 303s to help distinguish “the thing” from “something about the thing”.

Secondly, even if they did try to rely on 303s to make this distinction, they would quickly get confused because the DOI is so often just the first in a chain of redirects which do not implement the same semantic distinction. At this point we should be clear - Crossref thinks these kinds of long redirect chains are a bad idea for two main reasons:

* They slow down resolution.
* They increase the number of potential failure points between the DOI and the item it resolves to.

But we also cannot legislate them away. They exist. And in the real world you will find plenty of DOIs that do a 303 redirect to a system that, in turn, does a 302 redirect to a system that does a 301 redirect and…eventually ends up someplace returning a 200. You get the picture. How on earth is a machine supposed to interpret a 303->302->301->302 redirect chain?

Furthermore - nowadays, after following this chain of redirects, you will often find yourself on a “page” that is *both* a landing page *and* the article itself. Dynamic, one-page applications can simply morph the one into the other without the use of additional HTTP requests.

In other words, using 303s is not helping machines interpret what the DOI is pointing at. And yet, people seem to be making good use of machine actionable DOIs and they are not complaining much about it.

Personally, I’d might have just been happy to switch back to using 302s *simply* so that I could cut down on my conversations with SEO hacks. But that wouldn’t be a principled approach. In 2010 we spent a lot of time considering the initial switch to 303s- we needed to consult with the LOD community on a potential switch back to 302s. At the January 2018 [PIDapalooza](https://pidapalooza.org/) I had a chance to talk to Henry Thomson about the 302/303 dilemma we faced, and he along with Jonathan Rees very generously provided the following feedback.

## Best practices for HTTP redirection by persistent identifier resolvers: 302 vs. 303

* Jonathan Rees (MIT CSAIL, <https://orcid.org/0000-0001-7694-8250>)
* Henry Thompson (University of Edinburgh, School of Informatics, <https://orcid.org/0000-0001-5490-1347>)

If one goes to the trouble to organize an identifier system, then the desire that such a system should last as long as possible leads one to aspirationally say it’s a *persistent* identifier (PID) system. The unwillingness of the major browser suppliers to implement new URI schemes for PIDs initially hindered their use on the Web and this in turn inhibited widespread adoption. More recently a number of PID approaches have enjoyed very rapid growth as a result of a compromise: these PIDs participate in the World Wide Web by defining simple conversion rules mapping identifiers to *actionable* (‘http:’ and/or ‘https:’) forms and providing resolution servers that redirect requests for such forms to the appropriate destination.This approach has been widely adopted and is very successful, because it is so useful. An identifier’s actionable form leads, via the HTTP protocol and one or more redirections, to a web page that bears on the ground identity of the associated entity – or perhaps even directly to the entity itself, if the system is one for document entities that are naturally provided as web pages. The nature of the retrieved web page varies from one system to the next.

A confusion arose, however, over claims in various technical specifications ([URIs](https://tools.ietf.org/html/rfc3986), [HTTP](https://tools.ietf.org/html/rfc2616), [Web Architecture](https://www.w3.org/TR/webarch/)) that the normal case is for the protocol to yield a “representation” of the “resource” “identified” by the URI. None of these terms is adequately defined by the specifications, and initially the language was not taken as normative. Those deploying identifier systems took the HTTP “resource” to be the entity associated with an identifier, and understood the “resource” as being “identified” by the URI, but it was never clear what was, or wasn’t, a “representation” of a given entity/resource: a description of the resource, the resource itself, a version of the resource, instructions on how to find the resource, etc. Sixteen years ago, in an attempt to clarify the intent of this part of the theory of URIs, and to allow applications to usefully and uniformly exploit the idea that an HTTP 200 response must deliver a “representation” of the “resource”, Tim Berners-Lee [asked](https://lists.w3.org/Archives/Public/www-tag/2002Mar/0092) the [W3C Technical Architecture Group](https://www.w3.org/2001/tag/) to consider what came to be known as the [httpRange-14](https://www.w3.org/2001/tag/group/track/issues/14) issue. It’s now 13 years after the TAG gave [advice](https://lists.w3.org/Archives/Public/www-tag/2005Jun/0039.html) which almost no one was happy with, and 5 years after work on issue [httpRedirections-57](https://www.w3.org/2001/tag/group/track/issues/57) (which superseded httpRange-14) ground to a halt. There’s still no consensus on whether it’s OK to return landing pages with a 200 status in response to requests for pictures or publications, but the Web seems to be working nonetheless, and no one seems to be bothered much anymore.

The provision of HTTP-based resolution services has stimulated widespread support for the use of identifier systems with Web resolution, particularly in the scholarly journal publication context. Those setting up HTTP resolvers responsible for identifier systems must decide which HTTP response code should be used. The TAG’s advice sows doubt on the use of the 200 response code when the response would have been a landing page, and many resolvers avoid 200 regardless and use redirection for administrative purposes, for example

‘<https://dx.doi.org/10.1109/5.771073>’ to

‘<http://ieeexplore.ieee.org/document/771073/?reload=true>’ for the DOI

‘10.1109/5.771073’, or ‘<https://identifiers.org/uniprot/A0A022YWF9>’ to

‘<http://www.uniprot.org/uniprot/A0A022YWF9>’ for the Uniprot identifier

‘A0A022YWF9’.

So the response should be a redirection, but what kind, 301, 302, or 303? (Or 307, which is almost the same as 302.) A 301 redirect seems to say that the URI is not persistent (since its target is deemed “more persistent”). A 302 redirect seems to say that the response could have come via a 200, and so suffers the same fate as 200. That leaves 303, as hinted at in the TAG’s advice. This idea got some traction: Ten years ago a Semantic Web interest group promoted the TAG’s advice in [a published note](https://www.w3.org/TR/cooluris/), and seven years ago one of us wrote a [blog post](https://odontomachus.wordpress.com/2011/05/04/crossrefs-gift-of-metadata/) giving the same advice for resolvers for PIDs in publishing.

However, not only is there neither consensus nor general utility around this strict understanding of the use of the various response codes – that is, that resolution to a landing page is inconsistent with a 200 (and *a posteriori* therefore with a 302) – but also the range of usage patterns for redirection of HTTP requests has grown and ramified over time as the Web has grown and become more complex. It’s on the face of it unlikely that a mere three response codes can capture all the resulting complexity or cover the space of outcomes (in terms of e.g. what ends up in the browser address bar or what search engines index a page under) that a page owner might like to signal.

We find in practice that some PID redirections *are* ending up (usually after further publisher-local redirects) at the “identified” document, some at landing pages, and some at one *or* the other depending on the requesting site, for example in the case of paywalled material.

In the absence of a rethinking of the whole 3xx space, it seems to us that only the 301 vs. 302 distinct ion (roughly, 301 = permanent = please fix the link, and 302 = temporary = don’t change the link) is well understood and more or less consistently treated, whereas for 303, web servers are not very consistent and both [search engine](http://sharkseo.com/nohat/303-redirects-seo/) and citation crawler behaviours are at best inconsistent and at worst downright unhelpful.

So, we believe it is in both users’ and publishers’ interests for resolvers of actionable-form PIDs to use 302 redirects, not 303.

If we want to help machines better understand the resource that a DOI points at, we have to explore using more nuanced mechanisms.

Just using 302 for the first redirect doesn’t do everything necessary to effectively support the emerging PID+redirection architecture. It’s at the *end* of the redirect chains that we need more: a standardised way to find the PID back at the start of the chain. The [‘cite-as’ proposal](https://datatracker.ietf.org/doc/draft-vandesompel-citeas/) does exactly this, and we hope it’s quickly approved and widely adopted. Once *that* happens a proposal for augmenting browser (and API) behaviour to prefer, or at least offer, the ‘cite-as’ link for bookmarking and copying will be needed.
