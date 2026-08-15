---
title: "Pipes and Filters for the Internet"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-02-07
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/02/pipes_and_filte.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Pipes and Filters for the Internet

## Full text

Yahoo!'s new [Pipes](http://pipes.yahoo.com/) service is a milestone in the history of the internet. It's a service that generalizes the idea of the mashup, providing a drag and drop editor that allows you to connect internet data sources, process them, and redirect the output. Yahoo! describes it as "an interactive feed aggregator and manipulator" that allows you to "create feeds that are more powerful, useful and relevant." While it's still a bit rough around the edges, it has enormous promise in turning the web into a programmable environment for everyone.

Before I get into the details of what it is and how it works, I want to give a little background on why I'm so excited. This is something I've been waiting nearly ten years for.

Back in the summer of 1997, at our first Perl conference, [Jon Udell](http://207.22.26.166/) (who is [among the most prescient of technology visionaries](http://www.oreilly.com/pub/a/oreilly/ask_tim/1999/pracintgr_preface.html) and the prototype for my concept of the alpha geek) gave a talk that electrified me. Jon expressed a vision of web sites as data sources that could be re-used, and of a new programming paradigm that took the whole internet as its platform. This was well before web services were au courant. We don't have a record of that talk, but a few years later, in a [keynote at the 8th International Python conference](http://www.oreillynet.com/pub/a/network/2000/02/02/zopekeynote.html), he said much the same thing:

> To a remarkable degree, today's Web already is a vast collection of network services. So far, these services are mainly browser-oriented. My browser "calls" a service on Yahoo to receive a page of a directory. Or it "calls" a service on AltaVista to receive a page of search results.   
> 
> 
> One of the nicest things about the Web, however, is that browsers aren't the only things that can call on the services offered by websites. Programs written in any URL-aware language -- including Python, Perl, JavaScript, and Java -- can "call" these Web services too. To these programs, the Web looks like a library of callable components. What's more, it's very easy to build new Web services out of these existing components, by combining them in novel ways. I think of this as the Web's analog to the UNIX pipeline.

I picked up Jon's theme in my own keynote at JavaOne that year, a talk entitled [The Network Really is the Computer](http://www.oreillynet.com/pub/a/network/2000/06/09/java_keynote.html):

> I want to talk about the implications for that marvelous aspect of the fundamental UNIX design: the pipe, and its ability to connect small independent programs so that they could collectively perform functions beyond the capability of any of them alone. What is the equivalent of the pipe in the age of the web? ...This is one of the REALLY BIG IDEAS that is going to shape the next five or ten years of computing.

Now, many of you may think that mashups are already the equivalent of pipes. They certainly satisfy many of the requirements that Jon and I were talking about back in 2000. They allow developers to use two websites in a way that their creators didn't quite intend, which extends them and makes them more useful. But mashups have generally been limited in their scope, pairwise combinations with their output typically being simply another web site. That is, the pipes and filter mechanism had not been generalized. 

But perhaps more significantly, to develop a mashup, you already needed to be a programmer. Yahoo! Pipes is a first step towards changing all that, creating a programmable web for everyone.

Using the Pipes editor, you can fetch any data source via its RSS, Atom or other XML feed, extract the data you want, combine it with data from another source, apply various built-in filters (sort, unique (with the "ue" this time:-), count, truncate, union, join, as well as user-defined filters), and apply simple programming tools like for loops. In short, it's a good start on the Unix shell for mashups. It can extract dates and locations and what it considers to be "text entities." You can solicit user input and build URL lines to submit to sites. The drag and drop editor lets you view and construct your pipeline, inspecting the data at each step in the process. And of course, you can view and copy any existing pipes, just like you could with shell scripts and later, web pages.

Now, while I say Pipes opens up mashup programming to the non-programmer, it's not entirely for the faint of heart. At minimum, you need to be able to look at a URL line and parse out the parameters (so, for example, you can use Pipes' "URL builder" module to construct input to a site's query function), understand variables and loops, and so on. But you don't really need to know these things to get started.

Pipes can simply be used as a kind of "power browser." (something Dale Dougherty has been looking for even longer than I've been looking for pipes and filters for the web). For example, you can build a custom mashup to search for traffic along your own routes every morning, or a news aggregator that searches multiple sites for subjects you care about. All you have to do is start with one of the existing modules. (And presumably, once pipes is opened to the public tonight, there will be many more, as anyone can publish their own modules.)

Brady Forrest is writing a separate post to dig more deeply into the how-to side. But to get the concept across, let's look at [Aggregated News Alerts](http://pipes.yahoo.com/pipes/fELaGmGz2xGtBTC3qe5lkA/), a pipe that aggregates news alerts from bloglines, findory, Google News, Microsoft Live News, and Yahoo! News.

A preview of the pipe's output is shown below, after I've used the text input field to search for Linux:

[](http://radar.oreilly.com/archives/NewsAggregator.html)

But I don't just get to look at this output on the pipes web site. I can pipe it further, as an RSS feed in its own right, I can send it to my feed aggregator of choice, and I can even get results by email or SMS.

OK. That's nice. But what's nicer is that even if I'm not much of a programmer, I can start to copy and paste to modify this pipe even further. I start by cloning the pipe. Now I have my own copy to play with. I can start by subtracting some feeds, and adding some others. For example, if I like to search for open source topics, I might want to subtract some of the general news sources and instead point to news sources like [slashdot](http:///www.slashdot.org) and the [O'Reilly Network](http://www.oreillynet.com). 

It's not quite as easy as drag and drop. I have to understand the query syntax of the sites I want to search, and modify the URL-builder modules to use that syntax rather than the syntax of the sites I'm replacing. But it's relatively easy once you play around a bit.

What's really lovely about this is that, like the Unix shell, Pipes provides a gradual introduction to web programming. You start out by modifying someone else's pipe just a bit, then branch out into something more adventurous.

As I wrote in [Unix Power Tools](http://safari.oreilly.com/0596003307/upt3-CHP-1-SECT-2) back in 1993:

> It has been said that Unix is not an operating system as much as it is a way of thinking. In The UNIX Programming Environment, Kernighan and Pike write that at the heart of the Unix philosophy "is the idea that the power of a system comes more from the relationships among programs than from the programs themselves."   
> 
> 
> Most of the nongraphical utility programs that have run under Unix since the beginning, some 30 years ago, share the same user interface. It's a minimal interface, to be sure — but one that allows programs to be strung together in pipelines to do jobs that no single program could do alone. 
> 
> Most operating systems — including modern Unix and Linux systems — have graphical interfaces that are powerful and a pleasure to use. But none of them are so powerful or exciting to use as classic Unix pipes and filters, and the programming power of the shell.
> 
> A new user starts by stringing together simple pipelines and, when they get long enough, saving them for later execution in a file (Section 1.8), alias (Section 29.2), or function (Section 29.11). Gradually, if the user has the right temperament, he gets the idea that the computer can do more of the boring part of many jobs. Perhaps he starts out with a for loop (Section 28.9) to apply the same editing script to a series of files. Conditions and cases soon follow and before long, he finds himself programming.
> 
> On most systems, you need to learn consciously how to program. You must take up the study of one or more programming languages and expend a fair amount of concentrated effort before you can do anything productive. Unix, on the other hand, teaches programming imperceptibly — it is a slow but steady extension of the work you do simply by interacting with the computer.
> 
> Before long, you can step outside the bounds of the tools that have already been provided by the designers of the system and solve problems that don't quite fit the mold. This is sometimes called hacking; in other contexts, it is called "engineering." In essence, it is the ability to build a tool when the right one is not already on hand. 

I think that's a pretty good description of Pipes as well. It democratizes web programming, making it easier for people to have more control over the internet information services they consume, and providing a general-purpose platform for interacting with sites that is more powerful than the browser or feed-reader alone, but without requiring full programming skills.

Pipes still has a ways to go in the ease of use department. Parsing and filtering a stream of xml isn't as easy as parsing Unix's ascii stdout. And the user interface of the editor itself needs a lot of work to make it easier to use. But it's a great start. Kudos to Pasha Sadri and the rest of the Pipes team!

Tags: [pipes](http://radar.oreilly.com/tag/pipes) [web 20](http://radar.oreilly.com/tag/web_20) [yahoo](http://radar.oreilly.com/tag/yahoo)

[Sphere It](http://www.sphere.com/search?q=sphereit:http://radar.oreilly.com/archives/2007/02/pipes_and_filte.html "Related Blogs & Articles")

## Trackback Pings

TrackBack URL for this entry:  
http://blogs.oreillynet.com/mt/trackback/1751
