---
title: "The Annotation Layer As a Marketplace for Context: A Proposal"
person: mike-caulfield
section: by
type: blog-post
year: 2017
date: 2017-05-11
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2017/05/11/the-annotation-layer-as-fact-checking-and-context-marketplace-a-proposal/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# The Annotation Layer As a Marketplace for Context: A Proposal

## Full text

A lot of our thinking about giving articles a “fact-checking” context has been about automated, centralized, closed approaches — Facebook algorithms that flag things, plugins that provide context, etc. Some of these things are deep in proprietary plumbing of platforms. Others are service-based real-time overlays of information. All of them require you opt-in to some particular company’s product, approach, extension, or algorithm. This leads to a real problem for a couple reasons:

  1. We’re going to end up putting all the eggs in one solution basket. Do you use AI or SNA or flagging? My 108-variable algorithm or your 52-variable one? And once there’s lock-in to that approach — once browsers or platforms or whatever have selected a solution, competition disappears — it’s winner take all. We’re already seeing everybody jockeying for position here, trying to be *the* solution. Things like this don’t end well.
  2. Centralizing this sort of stuff is attractive, yet problematic. I’m a believer in smart defaults. But without ability to select from multiple context providers the centralization will eliminate broad swaths of valuable perspective. Worse — we won’t notice those perspectives have become invisible.

In the relatively short time since the election, I’ve met so many intelligent people working on these issues. T. S. Waterman wants to look at issues around time and place and credibility, in a way more people should be thinking about. The Hoaxy people are looking at propagation networks. Others are coming up with crowdsourcing approaches, or domain credibility signals.

So much good work. This community feels alive, and vibrant, and energized. These are some of the smartest people I’ve met in my life, and if we keep working together, we can truly make the web better. And yet I can feel the pressure here — who is going to get funded? Whose approach is going to win? The vibrancy and creativity of the community is unfortunately being undermined by the race of funders and platforms to find  _the_ solution.

## Annotation As a Marketplace for Context

Here’s my thought: before we lock in to this approach or that one, maybe we should think about an approach that allows the sort of creative experimentation we need to foster in this area. And if we do that, annotation is the obvious marketplace we could use.

How does this work? Well, say you have a document — a web page.

Now, different researchers and tool providers may have different insights about this page:

  * Researcher A has compiled a list of all major newspapers that meet a certain standard of legitimacy, and can test “Tulsa World” against that.
  * Researcher B has a kickass social network analysis which shows the networks this article is flowing through, and can identify with reasonable confidence whether this article is favored by conspiracy theorists.
  * Researcher C has a kickass social network that also looks for conspiracy and hoaxes but with different strengths than Researcher B.
  * Researcher D has an NLP tool which can identify if this is Op-Ed content or a news story, or somewhere in-between.
  * Tool maker A has a program which looks for a “credibility signal” from the domain, and publishes it on a scale of 1-10
  * Tool maker B has a tool that looks up all the organizations in the article to see if they are Front Groups, and all the experts cited to see if they are recognized by Google Scholar
  * Organization A (say, Politifact) has information about certain claims in the article.
  * Organization B (say, Factcheck.org) has information about certain claims in the article.

And so on. Now we could go through eight different tools to benefit from those different insights. Or we could take these multiple insights, hand them to someone, and say “use these insights to make the best possible tool to help people evaluate this article.” Or the Facebook of the industry could hire Researcher A, use the work of Researchers B & C, ignore Researcher D, and decide whether to partner with organization A or B.

None of these seem right to me. They all lead to the single platform invisible algorithm nonsense that got us into this mess. They all shut down the vibrant conversation and collaborative experimentation that has developed in this space. If a new approach to article contextualization isn’t up-and-running when the big checks are cut, its insights get lost to history.

So what to do? I’d suggest we do what we often do when we want to move more quickly: separate the data layer from the interface layer. And I’d suggest that the best way for everyone to work together is to use the newly [W3C-approved annotation layer](<https://hypothes.is/blog/annotation-is-now-a-web-standard/>) as that data layer.

How would this work in practice? Let’s say I have some idea for contextualizing articles on the web. I’ll choose here a little thing I’ve been working on — looking at news stories and scanning them for astroturf industry groups, e.g. coalitions of coal industry groups posing as Scientists for Progressive Energy Policy or the like. I’ve developed a database of these groups and links to wiki pages summarizing the the funding and governance of these groups and their history. I want to get that to the user.

One method — the method many people seem to want to use — is to make an extension that looks at pages and highlights these organizations and links to the research. But of course I’ve already got half a dozen extensions, and the cost of marketing to get people to adopt yet another extension far exceeds the cost of funding the design of the tool (and takes away funds from improving identification of claims, lies, and context). It balkanizes effort, leading to dozens of tools all which do a fraction of the job required.

Another method is to go to a big provider like Facebook and say you should provide this front group research as context to your users. Maybe they say yes, and maybe they say no. But in choosing what they want to choose they centrally determine the approaches that will be use. It’s OK for them to do that, certainly. But if you have a tool or approach that works, do you really want to move it into the sealed vault of Facebook code?

The annotation alternative is more attractive. Instead of creating an extension to show my generated context or playing the zero-sum Facebook game, I run my tool as a bot on web pages, generating machine-and-human readable context in the annotation layer. For example, in this scenario, our bot spots the phrase “Americans for Medical Progress” …

…and tags that as the name of a known industry front group:

You’ll note we have a human readable note here. But we also have some machine readable tags that identify this issue, and a link to information on the front group.

Doing it this way, some other process can come in and tag the page with additional information. A hoax bot can look at a social network analysis of how this page is moving through the net and determine that it’s got a viral hoax rating of zero:

Because annotation is just a data layer, you can add as many of these as you want, stored with reference to the URL and anchored to specific text on the page.

This allows anyone that has a piece of the solution to spin up an annotation bot with a few lines of Python code and push their information out to the reader endpoints. For example, we can imagine that Politifact could not only debunk claims, but send bots out that look for those claims and link to those claim analyses on the Politifact site. Here, we imagine that Politifact has done a treatment of the claim referenced here (they haven’t — this is just an example):

As you can see, various amounts of signal and context can be layered on here. And since this is all retrievable by API, front end services can decide what sorts of signal and context they want to look at (and from whom) when they make different display decisions. A front-end extension could pull information from 20 or 30 separate annotation providers in giving context to a page. A service such as Facebook could pull from hundreds if they wanted to. But the data — the listing of what we know about the pages from all different approaches and veins of research — is open to anyone to build and innovate on top of. And crucially, it makes entry into the marketplace of analysis extraordinarily cheap.

## Concerns

The first concern that people will come up with is whether botting is inefficient compared to centralized management of this process, or the just-in-time approach you can do with an extension. The tagging of hundreds of thousands of pages and the associated management of things stored in the annotation layer just seems exhausting. Won’t you have to bot the whole internet? Doesn’t that make everyone have to run their own Googlebot?

In practice, no. The thing is if you have an analysis that you want to share, you most likely have identified a set of pages already, and that set is likely relatively small. So, for instance, if I’m the hoaxish bot above, I’m not looking at every page on the internet — I’m just looking at higher sharecount pages moving across Facebook. Even if I’m looking at the top 50,000 Facebook pages of the day, tagging those pages is still the sort of thing that could batched overnight. But even there, if 99% of those pages are not new you’re tagging 500 pages a day, which is similar to what I did last night from Starbucks on a laptop while they were making my cappuccino. There’s a power law to this stuff, and it favors botting.

The second but more serious question is about the transparency. One of the advantages that Facebook has is it hides it’s signal. You don’t know you’re being discriminated against as a site or a sharer, and you don’t know how it was computed. Facebook’s take on your content is like a credit score that you can never look up, and that’s good for Facebook, because it makes it harder to game or contest.

On the whole, though, I think this is more feature than bug. Yes, being able to look at your page ratings over 100 signals from different providers will make it easy to game the system and also let you know who is ranking you down or highlighting your use of bad sources. But ultimately, while we need to protect the researchers who produce these tools we also need to give people more transparency into why their pages are suddenly not drawing traffic. Not only is that fair, but it might also put some pressure on legitimate entities to clean their act up: if my front group bot keeps finding quotes from front groups in my local paper, maybe they’ll be a bit more diligent about source checking.

## Future

So how do we make this distributed, open approach to this happen? How do we make the annotation layer a marketplace for context? And how do we make sure that market is functional, navigable, and useful both to tool makers and end-users? I leave that all to you. But let’s think about this — let’s not put all our eggs in another sealed basket. Let’s keep the energy around this issue and invite all comers to add their piece of insight. The other path — closed, single platform, invisible solutions? We’ve been through that already. It’s how we got here. Let’s not repeat that mistake again.

#### Credit

I apologize that crediting this set of realizations is such a mess, actually: it goes back to conversations at Hewlett Open Educational Tools conference about annotation as the universal bus in January (which was based on prototypes of citing capability I had built with Jon Udell in November). And then at iAnnotate I ended up having the same conversation with people throughout the three days of the conference, and pulling insights from previous conversations into the next conversation until who knows what came from where in the end. It came to a head in a conversation over sliders with Jon, T.S. Waterman, Peg Fowler, and Tom Gillespie on Friday night, but others I talked to will see their conversations in here too, particularly the unconference group on Day One where we came up with a “stub articles” proposal (great unconference group, or greatest unconference group of all time?). Apologies all around about the credit, really.
