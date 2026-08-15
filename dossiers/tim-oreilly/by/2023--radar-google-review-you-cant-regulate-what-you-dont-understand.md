---
title: "google-review-You Can’t Regulate What You Don’t Understand"
person: tim-oreilly
section: by
type: blog-post
year: 2023
date: 2023-04-13
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/google-review-you-cant-regulate-what-you-dont-understand/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# google-review-You Can’t Regulate What You Don’t Understand

## Full text

The world changed on November 30, 2022 as surely as it did on August 12, 1908 when the first Model T left the Ford assembly line. That was the date when OpenAI released ChatGPT, the day that AI emerged from research labs into an unsuspecting world. Within two months, ChatGPT had over a hundred million users—faster adoption than any technology in history.

The hand wringing soon began. Most notably, The Future of Life Institute published [an open letter calling for an immediate pause in advanced AI research](<https://futureoflife.org/open-letter/pause-giant-ai-experiments/>), writing hyperbolically: “Should we let machines flood our information channels with propaganda and untruth? Should we automate away all the jobs, including the fulfilling ones? Should we develop nonhuman minds that might eventually outnumber, outsmart, obsolete and replace us? Should we risk loss of control of our civilization?”

In response, the Association for the Advancement of Artificial Intelligence [published its own letter](<https://aaai.org/working-together-on-our-future-with-ai/>) citing the many positive differences that AI is already making in our lives and noting existing efforts to improve AI safety and to understand its impacts. Indeed, there are important ongoing gatherings about AI regulation like [the Partnership on AI’s recent convening on Responsible Generative AI](<https://partnershiponai.org/responsible-generative-ai-lets-get-started/>), which happened just this past week.

The UK has already [announced its intention to regulate AI](<https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper>), albeit with a light, “pro-innovation” touch. The EU and US are sure to follow, in the worst case leading to a patchwork of conflicting regulations. 

All of these efforts reflect the general consensus that regulations should address issues like data privacy and ownership, bias and fairness, transparency, accountability, and standards. [OpenAI’s own AI safety and responsibility guidelines](<https://openai.com/safety>) cite those same goals, but in addition call out what many people consider the central, most general question: how do we align AI-based decisions with human values? They write:

> _“AI systems are becoming a part of everyday life. The key is to ensure that these machines are aligned with human intentions and values.”_

But whose human values? Those of the benevolent idealists that most AI critics aspire to be? Those of a public company bound to put shareholder value ahead of customers, suppliers, and society as a whole? Those of criminals or rogue states bent on causing harm to others? Someone well meaning who, like Aladdin, expresses an ill-considered wish to an all-powerful AI genie? 

Still, too much of the discussion focuses on safeguards against the emergence of “rogue AI.” Despite [the prognostications of doomsayers](<https://www.wired.com/story/plaintext-how-to-start-an-ai-panic/>), these systems are still very much under human control. They do what they are told, and when the results don’t match expectations, their training is quickly improved. _What we need to know is what they are being told._

There is no simple way to solve the alignment problem. But building robust institutions for disclosure and auditing are a good first step. If we want prosocial outcomes, we need to design and report on the metrics that explicitly aim for those outcomes and measure the extent to which they have been achieved.

What should be disclosed? There is an important lesson for both companies and regulators in the rules by which corporations—which science-fiction writer Charlie Stross has memorably called “[slow AIs](<https://boingboing.net/2017/12/29/llcs-are-slow-ais.html>)”—are regulated.

The systems of accounting that we take for granted today and use to hold companies accountable _were originally developed by medieval merchants for their own use._ They were not imposed from without, but were adopted because they allowed merchants to track and manage their own trading ventures. They are universally used by businesses today for the same reason.

We have dozens of organizations that publish AI principles, but they provide little detailed guidance. They all say things like “Maintain user privacy” and “Avoid unfair bias” but they don’t say exactly under what circumstances companies gather facial images from surveillance cameras, and what they do if there is a disparity in accuracy by skin color. The devil is in the details.

So, what better place to start with developing regulations for AI than with the management and control frameworks used by the companies that are developing and deploying advanced AI systems? The creators of generative AI systems and Large Language Models already have tools for monitoring, modifying, and optimizing them. Techniques such as [RLHF (“Reinforcement Learning from Human Feedback”)](<https://huggingface.co/blog/rlhf>) are used to train models to avoid bias, hate speech, and other forms of bad behavior. The companies are collecting massive amounts of data on how people use these systems. And they are stress testing them. They’ve already learned that factors such as session length and the nature of the questions asked can affect AI results. They are post-processing the output, building safety layers, and have begun to harden their systems against “[adversarial prompting](<https://arxiv.org/abs/2203.10714>)” and other attempts to subvert the controls they have put in place. But exactly how this stress testing, post processing, and hardening works—or doesn’t—is mostly invisible to regulators.

_Regulators should start by formalizing and requiring detailed disclosure about the measurement and control methods already used by those developing and operating advanced AI systems._

In the absence of operational detail from those who actually create and manage advanced AI systems, we run the risk that regulators and advocacy groups “[hallucinate](<https://spectrum.ieee.org/ai-hallucination>)” much like Large Language Models do, and fill the gaps in their knowledge with seemingly plausible but impractical ideas.

_Companies creating advanced AI should work together to formulate a comprehensive set of operating metrics that can be reported regularly and consistently to regulators and the public, as well as a process for updating those metrics as new best practices emerge._

Current disclosures by companies are haphazard and inconsistent, sometimes appearing in research papers, sometimes in earnings calls, and sometimes from whistleblowers. It is almost impossible to compare what is being done today with what was done in the past or what might be done in the future. Companies cite user privacy concerns, trade secrets, the complexity of the system, and various other reasons for limiting disclosures. This is unacceptable.

Imagine, for a moment, if the [Generally Accepted Accounting Principles](<https://www.investopedia.com/terms/g/gaap.asp>) or the [International Financial Reporting Standards](<https://www.investopedia.com/terms/i/ifrs.asp>) that guide financial reporting simply said that companies must accurately reflect their true financial condition without specifying in detail what that reporting must cover and what “true financial condition” means? Bodies such as the [Financial Accounting Standards Board](<https://www.fasb.org/>), which created and oversees GAAP, specify those things in excruciating detail. Bodies such as the Securities and Exchange Commission then require public companies to file reports according to GAAP, and auditing firms are hired to review and attest to the accuracy of those reports.

So too with AI safety. What we need is something equivalent to GAAP for AI and algorithmic systems more generally. Might we call it the Generally Accepted _AI_ Principles? We need an independent body to oversee the standards, other bodies equivalent to the [SEC](<https://www.sec.gov/>) and [ESMA](<https://www.esma.europa.eu/>) to enforce them, and we need an ecosystem of auditors that is empowered to dig in and make sure that companies and their products are making accurate disclosures.

Like the regular financial reporting required of corporations, this reporting must be regular and consistent. But unlike financial disclosures, which generally apply only to publicly traded companies, we likely need disclosure requirements to apply to much smaller companies. It might also be worthwhile to enable testing by an outside lab to confirm that best practices are being met and what to do when they are not. One interesting historical parallel for product testing may be found in the certification of fire safety and electrical devices by an outside non-profit auditor, [Underwriter’s Laboratory](<https://ul.org/about#history>). UL certification is not required, but it is widely adopted because it increases consumer trust.

In short, what we need is an ongoing process by which the creators of AI models fully, regularly, and consistently disclose the metrics that _they themselves_ use to manage and improve their services and to prohibit misuse, much as accounting regulations have formalized the tools that companies already used to manage, control, and improve their finances. It’s not always comfortable to disclose your numbers, but mandated disclosures have proven to be a powerful tool for making sure that companies are actually following best practices.

This is not to say that there may not be regulatory imperatives for cutting-edge AI technologies that are outside the existing management frameworks for these systems. National security considerations are a good example. Especially with small LLMs that can be run on a laptop, there is a risk of an irreversible and uncontrollable proliferation of technologies that are still poorly understood. This is what Jeff Bezos has referred to as a “[one way door](<https://www.inc.com/jeff-haden/amazon-founder-jeff-bezos-this-is-how-successful-people-make-such-smart-decisions.html>),” a decision that, once made, is very hard to undo. One way decisions require far deeper consideration, and may require regulation from without that runs ahead of existing industry practices.

Furthermore, as Peter Norvig of the Stanford Institute for Human Centered AI noted in a review of a draft of this piece, “We think of ‘Human-Centered AI’ as having three spheres: the user (e.g., for a release-on-bail recommendation system, the user is the judge); the stakeholders (e.g., the accused and their family, plus the victim and family of past or potential future crime); the society at large (e.g. as affected by mass incarceration).”   

As Princeton computer science professor Arvind Narayanan [has written](<https://knightcolumbia.org/content/understanding-social-media-recommendation-algorithms>), these systemic harms to society that transcend the harms to individuals require a much longer term view and broader schemes of measurement than those typically carried out inside corporations. But despite the prognostications of groups such as the Future of Life Institute, which penned the AI Pause letter, it is usually difficult to anticipate these harms in advance. Would an “automobile pause” in 1908 have anticipated the risks of climate change? Would an “assembly line pause” have led us to anticipate the massive social changes that 20th century industrial production was about to unleash on the world? 

Given the radical uncertainty about the progress and impact of AI, we are better served by mandating transparency and building institutions for enforcing accountability than we are in trying to head off every imagined particular harm.

We shouldn’t wait to regulate these systems until they have run amok. But nor should regulators overreact to AI alarmism in the press. Regulations should first focus on disclosure of current monitoring and best practices. In that way, companies, regulators, and guardians of the public interest can learn together how these systems work, how best they can be managed, and what the systemic risks really might be.
