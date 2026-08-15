---
title: "\"AI is less like programming and more like spreadsheets\": An Interview with Mike Caulfield About Deep Background, AI Literacy and Future Skills"
person: mike-caulfield
section: by
type: interview
year: 2025
venue: "AACE Review (Association for the Advancement of Computing in Education)"
authors: "Mike Caulfield (interviewed for the AACE Review)"
source_url: https://aace.org/review/caulfield-ai/
retrieved: 2026-08-13
content: full-text
notes: "Interview about his Deep Background LLM tooling, AI literacy and SIFT-for-AI. Captured via r.jina.ai."
---

# "AI is less like programming and more like spreadsheets": An Interview with Mike Caulfield About Deep Background, AI Literacy and Future Skills

## Full text

By **[Stefanie Panke](https://aace.org/review/author/stefanie-panke/)** for AACE Review, August 13th 2025

Mike Caulfield, co-author of[Verified](https://press.uchicago.edu/ucp/books/book/chicago/V/bo207015182.html), a practical guide on using the Internet to verify claims, recently released ‘[Deep Background](https://chatgpt.com/g/g-684fa334fb0c8191910d50a70baad796-deep-background-fact-checks-and-context)’ a rigorous AI-based fact-checker that anyone can use for free. You can access [‘Deep Background’ in ChatGPT](https://chatgpt.com/g/g-684fa334fb0c8191910d50a70baad796-deep-background-fact-checks-and-context) or paste the [prompt](https://checkplease.neocities.org/) in at the beginning of a chat session with an LLM. Based on Mike Caulfield’s extensive testing, he’s found LLMs using this prompt will[come to better conclusions](https://mikecaulfield.substack.com/p/yes-llms-can-be-better-at-search), hallucinate less, and source conflicting perspectives more systematically.

The “superprompt” is partly based on Mike Caufield’s SIFT model (originally coined ‘four moves’, cf., [Caulfield, 2017](https://open.umn.edu/opentextbooks/textbooks/454)).

**STOP.** Ask yourself whether you recognize the website or source, and what the reputations of both the claim and the source are.

**INVESTIGATE.** Not sure about that reputation? Learn about the source before you let the information sink in. Knowing its expertise and agenda is crucial to interpreting what it says.

**FIND.** Still concerned? Look for the best available source on this topic—or, just as importantly, scan multiple sources to see where expert consensus lies.

**TRACE.** Much of what we find online has been stripped of context. Trace the claim, quote, or media back to its origin so you can see it in its original context and judge whether the version you saw was accurate or misleading.

Sometimes these techniques reveal that claims are outright wrong or that sources are acting in bad faith. More often, they simply restore context and create nuance so you can come to a balanced conclusion.

The process for using SIFT with the Deep Background prompt or GPT is simple:

*   Pick a claim you’ve recently read on social media, or encountered anywhere on the Internet. Keep it short and precise —one or two sentences.
*   After the initial check, type “another round”. Watch it double-check its check.
*   Type ‘source table’ to see an overview of the sources used.
*   Finally, type “context report” to get a succinct summary of what was found.

[I interviewed Mike Caulfield in 2018 about his approach to fact checking](https://aace.org/review/interview-mike-caulfield/), and was eager to hear more about his take on generative AI, agentic AI, information literacy and future skills in an AI-saturated society.

You can watch the recording or read the edited transcript below.

[](https://uncch.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=43b90f43-dc83-44da-831b-b32501173d65)

## Edited Transcript

**Stefanie Panke:**The last time we talked about digital literacy and misinformation was in 2018, and Mike, you had just published a free ebook on the SIFT method for student fact checkers. Back then you explained that there’s probably less misinformation than we expect, but it affects us way more than we think. How has the internet changed since then? In your view, has misinformation gotten worse, or have we maybe gotten better at detecting it?

**Mike Caulfield:** It’s a mixed story. In certain dimensions it got better. As one example, some of the problems we were dealing with in, say, 2017 with completely fake news sites—the platforms figured out how to deal with the completely fake news sites, the initial sort of thing where you had a fake local news source saying that the Pope had endorsed Donald Trump—that sort of stuff was addressed by the platforms. A lot of the more outrageous stuff saw a downtick, or at least some contextualization around it, because platforms engaged with addressing it.

But there has been a dramatic uptick in miscontextualized information. Even back then, the majority of what you would call misinformation was not necessarily a fact that was by itself wrong, but instead someone presenting a fact as evidence of something that it could not be evidence of once you knew the full context. That’s a subtle point, and maybe we’ll get into that later, but that pattern has dramatically expanded.

The truth is, still, even today, most things you see on the internet are true. But there’s a lot of stuff that’s lacking context, and sometimes it lacks so much context that it becomes deceptive.

**Stefanie Panke:** Thank you for that clarification. I still recall two points you made during that first interview. The first was that you advised getting fact-checking down to a really short routine—30 to 60 seconds—and you explained it with brushing teeth: it’s better to brush your teeth every day and do it briefly than do it very thoroughly but only on the weekends. That’s really good advice. The second was your personal fact-checking routine: investigate everything you share and everything you have a strong reaction to. Are both these rules still true in this day and age?

**Mike Caulfield:** Absolutely. That piece hasn’t changed. When it comes to this stuff, good habits eat deep engagement for lunch. That’s still the case. One thing that has shifted: as people start to share generated text through LLMs, they’re not just sharing a single fact or image. They’re often sharing something quite extensive that has a lot of facts embedded in it that haven’t been checked by anybody—it’s just been generated. I worry that people are unaware of their ethical requirements when they share these longer pieces of text. If you’re sharing some AI-generated text and it has little details wrong that aren’t particularly important and you’re just sharing it with friends, it’s probably fine; you would probably make some errors in what you’d share if it wasn’t AI-generated as well. But the ability to push a button and generate five pages of text that no human has fact-checked yet fundamentally shifts things. I hope people understand their obligations when they do that.

**Stefanie Panke:** Since you brought up generative AI—the elephant in the room—it’s pretty much a time now where people start to wonder if democracy will survive the coming influx of deepfakes and automatically generated misinformation. You decided, instead of catastrophizing, to lean into AI for fact-checking. Can you explain for laypeople what your AI tool does, and how educators can use it?

**Mike Caulfield:** I’ll back up and answer a bit of that first.

A lot of people worry that AI is going to undermine democracy. I’m not saying it isn’t being used that way; I think it is. But people should remember that where we are in terms of the fragility of democracy—we got there with social media. It’s odd to see people on social media saying you can’t possibly use AI because it undermines democracy—you’re on the machine that undermined democracy while saying that.

My perspective has always been: if you retreat from a tool space being engaged with by bad actors, you leave it to them. You leave the definition and future of that tool to them, and you leave its capabilities on the table. I don’t believe in unilateral disarmament with AI—“we’ll solve AI being used for harm by not using this powerful tool at all for good.” That’s never made sense to me. I respect people who believe that, but it hasn’t resonated with me.

On AI and fact-checking: I started as an AI skeptic. In November 2022, when the ChatGPT interface first rolled out, I used it and, from a verification perspective, thought, “This is junk.” It got my standard tests universally wrong; the writing was homogenized.

That changed when they added search capabilities. With search, these tools are no longer just text-prediction engines. If you can use the search functions the right way, you create something like a search engine with additional capabilities. I’ve called it “scaffolded search”: you have search, and you have the AI helping you through a complex search, going through results and summarizing them.

I’ve taught students to search for over a decade. The simple stuff is easy, but the more complex stuff—especially decontextualization where you don’t know the context you’re missing—can be hard. So the interest for me was: what if we combine the strengths of search with the strengths of AI, rather than seeing them in conflict? What if we create a tool that handles contextualization better than either one alone?

That’s what the tool is about. I’ve had a couple of names for it—SIFT Toolbox and, more recently, Deep Background. It’s a superprompt: how do we combine the best of search with the best of AI to create something really strong at contextualization?

**Stefanie Panke:** You literally wrote the book on verifying information on the internet. Clearly, your custom GPT comes from deep expertise. But there are hundreds, maybe thousands, of custom AI applications out there. How can users assess the quality of these custom GPTs and custom agentic AI models?

**Mike Caulfield:** Great question. It’s not much different from assessing another source. If you’re looking at something meant to help with chemistry, you’d want to know that the person is in a position to know about chemistry—that they have expertise or professional insight.

In the first book we talked about wanting someone in a position to know and someone careful with the truth. That doesn’t mean always truthful—people get things wrong—but someone with a history or demonstrated method of making sure what they give you is valid. You’d want to know they wouldn’t just put this out without testing it. What did they do to test it?

People look at me weird when I say I’ve been working on a superprompt called Deep Background for six months. It’s about 3,000 words, but a lot of the work is testing. As examples come into view, I run them against it constantly. I’ve run thousands of questions and claims against Deep Background because that’s the person I am.

One problem with these prompts is people aren’t talking enough about testing. It’s easy to build a prompt that seems to work, but did you take weekends and methodically go through links it produced? Did you take 50 responses and go through all 20 links each time to make sure it’s not hallucinating? That’s how I found that on Gemini 2.5, my prompt hallucinated links. I wouldn’t have noticed if I hadn’t gone through methodically, because it was around the 10th or 11th link where it went off the rails. If I’d just clicked the first few, I would have recommended Gemini—but I didn’t.

I particularly worry about this in education—the issue of quality. We want to bring in people with position-to-know—teachers—but teachers may not have time to rigorously test these things. How do we do that?

There’s always a tension: people in a position to know aren’t always the people careful with the truth—not because they’re liars, but because they might not have time to check something. A piece of what we need to do is teach teachers how to test their stuff. Maybe I need to put something together on that. There’s a whole workshop opportunity in teaching teachers how to systematically test a prompt.

**Stefanie Panke:** As you can tell, I’ve engaged with your Deep Background GPT quite a bit. While I try not to personify AI—I talk to my car and ask how it’s doing—I’ve had spirited discussions where I thought I was right and it gave me nuance: “this is true-ish,” “somewhat true,” “there’s some truth to this.” Do you use it yourself? Do you find yourself having moments where you expect it to agree and it doesn’t?

**Mike Caulfield:** I do. I use it quite a lot. In my habits, it’s become my go-to instead of Google for any question with depth. If I’m looking for “What age was Sharon Osbourne when she married Ozzy Osbourne?”—go to Google. We don’t need Deep Background for that. But for any question with depth, I go to it, because of contextualization. In the newest version I took out the “what a fact-checker might say” verdict, because people get locked onto that. The biggest thing it gives me is perspective. Example from education: I have a prompt I play with—does teaching children chess help them in other academic subjects? I thought that was a fully garbage claim because far transfer is extremely rare. And Deep Background showed the research is not on the side of that narrow question. But it has a section called “Potential leads,” and it points out that life isn’t purely about trigonometry scores. There are promising effects on self-worth and self-efficay. Maybe we should look at that. It made me think I was coming at this too narrowly.

That’s one of the things it does for me. It broadens your questions. Composition instructors like it because it helps students see their narrow question isn’t particularly interesting; here are places where there’s debate where you might find a better question or position.

**Stefanie Panke:** This would be a nice tool for PhD students starting out—“What do I want to do my research project on?”—and for testing first ideas. Also for grant proposal writing. Do you have any data—do you collect data or anecdotes—on who uses this tool in education and why?

**Mike Caulfield:** I don’t know, and I’ve got to figure out a way to do that without being a Facebook-like tracker. I only see what people post on Bluesky, LinkedIn, and so on.

For the large mega-prompt on checkplease.neocities.org, you copy and paste it—there’s no way (for me) to track usage. I do know that Anna Mills, who does a lot of work in rhetoric and AI, recently had a workshop about educators putting together their own prompts and used it as a model; it was well-attended and well-reviewed. So that’s one thing I’m happy about is that this prompt has had an impact not just on people using it directly, but on how people think about prompting. When I came into the educational prompting space, a lot of people were doing relatively simple prompts—a paragraph: “Imagine you’re a sociologist,” “Be careful with your facts.” My prompt pushes this further and shows teachers that many of their teaching skills transfer to prompting.

For prompting, you need someone who can explain in natural language things that are non-intuitive at a level of detail where something that doesn’t understand the domain won’t mess up. And teachers do this. A programmer wants deterministic behavior; a teacher thinks about all the ways instructions can be misunderstood and corrals that. Prompting ends up being like that.

My prompt provides LLM ways to self-assess its work, think of a few searches it will execute, consider bias in those searches, revise them, and so on. It’s like an assignment for an LLM. I think it’s had impact in those ways (in showing teachers that their teaching skills are also prompting skills and encouraging them to take their prompting further), but I don’t know how to measure it.

**Stefanie Panke:** You are an educator, trainer, consultant, writer. How has generative AI transformed your work? Which tools do you use frequently? What’s the best, and what’s the worst, part of this transformation?

**Mike Caulfield:** I use the large platforms. I don’t have a lot of one-off tools in my belt. I don’t use tools like Elicit, although it’s popular with researchers. I’m interested in engaging directly with the larger web interfaces of the larger models.

How has it transformed my work? I’ve been deep into seeing how far I can push it with fact-checking. The biggest change is that it’s become a go-to instead of search as a first step, and then a lot of the work falls on going through sources. I wouldn’t have expected that two years ago, given that most of my work over a decade was about how to search better.

Worst part: Hard to choose, there are so many bad impacts. Writing and production used to be a signal of effort and care; now it’s not. Hiring managers are getting thousands of resumes perfectly crafted for positions. Magazines are being flooded with auto-generated short fiction. Spotify is being overrun with AI bands and tracks competing with real people. That’s horrible. There’s an “AI slop” angle.

On the other side, some people are far too trusting of AI and use it in inappropriate, dangerous ways because they don’t understand how it works. I’m not someone who says “it’s just a prediction machine.” In practice it can do incredible things, but it has major flaws, and people don’t understand how those manifest. I’ve seen software companies code their way with these tools and end up deleting their company database. The downsides are a world of hurt. I don’t think that toothpaste is going back in the tube—so we’re back to toothbrushing.

**Stefanie Panke:** If the toothpaste can’t go back, maybe we should make rules about where it can and can’t go. Should governments regulate web technologies such as generative AI, and maybe social media as well? How should regulation look—bans for certain purposes, age limits, algorithmic transparency? Should governments invest in open access and open source? Demand more transparency? What’s the way forward for society and for digital citizenship?

**Mike Caulfield:** For a while the platforms engaged with misinformation, and then they kind of stopped when political pressure went the other way. I think there are plenty of things platforms could do, but I worry that stuff is subject to political winds. I don’t have much faith in that.

In a perfect world, there should be some traceability. Efforts to embed fingerprinting in images—so platforms can say, “this is likely AI”—are useful. I’m interested in fingerprinting in longer documents like resumes (even if) many p eople will always get around it.

The model for a lot of this is spam. If you remember, spam used to be a lot worse; there were periods between 2004 and 2008 where email was pretty much unusable. That slowly got better. As Sarah Jeong talks about in _Internet of Garbage_, it wasn’t one thing that stopped spam; it’s a never-ending battle between platforms/technologies and people trying to get junk into your inbox. It’s still going on. These things don’t get “solved,” but spam shows a world where, if we agree it’s a social problem and users are vocal about what they want, when companies take it seriously and put resources into it, we can find a livable space—even if it’s not a utopia.

**Stefanie Panke:** If people want to learn more about your work, or engage with Deep Background or the model prompt, what are good ways to find and follow you?

**Mike Caulfield:** The prompt itself is on a Neocities site: checkplease.neocities.org, If you want the prompt, go there (It runs on paid versions of Claude, and on ChatGPT 5).I write about the development of the prompt and other issues on Substack at mikecaulfield.substack.com. I occasionally do video walkthroughs there as well. I used to post on Bluesky about AI literacy work, but people there aren’t very fond of AI, and posting wasn’t fun. So those two places work.

**Stefanie Panke:** One very last question. Many sectors will be impacted by generative AI. As educators, what should we do to prepare students? Are we doing enough? Any thoughts or advice?

**Mike Caulfield:** We don’t really know yet, so I’d caution against over-rotation on this. There’s this idea we’re going to teach all students to be prompt engineers. What I’ve found is that the most useful thing for someone writing a prompt is to have a theoretical model they understand and attempt to implement through a prompt.

The reason my prompt works well is that I have theoretical and pedagogical models for dealing with contextualization developed over 10 years. I can transfer those in. There’s an idea that this will be like programming, where you learn a specialized language and the language itself is the goal. I think people most advantaged by AI are those with knowledge or expertise they bring to the table and can translate through it.

AI is less like programming and more like spreadsheets. The impact of spreadsheets was huge. What spreadsheets did was not advantage a fleet of people super good at spreadsheets; it let engineers and others learn enough to take their deep knowledge and translate it into something valuable on their own. The value came from the knowledge they brought, not the spreadsheet itself.

I started my work in educational software at an energy consulting company. They had a legendary spreadsheet: you plug in a zip code and house specs and it tells you the size of your space heater/cooling system, pulling in weather tables and more. The person who built it wasn’t an Excel genius; he was an engineering mind who could think through how weather patterns affect heating and cooling, humidity, etc., and meticulously calculate them. Spreadsheets let him implement it efficiently.

I think AI will be like that. People should play with and engage with AI, but the value won’t come from people with only AI skills. It will come from students with deep specialized knowledge, theoretical frameworks, application frameworks—things that have been difficult to implement but may now be easier. We’ve got to get them that knowledge. What will make them valuable is what they bring to the AI, not what they do inside the AI.

**Stefanie Panke:** Mike, thank you so much for your time and expertise, and for sharing these insights, practical tips, and concrete steps for conceptualizing generative AI in education.

**Mike Caulfield:** You’re welcome.

[](https://aace.org/review/caulfield-ai/# "Printer Friendly, PDF & Email")

Be the first to write a comment.
