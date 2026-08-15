---
title: "Building an \"Event Checker\" for a Hallucination and Error Research Project"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-07-06
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/building-an-event-checker-for-a-hallucination
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Building an "Event Checker" for a Hallucination and Error Research Project

*A couple tricks*

## Full text

I want to start looking at ways to reduce error and hallucination via prompting techniques. The problem with such things is it’s very time-consuming to go through LLM output and find every error, which makes figuring out if the changes you made helped or hurt.1 People who haven’t checked things for a living radically underestimate how long it takes to check something rigorously. So the problem is if I make two versions of something to see which hallucinates less, and it takes 60 minutes to verify each output, and I want to do that three times to make sure I’m not just looking at a lucky run, that’s 6 hours of work to figure out the impact of one change. 

I suppose that might be fine if I had research funding and a room full of undergrads, but it’s just me here. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

## The Event Project

Let me start by talking about the larger project, an LLM-produced calendar of interesting events in a given place. Why am I trying that? I guess I was thinking back recently about the early days of Web 2.0 experimentation, and particularly [Jon Udell’s](<https://blog.jonudell.net/>) focus on social event discovery back around 2006 or so. Part of his fascination with calendars was his instinct that good social media should connect us to our communities and surroundings, not disconnect us from them. For Jon, the focus on events was a way to test out a variety of theory and practice about syndication, self-publishing, inclusion by reference, etc. while doing it in the service of building our non-virtual lives.

So anyway, I thought I might like to play around the next few weeks making an event finder. I started one a few days ago, but ran into some hallucination problems when I turned it to situations where there was less stuff to pull from. So how to figure out how to minimize hallucinatory behavior, so I can talk more authoritatively about how to mitigate them? 

This may seem odd, but I decided to start by building an event fact-checker. I’ve decided to stop sharing full prompts until I have them where I like them, but the core of the prompt at present is this:
    
    
    ## Each round
    
    Take the rows {#1} through {#5} of the checking queue and use web search to check each element (including description). For each element that checks out place a green check in the table cell, if the item cannot be verified or is incorrect, write a note.  For generic links, if you have a better and more direct link, provide it in the cell (examples might be the official festival page, or a Wikipedia page on the event, or failing that a specific page -- not a huge table-- from a travel agency or site). For the date, from the source you used to verify quote the entire phrase (if there is a phrase) containing the date (including the year if it is in the phrase) and link it to the source that you used to verify the date.
    
    Note: Row numbers are variables and are usually iterated each round after initial startup; see iteration rules in "next checks" template.

I then iterate it as I discussed in the post on Friday, and get this:

[](<https://substackcdn.com/image/fetch/$s_!TLah!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f17954f-f6ba-436f-bf3b-9e677508ed1e_1529x775.png>)

It still requires a bit of follow-up. Sometimes it can’t independently verify an event. Other times it gets a bit aggressive with calling things errors, or makes a judgment call that’s just a judgment call (for example, deciding the “fan night” the night before a hot rod rally doesn’t count as the starting date of the rally). But it seems to do pretty well, and should allow me to try a variety of prompting techniques and see which ones cause more errors and hallucinations (this one was blessedly hallucination-free).

## One Dumb Trick: Make the iterative canvas output also a “Left To Do” list for session portability

I did use one dumb trick of note. One reason the event fact-checker works is it takes five events at a time and runs searches on each event. Of course that dramatically scales up your input tokens, because for each event you’re processing ten or so web sources. And that, in turn, means your session token limit in Claude is reached pretty fast. In my list of 70 or so events, I can get through maybe 20 before I hit a session limit. 

People hit this sort of thing quite a bit, and even where enforcement of session token caps aren’t as aggressive as Claude it’s still the case that a session with a lot of search carries around a lot of context that is not necessarily helpful and gets quite expensive. 

What I did to deal with this is I turned the output format into a running to do list, and had the prompt recognize when I upload a half-completed chart I wanted it to start from where the last session left off. So as a first step it takes a list of all the events you upload and makes a table where all the fact-checking cells contain only a “-”. Then as it checks things it fills those out, but you can see how far it’s gotten, as here:

[](<https://substackcdn.com/image/fetch/$s_!VCFQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F627a9774-4ad5-498f-8eb2-cdd16d93e893_1739x965.png>)

Those last two events (and all the ones below them) are undone. 

Now if you are starting to get close to session limits, you can copy that artifact…

[](<https://substackcdn.com/image/fetch/$s_!FtEI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F983f8958-6d0e-4b53-adab-c2f088885ee3_799x359.png>)

And paste it into a fresh session. The session will recognize it is partially completed, and find the last completion point:

[](<https://substackcdn.com/image/fetch/$s_!9qIR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa16692cb-0695-4f01-8e2c-44357fdb1ff0_986x740.png>)

It will then start from there, but without all the context window baggage of the searches it used previously. 

[](<https://substackcdn.com/image/fetch/$s_!RKFu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F527e2974-1919-4e7a-b2a2-79200817bc4f_962x476.png>)

Obviously if you are just using the API to do this you can ditch the context window entirely after each row check, but I remain interested in what’s possible through directly using the web interface platforms, because in my mind teaching people to use that is the way to create the broadest and most small-d democratic impact. 

You can cook your own solution to use this technique, but here’s a snippet of my prompt:
    
    
    ## First Response 
    
    When a chat has just started, use javascript's console.log and datetime to fetch the current date but not time. Pay particular attention to the current date.
    
    ## User Uploaded Fresh List Condition
    When given a list of events with dates, times, descriptions, locations, and links you will first create a monster table that for each event has each of these elements in a column. This is the "checking" queue. You can use the Markdown file in the knowledge base as a model of what it looks like partway through a check. 
    
    At the end of producing this you will see if you have the same number of rows as the input (uploaded) table. If you do not, you will figure out where you stopped and offer to continue to add to the table.
    
    ## User Uploaded Partially Completed Queue Condition
    When given a list that looks like a partially complete queue from this process (perhaps from another session) start by reproducing the table exactly as an artifact. 
    
    At the end of producing this you will see if you have the same number of rows as the input (uploaded) table. If you do not, you will figure out where you stopped and offer to continue to add to the table.
    
    Then figure out where the fact-checking process was stopped and start from there, checking the next five events.

## Final Note: Why not build the plane out of the black box?

There’s an old joke about the black box that they recover from airplane crashes. If the black box always survives the crash, why not build the plane out of the material of the black box. Problem solved. 

So the question comes up if the fact-checker is so good at finding error, why not just apply the fact-checker to the output the first time? 

To be quite honest, that might work. I think people radically underestimate the effectiveness of a “layered output” approach, where the result of an LLM gets checked by another LLM process and corrected before it is shown to the user. It feels less elegant than getting it in one go, but my experimentation shows it to be very effective. It’s effectiveness is one reason why I always think it’s weird that people think hallucinations can’t be mitigated. I’m not saying they’ll be “solved” but in my experience a layered approach gets most of them ironed out.

That said, I think it’s still interesting to see what sort of prompting tends to dial them up. Is it asking for too many results? Exhausting too many searches in a row so that the system starts trying to conserve resources? I just feel it would be good to know such things.

Now on to seeing what seems to make hallucinations worse, and what makes them better…

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

1

I am going to ask people to consider if they are thinking of commenting “Why don’t you just get the events without an LLM, then you won’t have to check your work?” that while that does say something about LLMs it may also say something about the quality of your work. It’s true that LLMs fail in particularly weird ways, and I would say in general have somewhat more error, but everybody needs to check their work, regardless of how it is compiled.
