---
title: "[etech] Day 2 – Folksonomies panel"
person: david-weinberger
section: by
type: blog-post
year: 2005
date: 2005-03-16
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2005/03/16/etech-day-2-folksonomies-panel/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [etech] Day 2 – Folksonomies panel

## Full text

Clay Shirky moderates a panel on folksonomies. Participants: Jimbo Wales (wikipedia), Joshua Schachter (del.icio.us) and Stewart Butterfield (flickr).

Clay: Why did you decide to let users in to categorization?

Jimbo: We launched our categorization system last June. For the first few weeks, it was a complete madhouse in the English wikipedia. In the German one, they held off for a couple of weeks. It took a little while for things to be rationalized. We decided to let the masses categorize it because that’s just the Wiki way.

Stewart: We added it because Joshua told us to. I don’t think of it as categorization primarily. Tags are to help users. They aren’t a replacement of categorization.

Joshua: I’d been collected links in a text file. I started adding a hash mark and then some text so I could grep them out. Then he decided to make it massively multiplayer. Tags were originally for people to categorize their own bookmarks, but it’s gone social and used for purposes other than categorization.

Clay: When tensions arise between the individual and the group, and how is that resolved?

Jimbo: The tension is really more between the individual and the quality of the encyclopedia. We don’t allow people to categorize things in individual ways because they’re categorizing the encyclopedia itself.

Joshua: Maybe there’s a need for some mechanism for consensus because tag sets overlap…At Wikipedia, people fight over the same space whereas at delicious, everyone has his own page. The top tags for Wikipedia are free and reference, which are not words that appear on Wikipedia’s home page, so people are thinking about you differently than you are.

Jimbo: Very interesting.

Clay: There’s a large collection of “circle in square” photos on Flickr. That’s a place where some sort of social group. At delicious, people use the comments field to have a conversation, with the link serving as an anchor.

Joshua: Why do you have a distinction between groups and tags, Stewart?

Marc Cantor: Can we connect tags between systems

Jimbo: I talked with Technorati. We should all get together and share database dumps of tags just to see what people are doing in different systems. E.g., photos in flickr might be useful for the encyclopedia.

Stewart: Technorati is already doing that. We have 200,000 distinct tags and 12M total tags.

Joshua: We have different axes of why you’re tagging, what you’re tagging, and how it happens. E.g., at Flickr you’re mostly tagging your own stuff for your purposes, at delicious it’s mostly other people’s stuff mostly for your own purposes, technorati you’re tagging your stuff for others. Calling them all “tags” over-simplifies. We need better understanding before we start plugging things in.

Q: How are you giving users feedback to get their tagging better?

Jimbo: It’s a tight knit community of 600-1000 people who do the vast majority of the work.

Stewart: There are no bad tags, at least within the context of Flickr. The point isn’t for you to find all and only the photos of elephants. It’s to give them tools for organizing their own stuff. The rest is a happy accident. And when you have millions of photos, you don’t have to find all of them.

Joshua: I’ve tried to close the loop. With the experimental bookmarklet you can see all of your tags, the top tags for the thing you’re bookmarking, and the intersection of your tags with everyone’s. I don’t want people to be dominated by groupthink. Your instinct is the most reliable and reproducible — it’s the way you’ll remember.

Clay: Traditionally, we don’t allow users and time because we want timeless categories.

Q: The semantic web community is creating taxonomies in particular areas. But there are problems scaling it. What about a folksonomic approach to creating large scale taxonomies.

Stewart: I think the wikipedia model works.

Jimbo: To create a large scale category system, a small group of experts can’t even begin to compete with a large, open group of people.

Stewart: The idea that there is a proper way to cleave nature at the joints is difficult.

Joshua: Dividing the world into a complex, fine-grained tree doesn’t pay attention to what people are trying to do. They’re trying to find things. There’s a natural sort of scale. You tend not to tag too high (“computers”) and not to tag too finely. There’s a natural middle ground. [Cf. Eleanor Rosch: Why do we sit in a chair instead of in furniture? It turns out to do with the bodily nature of epistemology. But what about on the bodiless web?]

Q: What happens when we have thousands of services tagging? How do we bring all that knowledge together?

Joshua: First we have to know what we’re doing. People use tags for different purposes.

Q: What about using RDF to manage this infrastructure?

Joshua: I emit RDF because it’s convenient. They can work together.

Me: How much metadata about tags will we have to capture? E.g., it might be useful to know the author of a tag, whether it’s a place or a topic, when it was created, which app created it, etc.

Joshua: that would make tags too complex.

Stewart: You have to do it after the fact. You can’t make people express it explicitly.

Jimbo: If we saw two tags for Ohio, “Ohio” and “OH,” someone would catch it and fix it. And since our categories are hierarchical, we don’t have to disambiguate “cardinal” as a bird or a baseball team.

Joshua: I’m now letting users create “bundles,” i.e., second level tags. BTW, hierarchies sort nicely alphabetically. (E.g., computers.languages.perl sorts next to computers.languages.python.)

[Technorati tags: etech taxonomy folksonomy tags]
