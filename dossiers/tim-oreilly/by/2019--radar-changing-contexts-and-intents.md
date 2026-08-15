---
title: "Changing contexts and intents"
person: tim-oreilly
section: by
type: blog-post
year: 2019
date: 2019-03-13
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/changing-contexts-and-intents/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Changing contexts and intents

## Full text

Every day, someone comes up with a new use for old data. Recently, IBM scraped a million photos from Flickr and turned them into a training data set for [an AI project intending to reduce bias in facial recognition](<https://www.ibm.com/blogs/research/2019/01/diversity-in-faces/>). That’s a noble goal, promoted to researchers as an opportunity to make more ethical AI.

Yet, the project raises numerous ethical questions of its own. Photographers and subjects weren’t asked if their photos could be included; while the photos are all covered by a Creative Commons non-commercial license, one of the photographers quoted in [an NBC article about the project](<https://www.nbcnews.com/tech/internet/facial-recognition-s-dirty-little-secret-millions-online-photos-scraped-n981921>) asks by what rationale anything IBM does with his photographs can be considered “non-commercial.” It’s almost impossible to get your photographs removed from the database; it’s possible in principle, but IBM requires you to have the URL of the original photograph—which means you have to know which photographs were included in the first place. (NBC provides a tool to check whether your photos are in the database.) And there are plenty of questions about how people will make use of this data, which has been annotated with many measurements that are useful for face recognition systems.

Not only that, photographic subjects were, in effect, turned into research subjects without their consent. And even though their photos were public on Flickr, a strong case can be made that the new context violates their privacy.

Cornell Tech professor Helen Nissenbaum, author of the book [_Privacy in Context_](<https://www.sup.org/books/title/?id=8862>), reminds us that we need to think about privacy in terms of when data moves from one context to another, rather than in absolute terms. Thinking about changes in context is difficult, but essential: we’ve long passed the point where any return to absolute privacy was possible—if it ever was possible in the first place.

Meredith Whittaker, co-director of the AI Now Institute, made a striking extension to this insight in a quote from the same NBC article: “People gave their consent to sharing their photos in a different internet ecosystem.”

We do indeed live in a different internet ecosystem than the one many of our original privacy rules were invented for. The internet is not what it was 30 years ago. The web is not what it was 30 years ago, when it was invented. Flickr is not what it was when it was founded. 15 or 20 years ago, we had some vague ideas about face recognition, but it was a lot closer to science fiction. People weren’t actually automating image tagging, which is creepy enough; they certainly weren’t building applications to [scan attendees at concerts](<https://www.theverge.com/2018/12/12/18137984/taylor-swift-facial-recognition-tech-concert-attendees-stalkers>) or [sporting events](<https://www.bbc.com/news/technology-44089161>).

IBM’s creation of a new database obviously represents a change of context. But Whittaker is saying that the internet itself is a changing context. It isn’t what it has been in the past; it probably never could have stayed the same; but regardless of what it is now, the data’s context has changed, without the data moving. We’re right to worry about data flows, but we also have to worry about the context changing even when data doesn’t flow. It’s easy to point fingers at IBM for using Flickr’s data irresponsibly—as we read it, we’re sympathetic with that position. But the real challenge is that the meaning of the images on Flickr has changed. They’re not just photos: they’re a cache of data for training machine learning systems.

What do we do when the contexts themselves change? That’s a question we must work hard to answer. Part of the problem is that contexts change slowly, and that changes in a context are much easier to ignore than a new data-driven application.

Some might argue that data can never be used without consent. But that has led us down a path of over-broad [clickwrap agreements](<https://en.wikipedia.org/wiki/Clickwrap>) that force people to give consent for things that are not yet even imagined in order to use a valuable service.

One special type of meta-context to consider is intent. While context may change, it is possible to look through that changing context to the intent of a user’s consent to the use of their data. For example, when someone uses Google maps, they implicitly consent to Google using location data to guide them from place to place. When Google then provides an API that allows Uber or Lyft or Doordash to leverage that data to guide a driver to them, the context has changed but the intent has not. The data was part of a service transaction, and the intent can be “well-intentionedly” transferred to a new context, as long as it is still in service of the user, rather than simply for the advantage of the data holder.

When Google decides to use your location to target advertisements, that’s not only a different context but a different intent. As it turns out, Google actually expresses the intent of their data collection very broadly, and asks its users to consent to Google’s use of their data in many evolving contexts as the cost of providing free services. There would surely be value in finer grained expression of intent. At the same time, you can make the case that there was a kind of meta-intent expressed and agreed to, which can survive the context transition to new services. What we still need in a case like this is some mechanism for redress, for users to say “in this case, you went too far” even as they often are delighted by other new and unexpected uses for their data.

There are other cases where the breach of intent is far clearer. For example, when my cell phone provider gets my location as a byproduct of connecting me to a cell tower, other use of my data was never part of the transaction, and [when they resell it (as they do)](<https://techcrunch.com/2019/01/09/us-cell-carriers-still-selling-your-location-data/>), that is a breach not only of context but of intent.

Data ethics raises many a hard problem. Fortunately, the framing of context as a guiding principle by Nissenbaum and Whittaker gives us a powerful way to work toward solving them.
