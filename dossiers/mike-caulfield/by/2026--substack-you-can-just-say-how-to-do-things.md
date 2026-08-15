---
title: "You Can Just Say How To Do Things: A Radical Approach to Expert Prompting"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-04-27
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/you-can-just-say-how-to-do-things
retrieved: 2026-08-13
content: full-text
notes: ""
---

# You Can Just Say How To Do Things: A Radical Approach to Expert Prompting

*The magic tricks phase of prompting is over. Just focus on how to do the thing.*

## Full text

I’ve been working on a film analysis tool for a site called “Couch to 4k”. It combines something I used to do a million years ago in grad school (narratology and stylistic analysis) with my interest in LLMs. It’s fun.

So I was working on it this weekend. In building it, I was being lazy and getting into a cycle of having Claude build the prompt for me, look at the results and critique them. I’d give more feedback, which Claude then used for revision. And what a beautiful prompt it was producing. Multi-step, loopbacks, little code-based checks, quality gates. Everything super clear. It had a definitions section! Each step had multiple bullet points, quality criteria.

And when I ran it, it sucked. And as I had Claude build it out it kept on sucking more and more. The analyses kept getting worse. At one point it told me the climax of Rocky was when Rocky says “Cut me” to get back in the ring, not when Rocky is still standing at the bell.1

So this thing was getting worse and worse and I started to get into that very oppositional “for god’s sake” mode with it. It mucked up Cast Away, it mucked up Invasion of the Body Snatchers (1978). These are difficult films to map to be honest. But all that structure in the file just made it focus on weird little details, and error out in bad ways.

By a stroke of fate, I ran out of tokens. And in my frustration I thought, well, I have 40 minutes until token renewal, so let’s just sit down and write the process I use to map out a film. And I started writing. First, identify possible themes. Keep it fuzzy for now. Cast Away has fixations on time, and control, and loss. Now three theories about the difference between what the main character wants/does and what they need/should do, and how that shifts as a result of crisis. And so on. I just wrote it out. 

And man, did I. No real editing, some cleanup. But it was in the end something that looked more like a lesson to students plus some homework than a prompt, and a bit half baked at that.

[](<https://substackcdn.com/image/fetch/$s_!gGXN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33c1256b-05c9-4aa3-959b-f25ba4409ab4_885x536.png>)

I took about an hour and a half to write it, just going manually through some examples, thinking through what I was doing, writing more clearly or broadly. I didn’t think about Claude at all. After an hour and a half I had tokens, and I dropped it in and ran it

[](<https://substackcdn.com/image/fetch/$s_!sVJk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F194e3e92-12f1-4c6b-8406-e42f8b187841_1010x568.png>)

And it worked. Not perfectly every time, which is good. A world where my tool only discovers my interpretation of Cast Away would be boring. But it did find my interpretation within the runs, and the other interpretations it did were pretty solid. 

I know this but like a lot of people, I still forget sometimes. You want to build something great? Focus on how you do the thing. The prompting is secondary.

I’m still fiddling with this to get it right, but let me repeat. There is almost no “prompting best practice” in here. I mean, I wrote a thing with a _preamble._ And then I just said what to do:

[](<https://substackcdn.com/image/fetch/$s_!cbWA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192f6466-e8a4-4478-87d9-d510ca51bee5_831x486.png>)

Note that this is a bit stream of consciousness! Actually more than a bit. It’s _embarrassing,_ really. I tried to have Claude cut it down to less words but it’s still 3,000 words of me babbling how I think about the problem and how I do the task.

And here’s the result:

<https://claude.ai/share/a7d1a422-8dda-47cd-b3d6-087e8510a7b5>

I don’t know if you can see this, but that is a beautiful analysis.

## Stop thinking about how to prompt, and start thinking about how to do things. 

So how did my prompt work? My terminology is muddled, I don’t use consistent terms. I think some of my concepts aren’t locked in. 

But I have a method for _doing the thing_. When analyzing films, I start with themes, then I look for whether the theme expresses a concept that highlights a distance between an approach the character is taking and one they should be taking. I use the themes to help find the climax. For the climax. I choose a climax that fits the themes, has high stakes, and feels like the film was set up to arrive at. I check the themes first because in a complex film like Cast Away there are multiple points people think are the climax, and theme-climax fit is a way of dealing with that. 

Then I ask the question is the main character’s approach to things tested by the climax. If we have that triangle — where themes and approaches to the problem are tested by a high stakes event, we feel pretty good.

If you’ve never analyzed film, this will seem unnecessarily complicated. The climax is the climax. It’s when Rocky wins, right? (Nope. Rocky doesn’t win and the climax isn’t when he loses either). The thing is I’ve done this task of analysis hundreds of times and I know where all the traps are. I know what to do first, and what to do second. I know how I think about it. The hour and a half I spent on the prompt was me thinking through how to give the best version of the process. Writing down what I think one should do, then walking through that and asking — is this going to get confusing? Then revising. And so on.

On the other hand, if you’ve looked at all the advice about prompting, the prompt construction piece will seem almost _disturbingly_ simple. Figure out the understanding you have about something and the process you use and write it down. 

But wait, don’t you need a method? After all we are supposed to structure our prompts and there is an entire industry on how you make those prompts super-duper effective. Here’s just some of the candidates:

  * **RISEN:** **R** ole, **I** nstructions, **S** teps, **E** nd Goal, **N** arrowing Constraints.

  * **CRAFT:** **C** ontext, **R** ole, **A** ction, **F** ormat, **T** arget Audience.

  * **CARE:** **C** ontext, **A** sk (what you want), **R** ules (constraints), **E** xamples.

  * **CLEAR:** **C** ontext, **L** anguage (or Logistics), **E** xamples, **A** udience, **R** ole (or Reflective).

  * **TRACI:** **T** ask, **R** ole, **A** udience, **C** reate (Format), **I** ntent.

  * **PGTC:** **P** ersona, **G** oal, **T** ask, **C** ontext.

  * **5 P’s:** **P** rime (Context), **P** ersona, **P** rivacy, **P** roduct (Goal), **P** olish.

  * **ACTIF:** **A** ction, **C** ontext, **T** arget, **I** nstructions, **F** ormat.

  * **CREATE:** **C** haracter, **R** equest, **E** xamples, **A** djustments, **T** ype of Output,

I didn’t use a role. I gave two examples — you know how I got them? I ran the prompt and pasted the output I liked in. The prompt already worked without them. I never talked about an audience. And so on, and so on. 

Perhaps you think — well, in some cases those things will matter! Sure they will. If you don’t like the output you can add some notes. Trust me, it won’t be hard to figure out. Your value add is probably not remembering to say “I would like titles bolded” or “can this be a csv?” 

Your value add is, for the most part, figuring out how to do things, and figuring out how to explain them in a way that someone other than you can do them. In a word, your skill is teaching. 

Does all this stuff — these acronyms and such — hurt? Not directly. But I think it convinces people that the skill of prompting is something like learning Python or JavaScript. That in turn convinces people that this is like coding in that if you know a certain syntax you have special powers. 

Your special power is in better understanding the things you already know. Focus on how to do the thing. Test how to do the thing. Write down how to do the thing. Pay attention to whether it works.

That’s it. 

I'll probably continue to edit my film analyzer and improve it. It’s a first pass, even is a promising one, and I’m a futzer. But if you know how to do something yourself, realize the era of “I know how to prompt” is coming to an end. Learn stuff. Know stuff. Focus on knowing how to do, and the rest will probably sort itself out.

Prompt (edited down a bit by Claude, but I think it didn’t break it) [here](<https://checkplease.neocities.org/film-plot-analyzer/>).

## The Cast Away Analysis

Sorry, I do like this analysis quite a lot, so I am putting the [output of the process](<https://claude.ai/share/a7d1a422-8dda-47cd-b3d6-087e8510a7b5>) here:

**EQUILIBRIUM.** Memphis and the global FedEx network. Chuck as the apostle of the clock. Kelly as the relationship subordinated to schedule, the pocket watch as the icon — her face inside the instrument of his tyranny. A man organized around the deferral of presence.

**INCITING INCIDENT.** The plane crash in the South Pacific. The systems fail catastrophically; Chuck washes up on a beach where none of his tools apply.

**RESISTANCE / DEBATE.** The first days on the island. Chuck still operating in rescue-time — checking the watch, expecting search planes, trying to send signals. The debate is not “should I survive” but “what kind of problem is this?” — and Chuck initially treats it as a short-term logistical one.

**POINT OF NO RETURN.** Making fire. “I have made fire!” The shift from waiting-for-rescue to surviving-here. The project becomes real, even if Chuck doesn’t yet know how long it will last.

**RISING ACTION / INITIAL PATH.** The first stretch on the island. Spearing fish, mapping the cave, opening the FedEx packages (except the winged one), creating Wilson, attempting an early raft and being beaten back by the breakers. The initial path is _escape through effort_ — apply the tools of the engineer to the new domain, solve the island, get home. Wilson is part of this path: a manufactured social world that lets Chuck remain the kind of person who can execute a plan.

**CRISIS.** The suicide-test scene. Chuck on the high rock with the rope, dropping the log to test the branch, watching the branch break. The terminus of will. The old path — engineering outcomes — exhausts itself; he can’t even reliably exit on his own terms. He comes down. A new orientation takes hold without being articulated: keep breathing, wait, see what the tide brings.

**FALLING ACTION / NEW PATH.** The four-year time jump. Chuck weathered, gaunt, integrated into the island’s rhythms. The new path is not articulated but visible in his body and his patience. Eventually the tide literally brings him the sail — a piece of porta-potty plastic washes ashore, and only now does the raft become possible. The escape is not willed into being; it is received and then acted on.

**ESCALATION.** Wilson lost on the open ocean. Chuck, exhausted, asleep on the raft, wakes to see Wilson drifting away. He swims after, can’t reach, returns to the raft weeping “I’m sorry, Wilson.” The new path is tested: can he hold the orientation when the relational world he built is taken? He can. He survives the loss without abandoning the raft, without abandoning the breathing.

**CLIMAX.** The reunion with Kelly. Chuck at her door in the rain, the embrace in the kitchen, the drive in her car, and the moment on her front lawn where they hold each other and Chuck tells her to go back inside, back to her family. The post-crisis tool — keep breathing, accept what the tide brings, hold no power over outcomes — is tested at the highest emotional stakes the film can stage. He passes. He lets her go.

**WIND-DOWN.** Returning the unopened FedEx package (the angel-winged one) to the woman’s empty Texas ranch house. The note he leaves: this package saved my life. The crossroads. The woman in the pickup truck stopping, giving directions, driving away. Chuck looking each way, then looking after her truck. The wind-down validates the quadrant: a new equilibrium that incorporates the shift, with the world having brought him an unforced direction he is free to follow or not.

1

Rocky is a fascinating script, by the way, the other mistake people make is thinking the climax is when he is announced as winner, but Rocky’s emotional path is understanding that it is not “winning” that his life is missing, it’s “going the distance”, to know that for once he gave it everything and was not just a bum from the neighborhood. The climax is standing at the bell.
