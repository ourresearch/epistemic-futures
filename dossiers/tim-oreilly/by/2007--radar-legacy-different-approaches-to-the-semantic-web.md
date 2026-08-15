---
title: "Different Approaches to the Semantic Web"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-03-12
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/03/different_appro_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Different Approaches to the Semantic Web

## Full text

I've been thinking a bit more about why [I'm more excited about Metaweb](http://radar.oreilly.com/archives/2007/03/freebase_will_p_1.html)'s [freebase](http://www.freebase.com) than I have been about previous Semantic Web projects that I've been exposed to.

I think that part of it is the difference in how they capture data about relationships. A good example is [Semantic MediaWiki](http://en.wikipedia.org/wiki/Semantic_MediaWiki), which Stefano Mazzocchi pointed me to. They capture relations in a very explicit way, in this case, using structured wikitext. For example, as the wikipedia page on Semantic MediaWiki explains, an entry about Berlin might include the wikitext:
    
    
     ... the population is [[population:=3,993,933]]

resulting in the output text "the population is 3,993,933" and the hidden semantic tuple "'Berlin' 'has population' '3993933'".

It seems easy enough, but why hasn't this approach taken off? Because there's no immediate benefit to the user. He or she has to be committed to the goal of building hidden structure into the data. It's an extra task, undertaken for the benefit of others. And as I've written before, one of the secrets of success in Web 2.0 is to harness self-interest, not volunteerism, in a natural "[architecture of participation](http://www.oreillynet.com/pub/a/oreilly/tim/articles/architecture_of_participation.html)."

By contrast, in freebase, an entry about Germany would show an explicit form intended to capture critical statistics about a location. What's so clever is that by articulating the types as a separate structure from the data, and having instances inherit that structure when they are created, users don't think they are providing metadata -- they think they are just providing data.

Because anyone creating a new instance is prompted to fill out the data in a structured way, that it doesn't seem like an extra task, but rather that the software is being helpful. Any data field can be left blank, but it can also easily be updated by anyone else who cares to do so. And in fact, applications that don't explicitly present themselves as Semantic Web applications, like the Web 2.0 family tree maker, [Geni](http://www.geni.com), work exactly the same way. The user is given an opportunity to create a very structured entry that doesn't feel like a chore but just the natural way to perform the task.

And these applications are fairly addictive. Go try Geni, and I bet that before long, you've got your whole family at work on it. (I do.) Similarly, once freebase is open to the public, everyone will be busily constructing entries on themselves, their businesses, their products -- all the commercial activity that is explicitly banned from wikipedia. (Freebase's supersetting of wikipedia is very clever in this way. If you've got a wikipedia entry, it's included. But if not, you get to write about yourself.)

That being said, one of the other sites that Stefano pointed me to, [dbpedia](http://dbpedia.org/docs/), shows what is ultimately perhaps an even more powerful tool, namely extracting implicit structure from data already out there on the web where it can be found. 

This was the vision of a company called [Invisible Worlds](http://www.google.com/search?q=Invisible+Worlds+Malamud+Rose), founded by Carl Malamud and Marshall Rose before the dotcom bust. (I was on the board.) Carl and Marshall realized that there were many types of semi-structured data out on the web -- e.g. the Edgar database of the SEC -- and that it was possible to extract that structure and make it more accessible. 

This is what dbpedia is doing with Wikipedia, and what Adrian Holovaty is doing with [Chicagocrime.org](http://www.chicagocrime.org), but it's also what Google is doing with PageRank.

This is the true Web 2.0 way: don't ask users to provide structure, unless it's useful to them. But do design your applications in such a way that structure is generated without extra effort on the user's part. And mine structure that already exists, even if it's messy and inefficient.

Consider one of my favorite examples, the still to-be-built Web 2.0 address book. A formal Semantic Web approach might say: "Users should create [FOAF](http://www.foaf-project.org/) files, expressing their social network." But the fact that I have someone in my address book already expresses a relation! And all the data that _could_ be collected (as Google collects and analyzes web data) expresses even more detail. How often do I contact this person? by phone? by email? by IM? by SMS? How quickly do a respond? What topics do I tend to share with which of my correspondents? All of these heuristics, properly collected, would provide a far more powerful "friend of a friend" network than anything built explicitly with FOAF. (The first big communications company -- email, phone, or IM -- that does this right will have a killer app!)

We might call this the "small s semantic web" by contrast with the formal Semantic Web.

Now it may be that FOAF will be the right mechanism for expressing the data that my imagined Google-style peoplefinder collects, but I tend to doubt it. PageRank and all the other factors that Google uses probably could be expressed using Semantic Web style syntax, but I somehow doubt that they are.

The semantic web is definitely coming. But it's coming through different mechanisms, I think, than the Semantic Web pioneers imagined.
