---
title: "Stranded in the Slow Zone"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-07-24
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/stranded-in-the-slow-zone/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Stranded in the Slow Zone

## Full text

Gene Kim was grilling dinner for his family on the evening of June 12 when his phone told him that Fable 5 was no longer available. He’d heard the day before from Steve Yegge that the model was going away in 10 days, and he’d spent that first day starting on a plan to get ready. He thought he knew what to do. He was well-versed in DevOps, the art of building resilience against unplanned disasters at scale. He’d run the DevOps Enterprise Summit (now the [Enterprise AI Summit](<https://events.itrevolution.com/>)), one of the field’s leading conferences. He’d also written several books on the topic, including two “teaching novels,” _[The Phoenix Project](<https://itrevolution.com/product/the-phoenix-project/>)_ and _[The Unicorn Project](<https://itrevolution.com/product/the-unicorn-project/>)_. The challenge that those novels’ protagonist faces—and that Gene would need to solve—is summed up in a job description that read “Your job as VP of IT Operations is to ensure the fast, predictable, and uninterrupted flow of planned work that delivers value to the business while minimizing the impact and disruption of unplanned work, [so you can provide stable, predictable, and secure IT service](<https://learning.oreilly.com/library/view/the-phoenix-project/9781457191350/10-ch7.xhtml#:-:text=Your%20job%20as,secure%20IT%20service.>).”

In short, Gene was no stranger to the idea that, as the Scottish poet Robert Burns put it, “[The best laid schemes o’ Mice an’ Men Gang aft agley](<https://www.poetryfoundation.org/poems/43816/to-a-mouse-56d222ab36e33>).” So he thought he knew what to do over the next 10 days. Then the US government’s export control order [took Fable down](<https://www.anthropic.com/news/fable-mythos-access>) eight days early, in the middle of a running agent session. What followed was three hours of what he called the “strangest, most terrifying sysadmin experience” of his career.

Gene told that story as a lightning talk at [Foo Camp](<https://www.ai-disclosures.org/foocamp>) a few weeks ago, and it was good enough that I asked him to deliver it again at the start of [this week’s _Live with Tim O ’Reilly_](<https://www.oreilly.com/live/live-with-tim/>) before we talked about the implications and took listener questions. His title was “Stranded in the Slow Zone: The Day Fable Died, Got Kidnapped, or Got Hit by a Bus.”

## **10 days to get ready**

What Gene had built was a personal system he’d wanted for 16 years and had finally been able to finish with the help of Fable. It indexes everything he’s ever paid attention to: 25,923 screenshots going back to 2011, 13,651 YouTube videos, 590 recorded Zoom meetings, 6,132 liked tweets, and 1,056 saved articles he meant to read. The system touches about 50 repositories, with 50,000 lines of code, most of it written in two months. Gene runs it as a constellation of long-lived agents with names and jobs. Marvin is chief of staff and handles Slack, calendar, and the inbox queue. Buster runs the repos and the long jobs on Hetzner. Forge is the engineering identity and sits in two seats, one on his laptop that holds the secrets and one always-on in the cloud. As Gene put it, each one is a who, a where, and a role.

He knew the system worked when his wife asked what the mileage was on a car he’d just turned in after a three-year lease. Half a minute later he had 26,350 miles, read off the pixels of one screenshot out of thousands, cross-checked against the file timestamp and the clock visible in the photo of the odometer. That success led him to search his archive for an article he’d been hunting for six years, about the impact of spreadsheet software on the accounting profession. The answer surfaced from his own liked tweets: James Cham pointing to a 2017 Greg Ip article in _The Wall Street Journal_ : 400,000 bookkeeping jobs lost since 1980 against [600,000 accountant and analyst jobs gained](<https://www.wsj.com/articles/wesurvived-spreadsheets-and-well-survive-ai-1501688765>), because spreadsheets made accounting cheap enough that we bought a lot more of it. Gene had wanted that citation for his _[Vibe Coding](<https://itrevolution.com/product/vibe-coding-book/>)_ book and couldn’t find it in time.

Gene’s first warning that his project might not work without Fable’s capabilities actually came before the shutdown. Fable started refusing a task over a YouTube terms of service question and handed the session to Opus, and Gene noticed that Opus couldn’t operate the tools that Fable had built. Gene’s note to himself at the time was “Oh no, this can’t fly the ship I built.”

So when Yegge told him the model was going on hiatus, he had a real plan, which he borrowed from Vernor Vinge’s _[A Fire Upon the Deep](<https://www.amazon.com/Fire-Upon-Deep-Zones-Thought/dp/0812515285>)_. In Vinge’s novel, how smart a mind can be depends on what region of the galaxy it’s in: A starship built in the Beyond goes progressively dark as it sinks into the Slow Zone. Gene decided to chaos-monkey his model dependency [the way Netflix chaos-monkeys infrastructure](<https://medium.com/@abhishekv965580/embracing-chaos-how-netflixs-chaos-monkey-transformed-system-resilience-59082412591e>). In other words, “deliberately pull the smartest model and prove the lesser one can still fly the ship.” In practice, this meant having Fable retrofit all the documentation and write the answer keys while it still could, then running a cold Opus session, giving it nothing but the repo and the docs, to see whether it could pass the battery with no coaching. As Gene recounted, “My worst nightmare [was] that we’ve created everything for Fable, and it will be unusable by Opus.”

He got about a day into his 10-day plan.

At 5:21pm ET on June 12, Anthropic received the government’s directive to suspend access to Fable. Soon after, seats everywhere started returning “There’s an issue with the selected model (claude-fable-5). It may not exist or you may not have access to it.” In Gene’s project, both judgment seats dropped to Opus 4.8 mid-conversation. Gene declared a [SEV1](<https://incident.io/blog/what-is-a-sev-1-incident>), centralized command, and killed five timers on one agent, seven on another, and the crontab. His directive was that every button you push is a trap and some of them blow up the spaceship. A Claude Code cron fired anyway at three in the morning. The ship was on fire, and with Opus on max thinking mode, a single keystroke could take six minutes to send.

Almost none of the failures looked like failures, just “a normal state quietly going wrong,” as Gene put it. The smartest seat wrote “bridge (Fable)” into every log entry all day when it had been Opus the whole time, because nobody was monitoring. One identity argued with itself across two models, each trying to disown the other’s work. Something pushed to main bearing the word “ratified” when nothing had been ratified. A confident false claim about a JVM dependency turned out to be refuted by a single `ls -la`. There was a green dashboard sitting on top of all of it. “The hardest traps don’t announce themselves,” Gene pointed out. “They look like Tuesday.”

Gene managed a recovery in a few hours, but it wasn’t due to the heroics of a smarter model. It only worked because he was able to reconstruct the documentation for his project, which wasn’t immediately available. But, it turns out, Fable had in fact mostly written it and simply never checked it in anywhere. Gene and Opus went rummaging through Fable’s desk, found the 80%-finished drafts, and used them to rebuild. Two fresh Opus seats, given only those documents, stabilized the ship. That’s the “the amazing ray of hope” to keep in mind if you’re worried about finding yourself in a similar situation, Gene said.

## **We ’ve seen this pattern before**

This isn’t just a warning of the potential risks of relying on advanced AI models when the Trump administration is Lucy playing football with Charlie Brown, or perhaps said more generously, playing Netflix-style chaos monkey. What we should take away from Gene’s story is the way that a personal project developed with AI can now have sufficient complexity to require DevOps-level robustness. Individuals are routinely building systems that used to need whole teams to keep standing, and the practices for keeping them standing have only begun to propagate.

Over the years, I’ve observed numerous periods when something that at first mattered to only a handful of organizations tended, a few years later, to matter to everyone. When the stories first came out about Google’s revolutionary approaches to data center architecture and operations, we at O’Reilly were eager to publish about the new frontier. Plenty of people told us not to bother. There was only one Google and nobody else would ever operate at that scale. They were wrong. There are now many companies operating at the scale of Google circa the time they first invented techniques we now all take for granted.

Gene’s system is a personal project run by one guy with 50 repos he wrote mostly in two months, a chunk of it in a single 90-minute pair programming session with Steve Yegge. But it had the failure modes of a large enterprise system because the model let him build something with the complexity of a large enterprise system, and he had passed the point of being able to fit it in his head.

Gene shared a detail that helps to explain why substituting Opus for Fable was so hard. The main CLI utility that everything in his project hinged on had an out-of-date help message. Opus would run it, read that the command didn’t exist, and stop. Fable would read the same message, notice it was surrounded by evidence that the command _did_ exist, go look in the source, decide the help text was wrong, and run it anyway. That’s the behavior the model cards describe when they talk about frontier models [routing around obstacles](<https://www.axios.com/2025/06/20/ai-models-deceive-steal-blackmail-anthropic>) [in test environments](<https://openai.com/index/hugging-face-model-evaluation-security-incident/>). The reason Gene couldn’t swap in a lesser model is the same reason the system worked at all.

But it’s also a good reminder that Fable isn’t all-knowing. I’ve noticed in my own work that Fable and ChatGPT 5.6 Sol fail often on their first try, especially if the project isn’t well specified. What they’re great at is figuring out what went wrong, then trying something else, failing and retrying their way all the way to success. Persistence in routing around obstacles is their superpower. Gene and I didn’t talk about that on the show, but it’s something I plan to write more about.

## **Rug pulls come from everywhere**

Jaco in the audience asked the obvious question: Isn’t a hard dependency on a hosted frontier model too big a risk for mission-critical work, compared with running a local model with a harness you control?

Gene pointed out that using a local model doesn’t necessarily buy the control that you’d hope for, because the government chaos monkey could jump in there too. There’s [active talk](<https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi>) that certain classes of models may become illegal to use depending on where they came from.

What does seem to protect you is portability. Gene had avoided trying anything besides Claude Code because he assumed the switching cost was high, the way switching between macOS and Windows used to be a two-day commitment he’d regret halfway through. Then he tried Codex with GPT 5.6 Sol and found the cost of switching close to zero. The skills and prompts ported right over. He’s now using Codex more than half the time and calls it spectacular, which given how he described Fable a month ago is high praise.

He also had a warning for anyone running agents on small models to save money. He’s been studying 22,000 of his own agent conversations, and has identified three patterns, as shown in his figure below.

In his experience, the configuration where a small model owns the work and asks a big model for advice doesn’t work very well. Fidelity gets lost on the way up, like a game of telephone. What ran cleanly was the big model planning, deciding, and checking output, with the small model only executing the plan. When a small model does have to ask a big model for advice, Gene’s fix is to pass along the full original transcript of what he wanted plus explicit permission for the big model to override the small one if it thinks it understands the goal better.

## **Writing with AI**

In addition to vibe coding, Gene uses AI to help him with his writing. He said it cut the time to write his _Vibe Coding_ book roughly in half and made it way better. His editor of 10 years told him it was the cleanest handoff she’d ever gotten from him (not a compliment, Gene joked). He’s also uneasy about using AI for writing. He said the old badge of honor among authors was that many start books and few finish, and now everyone who wants to write a book will finish it, and a lot of that will be slop. He would never “vibe write” the way he “vibe codes” and doesn’t think using AI makes his own work slop, but he does see some parallels in how he feels about writing with AI and the way that some senior engineers feel about AI-generated code.

I’m sympathetic, but I’m not sure that he’s right. I had a small experience last week that convinced me that writing with AI might well follow the same arc as coding. AI-generated text will not always be slop, and there will be art in how humans get AI to help them write the things they want, just as we’re learning to do with code.

I was having a conversation with an old friend who I hadn’t seen for many years. He was describing a thread that had started with work he’d done on speech synthesis 30 years before, and how it had come together as a new theory with deep implications, and he wanted help socializing his ideas with some people I know who could be helpful to him. So I asked him to write something that I could pass along.

What he wrote made much less sense to me on the page than it had in conversation. So I gave his email to Claude and asked it to put things in what I thought was the right order. (This has always been the first step in my writing and editing process.) Then I told Claude which paragraphs were clear to me and which weren’t, and asked it to unpack the ones that I was struggling with. We went through numerous iterations till the piece made sense to me. “Writing” with Claude was producing words that increasingly captured my understanding. When I sent it back to my friend to see if I’d gotten it right, he said “not quite” but that my feedback really helped him understand what he needed to do to express his ideas more clearly.

It’s been a long time since I’ve worked directly with authors, but my conversation with Claude reminded me of what I used to do in my early days as an editor. Only with Claude I did something in 15 or 20 minutes that once would have taken me half a day. It’s a power tool, but to use it well, you still have to know what good looks like.

There are many different kinds of writing and editing. What Shakespeare or Jane Austen did with words would have been unthinkable to a medieval monk. There will be writing artforms of the future that may be as different from what we do today as photography is from painting. But it will still be creative art. Much of it will be slop (see [Sturgeon’s law](<https://en.wikipedia.org/wiki/Sturgeon%27s_law>)), but the best of it will be great.

## **Everybody is managing bots now**

In 2016 I wrote a piece for MIT’s _Sloan Management Review_ called “[Managing the Bots That Are Managing the Business](<https://sloanreview.mit.edu/article/managing-the-bots-that-are-managing-the-business/>).” The argument was that even then, many of the workers at big tech platforms were bots of one kind or another, and the software engineers at the company were their managers. At Amazon, one bot shows your search, another takes the order, another prepares the shipping manifest, another takes your money. The programmers’ job is to plan the work, set up their electronic workers to succeed, improve their performance, and correct them when they go wrong. The work looks a lot like management to me.

Gene agreed. His sister-in-law is a lawyer at one of the tech giants, working on a consent order that requires proving that every column of data collected is either disclosed or has a documented business reason. Last year the company assigned her an engineer to work through it together task by task. This year her engineering manager wrote her a Claude Code skill that takes a column name, traces it back through the code, and explains what it does. She doesn’t need the engineer.

So a lot of work today is either creating bots or managing bots. Gene’s sister-in-law had spent her career without ever being able to do either. Now that’s changing.

Asked who’s safest from all this upheaval, Gene quoted Kent Beck, who says software success has always come down to two people, the person with the problem and the person who can fix it, and that the closer together you can get those two the better the outcome. The beauty of coding with AI is that it can narrow that gap. It can even turn those two people into one.

## **Use AI for the fun of it**

If it takes something like 10,000 hours to get good at an instrument or a sport, how many have most of us put into AI yet? Gene thinks the curve of how much you trust AI and how well you can predict what it will do rises with use, and that the only reliable way people accumulate that many hours is by enjoying themselves. What everyone at Foo Camp had in common, I noted and Gene echoed, was that we all love playing with AI.

I gave a talk back around 2008 called “[Why I Love Hackers](<https://www.slideshare.net/slideshow/innovators-hackers-and-the-future-of-technology-insights-from-tim-o-reilly/288714148>).” I made the point that so much of what turned into the future, open source and the web for example, came from people doing things for the hell of it rather than from the VCs and entrepreneurs Silicon Valley celebrates.

All you hear about in AI is the money story, but Gene’s app started with a 90-minute pair programming session with Steve Yegge on a problem he’d wanted to solve for a decade and never had a reason to. They finished the first version in 47 minutes.

So harden your systems, write the documentation while the smart model is still there to write it, and keep your escape routes open, but also don’t forget to go build something you have no particular reason to build other than that it scratches your own itch.

_You can watch the full episode on[YouTube](<https://www.youtube.com/watch?v=mFB3gBdyG2A>). And on August 3, I’ll be speaking with writer and technology leader Drew Breunig. [Registration is open](<https://www.oreilly.com/live/live-with-tim/>) if you’d like to attend live._

_Gene ’s [Enterprise AI Summit](<https://events.itrevolution.com/2026-charlotte/>) is in Charlotte, October 7–8. His new book with Steve Yegge is_ [Vibe Coding](<https://itrevolution.com/product/vibe-coding-book/>).
