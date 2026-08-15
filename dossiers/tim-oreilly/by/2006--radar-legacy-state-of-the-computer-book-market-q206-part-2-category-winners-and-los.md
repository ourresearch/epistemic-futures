---
title: "State of the Computer Book Market, Q206, Part 2:  Category Winners and Losers"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-07-26
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/07/state_of_the_computer_book_mar_4.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# State of the Computer Book Market, Q206, Part 2:  Category Winners and Losers

## Full text

Yesterday, I talked about the [overall market trend in computer books versus last year](http://radar.oreilly.com/archives/2006/07/state_of_the_computer_book_mar_1.html). As always, though, the opportunities and interesting tidbits are in the category visualizations we do. Here's a treemap view of the quarter on quarter differences between Q2 of 2006 and the same period last year:

[](http://radar.oreilly.com/archives/Q2YoYtreemap.html)

As I've previously described in [ Book Sales as a Technology Trend Indicator](http://radar.oreilly.com/archives/2005/04/book_sales_as_a.html), in a Treemap visualization, the size of a square indicates the relative size of the category, and its color indicates the rate of change. A category that is bright green is up significantly. One that is bright red is heading strongly in the other direction. Colors that are more muted show smaller rates of change. As you can see from the controls at the top of the display, we're showing quarter on quarter unit sales compared to the same period in the previous year. (Note: quarters are 13 week periods as closely aligned to calendar quarters as possible. Because Neilsen reports data weekly, and weeks don't match up exactly with quarters, we do a best fit.)

A few high-level observations: 

  * C# book sales continues to gain on Java, with a 49% unit sales increase compared to Java's 10% decrease. 

  * Ruby continues its momentum, and is the fastest-growing programming language in terms of book sales. 

  * Microsoft's new release of SQL Server has continued to drive significant book sales, with that market up 86%. ASP.Net is also on a roll, with book sales up 61%. 

  * It's amazing how many books so simple a device as the iPod can manage to sell!

**Drilling Down Into the Data**

As described in previous postings about our technology trend research, we've organized the Bookscan data into a five level category hierarchy. At the top level, books are grouped into Systems and Programming, Web Development, Digital Media Applications, Business Applications, Consumer Operating Systems and Devices, and Other. In addition, though, because books can only be in one category (tagging style approaches with overlapping categorization don't work when you want to count and compare), we do alternate rollups along dimensions that are of interest to us, such as programming languages, databases, and operating systems. (To understand the difference, consider for example that a Ruby on Rails book will appear in the RoR category, but also needs to be counted as a Ruby language book.)

**Computer Languages**

For this reason, we'll start with some of the alternate rollups, because they give a truer picture of the actual change in key areas. First, let's look at computer languages:

[](http://radar.oreilly.com/archives/Q206YoYproglangtree.html)A 

  * As you can see, the gains of C#, mentioned above, are even more striking than on the primary category treemap. While Java is off 10%, C# is up 78%. And that's without counting books whose programming language shows up as ".Net Languages." These are books that cover both C# and VB.Net. Combining these two categories, the C# book market is now actually a bit larger than the Java book market. 

  * The Ruby book market, up 743% since the same period last year, driven largely by the success of Ruby on Rails, is now almost as large as the Perl book market. Python also continues to gain on Perl, with book sales up 4% to Perl's 4% loss. While PHP continues to show some growth, its rapid growth from previous years also appears to suffer from the incursions of Ruby. 

  * Javascript, driven by the interest in Ajax, is up 171%. It will be really interesting to see the surge grow even faster with new books coming this fall to cover the first new release of Javascript in over six years. 

  * Books on SQL continue to show strong growth, showing the increased importance of databases in today's applications. 

  * C and C++, which have held steady for years, finally seem to be on a bit of a decline.

When I circulated a preliminary draft of this piece to the O'Reilly editors, [chromatic](http://www.oreillynet.com/pub/au/176) wrote: "Ugh, I can only imagine the language FUD that will fly without any further explanation here." So Roger Magoulas, the director of [O'Reilly Research](http://research.oreilly.com), offers some further insight and qualifications about this data:

> The book market being what it is, new, popular books on a topic will distort sales during their first few weeks/months of release. This is why I like to spot interesting areas in the treemap, then look at the time series, and, if time warrants, the individual titles that make up the topic to see what's behind a trend. For example, in Perl, last year a bunch of new versions of popular titles were released and sales have faded in what may be a mostly saturated market. For Ruby and Javascript, new topics (Rails, AJAX) with pent up interest and a few well received titles released in late 2005 and 2006, and, in the case of Ruby, a small base, mean big treemap increases. 
> 
> So does what does what does this mean? Well, it may sound simplistic, but Ruby and Javascript are of increasing interest to developers and have become more important topics. Perl, with not much new and competing with languages reputed to be easier to maintain, read and with better object-oriented support is losing relative interest. Supporting the book trends, perl jobs are down year over year and biggest job growth areas are Ruby, AJAX and Web 2.0.
> 
> I'll point out another example of why book results require careful analysis: The new Microsoft products released in Nov 2005, C# 2005, Visual Studio 2005 and SQL Server 2005 (I'm skipping Visual Basic 2005 - so far gone it doesn't register) show big increases in book sales. When we look at the job data we don't see any corresponding changes. We also don't see much overlap between Windows and other development environments (e.g., ~14% of Windows .Net oriented job postings also include Java). So, our conclusion is that the new version - the first in five years - generated a lot of developer interest in Windows shops, but doesn't represent a trend towards increased use of Microsoft products.

(The job data that Roger refers to comes from analysis of job postings from all of the online job sites, which we receive as part of a data sharing arrangement with [SimplyHired](http://www.simplyhired.com). Just as we do with the computer book market, we've built a data warehouse for technical job data and trends, which helps to put some "hard numbers" into the O'Reilly Radar.)

[Andrew Odewahn](http://www.oreillynet.com/cs/catalog/view/au/603) added: "There are 9 books in our Ruby + RoR categories. The two biggest, _[Programming Ruby](http://www.oreilly.com/catalog/0974514055/index.html)_ and _[Agile Web Development With Rails](http://www.oreilly.com/catalog/097669400X/index.html)_ , account for over 75% of the total market. For Perl, there are 37 titles, and the top 2 titles (_[Learning Perl](http://www.oreilly.com/catalog/learnperl4/index.html)_ and _[Programming Perl](http://www.oreilly.com/catalog/pperl3/index.html)_) account for about 33% of the market.... as chromatic suspects, [the Ruby book market is] much more concentrated -- the bulk of the market goes to a few superstars. It remains to be seen if it can support the rich and long lasting ecosystem of perl." This question will be tested in the second half of the year, as a flood of new Ruby and Ruby-on-Rails books hit the market.

Looking at the sales rate of the category bestsellers is also telling. The top Ruby language book, _Programming Ruby_ , released in October 2004, sold 3715 units in Bookscan-reporting stores during the quarter, while _Learning Perl_ , the top Perl book, whose fourth edition was published in July 2005, sold 2232 copies, and _[Learning Python](http://www.oreilly.com/catalog/lpython2/index.html)_ , the top Python book, published in December 2003, sold 1903 copies. (_Agile Web Development with Rails_ sold even more copies than _Programming Ruby_ , but it seems fairer to compare the books on the actual language.)

  
**Databases**

Looking at the Database rollup, we again see the strength of SQL Server, the decline of Oracle book sales, and that while MySQL is still a much larger category than Postgres, Postgres is showing some curious strength. This is one of the things that treemap visualizations are good for. Small, bright green categories stand out, and you can start paying closer attention. (Ruby also showed bright green while it was still a tiny category before its remarkable surge over the past year.) We also see the continuing popularity of personal databases like Access and Filemaker.

[](http://radar.oreilly.com/archives/Q206YoYdbtree.html)

**Operating Systems**

The operating system rollup shows that, absent significant new releases, there's not a lot of action in operating system books. The only categories showing strength are Cisco, up 31%, and Blackberry, up 105%. (The tiny bright-green dot in the lower right corner is books on Juniper, up 76%, so while the market is still small, Cisco doesn't have it entirely to itself.) 

Mac OS X's 12% YoY decline should not be seen as a sign that the OS is falling behind. During the second quarter of last year, many of the books on the new Tiger release were still in the full flush of their initial sales. We expect the Mac OS X category to revive significantly with new releases this fall, while Windows will need to survive yet another series of delays. As noted in previous postings on the subject, books that cover applications for both Mac and Windows are categorized as "Common Desktop.)

[](http://radar.oreilly.com/archives/Q206YoYopsystree.html)

**Systems and Programming Category View**

Returning to the category by category view, let's take a closer look at the top level systems and programming category:

[](http://radar.oreilly.com/archives/Q206YoYsysprogtree.html)

Here you can see some of the changes in the software engineering areas. Agile programming continues to be a hot topic, as does software project management. The fact that patterns books are off 10% is an artifact of a single book, _[Head First Design Patterns](http://www.oreilly.com/catalog/hfdesignpat/index.html)_ , which first came out last year and drove the category to new heights. The book is still selling extremely well, but is not in the first flush of its youth.

Other categories that are worthy of note are data warehousing, up 44 %, and data analysis, up 174%. We believe that [data is the Intel Inside]() of the next generation of computer applications, and that as more people realize this, advanced data management and visualization categories will continue to become more important.

Finally, we note the continued growth of interest in books on Linux distributions other than Red Hat, and the dog that continues to surprise us by not barking in the night. Despite all the obvious need for better security practices, security books remain in the doldrums.

**Web Design and Development**

Here's a closer look at the top level categories in the Web Design and Development area:

[](http://radar.oreilly.com/archives/Q206YoYwebappstree.html)

Besides the continued strength of ASP.Net, which was noted yesterday, what's striking here is that there are a number of categories that had been written off by publishers after early efforts failed, but are now making a comeback, namely web services, blogging, and podcasting. I'll also note that JBoss books are starting to make a mark. Finally, I'll note that the 0% showing for AJAX is an artifact. There were no AJAX books a year ago, so there's nothing to generate a rate of change. It is not zero, but immeasurably large.

**Digital Media Applications**

Next, let's take a look at Digital Media Applications:

[](http://radar.oreilly.com/archives/Q206YoYDigMedTree.html)

Here, the most noteworthy changes are the huge upsurge in books on the iPod, which has turned out to be a winning category, with huge numbers of low-priced books sold. It's also worth noting that an increasing number of books cover the Adobe CS suite rather than just Photoshop, although the number is still very small by comparison. We also note the surge in books on animation, and in general books on digital music (that's the bright green vertical bar on the lower right edge, up 497%.) Finally, we note the success of the new Premiere Elements, a lightweight version of Adobe Premiere. 

Tomorrow: [How Publishers Fared](http://radar.oreilly.com/archives/2006/07/state_of_the_computer_book_mar_5.html).
