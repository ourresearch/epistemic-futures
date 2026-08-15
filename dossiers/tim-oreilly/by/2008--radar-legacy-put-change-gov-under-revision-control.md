---
title: "Put change.gov Under Revision Control!"
person: tim-oreilly
section: by
type: blog-post
year: 2008
date: 2008-11-28
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2008/11/change-gov-revision-control.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Put change.gov Under Revision Control!

## Full text

Last week, the New York Times wrote about [Changes at change.gov](http://thecaucus.blogs.nytimes.com/2008/11/18/changes-at-changegov-return-of-the-agenda/): 

> The policy section of the transition site was removed without notice just days after Change.gov went live shortly after the election. At the time a spokesman for the Obama-Biden transition effort said they were “re-tooling” it. 
> 
> There was an almost instantaneous outcry from bloggers and other advocates of transparency in government who noticed disappearance. At least one site [posted a complete archive of the old Agenda pages](http://notatypewriter.com/Obama-ChangeGov/). (Increasing transparency, by the way, is a key feature of Mr. Obama’s government reform agenda, [according to the site’s “Ethics” page](http://www.change.gov/agenda/ethics_agenda/).) 

The changes, as it turned out, were mostly to tone down the partisan politics of the policy documents as published during the campaign. But the lesson remains: when public documents can be changed without notice, it's essential for the public to be able to see what changed, and why. 

There's a profound and simple tool that the Obama administration can use to improve government transparency. It's something that's enabled worldwide collaboration among software developers, and whose relevance for content development has been definitively demonstrated by wikipedia: Revision control. Not only does revision control allow a community to work independently on a common project, it makes it possible to review the changes. 

There's a primitive form of revision control in word processing products like Microsoft Word, but we need more than that, especially for documents that bring together the work of multiple independent authors. For change.gov, the wikipedia model might work: logging of every change, with only authorized participants allowed to make changes, but everyone (the public) able to review and comment on associated discussion pages. 

The real holy grail, of course, would be to provide revision control on all government regulations, and eventually, on legislation. This would no doubt be fought tooth and nail by lobbyists who don't want their fingerprints on the final result, but that's precisely why it would be such a breakthrough. And that's also why I suggest that the Obama team start with change.gov: demonstrate that the system works, that it has enormous benefits in transparency, and work from there. 

Of course, there are major technical and workflow obstacles. Many of the documents in question are probably worked on independently as Microsoft Office files, with bulk merges that obscure the history. What we really need are distributed revision control tools. There's a lot of good work happening in this area in the software development community; it would be fascinating to see it extended to collaborative document development. (Of course, shared editing a la Google Docs is coming to Microsoft Office as well, so perhaps the point of leverage is for Google to improve the revision control capabilities in Google Docs, starting an arms race with Microsoft. Once the tools are in place, the social pressure to use them has a point of leverage.) 

Like so many things that go under the rubric of "change," I'm sure that there would be many complications to this proposal, many problems I haven't thought of. Many current assumptions and processes would need to be challenged, and some of the challenges would take us down dead ends. But that's what change is all about. If it was just like the present, it wouldn't be change. 

I'd love your thoughts both on the general proposal and specific ideas for implementation. 

P.S. I wrote on this same subject about a year and a half ago, in a post entitled [Why Congress Needs a Version Control System](http://radar.oreilly.com/archives/2007/07/why-congress-ne.html). It was [Karl Fogel](http://www.red-bean.com/kfogel/) who first put this idea into my head, and that post explains his thinking. There are also some comments there from 2007 that may provide more grist for the discussion.
