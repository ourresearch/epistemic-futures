---
title: "Copyright-Aware AI: Let’s Make It So"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-04-02
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/copyright-aware-ai-lets-make-it-so/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Copyright-Aware AI: Let’s Make It So

## Full text

On April 22, 2022, I received an out-of-the-blue text from Sam Altman inquiring about the possibility of training GPT-4 on O’Reilly books. We had a call a few days later to discuss the possibility.

As I recall our conversation, I told Sam I was intrigued, but with reservations. I explained to him that we could only license our data if they had some mechanism for tracking usage and compensating authors. I suggested that this ought to be possible, even with LLMs, and that it could be the basis of a participatory content economy for AI. (I later wrote about this idea in a piece called “[How to Fix AI’s Original Sin](<https://www.oreilly.com/radar/how-to-fix-ais-original-sin/>).”) Sam said he hadn’t thought about that, but that the idea was very interesting and that he’d get back to me. He never did.

And now, of course, given reports that Meta has trained Llama on LibGen, the Russian database of pirated books, one has to wonder whether OpenAI has done the same. So working with colleagues at the [AI Disclosures Project](<https://www.ssrc.org/programs/ai-disclosures-project/>) at the Social Science Research Council, we decided to take a look. Our results were published today in the working paper “[Beyond Public Access in LLM Pre-Training Data](<https://www.ssrc.org/publications/beyond-public-access-in-llm-pre-training-data-non-public-book-content-in-openais-models/>),” by Sruly Rosenblat, Tim O’Reilly, and Ilan Strauss.

There are a variety of statistical techniques for estimating the likelihood that an AI has been trained on specific content. We chose one called DE-COP. In order to test whether a model has been trained on a given book, we provided the model with a paragraph quoted from the human written book along with three permutations of the same paragraph, and then asked the model to identify the “verbatim” (i.e., correct) passage from the book in question. We repeated this several times for each book.

O’Reilly was in a position to provide a unique dataset to use with DE-COP. For decades, we have published two sample chapters from each book on the public internet, plus a small selection from the opening pages of each other chapter. The remainder of each book is behind a subscription paywall as part of our O’Reilly online service. This means we can compare the results for data that was publicly available against the results for data that was private but from the same book. A further check is provided by running the same tests against material that was published after the training date of each model, and thus could not possibly have been included. This gives a pretty good signal for unauthorized access.

We split our sample of O’Reilly books according to time period and accessibility, which allows us to properly test for model access violations:

  
_Note_ : The model can at times guess the “verbatim” true passage even if it has not seen a passage before. This is why we include books published after the model’s training has already been completed (to establish a “threshold” baseline guess rate for the model). Data prior to period _t_ (when the model completed its training), the model may have seen and been trained on. Data after period _t_ the model could not have seen or have been trained on, as it was published after the model’s training was complete. The portion of private data that the model was trained on represents likely access violations. This image is conceptual and not to scale.

We used a statistical measure called AUROC to evaluate the separability between samples potentially in the training set and known out-of-dataset samples. In our case, the two classes were (1) O’Reilly books published before the model’s training cutoff (t − n) and (2) those published afterward (t + n). We then used the model’s identification rate as the metric to distinguish between these classes. This time-based classification serves as a necessary proxy, since we cannot know with certainty which specific books were included in training datasets without disclosure from OpenAI. Using this split, the higher the AUROC score, the higher the probability that the model was trained on O’Reilly books published during the training period.

The results are intriguing and alarming. As you can see from the figure below, when GPT 3.5 was released in November of 2022, it demonstrated some knowledge of public content but little of private content. By the time we get to GPT 4o, released in May 2024, the model seems to contain more knowledge of private content than public content. Intriguingly, the figures for GPT 4o mini are approximately equal and both near random chance suggesting either little was trained on or little was retained.

AUROC Scores based on the models’ “guess rate” show recognition of pre-training data:

Note: Showing book level AUROC scores (n=34) across models and data splits. Book level AUROC is calculated by averaging the guess rates of all paragraphs within each book and running AUROC on that between potentially in-dataset and out-of-dataset samples. The dotted line represents the results we expect had nothing been trained on. We also tested at the paragraph level. See the paper for details.

We chose a relatively small subset of books; the test could be repeated at scale. The test does not provide any knowledge of how OpenAI might have obtained the books. Like Meta, OpenAI may have trained on databases of pirated books. ([_The Atlantic_ ’s search engine against LibGen](<https://www.theatlantic.com/technology/archive/2025/03/search-libgen-data-set/682094/>) reveals that virtually all O’Reilly books have been pirated and included there.)

Given [the ongoing claims from OpenAI](<https://www.linkedin.com/posts/chris-lehane-2562535_for-decades-the-legal-concept-of-fair-use-activity-7310623933781745664-iCe3/>) that without the unlimited ability for large language model developers to train on copyrighted data without compensation, progress on AI will be stopped, and we will “lose to China,” it is likely that they consider all copyrighted content to be fair game.

The fact that DeepSeek has done to OpenAI itself exactly what it has done to authors and publishers doesn’t seem to deter the company’s leaders. OpenAI’s chief lobbyist, Chris Lehane, “[likened OpenAI’s training methods to reading a library book](<https://techcrunch.com/2025/02/10/openai-spoke-to-government-officials-about-its-deepseek-probe/>) and learning from it, whereas DeepSeek’s methods are more like putting a new cover on a library book, and selling it as your own.” We disagree. ChatGPT and other LLMs use books and other copyrighted materials to create outputs that _can_  substitute for many of the original works, much as DeepSeek is becoming a creditable substitute for ChatGPT. 

There is clear precedent for training on publicly available data. When Google Books read books in order to create an index that would help users to search them, that was indeed like reading a library book and learning from it. It was a transformative fair use.

Generating derivative works that can compete with the original work is definitely not fair use.

In addition, there is a question of what is truly “public.” As shown in our research, O’Reilly books are available in two forms: portions are public for search engines to find and for everyone to read on the web; and others are sold on the basis of per-user access, either in print or via our per-seat subscription offering. At the very least, OpenAI’s unauthorized access represents a clear violation of our terms of use.

We believe in respecting the rights of authors and other creators. That’s why at O’Reilly, we built a system that allows us to create AI outputs based on the work of our authors, but uses RAG (Retrieval Augmented Generation) and other techniques to [track usage and pay royalties,](<https://www.oreilly.com/radar/the-new-oreilly-answers-the-r-in-rag-stands-for-royalties/>) just like we do for other types of content usage on our platform. If we can do it with our far more limited resources, it is quite certain that OpenAI could do so too, if they tried. That’s what I was asking Sam Altman for back in 2022.

And they _should_ try. One of the big gaps in today’s AI is its lack of a virtuous circle of sustainability (what Jeff Bezos called “[the flywheel](<https://feedvisor.com/resources/amazon-trends/amazon-flywheel-explained/>)”.) AI companies have taken the approach of expropriating resources they didn’t create, and potentially decimating the income of those who do make the investments in their continued creation. This is shortsighted.

At O’Reilly, we aren’t just in the business of providing great content to our customers. We are in _the business of incentivizing its creation_. We look for knowledge gaps—that is, we find things that some people know but others don’t and wish they did—and help those at the cutting edge of discovery share what they learn, [through books, videos, and live courses](<http://oreilly.com>). Paying them for the time and effort they put in to share what they know is a critical part of our business.

We launched our online platform in 2000 after getting a pitch from an early ebook aggregation startup, Books 24×7, that offered to license them from us for what amounted to pennies per book per customer—which we were supposed to share with our authors. Instead, we invited our biggest competitors to join us in a shared platform that would preserve the economics of publishing and encourage authors to continue to spend the time and effort to create great books. This is the content that LLM providers feel entitled to take without compensation.

As a result, copyright holders are suing, putting up stronger and stronger blocks against AI crawlers, or going out of business. This is not a good thing. If the LLM providers lose their lawsuits, they will be in for a world of hurt, paying large fines, re-engineering their products to put in guardrails against emitting infringing content, and figuring out how to do what they should have done in the first place. If they win, we will all end up the poorer for it, because those who do the actual work of creating the content will face unfair competition.

It is not just copyright holders who should want an AI market in which the rights of authors are preserved, and they are given new ways to monetize, but LLM developers. The internet as we know it today became so fertile because it did a pretty good job of preserving copyright. Companies such as Google found new ways to help content creators monetize their work, even in areas that were contentious. For example, faced with demands from music companies to take down user-generated videos using copyrighted music, YouTube instead developed [Content ID](<https://support.google.com/youtube/answer/2797370?hl=en>), which enabled them to recognize the copyrighted content, and to share the proceeds with both the creator of the derivative work and the original copyright holder. There are numerous startups proposing to do the same for AI-generated derivative works, but, as of yet, none of them has the scale that is needed. The large AI labs should take this on.

Rather than allowing the smash and grab approach of today’s LLM developers, we should be looking ahead to a world in which large centralized AI models can be trained on all _public content_ and _licensed private content_ , but recognize that there are also many specialized models trained on _private content_ that they cannot and should not access. Imagine an LLM that was smart enough to say “I don’t know that I have the best answer to that; let me ask Bloomberg (or let me ask O’Reilly; let me ask _Nature_ ; or let me ask Michael Chabon, or George R.R. Martin (or any of the other authors who have sued, as a stand in for the millions of others who might well have))_and I’ll get back to you in a moment.”_  This is a perfect opportunity for an extension to [MCP](<https://www.anthropic.com/news/model-context-protocol>) that allows for two-way copyright conversations and negotiation of appropriate compensation. The first general-purpose copyright-aware LLM will have a unique competitive advantage. Let’s make it so.
