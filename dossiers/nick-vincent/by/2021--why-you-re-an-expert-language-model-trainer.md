---
title: "Why You're an Expert \"Language Model Trainer\"!"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2021
date: "2021-03-31"
venue: "PSA Computing Blog (People, Space and Algorithms Research Group, Northwestern University)"
authors: "Nicholas Vincent"
source_url: "https://www.psagroup.org/blogposts/78"
retrieved: "2026-08-13"
content: "full-text"
notes: "Site is a JS SPA; text retrieved via the underlying WordPress REST API (https://www.psagroup.org/blog/wp-json/wp/v2/posts/78)."
---

# Why You're an Expert "Language Model Trainer"!

## Full text

This is a first draft, initially published on March 31st, 2021. I’m hoping to update this blog post, incorporating comments and thoughts you may have (and crediting all feedback givers, if you’re ok with that!). Thanks to Hanlin Li and Jack Bandy for comments on the first draft.

I’ve previously written about how if you ever edited Wikipedia, voted on Reddit posts, or published publicly available text on the web (that appears in the Common Crawl), you helped train the headline–grabbing and controversial GPT-3.

With eleuther.ai’s release of “The Pile” dataset and corresponding GPT-Neo language model, the chances you’re a contributor to language-related AI systems are higher than ever. There are good reasons that you may be concerned to hear this, but there are also reasons to feel excited about being a contributor to this dataset!

If you’ve ever posted

-a paper on arXiv

-code on Github

-a question or answer on Stack Exchange

-a comment on HackerNews

-papers to a variety of other publicly accessible sources (e.g. PubMed, FreeLaw, PhilPapers)

Your contributions will help train any systems that use The Pile, a new open-source “set of datasets”. There’s a good chance The Pile will become quite popular for training language models and other powerful text-related AI systems, especially considering the exact data used to train GPT-3 is not available to directly download.

Should you be concerned about this? A recent high-profile paper highlighted many possible risks about large language models. It’s not hard to imagine a scenario in which a language model spits out some seriously harmful text, and indeed researchers have found both high-profile examples and have studied such harms systematically.

I will note that in the Pile’s pre-print, the authors make a serious effort to engage with literature that has suggested ways to deal with the harms of large text datasets. I don’t feel qualified to make a judgment here as to how successful they were, and I’m curious what others think about this topic! I would definitely suggest checking out Sections 6 and 7 of the above pre-print, and the references they engage with.

So there are some strong arguments for being unhappy that you might be unwittingly training harmful AI systems. What about when language models work well, creating utility for people (e.g. better search results) and creating profits for firms? Well, if you helped create the technologies, do you deserve some of the profits? You could certainly argue that you deserve more than just access to online services for your labor, but the specifics are up for debate.

If you are angry about language models, or think you deserve compensation for your labor, what can you do about it?

With recent advances in privacy protection tools and laws, a group may be able to exert “data leverage” by deleting, withholding, modifying, or redirecting data (see here for more on how you might exert data leverage today!). However, deleting or poisoning your data seems hard in the case of massive open datasets: all this text is already “out there”. The Pile pre-print also engages with early questions around the legality and ethics of using so-called “public” data, though there are no easy answers here. Additionally, in the case of data in The Pile, you probably don’t want to take your papers off arXiv or your code off GitHub. Do you need to consign yourself to being an unpaid expert language model trainer for perpetuity?

On one hand, we simply don’t know how the legal disputes around data deletion for this kind of datasets will shake out. It may be the case that you can delete your data, but it may be that the horses are truly out of the barn. You can, however, delete data now (or withhold data you would have otherwise contributed) so it’s not collected in the future.

On the other hand, choosing to keep data contributions in these datasets can also exert data leverage. “Conscious data contribution” allows the public to exert leverage by providing data to help smaller companies compete with large ones. From this perspective, contributing data to a large open source dataset can be seen as helping to level the training data playing field. In other words, the fact you contributed to The Pile could help a new start-up compete with OpenAI or Google (though these organizations can also benefit from the data). Of course, actually using datasets like The Pile requires capital for computation, hiring employees, etc, so the pool of organizations that can fully benefit from “conscious data contribution” is limited. Nonetheless, it makes sense to consider that contributing to such datasets may be well aligned with your values (though it would still be entirely reasonable to want to delete data contributions you’ve made to other firms’ proprietary datasets).

Furthermore, as more datasets become “open” (and therefore “data strikes” are harder to engage in), there may be a stronger argument for state intervention. One option, which I’ve been involved in writing about, would be a “data dividend” implemented as a data-dependence tax that funds public goods and data industrial policy .

One takeaway I feel confident in is that The Pile provides more evidence that almost all “AI” systems are the products of massive collective effort. The public plays a critical role in making the marvels of modern computing possible, and we must prepare for how this will reshape the power dynamics of computing.
