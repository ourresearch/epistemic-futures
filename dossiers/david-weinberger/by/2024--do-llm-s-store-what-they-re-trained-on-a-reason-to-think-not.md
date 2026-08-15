---
title: "Do LLM’s store what they’re trained on? A reason to think not."
person: david-weinberger
section: by
type: blog-post
year: 2024
date: 2024-09-05
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2024/09/05/do-llms-store-what-theyre-trained-on-a-reason-to-think-not/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# Do LLM’s store what they’re trained on? A reason to think not.

## Full text

If you ask chatGPT to give you the first paragraph of Moby-Dick, it gets it exactly right. This and other such examples are sometimes taken as evidence that it has kept a copy of that book in memory, a potential copyright violation. The makers of these Large Language Models say they don’t, or at least I haven’t come across any who cop to it.

My understanding is that they analyze the terxts they’re trained on looking for statistical relationships, keep the stats and ditch the texts. (In this, they’re similar to how search engines compile their indexes.)

But my understanding is quite limited. So, I poked around.

PROMPT: What is the first paragraph of Moby-Dick, verbatim?

CHATGPT:

Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can

Perfect.

PROMPT: What is the first paragraph of David Weinberger’s book Everything Is Miscellaneous?

CHATGPT:

The first paragraph of Everything is Miscellaneous by David Weinberger reads:

“If you keep your music in iTunes or your photos in Flickr, you’re using an application that lets you put a piece of information in more than one category at a time. That’s weird. In the real world—where our species evolved—everything has its place. Our books are on one shelf at a time, our plates are in one cupboard, and our shoes are by the door or in the closet. That’s the way it’s supposed to be because that’s the way the world is. Except, of course, it’s not.”

This opening sets the stage for Weinberger’s exploration of how digital organization challenges traditional, physical-world categorization.

That’s not a bad intro to the book’s themes: it picks up some of the examples in the book, and it is certainly reminiscent of my style of writing. But it has nothing to do with the first paragraph of the first chapter:

Before the Web, browsing was usually a polite way of telling a salesperson to buzz off. “May I help you?”, a salesperson asks. “I’m just browsing,” you reply with a little smile.With that word, a customer declares a lack of commitment, With that smile, she asserts that she’s within her rights: “Just try and stop me, salesboy!”

I’m slightly embarrassed by that, but the point is that the real first paragraph doesn’t talk about anything mentioned in chatGPT’s attempt to quote it.

Further, while chatGPT can quote the opening of Alice’s Adventures in Wonderland, if you ask it to quote the opening of Carroll’s lesser known “Sylvie and Bruno” it responds:

One winter night, at a little town called Elveston, a telegram was received by the Sub-Warden, who sat sipping his coffee, and wondering lazily whether it was worth while to finish his cigar, or whether he would take a stroll down to the Club, and see if Captain Muriel had returned yet.

Here’s the actual opening:

—and then all the people cheered again, and one man, who was more excited than the rest, flung his hat high into the air, and shouted (as well as I could make out) “Who roar for the Sub-Warden?” Everybody roared, but whether it was for the Sub-Warden, or not, did not clearly appear: some were shouting “Bread!” and some “Taxes!”, but no one seemed to know what it was they really wanted.

The phrase “one winter” doesn’t appear anywhere in the original. Nor does “a little town called Elveston”.

Finally, if you repeat the prompt, it gives substantially different responses, including the unfortunately smutty these days:

‘Less bread!’ cried the poor. I looked again, and saw it was not bread they had needed, but more head.

It seems to unqualified me that this bolsters the claims of the LLM makers that they don’t keep copies of their training materials (or at least don’t make them accessible to the model in operation), and that the training-time statistical analysis of texts that quote other texts, plus the magic of transformer technology, is sufficient to explain how they can provide verbatim quotes of oft-cited works.

Am I wrong? It’s highly likely.
