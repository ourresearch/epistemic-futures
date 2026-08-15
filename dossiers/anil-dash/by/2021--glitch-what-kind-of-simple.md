---
title: "What do we mean by \"simple\"?"
person: anil-dash
section: by
type: blog-post
year: 2021
date: 2021-06-15
venue: "Glitch blog (blog.glitch.com; formerly Fog Creek)"
authors: "Anil Dash"
source_url: https://blog.glitch.com/post/what-kind-of-simple/
retrieved: 2026-08-13
content: full-text
notes: "Company blog post authored by Dash as CEO"
---

# What do we mean by "simple"?

## Full text

Recently, we [launched a whole new set](<https://blog.glitch.com/post/a-closer-look-at-the-new-glitch-starter-apps>) of starter apps on Glitch, with the goal of making it nearly instant to build apps using the latest and greatest frameworks. Naturally, while creating these new experiences, we wanted things to be simple. But that raised an important question:

**What kind of simple?**

Going back a few years, we built Glitch around the idea that anyone should be able to create a real website or app using standard code, right from their browser, and have it up and running instantly. Today, that’s more or less the case, and the evidence is that clever folks (like you!) have used Glitch to build over ten million apps.

For some users, like students learning to code for the first time, “simple” may best mean “has the fewest distractions”. And in that context, distractions can be things like metadata or configuration options that, while useful for a production website, might require a lot of confusing explanation at a point when a learner is first trying to understand the major concepts they’re wrangling with.

By contrast, for coders who may be familiar with web development in general, but might not know the specifics of a new framework that they’re trying out for the first time (or for the first time in a long time), the typical boilerplate that one might see in an app are familiar and reassuring parts of a web page that they expect to see. And so, “simple” means “it handles all those little default chores for you, so you don’t have to”.

These are both valid expressions of “simple”, and both vitally important to audiences we care deeply about. Having simple experiences that anybody can use to start coding productively is a key part of tackling the stress we call "[stack anxiety](<https://blog.glitch.com/post/ending-stack-anxiety>)". But these two versions of simplicity are also **mutually exclusive** — we can’t make an app that’s “simple” by having fewer lines of distracting metadata while simultaneously making one that’s “simple” by giving you all the default metadata out of the box. We can’t be simple by automatically handling configuration while also being simple by making it easy to customize configuration.

So we took an uncharacteristic path for Glitch: **We chose both.**

Typically, we’ve had a strong bias toward being opinionated, while offering customization under that hood. That way, we can have a predictable experience that users on the platform can share, and also we can smooth the rough edges of one particular designed experience. But we’re at a stage of maturity and familiarity with the ways that people want to build on Glitch which lets us offer a little more flexibility without losing that ease of use.

Thus: “Hello” and “mvp”. (Here, we're using "mvp" to mean "minimum viable product", a common industry term for the simplest version of a project that could possibly do the job.) For each of our common frameworks, we offer each of these two options:

  * **Hello: **a starter app that’s set up with all the most popular default configuration settings and boilerplate provided for you out of the box

  * **MVP: **a starter app that’s the absolute minimum to get you running, with nothing that you might want to delete and no distractions of anything unfamiliar These two approaches encompass two different but valuable views of simplicity:

  * “Do it for me, but let me change it later if I need to”

  * “Don’t do anything for me except the essentials, so I don’t have any distractions” We’d love to hear how those choices work for you, and also how you think about what “simple” is for creating. The early response to these choices has been phenomenal. One way we could tell that this approach is working is by looking at examples like these Preact starters, created by a community member, which already follow the implicit convention we’ve been creating. The fact that people in the community can intuit how these kinds of examples should work means that it’s comprehensible enough for people to understand the whole system, not just one individual implementation. And it’s creators in the community who see the benefit.

We’ll be accelerating our creation of opinionated new starter apps in both flavors of “simple”, using the toolkits, frameworks and libraries you’ve asked for most. If you want to be part of creating one, or to see your favorite technology featured, reach out and share your ideas (or example apps!) with us. And if you’ve tried out the new, simpler starter apps, let us know what would make them even more useful for your workflow. We want things to be as simple as possible.
