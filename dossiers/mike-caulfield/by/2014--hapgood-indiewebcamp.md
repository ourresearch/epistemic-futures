---
title: "#indiewebcamp"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-07-02
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/07/02/indiewebcamp/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# #indiewebcamp

## Full text

The first surprise about [IndieWebCamp](<http://indiewebcamp.com/>) were the people.

This is going to sound like I was expecting Really Bad Things, but you have to remember this is Portland. What’s “indie” in most cities is considered corporate in Portland. I don’t know how to explain this, except to say when I went out to dinner with Gardner Campbell, Tom Woodward, and Jon Becker in Portland a couple weeks ago, on the way there I passed this guy, unicycling between me and the food carts (sans flames that day).

My thoughts? Not bad. But a tad corporate for Portland.

Now if it was a BRONY on a unicycle….

### Pragmatism

So I had this worry that the camp might be a bit — well, let’s just say the worry was that the zeal/pragmatism balance might tend more towards zeal. My feeling on decentralization personally is that a revolution that expects users to accept less functionality and higher cost in exchange for more freedom is over before it starts. Decentralization has to be made easy, and ideally it has to let me do neat new things that centralization did not allow.

So the first surprise was the introductory presentations. This is a group that was founded as a pragmatic reaction against other attempts at re-decentralization. Not only does it focus on building stuff over talking about protocols, but Amber Case’s presentation actually showed a viable plan for re-taking the web. The plan is to focus first on journalists, who have very real and present problems caused by service Balkanization. By demonstrating value to journalists, they hope to amplify the movement, and push it into the next stages.

Maybe you disagree with that analysis. But it is far from the “And once they see the power of my code, the people will rise up” bullcrap that typically dominates this set of conversations. It also acknowledges that you want to fight an oligarchy of heavily funded corporations you need a marketing plan. It doesn’t have to be oppresive or all-consuming. But the thing that turns a personal project into movement is strategic and tactical thinking about how to advance it. Everyone I saw speak about their code that day had at least a thumbnail sketch of how they could get broader adoption, and that’s an oddity in this realm.

You can see that too in the [Why](<http://indiewebcamp.com/why>) page on the indiewebcamp site. The why is about what changes in the user’s experience of services, not on software as a political expression.

### Products

The products I saw were also surprising.

These technologies are things you check in on every year or so. And in general my experience with them has been there’s been very little focus on making them user-friendly. Why, this many years later, do you have to SSH up to your MediaWiki instance and edit a config file to make even the smallest change?

Talk to your average DIY-er, and they’ll tell you that learning to edit config files is good for you. But so is hanging out with my family, riding my bike, getting a drink at Trivia Night, and watching the new series of In The Flesh. And editing config files (and learning the ins and outs of SSH key-files, PUTTY, pico or whatever) takes time away from all those things. I’m not saying applications can’t be difficult — as much as I might curse Illustrator’s spline based interface, it’s the right way to empower many users. But forcing your users to manually handle integrations that you couldn’t figure out and selling it to them as virtue is precisely why this movement often seems stuck in 1993.

Not so here. Every presentation I saw focused *heavily* on user experience, whether it was on IndieBox, or Known, or IndieAuth. Even the discussions of how different products could be integrated were focussed on what the user would see, not on backend geekery.

### Demographics & Tone

It was not all young people. It was not all old people. It was not all men or women. It was probably too white (then again, it’s Portland). It had project managers in the mix as well as coders. Some people were launching new companies. Some people were doing this on the side of other higher paying corporate jobs.

People here weren’t allergic to making money, but they weren’t high off their own pitches either.

There’s been some people who have been tossing the idea around of Portland as the anti-Silicon Valley. A culture of experimentation and collaboration without the sickness that the Valley has acquired over the years. I know a number of people at IndieWebCamp were from other places, but I couldn’t help but think about that during this session. It’s the same sort of attitude I’ve found in the small but productive Open Education community here. It’s the same attitude you see in the [XOXO community](<http://2013.xoxofest.com/>).

Can Portland become the sane counter-balance to the hype of Palo Alto? They have Udacity; we have Lumen Learning. They have TechCrunch’s Disrupt; we have IndieWebCamp and XOXO.

Well, counterbalance is too strong a word, perhaps. But I actually expect great things out of this city.

If nothing else, it highlighted to me that I need to get more involved, and maybe move a tad more south. I’m 15 minutes away from the epicenter of something big, it’s stupid for me not to get down there more.

### Ward Cunningham and Federated Wiki

One of the highlights for me was meeting Ward Cunningham in person finally. We ended up having a 90 minute conversation which clarified my thinking on a lot of issues. Particularly, Ward highlighted for me how schemas — and particularly tight, locked-down database schemas — had killed user innovation. I realized that while Ward is the most brilliant coder I know, his heart lies in [Non-Programistan](<http://bavatuesdays.com/greetings-from-non-programistan/>). He want’s to get back to the idea of “applications without programmers” so that, in his words, “humanity can move forward”.

In a world where Silicon Valley’s solution to the power they have over our lives is that “people should learn to code”, Ward’s radical idea (well, radical by 2014 standards) is that maybe we should make software that lets people solve novel problems without them knowing how to code. If you’ve been following Jim’s Internet Course you know that this was the original vision of people like Ivan Sutherland (also a current Portland resident) and his Sketchpad:

So it all comes back to this question of whether you ship an application, or do you ship a [user innovation toolkit](<http://hapgood.us/2013/10/27/educational-technology-and-the-sources-of-innovation/>). And the idea of a user innovation toolkit should NOT be “if you can code this source you can innovate”. It has to embrace non-coders, because the vast majority of ideas on how to make the world better come from non-coders, just as the vast majority of ideas on how to make equipment better come from non-engineers. 

And the piece that fell into place for me in that conversation was that the choke point for a lot of that innovation is the schema (in practical terms, the tightly structured backend database which locks in assumptions about what you want to do). 

Around that issue, we started to talk about a project I am working on to demonstrate the Smallest Federated Wiki as a user innovation toolkit — the [Movie Night Demo](<http://hapgood.us/2014/06/30/explaining-federation-through-family-movie-night-part-i/>). And we ended up coming up with a new feature that Ward coded the next day at IndieWebCamp (unfortunately I had prior obligations and couldn’t make Day 2). 

The feature allows you to merge edits of any two pages, interleaving them into a single journal timeline. In terms of Movie Night Demo, this means I can come to a list of your top ten films you want to see and with a simple drag and drop gesture merge your list and mine (while preserving the history). 

And in classic user innovation toolkit style, the way this functionality is acheived makes possible dozens of other applications as well. Imagine, for example, students doing collaborative note-taking and being able to instantly merge those notes along the timeline of the presentation. Or people merging data collected from multiple locations to produce a crowd-sourced visualization.

Not bad for a weekend, right?
