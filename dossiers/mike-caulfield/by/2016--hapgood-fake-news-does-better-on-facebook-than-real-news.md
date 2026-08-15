---
title: "Despite Zuckerberg\u2019s Protests, Fake News Does Better on Facebook Than Real News. Here\u2019s Data to Prove It."
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-11-13
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/11/13/fake-news-does-better-on-facebook-than-real-news/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Despite Zuckerberg’s Protests, Fake News Does Better on Facebook Than Real News. Here’s Data to Prove It.

## Full text

(An investigation in which we decide to use Facebook’s social graph API to see whether fake news or real news is more viral).

_**UPDATE** : Since posting, there has been some discussion about this post’s use of the phrase “top stories from local newspapers”. A clarification on how that phrase is used has been appended at the end of the post with some methodology, and some small clarifying edits have been made. The title and core claim of the post remains accurate and stands. What we present here is not the best possible measure of fake vs. real virality, but it is a meaningful one, and deserves to be addressed._

Mark Zuckerberg told us recently that fake stories on Facebook were quite rare, less than 1% of total content. I’m not sure how he computes “content”, exactly. Is my status update content? Each photo I upload?

> Mark Zuckerberg says the notion that fake news influenced the U.S. presidential election is “a pretty crazy idea.”
> 
> He also says his company has studied fake news and found it’s a “very small volume” of the content on Facebook. He did not specify if that content is more or less viral or impactful than other information. [Source: [NPR](<http://www.npr.org/sections/alltechconsidered/2016/11/11/501743684/zuckerberg-denies-fake-news-on-facebook-had-impact-on-the-election>)]

Well, if Zuckerberg can’t specify if fake news is more viral on Facebook, maybe we can, using the publicly available Facebook APIs. Let’s help him out!

The question I want to ask is this: how do popular fake Facebook stories from fake local newspapers compare to top stories from real local newspapers? Not “how many stories are there of each” but rather “Is fake news or real news more likely to be shared, and what’s the size of the difference?”

If Facebook is truly a functioning news ecosystem we should expect large local newspapers like the Boston Globe and LA Times to compete favorably with fake “hoax” newspapers like the Baltimore Gazette or Denver Guardian — fake “papers” that were created purely to derive ad views from people looking for invented Clinton conspiracies.

For our fake story, we’re choosing the most popular story from the Denver Guardian, a fake newspaper created in the final days of the election. Its story “FBI Agent Suspected In Hillary Leaks Found Dead In Apparent Murder-Suicide”has now been shared on Facebook well over half a million times, as you can see with [this call](<https://graph.facebook.com/?id=http://denverguardian.com/2016/11/05/fbi-agent-suspected-hillary-email-leaks-found-dead-apparent-murder-suicide/>) to Facebook’s API. This story exists on a site made to look like a real local newspaper and details quotes from people both real and fake about the murder-suicide of an FBI agent and his wife supposedly implicated in leaking Clinton’s emails. According to the story he shot himself and his wife and then set his house on fire. Pretty fishy, eh? Add it to the Clinton Body Count.

The story is, of course, completely fake. But at 568,000 shares (shares, mind you, not views) it is several orders of magnitude more popular a story than anything any major city paper publishes on a daily basis.

“Oh, hold on Mike, you say, ‘orders of magnitude’, but a lot of people misunderstand that phrase. Something shared several orders of magnitude more frequently would have to be shared literally around a thousand times more.”

Yep. That’s what I am saying: this article from a fake local paper was shared one thousand times more than material from real local papers.

Don’t believe me?

For our “real” stories, we are choosing the stories the papers have identified as their most popular of the day, via their “most popular stories” section on their site. (We are not choosing the most popular story they have based on Facebook data — I don’t currently have a way to know that).

The Boston Globe’s most popular article today (according to their site) is an article from its famous Spotlight team (yes, [that Spotlight team](<http://www.bostonglobe.com/lifestyle/names/2015/10/30/how-spotlight-movie-got-made/wXVXUiYPkoF3hEP9K4dydP/story.html>)) on the tragedy of shutting down psychiatric facilities in Massachusetts and elsewhere and replacing them with nothing. Number of shares? [181](<https://graph.facebook.com/?id=https://apps.bostonglobe.com/spotlight/the-desperate-and-the-dead/series/jury/>).

The LA Times has an editorial piece that is today’s most popular on their site titled “We’re called redneck, ignorant, racist. That’s not true’: Trump supporters explain why they voted for him.”That ought to share more generally than LA people, right? Number of shares: [342 shares](<https://graph.facebook.com/?id=http://www.latimes.com/politics/la-na-pol-donald-trump-american-voices-20161113-story.html>).

The Chicago Tribune has a truly national story currently trending, “Trump and advisers back off major campaign pledges, including Obamacare and the wall”. The story is originally from the Washington Post, but is about as major a story as you get. Number of shares: [1774](<https://graph.facebook.com/?id=http://www.chicagotribune.com/news/nationworld/politics/ct-trump-campaign-pledges-20161112-story.html>).

Now you could go national as well — that story from the Tribune was from the Washington Post, and is a top trending story there as well. So what does a truly national, click-ready story get you? Number of shares: [38,162](<https://graph.facebook.com/?id=https://www.washingtonpost.com/politics/trump-and-aides-hedge-on-major-pledges-including-obamacare-and-the-wall/2016/11/11/9196b364-a82f-11e6-8fc0-7be8f848c492_story.html>).

Let’s plot that on a graph, shall we? Again, remember that these are not random selections — these are stats for the trending stories from each publication:

To put this in perspective, if you combined the top stories from the Boston Globe, Washington Post, Chicago Tribune, and LA Times, they still had only 5% the viewership of an article from a fake news site that intimated strongly that the Democratic Presidential candidate had had a husband and wife murdered then burned to cover up her crimes.

The fact that Mark Zuckerberg can shrug his shoulders with his best “Who, me?” face — I’m trying to stay logical here, but I feel very sick to my stomach. There is nothing trivial, rare, or occasional about fake news on Facebook. Fake news outperforms real news on Facebook by several orders of magnitude. The financial rewards for pushing fake news to Facebook are also several orders of magnitude higher, and so expect this to continue until Zuckerberg came come to terms with the conspiracy ecosystem he created, and the effect it has had of U.S. Politics.

**UPDATE:** Dan Barker notes that there are some stories on the LA Times site (and other sites) that have outperformed what those sites self-identify as their “top stories” or “most popular stories”. As one example, a story about a KKK march in the LA Times yesterday got north of 250,000 shares on Facebook yesterday, but for reasons that aren’t clear is not listed as a “most popular” story on the LA Times site. That might be because people shared it without clicking through, or it could be because the algorithm they use rolls day-old stories off the trending list.

Outside of the fact that that still puts the LA Times at a disadvantage to the fake Denver Guardian, I think the analysis is still valuable here. What we are looking at is how likely a popular story on a news site is to go viral as compared to what can be achieved on a fake news site. This is interesting because the popular stories on a news site exist (to some extent) outside Facebook’s algorithm, and provide a sense of what we might think of as traditional top news stories.

Is it the best comparison that can be made? No — so let’s make better comparisons. Please. Show me up. Build the tools to do it, and get Facebook to open access to its data so it can be done systemically. But let’s not take Facebook at its word here.
