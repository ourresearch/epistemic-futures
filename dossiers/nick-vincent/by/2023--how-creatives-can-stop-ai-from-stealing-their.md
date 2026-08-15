---
title: "How creatives can stop AI from stealing their work"
person: "nick-vincent"
section: "by"
type: "op-ed"
year: 2023
date: "2023-10-03"
venue: "Bulletin of the Atomic Scientists"
authors: "Nick Vincent"
source_url: "https://thebulletin.org/2023/10/how-creatives-can-stop-ai-from-stealing-their-work/"
retrieved: "2026-08-13"
content: "full-text"
---

# How creatives can stop AI from stealing their work

## Full text

As artificial intelligence and related areas of computing progress, researchers from a variety of communities have been forecasting and discussing the potential economic impacts of the technology. The buzz isn’t just limited to those studying the field. Earlier this month, we saw headlines like “AI took my job, literally,” while Margaret Atwood penned “Murdered by My Replica,” an Atlantic article in which the acclaimed novelist discusses how her written words were used to train AI.

It’s been less than a year since the release of ChatGPT. Over that time, large language and text-to image models and other variants of generative AI have continued to proliferate. Public discussion of AI’s impact on society, including worries regarding harmful externalities of AI systems, is continuing in earnest. In recent months, a new concern has garnered attention: Powerful generative AI models were trained using massive amount of contents covering a wide array of domains—from journalistic texts to niche blogs. The creators of content used in these trainings received neither compensation nor a choice with regards to this data use.

Put simply, the unanticipated development of AI capabilities has led to a situation in which writers, artists, coders, and other creators who put their content onto the Internet don’t have a meaningful ability to consent to training generative AI models. This dynamic is, to some extent, an unavoidable aspect of innovation in computing and information technologies. When humanity discovers new ways to process, link, mix, and augment data and records, it’s not possible to achieve a public mandate, formal indication of consent, or even a broad consensus until that advancement has been publicly circulated and digested. Concerns along these lines have been spreading for more than a decade in regards to genetic testing firms and their data collection, but the same argument applies to large language models that use blog posts and code repositories, or a text-to-image systems that scrape personal art or a photograph of someone’s face. When properly aggregated, filtered, and processed, our collective set of documents really is quite valuable (and new data valuation techniques may shed light on exactly which kinds of data are most impactful).

In the long term, there will need to be a societal rethinking of norms and laws for sharing content and data. In the meantime, however, there are avenues for creators to exert agency over how their contributions flow to AI systems. Given that the process of setting new standards will be slow, exploring these avenues in the short term is critical because it can provide an immediate source of bargaining power for creators (and feedback for AI developers), as well as shape the development of new norms. If organizations regularly manipulate how their data contributions flow to AI systems, this could increase the chance that in the long-term AI governance is characterized by democratic and responsive processes.

Furthermore, it could be the case that exerting agency over data flow could be just on the cusp of giving creators serious leverage (but they can’t quite get enough participation, or certain tools or legal avenues are just out of reach). In these scenarios, policy initiatives that lower the barrier for people to act with their data could have an outsized effect and enable impactful collective action.

Ultimately, the use of “data leverage”—bargaining power stemming from data—can lead to a symbiotic paradigm of AI in which creators and AI operators balance their respective incentives and concerns, rather than a myopic and consumptive approach in which AI systems unintentionally burn out the online ecosystems that create the very data points that are used to fit models in the pursuit of useful outputs. Systems like large language models are useful because they promise to combine the best aspects of online encyclopedias, help forums, scientific papers, and blog posts. If there’s nowhere for people to actually produce original content, nobody wins.

To this end, there are actions available to creators that are likely to impact the likelihood they can wield “data leverage.” Creators will have to contend with some considerations that are specific to the new generative AI paradigm, including the incredibly fast-paced nature of the field and the use of web-scale datasets.

RELATED:

AGI’s ETA: Delayed (again) due to technical difficulties

Data strikes: Lawsuits, robots.txt, and consumer-facing tools. Some organizations, such as The New York Times, have taken actions that involve withholding or retracting data, what could be called a “data strike.” The basic logic of a data strike is that the most fundamental resource in any AI system’s pipeline is training data. If an organization takes action to reduce data availability—via legal action or technical means, such as blocking AI bots from accessing the data–it can reduce the capabilities of downstream AI systems.

The impact of data strikes can be better understood by looking at data scaling, or how AI capabilities increase with more data availability. In short, across a variety of domains one can observe a characteristic diminishing returns curve explained by a power law function. This means a small drop in data might cause imperceptible performance changes, but as the size of a data strike scales up, the impact increases in an accelerating fashion.

These trends of data scaling mean that data strikes require large-scale (or highly targeted) action. This will likely become a key factor in determining which data strikes are successful, and as more organizations test the waters, we may gain a more precise empirical understanding of the contexts in which data strikes are both efficacious (or have a large effect on AI capabilities) and feasible.

Data poisoning: Adversarial attacks as protest. Legal avenues can, at times, seem unpromising. This can be because in some creative domains, there may not exist professional organizations or firms to bear the brunt of the associated costs. It could also be that some cannot avoid sharing their work online due to a loss of business. In such cases, it may be possible to continue sharing data, but with some degree of poisoning or perturbation. More whimsically, this could be described as adding a little extra hot sauce to a lunch that some mysterious coworker keeps stealing from the shared fridge.

There’s a long line of academic work that seeks to understand just how impactful a small batch of poisoned data can be. Given certain assumptions about the modeling process, it’s often possible to create large effects. In the context of image generation, the Glaze project has received significant attention from online communities of artists. Glaze attempts to balance visual artifacts that are perceptible to humans with imperceptible changes to the image that make it harder for generative models to replicate an artist’s style. One challenge with this type of approach is that artists must make a judgment call about the intensity of their poisoning efforts: More effective perturbations are also more visible.

Other research suggests that in the long run, poisoning may lose effectiveness, but it can still be powerful in the short term. Furthermore, it might be possible to argue that the processing of an image (or other piece of content) to “undo” poisoning represents an attempt by the AI operator to actively defeat a protective measure, changing the legality of using that data. This remains untested so far but if this angle pans out, using even simple data poisoning and processing techniques could prove very powerful.

Finally, it’s important to consider that even if a particular data-poisoning attack is “defeated” in the long run—because models are robust against the poisoned data, AI developers can identify and avoid poisoned data, or AI developers can undo perturbations—the act of data poisoning can still serve as a means of protest.

Data contribution to a competitor. In some cases, there really may not be much that a particular group can do in terms of withholding or poisoning data. Perhaps a group wants to data strike but lacks the resources to solicit participation that hits some critical threshold. For instance, if a single newspaper wanted to go on a data strike but could not get other newspapers to join, they might be unable to effectively impact a model like ChatGPT’s “produce journalistic content” capabilities.

RELATED:

The Trump administration won’t face the facts

In any of these cases, a third option might involve giving data to a competing organization. This idea exploits a fundamental aspect of the learning process at the heart of AI. In cases in which data strikes are ineffective, we can expect adding data to be especially impactful. There’s a sort of “strike-contribution” tradeoff: A task that can be solved with data efficient techniques is robust against data strikes, but standing up to a competitor is easy. A task that really needs every last drop of data is naturally not robust against data strikes or poisoning.

How generative AI changes the game for data leverage. Because generative AI systems and products are updated on a near-weekly basis, creators who wish to push back are faced with continual questions. However, there’s been progress in work that specifically understands generative AI systems in terms of questions about data counterfactuals. How, for example, might an AI system change if it loses access to some content? As long as researchers have some idea about how to answer these kinds of questions, it will be possible to make more informed data-sharing decisions.

And of course, there’s nothing stopping a frustrated organization from just trying out a data strike to see how it goes. These “data strikes in the wild” could, in fact, contribute to a more complete scientific picture of generative AI capabilities. In the long run, it’ll be important to understand how ChatGPT performs without Wikipedia, and perhaps even how an AI art system performs without certain famous artists. Ultimately, trying out more configurations of training data will better inform creators and researchers about the strengths and weaknesses of different modeling approaches.

Translating our knowledge about pre-generative AI systems to the new paradigm will be an important challenge to tackle. Early work looking at data-focused actions to give a group bargaining power focused on smaller “academic-scale” tasks like movie recommendation, toxic text classification, and image classification. Findings in these domains do likely generalize—even though machine learning research sometimes uses “toy” tasks or otherwise unrealistic tasks, the core improvements we’ve seen produced by the machine learning community have clearly led to progress in products that are deployed across many contexts.

We have some intuition that more data in a given domain should increase performance in that domain. But web-scale data makes the boundaries of these domains murky. Just how helpful is a dataset of Python code when it comes to outputting other coding languages with similar use cases, like R or Julia? Empirical investigation will continue to unveil these boundaries.

It’s important to note that generative AI systems now involve careful filtering and data selection procedures. These choices have major implications for the viability of data leverage campaigns as well, so initiatives that document and share these choices could help give creators more power and avoid futile campaigns.

For now, there are a variety of actions available to individuals (but ideally performed as a group) that act on data. Creators can withhold new data contributions, use institutional processes to attempt to retract already created records, poison content, and tactically send data to organizations they want to support. None of these individual actions are new, and researchers can make some educated guesses about the impacts they might have. However, by carrying out a combined program of scholarly inquiry into data-related collective actions and simultaneously supporting policy and tools that enable such data leverage campaigns, those against the liberal scraping of their data can greatly amplify the “data pipeworks” as another theater for the battle over AI’s future. I believe that the potential to create responsive, democratic feedback loops makes this avenue especially fruitful for creating positive-sum AI systems that navigate tough conflicting incentives between data creators and data consumers to build highly capable, yet prosocial AI systems.

####
