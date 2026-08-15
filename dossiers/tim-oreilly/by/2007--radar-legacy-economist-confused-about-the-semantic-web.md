---
title: "Economist Confused About the Semantic Web?"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-09-18
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/09/economist-confused-about-the-s.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Economist Confused About the Semantic Web?

## Full text

Jimmy Guterman made [brief reference](http://radar.oreilly.com/archives/2007/08/the_economist_o.html) recently to [an Economist story](http://economist.com/displaystory.cfm?story_id=9716955) that described three companies as "semantic web companies." While flattered by the attention (all three are O'Reilly investments -- I am a personal investor in Rael Dornfest's [ValuesOfN](http://www.valuesofN.com), creator of the [Sandy](http://www.iwantsandy.com) application described in the story, and [OATV](http://www.oatv.com) is an investor in both [Wesabe](http://www.wesabe.com) and [Tripit](http://www.tripit.com)), I am confused at hearing the semantic web characterization. 

The article notes: 

> The semantic web is so called because it aspires to make the web readable by machines as well as humans, by adding special tags, technically known as metadata, to its pages. Whereas the web today provides links between documents which humans read and extract meaning from, the semantic web aims to provide computers with the means to extract useful information from data accessible on the internet, be it on web pages, in calendars or inside spreadsheets

The article then goes on to describe how RDF, OWL, and SparQL are the foundational technologies of the Semantic Web. I'm with them so far. But as far as I know, none of the three companies profiled are based on these Semantic Web technologies. In short, the Economist is using "the semantic web" as an equivalent to "this application seems able to do things that we used to think took a person to do." 

That's not a bad concept, and it's certainly aligned with the _vision_ of the semantic web. And ultimately, no one will care what kind of technology is under the covers. 

But I want to return to some ideas I outlined in a previous post entitled [Different approaches to the semantic web](http://radar.oreilly.com/archives/2007/03/different_appro_1.html). There's no question in my mind that applications are becoming more intelligent. But there are lots of questions about the right way to get there. The Semantic Web (capitalized to refer to the suite of official technologies) is about developing languages, if you will, with which we can encode meaning into documents in such a way that they are more accessible to computers. 

By contrast, I've argued that one of the core attributes of "web 2.0" (another ambiguous and widely misused term) is "collective intelligence." That is, the application is able to draw meaning and utility from data provided by the activity of its users, usually large numbers of users performing a very similar activity. So, for example, collaborative filtering applications like Amazon's "people who bought item this also bought" or last.fm's music recommendations, use specialized algorithms to match users with each other on the basis of their purchases or listening habits. There are many other examples: digg users voting up stories, or wikipedia's crowdsourced encyclopedia and news stories. 

But for me, the paradigmatic example of Web 2.0 is Google's Pagerank. Not only did it lead to the biggest financial success story to date, it is the example that makes us think hardest about the true meaning of "collective intelligence." What Larry Page realized was that _meaning was already being encoded unconsciously_ by web page creators when they linked one page to another. And that understanding that a link was a vote allowed Google to give better search results than people who, up to that time, were just searching the contents of the various documents on the web. 

And so, it seems to me that Pagerank illustrates the fundamental difference between the approaches of the Semantic Web and Web 2.0. The Semantic Web sees meaning as something that needs to be added to documents so that computers can act intelligently about them. Web 2.0 seeks to discover the ways that meaning has already been implicitly encoded by the way people use documents and digital objects, and then to extract that meaning, often by statistical means by studying large aggregates of related documents. 

Looking at it this way, you can see that Wesabe is very much a Web 2.0 company. Their fundamental insight is that the way that people spend money is a vote, just like a link is for Pagerank, and that you can use that aggregated vote to build various kinds of intelligent user-facing services. 

valuesofN (Sandy) and Tripit are much less obviously web 2.0 in that sense. They provide services to an individual, based on his or her own data, with little or no "collective intelligence" benefit. They do, however, work to extract meaning from documents, rather than requiring that it be structured in some special way. 

Sandy uses a "little language" so that email can be used to inform a bot to keep track of various kinds of information on your behalf. Tripit merely recognizes that certain types of documents -- in particular, reservation confirmations from airlines, hotels, and rental cars -- have clear structure from which meaning can be extracted. They then mash up additional relevant data such as maps and user notes to construct useful itinerary documents. These are both applications that are closer to the Semantic Web way of thinking, but again, no formal ontology was ever developed. The application developers simply realized that there was sufficient meaning in scope-limited interactions that it becomes possible to build a seemingly intelligent agent. 

Where I think the two approaches meet, and will find common cause, is in the design of applications that don't require people to think at all about ontology or document structure, but nonetheless produce documents that are more amenable to the automated extraction of meaning. Social networking is a good example. Users are gradually building out the "Friend of a Friend" network that [FoaF](http://www.foaf-project.org/) advocates dreamed of. It's missing a lot of the nuanced intelligence that was designed into the FoaF specification -- after all, what does it _mean_ that someone is your friend on Facebook? By focusing on short-term utility (initially, getting to know your classmates in a college context), Facebook built something that was adopted far more quickly than the carefully thought out FoaF project. 

The Semantic Web is a bit of a slog, with a lot of work required to build enough data for the applications to become useful. Web 2.0 applications often do a half-assed job of tackling the same problem, but because they harness self-interest, they typically gather much more data. And then solve for their deficiencies with statistics or other advantages of scale. 

But I predict that we'll soon see a second wave of social networking sites, or upgrades to existing ones, that provide for the encoding of additional nuance. In addition, there will be specialized sites -- take [Geni](http://www.geni.com), for example, which encodes geneaology -- that will provide additional information about the relationships between people. Rather than there being a single specification capturing all the information about relationships between people, there will be many overlapping (and gapping) applications, and an opportunity for someone to aggregate the available information into something more meaningful. 

I expect there to be a lot of confusion before things start to become clear. But I'm confident that in the end, Web 2.0 and the Semantic Web are going to meet in the middle and become best friends.
