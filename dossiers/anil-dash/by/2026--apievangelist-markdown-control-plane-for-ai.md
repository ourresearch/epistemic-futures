---
title: "Anil Dash (Antitech): on how a deliberately loose plain-text format became the control plane for AI, why looseness beats standardization, and keeping faith in the open web"
person: anil-dash
section: by
type: interview
year: 2026
date: 2026-06-23
venue: "API Evangelist Conversations (Kin Lane)"
authors: "Anil Dash (interviewed by Kin Lane, API Evangelist)"
source_url: https://conversations.apievangelist.com/store/2026-06-23-anil-dash/
retrieved: 2026-08-14
content: full-text
notes: "Q&A interview; filed in by/ per the interview-format rule. Added in the 2026-08-14 cleanup pass \u2014 not on anildash.com/press/, so the 2026-08-13 collection pass did not see it. The interviewer's question headings are kept in bold so the exchange structure survives; the interviewer's framing paragraph is marked as such. Site chrome, the author bio box and newsletter promos were stripped. Identifies him as principal and cofounder of antitech."
---

# Anil Dash (Antitech): markdown as the control plane for AI

## Full text

*Interviewer's introduction:* Anil Dash is a technologist and writer who has spent more than two decades building internet technologies and chronicling what they do to the people who use them. In this conversation we start with markdown — the plain-text format he helped shepherd into the world as the product manager for Movable Type — and trace how a deliberately loose, "good enough" convention became the control plane for AI. Anil makes the counterintuitive case that markdown succeeded precisely because it was never tightly specified, and that technical correctness and standardization too often hand the keys to the biggest companies in the room. From there we go wider: how he reconciles the hopeful early web with today's enshittified platforms, why he writes for the people at and below the API line, and where the next wave of opportunity hides in the AI noise. We close on history, cycles, and his enduring belief that the antidote is for everyone to keep blogging and narrating their own stories.

**What is markdown?**

At the simplest level, markdown is a format for a plain text file — really a convention people were already following. If you wanted a bulleted list, you put an asterisk at the start of a line. What John Gruber did was recognize that behavior and write a little Perl script that consistently transformed it into HTML for his blog, then make it a plugin for Movable Type, which I was the product manager for, going back 25 years now. Movable Type was the WordPress of its time — back then it was essentially the entirety of influencer and social media. Gruber understood that the easier you made rich formatting — bold, italics, links, images — without forcing people to learn HTML or risk breaking their site, the more powerful it would be. It rolled slowly for a few years, then GitHub and Stack Overflow picked it up, and because developers met markdown where they already gathered, they carried it everywhere.

**What is the relationship between markdown and artificial intelligence?**

It’s interesting, because markdown has become the control plane for AI. You can have the most cutting-edge frontier model from a trillion-dollar company, and you’re making a plain text markdown file to try to orchestrate it. In the most low-tech, basic play you can sit in Vim writing a plain text file, and that’s how you control it — which is pretty extraordinary. It almost feels like what Unix pipes are, but the next layer of the stack up: that pervasive, that default a level of piping information through, connecting things together. In my world we went from XML to JSON to YAML, and markdown has become the minimum viable structure for feeding context to these models. It’s the default assumption now — the place where human writing and machine orchestration meet.

**Markdown is the control plane for AI — and yet it was never tightly specified.**

In the early days it made me very itchy that markdown was so nonstandard. As a coder I knew there were edge cases nobody had tightly specified, and I thought that was just wrong — not technically correct. With the hindsight of twenty-plus years, and it still makes me itchy to say it, I think that’s part of why it succeeded. Look at HTML: the version that actually got adopted might as well have been scrawled on the back of an envelope. The fact that markdown is a little bit of a toy is part of why it’s so good. “Markdown enterprise-grade” would have been a nightmare. That looseness is exactly what let it spread everywhere and become the substrate AI now rides on — if we’d locked it down with formal specs and enterprise extensions, it never would have become universal.

**What is the optimal ecosystem for standards growth and adoption?**

The first versions of things like OpenID and OAuth were markdown-style — I could implement them even as a lousy coder. Then they all got “enterprised up.” As a dev-rel person I was thrilled: Microsoft’s on board, IBM’s on board, this is validation! And then the enterprise-grade version became impossible to implement. What I used to hack together by viewing source now took all weekend just to get running. RSS went through the same thing — huge emotional battles to formalize an XML spec and take it to the IETF, and none of it amounted to a hill of beans. The thing that actually worked was “make it work, run some conformance tests, ship a profile that’s good enough.” Technical correctness and standardization make capture easy for whoever has the budget to send someone to a standards meeting — so I’ve learned to be wary of my own bias toward it.

**How do you reconcile the early web with what we have today?**

There have been times I’ve lost faith and been disheartened by how awful it is — so much of our careers were built on being out there making real connections, and a platform like Twitter, where I made my reputation, is now somewhere I’ll never be again. So you grieve it, and you think, well, it must be over. But then I look at someone like Steve Yegge writing about Ghosttown, full mad-scientist mode, AI all the way down — purely his own vision, no corporate overlord behind it. Or Simon Willison, just putting points on the board every day: “here’s what I found,” no hype. Both have been doing that for twenty-plus years. And there’s some young coder on the other side of the world reading it thinking “I can do that” — she’ll make the next markdown. You cannot stop that. The web gave me everything, so the next person who shows me how to make something great on it is my friend.

**Do you feel that you write for an audience who is at or below the API line?**

I think that’s right. Tim O’Reilly is an optimist with access to a lot of power and resource, and it’s easier to be optimistic from there — he writes above the line. I’m an optimist too, but I’m closer to a lot of people who don’t have that, so I tend to write for them, and unapologetically so. A lot of people on LinkedIn are writing for their boss; that’s well covered, and it’s very easy to tell comforting things to your boss — I did plenty of that as a CEO, fitting neatly inside what VCs want to hear. My highest mandate now is to teach how systems work, especially for people early or vulnerable in their careers, because if you understand the system you can have power in it. People sometimes read that as me being critical, but debugging is an act of hope — you’re trying to make it run. “Pull requests welcome” is an invitation to join a community.

**Is there opportunity for someone to find the signal in the AI noise?**

Think about what’s actually happening: systems that build software at unimaginable scale, from an individual, to the point where it’s almost disposably cheap. I can imagine building competing versions of the same app, testing which runs best, and throwing away ninety percent of them — it’s too cheap to meter. Now, the wealthiest, most powerful people in our industry have spent fifteen years banging the “software is eating the world” drum to get all the power and wealth they wanted. But in a world where making software is that cheap, what kind of power do they actually have? Maybe it shifts to the people who understand this new world. Remember, when we built a company in 2001 the unbeatable gorilla was AOL — a third of America connected through them. Yahoo was number one in every category. Ask a kid today what they think of Yahoo. The incumbents always look insurmountable right before they aren’t.

**What gives you hope?**

I’m very much a student of history and cycles. You look at a hundred years ago: you had a pandemic, then a global rise of an authoritarian movement, then economic hard times. And then — what happened with labor? With civil rights? With jazz, with film? An enormous amount of creativity and progress came out the other side. So there are real causes for optimism here, and it takes time. I don’t think of this as a two-year project. It’s a rest-of-my-life effort, and I’m fine with that. The new capabilities we’re building can reinvent what we think is possible the same way commodity open-source tools once let a scrappy team scale the first social networks past the giants who were charging millions in database rent. If you want to predict the future, invent it — and a lot of us can imagine making things people actually want to adopt, consensually.

**Why do you blog?**

We’ve got so many stories to tell, and I want everybody who has the ability to be blogging to narrate theirs, because there’s such a hunger for it. People want more real things, more experiences; they want to hear more of the story. So that’s the thing I teach everyone to do: take a minute. You don’t have to be some elaborate storyteller, it doesn’t have to be 10,000 words — just a little bit of that every day, as often as you can. I think it’s so valuable. You’ve got to be human, and that’s what’s going to shine in this AI moment. The entire internet is made of regular people who, in between going out for beers or planting their garden, are viewing source and copying and pasting. That’s how it was made, and that’s how it can be made again.
