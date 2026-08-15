---
title: "Weekly Roundup (October 23, 2024)"
person: tim-oreilly
section: by
type: blog-post
year: 2024
date: 2024-10-23
venue: "Asimov’s Addendum"
authors: "Tim O'Reilly, Ilan Strauss"
source_url: https://asimovaddendum.substack.com/p/weekly-roundup-207
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “The world of AI, innovation, competition, and regulation as we think of it.”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# Weekly Roundup (October 23, 2024)

## Full text

**The Geopolitics of Technological Innovation**. While it is not directly or solely connected to AI governance, Henry Farrell’s latest post, [“Small Yard, High Fence”: These four words conceal a mess](<https://www.programmablemutter.com/p/small-yard-high-fence-these-four>), frames the larger context perfectly. When we proposed our project on mandating a higher level of AI disclosure, one insightful funder proposed a one-word critique of our thesis: “ _China_.” Regulation of new technologies is embedded in a web of social and geopolitical considerations. One of Henry’s recommendations is that academics “build intellectual frameworks that better capture the trade-offs of innovation and national security.” We wholeheartedly agree.  
  
**Sabotage Evaluations for Frontier Models**. Anthropic’s [latest announcement ](<https://www.anthropic.com/research/sabotage-evaluations>)on a [new set of evaluations](<https://assets.anthropic.com/m/377027d5b36ac1eb/original/Sabotage-Evaluations-for-Frontier-Models.pdf>) that test a model’s capacity for _sabotage_ highlighted two things for us: 1. It would be great if the industry could converge on a comprehensive set of evals, so that all models are safe, not just those, like Anthropic, that seem to be especially committed to AI safety. 2. We need to go beyond safety testing in the lab to understand how AI models will be deployed with ongoing monitoring. The blog post announcing the new evals gave a hint of this idea in its opening analogy – “Nuclear power stations have continuous radiation monitoring and regular site inspections” – but the post didn’t disclose the extent to which the new evals would actually be deployed continuously rather than simply tested during model development. In this case, the research results don’t yet call for ongoing monitoring, but the distinction is an important one to make. We cover this idea a bit more in our recent post “[Is AI Safety a Potemkin Village?](<https://open.substack.com/pub/asimovaddendum/p/is-ai-safety-a-potemkin-village?r=8vqsy&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true>)” The extent to which safety controls are deployed as part of user and developer-facing services is something that should be disclosed. _These are ongoing services, with all that implies, not just fixed products that can be tested then deployed without monitoring_.  

_Thanks for reading Asimov’s Addendum!_ (More below.) Subscribe here:

Subscribe

  
**Name Related Bias in LLMs**. OpenAI released a [new study](<https://openai.com/index/evaluating-fairness-in-chatgpt/>) focusing on how answer quality varied depending on a user's name on their own models. Given that model bias has been to shown to [significantly hurt performance](<https://arxiv.org/abs/2311.04892>), this was an important thing to test for. And even more so given that GPT now seems to include the user’s name when responding to queries.

**Mistral Changes Course**. In a major departure from the past, [Mistral AI](<https://docs.mistral.ai/getting-started/models/models_overview/>), who were once seen as the open alternative to llama, have now added a restrictive research licence to their new [8b model](<https://mistral.ai/news/ministraux/>) making it the smallest model they released with a restrictive licence. They also did not publicly release the [3b model](<https://mistral.ai/news/ministraux/>) they announced and will instead only allow it to be used in a commercial agreement.

[](<https://substackcdn.com/image/fetch/$s_!CGu1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ed245f3-ca4b-4754-afc3-9ec0174f81a9_876x396.png>)

**The global AI market**. One result of a lack of AI regulation in the U.S. is that more regulated Chinese firms are looking to enter this market. Notes [Bloomberg](<https://www.bloomberg.com/opinion/articles/2024-10-16/can-china-s-ai-dragons-make-it-in-the-us?utm_medium=email&utm_source=newsletter&utm_term=241018&utm_campaign=sharetheview>): "domestic [Chinese] consumers have shown a reluctance to pay for AI apps, and strict regulation limits their utility", leading the major Chinese AI companies to now enter the U.S. AI market. So, far from a lax domestic regulatory environment making U.S. AI firms more competitive, it might just instead help subject them to greater competition from more regulated companies abroad.

**AI Agents and Monetization Strategies**. With Microsoft releasing AI agents in preview in December, a diversity of related monetization strategies is emerging. "The agents are like smartphone apps for the AI age, said [Jared Spataro](<https://www.bloomberg.com/news/articles/2024-10-21/microsoft-launches-ai-agents-deepening-rivalry-with-salesforce>), who oversees Microsoft’s workplace AI products". While this analogy seems a bit off, how exactly AI Agents will be monetized remains an important mystery. Microsoft will include the agents in its Copilot Studio subscription for now it seems. Salesforce, by contrast, will deploy its AI agents to handle tasks like customer service without any human supervision and [charging](<https://www.bloomberg.com/news/articles/2024-10-21/microsoft-launches-ai-agents-deepening-rivalry-with-salesforce>) $2 per conversation. Monetizing based on conversation quantity (or length) might introduce a bunch of economic motives which risk harming consumer outcomes if we aren’t careful, just like monetization based on engagement did. Only corporate disclosures of their internal A/B testing — their ongoing monitoring of deployed models — and time will tell.  
  
**Power and Progress for AI Institution Building**. Daron Acemoglu, Simon Johnson and James Robinson won the Nobel Memorial Prize for Economics for their novel empirical work establishing that [institutions shaped differences in economic growth](<https://www.nobelprize.org/uploads/2024/10/advanced-economicsciencesprize2024.pdf>) between countries, and that colonial strategies was a key driver of institutional change.* More generally, they found that more inclusive institutions are the key to greater long term prosperity. This seems like a very relevant framing of the choice we face with AI. For example, the unfettered ability of AI model developers to extract value from existing content providers without compensation echoes the resource extraction regime of many colonialist powers. The kind of inclusive economy I described in “[How to Fix AI’s ‘Original Sin’](<https://www.oreilly.com/radar/how-to-fix-ais-original-sin/>)” points to the need for a different set of institutions and approaches. Acemoglu and Johnson’s 2023 book, _[Power and Progress](<https://shapingwork.mit.edu/power-and-progress/>)_ , tackles the question of what institutions and approaches are needed to spread the benefits of new technologies – including AI – more broadly. It is required reading. Here are some insightful reviews: Bill Janeway’s "“[The Political Economy of Technology](<https://www.billjaneway.com/the-political-economy-of-technology>)”, [Noah Smith’s critique](<https://www.noahpinion.blog/p/book-review-power-and-progress>), and [Henry Farrell’s rebuttal](<https://www.programmablemutter.com/p/dr-panglosss-panopticon>).  

* * *

* **** The two key papers cited in the [Prize’s scientific background paper](<https://www.nobelprize.org/uploads/2024/10/advanced-economicsciencesprize2024.pdf>) will be familiar to economists:**  
  
** \- **** Acemoglu, D., S. Johnson, and J.A. Robinson (2001), “The Colonial Origins of Comparative Development: An Empirical Investigation”, American Economic Review 91, 1369–1401.   
  
\- Acemoglu, D., S. Johnson, and J.A. Robinson (2002), “Reversal of Fortune: Geography and Institutions in the Making of the Modern World Income Distribution”, Quarterly Journal of Economics 117, 1231–1294.
