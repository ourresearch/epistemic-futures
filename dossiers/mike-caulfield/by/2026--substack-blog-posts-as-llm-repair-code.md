---
title: "Blog Posts as LLM Repair Code"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-07-22
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/blog-posts-as-llm-repair-code
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Blog Posts as LLM Repair Code

*To Fix the Crappy Prompts Claude Wrote for You, Have Claude Read My Blog Post*

## Full text

I did a very weird thing today. I fixed my prompts by having Claude read my blog post on why its Claude-edited prompts perform so poorly.

Let’s start with the problem.

As I mentioned a couple weeks ago, all the prompts Claude writes for you [are ](<https://mikecaulfield.substack.com/p/i-finally-understand-why-llms-suck?r=hbr2>)_[bad](<https://mikecaulfield.substack.com/p/i-finally-understand-why-llms-suck?r=hbr2>)_ , they are both overspecified and too general and the the way that Fable processes them will make them fail even more. This will happen because among other things Fable takes all those ridiculous guardrails Opus wrote into your prompts much more seriously than Opus did. 

But if you’re like me and have found out that Claude Opus has been “helpfully” “improving” your prompts and tags behind the scenes and degrading performance, you have dozens or hundreds of these out there that need all that overspecified cruft removed. I detail all this and the particular failure modes of Claude-created prompts in this [linked post](<https://mikecaulfield.substack.com/p/i-finally-understand-why-llms-suck?r=hbr2>). I explain why Claude-created prompts fail, and what you have to do to fix them. But it’s still a lot of work to clean them up.

But there’s a very weird fix to this. 

**You can have it read my blogpost on this issue.**

Here’s what I did 20 minutes ago that worked at least on my prompts. I typed in this to Claude Code:

> read this and then look through my tag definitions and find the 20 worst offenders and suggest rewrites <https://mikecaulfield.substack.com/p/i-finally-understand-why-llms-suck>

[](<https://substackcdn.com/image/fetch/$s_!IEQG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e899863-9f40-4021-ab56-e0c7c6e5893c_1693x318.png>)

I say tags here in this prompt, but you can do it with any prompt with an inclusion condition. And you will get something like this:

[](<https://substackcdn.com/image/fetch/$s_!4E1N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c004cf6-ab5c-44c1-8336-0ff1225b91a8_1665x573.png>)

This can also work it you yourself have added too much detail. Or you can write you own blogpost on your own issue, and link to that.

Watching this all it just struck me that this is a very weird world. A world where the way I fix errors in my prompts is write a blog post about the error pattern and have Fable read it. The idea of a blog post as a referenceable bug fix for your code base. And a failure mode that is incredibly dumb, but a repair mode that is beyond cool.
