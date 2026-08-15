---
title: "Markets, Bureaucracy, Democracy, ... AI?"
person: henry-farrell
section: by
type: blog-post
year: 2025
date: 2025-06-30
venue: "Programmable Mutter (Substack)"
authors: "Henry Farrell"
source_url: https://www.programmablemutter.com/p/markets-bureaucracy-democracy-ai
retrieved: 2026-08-13
content: full-text
notes: "Substack post id 166440655; free to all readers (audience: everyone). Retrieved via the Substack API (api/v1/posts/by-id). Images/captions and comments removed."
---

# Markets, Bureaucracy, Democracy, ... AI?

*What large models share with the systems that make society run*

## Full text

One of the great intellectual treasures of the world is the Annual Reviews system. They run journals across a variety of sciences and social sciences, publishing articles which aren’t aimed at laying out new research findings, but synthesizing what is happening in particular areas of research and making arguments as to where they ought be going. I’m particularly fond of the Annual Review of Political Science, not simply because I am on their editorial board, but because they make most of their content publicly available for free. 

And now, the 2026 volume which has just been published, includes an article by me on “AI as Governance.” It’s available under a Creative Commons License - to make it easier for people to reuse/remix, I’m providing rough-and-ready Pandoc-ed versions of the text in Word, Markdown and .tex. If you just want to read it, either keep on scrolling, or go here and click PDF in the top right corner to get a prettier version.

If you’ve been following this newsletter over the last couple of years, plenty will be familiar to you. In particular, the second half of the article is a more political science specific version of Applied Gopnikism, as developed in this Science article with Alison Gopnik, Cosma Shalizi and James Evans, as well as elsewhere. But there are some useful additions to the organizing framework, including perhaps the table at the top of this post, which is deliberately spicy, for ‘somewhat recondite and academic’ values of spicy. 

There’ll be more to say about this soon - but it is usually more useful to develop ideas and frameworks in conversation than as Grand Statements. In particular, there is a very useful debate to be had with Leif Weatherby’s fascinating new book, Language Machines. But that book deserves its own separate post first. So, here, in temporary lieu, is AI as Governance.

Subscribe now

 AI as Governance

This work is licensed under a Creative Commons Attribution 4.0 International License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. See credit lines of images or other third-party material in this article for license information.

ABSTRACT

Political scientists have had remarkably little to say about artificial intelligence (AI), perhaps because they are dissuaded by its technical complexity and by current debates about whether AI might emulate, outstrip, or replace individual human intelligence. They ought to consider AI in terms of its relationship with governance. Existing large-scale systems of governance such as markets, bureaucracy, and democracy make complex human relations tractable, albeit with some loss of information. AI's major political consequences can be considered under two headings. First, we may treat AI as a technology of governance, asking how AI's capacities to classify information at scale affect markets, bureaucracy, and democracy. Second, we might treat AI as an emerging form of governance in its own right, with its own particular mechanisms of representation and coordination. These two perspectives reveal new questions for political scientists, encouraging them to reconsider the boundaries of their discipline.

INTRODUCTION

Political scientists are belatedly catching up with public debates about artificial intelligence (AI). Machine learning (Grimmer et al. 2021, Morucci & Spirling 2024), empowered by new techniques (neural networks) and more powerful computing equipment, is remaking the digital economy, with possible consequences for society and politics. Generative AI such as large language models (LLMs) and diffusion models has generated enormous excitement—and worry—because its outputs can approximate human generated content such as text, images, and increasingly video.

While some political scientists research AI's secondary political consequences, few engage with its specific workings, which seem the proper domain of computer scientists. The term AI suggests that these technologies should be compared with individual human intelligences, which some expect AI to emulate or outcompete, rather than with collective political or social phenomena.

Social scientists have more to contribute than they think (Oduro & Kneese 2024). Burgeoning debates on the politics of algorithms and data (Burrell & Fourcade 2021, Johns 2021, Matias 2023) that investigate how LLMs may be a “cultural technology” (Yiu et al. 2024) that summarizes, organizes, and remixes human-produced knowledge are already underway. Political scientists can usefully think of AI in terms of its relationship to governance arrangements, the various large-scale collective means through which humans process information and make decisions, such as markets, bureaucracy, and democracy. Governance arrangements do not think (Arkoudas 2023, Mitchell 2023, Nezhurina et al. 2024), but they usefully reorganize human knowledge and activity. So too does AI (Yiu et al. 2024).

In addition to asking how AI ought to be governed (Stanger et al. 2024), we can think of AI as a technology of governance. AI provides new means for implementing the basic tasks (such as classification or categorization) that markets, bureaucracy, and democracy rely on. Some kinds of AI, such as LLMs, may become sufficiently distinctive and important to be a form of governance in their own right, an independent collective means of information processing and coordination, equivalent to markets, bureaucracy, and democracy, rather than a mere technological adjunct.

In practice, AI blurs into market behavior, bureaucratic routine, and (perhaps in the future) democratic representation, just as, for instance, markets shade into intrafirm bureaucracy. But thinking of AI as either a technology or a form of governance helps social scientists understand how to study AI and address questions that are currently obscured by excited rhetoric about imminent superhuman intelligence.

Studying governance and AI would require political scientists to develop some technical understanding of AI and to think more clearly about the relationship between politics and technology. Half a century ago, Simon [2019 (1968)] suggested we consider the social sciences and AI as manifestations of the “sciences of the artificial.” We should take this suggestion seriously. Just as the major social sciences were responses to the shock wave of the Industrial Revolution (Tilly 1984), we should work across academic disciplines, perhaps even building new ones, to respond to the lesser but possibly impressive changes that are now happening around us.

WHAT AI AND GOVERNANCE MEAN

AI and governance are contested terms. John McCarthy coined the term “artificial intelligence” to distinguish it from cybernetics (Mitchell 2019), which considered feedback and information flows across a wide variety of systems (Davies 2024). However, the meaning of AI has changed. For decades, AI was dominated by symbolic approaches, which emphasized formally derived logic and rules. Now, the rival connectionist approach, which combines machine learning with neural nets (statistical processing engines that notionally resemble networks of biological neurons), is in ascendance (Mitchell 2019). Not all soi-disant AI involves these techniques, nor is AI the best descriptor for them, but it is the term that has taken hold.

Connectionist AI parses data to discover useful approximate representations for relationships that may be obscure, complex, and nonlinear. Neural networks are multilayered models that create, alter, and transmit weighted guesses about various aspects of the data onward via “hidden layers” of “neurons.” The final output is reweighted via gradient descent (alternatively, backpropagation) so that it better converges on some broad optimum.

These models can classify and predict. In supervised learning, AI is trained on labeled data, canonically on images that have been labeled as containing cats or dogs. As the data from the images pass through the layers of the neural network, the model can identify increasingly complex features (e.g., patterns associated with a particular shape of ear) that are more likely to be found in pictures labeled “cat” than “dog.” It may also pick up on nonsalient information—for example, if cats are more likely to be photographed in indoor settings, and dogs in outdoor settings, it may mistakenly guess that dogs photographed indoors are cats. In unsupervised learning models such as LLMs (Radford et al. 2019), the AI is tasked to predict or classify from unlabeled patterns in the data.

Some AI applications (e.g., modeling of protein folding) are remote from political science. Others might directly reshape the economy, society, and politics. AI systems are scalable, although they can be computationally expensive to train and implement, and the processes through which they arrive at specific outcomes may be opaque. It is often impractical to determine how a neural network processes initial data to arrive at its final classification decision, and the techniques used to improve gradient descent are based on the trial and error of “alchemy” (Rahimi & Recht 2017) rather than deep understanding.

LLMs like GPT-4.5 are produced by transformers, a neural network architecture that encodes the relationships between vectorized words and word parts (tokens) in enormous corpora of text that have been mined from the Internet, digitized books, and other readily available content. The transformer produces a set of weighted vectors that capture its mapping of the relationships among word tokens in the corpus (whether words regularly or rarely occur close together). This set of vectors is the LLM, which, after further processing (technical fine-tuning and reinforcement learning through human feedback or, increasingly, synthetic data), can predict the text or content that ought to follow a given prompt.

Political scientists might engage AI by investigating its relationship to governance. How does AI affect existing forms of governance, such as markets, bureaucratic hierarchy, and democracy? Is AI itself a kind of governance?

However, governance too is a vexed term (Mayntz 2009). As Peters (2012, p. 19) tartly remarks, “the ambiguity of the concept…has been one of the reasons for its popularity.…It…obfuscates meaning at the same time that it perhaps enhances understanding.” Peters, however, notes that despite its variety of meanings, the word governance originally referred to steering a boat, like cybernetics (derived from the Attic Greek word for “steersmanship”). Governance, along with cybernetics and control (Beniger 1986, Wiener 2019, Yates 1993), is a catchall phrase for forms of social, political, and economic coordination that especially emphasize information processing.

Stealing from broadly analogous ideas presented by Simon [2019 (1968)], I treat governance as an umbrella term for the large-scale systems for processing information and social coordination that allow complex societies to work. A system of governance, then, has (a) an input, some large-scale source of complex information; (b) a technology for turning that information into useful, albeit lossy representations that can more readily be manipulated; and (c) outputs that can be used to coordinate on the basis of those representations.

In markets, the price mechanism summarizes tacit knowledge (Polanyi 1966) about relations of production, allowing widespread economic coordination (Hayek 1945, Lindblom 2002). In bureaucratic hierarchy, authority relations and classification systems turn diffuse social knowledge into tractable information that can enable government rulemaking (Scott 1998, Weber 1968). In democracy, mechanisms for representation and voice turn the desires and knowledge of citizens into tractable representations that enable feedback and control over their collective circumstances (Allen 2023, Dewey 1927).

These systems of governance are at best highly imperfect. The price mechanism, bureaucratic categories, and representations of the democratic public are “simulations” [Simon 2019 (1968)] or very lossy coarse-grainings (Flack 2017) of irreducibly complex underlying realities. But even harsh critics (Scott 1998) acknowledge that modern large-scale societies would be impossible without them.

They are deeply entangled with one another. Markets depend both on the external institutions of government (North 1990) and on the internal bureaucratic hierarchy of the firm (Coase 1937). Bureaucracies draw on markets and have regularly sought to import their logic (Dunleavy & Hood 1994). Democracy depends on bureaucratic hierarchy to implement decisions and, as Lindblom (2002) observes, seems practically conjoined to the market economy.

The value of this approach to governance is not that it provides precise definitions, let alone testable hypotheses, but rather broad heuristics. We can see how AI may not be a putative substitute for individual human intelligence but instead a means of collective information processing and coordination. Specifically, we can consider AI either (a) as an external technology, affecting how existing systems of governance coordinate and process information, or (b) as a possible form of governance in its own right, with its own particular form of coordination and information processing. How does AI affect the internal workings of existing forms of governance? Might it become its own form of governance, with associated pitfalls and possibilities (Farrell & Shalizi 2023)? These two broad questions motivate different but partially overlapping research agendas.

AI AS A TECHNOLOGY OF GOVERNANCE

How has AI affected existing forms of governance such as markets, bureaucracy, and democracy? Political scientists might learn from scholars of science and technology studies (Beniger 1986, Yates 1993), communications (Noble 2018), sociology (Fourcade & Johns 2020), and history (Cronon 1991), who have examined the succession of technologies affecting the workings of bureaucracies, markets, and perhaps democracy.

Markets, bureaucracy, and democracy all involve classification, and AI provides systems for classifying at scale. Bowker & Star (2000, p. 11) define a classification system as a “set of boxes (metaphorical or literal) into which things can be put to then do some kind of work—bureaucratic or knowledge production.” Not only bureaucracies but also markets and democracies rely on classification systems, for example, to enable impersonal trade (Cronon 1991) and to make tangible the needs and wishes of democratic publics (Perrin & McFarland 2011). Now, AI can assign persons, things, and situations to boxes, automatically and at scale. YouTube, for example, may use AI to classify billions of particular users, guessing which video to serve up next to each. Depending on the user's response, the algorithm might update its guess as to how the user ought be classified, without human intervention.

So what happens as older classification systems (ranging from technologies as prosaic as the filing cabinet to vast collective undertakings such as censuses) are modified or replaced by AI (Farrell & Fourcade 2023)? The immediate consequences are most visible in online platforms such as YouTube and Facebook. AI generates quite finely grained categories; for instance, the YouTube recommendation system described above has deployed high-dimensional embeddings (representations of relationships) of videos and users to generate and rank a list of candidate videos to serve up next (Covington et al. 2016). Such categorizations may change rapidly and without notice: No one without internal access to the technology sees them directly.

These techniques are applied at scale by platform companies but only haphazardly elsewhere. AI uptake has reportedly been quite slow. McElheran et al. (2024) find that only 6% of US firms, accounting for approximately 18% of total employment, report using AI (although most very large businesses do use it). In the United States, many federal agencies have experimented with “artificially intelligent regulation” (Engstrom et al. 2020), but change has advanced by inches (Cuéllar & Huq 2022). What research there is on government uptake in China, India, Europe, and elsewhere suggests a similar picture: much interest, but lagging deployment. While discussions of AI-enhanced democracy abound (Allen & Weyl 2024, Gilman & Cerveny 2023, Landemore 2021, Sanders et al. 2024), there are no real implementations at scale.

It is possible that AI may not have the large-scale economic, organizational, and political consequences that many expect. Its benefits might be limited or outweighed by other desiderata, it may turn out to have irredeemable flaws, or it may provoke insuperable political opposition. However, new social technologies only very rarely have an immediate and dramatic impact, especially when their use requires large-scale organizational change.

It is wise at least to consider the possibility that AI may also have large-scale consequences, even if it takes years or decades to see them. If, as Cuéllar & Huq (2022, p. 335) suggest, a new “era” of artificially intelligent regulation (and markets and politics) is at hand, we should start considering the implications. This must necessarily be speculative, extrapolating from what we can see (e.g., platform implementation) and reasonable inferences about future developments.

From one perspective, the platform economy seems to demonstrate how AI can supercharge market coordination. Platforms such as Facebook and YouTube deploy other algorithms than AI and were established before connectionist AI came into its own, but they increasingly rely on AI to automate feedback loops in which users, content, or situations are categorized and acted on, and the consequences are then measured and fed back into the system (Fourcade & Healy 2024). Platforms have bet that much of the expensive internal bureaucratic hierarchy of the firm can be replaced by objective functions that direct AI technologies to maximize or minimize on some set of vectors (Reich et al. 2021). That helps platform companies with tens of thousands of employees manage interactions among hundreds of millions or billions of users. More sensitive decisions are still made by humans, while poorly paid contractors back up algorithmic moderation and are obliged to engage daily with some of the most toxic aspects of human collective behavior (Gonzalez & Matias 2024).

AI can underpin two-sided attention markets, in which platforms publish consumer-created content while advertisers compete for consumers’ eyeballs. It also facilitates the workings of vast traditional markets, such as Amazon, eBay, and Temu, with little human oversight. We know more about the former than the latter, in part because of data availability problems [which are provoking both organization among scholars (Coalit. Indep. Technol. Res. 2024) and political responses (Eur. Comm. 2024)].

Economists and many computer scientists have focused on the efficiency of AI algorithms. More pessimistic sociologists, communications scholars, and other computer scientists have asked how they affect accountability and power relations within public and private bureaucracies, often emphasizing AI's sloppiness, bias, and imperviousness to outside correction.

Slop—prediction and categorization errors—is inevitable. AI algorithms are imperfect means for fitting curves to the complex processes they look to summarize. The owners of platform companies often care most about exploiting economies of scale and are relatively insensitive to local mistakes. Amazon uses AI to hire and fire its fleet of self-employed drivers, on the basis of classification decisions that may appear arbitrary to humans. As one of the engineers who designed the system explained in vulgar terms to Bloomberg (Soper 2021), “Executives knew this was gonna shit the bed. That's actually how they put it in meetings. The only question was how much poo we wanted there to be.” More generally, engineers often view themselves as part of a “we” designing and implementing the systems rather than the “they” whom these systems are deployed to categorize, manage, and predict (Eliassi-Rad 2024).

AI can also reflect or accentuate bias. AI learning may pick up on gender, racial, or other biases in the data that it has been trained on. In one widely discussed case (Dastin 2018), Amazon reportedly trained a system on the resumes of successful job applicants to sort through new applications. The learning system penalized resumes that included the word “women's” as in “women's chess club captain,” turning past informal biases into direct criteria of selection. Such bias can potentially be self-reinforcing, including in highly sensitive government functions. Benjamin (2019) argues that algorithmic policing decisions may turn bias into feedback, such as identifying areas with high arrest counts (likely because of racial bias) for increased police intervention, which may again increase arrest counts in a perverse feedback loop. While some criminologists (e.g., Berk 2021) claim that these concerns are overstated, they acknowledge legitimate concerns about fairness and accuracy.

There may be more subtle forms of bias. Categories that are underrepresented in the training data will be poorly captured by the model. Furthermore, there are fundamental trade-offs between different kinds of bias (Chouldechova 2017, Kleinberg et al. 2018) that are impossible to resolve fully. These and related problems are discussed in a wide-ranging literature that has sharp political implications but so far has been developed largely by computer scientists and philosophers, rather than by political scientists and political theorists.

The widespread adoption of AI by platform companies, and the prospect of its broader use, is giving rise to vigorous debates over how best to correct bias and mistakes, especially as governments take it up. Some social scientists are pessimistic: Fourcade & Gordon (2020) suggest that the “dataist state” is whittling away the discretion of bureaucrats and creating algorithmic black boxes. Others are cautiously optimistic, arguing that algorithms may sometimes be more accountable than bureaucrats (Kleinberg et al. 2018) or that, with appropriate safeguards, AI can provide greater efficiency with acceptable downsides.

Optimists often focus on the objective functions that AI and other algorithms maximize or minimize on: These describe goals and trade-offs more transparently than, say, traditional bureaucratic guidelines. Pessimists point to the difficulty of retracing and understanding how AI learning algorithms make particular decisions. It is often impracticable to track the factors feeding into a specific decision that passes through multiple hidden layers in a neural network, and in any case these factors might not translate easily into traditional human notions of accountability and bureaucratic ethics.

Such perplexities suggest that some popular and semipopular commentary about all-powerful “surveillance capitalism” (Zuboff 2019) and its convergence with authoritarianism (Harari 2018) is overblown. Both boosters and critics tend to overstate AI's efficacy (Healy 2016). E. Yang (unpublished manuscript) finds that China's AI surveillance techniques are poorly suited to predicting political trouble for the regime without data from other sources. What it wants to know is precisely what it cannot readily observe, because citizens self-censor, skewing the training data. AI may help authoritarians sieve through vast quantities of data; it may also reinforce their internal political biases and make them less capable of seeing what is relevant to their survival. There is much less research on these topics than their importance warrants.

More generally, there is remarkably little research that systematically compares traditional bureaucratic decision-making and recourse to AI algorithms. Traditional bureaucracies are essential underpinnings of complex societies but are sometimes monstrous in the ways described by Kafka (Jarrell 1941), enabling the Nazi mass murder of Jews, Roma, Sinti, and other populations in Europe and helping to precipitate the great famine in China, as well as other large-scale crimes and catastrophes (Scott 1998).

Part of the problem is translational: While political scientists think and write extensively about bureaucracy and its consequences, they employ different informational frameworks than do computer scientists. Renewed inquiry into bureaucracy as a system of information processing would help build bridges (D. Berliner, unpublished manuscript). Nonetheless, there is a smattering of relevant research. Alkhatib & Bernstein (2019, p. 2) observe that algorithms, including AI algorithms, may be less well-suited than street-level bureaucrats to reshape categories on the fly, noting that when algorithms “encounter a novel or marginal case, they execute their pre-trained classification boundary, potentially with erroneously high confidence” (see also Kaminski & Urban 2021). Far more research along these lines is needed.

The political questions surrounding feedback go beyond bureaucracy. Some scholars suggest that AI feedback loops might enhance democracy, allowing better measurement of opinions, enhancing feedback from people who are less capable of articulating and defending their interests in technocratic terms, or providing citizens with feedback that interrogates their views and guides them toward a common understanding of the good. Others fear that AI might undermine existing forms of democratic coordination and knowledge creation. They suggest that AI might potentially worsen polarization by facilitating social media feedback loops that optimize on engagement (feed people provocative political content that keeps them watching but radicalizes them) or flood political debate with so much nonsense that ordinary discussion becomes impossible, worsening previous concerns about social media (Pomerantsev 2014, Roberts 2018). These very different prognoses have provoked lively discussions over whether the consumption of disinformation or misinformation (both vexed terms) and increased polarization are driven more by technology or by preexisting demand from some citizens (Budak et al. 2024, Munger 2024).

While political scientists have participated in these debates, they have often shoehorned AI into existing controversies rather than considering whether it might generate new ones. Claims that AI can be used to rebuild democracy on better foundations have typically welded together epistemic accounts of democracy (Schwartzberg 2015) with an engineer's enthusiasm for optimization. Such approaches tend to skimp on discussion of the trade-offs between the different kinds of information that citizens might contribute and the actual needs of the policy process (D. Berliner, unpublished manuscript). They also overvalue the knowledge-generating aspects of democracy and understate the political struggle between different approaches to politics and life (Schwartzberg 2015). Much of the emerging literature prefers to discount the contentious aspects of democratic politics, suggesting that they might be moderated or circumvented through the combination of machine learning with citizen deliberation.

There is enormous scope for more research and thinking about how AI intersects with political contention, what its consequences for organized groups and parties might be, and how it might affect the political distribution of power. Do these algorithms lower diversity among organizations (Caplan & boyd 2018), or do they reshape collective understandings of what constitutes the democratic public? Might they even constitute new kinds of citizens (Fourcade & Healy 2024), reordering their relationship with politics to emphasize “ordinal” ranking (Nguyen 2021) and individualized competition? These questions are both sorely underresearched by political scientists and urgently relevant to their interests.

Similarly, while political scientists have exuberantly debated the possibly negative consequences of social media algorithms, they have paid little attention to how platforms are organized and moderated (Steinsson 2024). This has left the field open to scholars of information, communication, and science and technology, who have debated the politics of moderation (Gillespie 2018, Matias 2019a), networked publics (Bak-Coleman et al. 2021, boyd 2010, York & Zuckerman 2019, Zuckerman 2014), power (Lazar 2024), and online harassment (Matias 2019b). These scholars disagree on many important questions, but they concur that platform companies’ management of the interaction of hundreds of millions or billions of users is not merely technical but inherently political. Platform companies have sought to evade these politics (Gillespie 2018) by appealing, with greater or lesser cynicism, to rhetoric about free speech and the marketplace of information; by suggesting, implausibly, that large-scale solutions will emerge organically from users themselves; by attenuating political disagreement; or by turning to outside sources of legitimacy to deal with thorny political issues. None has worked well. We urgently need to pay much more attention to how business has deployed AI to organize these spaces and how users have responded, especially as platform owners like Elon Musk (X) and Mark Zuckerberg (Meta) have become more visibly willing to take sides in politics.

More broadly, political scientists need to think more deeply about how technologies of governance affect democratic coordination and information processing. Democratic politics, too, depends on technologies of classification, even if political scientists rarely explore them (see, however, Prior 2007). As political sociologists (Perrin & McFarland 2011) have pointed out, the loose notion of a democratic public is rendered concrete by social technologies such as opinion surveys, which politicians and others turn to for a general sense of what the “public” believes, and which particular categories citizens fall into. Such surveys may actively shape and constitute democratic publics, creating self-fulfilling prophecies (Rothschild & Malhotra 2014). So too may other technologies, including voting systems. So what kinds of democratic individuals, collectivities, and publics may AI give rise to? How might AI reshape our understanding of the public in the future? If there is any organized debate on this topic, it is not among political scientists.

Understanding how AI can act as a technology of governance, affecting how markets, bureaucracy, and democracies coordinate action, will generate multiple important research agendas. It should also make political scientists pay proper attention to the blind spots in their own collective understanding of politics. We do not, as a discipline, regularly think hard about how technology affects the deep structures of the political economy, government in democratic and autocratic regimes, and democratic representation and feedback. That has to change.

AI AS A FORM OF GOVERNANCE

Treating AI as a technology of governance is already a challenge for political science. Still, one might go further. Could AI become its own novel and distinctive form of information processing and social coordination, rather than a secondary technology that affects existing modes? In other words: Does it make sense to treat some AI as an emerging form of governance in its own right? Doing so would build out an agenda on the basis of shared ideas laid out by Farrell et al. (2025).

Large models—LLMs and related forms of generative AI—do have implications that seem to go beyond their immediate consequences for markets, bureaucracy, and democracy. Specifically, they make certain kinds of cultural activity more tractable than they have previously been, affecting the possibilities of cultural coordination around shared beliefs as well as opening up new possibilities to magnify or counter biases and for discovery or reproduction.

There is a possible rationale for considering large models as a new form of governance. As Simon [2019 (1968)] argues, human beings (a) have limited individual information processing capacity and (b) live in a world that is enormously complex. Therefore, humans rely on various external technologies to coordinate information processing and to reduce complexity into manageable simplifications.

From this perspective, markets, bureaucracy, and democracy all generate lossy but useful representations that make impossibly complex underlying social realities more tractable. Prices summarize the tacit knowledge embodied in economic relations of production, helping to enable market coordination; bureaucratic categories summarize diffuse social knowledge, enabling government coordination; and democratic representations of the public summarize people's political beliefs and wants, allowing for political coordination. All indifferently represent the underlying complex realities that they purport to comprehend, but all are essential to managing the complexities of modern society. We can only make choices about our collective fate through the imperfect representations that make it visible.

As discussed below, large models too provide lossy but usable summarizations of much larger bodies of knowledge, rendering impossibly complex underlying wholes more tractable. They create useful but imperfect representations of broad categories of cultural knowledge (Yiu et al. 2024), mined from the Internet and elsewhere. Large models are and generate representations of written culture and images, summarizing enormous corpora of information that are scraped from the Internet, digitized sources, and elsewhere.

As with, for example, prices and bureaucratic categories, such representations are manipulable (Farrell et al. 2025), in ways that the wholes that they represent are not. Specifically, these models can be queried to reveal relationships that are not immediately visible; to combine different aspects of the culture they represent in seemingly creative ways; and to expand, reduce, and transform discrete cultural outputs.

These formal operations are not magical: They are (in their current form) practical applications of statistical predictive techniques to vectorized bodies of text. In a canonical example from an ancestor of LLMs, word2vec, subtracting the vector for “man” from the vector for “king” and adding the vector for “woman” arrives roughly at the vector for “queen.” When an LLM is asked, say, to rewrite the plot of Hamlet in the style of a chemistry textbook, it is using similar, though more complex operations on vectorized summaries to interpolate the plot and the style and provide a probable answer as to what the combination might look like. The technology has flaws. LLMs’ tendency to “hallucinate”—to generate plausible seeming but incorrect summaries—is part of how they operate. More generally, as Yiu et al. (2024, p. 875) argue, LLMs are incapable of distinguishing between “veridical and nonveridical representations in the first place,” because they have no direct interaction with, or direct capacity to learn from, the material world. What they actually do is model human-generated cultural content in tractable and manipulable ways.

This is still quite extraordinary. We now have technologies that can do for written and visual culture something like what prices do for economic information and bureaucratic categories do for social information. Large models generate representations of a vast and ungraspable whole that do not fully capture that whole but are manipulable and reproducible at scale. As of early 2025, businesses and related enterprises like OpenAI are betting hundreds of billions of dollars on the proposition that this will become a true general-use technology, reshaping the ways in which human beings access written, visual, and audiovisual culture, remix it, and create it. If this risky bet pays off, large models will become a crucial intermediary technology for the reproduction of human culture, shaping shared beliefs, reinforcing or mitigating biases, affecting processes of discovery, and remaking underlying political economic relations. This would justify considering large models as an alternative form of governance that can in principle be compared with markets, bureaucracy, and democracy ( Table 1 ).

Table 1 

Stylized forms of governance, including large models

As with the creation of impersonal markets (Cronon 1991) and the bureaucratic state (Yates 1993), the likely consequence would be political, social, and economic disruption. New forms of information processing will emerge in the space of culture, and old problems will reappear in new forms.

Earlier automated systems for generating cultural content have been quite limited. Conversational engines (Weizenbaum 1966) and algorithmic (Eno 1976), combinatorial (Queneau 1961), and aleatory (Calvino 2012) tools for generating culture have typically been spurs to human creativity and expression rather than substitutes. Now, we have predictive algorithms that require only minimal human input to generate fluent-seeming and detailed responses, which are often difficult for humans to distinguish from the responses of human beings. Our cognitive architectures predispose us to see certain patterns of activity as the product of conscious, volitional agents, leading us, for example, to mistake many natural phenomena for gods (Atran 2004). LLMs are neither conscious nor possessed of agency, but they seem as though they are, and their outputs may be persuasive in the same ways as human conversation.

There is lively debate about the consequences of automated persuasion. In a widely read paper, Bender et al. (2021, p. 617) describe large models as “stochastic parrots” and worry that the “ersatz fluency and coherence of [large models] raises several risks, precisely because humans are prepared to interpret strings belonging to languages they speak as meaningful and corresponding to the communicative intent of some individual or group of individuals who have accountability for what is said.”

These concerns have fed into existing worries about online political disinformation, provoking fears that LLMs will automate the production of highly persuasive propaganda (Goldstein et al. 2024, Kreps & Kriner 2024). Others have argued that LLMs’ powers of persuasion might be politically beneficial so that dialogue with LLMs can reduce people's beliefs in conspiracy theories (Costello et al. 2024) or produce consensus statements that elicit greater agreement among people with diverse political views (Tessler et al. 2024). Neither literature has yet built systematic connections either to the political science literature on persuasion (Coppock 2023) or comprehensively exploited the psychological literature on communication, deception, and vigilance (Sperber et al. 2010). While there is some reason to suspect that fears about AI-fueled misinformation are “overblown” (Simon et al. 2023), large models’ propensity to generate maximally unsurprising responses to initial prompts may target blind spots in human cognitive architecture (Sobieszek & Price 2022). Adjudicating the broader consequences is barely even a work in progress. We know far less about the interaction between human cognition and the output of LLMs than we need to.

Long-standing disputes over cultural control are spreading into new territory, as AI bias merges with cultural bias (Gallegos et al. 2024). LLMs and related models are trained on a variety of cultural material, much of which is scraped from the Internet. The predictable result is that they “encode stereotypical and derogatory associations along gender, race, ethnicity, and disability status” (Bender et al. 2021, p. 613). LLMs are less visibly biased than they used to be, in part because of reinforcement learning, but they often revert, for example, to gender stereotypes in pictures they generate, or assign characters with characteristically Black names to stereotyped roles in generated scenarios. Reinforcement learning only does so much. As Resnik (2024, p. 3) describes the problem, “To put it bluntly…a lot of what's in people's heads sucks…and, crucially…LLMs have no way to distinguish the stuff that sucks from the stuff that doesn't.”

A simple-seeming solution might be to stop training large models on biased cultural content. However, they are necessarily large: They require enormous corpora of cultural content. The corporate and nominally or actually nonprofit entities that build LLMs are typically disinclined to be selective in gathering text and images. Furthermore, they have become less willing to disclose their sources than previously (Dodge et al. 2021) as they look to preserve their commercial secrets, circumventing restrictions (Longpre et al. 2024) and fending off demands for compensation from those who generated the cultural content that the models are trained on.

More generally, engineering solutions are poorly suited to solve the problem of bias. That stems in part from technological limitations (Wolf et al. 2023). As Bommasani et al. (2021, p. 134) note, “Technical mitigation of all forms at present is severely limited: methods that measure or combat intrinsic bias are brittle or ineffectual.…Methods that measure or combat extrinsic outcome disparities may not align with stakeholder goals…and there is some evidence to suggest certain types of technical intervention may be simultaneously unsatisfiable…, impossible…[,] or may even exacerbate inequity.” Technical solutions that solve some problems may end up worsening others.

Yet the deepest dilemmas are political, not technical. There is no general consensus over what bias is, which biases are problematic, and how or whether biases ought to be removed. Instead, there is sharp political disagreement. That is in part inevitable, given the stakes, but it is not helped by a general disconnect between the purportedly technical debates over AI bias and social science and political theory discussions over how dissent works, when it is unavoidable, when it can be mitigated, and when it has benefits. This disconnect contributes to shallow understandings of what bias involves and what its consequences might be (Blodgett et al. 2020). It also makes it harder to argue out fundamental political disagreements. Should LLMs correct for a “dominant/hegemonic view” (Bender et al. 2021) that reinforces existing forms of inequality and oppression? Should they instead reflect some unfiltered version of the cultural content that has been scraped and fed to them, on the justification that this reflects some broad version of the “marketplace of ideas” (Zhang 2024)? These are profoundly political questions, even if few political scientists or theorists have so far taken them up.

Yet another set of debates involves how LLMs may affect human discovery and creativity, as they come to influence the creation of cultural content. Chiang's (2023) pithy depiction of LLMs as “blurry JPEGs” of the Internet suggests that their primary consequence will be to degrade human creativity and discovery, replacing it with an imprecise and inherently uncreative set of approximations and interpolations. Others (Shumailov et al. 2024; see also Alemohammad et al. 2023, Marchi et al. 2024) argue that LLMs are subject to the “curse of recursion.” As they generate an increasingly large share of cultural content, they are likely to increasingly be fed their own outputs. This will lead to a degenerative form of “model collapse” in which errors accumulate and feed on themselves, eventually producing incoherent nonsense. Equally, some amount of synthetic LLM generated data may be useful—determining the practical conditions of recursive collapse is an open research agenda. Fourcade & Farrell (2024) make a related but weaker argument, drawing from sociology rather than computer science, to suggest that LLMs are extremely well-suited to the automated performance of organizational ritual, such as the production of personal statements and performance reviews. As they become more prolific, information-generating social obligations, such as academic peer review, may degenerate, leading to inferior knowledge and lower trust (Z. Wojtowicz & S. DeDeo, unpublished manuscript).

Other scholars argue to the contrary, claiming that LLMs and related technologies may enable creativity and discovery rather than undermining it. Most obviously, LLMs can automate tedious tasks, such as summarizing large texts and generating bibliographies (they do so imperfectly, but so do research assistants). Yet they can also enable broader discovery. The embeddings at the heart of these models can provide summarized indices of information about the cultural and social patterns within which discovery occurs. This explains why LLM bias is such a difficult problem to solve, but also provides more sophisticated means for the mapping of culture ( Kozlowski et al. 2019). A combination of word2vec with a convolutional neural network can map very large corpora of scientific text, identifying possible combinations of concepts and materials that would not readily occur to human beings but might plausibly produce novel discoveries (Sourati & Evans 2023). More generally, combining the study of generative AI with evolutionary models might provide useful insights into how LLMs affect the selective retention of some aspects of culture, as well as the production of variation in others (Brinkmann et al. 2023, Yiu et al. 2024). The literature on complex problem-solving argues that these problems are most readily solved when agents with diverse understandings of the problem space can combine their representations (Bednar & Page 2018, Hong & Page 2004). Some early research suggests that generative models can loosely emulate group majority voting among people with less sophisticated understandings of the problem, by eliminating idiosyncratic errors (Zhang et al. 2024). It remains to be discovered whether such models, which surely contain compressed information about the diverse viewpoints of many actors, can be deployed in more genuinely creative ways.

Finally, large models are generating political battles over who gets what in the economy of cultural production. As noted above, there are open questions (Ramani & Wang 2023) over how and whether AI will lead to the vast economic transformations that optimists have predicted. But it will certainly lead to less sweeping forms of disruption, as cultural producers battle over the distribution of benefits and costs. What large models most obviously do is to generate imperfect substitutes for many products of human cultural labor—software code, articles, books, images, and increasingly video content. These substitutes may compete with original human production in the marketplace, generating economic tensions that may resemble the disruptions of the early nineteenth century, when craft-based forms of disruption were displaced by factory mass production, prompting the formation of the Luddite movement (Acemoglu & Johnson 2023, Thompson 1963).

It is still unclear how thoroughly generative AI can substitute for creative human labor. There is, more or less, no evidence to date of labor displacement (Acemoglu et al. 2022). Large models’ output still displays quite high degrees of slop and inconsistency and frequently tends toward the generic, limiting their applications for a number of high-value-added tasks. This may change.

If these problems are not solved, generative AI will be less broadly applicable, and there will be correspondingly less potential for broad political contention over its uses. But to the extent that AI does prove useful, it is likely to substitute for the work of relatively highly trained workers, who are plausibly better positioned to defend their interests than the unskilled and semiskilled workers in advanced industrial countries, who have lost bargaining power over the last few decades. Existing and forthcoming research (e.g., Thelen 2025) provides some understanding of the economic consequences of the platform economy, but there is still remarkably little work by political scientists on the political economic consequences of algorithms and AI as such.

As with other forms of AI, it is unclear how important large models will be over the long run. Even so, comparing them with existing large-scale forms of governance clarifies how they resemble them in principle, providing useful but lossy representations of vast bodies of cultural knowledge. If they succeed and spread, these models will plausibly reshape processes of cultural reproduction and coordination.

CONCLUSIONS

Tilly (1984) complained that the social sciences still suffocate beneath the incubus of the Industrial Revolution and its reordering of society and economy. He wished to know “how can we improve our understanding of the large-scale structures and processes that were transforming our world in the nineteenth century and are transforming it today” (p. 2).

Forty years later, we face a new version of Tilly's challenge, as technologies reshape the economy in unpredictable but possibly consequential ways. These changes are likely smaller than the consequences of nineteenth-century industrialization, aftershocks rather than the quake itself (Shalizi 2010). But they are still important.

This review suggests that we can meet this challenge by reconsidering the relationship between AI and the kinds of “large-scale structures and processes” that Tilly wrote about. By treating AI as a technology of governance, we can ask how it changes the markets, bureaucratic processes, and forms of democratic representation that reshaped the world during the Industrial Revolution. By surmising, alternatively, that it might become a form of governance, we can ask whether it may have transformative consequences in its own right.

Such arguments are necessarily tentative and speculative. I have emphasized that both governance and AI are loose concepts that are more useful as heuristics than hypothesis generators. But structured speculation may have value in a moment of large-scale and unpredictable changes. It is certainly possible that AI will not have wide-scale consequences for politics and society, but it is at the very least reasonable to ask whether it might and, if so, what those changes may be. By considering both how it may affect the old and how it may create openings for the new, we can begin to organize our inquiries.

There is an enormous amount to inquire about. As this review suggests, there are many more open research questions than there are answers. There are whole hosts of questions that this article has had insufficient space to discuss properly or, in some cases, even mention—for example, the consequences of AI for authoritarian stability, for international politics (Horowitz & Lin-Greenberg 2022), and for economic development, as well as the socialist calculation debate. And there are surely other topics deserving of attention that are obscured by the intellectual blind spots of this review but might be visible—and urgent—from different vantage points.

All of these questions present challenges for political scientists, who have lagged behind computer scientists, sociologists, economists, communications scholars, scholars of science and technology studies, and others in inquiring about AI. To catch up, they will need to develop new skills and technological understandings.

Over the longer term, they and other social scientists, and computer scientists and engineers too, may need to recalibrate disciplinary boundaries to better reflect political, economic, social, and technological changes. When Simon [2019 (1968)] emphasized that both the social sciences and the study of AI could be readily encompassed as “sciences of the artificial,” he was expressing a particular version of a more general ambition. For decades, various cyberneticists, AI researchers, complexity scientists, and others have wanted to bring the various systems through which humans process collective information and take decisions under a common analytic framework.

This ambition has been regularly articulated—and just as regularly frustrated. It will likely go on being frustrated into the foreseeable future. But as scholars in different disciplines begin to extend the boundaries of their disciplines to incorporate new questions, they will inevitably change their disciplines’ self-understanding. They may unexpectedly find common cause with scholars who start from very different places. Old disciplines will shift their positions; new ones may emerge. If political scientists want to be part of this conversation (and they ought to want it), they need to hurry up.

Subscribe now

disclosure statement

The author is not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review.

acknowledgments

I am grateful to James Cham and Cosma Shalizi for specific comments on earlier versions of this article; to an anonymous editor for suggested revisions; and to Ted Chiang, Dan Davies, Marion Fourcade, Hahrie Han, Margaret Levi, Nathan Matias, Bruce Schneier, Dan Wang, and many others for broader conversations on these topics. The discussion of AI as a form of governance builds on specific collaborative work with James Evans, Marion Fourcade, Alison Gopnik, and Cosma Shalizi. The errors are mine, while any good ideas are largely owed to the collective.

literature cited

- Acemoglu D, Autor D, Hazell J, Restrepo P. 2022.. Artificial intelligence and jobs: evidence from online vacancies. . J. Labor Econ. 40:(Suppl. 1):S293–340

[Crossref] [Citing articles] [Web of Science] [Google Scholar]

- Acemoglu D, Johnson S. 2023.. Power and Progress: Our Thousand-Year Struggle over Technology and Prosperity. New York:: Hachette

[Google Scholar]

- Alemohammad S, Casco-Rodriguez J, Luzi L, Humayun AI, Babaei H, et al. 2023.. Self-consuming generative models go MAD. . arXiv:2307.01850 [cs.LG]

- Alkhatib A, Bernstein M. 2019.. Street-level algorithms: a theory at the gaps between policy and decisions. . In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, pap . 530. New York:: ACM

[Google Scholar]

- Allen D. 2023.. Justice by Means of Democracy. Chicago:: Univ. Chicago Press

[Google Scholar]

- Allen D, Weyl EG. 2024.. The real dangers of generative AI. . J. Democr. 35:(1):147–62

[Crossref] [Web of Science] [Google Scholar]

- Arkoudas K. 2023.. GPT-4 can't reason. . arXiv:2308.03762 [cs.CL]

- Atran S. 2004.. In Gods We Trust: The Evolutionary Landscape of Religion. Oxford, UK:: Oxford Univ. Press

[Google Scholar]

- Bak-Coleman JB, Alfano M, Barfuss W, Bergstrom CT, Centeno MA, et al. 2021.. Stewardship of global collective behavior. . PNAS 118:(27):e2025764118

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Bednar J, Page SE. 2018.. When order affects performance: culture, behavioral spillovers, and institutional path dependence. . Am. Political Sci. Rev. 112:(1):82–98

[Crossref] [Web of Science] [Google Scholar]

- Bender EM, Gebru T, McMillan-Major A, Shmitchell S. 2021.. On the dangers of stochastic parrots: Can language models be too big?. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, pp. 610–23. New York:: ACM

[Google Scholar]

- Beniger J. 1986.. The Control Revolution: Technological and Economic Origins of the Information Society. Cambridge, MA:: Harvard Univ. Press

[Google Scholar]

- Benjamin R. 2019.. Race After Technology: Abolitionist Tools for the New Jim Code. New York:: Wiley

[Google Scholar]

- Berk RA. 2021.. Artificial intelligence, predictive policing, and risk assessment for law enforcement. . Annu. Rev. Crim. 4::209–37

[Crossref] [Web of Science] [Google Scholar]

- Blodgett SL, Barocas S, Daumé H III, Wallach H. 2020.. Language (technology) is power: a critical survey of “bias” in NLP. . arXiv:2005.14050 [cs.CL]

- Bommasani R, Hudson DA, Adeli E, Altman R, Arora S, et al. 2021.. On the opportunities and risks of foundation models. . arXiv:2108.07258 [cs.LG]

- Bowker GC, Star SL. 2000.. Sorting Things Out: Classification and Its Consequences. Cambridge, MA:: MIT Press

[Google Scholar]

- boyd d. 2010.. Social network sites as networked publics: affordances, dynamics, and implications. . In A Networked Self: Identity, Community, and Culture on Social Network Sites, ed. Z Papacharissi , pp. 47–66. London:: Routledge

[Google Scholar]

- Brinkmann L, Baumann F, Bonnefon JF, Derex M, Müller TF, et al. 2023.. Machine culture. . Nat. Hum. Behav. 7:(11):1855–68

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Budak C, Nyhan B, Rothschild DM, Thorson E, Watts DJ. 2024.. Misunderstanding the harms of online misinformation. . Nature 630:(8015):45–53

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Burrell J, Fourcade M. 2021.. The society of algorithms. . Annu. Rev. Sociol. 47::213–37

[Crossref] [Citing articles] [Web of Science] [Google Scholar]

- Calvino I. 2012.. Il Castello dei Destini Incrociati. Milan:: Ed. Mondadori

[Google Scholar]

- Caplan R, boyd d. 2018.. Isomorphism through algorithms: institutional dependencies in the case of Facebook. . Big Data Soc. 5:(1). https://doi.org/10.1177/2053951718757253

[Crossref] [Web of Science] [Google Scholar]

- Chiang T. 2023.. ChatGPT is a blurry JPEG of the Web. . New Yorker, Febr. 9

[Google Scholar]

- Chouldechova A. 2017.. Fair prediction with disparate impact: a study of bias in recidivism prediction instruments. . Big Data 5:(2):153–63

[Crossref] [Citing articles] [Medline] [Web of Science] [Google Scholar]

- Coalit. Indep. Technol. Res. 2024.. About us. Mission Statem., Coalit. Indep. Technol. Res., https://independenttechresearch.org/about-us/#about-us-mission

[Google Scholar]

- Coase RH. 1937.. The nature of the firm. . Economica 4:(16):386–405

[Crossref] [Google Scholar]

- Coppock A. 2023.. Persuasion in Parallel: How Information Changes Minds About Politics. Chicago:: Univ. Chicago Press

[Google Scholar]

- Costello TH, Pennycook G, Rand D. 2024.. Durably reducing conspiracy beliefs through dialogues with AI. . PsyArXiv xcwdn. https://doi.org/10.31234/osf.io/xcwdn

[Google Scholar]

- Covington P, Adams J, Sargin E. 2016.. Deep neural networks for YouTube recommendations. . In Proceedings of the 10th ACM Conference on Recommender Systems, pp. 191–98. New York:: ACM

[Google Scholar]

- Cronon W. 1991.. Nature's Metropolis: Chicago and the Great West. New York:: Norton

[Google Scholar]

- Cuéllar MF, Huq AZ. 2022.. Artificially intelligent regulation. . Daedalus 151:(2):335–47

[Crossref] [Web of Science] [Google Scholar]

- Dastin J. 2018.. Insight—Amazon scraps secret AI recruiting tool that showed bias against women. . Reuters, Oct. 11. https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG

[Google Scholar]

- Davies D. 2024.. The Unaccountability Machine: Why Big Systems Make Terrible Decisions—and How The World Lost Its Mind. London:: Profile

[Google Scholar]

- Dewey J. 1927.. The Public and Its Problems. New York:: Holt

[Google Scholar]

- Dodge J, Sap M, Marasović A, Agnew W, Ilharco G, et al. 2021.. Documenting large webtext corpora: a case study on the Colossal Clean Crawled Corpus. . arXiv:2104.08758 [cs.CL]

- Dunleavy P, Hood C. 1994.. From old public administration to new public management. . Public Money Manag. 14:(3):9–16

[Crossref] [Google Scholar]

- Eliassi-Rad T. 2024.. Just machine learning. Talk presented at Santa Fe Institute, June 4. 

- [Google Scholar]

- Engstrom DF, Ho DE, Sharkey CM, Cuéllar MF. 2020.. Government by algorithm: artificial intelligence in federal administrative agencies. Public Law Res. Pap. 20-54 , NYU Sch. Law, New York:

[Google Scholar]

- Eno B. 1976.. Generating and organizing variety in the arts. . Studio Int. 192:(984):279–83

[Google Scholar]

- Eur. Comm. 2024.. The Digital Services Act. Fact Sheet, Eur. Comm., Brussels:. https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/digital-services-act_en

[Google Scholar]

- Farrell H, Fourcade M. 2023.. The moral economy of high-tech modernism. . Daedalus 152:(1):225–35

[Crossref] [Web of Science] [Google Scholar]

- Farrell H, Gopnik A, Shalizi C, Evans J. 2025.. Large AI models are cultural and social technologies. . Science 387:(6739):115356

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Farrell H, Shalizi C. 2023.. Artificial intelligence is a familiar-looking monster. . The Economist, June 21. https://www.economist.com/by-invitation/2023/06/21/artificial-intelligence-is-a-familiar-looking-monster-say-henry-farrell-and-cosma-shalizi

[Google Scholar]

- Flack JC. 2017.. Coarse-graining as a downward causation mechanism. . Philos. Trans. R. Soc. A 375:(2109):20160338

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Fourcade M, Farrell H. 2024.. Large language models will upend human rituals. . The Economist, Sept. 4. https://www.economist.com/by-invitation/2024/09/04/large-language-models-will-upend-human-rituals

[Google Scholar]

- Fourcade M, Gordon J. 2020.. Learning like a state: statecraft in the digital age. . J. Law Political Econ. 1:(1):78–108

[Google Scholar]

- Fourcade M, Healy K. 2024.. The Ordinal Society. Cambridge, MA:: Harvard Univ. Press

[Google Scholar]

- Fourcade M, Johns F. 2020.. Loops, ladders and links: the recursivity of social and machine learning. . Theory Soc. 49:(5):803–32

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Gallegos IO, Rossi RA, Barrow J, Tanjim MM, Kim S, et al. 2024.. Bias and fairness in large language models: a survey. . Comput. Linguist. 50:(3):1097–179

[Crossref] [Web of Science] [Google Scholar]

- Gilman N, Cerveny B. 2023.. Tomorrow's democracy is open source. . NOEMA, Sept. 12. https://www.noemamag.com/tomorrows-democracy-is-open-source

[Google Scholar]

- Gillespie T. 2018.. Custodians of the Internet: Platforms, Content Moderation, and the Hidden Decisions That Shape Social Media. New Haven, CT:: Yale Univ. Press

[Google Scholar]

- Goldstein JA, Chao J, Grossman S, Stamos A, Tomz M. 2024.. How persuasive is AI-generated propaganda?. PNAS Nexus 3:(2):pgae034

[Crossref] [Citing articles] [Google Scholar]

- Gonzalez A, Matias N. 2024.. Measuring the mental health of content reviewers, a systematic review. . Preprint, arXiv:2502.00244v1 [cs.CY]

[Google Scholar]

- Grimmer J, Roberts ME, Stewart BM. 2021.. Machine learning for social science: an agnostic approach. . Annu. Rev. Political Sci. 24::395–419

[Crossref] [Web of Science] [Google Scholar]

- Harari YN. 2018.. Why technology favors tyranny. . The Atlantic, Oct. 15

[Google Scholar]

- Hayek FA. 1945.. The use of knowledge in society. . Am. Econ. Rev. 35:(4):519–30

[Google Scholar]

- Healy K. 2016.. SASE panel on the moral economy of technology. Talk presented at Univ. Calif., Berkeley:, June 28. https://kieranhealy.org/blog/archives/2016/06/28/sase-panel-on-the-moral-economy-of-technology

[Google Scholar]

- Hong L, Page SE. 2004.. Groups of diverse problem solvers can outperform groups of high-ability problem solvers. . PNAS 101:(46):16385–89

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Horowitz M, Lin-Greenberg E. 2022.. Algorithms and influence: artificial intelligence and crisis decision-making. . Int. Stud. Q. 66:(4):sqac069

[Crossref] [Web of Science] [Google Scholar]

- Jarrell R. 1941.. Kafka's tragi-comedy. . Kenyon Rev. 3::116–19

[Google Scholar]

- Johns F. 2021.. Governance by data. . Annu. Rev. Law Soc. Sci. 17::53–71

[Crossref] [Web of Science] [Google Scholar]

- Kaminski ME, Urban JM. 2021.. The right to contest AI. . Columbia Law Rev. 121:(7):1957–2048

[Google Scholar]

- Kleinberg J, Ludwig J, Mullainathan S, Rambachan A. 2018.. Algorithmic fairness. . Am. Econ. Assoc. Pap. Proc. 108::22–27

[Google Scholar]

- Kozlowski AC, Taddy M, Evans JA. 2019.. The geometry of culture: analyzing the meanings of class through word embeddings. . Am. Sociol. Rev. 84:(5):905–49

[Crossref] [Citing articles] [Web of Science] [Google Scholar]

- Kreps S, Kriner DL. 2024.. The potential impact of emerging technologies on democratic representation: evidence from a field experiment. . New Media Soc. 26:(12):6918–37

[Crossref] [Web of Science] [Google Scholar]

- Landemore H. 2021.. Open democracy and digital technologies. digital technology and democratic theory. . In Digital Technology and Democratic Theory, ed. L Bernholz, H Landemore, R Reich , pp. 62–89. Chicago:: Univ. Chicago Press

[Google Scholar]

- Lazar S. 2024.. Governing the algorithmic city. . arXiv:2410.20720 [cs.CY]

- Lindblom CE. 2002.. The Market System: What It Is, How It Works, and What to Make of It. New Haven, CT:: Yale Univ. Press

[Google Scholar]

- Longpre S, Mahari R, Lee A, Lund C, Oderinwale H, et al. 2024.. Consent in crisis: the rapid decline of the AI data commons. . arXiv:2407.14933 [cs.CL]

- Marchi M, Soatto S, Chaudhari P, Tabuada P. 2024.. Heat death of generative models in closed-loop learning. . arXiv:2404.02325 [cs.LG]

- Matias JN. 2019a.. The civic labor of volunteer moderators online. . Soc. Media Soc. 5:(2). https://doi.org/10.1177/2056305119836778

[Google Scholar]

- Matias JN. 2019b.. Preventing harassment and increasing group participation through social norms in 2,190 online science discussions. . PNAS 116:(20):9785–89

[Crossref] [Citing articles] [Medline] [Web of Science] [Google Scholar]

- Matias JN. 2023.. Humans and algorithms work together—so study them together. . Nature 617:(7960):248–51

[Crossref] [Google Scholar]

- Mayntz R. 2009.. New challenges to governance theory. . In Governance as Social and Political Communication, ed. H Bang , pp. 27–40. Manchester, UK:: Manchester Univ. Press

[Google Scholar]

- McElheran K, Li JF, Brynjolfsson E, Kroff Z, Dinlersoz E, et al. 2024.. AI adoption in America: who, what, and where. . J. Econ. Manag. Strategy 33:(2):375–415

[Crossref] [Web of Science] [Google Scholar]

- Mitchell M. 2019.. Artificial Intelligence: A Guide for Thinking Humans. New York:: Farrar, Straus & Giroux

[Google Scholar]

- Mitchell M. 2023.. How do we know how smart AI systems are?. Science 381:(6654):eadj5957

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Morucci M, Spirling A. 2024.. Model complexity for supervised learning: why simple models almost always work best, and why it matters for applied research. Work. Pap., Michigan State Univ., East Lansing, MI:. https://arthurspirling.org/documents/MorucciSpirling_JustDoOLS.pdf

[Google Scholar]

- Munger K. 2024.. The YouTube Apparatus. New York:: Cambridge Univ. Press

[Google Scholar]

- Nezhurina M, Cipolina-Kun L, Cherti M, Jitsev J. 2024.. Alice in Wonderland: simple tasks showing complete reasoning breakdown in state-of-the-art large language models. . arXiv:2406.02061 [cs.LG]

- Nguyen CT. 2021.. How Twitter gamifies communication. . In Applied Epistemology, ed. J Lackey , pp. 410–36. New York:: Oxford Univ. Press

[Google Scholar]

- Noble SU. 2018.. Algorithms of Oppression: How Search Engines Reinforce Racism. New York:: NYU Press

[Google Scholar]

- North DC. 1990.. Institutions, Institutional Change and Economic Performance. New York:: Cambridge Univ. Press

[Google Scholar]

- Oduro S, Kneese T. 2024.. AI Governance Needs Sociotechnical Expertise: Why the Humanities and Social Sciences Are Critical to Government Efforts. New York:: Data Soc.

[Google Scholar]

- Perrin AJ, McFarland K. 2011.. Social theory and public opinion. . Annu. Rev. Sociol. 37::87–107

[Crossref] [Web of Science] [Google Scholar]

- Peters G. 2012.. Governance as political theory. . In The Oxford Handbook of Governance, ed. D Levi-Faur , pp. 19–32. New York:: Oxford Univ. Press

[Google Scholar]

- Polanyi M. 1966.. The Tacit Dimension. New York:: Doubleday

[Google Scholar]

- Pomerantsev P. 2014.. Nothing Is True and Everything Is Possible: Adventures in Modern Russia. London:: Faber & Faber

[Google Scholar]

- Prior M. 2007.. Post-Broadcast Democracy: How Media Choice Increases Inequality in Political Involvement and Polarizes Elections. New York:: Cambridge Univ. Press

[Google Scholar]

- Queneau R. 1961.. Cent mille milliards de poèmes. Paris:: Gallimard

[Google Scholar]

- Radford A, Wu J, Child R, Luan D, Amodei D, Sutskever I. 2019.. Language models are unsupervised multitask learners. Work. Pap., OpenAI, San Francisco:. https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

[Google Scholar]

- Rahimi A, Recht B. 2017.. NIPS 2017 Test-of-Time Award presentation. Talk presented at 31st International Conference on Neural Information Processing Systems, Long Beach, CA:. 

- [Google Scholar]

- Ramani A, Wang Z. 2023.. Why transformative artificial intelligence is really, really hard to achieve. . The Gradient, June 26. https://thegradient.pub/why-transformative-artificial-intelligence-is-really-really-hard-to-achieve

[Google Scholar]

- Reich R, Sahami M, Weinstein J. 2021.. System Error: Where Big Tech Went Wrong and How We Can Reboot. New York:: HarperCollins

[Google Scholar]

- Resnik P. 2024.. Large language models are biased because they are large language models. . arXiv:2406.13138 [cs.CL]

- Roberts M. 2018.. Censored: Distraction and Diversion Inside China's Great Firewall. Princeton, NJ:: Princeton Univ. Press

[Google Scholar]

- Rothschild DM, Malhotra N. 2014.. Are public opinion polls self-fulfilling prophecies?. Res. Politics 1:(2). https://doi.org/10.1177/2053168014547667

[Crossref] [Google Scholar]

- Sanders N, Schneier B, Eisen N. 2024.. How public AI can strengthen democracy. . Brookings, March 4. https://www.brookings.edu/articles/how-public-ai-can-strengthen-democracy/

[Google Scholar]

- Schwartzberg M. 2015.. Epistemic democracy and its challenges. . Annu. Rev. Political Sci. 18::187–203

[Crossref] [Citing articles] [Web of Science] [Google Scholar]

- Scott J. 1998.. Seeing Like a State: How Certain Schemes To Improve the Human Condition Have Failed. New Haven, CT:: Yale Univ. Press

[Google Scholar]

- Shalizi C. 2010.. The singularity in our past light-cone. . Three-Toed Sloth Blog, Novemb. 28. http://bactra.org/weblog/699.html

[Google Scholar]

- Shumailov I, Shumaylov Z, Zhao Y, Gal Y, Papernot N, Anderson R. 2024.. AI models collapse when trained on recursively generated data. . Nature 631:(8022):755–59

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Simon FM, Altay S, Mercier H. 2023.. Misinformation reloaded? Fears about the impact of generative AI on misinformation are overblown. . Harvard Kennedy Sch. Misinformation Rev. 4:(5). https://doi.org/10.37016/mr-2020-127

[Google Scholar]

- Simon HA. 2019 (1968).. The Sciences of the Artificial. Cambridge, MA:: MIT Press. , 3rd ed..

[Google Scholar]

- Sobieszek A, Price T. 2022.. Playing games with AIs: the limits of GPT-3 and similar large language models. . Minds Mach. 32:(2):341–64

[Crossref] [Web of Science] [Google Scholar]

- Soper S. 2021.. Fired by bot at Amazon: ‘It's you against the machine. .’ Bloomberg, June 28

[Google Scholar]

- Sourati J, Evans JA. 2023.. Accelerating science with human-aware artificial intelligence. . Nat. Hum. Behav. 7:(10):1682–96

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Sperber D, Clément F, Heintz C, Mascaro O, Mercier H, et al. 2010.. Epistemic vigilance. . Mind Lang. 25:(4):359–93

[Crossref] [Citing articles] [Web of Science] [Google Scholar]

- Stanger A, Kraus J, Lim W, Millman-Perlah G, Schroeder M. 2024.. Terra incognita: the governance of artificial intelligence in global perspective. . Annu. Rev. Political Sci. 27::445–65

[Crossref] [Web of Science] [Google Scholar]

- Steinsson S. 2024.. Rule ambiguity, institutional clashes, and population loss: how Wikipedia became the last good place on the Internet. . Am. Political Sci. Rev. 118:(1):235–51

[Crossref] [Web of Science] [Google Scholar]

- Tessler MH, Bakker MA, Jarrett D, Sheahan H, Chadwick MJ, et al. 2024.. AI can help humans find common ground in democratic deliberation. . Science 386:(6719):adq2852

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Thelen K. 2025.. Attention, Shoppers! American Retail Capitalism and the Origins of the Amazon Economy. Princeton, NJ:: Princeton Univ. Press

[Google Scholar]

- Thompson EP. 1963.. The Making of the English Working Class. New York:: Vintage

[Google Scholar]

- Tilly C. 1984.. Big Structures, Large Processes, Huge Comparisons. New York:: Russell Sage Found.

[Google Scholar]

- Weber M. 1968.. Economy and Society. New York:: Bedminster

[Google Scholar]

- Weizenbaum J. 1966.. ELIZA—a computer program for the study of natural language communication between man and machine. . Commun. ACM 9:(1):36–45

[Crossref] [Google Scholar]

- Wiener N. 2019.. Cybernetics or Control and Communication in the Animal and the Machine. Cambridge, MA:: MIT Press

[Google Scholar]

- Wolf Y, Wies N, Avnery O, Levine Y, Shashua A. 2023.. Fundamental limitations of alignment in large language models. . arXiv:2304.11082 [cs.CL]

- Yates J. 1993.. Control through Communication: The Rise of System in American Management. Baltimore, MD:: Johns Hopkins Univ. Press

[Google Scholar]

- York JC, Zuckerman E. 2019.. Moderating the public sphere. . In Human Rights in the Age of Platforms, ed. RF Jørgensen , pp. 143–61. Cambridge, MA:: MIT Press

[Google Scholar]

- Yiu E, Kosoy E, Gopnik A. 2024.. Transmission versus truth, imitation versus innovation: what children can do that large language and language-and-vision models cannot (yet). . Perspect. Psychol. Sci. 19:(5):874–83

[Crossref] [Medline] [Web of Science] [Google Scholar]

- Zhang E, Zhu V, Saphra N, Kleiman A, Edelman BL, et al. 2024.. Transcendence: Generative models can outperform the experts that train them. . arXiv:2406.11741 [cs.LG]

- Zhang J. 2024.. ChatGPT as the marketplace of ideas: Should truth-seeking be the goal of AI content governance?. arXiv:2405.18636 [cs.CY]

- Zuboff S. 2019.. The Age of Surveillance Capitalism. London:: Profile

[Google Scholar]

- Zuckerman E. 2014.. New media, new civics?. Policy Internet 6:(2):151–68

[Crossref] [Google Scholar]
