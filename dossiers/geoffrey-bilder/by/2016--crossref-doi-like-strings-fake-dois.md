---
title: "DOI-like strings and fake DOIs"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2016
date: 2016-06-29
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/doi-like-strings-and-fake-dois/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/8mj8h-2t809."
---

# DOI-like strings and fake DOIs

## Full text

**7 minute read.**

## DOI-like strings and fake DOIs

## TL;DR

Crossref discourages our members from using DOI-like strings or fake DOIs.

## Details

Recently we have seen quite [a bit of debate](https://go-to-hellman.blogspot.co.uk/2016/06/wileys-fake-journal-of-constructive.html) around the use of so-called “fake-DOIs.” We have also been quoted as saying that we discourage the use of “fake DOIs” or “DOI-like strings”. This post outlines some of the cases in which we’ve seen fake DOIs used and why we recommend against doing so.

## Using DOI-like strings as internal identifiers

Some of our members use DOI-like strings as internal identifiers for their manuscript tracking systems. These only get registered as real DOIs with Crossref once an article is published. This seems relatively harmless, except that, frequently, the unregistered DOI-like strings for unpublished (e.g. under review or rejected manuscripts) content ‘escape’ into the public as well. People attempting to use these DOI-like strings get understandably confused and angry when they don’t resolve or otherwise work as DOIs. After years of experiencing the frustration that these DOI-like things cause, we have taken to recommending that our members not use DOI-like strings as their internal identifiers.

### Using DOI-like strings in access control compliance applications

We’ve also had members use DOI-like strings as the basis for systems that they use to detect and block tools designed to bypass the member’s access control system and bulk-download content. The methods employed by our members have fallen into two broad categories:

* Spider (or robot) traps.
* Proxy bait.

### Spider traps

A “[spider trap](https://en.wikipedia.org/wiki/Spider_trap)” is essentially a tripwire that allows a site owner to detect when a spider/robot is crawling their site to download content. The technique involves embedding a special trigger URL in a public page on a web site. The URL is embedded such that a normal user should not be able see it or follow it, but an automated bot (aka “spider”) will detect it and follow it. The theory is that when one of these trap URLs is followed, the website owner can then conclude that the ip address from which it was followed harbours a bot and take action. Usually the action is to inform the organisation from which the bot is connecting and to ask them to block it. But sometimes triggering a spider trap has resulted in the IP address associated with it being instantly cut off. This, in turn, can affect an entire university’s access to said member’s content.

When a spider/bot trap includes a DOI-like string, then we have seen some particularly pernicious problems as they can trip-up legitimate tools and activities as well. For example, a bibliographic management browser plugin might automatically extract DOIs and retrieve metadata on pages visited by a researcher. If the plugin were to pick up one of these spider traps DOI-like strings, it might inadvertently trigger the researcher being blocked- or worse- the researcher’s entire university being blocked. In the past, this has even been a problem for Crossref itself. We periodically run tools to test DOI resolution and to ensure that our members are properly displaying DOIs, Crossmarks, and metadata as per their member obligations. We’ve occasionally been blocked when we ran across the spider traps as well.

### Proxy bait

Using proxy bait is similar to using a spider trap, but it has an important difference. It does not involve embedding specially crafted DOI like strings on the member’s website itself. The DOI-like strings are instead fed directly to tools designed to subvert the member’s access control systems. These tools, in turn, use proxies on a subscriber’s network to retrieve the “bait” DOI-like string. When the member sees one of these special DOI-like strings being requested from a particular institution, they then know that said institution’s network harbours a proxy. In theory this technique never exposes the DOI-like strings to the public and automated tools should not be able to stumble upon them. However, recently one of our members had some of these DOI-like strings “escape” into the public and at least one of them was indexed by Google. The problem was compounded because people clicking on these DOI-like strings sometimes ended having their university’s IP address banned from the member’s web site. As you can imagine, there has been a lot of gnashing of teeth. We are convinced, in this case, that the member was doing their best to make sure the DOI-like strings never entered the public. But they did nonetheless. We think this just underscores how hard it is to ensure DOI-like strings remain private and why we recommend our members not use them.

## Pedantry and terminology

Notice that we have not used the phrase “fake DOI” yet. This is because, internally, at least, we have distinguished between “DOI-like strings” and “fake DOIs.” The terminology might be daft, but it is what we’ve used in the past and some of our members at least will be familiar with it. We don’t expect anybody outside of Crossref to know this.

To us, the following is not a DOI:

10.5454/JPSv1i220161014

It is simply a string of alphanumeric characters that copy the DOI syntax. We call them “DOI-like strings.” It is not registered with any DOI registration agency and one cannot lookup metadata for it. If you try to “resolve” it, you will simply get an error. Here, you can try it. Don’t worry- clicking on it will not disable access for your university.

<http://doi.org/10.5454/JPSv1i220161014>

The following is what we have sometimes called a “fake DOI”

10.5555/12345678

It is registered with Crossref, resolves to a fake article in a fake journal called The Journal of Psychoceramics (the study of Cracked Pots) run by a fictitious author (Josiah Carberry) who has a fake ORCID (<http://orcid.org/0000-0002-1825-0097>) but who is affiliated with a real university ([Brown University](http://www.brown.edu)).

Again, you can try it.

<http://doi.org/10.5555/12345678>

And you can even look up metadata for it.

<https://api.crossref.org/v1/works/10.5555/12345678>

Our dirty little secret is that this “fake DOI” was registered and is controlled by Crossref.

Why does this exist? Aren’t we subverting the scholarly record? Isn’t this awful? Aren’t we at the very least hypocrites? And how does a real university feel about having this fake author and journal associated with them?

Well- the DOI is using a prefix that we use for testing. It follows a long tradition of test identifiers starting with “5”. [Fake phone numbers in the US start with “555”](https://en.wikipedia.org/wiki/555_(telephone_number)). Many credit card companies [reserve fake numbers starting with “5”](https://web.archive.org/web/20160707151357/https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm). For example, Mastercard’s are “5555555555554444” and “5105105105105100.”

We have created this fake DOI, the fake journal and the fake ORCID so that we can test our systems and demonstrate interoperable features and tools. The fake author, Josiah Carberry, is [a long-running joke at Brown University](http://library.brown.edu/hay/carberry.php). He even has a [Wikipedia entry](https://en.wikipedia.org/wiki/Josiah_S._Carberry). There are also a lot of other DOIs under the test prefix “5555.”

We acknowledge that the term “fake DOI” might not be the best in this case- but it is a term we’ve used internally at least and it is worth distinguishing it from the case of DOI-like strings mentioned above.

But back to the important stuff….

As far as we know, none of our members has ever registered a “fake DOI” (as defined above) in order to detect and prevent the circumvention of their access control systems. If they had, we would consider it much more serious than the mere creation of DOI-like strings. The information associated with registered DOIs becomes part of the persistent scholarly citation record. Many, many third party systems and tools make use of our API and metadata including bibliographic management tools, [TDM](https://en.wikipedia.org/wiki/Text_mining) tools, [CRIS](https://en.wikipedia.org/wiki/Current_research_information_system) systems, [altmetrics](https://en.wikipedia.org/wiki/Altmetrics) services, etc. It would be a very bad thing if people started to worry that the legitimate use of registered DOIs could inadvertently block them from accessing content. Crossref DOIs are designed to encourage discovery and access- not block it.

And again, we have absolutely no evidence that any of our members has registered fake DOIs.

But just in case, we will continue to discourage our members from using DOI-like strings and/or registering fake DOIs.

This has been a public service announcement from the identifier dweebs at Crossref.

## Image Credits

Unless otherwise noted, included images purchased from [The Noun Project](https://thenounproject.com/)
