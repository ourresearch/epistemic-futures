---
title: "State of the Computer Book Market, Part 2"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-04-20
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/04/state_of_the_computer_book_mar_3.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# State of the Computer Book Market, Part 2

## Full text

In this installment, I'll look at specific technology trends as demonstrated by book sales. First off, here's another view of our computer book treemap, this time tweaked a bit to show the hierarchical organization of the category database. As before, click on the image to pop up a larger version.

[](http://radar.oreilly.com/archives/Q106treemap11.html)

As you can see, the treemap no longer looks like Iowa from the air, with each category like a farm field of a different size, and its relative health shown by its color. Instead, you can see that the treemap is actually a structure of boxes within boxes, showing the hierarchical organization of the data mart. We've organized the data into six "super-categories" -- Systems and Programming, Web Design and Development, Business Applications, Digital Media Applications, Consumer Operating Systems and Devices, and Other. Within each super-category are sub-categories. For example, Systems and Programming includes programming languages, databases, software engineering, general programming, security, and so on. In total, there are six levels of hierarchy.

Remember that apart from the hierarchical structure, the layout of each block in the treemap is not meaningful -- only the area and the color. The subcategory blocks are laid out by an algorithm that fits them arbitrarily into the required space of the enclosing category block.

Recapping [the big picture from yesterday](http://radar.oreilly.com/archives/2006/04/state_of_the_computer_book_mar.html), you can see that the market's growth has been driven by web design and development -- a sign that "[Web 2.0](http://www.oreillynet.com/go/web2)" is in fact driving a lot of new learning activity. The second-strongest super-category is digital media applications. No surprise there, with the strength of the iPod and digital photography. Traditional consumer operating systems books, long the mass market mainstay, are off 5%. Presumably this will reverse next year when Vista finally ships. With the exception of spreadsheets and a couple of up and coming Web 2.0 areas (search, up 103% on the strength of John Battelle's bestselling book, [The Search](http://battellemedia.com/thesearch/), and geocoding and mapping applications, up 284%), business applications are also trailing the market as a whole. [Aside: next generation mapping and location technologies are the subject of our upcoming [Where 2.0 Conference](http://conferences.oreilly.com/where).]

I'm assuming that most of my readers are more interested in technical topics, so I'm going to limit my deep dive to the Systems and Programming, Web Design and Development, and Digital Media Applications areas. 

**Systems and Programming**

[](http://radar.oreilly.com/archives/Q106treemap21.html)

(Note that because life never neatly fits into hierarchies, some things that you might expect to be part of this category are not. For example, why is PHP not included in Programming Languages? Because it made more sense to include it with Web Design and Development along with related technologies such as Cold Fusion, ASP.Net, and JSP, as it is more of a specialized language, whereas the others are not limited to the web application domain. In order to redress this kind of difficulty, we have other rollups, including one that is specific to programming languages. I'll show that in a minute.)

You can study the visualization at leisure (and feel free to ask specific questions in the comments, if the labels aren't clear in the image), but here are a few of my major takeaways:

  * Microsoft languages (VB and C#) are both showing strong growth, while Java is weakening, continuing a years-long trend. Among the open source languages, Ruby is kicking butt, with Python book sales also growing nicely. Because of the way the data mart is structured, I discuss a better visualization of computer languages in more detail later in this piece. 

  * Database literacy in general continues to rise in importance, consistent with my Web 2.0 assertion that "[data is the new Intel Inside](www.oreillynet.com/pub/a/oreilly/)", and Hal Varian's comment "SQL is the new HTML." Again, more on databases below. 

  * The strengthening of Software Engineering suggests that we're moving out of the run and gun stage of new technology development into a period of consolidation and stability, where building right and to scale are once again becoming important to developers. The category Software Project Management is up 114%, driven in part by the success of Scott Berkun's bestseller, [The Art of Project Management](http://www.oreilly.com/catalog/artprojectmgmt/index.html). "Agile" (up 43%) has replaced "Extreme" (down 41%) as the lightweight development meme du jour. 

  * Linux books have lost a lot of their steam, with the category as a whole off 10%, with books on Red Hat hit particularly hard, off 52%. Other distributions, notably [Ubuntu](http://www.oreilly.com/catalog/ubuntuhks/index.html) and [Knoppix](http://www.oreilly.com/catalog/knoppixhks/index.html), have seen an increase of 37% over the preceding year. As [I've previously observed](http://www.oreillynet.com/pub/wlg/5573), the decline in Red Hat book sales began when they split off Fedora from their main line development, and they have never recovered. 

  * Books on Networking are up significantly, as you might expect, but books on Security are not. That's perhaps a bad sign, given the increased need for secure systems. While still a small category, VoIP is hot, up 96%, led by books from O'Reilly like [Asterisk: The Future of Telephony](http://www.oreilly.com/catalog/asterisk/index.html), [Switching to VoIP](http://www.oreilly.com/catalog/switchingvoip/index.html), and [VoIP Hacks](http://www.oreilly.com/catalog/voiphks/index.html). (Our commitment to this emerging area also shows up in our [Emerging Telephony Conference](http://conferences.oreilly.com/etel).)

**Web Design and Development**

[](http://radar.oreilly.com/archives/Q106treemap3.html)

  * As you might expect, Javascript book sales are up 121%, driven by the new interest in AJAX. (We don't yet track Ajax as a separate category, choosing instead to include it with Javascript.) Manning's [Ajax in Action](http://www.manning.com/crane/) is the top title, followed closely by our [Head Rush Ajax](http://www.oreilly.com/catalog/headra/) and [Ajax Hacks](http://www.oreilly.com/catalog/ajaxhks/). Flash, which introduced the "[Rich Internet Application](http://www.macromedia.com/devnet/ria/)" category, has benefited to some extent, but is up only 12%. 

  * As previously noted, ASP is up 60%. With the latest version, Microsoft has clearly found their stride in the web application development space. PHP is up only 4%, Cold Fusion up 9%, and JSP off 16%. Ruby on Rails shows in the treemap as flat, up 0%. However, this is a visualization artifact. There were no books about Ruby on Rails in the first quarter of last year, so there was a choice of representing the growth as either infinite, or zero. Given that [one book about Ruby on Rails](http://www.oreilly.com/catalog/097669400X/) is delivering nearly the same unit sales as the 20 books that make up the JSP category, nearly one-fifth of the sales of the 61 books in the ASP category, and one-sixth of the 52 books in the PHP category, one would have to conclude that RoR is hot. And of course, there are many more books on the way. 

  * In the web design tools category, Dreamweaver is consolidating its lead, and is the only application in the category whose books show growth, up 11%. 

  * The 30% growth in the Web Services category is driven almost entirely by professional books on topics like [Service Oriented Architectures](http://safari.oreilly.com/JVXSL.asp?x=1&mode=section&sortKey=rank&sortOrder=desc&view=section&xmlid=0131858580&k=20&g=&srchText=Service+Oriented+Architecture&code=&h=0&m=&l=1&j=list&catid=&s=1&b=1&f=1&t=1&c=1&u=1&r=&o=1&n=1&d=1&p=1&a=0&page=0). One could argue that books like [Google Hacks](http://www.oreilly.com/catalog/googlehks2/index.html), [Yahoo! Hacks](http://www.oreilly.com/catalog/yahoohks/index.html), [Amazon Hacks](http://www.oreilly.com/catalog/amazonhks/index.html), [Flickr Hacks](http://www.oreilly.com/catalog/flickrhks/index.html), and [Google Maps Hacks](http://www.oreilly.com/catalog/googlemapshks/index.html), which (in part) cover these "[real world web services](http://www.oreilly.com/catalog/realwws/index.html)", should also be in this category, but we have chosen to include them elsewhere.

**Digital Media Applications**

[](http://radar.oreilly.com/archives/Q106treemap4.html)

The digital media category is up 14% as a whole, led by the phenomenal growth of books on the iPod (up 228%), Digital Photography (general) up 59%, and some specialized areas, like books on the Camera Raw format, up 115%. We also see a slight shift towards books on the integrated CS suite, with sales in that category up 128% vs. 19% for books on Photoshop alone.

**Other Dimensions**

As noted earlier, one artifact of categorization is that, unlike in a [folksonomy](http://en.wikipedia.org/wiki/Folksonomy), books can belong to one and only one category, so that it's possible to sum the categories without counting books more than once. However, we can get around this by creating different dimensions in our data mart. In addition to the category-by-category rollup, we characterize every book by its operating system, and any languages or databases used in the book. So, for example, a book entitled _Game Programming in Java_ would be game programming by category, but Java by language. Or, more to the point, PHP and MySQL books are counted as PHP books for purposes of the category rollup (because we determined that PHP was the main sales driver) but show up as MySQL books for purposes of the database rollup. Similarly, Ruby on Rails books are in a separate category from Ruby language books, but in the language rollup, they are aggregated together. In short, this is the visualization to look at if you're interested in languages. 

With that preamble, here is the treemap for computer languages:

[](http://radar.oreilly.com/archives/Q106plangtreemap.html)

  * ".Net languages" refers to books that cover both C# and VB in the same book. If you give C# credit for all the books in this group, C# now just edges out Java as the most popular computer programming language. And if current growth trends continue, with Java off 6% and C# up 68%, C# will significantly extend its lead next quarter. 

  * Ruby continues its meteoric ascent. In book sales, it is now slightly larger than Python, 80% the size of Perl, and 1/3 the size of PHP. As more publishers jump on the Ruby and Rails bandwagons, we expect these numbers to grow even more significantly next quarter. What's more, when you consider that the Pragmatic Programmers, publishers of the two most popular Ruby books, [Programming Ruby](http://www.oreilly.com/catalog/0974514055/) and [Agile Web Development with Rails](http://www.oreilly.com/catalog/097669400X), have an aggressive direct sales program, including PDF-only downloads, and report that they sold as many copies direct as they sold through retail channels, you could argue that the Ruby book market is now larger than the Perl market, and 2/3 the size of PHP. Of course, those other languages could counter-argue that they have other strong sources of online documentation! 

  * The Python book market is now at 80% of the size of Perl, up from about 2/3 the size of Perl at this time last year. Perl remains in the doldrums as its adherents still wait for Perl 6. 

  * Lisp, Scheme, and Lua, while small, are clearly making something of a comeback. Sales of Lisp books are up 90%, Scheme up 462%, and Lua up 100%. The [folks who are mad at O'Reilly for not publishing a book on Lisp](http://www.paoloamoroso.it/log/040823.html) should be happy about that! (Honestly, we've got nothing against Lisp, and would love to see it take off.) 

  * Actionscript, which is really just Javascript for Flash, should not be overlooked. While Ajax clearly has the mindshare, there are still signs of strong uptake for Flash. And we know from other sources that Flash on mobile may be ready to explode.

Here's the database rollup:

[](http://radar.oreilly.com/archives/Q106dbtreemap.html)

  * The first thing to note is just how underrated "personal" databases are. The market for Access books dwarfs the demand for Oracle books. And even Filemaker remains a strong database category -- and with its new release, it's seen a 76% increase over this time last year. 

  * The SQL server book market is now more than twice the size of the Oracle book market, 50% larger than the MySQL book market, and growing faster than either of them. In fact, both the Oracle and MySQL book markets shrank versus the same period a year ago, with Oracle feeling more of the pain, off 9% to MySQL's negative 2%. DB2 is even worse off, with book sales down 14%. 

  * A surprise to many may be the strong growth of PostgreSQL, up 84% over a year ago. We've also been hearing some signs of growth in the Postgres market from our "alpha geek" radar, with reasons given including better support for geo data, and better handling of very large data sets. New companies like [Greenplum](http://www.greenplum.com) and [EnterpriseDB](http://www.enterprisedb.com) have also brought a little focus to this market. We're updating [our PostgreSQL book](http://www.oreilly.com/catalog/ppostgresql/index.html), and watching this market closely.

Disclaimer: By the terms of our contract with Nielsen, we are only allowed to share this data in the course of promoting our books. Hence the many references to O'Reilly books throughout the text. And hey, that's not a bad deal, as I don't mind promoting our books!

_Tomorrow: how publishers fared._
