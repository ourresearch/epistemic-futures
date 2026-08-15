---
title: "State of the Computer Book Market, Q306, Part 2"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-11-06
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/11/state_of_the_co_1.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# State of the Computer Book Market, Q306, Part 2

## Full text

Last week, I talked about the overall [state of the computer book market](http://radar.oreilly.com/archives/2006/10/state_of_the_co.html). But most of our readers don't care about the publishing business. They care about the technologies we cover. Here's where we get to the meat: category visualizations and trends showing which technologies are winning and which are losing in the book market. Here's a treemap view of the quarter on quarter differences between Q3 of 2006 and the same period last year: 

[](http://radar.oreilly.com/archives/Q306YoYTreemap21.html)

As I've previously described in [ Book Sales as a Technology Trend Indicator](http://radar.oreilly.com/archives/2005/04/book_sales_as_a.html), in a Treemap visualization, the size of a square indicates the relative size of the category, and its color indicates the rate of change. A category that is bright green is up significantly. One that is bright red is heading strongly in the other direction. Colors that are more muted show smaller rates of change. For this image, I've also dragged a slider to show the enclosing category hierarchy, so only the top level categories are proportionally sized. 

As you can see from the controls at the top of the display, we're showing quarter on quarter unit sales compared to the same period in the previous year. (Note: quarters are 13 week periods as closely aligned to calendar quarters as possible. Because Neilsen reports data weekly, and weeks don't match up exactly with quarters, we do a best fit.) 

A few high-level observations: 

  * Web Design and Development has been the most substantial bright spot in the market, with 22% year-on-year growth in this category. This might well be expected in a period in which Web 2.0 is the buzzword du-jour. In addition to breaking topics like Ruby on Rails, AJAX, Javascript, and ASP.Net, there's been nice growth in books on web design and web page creation. Books on blogging and podcasting have also finally caught on, after several prior false starts. 
  * Microsoft's server release earlier in the year is still driving strong sales of books on C#, Visual Basic, and SQL Server. However, other database topics are also up modestly. 
  * The growth in books on digital photography has slowed considerably. If not for the inclusion of the iPod category, the Digital Media supercategory would be flat. 
  * The hardest-hit part of the market was books on consumer operating systems, down 17% from the same period a year ago. 
  * The professional development and administration segment was down 2%, but might have been worse but for the strong performance of Microsoft languages, Python, Ruby, software project management, and database topics.

**Drilling Down Into the Data**

As described in previous postings about our technology trend research, we've organized the Bookscan data into a five level category hierarchy. At the top level, books are grouped into Systems and Programming, Web Development, Digital Media Applications, Business Applications, Consumer Operating Systems and Devices, and Other. In addition, though, because books can only be in one category (tagging style approaches with overlapping categorization don't work when you want to count and compare), we do alternate rollups along dimensions that are of interest to us, such as programming languages, databases, and operating systems. (To understand the difference, consider for example that a Ruby on Rails book will appear in the RoR category, but also needs to be counted as a Ruby language book.) 

**Computer Languages**

For this reason, we'll start with some of the alternate rollups, because they give a truer picture of the actual change in key areas. First, let's look at computer languages: 

[](http://radar.oreilly.com/archives/Q306YoYplangtree.html)

  * Ruby has continued to grow apace, although its 255% growth rate is off last quarter's torrid 687% increase! Interestingly, PHP also picked up some steam, up 11% vs. last quarter's 6% YoY increase. Python's 27% YoY gain, up from last quarter's 6% gain, shows even more strength. In short, while Ruby has become the language of choice for many web startups, PHP and Python are both far from out of the game. With the addition of web frameworks like Django and Pylons, Python is becoming a real contender as a first rate language for Web 2.0 applications. (Google's commitment to the language doesn't hurt either, as Google is a hiring magnet, and Python skills are much in demand.) 
  * The decline of Java book sales has accelerated, while C# books have continued their steady increase. When you aggregate books on both C# ".Net Languages" (books that cover both C# and VB.Net), the C# book market is now about 12% larger than Java. (Of course, some of those .Net Languages book purchasers could be buying them for their coverage of VB.) 
  * Javascript book sales are up 152% -- actually less than we expected given the new release of JavaScript this fall. If you aggregate sales of ActionScript books with JavaScript (and ActionScript is, after all, a dialect of JavaScript), it is now the 2nd largest language (after Java), in terms of book sales. (It's third if you aggregate the ".Net languages" category entirely to VB rather than to C#. See the note above about Java vs. C#.) 
  * While sales are still tiny, we see signs that developers are taking a second look at languages such as Lisp and Scheme. Specialized languages such as MDX (used with SQL Server) and Lua (used for game programming) are also showing growth.

**Databases**

Looking at the Database rollup, we again see the strength of SQL Server, and the decline of Oracle book sales. MySQL books have also seen decent growth again, after a slower period. And the curious surge in PostgreSQL, which we noted last quarter, seems to have fallen off. 

[](http://radar.oreilly.com/archives/Q306dbtree.html)

Note: due to the press of my travel schedule, and needing to grab screenshots at odd times, this treemap and the next are not dated precisely on the quarter boundary, but two weeks later. (I didn't manage to snap them before new data was added, and while resetting the date is possible, the differences aren't material.) 

**Operating Systems**

The operating system rollup shows that, absent significant new releases, there's not a lot of action in operating system books. We do see some strength in Linux, principally driven by books on new distributions like Ubuntu. Books on blackberry also remain strong. 

[](http://radar.oreilly.com/archives/Q306opsystree.html) />

**Systems and Programming Category View**

Returning to the category by category view, let's take a closer look at the top level systems and programming category: 

[](http://radar.oreilly.com/archives/Q306YoYProgTree.html)

Much as was the case with Design Patterns last quarter, the strength of the project management category is really a testament to the strength of one book, Scott Berkun's [Art of Project Management](http://www.oreilly.com/catalog/hfdesignpat/index.html). Similarly, the user interface category jump is primarily driven by Jennifer Tidwell's [Designing Interfaces](http://www.amazon.com/exec/obidos/ASIN/0596008031), also from O'Reilly. 

Two categories that surged, Data Warehousing and Data Analysis, should be no surprise to those who've followed our "data is the Intel inside" hypothesis. Wiley (and to a lesser extent McGraw Hill) has done a good job bringing books to market on this topic. (While we use data warehousing and analysis here at lot in our Radar group, and suggested this topic to our publishing group several years ago, we unfortunately never gave it enough priority. Shame on us. We did better in the Data Analysis category, with our bestselling [Information Dashboard Design](http://www.amazon.com/exec/obidos/ASIN/0596100167), the #3 book in the category behind [The Little SAS Book](http://www.amazon.com/exec/obidos/ASIN/1590473337) and Tufte's [Beautiful Evidence]().) 

The 80% growth in the Agile category is also one that shows the impact of Web 2.0 on development practices. Bestselling books include Microsoft Press's [Agile Project Management with Scrum](http://www.amazon.com/exec/obidos/ASIN/073561993X) and Pearson's [Agile Software Development with Scrum](http://www.amazon.com/exec/obidos/ASIN/0130676349). 

Strength in the Cisco category is primarily driven by certification books, dominated by Pearson's Cisco Press imprint. Similarly, the Microsoft programming category is primarily driven by MCTS certification books, and is dominated by Microsoft Press. 

Finally, we see the continued interest in Linux distributions other than Red Hat, most notably Ubuntu, a fact that has been [previously discussed on this blog](http://radar.oreilly.com/tag/ubuntu). But also notable is the big jump in the category we label "proprietary Unix," but should probably be renamed "Solaris", because there are no other variants selling any books to speak of. Sun's move to open source Solaris seems to be giving it nice traction in the marketplace. 

**Web Design and Development**

Here's a closer look at the top level categories in the Web Design and Development area: 

[](http://radar.oreilly.com/archives/Q306YoYwebtree.html)

As might be expected, the AJAX category is hotly contested, with O'Reilly's [Head Rush Ajax](http://www.amazon.com/exec/obidos/ASIN/0596102259) nudging out Manning's trailblazing [Ajax in Action](http://www.amazon.com/exec/obidos/ASIN/1932394613) for the top spot. O'Reilly's [AJAX Hacks](http://www.amazon.com/exec/obidos/ASIN/0596101694) and Wrox's (Wiley's, that is) [Professional AJAX](http://www.amazon.com/exec/obidos/ASIN/0471777781) are also doing very well. 

(As I did last quarter, I'll note that the 0% showing for AJAX is an artifact. There were no AJAX books a year ago, so there's nothing to generate a rate of change. It is not zero, but immeasurably large.) 

Ruby on Rails, another relatively new category, has also become very competitive. The Pragmatic Programmers' initial groundbreaking book, [Agile Web Development with Rails](http://www.amazon.com/exec/obidos/ASIN/097669400X), which once had the market to itself, now competes with at least three other titles, including the Prags' own [Rails Recipes](http://www.amazon.com/exec/obidos/ASIN/0977616606) and Manning's [Ruby for Rails](http://www.amazon.com/exec/obidos/ASIN/1932394699) O'Reilly's [Ruby on Rails: Up and Running](http://www.amazon.com/exec/obidos/ASIN/0596101325) has taken the top spot, but the book is too new to know whether or not its sales level will stick. 

Wrox's resurgence in Microsoft programming categories under Wiley's management can be seen in the ASP category, where [Professional ASP.Net 2.0](http://www.amazon.com/exec/obidos/ASIN/0764576100) is the category leader, with Microsoft's [Programming ASP.Net 2.0](http://www.amazon.com/exec/obidos/ASIN/0735621764) and Apress's [Pro ASP.Net 2.0 in C#](http://www.amazon.com/exec/obidos/ASIN/1590594967) duking it out for a distant second place. 

Blogging and Podcasting have hit the mainstream, as evidenced by the fact that the ubiquitous "For Dummies" books have now taken the dominant spot in each category. 

**Digital Media Applications**

Next, let's take a look at Digital Media Applications: 

[](http://radar.oreilly.com/archives/Q306YoYdigmedtree.html)

Perhaps most striking in the Digital Media category is the shift from titles on Photoshop to titles on digital photography technique. (It's striking, but not surprising. After all, it's been nearly a year and a half since the release of Photoshop CS 2.) Once again, the mainstreaming of digital photography is shown by the huge sales of [Digital Photography for Dummies](http://www.amazon.com/exec/obidos/ASIN/0764598023), which outsells the #2 title in this category by nearly 3:1. However, what's also interesting are the strong sales of "niche" books, from those aimed at professionals like O'Reilly's [The DAM Book: Digital Asset Management for Photographers](http://www.amazon.com/exec/obidos/ASIN/0596100183) to those aimed at consumers, like Thomson's [Digital Wedding Photography](http://www.amazon.com/exec/obidos/ASIN/1592004717). 

Tags: [books](http://radar.oreilly.com/tag/books) [bookscan](http://radar.oreilly.com/tag/bookscan) [hard numbers](http://radar.oreilly.com/tag/hard_numbers)

[Sphere It](http://www.sphere.com/search?q=sphereit:http://radar.oreilly.com/archives/2006/11/state_of_the_co_1.html "Related Blogs & Articles")

## Trackback Pings

TrackBack URL for this entry:  
http://blogs.oreillynet.com/mt/trackback/731
