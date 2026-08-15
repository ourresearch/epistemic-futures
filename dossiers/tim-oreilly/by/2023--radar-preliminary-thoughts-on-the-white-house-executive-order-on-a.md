---
title: "Preliminary Thoughts on the White House Executive Order on AI"
person: tim-oreilly
section: by
type: blog-post
year: 2023
date: 2023-10-30
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/preliminary-thoughts-on-the-white-house-executive-order-on-ai/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# Preliminary Thoughts on the White House Executive Order on AI

## Full text

**Disclaimer:** Based on [the announcement of the EO](<https://www.whitehouse.gov/briefing-room/statements-releases/2023/10/30/fact-sheet-president-biden-issues-executive-order-on-safe-secure-and-trustworthy-artificial-intelligence/>), without having seen the full text.

Overall, the Executive Order is a great piece of work, displaying a great deal of both expertise and thoughtfulness. It balances optimism about the potential of AI with reasonable consideration of the risks. And it doesn’t rush headlong into new regulations or [the creation of new agencies](<https://www.linkedin.com/pulse/shiny-ai-moment-needs-whats-much-less-jennifer-pahlka-bqysc/>), but instead directs existing agencies and organizations to understand and apply AI to their mission and areas of oversight. The EO also does an impressive job of highlighting the need to bring more AI talent into government. That’s a huge win.

Given my own research focus on [enhanced disclosures as the starting point for better AI regulation](<https://www.oreilly.com/content/you-cant-regulate-what-you-dont-understand/>), I was heartened to hear that the Executive Order on AI uses the Defense Production Act to compel disclosure of various data from the development of large AI models. Unfortunately, these disclosures do not go far enough. The EO seems to be requiring only data on the procedures and results of “Red Teaming” (i.e. adversarial testing to determine a model’s flaws and weak points), and not a wider range of information that would help to address many of the other concerns outlined in the EO. These include:

  * **What data sources the model is trained on.** Availability of this information would assist in many of the other goals outlined in the EO, including addressing algorithmic discrimination and increasing competition in the AI market, as well as other important issues that the EO does not address, such as copyright. The recent discovery (documented by [an exposé in The Atlantic](<https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/>)) that OpenAI, Meta, and others used databases of pirated books, for example, highlights the need for transparency in training data. Given the importance of intellectual property to the modern economy, copyright ought to be an important part of this executive order. Transparency on this issue will not only allow for debate and discussion of the intellectual property issues raised by AI, it will increase competition between developers of AI models to license high-quality data sources and to differentiate their models based on that quality. To take one example, would we be better off with the medical or legal advice from an AI that was trained only with the hodgepodge of knowledge to be found on the internet, or one trained on the full body of professional information on the topic?
  * **Operational Metrics.** Like other internet-available services, AI models are not static artifacts, but dynamic systems that interact with their users. AI companies deploying these models manage and control them by measuring and responding to various factors, such as permitted, restricted, and forbidden uses; restricted and forbidden users; methods by which its policies are enforced; detection of machine-generated content, prompt-injection, and other cyber-security risks; usage by geography, and if measured, by demographics and psychographics; new risks and vulnerabilities identified during operation that go beyond those detected in the training phase; and much more. These should not be a random grab-bag of measures thought up by outside regulators or advocates, but [disclosures of the actual measurements and methods that the companies use to manage their AI systems](<https://www.oreilly.com/content/you-cant-regulate-what-you-dont-understand/>).
  * **Policy on use of user data for further training.** AI companies typically treat input from their users as additional data available for training. This has both privacy and intellectual property implications.
  * **Procedures by which the AI provider will respond to user feedback and complaints.** This should include its proposed redress mechanisms.
  * **Methods by which the AI provider manages and mitigates risks identified via Red Teaming, including their effectiveness.** This reporting should not just be “once and done,” but an ongoing process that allows the researchers, regulators, and the public to understand whether the models are improving or declining in their ability to manage the identified new risks.
  * **Energy usage and other environmental impacts.** There has been a lot of fear-mongering about the energy costs of AI and its potential impact in a warming world. Disclosure of the actual amount of energy used for training and operating AI models would allow for a much more reasoned discussion of the issue.

These are only a few off-the-cuff suggestions. Ideally, once a full range of required disclosures has been identified, they should be overseen by either an existing governmental standards body, or a non-profit akin to the Financial Accounting Standards Board (FASB) that oversees accounting standards. This is a rapidly-evolving field, and so disclosure is not going to be a “once-and-done” kind of activity. We are still in the early stages of the AI era, and innovation should be allowed to flourish. But this places an even greater emphasis on the need for transparency, and the establishment of baseline reporting frameworks that will allow regulators, investors, and the public to measure how successfully AI developers are managing the risks, and whether AI systems are getting better or worse over time.

## **Update**

After reading the details found in [the full Executive Order on AI](<https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/>), rather than just the White House summary, I am far less positive about the impact of this order, and what appeared to be the first steps towards a robust disclosure regime, which is a necessary precursor to effective regulation. The EO will have no impact on the operations of current AI services like ChatGPT, Bard, and others under current development, since its requirements that model developers disclose the results of their “red teaming” of model behaviors and risks only apply to future models trained with orders of magnitude more compute power than any current model. _In short, the AI companies have convinced the Biden Administration that the only risks worth regulating are the science-fiction existential risks of far future AI rather than the clear and present risks in current models._

It is true that various agencies have been tasked with considering present risks such as discrimination in hiring, criminal justice applications, and housing, as well as impacts on the job market, healthcare, education, and competition in the AI market, but those efforts are in their infancy and years off. The most important effects of the EO, in the end, turn out to be the call to increase hiring of AI talent into those agencies, and to increase their capabilities to deal with the issues raised by AI. Those effects may be quite significant over the long run, but they will have little short-term impact.

In short, the big AI companies have hit a home run in heading off any effective regulation for some years to come.
