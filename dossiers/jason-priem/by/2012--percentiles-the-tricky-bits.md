---
title: "Percentiles, the tricky bits"
person: jason-priem
section: by
type: blog-post
year: 2012
date: 2012-09-12
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/31408899657/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Percentiles, the tricky bits

## Full text

\
Normalizing altmetrics seem by percentiles seems so easy!  And it is. except when it’s not.

Our first clue that percentiles have tricky bits is that there is no standard definition for [what percentile means](http://en.wikipedia.org/wiki/Percentile#Definition).  When you get an 800/800 on your SAT test, the testing board announces you are in the 98th percentile (or whatever) because 2% of test-takers got an 800… their definition of percentile is **the percentage of tests with scores less than yours.**  A different choice would be to declare that 800/800 is the 100th percentile, representing **the percentage with tests with scores less than or equal to yours.**  Total-impact will use the first definition: when we say something is in the 50th percentile, we mean that 50% of reference items had strictly lower scores.

Another problem: how should we represent ties?  Imagine there were only ten SAT takers: one person got 400, eight got 600s, and one person scored 700.  What is the percentile for the eight people who scored 600?  Well…it depends.

- They are right in the middle of the pack so by some definitions they are in the 50th percentile.
- An optimist might argue they’re in the 90th percentile, since only 10% of test-takers did better.
- And by our strict definition they’d be in the 10th percentile, since they only beat the bottom 10% outright.

The problem is that none of these are really *wrong*; they just don’t include enough information to fully understand the ties situation, and they break our intuitions in some ways.

What if we included the extra information about ties? The score for a tie could instead be represented by a range, in this case the 10th-89th percentile.  Altmetrics samples have a lot of ties: many papers recieve only one tweet, for example, so representing ties accurately is important.  Total-impact will take this range approach, representing ties as percentile ranges. Here’s an example, using PubMed Central citations:

![](https://i0.wp.com/i.imgur.com/flNKV.png?w=1000)

Finally, what to do with zeros?  Impact metrics have many zeros: many papers have never been tweeted.  Here, the range solution also works well.  If your paper hasn’t been tweeted, but neither have 80% of papers in your field, then your percentile range for tweets would be 0-79th.  In the case of zeros, when we need to summarize as a single number, we’ll use 0.

We’ll take these definitions for a [test-drive in the next post](http://wp.me/p2LlD9-7).

*([part 3](http://wp.me/p2LlD9-8) of a series on how total-impact plans to give context to the altmetrics it reports. see [part 1](http://wp.me/p2LlD9-b), [part 2](http://wp.me/p2LlD9-a), and [part 4](http://wp.me/p2LlD9-7).)*
