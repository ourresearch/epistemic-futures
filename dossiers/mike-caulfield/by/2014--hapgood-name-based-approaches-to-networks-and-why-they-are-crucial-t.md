---
title: "Name-Based Approaches to Networks, and Why They are Crucial to the Personal Web"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-06-19
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/06/19/name-based-approaches-to-networks-and-why-they-are-crucial-to-the-personal-web/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Name-Based Approaches to Networks, and Why They are Crucial to the Personal Web

## Full text

Alan Levine made a great comment on a previous post — the frustration in Smallest Federated Wiki is that “you never know where you are.”

This got me thinking about some foundational issues that need to be explained — issues bigger than any directed how-to. One of the reasons people feel lost on SFW is that 20 years of web browsing has taught us to think about the web in terms of “location” instead of “name”.

If we ask someone to get a book for us, there’s a couple ways we can do that. The first way is to specify by location: “Get me the book on the third floor of the library, first bookcase, 5th shelf down, three books from the right.”

This is roughly how the internet works. An address is in fact a location.

And that makes sense in a standard scenario:

  * Our library is always open
  * Books don’t change places
  * There is really only one library in which you can find each book you want

And if you look at that, that’s ARPANET circa 1970. Always-on, immobile server machines . A situation where most content was stored only a small number of places.

If you think about libraries though, they don’t define books by location. They define books by ID. You know that books are defined by ID and not location because the Library of Congress ID number you get when you look up a book in your library is the same number that is stamped on copies of that book all around the world. You don’t look up a book in a catalog and find an ID that says “second-shelf-two-books-in”. You get something like “G2207.P4C76 G7 1995”.

And so your path is different. You hand that number to the librarian. She says, nope, that books not in, but let’s check Interlibrary Loan.

This is useful, because the book exists in various locations, and the book at each location is intermittently available. If we were to build a system where books were identified by their location, the system would break every time a book was unavailable or the library was reorganized.

This situation — a series of intermittently available resources widely duplicated across a network — is much closer to the reality of the web in 2014 than the first model. Yet we hold on to the location-based model. And what that does is ensure that that the parts of the web that don’t look like 1970 — us, our laptops, our phones, our personal servers — can’t be full members of the web, because in a location-based system, transience is the cardinal sin.

Smallest Federated Wiki works the second way. Your link is to named content. Your system searches your trusted network for that named content — first looking on your starting context (site you started from), but then looking other places as needed. This means that very un-1970-like things can happen, such as the following:

  * I run a server on my laptop, post an article to an SFW site on my laptop.
  * Tim Owens comes by on his laptop, running his personal server, and writes an article that links to mine (on my laptop)
  * Amy Collier sees my article and forks it to her site on her laptop
  * I shutdown my laptop, my SFW site is no longer available for the day.

OK, so far, so good. But here’s where the magic happens.

  * Jim Groom comes to Tim’s page and clicks the link to mine.
  * I’m not online, so, assuming Amy is in his neighborhood, the link transparently pulls up Amy’s version of the page.

Notice that none of this required coordination. When Tim linked to my page, Amy’s copy didn’t even exist. Amy might not even be in Tim’s neighborhood. He might not even know Amy exists. Yet here Jim is arriving at Amy’s page via a link that Tim wrote.

This is only one example of the benefits of named content systems, but hopefully it sufficient to show that it opens up an array of possibilities just not possible before.

Does that reduce the compelling need to know “who the heck’s server is this?” on SFW? Not completely. After all, the content IDs used by SFW can point to radically different content. Authorship matters. And I’ll demonstrate some ways to deal with such things later. But it seemed impossible to do the “how-tos” without dealing with at least some of the “why-fors” up front.
