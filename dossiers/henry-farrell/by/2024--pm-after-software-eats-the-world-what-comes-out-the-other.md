---
title: "After software eats the world, what comes out the other end?"
person: henry-farrell
section: by
type: blog-post
year: 2024
date: 2024-10-03
venue: "Programmable Mutter (Substack)"
authors: "Henry Farrell"
source_url: https://www.programmablemutter.com/p/after-software-eats-the-world-what
retrieved: 2026-08-13
content: full-text
notes: "Substack post id 149715132; free to all readers (audience: everyone). Retrieved via the Substack API (api/v1/posts/by-id). Images/captions and comments removed."
---

# After software eats the world, what comes out the other end?

*Malkovich. Malkovich. Malkovich?*

## Full text

Once, and not too long ago, my notions of the cultural consequences of Large Language Models (LLMs) were guided by a common metaphor of monsters of appetite. As Cosma and I and said in an article, “the political anthropologist James Scott has explained how bureaucracies are monsters of information, devouring rich, informal bodies of tacitly held knowledge and excreting a thin slurry of abstract categories that rulers use to “see” the world.” LLMs would do much the same thing to human culture. 

Such images were hardly unique to Cosma and myself. I saw a lot of online commentary suggesting that LLMs would evolve to combine the less attractive features of the Human Centipede and the Worm Ourobouros, as they increasingly fed on their own waste products. There was even a Nature article that spelled out the consequences of the “curse of recursion,” in which LLMs’ outputs would become increasingly disjointed and meaningless as they devour the content that they and their cousins created. It was an excellent article, but like many articles that take off in the discourse, I suspect that it owed its success more to its cultural resonances than its scientific results.

Thanks for reading Programmable Mutter! Subscribe for free to receive new posts. If you want to support my work, buy my and Abe Newman’s book, Underground Empire.

Being a Philip K. Dick fan, I had a specific PKD riff on this, building on the moment in Martian Time-Slip when an imagined journey into the future collapses into horror. Dick was fascinated with the notion of entropy, and he describes a terrifying kind of context collapse, in which normality begins to give way, and both matter and meaning disintegrate into “gubbish”: gobbets of rot and excrement with the appearance but not the actuality of life. Gubbish seemed a nice metaphor for what we got with the curse of recursion, and LLMs seemed like gubbishers - so I had what seemed like the makings for a solid enough piece.

But recently, I’ve grown more inclined towards a different controlling metaphor.** The problem with the self-devouring curse of recursion is that it is a result about models, their inputs and their outputs. Human beings only feature at the very beginning of the story, when they generate the outputs that are initially fed to the model. But in actuality, LLMs, like other algorithms, repeatedly influence and are influenced by human culture. 

Hence, I’ve turned to a different image of recursivity: the disturbing moment in Spike Jonze’s movie, Being John Malkovich (scripted by Charlie Kaufman), where the eponymous actor crawls through a portal that leads back into his own head. He finds himself in a restaurant with patrons and staff. All of them: men, women, adults, children, waiters, lounge-bar chanteuse, are also John Malkovich. If you haven’t seen it, it’s certainly worth watching. Kaufman is influenced by PKD, and it shows.

The force of this image really came home to me over the last couple of days, as I started to play around with Google’s NotebookLM (as its name suggests, this combines a notebook with a Large Model). The point of Kaufman’s scene is that not just any old rubbish (or gubbish) comes out the other end of the tunnel. Instead, we end up in a world of sameness, a universal society of Malkoviches saying Malkovich, Malkovich, Malkovich! to each other. 

That suggests a subtly different vision of the cultural downside of LLMs. As Alison Gopnik points out, LLMs are quite good at reproducing culture, but not so good at introducing cultural variation. One might go further. There is good reason to believe that these models are centripetal rather than centrifugal. On average, they create representations that tug in the direction of the dense masses at the center of culture, rather than towards the sparse fringe of weirdness and surprise scattered around the periphery.

Hence, my experience with NotebookLM, which can take a URL, and generate a short podcast, in which two people discuss whatever text is to be found there. That seemed specifically relevant! The title of this newsletter is a joking reference to “programmable matter,” a 1990s term for nanotechnology, which generated some fun science fiction and then more-or-less disappeared. But how could I possibly refuse the opportunity of turning Programmable Mutter into a very literal programmable mutter, and seeing what happened? 

The result was superficially very impressive. Two generic podcast voices with American accents, one female and one male, chatting with each other about this newsletter’s contents! Perhaps you can tell that the voices were artificially generated: I really couldn’t (maybe they were a little too smooth, but I probably wouldn’t have noticed - they dropped in plenty of phatics for camouflage).

The actual content was an entirely different story. The discussion greased the generic talk-show-host chitchat with equally generic compliments, but it got didn’t accurately summarize what I had said in the posts that it talked about. My post on why it would be a disaster if Trump replaced sanctions with tariffs becomes an “argument for replacing sanctions with tariffs,” because sanctions “often hurt citizens more than leaders.” The podcast ‘hosts’’ discussion of “shitposting,” “shitmining” and “shitfarming” defined those terms in wildly different ways than the post did. And so on. 

It was remarkable to see how many errors could be stuffed into 5 minutes of vacuous conversation. What was even more striking was that the errors systematically pointed in a particular direction. In every instance, the model took an argument that was at least notionally surprising, and yanked it hard in the direction of banality. A moderately unusual argument about tariffs and sanctions (it got into the FT after all) was replaced by the generic criticism of sanctions that everyone makes. And so on for everything else. The large model had a lot of gaps to fill, and it filled those gaps with maximally unsurprising content. 

This reflects a general problem with large models. They are much better at representing patterns that are common than patterns that are rare. More technically:

Most real-world data naturally have a skewed distribution … with a small number of well-represented features and a “long-tail” of features that are relatively underrepresented. The skew in feature frequency leads to disparate error rates on the underrepresented attribute. This prompts fairness concerns when the underrepresented attribute is a protected attribute but more broadly relates to the brittleness of deep neural network performance in data-limited regimes.

Hence, a variety of challenges associated with large models, including the persistent tidal pull of DALL-E towards pictures that seem like a potpourri of DeviantArt circa 2015. Hence, also, the remarkable blandness of AI-produced beach books. What is common has cultural gravity. What is rare does not.

This has important implications, when combined with Gopnik’s thesis that large models are increasingly important engines of cultural reproduction. Such models will probably not subject human culture to the curse of recursion, in which noise feeds upon noise. Instead, they will parse human culture with a lossiness that skews, so that central aspects of that culture are accentuated, and sparser aspects disappear in translation. The thing about large models is that they tend to select for features that are common and against those that are counter, original, spare, strange. Instead of focusing on the gubbisher - a universally hungry agent of entropy and decay - one should emphasize the fact that it will disappear some aspects of culture more quickly than others.

This has implications for cultural discovery, and scientific discovery too. There is strong reason to suspect (as Marion Fourcade and I argued a few weeks ago) that scholars are increasingly relying on LLMs to pump out peer reviews. Ethan Mollick reports on a research paper which finds that computer science researchers are pretty happy with AI-generated peer review, and don’t view it as necessarily worse than what they get from human reviewers.* The authors of the paper did carry out some simple tests to see whether the AI-generated reviews were completely generic. 

But what they couldn’t easily test for - and what I think is the most crucial question - is whether AI reviews could identify and evaluate the features of the paper that were original and novel. I would lay a lot of money that AI reviews are much worse at this even than human reviewers. Such features are likely to be invisible to them, for much the same reason that Notebook LM had a harder time spotting the more unconventional claims of this newsletter. 

This is something that is hardwired into the technology. The more unusual a cultural feature is, the less likely it is to feature prominently in a large model’s representation of the culture. Notoriously, human peer reviewers too are often unwilling to recognize novel contributions. But they regularly at least recognize that these claims are novel, even if they frequently damn and blast them for their purported irrelevance and stupidity. Large models, instead, are more likely to quietly and simply strain them out.

This pushes back against the claim of Marc Andreessen and others that software is eating the world and It Is Going To Be Awesome as AI unleashes all that wonderful innovation. It focuses our attention on what comes out the other end of that act of devouring: a world in which recursion doesn’t quite turn us all into John Malkovich, talking about Malkovich to Malkoviches, but does bring us closer to that weird and unsettling scene than we are right now, as we converge ever more on what we have in common, smoothing away the particularities that distinguish the one from all the others.

The plausible destination that LLMs conduct towards is not entropy, or at least not entropy any time soon, but a cluster of cultural strong attractors that increase conformity, and makes it much harder to find new directions and get them to stick. The more that we rely on AI in its current form, the more that human culture (including scientific culture) will converge on what is central.

To be clear: technology is not destiny. Perhaps different cultural engines will have different affordances. And even the ones we have right now can be used in surprising ways. James Evans’ research, for example, suggests that AI generated maps of banality can be deployed against themselves to suggest the directions in which real innovation might most usefully proceed (I speak poetically, but that is not too far from the key insight). Still, those are not the most obvious, or the easiest, uses of large models and their kin.

Thanks for reading Programmable Mutter! Subscribe for free to receive new posts. If you want to support my work, buy my and Abe Newman’s book, Underground Empire.

 * There is some evidence that AI tends to provide higher review scores than human reviewers; this may also explain why authors like them. It is an unusual author altogether who prefers harsh excoriation to loving encouragement, and I have never to my knowledge met one myself.

** To be clear, a metaphor is only a metaphor. It highlights some aspects of the problem at the expense of others, and different metaphors might point to different understandings of the future. For example, PKD’s story “Second Variety,” where the machine intelligences become hostile to each other, generating the beginnings of their own ecology of competition and cooperation suggests an understanding of the future that would be closer to complex weirdnesses of Amazon Marketplace, with proliferating algorithms fighting it out against each other.
