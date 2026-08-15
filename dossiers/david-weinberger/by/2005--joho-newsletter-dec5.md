---
title: "JOHO — The Journal of the Hyperlinked Organization, 2005-12-05"
person: david-weinberger
section: by
type: essay
year: 2005
date: 2005-12-05
venue: "JOHO (Journal of the Hyperlinked Organization) newsletter"
authors: "David Weinberger"
source_url: https://www.hyperorg.com/backissues/joho-dec05-05.html
retrieved: 2026-08-13
content: full-text
notes: "Issue of Weinberger's long-running email newsletter (1995-2012). The live hyperorg.com/backissues/ directory now 404s; retrieved from the Internet Archive (https://web.archive.org/web/2020id_/https://www.hyperorg.com/backissues/joho-dec05-05.html). Each issue bundles several essays plus recurring departments (Cool Tool, Walking the Walk, Bogus Contest, Email/letters). Navigation and subscription boilerplate stripped."
---

# JOHO — The Journal of the Hyperlinked Organization, 2005-12-05

## Full text

December 5 , 2005

Contents

The year of unique IDs: We're about to get
very interested in assigning meaningless numbers to lots of things.
Very interested.

Living on an Internet houseboat: Save
the Net for aging hippies? Probably not going to happen.

My book: Progress report: Here's what chapter
3 looks like.

The year of unique IDs

Last year, it was Web
2.0 and tagging. This year, it's going to be unique
IDs (UIDs), and for the same reason that Web 2.0 and tagging matter: The
Web is going miscellaneous. (The fact that I'm writing a book about the
invigoration of the miscellaneous could not possibly have colored my perception.
Nope. All of this is based on highly scientifical research done by people
with clipboards who were teased as children.)

"Web 2.0" is one of those terms with lots of precise meanings,
none of them entirely consistent with the others. To me, it refers to the
way in which data and applications can be integrated across the Web, building
new apps out of snippets of old. (I'm not nearly as fond of the implication
that only with Web 2.0 did users come to have a voice on the Web. User
voice has driven the Web since it began.) Web 2.0 takes what were monolithic
apps and breaks them apart so they can be stitched together in new ways.
Tags break apart the world of hyperlinked pages so that we can pull them
together around meanings that we, the readers, supply.

But none of this restitching is possible without thread. That's where
unique IDs come in.

When you have a large pile of stuff, you need a way to identify it. The
more meaningful the names, the worse they scale. For example, if you want
to make a photo of a rabbit findable
by anyone across the Web, calling it "rabbit" or even "rabbit_305464" (because
there were 305,463 rabbit photos posted before yours) may make it easier
for English speakers to find it, but it makes it harder for those in other
languages. Plus, while you think it is a photo of a rabbit, someone else
may think it's a photo of a pet or dinner. A better solution is to take
the semantics out of the identifier so that multiple semantics can be layered
on top: "Ah, you mean photo #F345A90875264D3425! The one that Deb
Franklin calls 'Rabbit' and that Jean-Paul Lingerie calls 'Lapin.'" (Yes,
the alpha characters imply a particular alphabet, which may be a problem.)

We could wait for authorities in each domain to issue the numbers, but
we'll make more progress faster if we accept that multiple interest groups
within a particular domain are going to issue UIDs.

But there's the rub. In fact, there are several rubs, not all of them
as relaxing as a Swedish massage, unless a Swedish massage is the one where
they beat you with sticks.

For example: Books

UIDs allows the sort of specificity that computers love. For example,
when the person at the cash register (who well might be our daughter Leah,
so be nice to her!) wands your groceries, the cash register knows exactly
what you're buying. But some items don't come wrapped with neat little
UPC's printed on them. The canonical example is a book. And the canonical
book example is Hamlet.

Every edition of Hamlet since
the mid-Sixties has its own ISBN (International Standard Book Number).
The Signet hardcover, paperback, large print, and online versions each
have their own ISBN. But Hamlet itself
has no ISBN number. So how do computers know that this edition of Hamlet is
the same as that other edition of Hamlet, in some meaningful sense
of "same"?

They don't. I spoke with Tom Hickey, chief scientist at the Online Computer
Library Center (OCLC) about this. He began by describing a standard called
Functional Requirements for Bibliographic Records (FRBR) created by the
International Federation of Libraries Association. It describes several
levels of classification:

Works (e.g., Hamlet)

Expression (e.g., the Folger's Hamlet with annotations and
introduction)

Manifestation (a particular print run of Folger's Hamlet)

Item (a copy of Folger's Hamlet sitting on a shelf)

ISBNs apply somewhere between expressions and manifestations. But
you don't have to get all philosmellical about it: ISBNs are inventory
numbers intended to enable bookstores and publishers to automate the tracking
of books. Whatever commerce decrees is a unit is a unit.

Publishers buy blocks of ISBNs from R.R. Bowker and assign
them as they see fit. The numbers are almost without meaning: The initial
digits indicate the original publisher, and the the final digit is a checksum
used to verify that the number is legit. Beyond that, the numbers are given
out sequentially. Carol Cooper, Senior Director, Standards Services, at
Bowker, says that on average, 12,000 new publishers apply for a prefix
every year. (That's publishers, not books.) A large publisher might take
a block of 100,000 numbers at a time.

While Bowker owns the authenticating system for ISBNs, the ISBNs themselves
can be referenced and used without the permission of Bowkers or the publishers,
says Carol.

ISBNs are moving from 10 to 13 digits over the next couple of years. That's
not because they're running out of numbers but because the European Article
Number (a merchandise numbering system) is 13 digits long and Bowker wants
ISBNs to fit easily into the new system.

ISBNs work when you define books as commercial objects created by publishers
and sold by bookstores. That means Folger's Hamlet with
a New Introduction by Jim Carrey gets an ISBN, but Hamlet itself
does not because no one sells Hamlet-in-general...even though
most of us want to find a copy of Hamlet-in-general and don't
much care about which version it is.
ISBNs don't understand books at that level of abstraction.

There are a number of approaches to identifying when two books are in
some sense the same. One is OCLC's xISBN. "Key
in an ISBN for Hamlet,"
says Tom Hickey, "and you'll get a long list." The list is
compiled in part by hand by people working with OCLC's WorldCat,
an online catalog of books and other stuff in libraries.
Some of the clustering is done algorithmically and it's harder than one
might think. "There
are lots of different titles of Hamlet," Tom
points out: "Shakespeare's Hamlet, Shakespeare's Tragedy the Prince
of Denmark," etc. The algorithmic clustering is abetted by humans.
Tom says that they'd like to expand the clusters so that if you search
for Hamlet you'd
get back The Collected Works of Shakespeare, the audio versions,
and the various movie versions, but that's some ways off. Likewise, he'd
like to expand beyond books to magazines and journals. The system is free
for now and the foreseeable future.

ISBNs were designed for print books. Now there are Digital
Object Identifiers (DOIs) that "fall under the purview" of
R.R. Bowker, says Carol Cooper. A DOI is designed to function
as a clickable hyperlink that takes you to the publisher's choice of
pages
— perhaps an order page, a page listing various available versions,
or a digital frights page. (A "digital
fright page" is
a page that warns you against using content in ways you used to think were
legitimate. I just made it up.) The International DOI Foundation provides
the blocks of numbers and also the resolution service so that when someone
clicks on one of them, users are taken to the right page.

The scientific publishing industry is by far the main user of DOIs. Crossref.org "houses
14 million of the 20 million DOIs that are live today," says Carol.

DOIs were designed in part to enabled greater granularity. If you're a
publisher, you can assign some of the DOIs you've bought to charts, sections,
illustrations, or whatever you'd like. As we aim at more miscellaneousness,
greater granularity is key. (Enabling users to arbitrarily designate the
chunks that are useful to them would be a huge step forward.)

Talis, a UK provider of
library systems for thirty years, has a related offering. They recently
launched SkyWalk,
an attempt to map various library classification schemes so that users
can ask "Do you have a copy of Hamlet?" without having to
booleanly specify "OR Shakespeare's Tragedy of the Prince of Denmark
OR Hamlet, Prince of Denmark OR Hamlette: Shakespeare Misspelled?"
Paul Miller, the Talis technology evangelist, says that SkyWalk uses xISBN
to help with the mapping. It is a free service.

Yes, it's a complex field. That's because providing unique IDs is
an ontological problem. You need to know the level of abstraction at which
you're dealing and, even then, "When are two copies of Hamlet the
same?" is way too difficult a question to throw at a computer without
a whole lot of human sorting-through. For example, even if a system had
access to the full text (which these systems do not), two heavily annotated
student editions might look quite different.

So far, at least
in the realm of books, the successful sorting-throughs have been motivated
by crass commercial needs. That's why they work. But the commercial sense
of ontology — two
books are the same if the accounting entries are the same — isn't
the only one that matters to readers. This is not an issue we're ever going
to get perfectly right because there isn't one right answer. The rare book
collectors are always going to have a different sense of what needs a unique
ID than are the public school teachers.

But that won't stop us from slapping numbers on things using schemes that
slice up the world in ways that work at least pretty well for us.

ID's for the rest of us

For example, In September,
Ulla-Maaria Mutanen, a Finnish crafts blogger, thought it might be a good idea
to enable people to provide unique IDs for "long
tail producers," i.e., craftspeople and micro-entrepeneurs. She
talked about this with Jimbo
Wikipedia Wales who suggested that
the IDs be numeric and meaningless to avoid trademark fights and other "useless
legal complaints." Jimbo went on to say " My
thinking is that the ecosystems which may build on the identifiers should
be kept separate from the identifiers themselves." Bingo!

So Ulla started ThingLinks. "A
thinglink is a free unique identifier that anybody can use for making the
finding and recommendation of particular things easier in the Internet,"
says the site. The Thinglinks.org site
is not quite operational yet, but there's a basic ThingLink creator there.
It charmingly asks you to poke around to make sure the thing you're trying
to register doesn't already have an established code (such as UPC). Then
it creates an arbitrary number. But an ID system also needs some type of
registry so we can see what the meaningless numbers mean. Ulla writes,
in an email: "We need a thinglink database with some structured data,
free text, and folksonomic tagging - and that's what we're going to build
next."

Will ThingLinks catch on? Dunno. If it caught on for a particular type of
object — say it becomes the default ID system for garden gnomes, just as
DOIs are the default for some sets of scientific articles —
that would be success. And that's the point: In the distributed
world of the Web, we can always find ways to pull ourselves together. The
first thing is to get ourselves some workable IDs.

Why UIDs will be big and what they'll look like

UIDs are going to be important because they enable people and systems
to agree on what they're talking about. Thus can systems interoperate and
new applications can be built pulling together information and concepts
from their digital diaspora.

UIDs get the religious taxonomical questions out of the way by remaining
relentlessly meaningless. Even so, as we've just seen, religion creeps
back in when systems decide what constitutes a proper object. Communities
that want to share knowledge — scientists, for example — will have to
work out the issues themselves.

And they will. Which is why I think UIDs are more likely than global UIDs.
Competing groups will come up with their own schemes, perhaps
labeling incommensurate objects, and then as the need becomes pressing,
we'll map the systems together, however awkwardly. That may require a lot
of footnotes, but experience has shown (anyone remember SGML?) that we're
better off having relatively local groups succeed at ID'ing objects and
then knitting them together than waiting for the World Council on Numbering
Things to come up with a global standard. That hasn't happened since Adam
and Eve, and even they made an arbitrary decision to names classes of things
("Let's
call them 'dogs'") and not particulars ("Let's
name that thing 'Rover' and that thing "Fido'").

We're going to have to provide UIDs because before language, we at least
had pointing. UIDs are pointing for computers.

Great things will come of these UIDs. My hunch is that we're going to
see lots of activity over the next 12-18 months...

NOTE #1: I'm going to write about unique IDs in my
book, so if you have examples or if I'm going
wrong with this, please let me know. Thanks!

NOTE #2: Things need unique IDs. People do not, if only because things
aren't persecuted by rights-hostile governments. But that's a whole 'nother
argument...

Living on an Internet houseboat

As we survey the damage being done to the Internet by (sometimes) well-meaning
regulators trying to save the Net from itself, I find myself asking: Are
we living on the same Internet planet?

The answer pretty clearly is No. And it's not just regulators whose vision
of the Net is so at odds with mine. There are plenty of academics, librarians,
and even some of the Net's creators who view it as an occasional resource,
a place to go to do research, and a swamp of filth.

To me, the Internet is a social world. It's where most of my friends are.
It's where I hang out. To a serious extent, I live there. And the same is
true for lots of the people I know. Go to a tech conference or the Berkman
Center, and when there's a lull, people get on their laptops to mix it up
with their buddies. Outsiders
think we're antisocial, but we know that most of our friendships are
illuminated by screen light. We're being intensely social.

Or so I would have said last Friday. Then it occurred to me that they're
right and we're wrong.

Moored along the sides of the canals in Amsterdam are houseboats — apartment-sized
barges that move only when the law requires them to prove
they're not small houses with very wet basements. When
you walk along a canal and see them, you can't help imagining living in one.

Perhaps my friends and I are living in the equivalent of an Amsterdam houseboat.
We've been there so long, we think it's normal. In fact, we think it's obvious
that eventually everyone will be living in one. So, when the regulators come
and try to clean up the canals, which means getting rid of the old, creaky
houseboats, we look at them in amazement. "Dudes,
don't you know how great it is that everyone lives on houseboats now? The
gentle rocking, the sound of the rain, the freedom to moor anywhere you want?
How can you take that away from everyone?"

And the regulators look at us like we're crazy. Which we are.

I gotta say, though, that the Internet houseboat days have been fantastic...

My book: Progress report (Or: How I spent the autumn)

Although readers of my blog might not know it, working on Everything
is Miscellaneous is my full-time job. Here's what chapter 3 is currently
about, although it may undergo drastic revision.

Chapter 3: If a tree falls...

Here's how the chapter opens:

It's a long drive. The kids are in the back seat. They've colored
in their coloring books. They've listened to the CDs you brought for
them. They've eaten their fruit snacks – the ones that contain
2% fruit and 30% sugar. You know they're getting edgy because they're
starting to complain about each other. So, you interject in an overly-delighted
voice, “Let's play Twenty Questions!”

Although you just wanted to keep your kids quiet, by the time everybody
in the car has had a chance to be It, your children have learned a few important
lessons.

They've learned what scope of object is guess-able: A desk,
yes. Furniture, no. The guard's desk I saw in the Louvre in 1978, definitely
not, unless you're trying to drive your children to tears.

They've learned how to hint, a sophisticated process that requires
gauging not just how knowledge interlocks, but how knowledge appears
to others.

They've learned the difference between hinting and cheating, a lesson
in when we think it's ok to bend our own rules.

Perhaps most important, they've learned that the world is shaped
like a tree...

Then we finally get to talk about Borges'
famous, and famously absurd, list,
the one that ends with things "that from a long way off look like flies."
In its violation of the rules we can see the rules. The truly liberating
one for this particular list is the requirement to be a list for some
purpose; since Borges' purpose was to confound us, he was able to make a
list of things never found together on a list. But Borges also violates
a law of scope, putting "stray dogs" and "frenzied" as
entries. Where would we put a frenzied stray dog?

We do have ways of accommodating list items of different scope: Nesting.
Which brings us to Aristotle...

...By way of maps. There's controversy over which of two maps counts as
the first: a Babylonian map from 2,500 BCE and a Turkish one 4,000 years
older. The Turkish one may be merely a picture, not a map, but the Babylonian
one is definitely a map because it shows nested boundaries. Nesting goes
back at least that far. (And, as the chapter explains later, the relationship
between the nesting of geopolitical units and of ideas is not accidental.)

Nesting is a type of lumping and splitting in which one remembers the splits.
Aristotle was the first in our culture to be able to explain this adequately
because he did not assume (as did Plato) that categories of things are themselves
things. He saw what became what we today think of as
a conceptual tree.

We construct conceptual trees the same way we sort our
laundry, making decisions about where each item goes as we split our lumps
and then split those new lumps. Why are we sorting our ideas the same way
we sort our laundry?

To answer this, the chapter now looks at Linnaeus. After explaining Linnaeus'
aims and method, I describe my
visit to the Linnean Society Headquarters. The point is that the Linnaean
system of classification is deeply tied to how we organize physical objects,
including Linnaeus' own use of index cards to arrange the species he'd catalogued.
Start with index cards and you almost inevitably end up with a nested map
("I'll add this card to the Vertebrates, right next to this one for sloths...")
that can also be represented as a tree.

So what would a nested order look like if we didn't have to write it down
on paper? IBM's database of consultants suggests one type of answer. It's
a faceted classification system that can be sorted in any order one wants,
a tree that rearranges itself as we climb through it. IBM is claiming that
the system (created by Endeca in Boston)
saved it $500 million (yes, half a billion) in the first year.

The most remarkable fact is, though, that faceted classification was invented
70 years ago by an Indian librarian before computers were around. The chapter
tells S.R. Ranganathan's story and then comes back to talk about some
more business examples.

We are not going to give up nesting, the chapter concludes, but rather than
trying to construct the tree that represents some domain of knowledge,
we are often better off with systems that can dynamically create trees based
on our interests.

Here's how the current draft ends:

We will continue to find trees useful, although frequently
we will prefer dynamically created trees that mix up the structure of knowledge
in ways that would make Aristotle dizzy. But in the third order, knowledge
doesn't
have a shape. There are just too many useful, powerful and
beautiful ways to make sense of our world…

…Starting with pulling the leaves off the branches, piling them up,
and jumping into them like a kid in autumn's front yard.

I'd tell you about chapter 4 except I only just finished it and so it's
still too sore to touch. But I can say that the overall task of chapter 4
is to introduce the notion of the miscellaneous, and point to four basic
principles of organization that going miscellaneous changes. As it stands,
I discuss how we organize silverware, why Linnaeus shoved too much stuff
into the category "worms," why ambitious tree-like classification
systems such as Getty's Art and Architecture Thesaurus and NewsCodes are
limited by their attempt to be comprehensive, the rise of tagging at sites
like del.icio.us and flickr,
the BBC's new and useful miscellaneousness, why Wikipedia isn't alphabetized,
and then the four principles.

But, there's no telling what will be in the chapter after I unwrite it and
rewrite it several times.

Here's hoping your own life drafting is going well...

Editorial Lint

JOHO is a free, independent newsletter written and produced
by David Weinberger. If you write him with corrections or criticisms, it will
probably turn out to have been your fault.

To unsubscribe, send an email to [email protected]
with "unsubscribe" in the subject line. If you have more than one
email address, you must send the unsubscribe request from the email address
you want unsubscribed. In case of difficulty, let me know: [email protected]

There's more information about subscribing, changing your
address, etc., at www.hyperorg.com/forms/adminhome.html.
In case of confusion, you can always send mail to me at [email protected]. There is no need for harshness
or recriminations. Sometimes things just don't work out between people. .

Dr. Weinberger is represented by a fiercely aggressive legal
team who responds to any provocation with massive litigatory procedures. This
notice constitutes fair warning.

Any email sent to JOHO may be published in JOHO and snarkily
commented on unless the email explicitly states that it's not for publication.

.

The Journal
of the Hyperlinked Organization is a publication of Evident Marketing, Inc.
"The Hyperlinked Organization" is trademarked by Open Text Corp. For information about trademarks
owned by Evident Marketing, Inc., please see our Preemptive Trademarks™™ page
at http://www.hyperorg.com/misc/trademarks.html

This work is licensed under a Creative
Commons License.
