---
title: "Connected Copies, Part One"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-02-15
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/02/15/connected-copies-part-one/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Connected Copies, Part One

## Full text

_This is a series of posts I ’ve finally decided to write on the subject of what I call “connected copies”, an old pattern in software that is solving a lot of current problems. _

_It ’s really a bit of a brain dump. But it’s my first attempt to explain these concepts starting at a point most people can grasp (e.g. people who don’t have git or Named Data Networking or blockchain or federated wiki as a starting point). Hopefully publishing these somewhat disorganized presentations will help me eventually put together something more organized and suitable for non-technical audiences. Or maybe it will just convince me that this is too vast a subject to explain._

_Anyways …._

## The Party

Let’s imagine you are planning a birthday party for an office mate. And for both musical and technical reasons, let’s imagine you were doing this in 1983.

(Insert cassette of David Bowie’s _Let ’s Dance_ in 3… 2… 1…)

You’re planning a party for Sheila, and you want everyone to bring something. You talk to everybody and write up a list:

Cliff: Plastic silverware  
Norm: Vanilla ice cream  
Sam: Chocolate cake with cream cheese frosting  
Rita: Card, streamers  
Diane: Ice cream fixings

You write out this list, and you photocopy it. Each person gets a copy on Monday so they can prep Friday’s party.

Programmers call this sort of copying  _passing by value_ and it has a lot of advantages. Each person has a copy they can carry around. They can change that copy, annotate it. If Cliff loses his copy, Norm doesn’t lose his. And so on.

Unfortunately this party hits a snag. Norm is talking to Sheila and finds out that Sheila is lactose intolerant. On his copy he crosses out the ice cream, and replaces it with lactose-free cookies, making a note of her intolerance.

But because these sheets are copies, no one else ever sees his update. He comes with cookies, but Diane is still bringing ice cream fixings, and frankly we’re not quite sure whether that cream cheese frosting cake is such a good idea either. The party is a disaster.

Here’s another approach we could use for the party. Instead of making copies, we say “sign up on the kitchen whiteboard”.

If we run this with the office whiteboard, we get a different, and better result. When Norm finds out about the sensitivity, he changes his item to the cookies, and writes a note about the issue. Diane, seeing this, skips the ice cream fixings in favor of getting soda, and Sam reconsiders his cream-cheese cake, finding something more palatable. As each make their changes, they note them on the board.

Saying where the definitive list  _is_ (e.g. “The kitchen whiteboard”) instead of making copies of its value is what programmers call  _passing by reference_. As you’ll note, it has certain advantages.

## The Web Is a Series of Whiteboards

In our kitchen whiteboard example, of course, it has one big disadvantage, which is you can only access it when you’re in the kitchen. Of course, with the dawn of the Internet, this problem was largely solved. A web page is like a whiteboard you can read from anywhere. A calendar feed, a video link — these are all protocols which say, more or less, go find the set of values currently at this location.

The web is in fact built around this structure. It understands locations, not objects or copies.

What, for example, is the URL for “find me a copy of Moby Dick”? There is none. There is only a URL for “get me a copy of whatever is currently at the address that this one instance of Moby Dick is supposed to be at”.

It is important to note that the web doesn’t have to be structured this way. Torrents, for example, use a different approach. When you attempt to retrieve something through torrenting, your computer isn’t concerned with where the one true location is. Instead, your torrenting client asks for an object, and any locations that have that object can return pieces of it to you.

Programmers have developed ingenious ways to make requests for locations to act sort of like requests for objects (proxy servers are a simple example) but at the heart of the web as we currently use it is this assumption: things are defined by the location from which they are served.

Again, this model is an amazing model, and one that should be embraced in a lot more circumstances. As Jon Udell has noted, people can use a system of passing by reference to maintain tight control over their personal information: if I share a Word Document with you of my calendar, I lose the ability to update that; if I share my calendar feed, I retain central control.

But just as there are many circumstances where we are still passing around copies when we should be passing around references, there are also cases where we are not fully understanding some of the benefits copies provided.

## In Which Whiteboards Go White

I used to have a hobby of collecting old reference works. Ancient textbooks, encyclopedias, atlases, books of trivia from the 1800s; I loved them all.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2016/02/cata.png>)

What’s amazing to me (and what’s been amazing for a long time) is how durable these books were. Not as physical books, mind you, but as an  _information strategy_.

Here, for example, is a random page of a used bookseller’s catalog of used works available in 1812 or so:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2016/02/catalog1.png>)

These are individual issues, available for resale, from what I can tell. But look at the dates. Even at that time you have stuff from 200 years prior being sold in that store. What do we have on the web that will survive in 200 years?

Ah, you say, it’s just survival bias. These are the works that survived; we don’t know what didn’t.

Except, no.We can take this set of books as our little experimental cohort, start the clock in 1812, and then see how many make it through to today.

And when we do that we find the answer is to how many survived is… all of them. In fact, take a look, most of these are now digitized on the web:

  * [Universal Library, or Complete Summary of Science](<https://books.google.com/books?id=OhKUKw7u8LQC&dq=editions:QgXIbIB7ibUC&source=gbs_navlinks_s>)
  * [Vince’s Principles of Hydrostatics](<https://books.google.com/books?id=L99hAAAAcAAJ&pg=PP9&dq=Vince%27s+principles+of+hydrostatics&hl=en&sa=X&ved=0ahUKEwjtpIXIuPrKAhVN2WMKHVzfBsAQ6AEILjAD#v=onepage&q=Vince's%20principles%20of%20hydrostatics&f=false>)
  * [Ward’s Mathematician’s Guide](<https://books.google.com/books?id=8dY2AAAAMAAJ&printsec=frontcover&dq=Ward%27s+mathematicians+guide&hl=en&sa=X&ved=0ahUKEwi-6sPevPrKAhVG3WMKHa6cCXYQ6AEIKjAA#v=onepage&q=Ward's%20mathematicians%20guide&f=false>)
  * [Watt’s First Principles of Astronomy and Geography](<https://books.google.com/books?id=W_7CW9IX21MC&dq=Watt%27s+first+principles+of+astronomy+and+geography&source=gbs_navlinks_s>)
  * [Webb’s Complete Negociator](<https://books.google.com/books?id=FOxZAAAAcAAJ&dq=webb%27s+complete+negociator&source=gbs_navlinks_s>)
  * [Well’s Young Gentleman’s Astronomy](<https://books.google.com/books?id=yo9unZOxhkYC&dq=Well%27s+Young+Gentleman%27s+Astronomy&source=gbs_navlinks_s>)
  * [Weston’s Complete Merchant’s Clerk](<http://www.worldcat.org/title/complete-merchants-clerk-or-british-and-american-counting-house-in-two-parts-part-i-contains-a-system-of-book-keeping-according-to-the-italian-form-of-debtor-and-creditor-by-double-entry-as-practised-at-this-time-by-the-merchants-of-great-britain-c-comprehending-the-useful-varieties-incident-to-trade-and-the-method-of-balancing-rendered-familiar-to-the-meanest-capacity-by-means-of-an-open-ledger-illustrated-with-plain-and-easy-rules-for-journalizing-and-a-hint-to-the-judicious-on-treating-company-accounts-part-ii-contains-book-keeping-in-factory-as-at-present-used-in-the-sundry-factories-of-america-and-the-west-indies-the-knowledge-of-which-will-render-any-man-capable-of-managing-a-set-of-books-in-any-factory-with-facility-and-judgement-being-found-by-long-experience-the-best-and-most-expeditious-method-for-dispatch-of-business-wherein-is-described-the-utility-and-necessity-of-that-counter-part-of-the-ledger-the-sales-book-with-directions-for-posting-it-together-with-a-summary-of-book-keeping-for-a-wharf-and-plantation-calculated-for-the-information-of-such-as-have-occasion-to-go-to-america-or-the-west-indies-in-quality-of-factor-clerk-wharfinger-plantation-clerk-or-overseer-the-whole-in-a-method-founded-on-and-reducible-to-practice-by-a-series-of-examples-made-useful-to-the-mercantile-trader-in-the-four-quarters-of-the-world-by-william-weston-merchant/oclc/645779110?referer=di&ht=edition>) (behind logins unfortunately, but there)
  * [Whiston’s New Theory of the Earth](<https://books.google.com/books?id=pBlaAAAAYAAJ&printsec=frontcover&dq=Whiston%27s+New+Theory+of+the+Earth&hl=en&sa=X&ved=0ahUKEwi6_97ZwfrKAhUG4WMKHYsVDG0Q6AEIMTAB#v=onepage&q=Whiston's%20New%20Theory%20of%20the%20Earth&f=false>)
  * [Whyte on the Art of Reading and Speaking in Public](<https://books.google.com/books?id=yZdhAAAAcAAJ&dq=Whyte+on+the+Art+of+Reading+and+Speaking+in+Public&source=gbs_navlinks_s>)
  * [Wilkin’s Discovery of a New World](<https://books.google.com/books?id=NII5AAAAcAAJ&printsec=frontcover&dq=Wilkin%27s+Discovery+of+a+New+World&hl=en&sa=X&ved=0ahUKEwiSo8WfwvrKAhVX-GMKHX0GBsYQ6AEIKDAC#v=onepage&q=Wilkin's%20Discovery%20of%20a%20New%20World&f=false>)
  * [Williamson’s Mathematics Simplified](<https://archive.org/details/mathematicssimpl00willrich>)
  * [Willich’s Domestic Encyclopedia](<https://books.google.com/books?id=kchCAQAAMAAJ&dq=willich%27s+Domestic+encyclopedia&source=gbs_navlinks_s>)
  * [Wingate’s Arithmetick](<https://books.google.com/books?id=Pz6lEOSTg2YC&dq=Wingate%27s+Arithmetick&source=gbs_navlinks_s>)

The only works I can’t find here are the two works in Latin, and I’m guessing that’s just due to them not being digitized (or perhaps even due to me botching the search terms).

In other words, on a random page of a random bookseller’s sell-sheet from 1812, **every** **English language work identified has survived**.

How do we compare today?

Well, here’s a screenshot of part of a page from Suck.com in one of its reboots around 2001.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2016/02/suck.png>)

If you don’t know what Suck was, you can [read its history here](<http://www.keepgoing.org/issue20_giant/the_big_fish.html>), but what it was is kind of irrelevant in this example. What you need to know is that they aren’t linking out to fanzines here. They are linking out to major stories and major websites of the time.

There’s about 30 links on the whole page. Three of them work. Three. One of the links that works goes to another page on Suck.com, one goes to the Honolulu Advertiser, and one to a Guardian.co.uk article.

Go to any archived page of about the same time and you’ll find a similar pattern.

Random references to books that are 400 years old are stable. But references to web works that are 15 year old? You’ve got a one in ten chance that it’s still around. You’ve literally got a worse chance clicking a link on a fifteen year old article than you do scratching off a scratch ticket.

It’s like you were told the answer you need is on the work kitchen whiteboard, but when you go there, the whiteboard is erased. Or missing. Or filled with porn.

What the heck is going on?

## Read Something, Host Something

The biggest reason that all the works referenced by the 1812 bookseller survive is that books are copies.

The original proofs of these books did not survive. The specific physical books that were in that bookseller’s shop that year are also less likely to have survived. But some of each of the maybe 1,000 books printed in these runs did survive.

Books have a weird mode of replication. The more people that read a book, the more people host that book in their personal bookshelves.

It’s not one-to-one, of course. I might lend you a book to read. You might read a book in the local library, or buy one secondhand. But the nature of the system of physical books is that if 10,000 people read a book there will be 1,000 books hosted at various locations. And if more people start reading that more books are produced and distributed to yet more locations to be hosted.

You read something, you host it. When you share with others, you share your own copy.

Compare this to the web model. In the web model, a million people can read a story and yet there is one single site that hosts it. The person that hosts it has to take on the expense of hosting it. When it no longer serves their interest they take the copy down, and that work is gone, forever.

It’s worth noting that the web model is is less scalable than the book model. In the book model, the distribution and hosting function is spread out among current and former readers: as the book becomes popular the weight of hosting it and sharing it is dispersed. In the web system, something suddenly popular is a burden to the publisher, who can’t keep up with spikes in demand as they hit that specific URL.

You can imagine another system for the web fairly easily, where everyone has a small server of their own, the way everyone once had a bookshelf. When you share a link with a friend, you share a link to your copy of something on your bookshelf, hosted on your own server.

That friend reads the page and decides to share it with others. In doing so they make a copy to their server, and they share from there to more friends. As the work propagates out, server load is dispersed, and copies proliferate.

These are some of the ideas underlying recent inventions such as the Interplanetary File System and federated wiki (although each of those is much more than just that idea).

## Corporate Copies

These ideas may seem far out, but they’re not at all. In fact, because of the way web use has evolved, it’s inevitable that we’ll move in the direction of copies. It’s just a matter of whether we get the corporate version of this vision or a more radical reader-centered vision.

The corporate version is coming, without a doubt. Consider, for example, the day that _Jessica Jones,_ a ten episode Netflix series was released. Over that weekend I’m guessing that several thousand people in my zipcode binge watched those episodes. All streaming it from Netflix which was how many miles away.

Which, of course, makes no sense.

I’ve downloaded all 10 episodes. But when my neighbor gets the urge to binge, my neighbor’s set-top box doesn’t go 20 feet to get those files. It goes thousands of miles to Netflix’s servers (or hundreds of miles to Netflix’s distributed content network).

The Internet wasn’t really built for this sort of thing. The assumption the Internet was built on was “I want a certain remote machine somewhere to do something, send it a message and get the result.” When we look at content over the web, this translated to “Tell the remote computer to send me the file at this location or with this id”. But central to the protocol is we know the where and the where gives us the what.

This makes sense when we are trying to get specific information from specific computers. It starts to make less sense when we want a thing that could be in any of thousands of places, not a response from a particular machine.

Eventually this will fall away. Thirty-six percent of Internet traffic in the U.S. is Netflix shipping you videos you could more easily grab from your neighbors.

Of course, if corporations implement it, it will suck. Which is why there’s a whole bunch of others thinking through the implications of connected copies. And it’s a reason that you should be thinking about it too, if you want the next iteration of the web to be awesome and not suck.

The current system has us “know the where and get the what”. The next system will have us “know the what and get the where”. But thinking through the implications of that beyond Netflix delivery is what interests me, because it opens up a new way to think about copies entirely.

## 

## Next: [Connected Copies, Part Two](<http://hapgood.us/2016/02/17/connected-copies-part-two/>)
