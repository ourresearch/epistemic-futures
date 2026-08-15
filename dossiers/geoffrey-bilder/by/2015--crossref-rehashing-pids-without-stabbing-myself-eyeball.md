---
title: "Rehashing PIDs without stabbing myself in the eyeball"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2015
date: 2015-06-11
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/rehashing-pids-without-stabbing-myself-in-the-eyeball/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/42phf-m2534."
---

# Rehashing PIDs without stabbing myself in the eyeball

## Full text

**4 minute read.**

## Rehashing PIDs without stabbing myself in the eyeball

Anybody who knows me or reads this blog is probably aware that I don’t exactly [hold back](/blog/dois-unambiguously-and-persistently-identify-published-trustworthy-citable-online-scholarly-literature-right/) when discussing [problems](/blog/january-2015-doi-outage-followup-report) with the DOI system. But just occasionally I find myself actually defending the thing…

About once a year somebody suggests that we could replace existing persistent citation identifiers (e.g. DOIs) with some new technology that would fix some of the weaknesses of the current systems. Usually said person is unhappy that current systems like

[DOI](http://www.doi.org), [Handle](http://www.handle.net), [Ark](http://en.wikipedia.org/wiki/Archival_Resource_Key), [perma.cc](http://perma.cc), etc. depend largely on a social element to update the pointers between the identifier and the current location of the resource being identified. It just seems manifestly old-fashioned and ridiculous that we should still depend on [bags of meat](http://tvtropes.org/pmwiki/pmwiki.php/Main/CallAHumanAMeatbag) to keep our digital linking infrastructure from falling apart.

In the past, [I’ve threatened to stab myself in the eyeball](https://web.archive.org/web/20170811141334/http://blogs.plos.org/mfenner/2009/02/17/interview_with_geoffrey_bilder/) if I was forced to have the discussion again. But the dirty little secret is that I play this game myself sometimes. After all, [the best thing a mission-driven membership organisation could do for its members would be to fulfil its mission and put itself out of business](http://cameronneylon.net/blog/principles-for-open-scholarly-infrastructures/). If we could come up with a technical fix that didn’t require the social component, it would save our members a lot of money and effort.

When one of these ideas is posed, there is a brief flurry of activity as another generation goes through the same thought processes and (so far) comes to the same conclusions.

The proposals I’ve seen generally fall into one of the following groups:

* Replace persistent identifiers (PIDs) with [hashes](http://en.wikipedia.org/wiki/Hash_function), [checksums](http://en.wikipedia.org/wiki/Checksum), etc.
* Just use search (often, but not always coupled with 1 above)
* Automagically create PIDs out of metadata.
* Automagically redirect broken citations to archived versions of the content identified
* And more recently… use the [blockchain](http://en.wikipedia.org/wiki/Blockchain)

I thought it might help advance the discussion and avoid a bunch of dead ends if I summarised (rehashed?) some of the issues that should be considered when exploring these options.

Warning: Refers to [FRBR](http://en.wikipedia.org/wiki/Functional_Requirements_for_Bibliographic_Records) terminology. Those of a sensitive disposition might want to turn away now.

* DOIs, PMIDs, etc. and other persistent identifiers are primarily used by our community as “citation identifiers”. We generally cite at the “expression” level.
* Consider the difference between how a “citation identifier” a “work identifier” and a “content verification identifier” might function.
* How do you deal with “equivalent manifestations” of the same expression. For example the ePub, PDF and HTML representations of the same article are intellectually equivalent and interchangeable when citing. The same applies to csv & tsv representations of the same dataset. So, for example, how do hashes work here as a citation identifier?
* Content can be changed in ways that typically doesn’t effect the interpretation or crediting of the work. For example, by reformatting, correcting spelling, etc. In these cases the copies should share the same citation identifier, but the hashes will be different.
* Content that is virtually identical (and shares the same hash) might be republished in different venues (e.g. a normal issue and a thematic issue). Context in citation is important. How do you point somebody at the copy in the correct context?
* Some copies of an article or dataset are stewarded by publishers. That is, if there is an update, errata, corrigenda, retraction/withdrawal, they can reflect that on the stewarded copy, not on copies they don’t host or control. Location is, in fact, important here.
* Some copies of content will be nearly identical, but will differ in ways that would affect the interpretation and/or crediting of the work. A corrected number in a table for example. How would you create a citation form a search that would differentiate the correct version from the incorrect version?
* Some content might be restricted, private or under embargo. For example private patient data, sensitive data about archaeological finds or the migratory patterns of endangered animals.
* Some content is behind paywalls (cue jeremiads)
* Content is increasingly composed of static and dynamic elements. How do you identify the parts that can be hashed?
* How do you create an identifier out of metadata and not have them look like [this](http://en.wikipedia.org/wiki/Serial_Item_and_Contribution_Identifier)?

This list is a starting point that should allow people to avoid a lot of blind alleys.

In the mean time, good luck to those seeking alternatives to the current crop of persistent citation identifier systems. I’m not convinced it is possible to replace them, but if it is- I hope I beat you to it. 🙂 And I hope I can avoid stabbing myself in the eye.
