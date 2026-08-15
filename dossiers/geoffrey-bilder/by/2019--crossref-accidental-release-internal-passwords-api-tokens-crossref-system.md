---
title: "Accidental release of internal passwords, & API tokens for the Crossref system"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2019
date: 2019-10-04
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/accidental-release-of-internal-passwords-api-tokens-for-the-crossref-system/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/8nfc6-jze16."
---

# Accidental release of internal passwords, & API tokens for the Crossref system

## Full text

**5 minute read.**

## Accidental release of internal passwords, & API tokens for the Crossref system

## TL;DR

On Wednesday, October 2nd, 2019 we discovered that we had accidentally pushed the main Crossref system as part of a docker image into a developer’s account on Docker Hub. The binaries and configuration files that made up the docker image included embedded passwords and API tokens that could have been used to compromise our systems and infrastructure. When we discovered this, we immediately secured the repo, changed all the passwords and secrets, and redeployed the system code. We have since been scanning all of our logs and systems to see if there has been any unusual activity that could be related to the exposure of the container.

Please note that no external data e.g. member passwords or personal information were exposed; our source code contains only internal passwords and ‘secrets’ such as API tokens.

Thankfully, the way in which these secrets were exposed (in compressed, binary files which were, in turn, in a Docker image) means that they were probably overlooked by the automated exploitation tools which focus on scanning source code. And, so far, we have seen nothing that would indicate that these passwords and secrets have been exploited. We will, of course, inform our members directly (and update this blog) if that changes.

## More than you probably want to know

If you are continuing to read this, my guess is that you might have questions like:

1. Why are you doing something as silly as embedding secrets and passwords in your code?
2. And wait a minute… I thought Crossref code was open source?
3. And why is the director of strategic initiatives announcing this?

Let me answer these questions in random order.

In March 2019 I took over Crossref’s technical teams when Chuck Koscher announced that he would be retiring at the end of the year. I’m now the director of technology & research.

A few months earlier we had already concluded that a major portion of the Crossref system had accumulated 20 years of technical debt and that we were going to spend a significant portion of 2019 and 2020 paying down that debt.

Specifically, a lot of the code that runs Crossref was inherited from a third party who developed it back in the early 2000s. This means that, even though any new systems that we’ve developed since 2007 have been open-source, the code for the oldest parts of the system has remained closed because it contained potentially proprietary code as well as a lot of deprecated coding practices. Also - the architecture, the tooling, and the development processes behind the Crossref system had not changed much in those twenty years. It was fantastic architecture, tooling, and code for its time. But architectures that scale to millions of records need to change to handle hundreds of millions of records. Processes that work for configuring one service need to change when you are managing dozens of services. And support tools that work for a few hundred members break down when you are dealing with tens of thousands of members.

These parts of the Crossref system were decidedly not [12 factor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology). We were not using [DevOps](https://en.wikipedia.org/wiki/DevOps) or [SRE](https://en.wikipedia.org/wiki/Site_Reliability_Engineering) working practices to run them. And the bulk of that part of the system is still being run in a traditional data center.

But since March we have been slowly fixing that. In incremental steps. Some of which are visible as a side effect of the security incident that precipitated this blog post. For example, one of our first moves was to move our development to [Gitlab](https://gitlab.com/crossref). Even though a big chunk of the base Crossref code is still closed source, we saw moving to Gitlab as a priority because Gitlab offers a fantastic suite of tools to help automate and manage our deployments. Similarly, we have been Dockerizing the Crossref system so that it is easier to scale and run in different environments. And as part of this effort, we have spent a lot of time on the issue of how to best handle secrets. We knew our secrets management in this part of the codebase was horrible. We have been developing some experiments and infrastructure for handling these secrets securely. But we haven’t finished this work yet. And so the system slipped out into a public repo too early. Ironically, this too illustrates a fundamental change in the way we develop things. [Our default is to be open and transparent](/truths/). This case is currently an exception. An exception we want to eliminate, but one we are not ready to do yet. We have to audit and scrub the code first.

Yes, this incident has been embarrassing. But not nearly as embarrassing as the fact that Crossref has succumbed to a technology industry cliche. That we spent so much time growing and focusing on new features for our members, that we neglected some of the creaking infrastructure of our infrastructure.

And I should be clear about two things:

First, not all of our code is like this. We have, for a long time, been building open source software and using modern best practices for secrets management in our newer subsystems and services. The problems described above are confined to twenty-year-old-code that we didn’t write in the first place and that we had been avoiding refactoring.

And second, the technology team has been marvelous at responding to the challenge we face. They have adopted new processes and tools. They are learning new techniques. We are steadily chipping away at these problems.

It is generally considered bad practice to praise or reward technology teams for fire-fighting instead of fire prevention, but this may be the exception that proves the rule.

I was blown away by how the technology, product, and support teams worked together. When we discovered this problem, I sat at my desk in rural France and watched as staff from the UK, and all three US time zones shut down this problem in just a couple of hours. Obviously, I wish we hadn’t had the problem in the first place, but seeing their response did a great deal to encourage me that we are on the right track.

In any case, it looks like we’ve been lucky. And we’ll be working even harder to refactor our code, tools, and processes so that this kind of thing doesn’t happen again.
