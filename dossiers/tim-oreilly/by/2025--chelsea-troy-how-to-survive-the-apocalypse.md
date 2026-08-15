---
title: "How to survive the apocalypse: a conversation with Tim O’Reilly about Generative AI"
person: tim-oreilly
section: by
type: interview
year: 2025
date: 2025-06-25
venue: "chelseatroy.com"
authors: "Tim O'Reilly; Chelsea Troy"
source_url: https://chelseatroy.com/2025/06/25/how-to-survive-the-apocalypse-a-conversation-with-tim-oreilly-about-generative-ai/
retrieved: 2026-08-13
content: full-text
notes: "Published conversation on the interviewer’s personal blog; O’Reilly’s answers are interleaved with the author’s own framing narrative and commentary."
---

# How to survive the apocalypse: a conversation with Tim O’Reilly about Generative AI

## Full text

Reading Time:  21 minutes

Sunlight fire-hosed through my east facing window at 5:15 AM last Wednesday. 

I have learned, in my eleven Chicago years, to welcome this part of summer. 

I scraped up a pair of shorts, tromped downstairs, and perched on the edge of my couch with a snifter of cold brew coffee. 

Then I opened my email: I had one from Tim O’Reilly.

Tim had emailed me a blog post from a tech company purporting to quantify the productivity boost that AI tools give to their developers. The investigation enlists pretty shaky methodology, but at least it relies on developer estimates—a measure historically regarded with somber reverence for its reliability, _of course_.

Given the way this specific company works, I confess I wonder why the investigation used developer estimates when they had a sounder metric _right there_ : comparing the closure speeds of tickets during the experiment to the closure speeds of matched pair tickets from 2022 (prior to ChatGPT’s release). Even if they had done that, though, I’m not sure it would save the investigation’s external validity. When we’re attempting to measure developer productivity, we need an accurate proxy for what it means to do a developer’s job. I think tickets, along with most of our proxy attempts, fall short right now.

## In a few hours, Tim and I would talk about exactly that on a live stream.

When people first encounter my penchant for questioning documented experiments, they either roll their eyes and mutter “Wow, she must be fun at parties” or their faces light up and they exclaim “Wow, she must be fun at parties!” Luckily for me, Tim falls into the _second_ category: he had listened to me do this on a recent superstream and expressed interest in a longer conversation. Here’s that part of the superstream:

We recorded the longer conversation, too, [which you can listen to in full right here](<https://learning.oreilly.com/videos/chelsea-troy-live/0642572020332/>). 

In the meantime, I have some snippets to share with you. _Also,_ Tim sent me some potential questions ahead of the conversation, and we didn’t get to all of them on air. So I fleshed out answers to the ones we didn’t cover, and I’m including them here for you as well :).

**TIM: In your post[ _How does AI impact my job as a programmer?_](<https://chelseatroy.com/2024/05/26/how-does-ai-impact-my-job-as-a-programmer/>), you make the point that in today’s world, writing code from scratch represents only about 10% of a programmer’s actual job**:

> “Reading, understanding, and fixing code written by others consumes 90+% of the time a programmer spends in an integrated development environment, command line, or observability interface. This is because most programmers work on legacy systems. But it’s also because, even if you’re writing greenfield apps, these days you’re mostly not writing logic from scratch. You are instead grouting together a mosaic of pre-built libraries that each do one of the things your system needs to do.”****

**And you make the point that whether that code is written by another human programmer or by an AI, the essential parts of the job aren’t going away. Can you say more about that?**

**ME:** I can. I want to preface with the fact that this effect isn’t new: what we’re looking at is the amplification of an existing cognitive dissonance in our understanding of a developer’s _role_ relative to what it actually is. We teach students, train new hires, and interview our candidates chiefly on their ability to write code from scratch, but as they advance in the workforce their _actual_ main responsibility is often reading, analyzing, debugging, or reorganizing code that they themselves did not write. 

Once upon a time, writing code from scratch comprised 90% of computer science educational assignments and, generously, 20% of the programmer’s professional responsibilities in the editor. That’s a huge gap already, but the advent of generative AI tools has pushed the gap even wider. Those tasks that _once_ required writing from scratch manually now often include asking a large language model to write it instead, at which point what the programmer is once again reading, analyzing, debugging, or reorganizing code that they themselves did not write. What comprised 20% of developers’ time in the editor now looks more like 4% of the time.

And what has replaced not only that 16% difference, but also a good deal of the maintenance we were already doing, is specifically targeting those problems on which plugging in the LLM suggestion _did not work_. There’s a Ruby developer, Nickolas Means, who does a number of excellent talks about what we can learn as software developers from the world of aeronautics, and in his [2024 RubyConf keynote](<https://www.youtube.com/watch?v=HqyF4w_jdSA>) he introduces this 1983 paper by Lisanne Bainbridge called “[Ironies of Automation](<https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf>).” 

People generally object when I bring up any academic paper that is more than a week old in a discussion about AI, but I have no intention of stopping. Why not? Because the fundamental intuition we need to use these tools effectively is in most cases _not new_ , and is _well documented_ years or even decades ahead of the latest model’s release date. The paper says a number of things that Nick pulls out in his talk, but _one_ of them is this:

> When manual take-over is needed, [it’s expected] that unusual actions will be needed, and the operator needs to be more rather than less skilled, and less rather than more cognitively loaded.

I think this is true of software engineers attempting to operate with AI tooling on relatively complex code bases, or possibly really any code base. We say the same about “magic” in frameworks, like Rails or Django or Spring. Engineers will use the term “magic” as a pejorative sometimes to describe how these frameworks just solve certain problems for them, because everything’s fine _until it’s not_. Once it’s not fine, the precise location and nature of the problem is not explicitly there in the code, so you _have_ to understand what’s happening under the hood to find and fix the issue.

**TIM, on behalf of JG in the Livestream: How much do software engineers need to know about LLMs under the hood?**

**TIM:** **Do you think AI Engineering is a good name for this part of the software engineering discipline?**

**Me:** I’ll be candid: I don’t think AI Engineering is a good name for this part of the software engineering discipline. I think it fails to differentiate between three drastically different jobs, and people search for that term while trying to better understand any one of those jobs. 

  1. Being a machine learning engineer who builds generative models 
  2. Being a software engineer who works on systems that _integrate_ with generative model APIs or SDKs, or builds the products that incorporate and serve those models
  3. Being any kind of tech-related professional accessing the user interface of the tools built by the people doing numbers 1 and 2 during the course of the workday

All of these are different things involving different subject matter expertises and skill sets, and I don’t think it’s true that you need the skill set for #1 to do #3 or even #2. I would _much_ prefer if we would differentiate _generative model engineering_ from _generative model integration_ from _manual generative model use,_ as categories of skill set. 

**TIM: We’re seeing slower hiring and layoffs in anticipation of all the unknown changes coming with generative AI. You wrote a great post last year called[ _What layoffs teach us about technical leadership_](<https://chelseatroy.com/2024/10/31/what-layoffs-teach-us-about-technical-leadership/>), in which you identified the reasons why individuals are chosen for layoffs, and what both employees and managers should do to handle them. What’s your advice for engineers? And what’s your advice for technical managers? And maybe even, what’s your advice for executives?**

**Me:** I did, yeah, and it’s my maybe-not-so-humble opinion that the things I talk about in that blog post apply to technical leadership irrespective of the company or its employees’ positions on generative AI tools. I’d love to address these three buckets of advice in reverse order, so I’ll start with executives, and then technical managers, and finally engineers.  
  
**I will disclaim what I have to say to executives with the fact that I have not, at this point, been a tech executive.** But I know that executive leadership at tech companies tends to face two critical constraints in achieving their goals: access to capital, and access to talent. Those have been, as I understand it, their two hard things. And wickedly, there are many ways to aggressively pursue _one_ of these that jeopardizes the other. 

I think the current zeitgeist suggests that access to talent is no longer going to be a constraint because of generative AI. I’m not convinced of this for basically two reasons. 

First of all, though I have a lot of problems with the way that we discuss and use the idea of the 10x engineer in our industry, it _is true_ that there is _one_ scramble for talent at the workaday programmer level, and there’s a completely _different_ scramble for talent at the “ten thousand most skilled, niche, and successfully branded engineers in the industry” level. That second scramble is _much_ , much _fiercer_ , and a code generation plugin does not possess the feature set necessary to affect it. To draw an analogy, model-generated background music affects the prospects of independent musicians who professionally record instrumental period jazz. That doesn’t mean Beyoncé, Adele, or Celine Dion will suddenly find themselves harder pressed to sell out their tours.

Second of all, I’m not seeing convincing evidence right now that AI _is really replacing engineers, for real_. There’s this blogger, Ed Zitron, who writes about the tech industry, and candidly I’d characterize his blogging persona as crank dad energy. _However_ , he published a piece a couple of days ago entitled _[Sincerity Wins The War](<https://www.wheresyoured.at/sic/>) _in which he says some things that I think the tech zeitgeist sorely needs to hear. He points out that, when journalists and pundits uncritically report what a couple of powerful people _speculated_ might happen as a result of generative AI availability, what they’re doing is remarkably poor journalism. To make business decisions _based_ on remarkably poor journalism is remarkably poor executive leadership. He then says:

> _It feels like the easiest way to push back on these stories is fairly simple: ask reporters to show the companies that have actually done this._
> 
> _No, I don’t mean “show me a company that did layoffs and claims they’re bringing in new efficiencies with AI.” I mean actually show me a company that has laid off, say, 10 people, and how those people have been replaced by AI. What does the AI do? How does it work? How do you quantify the work it’s replaced? How does it compare in quality? Surely with all these headlines there’s got to be one company that can show you, right?_
> 
> _…I really don’t mean “we’re saying this is the reason,” I mean show me the actual job replacement happening and how it works._

He’s right. You want me to report on the money? Open the vault and show me the money. Don’t handwave at me about concepts of the money in your loquacious corporate email. I think Ed’s right to challenge reporters to demonstrate causation. The “dynamic Generative AI environment” makes a fantastic scapegoat right now for executives who don’t want to admit that they’re doing layoffs because they fucked up at the executive level and failed to establish a reliable long-term revenue stream to cover payroll. Most layoffs derive from failures at the executive level. 

I’ll remind you that I [talked about the tech industry layoff flu in April of 2023](<https://chelseatroy.com/2023/04/11/money-dont-buy-class-privilege/>). On that date, ChatGPT had been released for a grand total of four months, Gemini wouldn’t be announced to the public until the following month, and Claude Code wouldn’t hit the market for another 22 months. Gosh, I bet all the companies that started laying people off before all this happened wish they’d had these products available to blame their layoff on at the time!

In fact, I’d go even further than to make journalists responsible for demonstrating causation. I’d also consider journalists responsible for examining who _benefits_ from the speculations they’ve been fed for their article. To be brazenly specific, I think they should examine whether the names of the people feeding them the speculation are on that beneficiary list. I think it’s fair and reasonable to expect that of journalism, but since we evidently can’t expect that, we’re instead relegated as _consumers_ to wallow in despair about what we’ve read until our therapists remind us to do this in _lieu_ of the reporters who should have done it.

Frankly, if I have to ask “who benefits from this type of coverage?” on behalf of the reporters who did the covering, we don’t have a free press: we just have corporate public relations copywriters for hire. _Maybe_ they’re _kinnnda_ competing with each other on their ability to convincingly cosplay investment in the public interest, but I don’t even think news outlets bother with that veneer anymore beyond maybe their website subheading.1

**Chelsea, why does any of this matter to this discussion about advice for executives?** Great question. It matters because your layoff practice as an executive team impacts your ability to compete in a talent market. A layoff is a tradeoff a company makes against their ability to retain access to talent in order to retain access to capital, usually. I interviewed at my current employer in the year 2020, a year in which it had performed two layoffs. A lot of my interview loop was me asking managers and executives about those layoffs. I am now an interviewer at that same employer in the year 2025, the year in which it has performed several layoffs. The candidates who inspire hiring managers to fight for them, coincidentally, are also the ones rhetorically pinning me to the wall about those layoffs. I’m not even a tiny bit surprised.

Here’s what I want executives to hear: if you need to do a layoff, cut once and cut deep. Do not do 19 separate mini-layoffs. Everybody with some amount of career experience understands and empathizes with the need to make hard choices sometimes. But when “sometimes” becomes “multiple times per presidential administration,” you just look overwhelmed and underskilled in the strategic planning department. That makes coming and working for you a high-risk, low-return endeavor.

It furthermore torches psychological safety at your organization for anyone remaining. When you do that, you disproportionately spike attrition among your share of that top ten thousand we talked about. Why? Couple of reasons:

  1. Your Beyoncés, Adeles, and Celine Dions are, relative to workaday programmers, disproportionately reliant on innovation, heterodoxy, and (effectively applied) contrarianism to power their outstanding contributions. 
  2. Your Beyoncés, Adeles, and Celine Dions are, relative to workaday programmers, disproportionately able to quickly secure employment outside your company.   

Doing a bunch of repeated layoffs drastically affects your long-term prospects in ways that a balance sheet and quarterly earnings call are poorly designed to warn you about. Unless you are _totally committed_ to executive myopia, you’ll look around in a year or two and ask yourself “Gee, why does everything suck now?” The answer isn’t “the market”: that’s what you say in PR emails, but we both know it’s not the real reason. There are still places people wanna work during hard times2. Being one of those places in the future requires you to reflect on why you’re not one of those places now. So my advice to executives would be to do that.   
  
Okay, technical managers. In that blog post you mentioned, Tim, I tell technical managers that they need to do what they can to accomplish three things: 

  1. Get their reports onto projects with visible and desirable impact
  2. Help their reports deliver successfully on those projects through helping those reports understand client needs and urgency
  3. Make sure that reports’ contributions to those visible and desirable impacts is crystal clear to executives making layoff decisions.

People have asked me if this advice applies to help people get promoted; it doesn’t. I find the sample size of people successfully internally promoted as individual contributors at most tech companies to be too small to build any kind of data-driven analysis of how to do it.

Okay! Individual contributors, software engineers. Actually, we _did_ get to this part in the livestream itself:

**TIM, on behalf of an attendee in the chat: Isn’t it the case that most tech debt comes from bad coding practices, and AI can help us institute better coding practices to the extent that we use it to write pure functions and other good coding practices?**

**TIM: In the Claude 4.0 announcement, “Dario talks about the big question: what happens if the cost of software drops dramatically? He says that previously you wouldn’t have built custom software unless it was for thousands of end users – the economics now are completely different, it’s much more feasible to build custom things. This is my optimistic angle on this too: I think demand for custom software (and our skills as developers) goes through the roof as costs come down.” Your thoughts?**

**Me:** Well…I think the premise is arguable here. People who write code have been building custom software for audiences of one since practically the second that personal computers facilitated it. Creative and investigative will are endemic to the human condition. To the extent that generative AI tools have made that creation and investigation feasible for a much larger population in the medium of software, I think we’ll see more of it. I also happen to think that building for oneself has a place in the constellation of ways to innovate, specifically in an immature market, as I argued in _[The Oxymoron of Data-Driven Innovation](<https://chelseatroy.com/2021/07/30/the-oxymoron-of-data-driven-innovation/>)_.  
  
But custom projects are, exceptional cases excluded, a completely different ecosystem than the market for large-scale production software of the type that Dario centers in the claim. For every Ebay that started as someone’s personal experiment and made it to a $35 billion market cap, there are tens of thousands of projects like [One Million Checkboxes](<https://onemillioncheckboxes.com/>) or [this personal travel blog](<https://cestlavie.app/u/teon/passport>) or [git-revise](<https://github.com/mystor/git-revise>). It’s custom; it’s personalized; the code itself rarely or never needs to be maintained (this is a particular weakness of AI-generated code). It’s also not making money. A tip jar that generates enough cash to occasionally buy a coffee doesn’t count.

I think that when Dario says “you wouldn’t have built….” he probably means “you wouldn’t have _hired someone else_ to build.” If you could even call the ecosystem of custom software a market, it’s a market based less on the cost of production associated with hiring someone _else_ to build something, and more on the accessibility associated with independently or cooperatively undertaking such a build. 

Could the demand for our skills as developers skyrocket with the appetite to hire _other people_ to write custom software? I think if it does, it won’t be at the price points we’ve become accustomed to in the United States. Maybe we _could_ all get hired on contract by a couple of law school buddies who would have sought a technical cofounder in exchange for equity ten years ago, but it would be for like USD 17 an hour. Then again, I also think the two law school buddies would often pay that _now_. The problem is, they can’t get a competent developer to _bite_ at that price, hence the equity thing (and maybe some delusions about their chances of success). For the reasons we discussed before, I’m not convinced generative AI is going to _make_ a competent developer out of someone with a USD 17-per-hour level of experience. Will generative AI _zeitgeist_ convince developers with USD 70-per-hour (and more) levels of experience that this is the new normal they need to accept? Well, I think a lot of the people you see news outlets breathlessly quote certainly hope so.

**TIM: What resources do you follow to keep up with the incredible fast pace of evolution of all this AI technology?**

**Me:** Oh, I fear I have a discouraging answer to this question 🙂 

I haven’t found any one individual newsletter or online community to be a comprehensive summary here. But here’s what I do: I subscribe to a number of online newsletters from several engineers and journalists whose analysis and opinions I’ve come to respect. I take what they have to say with a grain of salt, but I can recognize when they’re making a good point. I also take a look at their sources. I get a lot of tipoffs to good papers coming out from a network of other people who keep up on this kind of thing, most of whom I met at conferences. I also scour journals myself to look for things, and share what I find that I think is interesting. 

In terms of volume, I probably end up getting through about three papers a day, which isn’t an enormous number so the vetting system is pretty crucial for me. Then I’ve usually also got a book or two going, which I tackle one chapter at a time. Because I also work in machine learning operations and teach graduate students, a lot of what I’m reading for one job has applicability in the others. I also work periodically on my own projects, because I find that having an application for the knowledge I’m gathering focuses and motivates my efforts really effectively. This winter it was a compiler that I built in Rust, which is a language I don’t write a lot of, and that gave me the chance to mimic the experience of my students completing assignments for me in a class that I teach—which is basically Accelerated Python Programming. I can’t mimic their experience in Python because they’re _learning_ Python and I’m pretty familiar with it, but I _can_ mimic their experience in a language I’m less familiar with. Currently, my project is overhauling that Python course to center the skills for engineers that I mentioned earlier in this interview, and also just refocus the content less on “this is how Python works” and more on “this is _why_ Python works like this, and what you can learn from it about how to approach your own programming problems.” My general interests as a lecturer already lean in that direction because to me, syntax is transient and Googlable, but learning the why is not only a transferable skill, but also candidly a more fun one to employ. It’s just not the way programming classes are usually built, so we’ll see how this goes.

**Finally, Tim asked me to speak to the resources available on O’Reilly. I do a lot of live and on demand teaching on O’Reilly, so I have some thoughts on the niches that the different resources fill** :

If you’re looking to attend one of my live workshops on O’Reilly, or take one of my On-Demand courses there, or see recordings of some of my other appearances over there, you can find all of that [from my creator page at their website](<https://learning.oreilly.com/search/?q=author%3A%22Chelsea%20Troy%20%22&rows=100&language=en>)! 

## Footnotes

  1. The perk for you of seeing the directors’ cut on my blog is that I don’t usually get this spicy on other people’s platforms, but I don’t mind doing it on my own platform 😉 ↩︎
  2. This i _s especially_ true in the US, because even people with nest eggs need health insurance. ↩︎

## If you liked this piece, you might also like:

_[The Oxymoron of Data-Driven Innovation](<https://chelseatroy.com/2021/07/30/the-oxymoron-of-data-driven-innovation/>)_

[_What layoffs teach us about technical leadership_](<https://chelseatroy.com/2024/10/31/what-layoffs-teach-us-about-technical-leadership/>)

[_How does AI impact my job as a programmer?_](<https://chelseatroy.com/2024/05/26/how-does-ai-impact-my-job-as-a-programmer/>)

### Share this:

  * [ Share on X (Opens in new window) X ](<https://chelseatroy.com/2025/06/25/how-to-survive-the-apocalypse-a-conversation-with-tim-oreilly-about-generative-ai/?share=twitter>)
  * [ Share on Facebook (Opens in new window) Facebook ](<https://chelseatroy.com/2025/06/25/how-to-survive-the-apocalypse-a-conversation-with-tim-oreilly-about-generative-ai/?share=facebook>)
  * 

### Like this:

Like Loading…
