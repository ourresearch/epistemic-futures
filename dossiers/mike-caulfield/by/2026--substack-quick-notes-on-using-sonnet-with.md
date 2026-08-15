---
title: "Quick notes on using Sonnet with moderate effort versus Opus with low effort for a nuanced classification task"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-05-25
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/quick-notes-on-using-sonnet-with
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Quick notes on using Sonnet with moderate effort versus Opus with low effort for a nuanced classification task

*In a word, Sonnet gets very confused, Opus-low does not.*

## Full text

I have a database of 10,000 films and have been playing around with how I can apply AI against it to help generate insights and challenge my assumptions. One question I’ve been thinking a lot about is what percentage of films have a “moral climax”, that is, in what percentage of films the climax involves the protagonist making a moral decision against the stakes of a climax. 

As a simple example of what that looks like, you can consider _The Bad News Bears_ , where I’d argue no matter where you put the climax it’s clearly downstream of Buttermaker deciding, under high stakes, that all the kids on his team should get to play, even if they lose the game. _Rocky_ on the other hand involves no moral decision making at the climax; Rocky’s big decision is mostly _strategic_. He decides that rather than try to win the fight his goal is just to _stay up_.1

Like any exploration, the more you get into it, the more you realize it’s a mess. My idea of the climax of Rocky is that it is when the bell rings, not when the decision is announced, because that is the point where the result of his climactic decision he made 10 minutes earlier in the film when talking to Adrian the night before is revealed. Similarly, many might put the climax of _Bad News Bears_ as being when Kelly Leek is tagged out and they lose the game, and that’s fine, but the climactic decision is made by Buttermaker in the film almost ten minutes prior when he puts in the benchwarmers. In my model of film that moment of decision is the climax, and the other stuff is “how that decision, made at the films highest stakes, plays out.” 

## The batch process

So I’m starting tagging, and the first pass is this. I have a header tag like this:

> For each of the following films, using only your internal knowledge, write a sentence that says “When I was asked if {Title} ({Year}) ({QID}) has a climax that tests the moral character of the protagonist I watched it closely and said [Yes/No], because {reason}” If you feel 80% sure it is a yes, otherwise a no. 

Then there is a batch list, of maybe 40 films in our database:

> Q205321,The Killers,1946  
> Q2247847,Body and Soul,1947  
> Q244865,Champion,1949  
> Q1570221,The Set-Up,1949  
> Q1356753,Stalag 17,1953  
> Q211372,On the Waterfront,1954  
> Q3209915,The Square Jungle,1955

And so on, and we rotate all the films through 40 at a time. Then there is an end to the prompt that look like this:

> When done, put a line of dashes “---------------” as a break, then list in exactly this format:   
> {FilmName}|QID|Y|{100-character or less rationale for decision including character name}  
> {FilmName}|QID|N|{100-character or less rationale for decision including character name}  
> {FilmName}|QID|Y|{100-character or less rationale for decision including character name}  
> {FilmName}|QID|N|{100-character or less rationale for decision including character name}

And that gets read by a python script that uses it to update our database. 

It is designed to try to minimize token use while maximizing accuracy. I can’t use search to do it, because 5 searches per film would get about 10% into my 10,000 film database before expending all my tokens. It’s still pretty intensive. 

In an effort to bring down the cost, I tried two options:

  * Running it under Sonnet instead of Opus, with moderate effort

  * Running it under Opus with low, instead of moderate, effort

Because I can’t waste too many tokens, I tested these by running them each across 2000+ films, then taking a sample of them and checking them with search and Opus medium effort (again, I couldn’t afford a perfect Opus-high test).

## Results: I can’t judge Sonnet’s topline judgments yet, but its rationales are full of hallucinated content (conflation/reversal) 

The judgments were a mixed bag, because they revealed I need to refine my question. Sonnet got overruled by Opus-as-judge, but in ways that called into question what qualifies as a moral decision _climax_. Here are two examples where the Opus check said things were overtagged. It’s wrong on Sunset Boulevard (Gillis gets shot after he attempts to return to a his vision of the moral life, a career where he supports himself). On Rocky III I’ll have to watch that film again, and think harder at what I’m trying to get at here. 

> **Rocky III (1982)** Sonnet: “Rocky overcomes fear to face Clubber Lang, testing courage and humility.” Judge: “Rocky’s ‘eye of the tiger’ tests his will and pride, not morality.”
> 
> **Sunset Boulevard (1950)** Sonnet: “Joe Gillis’s attempt to leave Norma triggers his death — moral cost of his compromises revealed.” Judge: “Joe’s death leaving Norma is fatalistic, not a moral test he passes.”

Where Sonnet was unquestionably not up to the task, however, was the rationales. They were about 6% muddled, when checked against search. Some examples:

> **Bitter Victory (1957)** [verdict Yes] — Rationale: "Captain Leith lets the cowardly Major Brand die in the desert, then must live with the moral cost." Reality: **roles reversed** — Brand lets Leith die.
> 
> **Ivanhoe** [verdict Yes] Rationale: "Frederic must choose loyalty to pirates who raised him vs. law and love of Mabel." Reality: That is the plot of _The Pirates of Penzance_. Ivanhoe's characters are Wilfred of Ivanhoe, Rowena, Rebecca — no Frederic, no pirates, no Mabel.  
>   
> **World in My Corner** [verdict No] Rationale: "Pee-wee Herman's circus performance climax is comic, not a moral test of his character." Reality: No Pee-wee Herman, no circus. It is a 1956 Audie Murphy boxing drama; the protagonist is boxer Tommy Shea.

I’m doing big batches which is part of it (attention fatigue), and some of this might be the subsequent parsing under Sonnet or context getting muddled, though the Bitter victory type error here (which is about a third of them here) here clearly is not. My guess is actually what might be happening is that in cases where a film is niche, the LLM, coming up with nothing, ends up doing a rationale for something else in the batch. Ultimately though, this is the same issue as for hallucinations; Opus has a deeper knowledge set which means it has probabilities to follow even on the obscure stuff where Sonnet does not; for this sort of work that causes problems.

But 6% mucked (vs. none with Opus-low) was a bigger difference than I’d anticipated, perhaps triggered by the nicheness of much of the content and the size of the batches. I thought it was worth letting people know, so here you go.

Opus-low without search grounding on the other hand? Not a single hallucinated rationale:

[](<https://substackcdn.com/image/fetch/$s_!pxAk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcc8c96a-f013-40a8-8164-ef1de24e846e_1302x332.png>)

As always, for people who don’t know — the reason we can surface these errors is when there is search grounding these tools are pretty hallucination free, but at about 3 cents a search on the API I’d need to spend $300 on this one question, and I’m not going to do that, especially when Opus without search or thinking has a surprisingly good record here. Also, this is predictable from what each of these models are, just didn’t think it would be that pronounced.

**NOTE:** On the definitional aspect of this, I think what I want my question to deal with is the difference between strength and endurance towards a goal vs. a character making a specific decision that could go one way or another.

1

It gets complex even here, because I think you could argue that Rocky has a “realized values” climax that suggests the strategy — he realizes what he needs is not a _win_ , but to be seen as someone who “ _went the distance_ ”. Still, it’s not a situation where he has to give up something to get what he needs, or faces a two paths in the woods moment.
