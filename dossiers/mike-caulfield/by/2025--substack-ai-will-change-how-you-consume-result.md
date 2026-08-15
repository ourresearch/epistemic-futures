---
title: "AI will change how you consume result sets (and that's good)"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-04-29
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/ai-will-change-how-you-consume-result
retrieved: 2026-08-13
content: full-text
notes: ""
---

# AI will change how you consume result sets (and that's good)

*I'm using Claude to get "evidence-aware" search results, and I don't want to go back.*

## Full text

## A defense of the humble result set

I think when LLMs first came out the assumption was that the main impact on search would be replacing _result sets_ with _answers_. And that’s been a lot of the shift, and there’s pros and cons to that. 

Sometimes a straight-up answer is what you need. I don’t need a portfolio of sources when I want to know what weight oil my car takes, or who founded the city of Eugene, Oregon. (Was it named after the founder’s first name I wondered? Yes it was. It really was named after a guy named Eugene.) 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

But when it comes to _research_ , result sets are invaluable. And augmenting research — not providing answers — is at the heart of knowledge expansion. Result sets, as I’ve argued with my co-author Sam Wineburg, help us to _read the room_ on a subject — seeing what various sources are contributing to a discourse, and giving us a sense of what’s settled, what’s debated, and how those debates break down. Reading a result set gives a view of a subject that resists easy summary, and _prepares us to enter the conversation ourselves_. Even when questions are fairly simple, result sets resist the tendency of AI answers to puree sources and insights into an AI information smoothie, a response which goes down easy but disguises its underlying ingredients and contradictions (yeah, I’m pushing this metaphor, live with it) in ways that aren’t always helpful.

So, just because we can get AI answers doesn’t mean we should abandon result sets. To do so would treat human knowledge as a finite pool, rather than a foundation to build on, rather than pieces to rearrange. We won’t need it for as many things as we used to, but we’ll definitely need it.

Recently I’ve been thinking of some possible ways that LLMs can enhance result sets, in particular through being “evidence-aware”. And I’m starting to think there’s a lot of future left to be had in AI-augmented traditional search, should we want to pursue it.

And in case I’ve not been clear, we definitely should pursue it.

## From result set to sources table

The [SIFT Toolbox](<https://mikecaulfield.substack.com/p/minor-sift-toolbox-for-claude-37>) I built has an output I designed called a _sources table_. I think it shows a hint of what search in the future will be like. 

What do I mean by that?

A good example came up today when I wondered where Trump had gotten a claim — one he first made in 2018 but apparently rehashed recently. The claim was that Japanese regulators dropped bowling balls onto imported American cars as part of a safety test designed to cause them to fail. 

So two things. First, this isn’t true. Japanese regulators don’t do that. Second, Trump _probably_ just misheard something in conversation 20 years ago and it became a core belief as he repeated the story over time. Occam’s razor there.

But a good searcher doesn’t simply go on instinct. The “F” in SIFT requires that we see what other people have said about this before we lock into our own conclusions. And so we turn to search to do that.

## Traditional search

The way I’d normally do this in search for something like this — my query below is a bit wordy, but you get the point. I search for something like _origin bowling ball story_ or _where did trump hear bowling ball story_. (I know the stop words don’t get counted but I tend to throw them in anyway for good reasons I can explain later if you want, just ask me in the comments).

So you do that search and… you get a _great set of resources_ actually. It’s really good!

But look at how it is ordered below and get the feel of what it’s like to skim this trying to learn more about specific theories about _**where this bowling ball story came from**_ :

[](<https://substackcdn.com/image/fetch/$s_!CsEb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Face87cfb-91ef-46d5-bf28-1bdc78c6d7e9_898x783.png>)

Each of these _probably_ has information about where Trump might have gotten that story, and normally the procedure is to go into each one, skim or search to see what possible origins it might mention, then go to the next result. Click in, skim, go back. Click in, skim, go back. 

This process has some things to recommend it — for one, the need for users to click through each link to see if the page provides insight is better aligned with ad revenue models. So I want to raise that issue as something outside the scope of this post, but a larger issue. 

From a user experience perspective, though, it’s a clunky search result and a horrible process. The searcher is already aware of _some_ theories but not _others_ , but there’s no way to get a snippet that indicates what theories each page has. So what the user has to do is click through multiple links and see if what they see there is the same story as the last one they clicked or if it’s something different.

## Sources Table in SIFT Toolbox

If you just go into Claude with no larger instructions active and tell it to make a table of links you already get something that is more useful, providing a summary that links to your question directly:

[](<https://substackcdn.com/image/fetch/$s_!ysUW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2e34ff9-9b17-4be6-ac55-8ef391d95945_764x645.png>)

But as you skim through this that you realize you have the same problem as the search results. As a researcher, what you want to make sure that you know _all the theories_ out there, and make sure that for each theory out there you have at least one page you can click through to see more information (and perhaps use as a citation). Your unit of research is not really pages — it’s underlying facts, claims, and theories. It’s the stuff you have to collect, check, and integrate as you build your understanding, not the pages themselves.

That’s what SIFT Toolbox’s “sources table” is about. So, for example, I start a session by uploading this text:

[](<https://substackcdn.com/image/fetch/$s_!AZQi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9ce3a10-6aa2-47bc-a0a0-169bf71cb921_633x209.png>)

And if once the system runs the initial analysis on it I type:

[](<https://substackcdn.com/image/fetch/$s_!2gwL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53814898-d4e3-4b41-acb9-8f17195d9e5e_571x90.png>)

That will produce this:

[](<https://substackcdn.com/image/fetch/$s_!Du1d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F938370c5-6215-493d-bb3d-57c03fad3953_882x1739.png>)

Now, note the difference here — this search response is still a set of results, but is not organized _solely_ as a set of sources. It’s organized by your _investigative needs_. By the pieces you need to explore what linguists call the QUD — the question or questions under discussion.

You have a list of the different known explanations for Trump believing this story, and for each one you have a summary of what piece of evidence regarding that that the page brings to the table. Obviously, many pages cover multiple theories, but with this design I know if I want to know more about the David Letterman claim I can go to the _Spin_ magazine links, and if I need any industry reaction I can click through to _NBC News_. You’re looking at sources, but they are organized according to the needs of the sense-making task you are engaged in.

For this Trump example the table was formed around the different theories about the bowling ball, but in other cases the sources table forms around _different elements of a story_ , and describe what unique element the source brings to that story/context. 

For instance, there is a test I do that uses this screenshot as an input, a snapshot of a video from the 1972 Olympics gymnastics competition and a description that reads:

_“The banned ‘Dead Loop’ of Olga Korbut in the 1972 Olympics. It was the first and last time the trick was performed.”_

[](<https://substackcdn.com/image/fetch/$s_!Ae9a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73a1db55-45c7-4c1b-8b6b-7a609f6213f3_635x631.png>)

Ominous!

Now this isn’t true, as the automatic fact-check SIFT Toolbox will tell you. Variations of this move were used up until 1985. It was banned for safety (mostly) but it wasn’t as movie-level dramatic as this makes it out to be. 

If you ask for a sources table here, SIFT Toolbox shows what each source might bring to the larger context you are constructing. For instance, the result set shows that _Wikipedia_ can give you the overview. That _Gymnast Gem_ confirms how revolutionary the move was, and mentions another gymnast added a twist to it in 1977. That _The Sun_ , which is not a great paper but probably OK here, gives the names of five other gymnasts said to have done it after her. That _Buzzfeed_ provides a specific date (1985) when it was last done and _DNA India_ seems to be the one source that has Korbut’s more recent comments on what she thought of the ban. And that _FloGymnastics_ lists nine other moves that were either banned or fell into disfavor, providing some larger context.

[](<https://substackcdn.com/image/fetch/$s_!2JwK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96a3aead-85c4-44bb-a590-40cb692f0fb1_730x2042.png>)

## This is a quiet revolution in search, actually

I’ve been searching documents since the days of command-line Dialog (I couldn’t find a Dialog screenshot from 1992 so I grabbed this 2007 one instead). 

[](<https://substackcdn.com/image/fetch/$s_!JX6g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd716b991-3f68-4122-a32d-c8079433b147_811x474.png>)

Search has gotten a lot better over the years, and the improvements are too many to name. But I think this ability to structure and preview result sets in this evidence-aware way is one of the biggest shifts since full text search.

Part of the reason I know it’s a big shift is that _I’ve_ become a bit addicted to searching this way, using the SIFT Toolbox sources table. I am, after all, a person who loves traditional search, who made teaching traditional search my life, who along with Sam Wineburg wrote [one of the definitive books](<https://www.amazon.com/Verified-Straight-Better-Decisions-Believe/dp/0226822060>) on using traditional search for sense-making. I am not joking when I say that a search curriculum I co-designed has been offered to over a million people around the world. 

And yet I find myself making this my first stop more and more.

As you can probably tell from this post, I still lack a language to talk about this, jumping between evidence-aware, claims-aware, sense-making, investigative needs and smoothie analogies. I hope I’ve gestured clearly enough in the direction of my thinking that you, the reader, can see something of what I’m seeing here. If not, I’ll be coming back to this issue in a future post, when my ideas are a bit more settled. 

P. S. if you want to try the sources table feature, there’s [instructions for using the Toolbox here](<https://mikecaulfield.substack.com/p/minor-sift-toolbox-for-claude-37>). I recommend that you use the $20 version of Claude and run the toolbox under Sonnet 3.7.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
