---
title: "AI can walk through all the doors at once"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-09-23
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/ai-can-walk-through-all-the-doors
retrieved: 2026-08-13
content: full-text
notes: ""
---

# AI can walk through all the doors at once

*An explanation of why AI can be helpful with sourcing and contextualization and why it sometimes doesn't look that way in retrospect*

## Full text

Immediately after I demonstrate a cool way to use AI to research something, someone usually asks “But couldn’t you do this without AI?”

It’s a weird question in a way. The most honest answer is that I don’t generally choose technologies that make my life harder, and so if I am using AI it’s because I am getting some benefit from it. It’s making me faster, more accurate, more thorough, or getting me to better answers. It’s true that sometimes people delude themselves, but I am not a person with no knowledge of research suggesting these tools might help. This is actually my area of expertise.

I think about someone explaining the advantages of WordPerfect for DOS back in the day to someone who had never used it. So what can you do with it that you couldn’t do with a typewriter? In a way, nothing. The end result is a sheet of paper with words on it. If anything the dot matrix copy looks worse. But you can edit! Sure, says the person, I can do that with an 89 cent bit of white-out. I can print multiple copies! Sure, says the person, ever heard of a photocopier? Maybe you convince the person to use WordPerfect. They try it and complain it takes them 10 times longer to get a simple memo typed. They joke they have to type a bunch of things that are going on a page on a screen and then have to go to a _different_ machine to put them on a page. Efficiency!

And so on. My point here isn’t so much whether AI is useful or not, it’s more that with any technology, good or bad, there’s a point where talking isn’t going to help. The people who find it useful will use it, some people won’t, and it’s fine. For most people, there will eventually be one advantage that finally clicks, but that takes time.

Or perhaps more succinctly, everything is this video clip of Bill Gates trying to explain the concept of streaming internet audio to David Letterman.

## One Big Advantage: AI Can Walk Through All The Doors At Once

That said, I do think there are some big ideas that can help people who know a specific domain well to _maybe_ see the advantage.

I’ve been thinking what those ideas are for digital investigation. I think I’ve got one, and it’s this: _AI can walk through all the doors at once_.

Here’s what I mean by that. A digital investigation is a series of choices that fan out, and a lot of them terminate in disappointment. Even a good choice leads to more choices and you often have to stack good decisions on top of good decisions to get to what you want:

[](<https://substackcdn.com/image/fetch/$s_!kR2D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78460a37-7aee-467a-a5a8-24a12148c8d2_879x595.png>)

Take this question of whether this frame from an old film reel is of the skyline of 1940s Newark.

[](<https://substackcdn.com/image/fetch/$s_!T7A_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa723eac3-6165-40c9-950d-30b5d662ecdd_1600x1357.png>)

How would you check that?

You could search for 1940s Newark skyline and see if there are photos to compare. Or maybe you search for 1940s OR 1950s – would it be that different? Maybe you zoom in on that Federal Trust building, and search Federal Trust Newark. Or maybe the better thing would be to not assume it is Newark and see what city has an Art Deco-ish Federal Trust building. But it’s _federal_ trust, there might be these buildings all over the country. You notice a more unique name in the photo, displayed backwards – “Kresge”. Maybe that’s what you should go with? Local department store, perhaps?

Some of these will get you there and some won’t. Of those that get you there, some are a longer journey than others. Each path is not only about the general path but the terms you choose, how narrowly or broad you start. In this case you actually only need one path to pan out. The process is a series of doors. And once you choose the right sequence the path is obvious, but in practice you spend a lot of time choosing the wrong doors and backtracking.

In this case, however, we give AI Mode the photo, it executes dozens of different searches and comes back with this:1

[](<https://substackcdn.com/image/fetch/$s_!Hieu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7981afc3-f12d-409b-aace-15289736b2cc_1572x975.png>)

Clicking through the provided link on the Federal Trust building gets you here

[](<https://substackcdn.com/image/fetch/$s_!WwWG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63995b80-d960-4b34-9abd-031523f23af5_1600x1307.png>)

And in this case you’re done in less than 10 seconds. This captured film frame is from Newark.

With verification, the search-assisted LLM advantage is _not_ that AI is better at reading clues or skimming individual files than an expert. It’s not. But it can fan out and _try all the paths at once_ and return with the most obvious stuff on all the explored paths. And that takes what might have been 10 or 20 minutes of going through wrong doors and reduces it to 10 seconds.

Once you see the path, of course, it looks like the LLM has not added anything at all. After all, if you search _federal trust newark_ and scan down to result number eight that postcard is right there. Now that you know the path you can see it without the AI. You’re not going to know where the other options would have landed at or how long they would have taken. For any given search an argument can always be made you would have got this anyway. It’s not accomplishing anything you couldn’t do with search! But what you notice over time is you’re just faster. You spend less time on dead ends. You spend a _lot_ less time exploring some obscure option only to realize you missed the obvious thing (happens more than most would admit).

Of course, in the cases you get garbage back, well, you probably have to put the AI on pause and walk through the doors yourself. But it’s not every time, and it’s not even half the time.

Obviously this “AI can try all the doors at once” story is told here through the lens of sourcing and contextualization but I think it probably applies to many things as well. For experts, the value of using AI in critical processes isn’t the depth of analysis or the instincts about what matters, which are just better handled by an expert. But for an initial exploration of a problem space, what I’ve talked about before as “mapping the discourse environment” it remains a uniquely effective tool.

1

I’ll also note that this result contains a straight-up hallucination. I was trying to source some historic film that contained this shot; I got lazy and called it a photograph, AI Mode then conjured a whole backstory about photographs taken from the train tracks that is 100% made up. But when I see that I know that that is part of the _not-at-issue content_ problem that LLMs have with prompts and ignore it. So yeah, it’s hallucinating and it is actually not an issue at all.
