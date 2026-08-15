---
title: "Decentralized Centralization: Rosters in Federated Wiki"
person: mike-caulfield
section: by
type: blog-post
year: 2015
date: 2015-06-12
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2015/06/12/decentralized-centralization-rosters-in-federated-wiki/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Decentralized Centralization: Rosters in Federated Wiki

## Full text

We have developed this new feature in federated wiki called Rosters. I think the implications of it are pretty big for how fedwiki develops. I want to tell you about it.

So let’s start at the beginning. People have had trouble connecting with one another on federated wiki in the happenings. The architecture of federated wiki made it very easy to grow a large organic network of collaborators over time, but somewhat difficult to spin up a group quickly in the way that many groups spin up.

So Ward and Paul built this thing called the Roster.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/roster.png>)

Rosters are ways to organize all the sites you read. Up at the top you can see I write or have written eight or so sites I might want to being into my search neighborhood, in a “I know I wrote something about that somewhere” sort of way. I’m also watching Ward Cunningham’s writings on the four sites of his I care about (but not, for example, watching his sites on programming issues).

When I want to “load” these sites into my neighborhood (which is what we call the search, activity, and link resolution context) I click that little sideways chevron arrow at the end of the squares that represent the sites and my neighborhood loads information about those sites that allows neat things to happen.

The rosters are configured with text. Here’s the text that produces the Roster above:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/config.png>)

You just click in and edit it yourself.

Now this is cool stuff in and of itself, because it makes getting connected to others in the federation much easier than before, and allows you to organize those connections in ways that support your workflow.

However, there’s a neat and potentially game-changing feature we’ve added in — rosters can consume other rosters.

So for instance, I can remotely pull in a roster of Ward’s like so:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/roster2.png>)

And it comes through like this:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/ward.png>)

You see how I can pull in the people that Ward follows, and supplement my page with them?

It actually gets even crazier, because you can use these rosters to customize your activity feeds. So, for example, I can go into my Recent Activity feed and tell my feed to look at only the sites that are in Ward’s Developer category. So here I edit my activity feed to show just the stuff from Developers, and to get really fancy, I say I only want to see the stuff that has been forked at least once by some other site.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/language.png>)

And when I do that I see the set of pages that are presumably important or interesting or useful to multiple developers of Ward’s choosing:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/green.png>)

And because we pull this roster by reference, not value, if Ward updates his roster we pull updates from the new set of people he’s defined. And before you ask, yes, you can even have rosters that pull in rosters of other rosters. I don’t know if that’s advisable, but it’s there for you (Ward has built in a protection against infinite recursion, though, so experiment all you want).

You see the point though, right? I can subscribe to a Roster that is maintained by someone else — a teacher, an expert, or a stranger that seems to have good taste. As they maintain the list what I see changes.

This makes possible all sorts of new use scenarios.

## But wait a minute, I thought you were all about the decentralization!

We are. But part of aiding individuals is giving them the power to self-organize, or to divide/assign community maintenance tasks. Creating a open network with no tools for self-organization is disempowering. The question is what kind of tools you create.

I like this approach to centralization — you give people the ability to build and maintain their own communities with a set of LEGO blocks, but like LEGOs they can be pulled apart and reassembled as something else in the case that your current community becomes tyrannical, harassing, or just boring over time. You can take your pages with you and reassemble into newer, hopefully better communities.

## Enough, when is the next Happening, and what’s it about?

I want to start the next happening as soon as possible. Here’s what it is going to be about.

We’re going to test this roster functionality by setting up “pods”. Pods will form around a task or research question — for instance, you could structure a pod around the task of improving the Wikipedia coverage of Mario Bava, or increasing the quality of articles on the world’s oceans, or something non-wikipedia like compiling every piece of information about where the “I[mages are processed 60,000 times as fast as text](<http://cogdogblog.com/2015/03/27/dialed-back-to-1982/>)” myth comes from.

You put together your set of people you want working on this, and build a roster you share out to the others. And then you start to build out your knowledge in that weird federated wiki way, where things start to link together in ways you had not imagined. When the time is up, you consolidate your work — moving things into wikipedia, sharing as a more “normal” looking wiki, publishing your results or whatever.

All we need are Pod Leaders who are willing to facilitate the investigation of a subject of general interest. We could keep the pod sizes small — 3 to 12 people so that there is not that much community maintenance involved. And the experience could be two weeks or a slow burn at a few months. If you’re Pod Leader you’d get to choose the timeline and the topic.

So email me at caulfield.mike@gmail.com if you would like to be a Pod Leader or learn more about being a Pod Leader, and we’ll get this show on the road.
