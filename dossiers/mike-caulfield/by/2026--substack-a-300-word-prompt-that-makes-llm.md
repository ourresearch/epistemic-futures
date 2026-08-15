---
title: "A Claude Skill that Makes LLM Paragraphs More Bearable"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-04-15
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/a-300-word-prompt-that-makes-llm
retrieved: 2026-08-13
content: full-text
notes: ""
---

# A Claude Skill that Makes LLM Paragraphs More Bearable

*And they said studying Christensen's rhetoric of the sentence was a waste of time...*

## Full text

**Update:** I’ve made this into a skill for Claude as well as a prompt. Find the skill text file [here](<https://checkplease.neocities.org/jamesian/skill>); you can paste it into Claude and ask it to make it into a skill. If you want to use a prompt, the prompt is [here](<https://checkplease.neocities.org/jamesian/prompt>). These both work best with a paid version of Claude.

I called the skill “jamesian” not because I think it could ever write like Henry James. That would be absurdity. I doubt in fact there will ever be another _human_ who can write with pure control of the English language with that particular baroque precision. I called it “jamesian” because I think a world where prose on the whole is a _bit_ more complex and where people read more complex prose is a better world with better thinking in it. And I worry that the punchy short sentences that LLM’s give us and that we are now consuming daily move us increasingly away from that world.

So I call it “jamesian” not because it could ever be produce a shadow’s shadow of that craftsman’s work, but because my desire is that our prose (and world) becomes a “bit more Jamesian and a bit less LinkedIn,” and if this can contribute to that even a bit, so be it.

**ORIGINAL POST FOLLOWS**

Years ago, back in the 1990s, I studied literature and linguistics at Northern Illinois University. Part of that degree was in rhetoric (it was a mixed degree that was about the analysis of literary prose and narrative structure, back in the heyday of stylistics and narratology). NIU happened to have been the teaching home of a guy in the 1960s that believed the key to better writing was to teach something he called generative rhetoric. His core belief, over many many years and honestly a bit of ridicule by more serious people was that sentences structures were templates for thought and by teaching what he saw as the “generative” power of sentences — the way that sentences open up spaces to _add things_ , that students could become better writers. Stick to subject-verb-object and you’ll have subject-verb-object levels of thinking. Learn the variations of structure and suddenly the sentence is asking you what it is _about_ , what it _needs_. 

His name was Francis Christensen, and his work is mostly a footnote in the study of rhetoric. He’s the sort of guy you can write a unique dissertation on because he’s the sort of guy no one writes their dissertation on. Including me, as I ditched my PhD for a life in educational technology.

I have exactly two things I took with me from NIU. The first is my wife, Nicole, the reason why I left that PhD, got married, and had wonderful kids and am currently in my 29th year of marriage. Best decision of my life. 

The second is a beaten-up copy of _The Christensen Method,_ a textbook that the library was jettisoning at one of its library sales while I was there. 

[](<https://substackcdn.com/image/fetch/$s_!ieGG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc3ff503-69bf-4db1-a5e9-cae841d54aa4_2268x2350.png>)

This is the most puzzling decision, keeping this book through thirty years of moves and spring cleanings. I’ve never used this thing. I’m not a Christensen superfan, or even a fan. I think it just felt sad to me, the library ditching this book from one of their weird 1960s residents, a guy who probably felt like getting that post at NIU was going to be the steppingstone to the whole world eventually realizing that they had been teaching paragraphs when they should have been teaching how to add medial free modifiers. I’m a sucker for people like that, I really am. 

Get on to the point I guess. 

So, I’ve been building this wiki to put together some initial research notes for a podcast I’m doing. The notes aren’t the end product; I just want something to run out and summarize what different people thought about a movie, note where the particular score of it is rated compared to other scores by the composer; learn things like whether the director had worked with these people before, how it fits into film history etc. And I thought the LLM tone wouldn’t bother me, but it started getting to me. The “It’s not X, it’s Y” etc. I wrote up a bunch of instructions for the wiki that stopped the worst offenses but it still felt off. Like this paragraph:

> Blow Out is set and filmed in Philadelphia — home of Independence Hall, the Liberty Bell, and the founding documents. The choice is not incidental. The film's climax takes place during a **Liberty Day celebration**, with fireworks and patriotic festivities providing the backdrop for Sally's murder. American political ideals were articulated in Philadelphia. In Blow Out, those ideals are shown to be hollow.

We know this style. If you know your ancient rhetorical forms this is all _paratactic_ , and it’s one of the defining elements of LLM style. The LLM places thing in sequence and lets the reader build the mental hierarchies. Subordinating clauses are risky; they start to show relationships and you can get relationships wrong. The last two sentences here are an example of this. These two sentences when assembled in my mind do make a perfect point about the ending of Blow Out, but structuring them without any subordination or controlling idea is _safer_ because it’s me that actually puts them together. [Paratactic structures](<https://www.google.com/search?q=Paratactic&rlz=1C1ONGR_enUS1168US1168&oq=Paratactic&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBBzE3NmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8>) have _give_ , they assemble like legos, and half the time they leave the assembly to the reader. For a machine trying not to make a mistake or spend a lot of clock cycles keeping track of hypotaxis, they are an efficient safe pattern. And they are, to paraphrase the great David Lynch line, “boring as shit”.

Anyway, I couldn’t get my de-LLM-ification to go the extra mile, and it suddenly occurred to me that while Christensen was solving the wrong problem for students, he was solving _exactly_ the problem the LLM was having. So I wrote a little Christensen-izer. 

NOTE: When I took it out of silent mode so you folks could watch it, it got a bit too aggressive and tried to be Henry James, so I’ve been adding some stuff to put the brakes on it. Also, I’m horrible at leaving things alone, so it’s no longer 400 words, sorry, lol. More words works slightly better, so I added more words, particularly so people could have presets   
  
**Please don’t see this as a “magic sauce” but as a backbone that you can tune to your own preferences. Dial it up, dial it down. Limit subordinate clauses or go wild. It’s a style skeleton, it’s not a recipe:**

[PROMPT](<https://checkplease.neocities.org/jamesian/prompt.md>)

It’s not meant to be aggressive. Getting too aggressive would trade one problem for another. But it does actually work really well. Here’s that paragraph from above. This is the original, already de-LLMed a bit from my other pass, but still annoying:

> Blow Out is set and filmed in Philadelphia — home of Independence Hall, the Liberty Bell, and the founding documents. The choice is not incidental. The film’s climax takes place during a **Liberty Day celebration**, with fireworks and patriotic festivities providing the backdrop for Sally’s murder. American political ideals were articulated in Philadelphia. In Blow Out, those ideals are shown to be hollow.

And here is the result:

> Blow Out is set and filmed in Philadelphia, home of Independence Hall, the Liberty Bell, the founding documents. The choice is not incidental. The film's climax takes place during a Liberty Day celebration, fireworks and patriotic festivities providing the backdrop for Sally's murder, American ideals furnishing the scenery for their own negation. The place where those ideals were first articulated becomes, in De Palma's hands, the place where they are shown to be hollow.

Maybe it’s preference, but I don’t think so. The second one is just better, for exactly the reasons Christensen detailed. First it has a rhythm that doesn’t feel like someone ca-chunking the office auto-stapler in the cubicle next door. But more importantly, as Christensen noted, opening up the sentences forces focus and (slightly) more complex structures of thought. The focus here is not actually the film, it’s De Palma’s treatment of the subject (“in De Palma’s hands”). The patriotic festivities aren’t merely a lego piece the user slots into a point, they are the scenery of American idealism forming a backdrop to it’s own negation. Corny? Maybe. But actually I don’t think so. Corny only in it stops handing you the bag of LLM legos and says this is how I’d build it.

It’s small, but if I figure out a way to run the article paragraphs through this maybe the prose will give me less of a headache. **Right now it only does one paragraph at a time though, so that’s a challenge.**

Here’s me going through multiple paragraphs in a video:

And here’s my favorite rewrite it produced, on how Invasion of the Body Snatchers differs from previous conspiracy thrillers:

> The film opened December 22, 1978. Jonestown had happened five weeks earlier, the mass death of over nine hundred Peoples Temple members at a compound in Guyana, most of them from the Bay Area, where the film is set. Kaufman has been direct about the overlap; they were people from San Francisco looking for a better world who found themselves, as he put it, in “pod-dom,” and it was fatal.
> 
> The conspiracy thriller had been running on the assumption that the threat was institutional and impersonal, a matter of agencies and cover-ups, forces that acted on people from above. Jonestown put a floor under that. The threat could also be voluntary, communal, a thing you walked into with your neighbors, seeking transcendence, finding oblivion. Body Snatchers caught the bounce.

I don’t love that last sentence, but if you watch the video you’ll see that it got here from something much blander and less focused. 

By the way, if your still using AI-detectors the double pass I make in the wiki (the standard looking for LLM idiom followed by this) produces prose that the “detectors” rate almost certainly human-produced. If 15 lines of Christensen can do that, the detectors aren’t long for this world I think.

I wrote this post in a bit of a winding way because it’s just a neat thing I discovered a short time ago. I do plan to refine it a bit and then I’ll write a proper post that gets to the point more quickly and shows a refined, more robust version.
