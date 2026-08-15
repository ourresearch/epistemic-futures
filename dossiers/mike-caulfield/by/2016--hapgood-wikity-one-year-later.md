---
title: "Wikity, One Year Later"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-11-20
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/11/20/wikity-one-year-later/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Wikity, One Year Later

## Full text

Consider this my one year report. 😉

The core idea of Wikity was simple: what if we bent the world of social media a bit away from the frothy outrage factory of Twitter and Facebook towards something more iterative, exploratory, and constructive? I took as my model Ward Cunningham’s excellent work on wiki and combined it with some insights on how to make social bookmarking a more creative, generative endeavor. The shortest explanation of Wikity I can provide is this: **Wikity is social bookmarks, wikified.**

It took me four months just to get to that explanation.

What does “wikified social bookmarks” mean? Well, like most social bookmarking tools, we allow for people to host private sites, but encourage people to _share their bookmarks and short notes with the world._ And while the mechanisms are federated, not centralized, we allow people to  _copy each other ’s bookmarks and notes, _just like Delicious or Pinboard.

That’s what’s the same. But we also do three things current social bookmarking sites do not.

  * We don’t bookmark pages. We _bookmark and name ideas, data, and evidence_. A single page may have multiple bookmarks for the different ideas, theories, and data referenced in the page.
  * _We provide a simple way of linking these “idea” bookmarks_, so that finding one idea leads naturally to other ideas. Over time you create an associative map of your understanding of an issue.
  * _As we revisit pages over time, we expand and update them_ , building them out, adding notes, sources, counterarguments, summaries, and new connections.

And the end result, after a year and about 300(!) hours of work, is something I love and I use every day. It’s a self-hosted bookmark manager for linked ideas and data that has (for me) revolutionized my ability to think through issues and find connections between ideas I would have otherwise missed. If you want to see me construct an argument about something, you can read my blog. But if you want some insight into how I conceptualize the space, you can visit my Wikity site, and follow a card like [Anger Spreads Fastest](<http://rainystreets.wikity.cc/anger-spreads-fastest/>).

I use it every day, and have accumulated over 2,000 “cards” in it, varying from interesting clippings on subjects of interest to more lengthy, hyperlinked reflections. As outlined a couple years ago in my [Federated Education keynote](<https://hapgood.us/2014/11/06/federated-education-new-directions-in-digital-collaboration/>), the cards often start out as simple blockquotes or observations, but often build over time into more complex productions, with links, sources, bibliographies, videos, and additional reflections.

(I’m tempted to recount every development decision here, to explain all the expansion and tweaking the product has undergone to get to its current state. I know some people may be looking at it and thinking “300 hours? Really?” But the path to product was never a straight one.)

## Wikity Today

Wikity is open. It’s constructed as a WordPress theme, and you can [download it from GitHub](<https://github.com/michaelarthurcaulfield/wikity-zero/>). It does a lot more than your average theme, but installation is a simple as uploading it to your WordPress theme directory and applying the theme. I learned PHP specifically for this project, so it’s not the most beautiful code you’ve ever seen. But it does work, and shows another way of thinking about our web interfaces and daily habits.

Now that Wikity is easily installable as a theme on self-hosted WordPress, I’ll be phasing out signups on the wikity.cc site, which I was running as a central space for new users to try out Wikity. In its place I hope to put an aggregation site that makes it easier for different people’s Wikity installs to see what other people are writing about. That will reduce the cost and effort of running and maintaining an enterprise server for other people’s content. I’ll be reaching out to the owners of the 127 sites on there.

I should also mention to some early users that the scope of what Wikity does has actually been reduced in many ways. There’s a way in which this is sad, but in other ways the biggest advance over the past year in Wikity has been realizing that the core of Wikity could be expressed as “social bookmarks, wikified.” If you’ve ever built a product, you know what I mean. If you haven’t — trust me, it’s a painful but necessary process.

You can still use Wikity for a variety of things other than wikified bookmarks and notes — I worked with a professor in the Spring, for example, to use it to build a virtual museum, and as far as I can tell, Wikity is the simplest way to run a personal wiki on top of WordPress. But the focus is a hyperlinked bookmarking and notetaking system, because after a year of use and 2,000 cards logged, I can tell you that is where the unique value is. The beautiful thing is if you think the value is somewhere else the code is up there and forkable — sculpt it to your own wishes!

Finally a promise: Wikity core is safe from the demons of decay, at least for now. It will continue to be maintained and improved, mainly because I am addicted to using it personally. On top of that, we’re currently organizing a Wikity event for Christmas break, to introduce educators to the platform as a learning and research tool for students.

Now lets talk about some of the struggles we’ve been through here, and where we’re going in the future.

## The Long and Winding Road

I have to admit, I thought early on that there would be larger appetite for Wikity. There may still be. But it has proved harder than thought.

Part of the reason, I think, is that the social bookmarking world that I expected Wikity to expand on is smaller than I thought, and has at least one good solid provider that people can count on (Pinboard, written and maintained by the excellent Maciej Cegłowski). More importantly, people have largely built a set of habits today that revolve around Twitter and Facebook and Slack. The habits of personal bookmarking have been eroded by these platforms which give people instant social gratification. In today’s world, bookmarking, organizing, and summarizing information feels a bit like broccoli compared to re-tweeting something with a “WTF?” tag and watching the likes roll in.

I had a bunch of people try Wikity, and even paid many people to test it. The conclusion was usually that it was easy to use, valuable, cool — and completely non-addictive. One hour into Wikity people were in love with the tool. But the next day they felt no compulsion to go back.

We could structure Wikity around social rewards in the future, and that might happen. But ultimately, for me, that struggle to understand why Wikity was not addictive in the ways that Twitter and Facebook were ended up being the most important part of the project.

I began, very early on, compiling notes in Wikity on issues surrounding the culture of Twitter, Facebook, social media, trolling, and the like. Blurbs about whether empathy was the problem or solution. Notes on issues like Abortion Geofencing, Alarm Fatigue, and the remarkable consistency of ad revenue to GDP over the last century. Was this the battle we needed to have first? Helping people understand the profound negative impact our current closed social media tools are having on our politics and culture?

I exported just my [notes and clippings](<https://mikecaulfield.wordpress.com/wp-content/uploads/2016/11/notes-for-lost-in-the-stream-how-social-media-destroyed-our-democracy.pdf>) on these issues the other day, from Wikity, as a pdf. It was over 500 pages long. I was in deep.

As the United States primary ramped up, I became more alarmed at the way that platforms like Facebook and Twitter were polarizing opinions, encouraging shallow thought, and promoting the creation and dissemination of conspiracy theories and fake news. I began to understand that the goals of Wikity — and of any social software meant to promote deeper thought — began with increasing awareness of the ways in which our current closed, commercial environments our distorting our reality.

Recently, I have begun working with others on tools and projects that will help hold commercial social media accountable for their effect on civic discourse, and demonstrate and mitigate some of their more pernicious effects. Tools and curriculum that will help people to understand and advocate for the changes we need in these areas: algorithmic transparency, the right to modify our social media environments, the ability to see what the feed is hiding from us, places to collectively fact-check and review the sources of information we are fed.

Wikity will continue to be developed, but the journey that began with a tool ended at a social issue, and I think it’s that social issue — getting people to realize how these commercial systems have impacted political discourse and how open tools might solve the problem — that most demands addressing right now. I don’t think I’ve been this passionate about something in a very long time.

I’ve had some success in getting coverage of this issue in the past few weeks, from [Vox](<http://www.vox.com/2016/11/16/13626318/viral-fake-news-on-facebook>), to [TechCrunch](<https://techcrunch.com/2016/11/19/zuckerberg-reveals-plans-to-address-misinformation-on-facebook/>), to a brief interview on the U.S.’s Today Show this morning.

I think we need broader collaborations, and I think open tools and software will be key to this effort. This is a developing story.

So it’s an interesting end to this project — starting with a tool, and getting sucked into a movement. Wikity is complete and useful, but the main story (for me) has turned out to lead beyond that, and I’m hurtling towards the next chapter.

Was this a successful project? I don’t know what other people might think, but I think so. Freed from the constrictions of bullet pointed reports and waterfall charts, I just followed it where it led. It led somewhere important, where I’m making a positive difference. Is there more to success than that?
