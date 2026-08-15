---
title: "On Feral Library Card Catalogs, or, Aware of All Internet Traditions"
person: henry-farrell
section: by
type: blog-post
year: 2025
date: 2025-04-17
venue: "Programmable Mutter (Substack)"
authors: "Henry Farrell"
source_url: https://www.programmablemutter.com/p/on-feral-library-card-catalogs-or
retrieved: 2026-08-13
content: full-text
notes: "Substack post id 161493665; free to all readers (audience: everyone). Retrieved via the Substack API (api/v1/posts/by-id). Images/captions and comments removed."
---

# On Feral Library Card Catalogs, or, Aware of All Internet Traditions

*A Guest Post by Cosma Shalizi*

## Full text

The below is a guest post by Cosma Shalizi, which was originally published here. Cosma is both a co-author and a friend, and has profoundly influenced my thinking about technology and culture for decades. Many of the pieces published here are really better considered as collaborations between me and my mental model of Cosma, which is somehow smarter than I am , but notably less intelligent than the real thing. So here’s the real thing. NB that Cosma’s post is too long for email: click through (or just click the ‘originally published’ link above) to get the full thing.

Subscribe now

Attention conservation notice: Almost 3900 words of self-promotion for an academic paper about large language models (of all ephemeral things). Contains self-indulgent bits trimmed from the published article, and half-baked thoughts too recent to make it in there.

For some years now, I have been saying to anyone who'll listen that the best way to think about large language models and their kin is due to the great Alison Gopnik, and it's to regard them as cultural technologies. All technologies, of course, are cultural in the sense that they are passed on from person to person, generation to generation. In the process of leaping from mind to mind, cultural content always passes through some external, non-mental form: spoken words, written diagrams, hand-crafted models, demonstrations, interpretive dances, or just examples of some practice carried out by the exemplifier's body [1]. A specifically cultural technology is one that modifies that very process of transmission, as with writing or printing or sound recording. That is what LLMs do; they are not so much minds as a new form of information retrieval.

I am very proud to have helped play a part in giving Gopnikism [2] proper academic expression:

Henry Farrell, Alison Gopnik, CRS and James Evans, "Large AI models are cultural and social technologies", Science 387 (2025): 1153--1156 [should-be-public link]

Abstract: Debates about artificial intelligence (AI) tend to revolve around whether large models are intelligent, autonomous agents. Some AI researchers and commentators speculate that we are on the cusp of creating agents with artificial general intelligence (AGI), a prospect anticipated with both elation and anxiety. There have also been extensive conversations about cultural and social consequences of large models, orbiting around two foci: immediate effects of these systems as they are currently used, and hypothetical futures when these systems turn into AGI agents --- perhaps even superintelligent AGI agents. But this discourse about large models as intelligent agents is fundamentally misconceived. Combining ideas from social and behavioral sciences with computer science can help us to understand AI systems more accurately. Large models should not be viewed primarily as intelligent agents but as a new kind of cultural and social technology, allowing humans to take advantage of information other humans have accumulated.

What follows is my attempt to gloss and amplify some parts of our paper. My co-authors are not to be blamed for what I say here: unlike me, they're constructive scholars.

Myth and Information Retrieval

To put things more bluntly than we did in the paper: the usual and even academic debate over these models is, frankly, conducted on the level of myths (and not even of mythology). We have centuries of myth-making about creating intelligences and their consequences [3], Tampering with Forces Man Was Not Meant to Know, etc. Those myths have hybridized with millennia of myth-making about millenarian hopes and apocalyptic fears. [4] This is all an active impediment to understanding.

LLMs are parametric probability models of symbol sequences, fit to large corpora of text by maximum likelihood. By design, their fitting process strives to reproduce the distribution of text in the training corpus [5]. (The log likelihood is a proper scoring function.) Multi-modal large models are LLMs yoked to models of (say) image distributions; they try to reproduce the joint distribution of texts and images. Prompting is conditioning: the output after a prompt is a sample from the conditional distribution of text coming after the prompt (or the conditional distribution of images that accompany those words, etc.). All these distributions are estimated with a lot of smoothing: parts of the model like "attention" (a.k.a. kernel smoothing) tell the probability model when to treat different-looking contexts as similar (and how closely similar), with similar conditional distributions. This smoothing, what Andy Gelman would call "partial pooling", is what lets the models respond with sensible-looking output, rather than NA, to prompts they've never seen in the training corpus. It also, implicitly, tells the model what to ignore, what distinctions make no difference. This is part (though only part) of why these models are lossy.

(The previous paragraph, like our paper, makes no mention of neural networks, of vector embeddings as representations of discrete symbols, of LLMs being high-order Markov chains, etc. Those are important facts about current models. [That Markov models, of all things, can do all this still blows my mind.] But I am not convinced that these are permanent features of the technology, as opposed to the first things tried that worked. I really think we should know more about is how well other techniques for learning distributions of symbols sequences would work if given equivalent resources. I really do want to see someone try Large Lempel-Ziv. I also have a variety of ideas for combining Infini-gram with old distribution-learning procedures which I think would at the very least make good student projects. [I'm being a bit cagey because I'd rather not be scooped; get in touch if you're interested in collaborating.] I am quite prepared for all of these Mad Schemes to work less well than conventional LLMs, but then I think the nature and extent of the failures would be instructive. In any case, the argument we're making about these artifacts does not depend on these details of their innards.)

What follows from all this?

- These are ways of interpolating, extrapolating, smoothing, and sampling from the distribution of public, digitized representations we [6] have filled the Internet with. Now, most people do not have much experience with samplers --- certainly not with devices that sample from complex distributions with lots of dependencies. (Games of chance are built to have simple, uniform distributions.) (In fact, maybe the most common experience of such sampling is in role-playing games.) But while this makes them a novel form of cultural technology, they are a cultural technology.

- They are also a novel form of social technology. They create a technically-mediated relationship between the user, and the authors of the documents in the training corpora. To repeat an example from the paper, when someone uses a bot to write a job-application letter, the system is mediating a relationship between the applicant and the authors of hundreds or thousands of previous such letters. More weakly, the system is also mediating a relationship between the applicant and the authors of other types of letters, authors of job-hunting handbooks, the reinforcement-learning-from-human-feedback workers [7], etc., etc. (If you ask it how to write a regular expression for a particular data-cleaning job, it is mediating between you and the people who used to post on Stack Overflow.) Through the magic of influence functions, those with the right accesses can actually trace and quantify this relationship.

- These aren't agents with beliefs, desires and intentions. (Prompting them to "be an agent" is just conditioning the stochastic process to produce the sort of text that would follow a description of an agent, which is not the same thing.) They don't even have goals in the way in which a thermostat, or lac operon repressor circuit, have goals. [8] They also aren't reasoning systems, or planning systems, or anything of that sort. Appearances to the contrary are all embers of autoregression. (Some of those embers are blown upon by wishful mnemonics.)

I was (I suspect) among the last cohorts of students who were routinely taught how to use paper library card catalogs. Those, too, were technologies for bringing inquirers into contact with the works of other minds. You can worry, if you like, that LLMs or their kin are going to grow into uncontrollable artificial general intelligences, but it makes about as much sense as if I'd had nightmares about card catalogs going feral.

Complex Information Processing, and the Primal Scene of AI

Back when all this was beginning, in the spring of 1956, Allen Newell and Herbert Simon thought that "complex information processing" was a much better name than "artificial intelligence" [9]:

The term "complex information processing" has been chosen to refer to those sorts of behaviors --- learning, problem solving, and pattern recognition --- which seem to be incapable of precise description in any simple terms, or perhaps, in any terms at all. [p. 1]
Even though our language must still remain vague, we can at least be a little more systematic about what constitutes a complex information process.

- A complex process consists of very large numbers of subprocesses, which are extremely diverse in their nature and operation. No one of them is central or, usually, even necessary.

- The elementary component processes need not be complex; they may be simple and easily understood. The complexity arises wholly from the pattern in which these processes operate.

- The component processes are applied in a highly conditional fashion. In fact, large numbers of the processes have the function of determining the conditions under which other processes will operate.

[p. 6]

If "complex information processing" had become the fixed and common name, rather than "artificial intelligence", there would, I think, be many fewer myths to contend with. To use a technical but vital piece of meta-theoretical jargon, the former is "basically pleasant bureaucrat", the latter is "sexy murder poet" (at least in comparison).

Newell and Simon do not mention it, explicitly, in this paper, but the component processes in a complex information-processing system can be hard-wired machines, or flexible programmed machines, or human beings, or any combination of these. Remember that Simon was, after all, a trained political scientist whose first book was Administrative Behavior and who had, in fact, worked as a government bureaucrat, helping to implement the Marshall Plan. Even more, the first time Newell and Simon ran their Logic Theorist program (described in that paper), they ran it on people, because the electronic computer was back-ordered. I will let Simon tell the story:

Al [Newell] and I wrote out the rules for the components of the program (subroutines) in English on index cards, and also made up cards for the contents of the memories (the axioms of logic). At the GSIA [= Graduate School of Industrial Administration] building on a dark winter evening in January 1956, we assembled my wife and three children together with some graduate students. To each member of the group, we gave one of the cards, so that each person became, in effect, a component of the LT computer program --- a subroutine that performed some special function, or a component of its memory. It was the task of each participant to execute his or her subroutine, or to provide the contents of his or her memory, whenever called by the routine at the next level above that was then in control.

So we were able to simulate the behavior of LT with a computer constructed of human components. Here was nature imitating art imitating nature. The actors were no more responsible for what they were doing than the slave boy in Plato's Meno, but they were successful in proving the theorems given them. Our children were then nine, eleven, and thirteen. The occasion remains vivid in their memories.
[Models of My Life, ch. 13, pp. 206--207 of the 1996 MIT Press edition.]

The primal scene of AI, if we must call it that, is thus one of looking back and forth between a social organization and an information-processing system until one can no longer tell which is which.

All-Access Pass to the House of Intellect

Lots of social technologies can be seen as means of effectively making people smarter. Participants in a functioning social institution will all act better and more rationally because of those institutions. The information those participants get, the options they must choose among, the incentives they face, all of these are structured --- limited, sharpened and clarified --- by the institutions, which helps people think. Continued participation in the institution means facing similar situations over and over, which helps people learn. Markets are like this; bureaucracies are like this; democracy is like this; scientific disciplines are like this. [10] And cultural tradition is like this.

Let me quote from an old book that had a lot of influence on me:

Intellect is the capitalized and communal form of live intelligence; it is intelligence stored up and made into habits of discipline, signs and symbols of meaning, chains of reasoning and spurs to emotion --- a shorthand and a wireless by which the mind can skip connectives, recognize ability, and communicate truth. Intellect is at once a body of common knowledge and the channels through which the right particle of it can be brought to bear quickly, without the effort of redemonstration, on the matter in hand.
Intellect is community property and can be handed down. We all know what we mean by an intellectual tradition, localized here or there; but we do not speak of a "tradition of intelligence," for intelligence sprouts where it will.... And though Intellect neither implies nor precludes intelligence, two of its uses are --- to make up for the lack of intelligence and to amplify the force of it by giving it quick recognition and apt embodiment.
For intelligence wherever found is an individual and private possession; it dies with the owner unless he embodies it in more or less lasting form. Intellect is on the contrary a product of social effort and an acquirement.... Intellect is an institution; it stands up as it were by itself, apart from the possessors of intelligence, even though they alone could rebuild it if it should be destroyed....
The distinction becomes unmistakable if one thinks of the alphabet --- a product of successive acts of intelligence which, when completed, turned into one of the indispensable furnishings of the House of Intellect. To learn the alphabet calls for no great intelligence: millions learn it who could never have invented it; just as millions of intelligent people have lived and died without learning it --- for example, Charlemagne.
The alphabet is a fundamental form to bear in mind while discussing ... the Intellect, because intellectual work here defined presupposes the concentration and continuity, the self-awareness and articulate precision, which can only be achieved through some firm record of fluent thought; that is, Intellect presupposes Literacy.
But it soon needs more. Being by definition self-aware, Intellect creates linguistic and other conventions, it multiplies places and means of communication....
The need for rules is a point of difficulty for those who, wrongly equating Intellect with intelligence, balk at the mere mention of forms and constraints --- fetters, as they think, on the "free mind" for whose sake they are quick to feel indignant, while they associate everything dull and retrograde with the word "convention". Here again the alphabet is suggestive: it is a device of limitless and therefore "free" application. You can combine its elements in millions of ways to refer to an infinity of things in hundreds of tongues, including the mathematical. But its order and its shapes are rigid. You cannot look up the simplest word in any dictionary, you cannot work with books or in a laboratory, you cannot find your friend's telephone number, unless you know the letters in their arbitrary forms and conventional order.

---Jacques Barzun, The House of Intellect (New York: Harper, 1959), pp. 3--6

A huge amount of cultural and especially intellectual tradition consists of formulas, templates, conventions, and indeed tropes and stereotypes. To some extent this is to reduce the cognitive burden on creators: this has been extensively studied, for instance, for oral culture, such as oral epics. But formulas also reduce the cognitive burden on people receiving communications. Scientific papers, for instance, within any one field have an incredibly stereotyped organization, as well as using very formulaic language. One could imagine a world where every paper was supposed to be a daring exploration of form as well as content, but in reality readers want to be able to check what the reagents were, or figure out which optimization algorithm was used, and the formulaic structure makes that much easier. This is boiler-plate and ritual, yes, but it's not just boiler-plate and ritual, or at least not pointless ritual [11].

Or, rather, the formulas make things easier to create and to comprehend once you have learned the formulas. The ordinary way of doing so is to immerse yourself in artifacts of the tradition until the formulas begin to seep in, and to try your hand at making such artifacts yourself, ideally under the supervision of someone who already has grasped the tradition. (The point of those efforts was not really to have the artifacts, but to internalize the forms.) Many of the formulas are not articulated consciously, even by those who are deeply immersed in the tradition.

Large models have learned nearly all of the formulas, templates, tropes and stereotypes. (They're probability models of text sequences, after all.) To use Barzun's distinction, they will not put creative intelligence on tap, but rather stored and accumulated intellect. If they succeed in making people smarter, it will be by giving them access to the external forms of a myriad traditions.

None of this is to say that large models are an unambiguous good thing:

- Maybe giving people access to the exoteric forms of tradition, without internalizing the habits that went along with them, is going to be a disaster.

- These technologies are already giving us entirely new political-economic struggles, especially about rewarding (or not) the creation of original content.

- As statistical summaries of large corpora, the models are intrinsically going to have a hard time dealing with rare situations. (More exactly: If there's an option, in model training, to do a little bit better in a very common situation at the cost of doing a lot worse in a very rare situation, the training process is going to take it, because it improves average performance.) In other words: sucks to try to use them to communicate unusual ideas, especially ideas that are rare because they are genuinely new.

- Every social technology has its ways of going horribly wrong. Often those arise from the kinds of information they ignore, which are also what make them useful. We know something about how markets fail, and bureaucracies, and (oh boy) democracies. We have no idea, yet, about the social-technology failure-modes of large models.

These are just a few of the very real issues which surround these technologies. (There are plenty more.) Spinning myths about superintelligence will not help us deal with them; seeing them for what they are will.

Subscribe now

[1]: I first learned to appreciate the importance, in cultural transmission, of the alternation between public, external representations and inner, mental content by reading Dan Sperber's Explaining Culture. ^

[2]: I think I coined the term "Gopnikism" in late 2022 or early 2023, but it's possible I got it from someone else. (The most plausible source however is Henry, and he's pretty sure he picked it up from me.) ^

[3]: People have been telling the joke about asking a supercomputer "Is there a god?" and it answering "There is now" since the 1950s. Considering what computers were like back then, I contend it's pretty obvious that some part of (some of) us wants to spin myths around these machines. ^

[4]: These myths have also hybridized with a bizarre conviction that "this function increases monotonically" implies "this function goes to infinity", or even "this function goes to infinity in finite time". When this kind of reasoning grips people who, in other contexts, display a perfectly sound grasp of pre-calculus math, something is up. Again: mythic thinking. ^

[5]: Something we didn't elaborate on in the paper, and I am not going to do justice to here, is that one could deliberately not match the distribution of the training corpus -- one can learn some different distribution. Of course to some extent this is what reinforcement learning from human feedback (and the like) aims at, but I think the possibilities here are huge. Nearly the only artistically interesting AI image generation I've seen is a hobbyist project generating pictures of a fantasy world, facilitated by creating a large artificial vocabulary for both style and content, and (by this point) almost exclusively training on the output of previous iterations of the model. In many ways, the model itself, rather than its images, is the artwork. (I am being a bit vague because I am not sure how much attention the projector wants.) Without suggesting that everything needs to be, as it were, postcards from Tlön, the question of when and how to "tilt" the distribution of large training corpora to achieve specific effects seems at once technically interesting and potentially very useful. ^

[6]: For values of "we" which include "the sort of people who pirate huge numbers of novels" and "the sort of people who torrent those pirated novel collections on to corporate machines". ^

[7]: If the RLHF workers are, like increasing numbers of online crowd-sourced workers, themselves using bots, we get a chain of technical mediations, but just a chain and not a loop. ^

[8]: I imprinted strongly enough on cybernetics that part of me wants to argue that an LLM, as an ergodic Markov chain, does have a goal after all. This is to forget the prompt entirely and sample forever from its invariant distribution. On average, every token it produces returns it, bit by bit, towards that equilibrium. This is not what people have in mind. ^

[9]: Strictly speaking, they never mention the phrase "artificial intelligence", but they do discuss the work of John McCarthy et al., so I take the absence of that phrase to be meaningful. Cf. Simon's The Sciences of the Artificial, "The phrase 'artificial intelligence' ... was coined, I think, right on the Charles River, at MIT. Our own research group at Rand and Carnegie Mellon University have preferred phrases like 'complex information processing' and 'simulation of cognitive processes.' ... At any rate, 'artificial intelligence' seems to be here to stay, and it may prove easier to cleanse the phrase than to dispense with it. In time it will become sufficiently idiomatic that it will no longer be the target of cheap rhetoric." (I quote from p. 4 of the third edition [MIT Press, 1996], but the passage dates back to the first edition of 1969.) Simon's hope has, needless to say, not exactly been achieved. ^

[10]: Markets, bureaucracies, democracies and disciplines are also all ways of accomplishing feats beyond the reach of individual human minds. I am not sure that cultural traditions are, too; and if large models are, I have no idea what those feats might be. (Maybe we'll find out.) ^

[11]: Incorporated by reference: Arthur Stinchcombe's When Formality Works, which I will write about at length one of these decades.
