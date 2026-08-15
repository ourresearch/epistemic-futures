---
title: "Federated Wiki, explanation as of April 2014"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-04-24
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/04/24/federated-wiki-explanation-as-of-april-2014/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Federated Wiki, explanation as of April 2014

## Full text

Someone emailed me and asked if I could point to posts on my blog that explain the federated wiki idea. I started to pull together some links, but realized that many explanations were out of date. I’ve been fooling around with this for several months now, and I know a bit more than I once did.

I find it easiest to start the explanation by talking about instructional technology support sites. But if you make it through that explanation, there’s a huge classroom application as well, and even huger OER implications.

[First, let me note I’m not talking here about [Ward Cunningham’s Federated Wiki](<http://wardcunningham.github.io/>), which was largely the inspiration for this, but about our local attempts to make Dokuwiki work in a way that approximates federation. But I think the use cases apply to Ward’s work as well. Conceptually, I would love to use Ward & co.’s SFW as a base for this sort of stuff, but there are some barriers, so we’re left at the moment with Dokuwiki hacks.]

Ok, so here goes the instructional technology support explanation. It’s not the thing I’m most excited about, but it’s the easiest to explain.

There’s really two approaches to producing support documentation for your faculty. The first way, and the way most people choose, is to produce documentation more or less from scratch. Here’s [a recent write up](<http://sites.keene.edu/at/2013/11/04/explain-everything-anywhere/>) of the tool Explain Everything by Judy Brophy at Keene State College.

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/04/explain.png>)

 

Meanwhile, here’s a screencast about Explain Anything from Samuel Williams, who works in IT at the University of Portland:  

If you look through Academic Technology sites, you can find half a dozen of these on this very limited subject. If look at something bigger, like uses of screencasting or flipped classroom implementation, you’ll find hundreds of these, all explained from scratch. That’s a lot of hours spent rewriting basic documentation.

Now, when we see something like this, usually someone will come up with the brilliant idea “We should have ONE CENTRAL SITE that WE ALL COULD WORK ON!” Imagine if Judy and Samuel worked together on the Explain Everything article. It’d be the Wikipedia of Edtech!

But there’s lots of reasons why such a thing doesn’t really work.

For one, maybe Judy has a very location-specific intro on that article (and actually she does, beginning it with a story about a Keene State professor). That’s a good thing, tying it back to the campus like that, and we don’t want to give that up for a wiki.

Second, when you send faculty to a generic wiki to solve their problem, they often look at you like you are throwing them off the boat. It took a lot for them to come to you with this question, and now you’re just spinning them off again into this generic resource. For various reasons, faculty find the presence of local support sites comforting, and see them as evidence that they are supported in their efforts.

Third, Judy and Samuel may have actual differences of opinion that make writing a single article hard. Samuel may think classroom use of clickers is the spawn of Hell. Judy may think it’s the Second Coming. When they send the faculty member to our group wiki, there’s an implicit endorsement of the views there — so who makes the call on the clicker issue? (Note: I really have no idea on what either Judy or Samuel think about clickers).

All of this stuff together makes it very difficult to come up with one version of things. So we continue on, either feeding faculty incoherent messes of links, or writing everything from scratch.

 

## Doctor, Heal Thyself

What’s fascinating to me about this is that for a bunch of people that are constantly telling faculty about the glories of reusing materials we actually suck at reuse. And we suck at it for the same reasons faculty do. Coherence and reuse are orthogonal to one another. We’re not willing to sacrifice the coherence of custom materials, so we sacrifice efficiency.

What we need is a system that promotes revisable reuse in our _own spaces_.

So enter federated wiki. The idea is pretty simple. Let’s say we start with 20 colleges. We all install our own support wikis on our own sites. And then we “federate”.

What does this mean? It means when I make changes to my wiki, they flow to yours. When you make changes to your wiki they flow to mine. And not only to our individual wikis, but to everyone in the federation.

So I go into my wiki and write up this guide to lightly blended courses:

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/04/fed1.png>)

Now when I hit save, it saves to my wiki. But it also notifies all the other members of the federation that there is new content. The admins of those sites will have a number of choices when they see this new content.

  1. Reject it. We don’t want your stinking article on our wiki.
  2. Accept it into a special “drafts” folder, for editing and future posting.
  3. Accept it as is into an editor, make edits on the spot and post.
  4. Accept it as is, and agree that future edits the original author makes to it will automatically flow through to our wiki.

So let’s say that person accepts it as is. But then they notice that there are a number of spelling errors in it, and also that the section on the “Understanding by Design” approach is a bit lengthy. So they pull out the Understanding by Design stuff into a separate article, link it, and fix the spelling errors. When saving it they put in the notes box that they did minor spelling edits and a pull-out of the UbD section.

So now everyone in the federation gets two notifications. First of all, the article has been updated. So they get notified of that. They also see the new article the reviser split off.

Not everything would have to flow through the federation. I might just edit the contact information on an article and decide to check the “Do not syndicate” box before I post. Entire portions of my site may not be federated. It may be that only one subdirectory or namespace is federated.

But you can start to see how this works. It’s like a wiki, but instead of editing a single copy, you “fork” one (and this, again, is the insight of Ward — on a wiki every page has an edit button; on a federated wiki, every page has a fork button). Changes flow back and forth through the network, but everyone maintains control of their own copy. And best of all, the backend would handle credit, so people who wanted to track who did what for the article could easily do that, and so that people who create broadly used pieces could get credit for their work (and warm fuzzy feelings about the amount of use it gets).

 

## **Academic & Pedagogical Uses**

I actually started exploring this idea not because of support sites, but because of barriers I hit with an instructional design project called Water106. The idea seemed simple — get multiple classes from multiple institutions to interact in a common space of the web. So if we were all looking at the issue of water from different scientific, engineering, and political angles we could produce a mega-wiki on water.

A lot of people want to do this stuff. Cross-institutional classes have been the “future of education” for a good decade now. But ultimately it’s a bit clunky to get going. That mega-wiki has to live somewhere. So maybe I own it here at Vancouver. But then I’m setting all the permissions and talking to the faculty in these other places providing support. That’s not really what the instructional technologists at these other institutions want — because ultimately they’d like to build and support this thing without depending on coordinating with me. We want to work together, but without the coordination hassle that could easily consume us.

Furthermore, there’s a pretty simple issue for classes. Instructors want outside influences in their classroom to promote critical thinking, but for grading purposes they want their students to have the last word on their work. They want to know when they are looking as a wiki article that it is in the state that the student believed was the “gradeable” state. They don’t want to have to sort through the issue if someone from outside the class modified it in ways that moved it away from student intention.

Federated wiki is a way around all this. If we all have academic wikis on the subject of water we federate them. Your students just do their work as if they were doing it alone, either on a wiki that your institution controls or on one they own themselves, with whatever security parameters, etc. that you/they need to have. But magically, this other work flows into the wiki that the students can approve or discard (or maybe even transclude?). And again, when students build pieces that get widely re-used throughout the federation, they can take some pride in that. To some extent, it’s like “Tumblr for wikis” — you post your stuff and see how many reblogs (“re-wikis”?) you get.

 

## **OER**

You know what? I’m not even going to go into Open Educational Resources. If you’ve been in the field a while, you can see that this sort of system could start to address the issues we’ve been trying to solve for over a decade. The problems we have reusing materials to help develop faculty are the same problems they have with reusing teaching materials. Solve the smaller problem and you’ve begun to crack into the bigger one.

I’ll just say this: most faculty have some materials/activities/assessments that work brilliantly, and a lot that are mediocre. You can start to see what is possible if 500 Psychology 101 professors start using federated wikis to build their course materials. A system where faculty are pulling the best and most effective bits of pedagogy from around the world is a system that could have amazing impact in education.

I’ve been involved with open education a good ten years now. I’ve gotten cynical about addressing the [Reusability Paradox](<http://www.oercommons.org/courses/the-reusability-paradox/view>). Certain developments in the past couple years have un-cynicalfied me. One is the Lumen Learning approach to OER implementation. Another is this. Good software ideas/implementations can create the possibility of doing something; great software creates a *culture* of doing something. Federated wiki, properly designed, is culture-creating software.

 

## **When Will This Thing Be Built?**

I’m working on Dokuwiki hacks I can, and Tim Owens has also given substantial time to it. I’ve played around with it enough at this point to understand that the primary barriers are not technical. Rather, the most difficult thing is to organize the process by which material gets syndicated throughout the federation in a way that people can easily conceptualize.

Meaning. with enough time to code we can get the files to do what we want. But that step of deciding what comes onto your wiki from the federation — what does that look like? It could get really noisy. It could get very difficult to know which updates of a dozen you want. It could be so time consuming to scan the updates and understand what they are that it’s easier to roll your own. Alternatively, the process could be so silent that everything flows into your drafts folder but never gets used. Things like attributing cleanly without gunking up the articles with too many lines of credits are also issues. Tracking what you have approved and not approved may get confusing as well (Did I review this already?) unless the system handles it elegantly.

And I’m still toying with the idea of using the Smallest Federated Wiki that Ward & co. are developing instead of hacking Dokuwiki. If SFW only had an Installatron setup, we’d be halfway there (i.e. students get personally owned server space via DoOO, login in, punch the installatron button and voila!). SFW would also have to be Section 508 compliant though, to make sure it’s not difficult for the visually impaired to use it. It currently doesn’t seem to play nice with JAWS, and unfortunately that’s a hard stop for us. So, until then, it’s Dokuwiki hacks for now. I’m a spaghetti coder on a good day, so it’s slow going.

Anyway, that’s the update. As I mentioned, I only have a fraction of my time to give to this right now — spending much more time getting Dokuwiki ready for internal use by faculty and putting together workshops for the summer. But I’m always willing to talk about this with anyone who is interested, so give me a shout-out on Twitter @holden. Or comment on this post.
