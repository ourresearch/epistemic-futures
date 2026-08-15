---
title: "Making the Web kid-readable"
person: david-weinberger
section: by
type: blog-post
year: 2019
date: 2019-10-06
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2019/10/06/making-the-web-kid-readable/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# Making the Web kid-readable

## Full text

Of the 4.67 gazillion pages on the Web, exactly 1.87 nano-bazillion are understandable by children. Suppose there were a convention and a service for making child-friendly versions of any site that wanted to increase its presence and value?

That was the basic idea behind our project at the MindCET Hackathon in the Desert a couple of weeks ago.

MindCET is an ed tech incubator created by the Center for Educational Technology (CET) in Israel. “Automatically generates grade-specific versions? Hahaha.”Its founder and leader is Avi Warshavsky, a brilliant technologist and a person of great warmth and character, devoted to improving education for all the world’s children. Over the ten years that I’ve been on the CET tech advisory board, Avi has become a treasured personal friend.

In Yeruham on the edge of the Negev, 14 teams of 6-8 people did the hackathon thing. Our team — to my shame, I don’t have a list of them — pretty quickly settled on thinking about what it would take to create a world-wide expectation that sites that explain things would have versions suitable for children at various grade levels.

So, here’s our plan for Onderstand.com.

Let’s say you have a site that provides information about some topic; our example was a page about how planes fly. It’s written at a normal adult level, or perhaps it assumes even more expertise about the topic. You would like the page to be accessible to kids in grade school.

No problem! Just go to Onderstand.com and enter the page’s URL. Up pops a form that lets you press a button to automatically generate versions for your choice of grade levels. Or you can create your own versions manually. The form also lets you enter useful metadata, including what school kid questions you think your site addresses, such as “How do planes fly?”, “What keeps planes up?”, and “Why don’t planes crash?” (And because everything is miscellaneous, you also enter tags, of course.)

Before I go any further, let me address your question: “It automatically generates grade-specific versions? Hahaha.” Yes, it’s true that in the 36 hours of the hackathon, we did not fully train the requisite machine learning model, in the sense that we didn’t even try. But let’s come back to that…

Ok, so imagine that you now have three grade-specific versions of your page about how planes fly. You put them on your site and give Onderstand their Web addresses as well as the metadata you’ve filled in. (Perhaps Onderstand.com would also host or archive the pages. We did not work out all these details.)

Onderstand generates a button you can place on your site that lets the visitor know that there are kid-ready versions.

The fact that there are those versions available is also recorded by Onderstand.com so that kids know that if they have a question, they can search Onderstand for appropriate versions.

Our business model is the classic “We’re doing something of value so someone will pay for it somehow.” Of course, we guarantee that we will never sell, rent, publish, share or monetize user information. But one positive thing about this approach: The service does not become valuable only once there’s lots of content. “Because sites get the kid-ready button, they get value from it”Because sites get the kid-ready button, they get value from it even if the Onderstand.com site attracts no visitors.

If the idea were to take off, then a convention that it establishes would be useful even if Onderstand were to fold up like a cheap table. The convention would be something like Wikipedia’s prepending “simple” before an article address. For example, the Wikipedia article “Airplane” is a great example of the problem: It is full of details but light on generalizations, uses hyperlinks as an excuse for lazily relying on jargon rather than readable text, and never actually explains how a plane flies. But if you prepend “simple” to that page’s URL — https://simple.wikipedia.org/wiki/Fixed-wing_aircraft — you get taken to a much shorter page with far fewer details (but also still no explanation of how planes fly).

Now, our hackathon group did not actually come up with what those prepensions should be. Maybe “grade3”, “grade9”, etc. But we wouldn’t want kids to have to guess which grade levels the site has available. So maybe just “school” or some such which would then pop up a list of the available versions. What I’m trying to say is that that’s the only detail left before we transform the Web.

The machine learning miracle

Machine learning might be able to provide a fairly straightforward, and often unsatisfactory, way of generating grade-specific versions.

“The ML could be trained on a corpus of text that has human-generated versions for kids.”The ML could be trained on a corpus of text that has human-generated versions for kids. The “simple” Wikipedia pages and their adult equivalents could be one source. Textbooks on the same subjects designed for different class levels might be another, even though — unlike the Wikipedia “simple” pages — they are not more or less translations of the same text. There are several experimental simplification applications discussed on the Web already.

Even if this worked, it’s likely to be sub-par because it would just be simplifying language, not generating explanations that creatively think in kids’ terms. For example, to explain flight to a high schooler, you would probably want to explain the Bernoulli effect and the four forces that act on a wing, but for a middle schooler you might start with the experiment in which they blow across a strip of paper, and for a grade schooler you might want to ask if they’ve ever blown on the bottom of a bubble.

So, even if the ML works, the site owner might want to do something more creative and effective. But still, simply having reduced-vocabulary versions could be helpful, and might set an expectation that a site isn’t truly accessible if it isn’t understandable.

Ok, so who’s in on the angel funding round?
