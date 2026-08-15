---
title: "An interesting attribute tagging approach with LLMs"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-05-28
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/an-interesting-attribute-tagging
retrieved: 2026-08-13
content: full-text
notes: ""
---

# An interesting attribute tagging approach with LLMs

*And why the literature on cognitive surrender can feel a million miles away to people who use this stuff*

## Full text

I’ve been building a [little film property analyzer](<https://plot.fyi>) using Claude Code. My idea is to build a film recommender that works without using “people” data. (Most recommenders nowadays use people data, for example what films a person who searches for _The Fugitive_ tends to also search for). 

I want to do something different and build a recommender that relies purely on film _structure and elements_. You put in _The Fugitive_ , a film about a conspiracy that frames a man who has to go on the run while proving his innocence and unmasking a devious plot. You get back a match for _Three Days of the Condor_ , a film about a conspiracy that frames a man who has to go on the run while proving his innocence and unmasking a devious plot. 

Initially I was making my recommender by inventing descriptive tags on an adhoc basis and applying them to films in my film database using Claude. “Hard time window! Gothic!” I would think while watching something, then have Claude tag a bunch of films with that tag. The idea was this would eventually form a dense enough tag base I could do tag intersection math on the tags and spit out a recommendation. This worked until it became a mess. Too many tags overlapped too much which resulted in a lot of “double counting” of film attributes, and many tags were too specific to provide coverage or too broad to be useful.

Then I came up with an interesting idea of building “connective clusters” of similar films. 

## Connective Clusters and Microgenres

So over a month of evenings I built little film clusters, like “Criminal heist, murder, or con unravels from within as criminals turn on one another under pressure of pursuit” (Reservoir Dogs, Pelham 123, Fargo) and then used Claude to take my little triplets and build them out. I built 113 of these on the idea that I would then have over 110 “microgenres” to categorize films. 

My method for building these was simple. I’d look at (or sometimes watch) a film and think “What’s an interesting film that is like this and why?” Once I had the two films, I’d try to stick in a third. Then I’d use the LLM to help fill out the other 12 or so examples.1 On a given night I could come up with and refine about four of these microgenres. 

My idea was with enough microgenres I’d be able to make a broad classification sweep. My little microgenre definition might only have 15 films in it, but if I applied it across a set of 10,000 films with the LLM maybe it would find 150. If you did that 113 times you’d uncover a lot of films. 

For various reasons that didn’t work. It’s complex to explain, but it was super expensive to tag, it wasn’t giving me the surprising “Fugitive to Three Days of the Condor” connections I wanted, and it was leaving vast numbers of films completely untagged. It was a good instantiation of _my_ intuitions about film, which is not nothing, but it wasn’t telling me that much I didn’t already know.

## Decomposing microgenres does the trick (maybe)

I was about to go back to hand tagging when I had an idea: most microgenres were really the collision of three or four atomic ideas. What if we had the LLM decompose the microgenres into constituent tags, then used _those_ tags as our tags? 

This would benefit from some of the insights of the microgenres while getting around the problem I had tagging before, where the tags were either too narrow (“unaware ghost”) or too broad (“Spielbergian”), and get around the cluster problem which was the clusters were informative but not particularly generative.

It took a little back and forth. I first made my microgenres a little less micro, and combined them until I got 60 slightly more general categories that were a couple of ideas rather than four or so. Then I had Claude decompose them further:

[](<https://substackcdn.com/image/fetch/$s_!VZWw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3355b5b9-86b7-41d9-9e33-d814ecc64d17_1002x645.png>)

Sample:

> 60 microgenres as atom intersections
> 
> ACTION:
> 
>   1. Buddy-cop = has_buddy_duo ^ is_police_film ^ has_culture_clash
> 
>   2. Wilderness siege = set_in_uninhabited_area ^ civilization_breakdown ^ is_action
> 
>   3. Lone-protector extract = has_lone_protector ^ is_extraction
> 
>   4. Heist with betrayal = is_heist ^ has_internal_betrayal,
> 
> 

> 
> and so on…

Some of these tags I already had developed (like “hard_time_window”) and it pulled in (I’ve been working on this project for months). But most are new — it created 75 new tags that could produce the 113 microgenres — and hopefully a lot more. 

The next step is a bit painful, because applying these tags is going to drain my Claude token budget very quickly, so it may be several weeks before I get everything tagged, since I’ll be running out of tokens each night. I might figure out ways of taking a slice of the data and see if we can make a useful or interesting recommender without having the LLM evaluate 10,000 films for 75 tags on Opus (as my last post indicated, we really have to use Opus here, because Sonnet does not know the niche films and that leads to conflation and hallucination). 

Is there a lesson for education here? I’m not sure. But this sort of classification task for mapping a space is the bread and butter of many professional domains. I think that most students think using AI in the workplace will look like typing questions into a chatbox and pasting the answer somewhere. That’s what a lot of people do right now, but that’s not going to be what people pay you to do. 

The point of education is to model the practice that is _not_ that of the naive amateur, so I’m trying to do that and show examples that have some complexity to them but are about some generally relatable stuff (which is why this is month six of working on LLMs and film). Also I just want to find some good movies.

When I work with LLMs I feel a million miles away from the literature on cognitive surrender. When I show examples like this, people always reply “Well, you’re smart, you know a lot. Students can’t do this stuff.” But what if the the real lesson of cognitive surrender is meaningless work is easily given up? 

More soon.

## Update!!

I managed to tag a 5% subset of films in the database then run my command line analysis tool on the database, and pardon my french, but _holy shit_. THIS is what I’m talking about. Here I put in “Monsters, Inc.” and got back “The Cabin in the Woods” as a top intersection.  
  
_**Cabin in the Woods**_**is actually** _**Monsters, Inc**_**is a god-tier take.**

[](<https://substackcdn.com/image/fetch/$s_!-VVy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7dcd9d7d-e90c-4418-be98-e5210901427e_1502x752.png>)

I may have gotten really lucky here on this example. I’m sure I did. And it’s actually possible that as we tag more things these sorts of insights could decline. But wow.

1

Noting there is a ton of back and forth in this process…
