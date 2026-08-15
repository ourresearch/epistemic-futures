---
title: "I Finally Understand Why LLMs Suck at Writing Prompts (And It Might Be Fixable)"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-07-11
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/i-finally-understand-why-llms-suck
retrieved: 2026-08-13
content: full-text
notes: ""
---

# I Finally Understand Why LLMs Suck at Writing Prompts (And It Might Be Fixable)

*I've wondered a long time why LLMs are so bad at writing prompts for users to use when they seem to be so good at prompting on the fly. It turns out the two things are related.*

## Full text

You may have noticed that LLMs suck at writing prompts. If you write a simple prompt like this:

> Produce near comprehensive list of all notable films throughout film history that have a “old dark house” or “old dark house adjacent” plot device. It typically involves   
>   
> a) the gathering of a group of people at   
> b) a mysterious or neglected or isolated property, and   
> c) a mystery emerges after their arrival or surfaces from the past that must be solved   
>   
> [details of how to do the scan removed]

it will work. If you ask an LLM to write a prompt to do that for you it will invariably write extrapolated garbage like this:

> The Old Dark House device assembles a set of people at a mysterious, neglected, isolated, or forbidding property, then forces them to confront a mystery that either **erupts after their arrival** or **surfaces from the property’s / family’s past**. Enclosure is thematically central: the group is, to some meaningful degree, _bounded_ — by weather, by a will-reading, by an invitation they can’t easily refuse, by a breakdown, by nightfall, by the isolation of the place itself.
> 
> A film qualifies as **core ODH** when it satisfies all four beats:
> 
>   1. **The property is the engine.** A mansion, manor, castle, decaying estate, isolated house, or equivalent forbidding structure is the primary setting and an active presence in the story — not merely a backdrop.
> 
>   2. **A gathering occurs** , via one of these three vectors (tag which one, or which combination):
> 
>      * **(a) Family gathering** — relatives convened by inheritance, a will-reading, a reunion, a summons, a death.
> 
>      * **(b) Strangers gathered** — a group who don’t (all) know one another, drawn together by invitation, contest, chance, or design.
> 
>      * **(c) Shelter-seekers** — travelers forced to take refuge from a storm, breakdown, or other exigency of the elements.
> 
>   3. **The group is bounded / trapped** , at least provisionally.
> 
>   4. **A mystery drives the plot** — an emergent threat (a death, disappearances, a hidden presence, picking-off) _or_ a buried secret exhumed from the past — and the gathered people must confront, investigate, or solve it.
> 
> 

This prompt looks impressive but in practice will exclude many things you care about. Take the phrase “the gathered people must confront, investigate, or solve it”. So, yes, sometimes the entire group of people there must solve the plot, but often a detective arrives after the murder occurs and the people are merely suspects not active solvers. Under the extrapolated definition all of those dozens of detective driven films are out. 

There are some good things in the LLM produced prompt. I like the clarification that the mystery must drive the plot. But the prompt will fail at what I need it to do which is surface the grand variety of films with this structure. If you let the LLM write your prompts for you it will lead to embarassing exclusions repeatedly. 

It will also lead to bizarre inclusions. I needed some director style prompts for my research project [plot.fyi](<https://plot.fyi>) recently. Since there were two hundred of them I wanted for classifications I had Claude write them, and I thought I was pretty insistent that they be very high level (“Is this movie Hitchcockesque, that is reminiscent of the films most identified with Alfred Hitchcock?”). 

When I ran these classifier prompts against the film vault, it ended up saying things like one out of every 10 films in the vault, across six continents and 120 years, resembled the films of Chris Columbus, the director of _Home Alone_ , _Mrs. Doubtfire_ , and the first two Harry Potter films.

Now this isn’t quite as bad as it looks — my film database is denser when it comes to more recent films, and I try to use the director tags in as fuzzy a way as possible, because the point is not precision, but to create broad categories of film. 

Still when I asked Claude to go through and simple ask for each film in the batch “Can you make any defensible case that this film resembles the films of Chris Columbus, the answer for two out of three films that were tagged using the Claude written prompt were “No, no defensible case at all.”

[](<https://substackcdn.com/image/fetch/$s_!Aq1a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1db3da8c-1469-4aa4-acbf-26b34985d567_783x477.png>)

I looked through the decisions, and all the ones I sampled showed that the tag had indeed been overapplied. Why? See if you can spot the problem with the classification prompt Claude was running, the prompt it had written and stored based on my request:

> Resembles the work of Chris Columbus: warm, sentimental mainstream family entertainment; plucky kids and harried parents in cozy suburban or holiday settings; broad comic set-pieces softened by earnest heart and reassuring resolution. (Home Alone, Mrs. Doubtfire, Harry Potter 1–2, Adventures in Babysitting)

I was a bit shocked. This is a horrible prompt! It proposes something that is probably a good set of search terms for finding “Columbusesque” _candidates_ but it’s a horrible set of inclusion criteria. If you feed this prompt to an LLM and ask is this like the works of Columbus, as defined here you’re going to get thousands of films because that list of things after the name (warm, sentimental family entertainment, broad comic set pieces, cozy suburbia) applies to thousands of films.

Whereas if you just tell the system to make 200 director prompts by having Python spit out “Is this film reminiscent of the films of ________?” in a loop you will get better performing prompts than if you tell Claude to handcraft you 200 director prompts.

Which is super weird, right? In fact, it’s beyond weird, it’s _bizarre_.

I wondered for a while what was going on. After a particularly painful experience with Claude induced prompt bloat this morning, I hit on the answer.

In modern LLMs there are really two types of prompts:

  * User prompts all of which are _contract prompts_ , since the user specifies what they want. This is used to create the metric for success and are the basis on which the LLM extrapolates what sort of output or process would satisfy the user request.

  * _Intermediate prompts_ , which are the LLM built extrapolations of the request based on the contract prompt. The system builds these understandings internally because what the user usually asks for is not detailed enough to operationalize. For example, in the work I do the LLM is going to need a lot of examples and search terms not supplied by the original contract prompt. Part of the _value_ of the LLM is the extrapolation or refinement of selection criteria.

At least for the work I do on plot.fyi, the ideal contract prompt has to be at a level of generality so that the model can adjust to findings as it goes. If during it’s process it stumbles on a line of detective driven old dark house elements it has to be able to see that those fit, and adjust its intermediate definition. At the same time it has to be generating internal prompts at a level of detail that it can derive search terms and develop search strategies from them.

The reason LLMs suck at writing prompts is _they write the intermediate prompt as the contract prompt_. They put in all the extrapolations they need to operationalize the request, because that’s how the architecture built into thinking mode understands prompting. 

This is fine if they do this for an internal, intermediate prompt, because they are _allowed to violate_ their own intermediate instructions if they prove fruitless or ill-conceived. But as a contract prompt it is a disaster.

Perhaps other people came to this earlier than I did. I had a sense of it before, but for me it came into focus at this level of clarity (contract prompt vs. intermediate prompt) this morning. Looking at it it seems to me there are some ways that one could use this insight to immediately improve LLMs or guide people in LLM use. Still parsing this all out but let me know if the explanation above is understandable or not.

* * *

  
_**Note on my research project Plot.fyi**_

 _I run[plot.fyi](<https://plot.fyi>) as a personal research project at my own expense. It does not make a dime. It’s an experiment that helps me understand in depth the strengths and weaknesses of using LLMs as classifiers (which is where the bulk of LLM productivity is likely to come from, classification tied to routing and action). _

_If you like what I write, what I would love you to do is go to Plot.fyi and find a film to watch. Or send it to a friend who used to talk about films they like and now just wants to rave about the decline in fertility rates or how much water a prompt uses. Maybe it won’t help you. But getting reengaged with film helped me a crucial time in my life and I’d love you to give it a shot._

[](<https://plot.fyi>)
