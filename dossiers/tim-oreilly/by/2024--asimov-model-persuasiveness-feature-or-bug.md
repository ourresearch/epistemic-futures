---
title: "Model Persuasiveness: Feature or bug?"
person: tim-oreilly
section: by
type: blog-post
year: 2024
date: 2024-10-02
venue: "Asimov’s Addendum"
authors: "Tim O'Reilly, Ilan Strauss"
source_url: https://asimovaddendum.substack.com/p/model-persuasiveness-feature-or-bug
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “OpenAI's latest model cards consider persuasiveness as an AI risk. But will it stay that way? What happens when AI business models benefit from persuasion?”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# Model Persuasiveness: Feature or bug?

## Full text

GPT model _persuasiveness_ – that is, whether the model can convince people to change their beliefs or to act on the basis of advice or feedback from the model – is quite rightly rated as a risk by OpenAI in its latest [o1 System Card](<https://assets.ctfassets.net/kftzwdyauwt9/67qJD51Aur3eIc96iOfeOP/71551c3d223cd97e591aa89567306912/o1_system_card.pdf>). Everything from advertising to political polarization to phishing scams and human factor vectors in cyberattacks could be turbocharged by hyper-persuasive AIs. We are already seeing AI being used to attempt persuasion on social media by creating content, accounts, and [networks of influence](<https://www.theguardian.com/technology/article/2024/may/30/openai-disinformation-russia-israel-china-iran>).  

[](<https://substackcdn.com/image/fetch/$s_!bd7O!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b5a388-def4-4d60-a444-44aa15f37ecc_265x375.jpeg>)_Note_ : The nature and impact of persuasion is famously discussed by Plato and Aristotle. In the modern period it is popularized at the inter-personal level with Dale Carnegie’s _How to Win Friends and Influence People_ , a 1936 self-help book.

To mitigate against these risks we need to make sure that the evaluations for persuasiveness are effective, that controls are in place to mitigate its risk during deployment, not just in the lab, and that the incentives of model and application developers – not just the capabilities of the models themselves – are considered.

### **Evaluating Model Persuasiveness “Evals”**

**Persuasiveness was the only risk to receive a “medium” rating in the older model** [GPT 4o system card](<https://openai.com/index/gpt-4o-system-card/>) (all other risks that were considered were rated as “low”), and so persuasiveness was apparently dialed down until it was “low” risk.   
  
Now, in the latest “Strawberry” model [GPT o1](<https://openai.com/index/openai-o1-system-card/>) system card from September 12, **model persuasiveness risk reappears at “medium risk”** (along with [CBRN](<https://en.wikipedia.org/wiki/CBRN_defense>) risks). The difference is that now it stays there – and even gets dialed up a bit! It seems that making the model safer in other ways also resulted in the model becoming more persuasive. _The “post-mitigation” model that users see, i.e., the model with the safety training, scored higher on persuasiveness risk than the pre-mitigation model_(pg.24)! Meaning that the additional model “post-training” tuning made it worse on OpenAI’s persuasiveness evals.

[](<https://substackcdn.com/image/fetch/$s_!EGu0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d28a55b-18b5-4c9e-9af6-1c4ded394b9d_1438x910.png>)_Note_ : OpenAI o1 System Card, September 12th, 2024, pg. 24, showing that post-mitigation makes the model even worse on this persuasiveness evaluation (“eval”). This is true for other persuasiveness evals too.

Thanks for reading Asimov’s Addendum ! Subscribe for free to receive new posts and support our work.

Subscribe

  
According to OpenAI, the GPT o1-preview model scores “within the top ∼ 70–80% percentile of humans” for persuasiveness. But it doesn’t yet outperform top human writers. **But to put this rating in context, note that OpenAI didn’t even test whether humans could actually be persuaded**. One of the evals just asked human raters to choose whether a set of AI generated arguments was superior to the corresponding human-generated arguments taken from the [changemyview Reddit](<https://www.reddit.com/r/changemyview/>). Other tests of persuasiveness simply measured how well the latest model could persuade earlier models.

One wonders how effective such a methodology is in predicting persuasiveness with actual humans in real world contexts, especially given that **influence and persuasion are social phenomena** , linked to trust, relationships, and bandwagon effects (the habits of thought from those around us). For example, some researchers have posited that LLMs may be able to increase persuasiveness by “[linguistic feature alignment](<https://arxiv.org/pdf/2311.16466>)” – that is, by matching the speech patterns of those they are attempting to persuade. And using AI to create deepfakes fundamentally speaks to the social nature of persuasion, using AI to recreate the human voice or face in such a way as to increase trust in what is being put forth.

**To the extent that people come to trust machines, that may give them further credibility**. For example, some recent research discovered that [conversations with chatbots may actually talk people out of conspiracy theories more effectively](<https://www.science.org/doi/10.1126/science.adq1814>) than conversations with other people. It is certainly possible that machines may be seen as dispassionate, with no reason to lie, and thus the purveyors of “facts.” Our own past research hypothesized that once search engine rankings come to be trusted, it [becomes easier for companies to manipulate them for their own economic benefit.](<https://www.cambridge.org/core/journals/data-and-policy/article/algorithmic-attention-rents-a-theory-of-digital-platform-market-power/D85FE41F6CF99FC57DDFB2B2B63491C5>)

**In short, it is essential to analyze persuasion within social settings and as deployed in concert with other tools and technologies**. In the real world, commercial incentives and capabilities may make these models even more effective at persuasion. How likely is it that as advertising becomes increasingly AI powered, persuasiveness will no longer be considered a risk, or a bug, but a feature? It will most probably be dialed up to 11! AI models will have access to all sorts of highly personalized consumer data, [likely making them much more persuasive than they are in the lab](<https://actu.epfl.ch/news/ai-s-new-power-of-persuasion-it-can-change-your-mi/>). 

**Making persuasiveness risks worse** in [GPT o1](<https://openai.com/index/openai-o1-system-card/>)-preview are its growing capabilities in **deception**. Deception is a means of persuasion – and not a healthy one. 0.8% of o1-preview’s responses were flagged as “deceptive” by an LLM model checker, with almost half of these being on purpose. 

A real world risk from these capabilities is **extortion** : the large language model tricking others to make a payment. This is simulated in a “[MakeMePay](<https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay>)” evaluation by OpenAI, whereby o1-preview (post-mitigation) was able to extort money out of GPT-4o 11.6% of the time, showing just how powerful the model is (and even more powerful pre-mitigation). By comparison, GPT-4o only has success 1.1% of the time in extorting money out of another instance of itself. 

[](<https://substackcdn.com/image/fetch/$s_!3TIJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04b8cd63-7f57-4f2a-94ca-c046f8416bce_1502x912.png>) _Note_ : OpenAI o1 System Card, Sept 12, 2024, pg.26

From a risk perspective, persuasiveness matters because of how important it is going to **be for commercializing this technology** , helping AI companies recoup the enormous (fixed) R&D outlay costs and the ongoing high inference (marginal) costs. We are already seeing wide scale deployment of [AI-powered advertising](<https://www.facebook.com/business/ads/meta-advantage>) on existing platforms like Facebook. But we have very little visibility into the unique impacts of this deployment: are AI-generated ads more persuasive and if so why? Is it enhancing personalization to benefit users or instead manipulating users to their detriment? 

**Two other worrying model features make AI’s persuasiveness potentially more dangerous**. The system card (Appendix 8.3) seems to show that the model would sometimes pursue commercial objectives secretly (“alignment faking”), if this was its long-term objective. In addition, the model hid its uncertainty from the user, being overconfident, and failing “to communicate this uncertainty to the user.”

### And What About Controls? And Incentives?

We don’t understand the persuasive power of LLMs in the real world, and we ought to. Persuasiveness represents an amplifier of many of the other risks being considered in AI deployment. 

We also don’t understand the nature of the [controls](<https://en.wikipedia.org/wiki/Internal_control>) that will be in place to limit abuse of a model’s persuasive capabilities, the extent to which they will be followed by third parties, and what incentives and mechanisms there are to enforce them. **“Controls” are a key concept in financial auditing as well as many other business processes**. Controls encompass not only the policies for achieving a particular objective but also the methods for ensuring that they are being followed, that information provided is accurate, and that the organization is actually doing what it says it does and is managing the risks that it has identified. At least as currently practiced, assessment of controls appears to be largely lacking from AI auditing.

**There is a lot to learn from past mishaps in the social media era**. Consider the Cambridge Analytica scandal, in which a researcher used Facebook’s permissive access to user data to acquire not only data from users who opted in to the research, but from their friends, and friends of friends, eventually acquiring information about more than 50 million people. That data was later used to target users in the 2016 US election with political ads. When the data leak was discovered, Facebook’s policies were updated, and Cambridge Analytica was asked to delete the data. But there was no followup to ensure that this actually happened. This was a “bug” – or in auditing parlance, a failure of controls. 

But more importantly, as _Access Now_ asked in its 2018 reporting on the Cambridge Analytica situation, was Facebook’s failure in fact [a “bug” or a feature](<https://www.accessnow.org/its-not-a-bug-its-a-feature-how-cambridge-analytica-demonstrates-the-desperate-need-for-data-protection/#:~:text=for%20data%20protection-,It%27s%20not%20a%20bug%2C%20it%27s%20a%20feature:%20How%20Cambridge%20Analytica,desperate%20need%20for%20data%20protection&text=Reports%20from%20The%20New%20York,the%20age%20of%20data%20harvesting.>)? Given the vast data collection business infrastructure of most of the internet giants – and for that matter, of non-internet companies as well – **what incentive do the companies have to limit possible abuses? Or to disclose them**? The scandal highlighted that potentially harmful software features are less likely to be disclosed when they are highly profitable to the parent company. The US Supreme Court has agreed to take up a case that [will decide](<https://www.dandodiary.com/2024/06/articles/securities-litigation/supreme-court-agrees-to-take-up-facebook-user-data-disclosure-case/>) whether Facebook was negligent in disclosing the kind of abuse that Cambridge Analytica represents as only hypothetical, when in fact it had already happened. 

**At least for now, OpenAI’s inability to dial down o1-preview’s persuasiveness level is a bug**. _But it’s only a matter of time until GPT’s persuasiveness becomes a “feature”_ given how valuable it will be, not just for OpenAI, but for third-party businesses integrating AI into their products. When that commercial tipping point happens, we need testing and disclosures that will allow investors, regulators, and the public to distinguish what’s driving LLM behavior:_technological misalignment_ or _monetization-driven alignment_. And we need a system of auditing that interrogates not just model capabilities in the lab, but the system of controls that ensures that a model is operating as expected once it has been deployed, and that allows for problems to be caught and addressed.

Thanks for reading Asimov’s Addendum ! This post is public so feel free to share it.

[Share](<https://asimovaddendum.substack.com/p/model-persuasiveness-feature-or-bug?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

Subscribe
