---
title: "When AIs outperform the experts that train them, is that AGI?"
person: henry-farrell
section: by
type: blog-post
year: 2024
date: 2024-06-26
venue: "Programmable Mutter (Substack)"
authors: "Henry Farrell"
source_url: https://www.programmablemutter.com/p/when-ais-outperform-the-experts-that
retrieved: 2026-08-13
content: full-text
notes: "Substack post id 145993298; free to all readers (audience: everyone). Retrieved via the Substack API (api/v1/posts/by-id). Images/captions and comments removed."
---

# When AIs outperform the experts that train them, is that AGI?

*A new paper suggests that the answer is no*

## Full text

One of the frequently re-iterated themes of this newsletter is that we should see “AI” not as an equivalent to individual intelligence, but instead as a new means for organizing and coordinating human intelligence. As Alison Gopnik puts it, it is a new cultural technology. A lot of this has involved making the case for what LLMs are not - AGI, or artificial general intelligence that is equal to or superior to human intelligence. It should be noted that AGI is a rather slippery term, with various definitions. There are a lot of people who jump readily from research findings suggesting that ‘this model performs as well or better than humans at this particular task’ to broader conclusions along the lines of ‘OMG-the-machine-is-actually-beginning-to-think-and-maybe-about-to-start-self-improving-us-into-the-post-human-Vingean-singularity.’ AGI - as a loose and not very coherent notion - seems almost perfectly engineered to introduce this kind of confusion.

Which is why it is really nice to see a research paper that (a) provides some interesting evidence that generative models can outperform (some) humans, (b) provides a specific mechanism to explain how this outperformance happens, and (c) uses this to build some of the foundations for what an AI-as-means-for-channeling-collective-intelligence research agenda might look like. 

Subscribe now

The paper, by Zhang et al, is titled “Transcendence: Generative Models Can Outperform The Experts That Train Them,” and has been getting quite a lot of attention. Some of that attention at least has been driven by the title, which might suggest to the careless that this is another exercise in purportedly discovering Sparks Of AGI Generative Awesomeness. But if you actually read the paper, you will discover that it is anything but. Its notion of “transcendence” is much more carefully defined, and is rooted in a quite different (and, I think, much more fruitful) research tradition than AGI/existential risk to humans.

So here’s my view from the cheap seats of what the paper is doing, and why it is so valuable. NB that this is a view from the cheap seats - I am not a computer scientist, but a spectator whose sole claims to knowledge are (a) that I have been chucking popcorn from the back of the house for a long time, and (b) have occasionally worked with people who have a much better idea of what is going on. But audience knowledge and co-author osmosis only go so far - so there may be mistakes in the below summary (and if there are, I’d love to know what they are). NB also that you couldn’t design a paper (if I understand it right) more perfectly calculated to appeal to my priors - again, discount accordingly.

As I read it, the paper starts from the following notion. Generative models, including transformer models, are potentially capable of ‘transcendence’ under some circumstances. That is, they may produce predictions better than any of the individual experts whose outputs they have been trained on. The authors want to figure out when this happens and how. They do this by working with a generative model that has been trained on chess moves, carried out in games by players with different levels of expertise.

So what do they discover? Crudely speaking, they find that under some circumstances, their model can perform better than any one of the experts that it has been trained on. It seems to be better capable of chess than they are. However, the ‘under some circumstances’ has some interesting limits. First, the model does not display transcendence when it has been trained on really good chess players. It just does better than mediocre or middling ones. Second, its improvement seems to come from its superior capacity to deal with a particular set of crucial ‘states’ - situations on the board where making the right or wrong move is likely to have long term consequences for the game. Third, it performs well under ‘low’ temperatures - i.e. when the model’s predictions are more faithful to its training data, and to pick the most ‘likely’ output, rather than having some randomness injected.

How the authors interpret these results really interesting. Rather than suggesting that the model is in some way itself intelligent, or on the way to being so, they treat it as a better means of extracting information from the collectivity of experts who trained it, which is more ‘intelligent’ in some sense than any individual within it. Thus, their approach is a group based technique that closely approximates majority voting among the individual diverse perspectives of the experts.

The basic insight is that, as they put it, “diversity beats strength.” It is pretty well known that an ensemble of sufficiently diverse ‘weak learners’ - statistical models that may only be barely better than chance in predicting an outcome - will outperform a single ‘strong’ model that does not have diverse perspectives to draw upon. There is a big literature in computer science on this topic, and on how techniques such as ‘bagging’ or ‘boosting’ may be applied to further improve predictive strength.

And this is what drives their results. There is a lot of diversity among mediocre and middling chess players. Much of this diversity is noise rather than intelligent play - sometimes, when not-so-fantastic chess players are presented with a crucial move, they make a decision that a majority of their peers would recognize as being the wrong one. That, in turn means that there are high returns to denoising, which is effectively what the model does. Because the model has the temperature turned down real low, it is likely to plump predictably for the most expected move that a chess player of the relevant level would make in a tricky situation. That approximates to the move that the majority of players might vote for, if they were given the opportunity to vote.

Provided that mediocre players’ errors aren’t highly correlated, this will probably be a good move! On average, then, the model will predict better moves than any individual mediocre or middling player. It will do better exactly because its predictions will be less noisy, just as the average of guesses about the weight of an ox at a fair (in Galton’s famous example) will likely be better than any of the individual guesses of moderately informed observers.

As they note, this has limits. They do not see transcendence happening when the model is trained on highly skilled players, because there aren’t the same benefits to denoising. Hence, they hypothesize that a “1000 rated player can be thought of as a noisy 1500 rated player, but a 1500 rated player cannot be thought of as a noisy 2000 rated player.” More generally, they conclude that transcendence is not evidence of AGI, but of the contrary:

we would highlight that the denoising effect addressed in this paper does not offer any evidence for a model being able to produce novel solutions that a human expert would be incapable of devising. In particular, we do not present evidence that low temperature sampling leads to novel abstract reasoning, but rather denoising of errors.

But this in a sense, makes their argument more powerful. It presents the beginnings of an approach to thinking of these models, not as capable of becoming reasoners in their own right, through some magical process of emergence, but rather as extracting diverse forms of human knowledge and making it more useful. Two words - “the beginnings” - are doing a lot of work here. Lowering the temperature to approximate simple majority voting only goes so far. But even so, there are some quite interesting plausible applications, and much bigger research agendas to be pursued.

Two come to mind immediately. The first is the work of political scientist Scott Page, who applies similar ideas to group decision making among human agents. He too has done a ton of work on modeling diversity, asking how combining the diverse perspectives of relatively uninformed human beings can provide better understanding of complex phenomena than relying on highly trained but very similar experts. As he says here, we might want to apply bagging and boosting as ways to improve collective decision making among human beings as well as statistical weak learners. If we started to think about generative models as a Page-ian technology for combining different perspectives and extracting the benefits, what would we get out of this? How could we do this well? Could you build models to do more complex forms of knowledge extraction than straightforward denoising?

The second is Helena Miton and Simon DeDeo’s work on the transmission of tacit knowledge. They provide a simple model of how tacit knowledge gets passed from person to person, and why cultural evolution tends to be bursty (short and simplified version: most tacit knowledge is fairly readily transmitted with reasonable fidelity, and most transmission errors go nowhere - hence, we only get real cultural change on the rare occasions when a transmission error leads to a long leap to a very different point in the solution space). This approach is reasonably close in its broad modeling assumptions to the ideas in Zhang et al. We also have an emerging body of work (see Brynjolfsson et al.) on how LLMs may affect the transmission of tacit knowledge within organizations. Could we begin to bring these together, to start thinking more systematically about how generative models will affect processes of cultural transmission? Do the Zhang et al. results help explain why LLMs seem to be good at improving the tacit knowledge of not-so-strong employees, but less effective for really good ones? I don’t have enough deep understanding even to begin to answer yes or no, but I have just enough to surmise that it would be a lot of fun to find out.

In short - this is a paper that is potentially generative - it implies some quite important research agendas. If we could bring together the literatures on collective learning among human beings with the computer science literature on how generative models represent diverse human knowledge, we could find out a lot more about the consequences of these models as they’re applied at scale. We could also possibly find out quite a lot about collective knowledge among human beings.

Subscribe now
