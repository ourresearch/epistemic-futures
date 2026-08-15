---
title: "Connected Copies, Part Two"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-02-17
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/02/17/connected-copies-part-two/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Connected Copies, Part Two

## Full text

_This is a series of posts I ’ve finally decided to write on the subject of what I call “connected copies”, an old pattern in software that is solving a lot of current problems. Part one of the series is [here](<http://hapgood.us/2016/02/15/connected-copies-part-one/>)._

_It ’s really a bit of a brain dump. But it’s my first attempt to explain these concepts starting at a point most people can grasp (e.g. people who don’t have git or Named Data Networking or blockchain or federated wiki as a starting point). Hopefully publishing these somewhat disorganized presentations will help me eventually put together something more organized and suitable for non-technical audiences. Or maybe it will just convince me that this is too vast a subject to explain._

_Anyways …._

## A Gym Full of People

Let’s think about connection a bit. I want to talk about how connection on the web happens. Because I don’t want to get too into the weeds I’m not going to talk about packets, or _too_ much about routing either. I’m sure many people will think my story here is inadequate for understanding connection on the web, but I think it will work for our purposes.

Imagine you are in a gym full of people, and you’re only allowed to talk to the people next to you. The web sort of works like this.

First, you have to know the domain name or IP of the server that has the thing you want. As we noted in the last post, this is really crucial. The web, as designed,  _starts with “where_“ _, not what._

For a simple example, let’s say what you really want in that gym is a physical book. Let’s say we’re in that gym, and everyone has a stack of books with them. You want a copy of the Connie Willis classic _To Say Nothing of the Dog._ The first thing you have to know is  _where that book is._

There’s huge implications to this fundamental fact of net architecture, but we’ll skip over them for the time being.

So the first thing you do is some research to find out who has this book. Your guess is that Jeff Bezos probably has it because he seems to have copies of *all* the books, as part of this little side business he runs called Amazon.

So you look to see whether any of the people around you are Jeff. But they’re not, so you say to a neighbor hey, here’s an envelope with a message in it — can you get this to Jeff? And in the envelope you put a message that says “Send me _To Say Nothing of the Dog_ ” and on the outside you write your name and address as the return address and Jeff’s name in the “To:” field.

In any case, the person you give the envelope to looks around and see if any of the people standing next to them are Jeff, and if they’re not they figure out who they can pass it to who has the most likelihood of getting it to Jeff.

After five or six people pass it, it ends up at Jeff, and Jeff opens it and reads your “Send _TSNOTD_ ” message. So he makes a copy of that book and put the copy in an envelope (or, for sticklers, puts pieces of the book series of separate envelopes) and then passes it back across the gym to me using the same method “Are you Mike Caulfield’s computer? No? Hmmm. Can you get a message to it then?”

At the risk of boring you, I want to reiterate some points here.

First, before we ask for something on the web — Jennifer Jones, The Gutenberg Bible, the most recent census data — we have to know *where* it is. When what we really wanted was “access to Stanford’s SRI mainframe” or “a videocall connection to Utah” this was an easy problem. What you wanted and the server you wanted it from were inextricably tied together.

But as the Internet (and eventually the web) grew, this became a major problem. Most things we wanted were things where we didn’t know the location.

So the first major giants of the web sprouted up: search engines and directories. They could translate your real question (what you wanted) into the form the web could understand (where to get it from). Essentially, they’d figure out the address to put on the outside of the envelope, so we can mail our request.

You’ll also notice this scheme privileges big sites, because the hardest thing is knowing where things are, and big sites containing everything solve your “from what to where” problem.

## What Would a Content-Centric System Look Like?

There are alternate ways of thinking about networking that are based around content instead of location. These ideas are not just theoretical: they are the basis of things like torrenting, Named Data Networking, and Content-Centric Networking. The priniciples behind the idea were outlined, as many brilliant ideas were, by Ted Nelson many years ago.

To get a content-centric implementation of networking, we ask: “What if instead of asking people around us if they could get a message to Jeff, we instead asked them ‘Do you or anyone you know of have a copy of _To Say Nothing of the Dog_ ‘?”

And then each person turned to other people and asked that until either Jeff or someone else said “Yes, I have it right here, let me send a copy to you!”

On the positive side, you’d probably get the book from someone closer to you. Books would flow from people to people instead of always from Amazon to people (and payment systems could be worked out — this doesn’t assume that these would be free).

On the negative side, this sort of protocol would be pretty time intensive. For every request we’d have to ask everyone through this telephone game, they’d have to check for it and so on. In even the gym it’d be a disaster, never mind on the scale of the Internet.

But but this is where connection comes in. Imagine that you had the Connie Willis book _The Domesday Book_ in your own library, which is part of the same series. And let’s imagine that you open the cover of that book and inside the cover is the entire copy history:

> _“ Antje H. copied this from Marcus Y. who copied it from Kin L. who copied it from Martha B. who copied it from Mike C. who copied it from Jeff B.”_

Well, if these people have one book in the series, they might have another, right? So you start with a location based request. But you still ask the content question, because you don’t care where it comes from:

> “Do you, or anyone you know, have a copy of  _To Say Nothing of the Dog_?”

You notice that Martha B. is standing right next to you, so you ask her. It turns out that she does  _not_ have a copy of this anymore. But she used to have a copy, and she made a copy for Pedro P., so she asks him if he still has a copy. He does, so he makes a copy, and passes it to Martha who passes it to you.

You just got a copy of something without knowing where it was. Congratulations!

More importantly, you just saw the power of connected copies.  _Connected copies_ are _copies that know things about other copies_. The connected piece is the “list of previous owners” inside the cover of that book you got, the knowledge that both _TSNOTD_ and _Domesday Book_ are by the same author, and the system that allows you to act on that knowledge.

## The Big Lesson

I think Content-Centric Networking (CCN) and its variants are very cool, and I hope they get traction. The Named Data Networking project, for example, was named as one of the NSF’s Future of the Internet projects, and feels to me like the early net, with a bunch of research university running nodes on it. The CCNx work at PARC is fascinating. Maelstrom, a BitTorrent-based browser is an interesting experiment as well. (h/t Bill Seitz for pointing me there)

But CCNx or NDN as an architecture for the entire web has an uphill climb, because it would destroy almost every current Silicon Valley business out there. Who needs Google when you can just broadcast what you want and the network finds it for you? Who need Dropbox, when every node on the web can act like a BitTorrent node? Who needs server space or a domain, when locations no longer matter? Who needs Amazon’s distribution network when you can just ask for a film from your neighbors and pay for a decryption key?

So while these schemes _will_ happen (see Part One for why CCN is inevitable), I don’t think they are coming in the next few years. But, importantly, you don’t have to rejigger the whole Internet to get better with content. You just have to think about the ways in which our location-centrism is contributing to the problems we are hitting, from the rise of Facebook, to the lack of findability of OER, to the Wikipedia Edit Wars.

In other words, the reason I spend time talking about the networking element above is that our location-centrism is so baked into our thinking about the web that it’s invisible to us. We think it’s very normal to have to know whose servers something is on in order to read it. We assume it’s good for things to be in one place and only one place, because we’ve structured the web in a way which doesn’t make use of multiple locations very well.

And crucially, we tend to think of documents as having definitive locations and versions (like the whiteboards) rather than being a set of things in various revisions with various annotations (like when I talk about a book like “The Great Gatsby” or play like “Hamlet”, which covers a wide range of slightly different objects). It’s that piece I want to talk about next.

## Next Post: Ward Cunningham’s Idea of a ‘Chorus of Voices’ and Other Stuff I Mostly Got From Ward
