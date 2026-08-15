---
title: "A Thought Experiment in AI Infrastructure"
person: adam-bly
section: by
type: essay
year: 2019
date: 2019-07-11
venue: "Medium"
authors: "Adam Bly"
source_url: https://medium.com/@ab_98871/a-thought-experiment-in-ai-infrastructure-f6f5788a2380
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via Medium's RSS feed (content:encoded), which carries the full post body; Medium's HTML page 403s non-browser clients. Images/figures stripped; inline links preserved as markdown."
---

# A Thought Experiment in AI Infrastructure

## Full text

For a moment, imagine that ten years ago a large healthcare company decided to invest $1 billion in fundamental AI research — making a bet that at some point in the near future, pharma and healthcare would be transformed by data and AI.

Let’s play this out.

It’s 2010. Health Co. hires 1,000 ML and data engineers and research scientists, builds massive data centers, and sets out to design and build the data and ML infrastructure they need to discover new compounds, predict drug interactions and side effects, improve patient outcomes, and invent new business models to drive preventative health. Because very little data and AI infra exists in the market, and because they decide to place a high priority on this bet, Health Co. designs their software from first principles, applicable laws, and the values of the company and their scientists and engineers.

A decade ago, society had already passed laws preventing companies from disclosing patient information and from discriminating on the basis of genetics. Recombinant DNA scientists had already laid out Asilomar principles. Funding from the National Institutes of Health carried the requirement of institutional review boards and open data sharing… and a handful of healthcare companies had started data collaboratives to share pre-clinical trial data in the interest of, for example, jointly tackling neglected tropical diseases. The FDA enforced strict rules around what needed to be demonstrated by Health Co. before shipping a drug out to society and what needed to be communicated and how to doctors and patients.

What would Health Co.’s novel data and ML infra look like? What technical goals would they have optimized for? What first principles would they have asserted?

Explainability (interpretability) would have clearly mattered a lot. Causality would have been a key concern. Data and algorithmic bias would have needed to be addressed from day one to produce common patient outcomes. Teams would have needed to be diverse. Labels, naming conventions, ontologies, identifiers would have had to be made clear and standardized. Data and knowledge sharing would have been required. Models would have needed to be well documented and highly reproducible. Data privacy would have been a non-negotiable.

Let’s leave our thought experiment and come back to the present.

Of course this isn’t how the story played out. Instead, a couple of Internet companies made the big bet on AI a decade ago (to their credit). They’ve since generously and strategically open-sourced many infra technologies. And so, today, AI looks like them… settings which are comparatively unregulated, optimized for closed fast feedback loops where nearly everything can be A/B tested, generally unconcerned by black boxes, and with nearly limitless free compute.

What’s the point of considering this counterfactual? I think it’s important to keep in mind that AI should look and work the way society wants and needs it to look and work — aligned with the mores, laws, ethics, and principles of the science and the society we all want.

I suggest we scrutinize the reasons why, instead, things look and work the way they look and work today. And allow for the possibility that the stack of the future might need to be designed from different first principles and under different conditions than the stack of the past.
