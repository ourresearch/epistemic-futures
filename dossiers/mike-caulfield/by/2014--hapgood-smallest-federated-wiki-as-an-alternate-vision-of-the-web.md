---
title: "Smallest Federated Wiki as an Alternate Vision of the Web"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-06-04
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/06/04/smallest-federated-wiki-as-an-alternate-vision-of-the-web/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Smallest Federated Wiki as an Alternate Vision of the Web

## Full text

The web is not going away. And you’ll probably never see anyone in your immediate family ever uttering the phrase “Smallest Federated Wiki”.

But after three weeks of using [Smallest Federated Wiki](<http://www.wired.com/2012/07/wiki-inventor/>), a reimagining of the wiki (and really, of the web) by wiki inventor Ward Cunningham and a cadre of incredibly talented coders, I’m struck by how SFW undermines some of the basic premises of the web.

And I’m even more surprised how good that feels.

### Writing in Hypertext

_Quoted Text_

_I had done a great deal of writing as a youth, and re-writing, and the intricacy of taking ideas and sentences and trying to arrange them into coherent, sensible, structures of thought struck me as a particularly intricate and complex task, and I particularly minded having to take thoughts which were not intrinsically sequential and somehow put them in a row because print as it appears on the paper, or in handwriting, is sequential. There was always something wrong with that because you were trying to take these thoughts which had a structure, shall we say, a spatial structure all their own, and put them into linear form._

— Ted Nelson, inventor of modern hypertext. [source ](<http://www.ics.uci.edu/%7Eejw/csr/nelson_pg.html> "http://www.ics.uci.edu/~ejw/csr/nelson_pg.html")

.. 

It’s been 20 years since MOSAIC and over 50 years since since Ted Nelson invented computer-based hypertext and we are still not writing in hypertext.

We **think** we are writing in hypertext. But look at what Nelson is talking about. Does the composition process he was trying to create sound like what you do when you compose? Are you constructing “spatially”, in two dimensions?

In all likelihood, you’re not. You’re linking pages to one another, but you aren’t doing anything like Nelson is describing here.

And you really can’t. Because the dominant paradigm of the web is that you are on one page at any given time. You don’t go into WordPress and work on three pages at once, fluidly shifting bits and pieces until a multi-page networked structure emerges.

Rather, almost all web writing begins with an idea that we are going to write Page X. And Page X can absolutely drop into a web of links to page Y and Z. But we are never invited to change Page Y and Z as a response to the existence of Page X. Or to write a concise and specialized version of Page Y uniquely tuned to the context of Page X.

That’s using links, but it’s not the spatial composition that Nelson is referencing. And strangely, it’s less than we had with some of the Hypercard variants of the 80s and 90s.

As Nelson himself said, the current web is [FTP with lipstick](<http://history-computer.com/Internet/Birth/Nelson.html>). It’s a works cited page with hidden links to other documents. But it ain’t hypertext.

Smallest Federated Wiki solves this through a focus on allowing page-refactoring across entire sites, along with features that make a pass at Nelson’s dream of a pool of reusable bits.

How does this work? Multiple columns with draggable text and data elements you can pull between pages as you build out your spatial text.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2014/06/refactoring1-sm.gif>)

Speaking of columns…..

### From Jump Links to Columns

Quoted Text 

_Project Xanadu is a much-misunderstood initiative to create a different kind of computer world, based on a different kind of electronic document –_

_**PARALLEL PAGES, VISIBLY CONNECTED!**_

_We should have stressed that point from the beginning._

— Ted Nelson’s Project Xanadu, [source ](<http://xanadu.com> "http://xanadu.com")

.. 

We call links internal to a page “jump links”, but really all links are jump links.

Worse yet, they are “blind jump links”. You’re reading along in a page, there’s a link to another page, providing (supposedly) additional context.

But when you click it, it doesn’t provide additional context. It provides a *new* context. And if in that new page there is yet another link, you are whisked again into a new location, usually reading text only marginally related to what the link was supposed to provide.

Every page, because it is a complete and total page (or as Nelson would explain, because it is essentially an FTP’d document) can’t truly supplement context. It has to own the context. Instead of connections, we get teleportation.

If you want connection — if you want to supplement context rather than replace it — you need parallel pages.

Parallel pages — or, in the case of SFW, pages laid out in columns — allow us to read spatially. New pages open to the right, while preserving your current context.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2014/06/multi-column.png>)

This seems small. What you learn after a couple weeks of writing and reading in SFW is it is anything but.

### From Unmixable Layout to Mashable Data

HTML is at heart a publishing format, one that does very well with static text. It’s a great format for a snapshot.

But when we add data to text, we either lock it into the document as an output (a chart or other output format) or, if we want to keep it editable, we embed it from a third-party application.

In other words, the process of publication becomes a process of freezing our data in place or exiling it elsewhere.

SFW has an elegant solution to this: **everything** becomes data. Your paragraphs are a little nugget of JSON, with a wrapper that tells the page “This data should be displayed as a paragraph.”

Sample JSON Data 
    
    
    {"type":"add","item":
      {
       "type":"paragraph",
       "id":"e824fa0816b71e50",
       "text":"The web is..."},
    "id":"e824fa0816b71e50","date":1401835049316},

.. 

Outside of the fact that that text can now be mashed and processed in any way you choose (write a Markdown plugin if you want to write paragraphs in Markdown), the system allows all types of data to become first class citizens of the page in a way they have never been. You have the capability to write or use interpreters for any microformats or domain-specific languages you use, from languages that communicate with remote sensors to ones that produce complex visualizations.

As a simple example, adding the MathTEX code
    
    
    \(\int\frac{d\theta}{1+\theta^2}= 
    \tan^{-1} \theta+C\)

into a the MathJax plugin adds this to the JSON representation:
    
    
    {"type":"mathjax",
     "id":"b76788f7a723b3be",
     "text":"\\(\\int\\frac{d\\theta} {1+\\theta^2}= \n\\tan^{-1} \\theta+C\\)"},

Which displays on the page like so:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2014/06/equation.png>)∫dθ1+θ2=tan−1θ+C

Images get stored not as external references, but as embedded JSON data that can follow the page. Graphs carry the data that generate them behind them. Calculator plugins define and compute data across pages.

Here’s me realizing it should be BETA not THETA and fixing the equation:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2014/06/equation-32-nodither.gif>)

I’ve flubbed up the explanation of this before (Jim will remember my peculiar ByteBeat obsession), but what’s notable here is your data travels *with the page*, and can be made to produce any appropriate format. This is what we mean when we say _data is a first class citizen_ in SFW.

Even better, all of these objects inherit the dragability, edit histories, and forkability of the text elements of a page. When you fork a page,you don’t fork something pointing to a bunch of references you can’t edit. You get the whole enchilada, not a pointer to one.

### Parallel Revisions

One of the big sticking points people have with the SFW interface is the bottom bar of revision history.

Each icon represents a specific action in the page history. Click any edit, and it opens up a copy of the page at that point in time.

That’s pretty standard for a wiki. But here’s where it gets pretty neat. First, a quick scan of the set of tiles shows you the history of the page concisely.

You can see the sequence and amounts of adds, edits, and deletes. If the page has had multiple editors, you can see how it was passed back and forth, and who did the bulk of editing, or even which editor tended to add, and which to delete, all at a glance.

Hovering over the edits gives you an even more detailed view of the sequence of changes. As you hover over each icon, each parallel page scrolls to the edit in question and highlights it.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2014/06/revisions.gif>)

It’s not quite [Heavy Metal Umlaut](<http://jonudell.net/udell/gems/umlaut/umlaut.html>) yet, but it’s getting there, and it’s already one of the slickest approaches to revision scanning I’ve seen. (Sorry for the small size image, but this page was getting too download heavy).

### Federation over Collaboration

It’s perhaps weird that I would cover the federation aspect of the Smallest Federated Wiki last in this article. But I have two good reasons for that.

The first is it is really hard to grasp what federation looks like in wiki-land without trying it.

The second is that federation is really a smaller idea in a larger vision. The core problem addressed in Smallest Federated Wiki is how to make a wiki that resists calcification.

Parallel columns, draggable elements, and revision features make reorganization cheap and attractive.

The JSON basis prevents fossilization of data elements, and allows an easy route to bring dynamic third party material into the site.

And federation’s secret weapon is diversity as an evolutionary strategy.

But this is perhaps enough of a post for today. The point here is to _just try it_. Explaining why you’d want to do this stuff is like explaining why you’d want to browse web pages in 1993.

Get started in the [sandbox](<http://sandbox.fed.wiki.org/view/welcome-visitors>). Put some time into this — this is a mental stretch, but it is worth it. Then talk to me if you want to go further.
