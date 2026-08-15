---
title: "Abulafia"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2005
date: 2005-07-01
venue: "Louche Cannon (gbilder.com)"
authors: "Geoffrey Bilder"
source_url: "https://gbilder.com/2005/07/abulafia/"
retrieved: "2026-08-13"
content: "full-text"
notes: ""
---

# Abulafia

## Full text

# Abulafia[#](#abulafia)

Way back in 1990, when I worked at Brown University, I wrote a hypertext application for the Macintosh called “Abulafia.” (named after the computer in Umberto Eco’s book, [Foucault’s Pendulum](https://www.amazon.co.uk/Foucaults-Pendulum-Umberto-Eco/dp/0099287153/ref=sr_1_1?crid=V3J761W5FNWG&keywords=foucaults+pendulum&qid=1552845684&s=gateway&sprefix=Foucoult%2Caps%2C431&sr=8-1). Recently I found some old Zip disks onto which I archived my Brown work when I left the university in 1995. I asked a hardware magpie friend of mine if he had a way of reading old 100MB Zip cartridges and he did. Amazingly, the old Zip cartridges were still accessible (thanks Iomega) and even more amazingly, I was able to find an old binary of Abulafia and run it under OS X’s classic emulation mode (thanks Apple).

Over the past few years I had grown self-consious about my periodic foam-at-the-mouth-old-man-rants concerning the paucity of the web hypertext model and about “how when I was a lad (way before that dang InterWeb) we did *real* hypertext.” I was happy, therefor, to discover that my memories had not deceived me and that Abulafia did some pretty kick-ass stuff. It seemed like it might be a good idea to document some of this via some screencasts as I doubt Abulafia will be runnable for much longer- particularly not with the Apple move to Intel processors.

## A Little History[#](#a-little-history)

At the time I initially wrote Abulafia, the web was still an experiment at CERN and Apple’s [HyperCard](http://en.wikipedia.org/wiki/HyperCard) had practically co-opted the term “hypertext” despite really being an application development environment. Abulafia was partially a response to HyperCard and was inspired by IRIS’s industrial strength research hypertext environment, [Intermedia](http://www.scholars.nus.edu.sg/landow/cpace/ht/HTatBrown/Intermedia.html). To a lesser extent, Abulafia was also influenced by Eastgate Systems’ “[StorySpace](http://www.eastgate.com/Storyspace.html)“- a hypertext system designed for the creation of interactive fiction. And of course all of these systems were, in turn, inspired by Ted Nelson’s [Xanadu](http://en.wikipedia.org/wiki/Project_Xanadu)…

My first version of Abulafia was – ironically – written in Hypercard. I demonstrated the first version of Abulafia to [CHUG](https://listserv.brown.edu/cgi-bin/wa?A2=ind90&L=CHUG-L&P=R1659) in October of 1990. Response to the HyperCard version of Abulafia was good. In fact, there was a brief period of time when Apple considered bundling it on Macintoshes sold to universities. Unfortunately- this was about the time that Apple decided that it wasn’t in the software business (Doh!) and spun out its software (including HyperCard) into a company called [Claris](http://en.wikipedia.org/wiki/Claris).

Some time during this period (chronology is hazy) I had grown sick of the limitations of HyperCard and rewrote Abulafia in a pseudo version of C++ that was then distributed with “[Think C](https://www.computer-dictionary-online.org/definitions-t/think-c.html).” In about 1992-3 I think that I realized that the web was going to take off (I was a [NeXT](http://en.wikipedia.org/wiki/NeXT) developer and had seen early versions of the [CERN web client](http://www.w3.org/People/Berners-Lee/WorldWideWeb.html)) and I dropped development to focus on creating various web tools.

The binary that I found on the Zip disks is the C++ version of Abulafia. I think I had to leave the source at Brown and I have no idea what happened to it.

## The Current State of Abulafia[#](#the-current-state-of-abulafia)

I was amazed when I managed to copy the binary off of the old Iomega disks and I was floored when I double-clicked on the application and it actually launched.

I didn’t have any good example hypertext “collections” and it was kind of a challenge to create demo collection because I had to be able to recreate all sorts of old versions of RTF, the old Apple “pict” graphics format, etc. Funnily enough, I had the least problem with multimedia formats because all Abulafia multimedia calls were done via the then-nascent QuickTime (although I can predictably crash Abulafia and the entire classic mode if I close any QuickTime window.)

Almost everything in Abulafia still seems to work. The only things that I can’t get to work are links to external applications, “automatic” dictionary links (possibly because they were hard-coded to lookup words on the dictionary service I had running on my NeXT cube) and links into/out-off particular spans of audio/video. It is also evident that there are a number of memory leaks in the app- this becomes painfully clear when I play quicktime movies that are larger than the entire hard drive on the Mac II that I developed Abulafia on. Ah, memories…

Abulafia supported single-user “collections”, in which case it stored all links and document information in a special file within a collection folder, but it also supported multi-user collections, where documents were stored on network drives (AppleShare, I’m afraid) and link and document status information (e.g. document locks) were stored in a SQL database (Sybase, running on my NeXT cube). I’m afraid I can’t get it to work in multiuser mode anymore…

## Explanation and Demonstration of Abulafia’s Features[#](#explanation-and-demonstration-of-abulafias-features)

(warning, the demo screencasts are large-ish QuickTime movies)

Abulafia supported links to and from text, graphics, sound and video/animation. In Abulafia, “links” were defined as connections between two sets of “spans” in two documents. A span could be a selection of text, an area of a graphic or the “in” and “out” points of video/sound. Spans were encoded in what I called “lightweight SGML” (XML didn’t exist back then). Links could also have arbitrary metadata associated with them. This architecture allowed Abulafia to support the following advanced linking features:

**Saved document properties**: You could set specified documents to open automatically when a collection was opened. You could also save the size and position of documents so that they always opened in the same place.

**Basic linking**: Links to and from text, graphics, sound and video/animation. Note that links *from* sound, video and animation don’t seem to be working, but this was a pretty cool feature. You could, for instance, have a video open up a text document when a certain point of the video was reached.

**Demo 1**: Here I launch Abulafia, set a default overview image, link from the overview to a text document and then link from the text document to a photograph. Finally, I save the collection and quit Abulafia.

[

There should have been a video here but your browser does not seem
to support it.
](assets/img/01.webm)

**Overlapping links**: The same span of text or area of a document could link to several places at one. Clicking on a linked span would provide a popup menu of the relevant links, whilst double-clicking on an active span would launch a dialog box listing the relevant links. Think of this as the ability to support overlapping HREFs.

**Renaming links**: Links could be renamed and remain persistent.

**Link annotation**: Links could be annotated. All links were stamped with their author name and time of creation. Link authors were able to provide short explanatory text for each link. This explanatory text would only appear in the link dialog box (not the link popup). This was actually all based on a generic ability to attach any metadata to a link. Note that, under OS X, Abulafia seems unable to determine a username and defaults to “Jane Doe” as the username. Hardly a surprise that this doesn’t work as I was probably grabbing the username from AppleShare settings.

**Demo 2**: Here I launch Abulafia again to show that the overview document now opens automatically. I follow the link to the text document, and then add two overlapping links to the same place that I linked from in example 1. I then rename and annotate the links to help disambiguate them. This example shows a link into a QuickTime movie (I don’t close the movie because doing so crashes everything).

[

There should have been a video here but your browser does not seem
to support it.
](assets/img/02.webm)

**Asynchronous linking**: When creating links, the author could start and end links in any order. This was really just an authoring convenience, but other hypertext systems of the time made linking documents a pretty tedious process.

**Multi-headed links**: Links that could originate from several spans within the same document. Handy, for instance, if you wanted to link from all of the examples of X in document A to a detailed explanation of X in document B. Under OS X all link types except for multimedia in/out points seem to still work.

**Multi-tailed links**: Links that targeted several spans within a document. For instance, you might want to link from the definition of X in document A to all examples of X in document B.

**Demo 3**: I open the text document again, and start several links. I then open the target documents and end the links. I go to the initial document again and start a “multi-headed link” from the several instances of the word “HyperCard”. I then rename the link to show that both anchors point to the same link. Finally, to demo a “multi-tailed link” I open a document that defines the word “Adjective” and I link it to four examples of adjectives in a not-very-original sample sentence.

[

There should have been a video here but your browser does not seem
to support it.
](assets/img/03.webm)

**Auto links**: Links to queries. So, for instance, you could link to a search for all instances of the word “foo” in any document. Again, this feature is broken under OS X- possibly because Abulafia can no longer find my NeXT cube ;-).

**Conditional Links**: Links that would be active or inactive depending on certain conditions. The conditions supported were “link state”, “date”, “time” and “random”. They worked like this:

* **State**: Links activate or deactivate depending on the whether or not other links have already been followed. For instance, could make a user have to follow a link to the introduction before they were alowed to follow links to more advanced topics. This could also be used by the interactive fiction crowd to create stories that changed as you navigated them.
* **Date**: Links only activate or deactivate depending on a date condition. So, for instance, you could have links that are only active before X date, only active after X date or only active between dates X and Y. This feature was put in to support learning management features (e.g. You can not access the answers to the problem sets until after their due date). It could also be used for creating date/time sensitive interactive fiction.
* **Time**: Similar to the above. You could set links to only activate at certain times. For some reason, this feature doesn’t seem to be working under OS X.
* **Random**: Links are given a 1 in N chance of being active. This feature was put in to support interactive fiction applications and it doesn’t seem to be working under OS X.

Of course you could combine conditions so that you could say that a certain link had a 1 in 2 chance of being active in the morning and a 1 in 100 chance of being active in the afternoon, but only after December 29th, 1996 and only if the user had already followed the link to the narrative about the butler. Kinda cool, if you were into that sort of thing.

[Demo 4][13]: I set a “state condition” on the link to the “Abulafia’s Features” document that only makes the link active if the user has already followed the “Abulafia Development” link. I also show how, if one wanted to, one could add a date condition to the link.

[

There should have been a video here but your browser does not seem
to support it.
](assets/img/04.webm)

**Persistent links**: Both originating and target documents could be edited and link integrity would be maintained as long as said documents continued to contain at least one origin and target span. When all all relevant origin or target spans were deleted, then the link would be deleted (after warning the user).

**Demo 5**: I open the text document, unlock it, and edit it. Finally, I show that all the anchors still exist and all the links persist.

[

There should have been a video here but your browser does not seem
to support it.
](assets/img/05.webm)

Anyway, I’m happy that I have finally been able to document Abulafia. Perhaps now I will stop frightening youngsters with tales of the hypertext systems of yore…
