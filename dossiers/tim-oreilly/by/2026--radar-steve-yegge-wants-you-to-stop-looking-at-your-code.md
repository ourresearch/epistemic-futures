---
title: "Steve Yegge Wants You to Stop Looking at Your Code"
person: tim-oreilly
section: by
type: blog-post
year: 2026
date: 2026-03-12
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Steve Yegge Wants You to Stop Looking at Your Code

## Full text

My “[Live with Tim](<https://learning.oreilly.com/videos/live-with-tim/0642572330194/>)” conversation with Steve Yegge this week was one of those sessions where you could imagine the audience leaning forward in their chairs. And on more than one occasion, when Steve got particularly colorful, I imagined them recoiling. Steve has always been one of the most provocative thinkers in our industry, going all the way back to his [legendary 2011 platform rant](<https://gist.github.com/chitchcock/1281611>) that leaked from inside Google. These days he’s channeling his energy into [Gas Town](<https://github.com/steveyegge/gastown>), an open source AI agent orchestrator, and into a relentless campaign to shake developers out of what he sees as a state of denial about where coding is headed. 

And yes, Gas Town is indeed named after the fuel depot in _Mad Max: Furiosa_ , and even features a managing agent named after the Mayor. But Steve’s Gas Town is anything but dystopic. If anything, it’s joyous. That gives you a deep sense of who Steve is: He goes into the deepest, darkest part of the forest, finds something scary, and then does his best to redeem it.

We covered a lot of ground: the eight levels of coder evolution, the addictive pull of multi-agent workflows, grief and denial in the developer community, the bitter lesson, and why taste may be the last remaining competitive advantage. Here are some of the highlights.

## **Everyone gets a chief of staff**

Steve’s “Eight Levels of Coder Evolution” framework has taken on a life of its own since he published it as part of [the Gas Town launch post](<https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04>). The first four levels are about increasingly sophisticated IDE use; levels five through eight are about coding agents. Here is an infographic showing the eight stages that I showed to anchor the start of our conversation. Note that I created this slide with Nano Banana 2. It is not directly from Steve.

The key transition, Steve argues, happens at level five: Your IDE goes away and you never open it again. As Steve described it, once you realize Claude Code can write pieces of your code, you start assembling them like Lego. But while one agent is working, you’re sitting there bored, so you fire up another one. And another. Before long, you’ve got six agents running in parallel, and one of them is always finished and waiting for your attention.

Steve drew an analogy to Amazon VPs who had executive assistant support. Those people were effectively two people. They didn’t have to worry about whether the printer was jammed, so they could spend all their time focused on the real problems. Gas Town, Steve argues, is topologically similar: It’s going to turn everybody into something like an executive with a chief of staff. “We all have a chief of staff now,” he said. “Everybody’s going to be able to spend their time more productively on whatever they want to spend it on instead of figuring out where the printer is jammed.”

> _On March 26, join Addy Osmani and Tim O’Reilly at AI Codecon: Software Craftsmanship in the Age of AI, where an all-star lineup of experts will go deeper into orchestration, agent coordination, and the new skills developers need to build excellent software that creates value for all participants.  _[_Sign up for free here_](<https://www.oreilly.com/AI-Codecon/>) _._

## **The AI vampire**

This is Steve Yegge, so he’s not just going to give you the upside. His post on “[the AI Vampire](<https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163>)” explained how AI-assisted productivity creates an insidious new kind of burnout, and I made sure to ask him about that.

The old version of overwork was your company piling tasks on you until you broke, he told us. The new version isn’t your boss asking you to work extra hours. It’s Claude saying, “Is there anything else you’d like me to do on this project?” And you say yes, yes, yes, because it’s fun, because it’s productive, because the AI is your buddy, not your employer.

But there’s a twist. The AI is solving all the easy problems and leaving you with nothing but hard ones. In our conversation, I said it can feel like your bike ride is all hills now, and Steve immediately connected it to watching Jeff Bezos in meetings at Amazon. People would bring him presentations where they’d already solved every easy problem, so Bezos was just getting the hard stuff, all day long. “Now this happens to you,” Steve said. “Everyone’s Jeff Bezos, everyone’s an entrepreneur. Everyone has a huge army of workers now. And I’m telling you, it’s exhausting.”

Steve told us he naps every day now, sometimes twice a day, feeling drained by the relentless cognitive intensity. These agents don’t just help you work faster; they fundamentally change what kind of work reaches your desk.

## **On the wrong side of the bitter lesson**

We spent a good stretch on Richard Sutton’s “[bitter lesson](<https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf>).” Sutton observed that raw computation consistently beats systems built on human-engineered structure. Steve treats it less as a paper and more as a daily operating principle. “Not a day goes by when I don’t think about the bitter lesson as a math formula,” he said, “at least five times a day.”

His practical test is simple: If you’re writing code that tries to make the AI smarter, by adding heuristics, parsers, regular expressions to handle what a model could handle, you’re on the wrong side of the bitter lesson. He watches even his own Gas Town contributors make this mistake, reaching for a little regex hack when they should let a model do the cognition. (Steve does admit that sometimes you do need to [provide prebuilt code if it saves tokens](<https://steve-yegge.medium.com/software-survival-3-0-97a2a6255f7b>).)

Sutton wrote about the bitter lesson in the context of training programs to beat humans at chess and go, but it’s more general than that, even more general than leaning into today’s AI in the way that Steve does. I shared my own first encounter with the bitter lesson, back in 1993 when O’Reilly created [GNN](<https://en.wikipedia.org/wiki/Global_Network_Navigator>), the first commercial web portal. Being publishers, we curated a catalog of the best websites. Then Yahoo! set out to list all of them, restricting curation to putting them into categories. Then Google did it algorithmically, creating a custom curation for every search. We know which approach won. The bitter lesson isn’t just about AI; it’s about a recurring pattern in the history of technology where scale and computation overwhelm hand-tuned solutions.

I still believe we have [to bet against the bitter lesson](<https://www.oreilly.com/radar/betting-against-the-bitter-lesson/>), because if we just give up, there will be no place for humans in the future knowledge economy. But we have to do it knowing that we aren’t going to win in the traditional sense. We aren’t going to outrace AI. We have to learn to ride it.

For anyone in a corporate setting, you will naturally want to fit AI into your current workflows. The bitter lesson says you should instead figure out what the AI can do by itself first, and then build a new workflow around that. I described Steve’s whole approach as looking the bitter lesson in the face and saying, “I’m going to turn AI loose on everything I can, and then figure out where the human fits in the loop.”

## **Code is a liquid**

Steve hit peak Yegge mode when an audience member asked why they should leave their IDE. His response was, as usual, quotable:

> If you’re looking at your code, then you’re in a Formula One race and you’ve parked your car and opened the hood and you’re looking at the engine. You’ve slowed time to the point where everyone is racing past you and you’re a frozen statue. Code is a liquid. You spray it through hoses. You don’t freaking look at it….
> 
> Look, I get it. This is painful for people. This is super painful. For me to say these things is painful for people to hear them. Because what I’m saying is your job is going to change.…And there’s still a lot of denial out there.
> 
> What’s the first phase of grief? The first phase of grief. The whole world is in it right now, Tim. They’re in denial. Right. They are grieving for what is going away. We’re at the end of an era. An age, a golden age, maybe, where we programmers, we’re writing all the code. And it was wonderful for 30, 40, 50 years or whatever. That era is ending and people are grieving because of it. And I feel for them. I’ve got empathy, right. But I’m also losing patience because it’s 2026 and this is an exponential curve, and we don’t have time to sit around and feel pity for ourselves.

He sees that grief everywhere, but he specifically called out Hacker News, which he described as the home of “the new Amish.”

## **Taste is the moat**

Another of the audience questions was about whether corporations with deep pockets have all the leverage and there’s no room left for individuals. Steve’s answer was emphatic: absolutely not. Steve made a passionate argument that creativity outweighs capital in the AI era. He’s certain there will be companies that waste millions of dollars of tokens building software that never sees the light of day, because they had no taste, no good ideas, just brute-force generation without direction. Meanwhile, an entrepreneur with open source local inference models and a good GPU can build something that matters, if they know what people want.

“Everything is going to come down to taste,” Steve said. “Companies don’t have an advantage anymore. As an entrepreneur, I think this is a golden opportunity for people to make huge, huge impact.”

## **It’s mentors all the way down**

Someone from the audience asked Steve about a question that’s on everyone’s mind: If senior developers are becoming PMs and juniors are being replaced by AI, where will new seniors come from? His answer was a classic reframe, and an update of what he wrote in “[Revenge of the Junior Developer](<https://sourcegraph.com/blog/revenge-of-the-junior-developer>).”

He made the case that your most junior engineers aren’t who you think they are anymore. They’re your product managers, your SDRs, your finance and sales folks, all of those people throughout your company who are now building things with AI. Your former junior engineers are actually well-trained engineers who make perfect mentors for this new bottom layer. And those juniors get mentored by seniors, and seniors by principals. It’s mentoring all the way down.

Steve pointed out that this connects to something [Matt Beane](<https://www.mattbeane.com/>) (who was in our audience) has researched on skills acquisition: You don’t learn from someone 40 levels above you; you learn from someone one or two levels ahead. Steve’s suggestion for companies is to organize around this. Find mentors within your organization who are just a step or two ahead of where each person is, and bring everyone along with empathy for what people are going through.

## **We ’re going to build bigger stuff**

Another audience member asked about research showing that AI atrophies critical thinking pathways. I couldn’t resist jumping in with one of my favorite historical analogues. Socrates said the same thing about the written word, arguing that it was impairing people’s ability to remember. And he was right, we did lose the ability to recite massive amounts of literature from memory. But we gained more than we lost. Things change.

I also shared a Rilke poem that I love, about Jacob wrestling with the angel: “What we fight with is so small, and when we win, it makes us small. What we want is to be defeated decisively by successively greater beings.” If AI is atrophying your thinking, it’s because you’re not wrestling with hard enough problems. The real opportunity is to be pushed, stretched, and defeated by bigger challenges, and come away stronger from the fight.

Steve agreed: “We’re going to build bigger stuff. That’s what everyone’s worried about. What’s going to happen? And the answer is we’re going to build bigger stuff and it’s going to be fun.”

> _Watch the full conversation[here](<https://learning.oreilly.com/videos/live-with-tim/0642572330194/>). Steve Yegge’s _[_Gas Town_](<https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04>) ___is at<https://github.com/steveyegge/gastown>. His blog posts on “_[ _T_](<https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163>)[ _he AI Vampire_](<https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163>) _, ” the “_[ _Revenge of the Junior Developer_](<https://sourcegraph.com/blog/revenge-of-the-junior-developer>) _, ” and “_[ _Software Survival 3.0_](<https://steve-yegge.medium.com/software-survival-3-0-97a2a6255f7b>) _” __are essential reading for anyone navigating this transition._
