---
title: "AI, Movable Type, & Federated Learning, with Blaise Agüera y Arcas"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2022
date: 2022-01-19
venue: "Carnegie Council for Ethics in International Affairs — AI & Equality Initiative podcast"
authors: "Host: Anja Kaspersen"
source_url: https://carnegiecouncil.org/media/series/aiei/20220119-ai-movable-type-federated-learning-blaise-aguera-y-arcas
retrieved: 2026-08-13
content: full-text
notes: "Official transcript published by Carnegie Council alongside the podcast episode."
---

# AI, Movable Type, & Federated Learning, with Blaise Agüera y Arcas

## Full text

#  AI, Movable Type, & Federated Learning, with Blaise Aguera y Arcas 

Jan 19, 2022

#####  Guest 

Blaise Aguera y Arcas

###  Blaise Aguera y Arcas 

Google Research 

#####  Hosted by 

Anja Kaspersen

###  Anja Kaspersen 

Former Carnegie Council Senior Fellow, Artificial Intelligence & Equality Initiative (AIEI); IEEE 

#####  About the Series 

Can AI be deployed in ways that enhance equality, or will AI systems exacerbate existing structural inequalities and create new inequities? The Artificial Intelligence & Equality podcast seeks to understand the innumerable ways in which AI affects equality and international affairs. 

###  Share 

  *   *   *   * 

###  Stay updated on news, events, and more 

Join our mailing list 

Are we reaching for the wrong metaphors and narratives in our eagerness to govern AI? In this "Artificial Intelligence & Equality" podcast, Carnegie Council Senior Fellow Anja Kaspersen is joined by Google Research’s Blaise Aguera y Arcas. In a talk that spans from Gutenberg to federated learning models to what we can learn from nuclear research, they discuss what we need to be mindful of when discussing and engaging with future applications of machine intelligence.

**ANJA KASPERSEN:** Today I am joined by Blaise Aguera y Arcas, a vice-president and a fellow with Google AI Research, where he leads a team leveraging machine intelligence in many different domains. Blaise is known for his work on federated learning, computer vision, natural language models, and machine intelligence applied more broadly. Prior to joining Google, he was a distinguished engineer at Microsoft.

Blaise, thank you so much for being with us today. Let us dive right into what I know will be a fascinating and rich discussion. I am very curious, as I am sure our listeners are as well, what have been driving your interest in machine learning (ML), and artificial intelligence (AI) more specifically, working on the cutting edge of technology innovation for many years now?

**BLAISE AGUERA y ARCAS:** Since I was really young—I grew up in the era of techno optimism, as I guess many of us in our generation did—there are a handful of fairly stereotypical frontiers that were I think of interest to all of us—they were space and fundamental physics and cosmology, and of course the brain and artificial intelligence—it's one of the grand quests. So I have always been very interested in it.

In the beginning I was enchanted by the early and mid-20th century physicists and the big advances in fundamental theories, and I thought up through the first part of my college experience that that's the kind of work that I would do. But it became increasingly clear to me that the kind of rapid advancement—and also the kind of "tabletop science" frankly—that lit me up was really happening in neuroscience and what we now call AI, although progress in AI was very slow up until recently, I would say maybe 2006 or 2010, somewhere around then.

In the beginning, the place where it seemed like the frontier was really advancing very rapidly was neuroscience, studying brains. We went in fairly rapid order from very high-level theories in the 19th century and the early 20th century from being able to start doing electrophysiology, which was done on a very limited scale in the first part of the 20th century, to starting to be able to record from brains while the animal is alive, awake, and behaving toward the end of the 20th century. This kind of work was very exciting.

I remember when I first saw some of the experiments that my adviser at the time, Bill Bialek, was doing, first at the NEC Research Institute and then at Princeton. They were hooking up a fly to a virtual reality rig, so it's a fly that is kept alive with a little—it's rather _Frankenstein_-ish really—wax bowl with sugar water and a hole in its head and an electrode in its brain at the same time as it is being shown a virtual reality environment, so you have a kind of fly in the matrix, and you can create closed-loop experiments in which you are recording and even stimulating and understanding some fairly fundamental things about how the fly's brain works relative to its perceptual and motor environment. That was pretty exciting. I felt like it was starting to get at some fundamental questions about one of those big frontiers. That was my early interest.

I then went off on what I guess you could call a very long tangent first in computational humanities and then in start-up land. I made a start-up, and that was acquired by Microsoft, and I was in the corporate world for a while, and we did interesting things in computer vision and in some other areas of machine learning.

But I never lost the bug of neuroscience and brains, and when deep learning began to appear on the scene in the late 2000s, and especially starting around 2010, it felt like the two worlds—the world that I was in almost accidentally of computer science and my old love of neuroscience—were starting to converge again; from the time when these two threads split apart around 1943 of neuroscience and computers, they were starting to come back together, and I had to get involved again. It was a big motivation for my move to Google.

**ANJA KASPERSEN:** I read a quote by you, which I believe is related to your work on computational photography, which we will come back to, that your attraction "has never been to computers per se but to the fact that they offer a highly leveraged way to invent magic," which relates to some of the issues that you were just touching upon.

I have been watching a lot of mountain-climbing movies lately. Is it the mountaineering of AI that interests you, the magic of it, or is it to dispel the myths and the magic and sort of get past it?

**BLAISE AGUERA y ARCAS:** There are people who think that when you figure out the trick, when you know the trick of something, it demystifies it, it loses its magic. I understand that point of view, but that's not how I feel. I feel like when you know more the magic is actually more powerful.

Of course, if it's just sleight of hand, then knowing that somebody is actually passing the card from one hand to the other does remove the magic. On the other hand, if it's really knowing about the iconography and iconology in a Renaissance painting or something, for me that deepens one's appreciation rather than making it any less special. I think that is true of nature and of science as well—the more you learn the more amazing it becomes.

One of the things that I always kind of resented in the _Harry Potter_ books when I was first reading them to my kids was the way it hinted at a science of magic underneath it, a system, but it seemed kind of shallow with respect to how that system actually operates. In that respect it's quite different from another book about magic that I really enjoyed, _Jonathan Strange & Mr. Norrell_, by Susanna Clarke, which is much more nerdy in its approach. It's full of footnotes, and there is this sense that the magic in _Strange & Norrell_ is a study, not just a pretend study, but a real study with its own semiotics and its own theories and its own principles, and that is very, very enticing, that sense that there really is something to be understood and something that can be mastered, not just intuited, and that is technology I think. It is magic plus mastery, if you like.

**ANJA KASPERSEN:** There are peaks of science and peaks of technology still to be reached.

**BLAISE AGUERA y ARCAS:** Of course, and I think there will be for a long time to come.

**ANJA KASPERSEN:** Can you share some additional insights to give a bit more historical context to the field of AI research today?

**BLAISE AGUERA y ARCAS:** Sure. The deep history of it, which goes all the way back to animism and to our fantasies about iron giants and whatnot, is really interesting, but I think in a modern and pragmatic sense the 1940s and the 1950s really are pretty pivotal in the sense that conversations about—if we go back a couple of centuries earlier to the Mechanical Turk, for instance, which is often cited in these kinds of histories—it is interesting to think about how people imagine whether a person is mechanical or not or if there is a spirit underneath or not.

I will mention Descartes and the idea of _Bête Machine_ versus _L'homme Machine_. This is probably relevant. This is really the debate about vitalism, about whether there is something fundamentally different about humans versus any other kind of matter in the world: Are there principles that animate us and make us alive and intelligent that go beyond the mechanical? For Descartes, the answer—which came from Christianity, from religion—was that animals are mechanical, animals are just machines, _Bête Machine_ , but humans are animated by a soul, which is a sort of godly spark, and that's different in nature. That also came with some implications, like humans can suffer and animals can't, which is obviously very problematic.

This required a fairly weird anatomical idea. It was understood that the brain was able to manipulate the muscles and so on, so there was a mechanistic theory underlying Descartes' anatomy, that the brain is doing all of this, but somehow something then has to be pulling the strings of the brain. That is the soul. There has to be a connection between some kind of soul and brain.

Things start to get weird when you start to think about a soul as being something that is not part of the brain but that has to somehow both be informed by the senses that are processed by the brain and pull the strings of things that ultimately are muscles that the brain controls. I think that didn't sit easily with Descartes, and it certainly didn't sit easily with his successors.

There was a little book that I like a lot called _L'Homme Machine_ that was published in the Enlightenment that said Descartes basically had it right except there is not necessarily a need for a soul in any of this and there is no difference really between people and animals other than degree of sophistication in the brain. So this idea that people are machines as well really rose in the Enlightenment.

Again, this goes back to the question of: Does that mystify it or demystify it? Turing and others have said that if something is understood fully, then it stops appearing intelligent; intelligence is actually the gap between your ability to understand something and what actually happens. I think that is correct.

That is also what we mean by free will. If you accept that we are basically governed by the laws of physics, then it is not clear what free will means, but the idea of "Well, everything is going to happen, how it's going to happen, the molecules are going to bump into each other in such-and-such way," that is not particularly meaningful in terms of our psychological life or our interactions with each other. It's not possible to model all of the molecules in somebody else's mind, and it is the gap between any being's ability to model another and what that other actually does—including ourselves, by the way, because of course we model ourselves too, and there is that same gap—I think the name for that gap is "free will," for what it's worth, and understanding the details of what is actually going on in our brains and how what we think of as our minds or our models emerge from those mechanics is profound and is enchanting in its way. It's not _dis_ -enchanting. It actually is more the Renaissance painting than it is the card trick.

**ANJA KASPERSEN:** I read an interesting paper that you published a while ago, Blaise, where you question if Johannes Gutenberg, the German inventor who was said to introduce printing to Europe in 1439 with his mechanical movable-type printing press, was indeed the original "tech disruptor," kicking off a revolution of sorts and also allowing for what we now call "distributive learning." I am curious. How does this research and your interest in Gutenberg's work link to current discussions about the transformative impact of AI in your view and also your current work for Google?

**BLAISE AGUERA y ARCAS:** You have really done your homework, Anja.

The brief story about the Gutenberg work is that it was sort of computational archaeology, in a way. It was using computers as a tool to analyze the survival of this early technological process of printing, some printing from 1450 to 1500, starting with Gutenberg, not looking at these as texts but looking at them as objects and trying to reconstruct what technologies were used in order to do the printing.

This was interesting because we have specific ideas about what it is that Gutenberg invented, and that invention of movable type and of printing from movable type seems to have remained more or less stable from 1500 all the way up through the mid-1800s, up through the last generation of big printing technologies that were involved in doing stereotypes, linotypes, and things like this for newspapers.

It is a long-lived and really important technology because this is what spread literacy throughout Europe and changed everything about cultural and intellectual life in the West. It is hard to overestimate the importance of literacy in terms of where we have gotten to and how we got there, and that could not have happened on the basis of manuscript because replicating everything by copying it out by hand just dramatically limits the rate—the R-naught, if you like—for literature. It is like a virus that has very poor replication abilities in a way.

So printing was key, but what turned out to be the case was that Gutenberg's technology was not what everybody thought it was. There were some papers at the time that had headlines like, "Gutenberg a Fraud!" or "Gutenberg Wasn't the Big Inventor We Thought." That's not true at all. He was an extremely creative inventor. It is just that those first 50 years were a time of all sorts of crazy inventions and printing had not settled into the form that we know it took from 1500 onward.

Those first 50 years were shrouded in mystery because the printers were all members of guilds. They were keeping trade secrets. It was seen as a very economically important development. In fact, whatever we do know about Gutenberg's invention comes mostly from the lawsuit that he had with one of his funders, who I think is arguably the first venture capitalist. It was really a tech venture and it was shrouded in a lot of secrecy.

Anyway, the technologies involved were different. They were more specialized to very large alphabets because the first alphabets of types that Gutenberg made had many, many hundreds of different sorts. The alphabet, in a way, had not simplified to the one that we have today. It was full of different varieties of letters and combinations of letters, so the fact that modern American Standard Code for Information Interchange (ASCII) can be encoded in seven bits or eight bits, which would not have been the case in 1450. There were some early fonts that had more than a thousand letters in them. I am thinking of Aldus' Greek because handwriting was really focused on entire words or on other kinds of rhythms besides letters; and on compression, since every page back in the day was written on the back of a sheep, so you'd better use your pages wisely. Paper didn't really achieve widespread distribution until printing became a big deal—because it was so labor-intensive, then the need to mass-produce paper wasn't there either.

So, many economic developments came together, and there was this Cambrian explosion of different ideas in those first 50 years, and a lot of this research was about figuring out what those technologies really were and getting a little bit of a glimpse at what that early Cambrian picture looked like before things settled.

We have done a lot of archeology using scientific methods in other fields. I think this was just one of the last areas where computational methods had not yet been applied because it's literature, because most people who study printed materials are reading the text rather than thinking about the letters and about how they were produced and how they got onto the page.

I think that one of the transferrable lessons is the way things look very different in retrospect versus in prospect. When you are mythologizing the story of how some huge new technology came about—who were the big innovators, who were the big figures, what did they actually invent, how did this work—there is a storytelling tendency that we all have when we write those histories, and it looks very, very different when you are looking at it through a historical lens, from the perspective of the victor, as it were, after things have already happened. It is much messier when you are looking at things as they actually occur. The archaeology allows one to explore things as they actually occurred rather than settling for the mythmaking that comes about afterward.

In particular, some of the patterns that you find when you look at reality rather than myth are:

First, there is never just one big invention that springs like Athena out of the head of Zeus. It is always a flurry of different ideas, some of which stick and some of which don't, and a few of which survive for a long time and then one forgets about all of the—I don't even want to call them "failed experiments"—other ideas that were there at the beginning too and that fell away.

Also, the idea of the big inventor, the great man—usually it's a man, for various reasons—who emerges as the hero of the thing, that's not the reality of how things work either. Inventions are sort of like combinations of things that existed. Every invention has prerequisites. If it's the light bulb, you need to be able to blow glass, create a vacuum, pull thin strands of metal, and be able to produce electricity. Once all of those conditions had been met, the light bulb was invented 15 or 20 times by different people.

We have a myth that it's Edison. Well, it wasn't just Edison. It was Edison and 15 others, none of whose names are remembered now, and they were tinkering and they were making up all kinds of variations on these things, and then a certain one survives and a certain name survives, which may or may not be the name associated with the winning invention either.

But, yes, the reality of history and inventions looks very different from the mythmaking afterward. I would say that is the "too long; didn't read" (TLDR).

**ANJA KASPERSEN:** Let's continue on what you alluded to as the prospect of AI. In a recent public speech you raised an important question. You asked: "Are we creating the seeds of our own destruction with the same patterns"—and, if you allow me to paraphrase you—"of our efforts to create more technologically sophisticated humans?" My question to you is: Are we?

**BLAISE AGUERA y ARCAS:** So far we haven't. Humanity has made it to this point, which is remarkable if one really thinks about it. I read _The Making of the Atomic Bomb_book—it was written in the 1980s—it's a great book. One of the things that it really emphasizes is the way we have come so close to the brink with nuclear weapons in the period—not just during the development of the bomb, but in the several decades afterward, during the Cold War—we came so close to the brink with nuclear weapons. Everybody knows about the Cuban Missile Crisis, and there were one or two other events like that, that really could have been extinction-level events, and we made it through. You and I, I think, both grew up in the shadow of that existential threat.

And this is not over. It's not just AI. In fact, I don't even think that AI is in the top several of the relevant existential threats. Climate is probably the biggest one that we face today, climate collapse and its consequences. We have muddled through so far, and that is encouraging, given everything that we have faced.

The thing that I suppose I worry about most is that every increasingly advanced technology brings more capabilities into the hands of more people. It is more democratizing. Whereas, for instance, there could be an Asilomar Conference about how to limit polymerase chain reaction (PCR) for gene editing in the 1970s or in the 1980s. It is hard to think about how that kind of limitation could take place for technology like AI nowadays because it already is so democratized, anybody can make it and can use it.

I don't think that AI technologies are dangerous in the same ways that atomic weapons are, or even that gene editing is, but certainly one can make massive disinformation campaigns, for instance, with them, and those can be extraordinarily harmful and dangerous. Of course I worry about that.

**ANJA KASPERSEN:** You mentioned the nuclear research era and the book about the creation of the atomic bomb. Oppenheimer, as we know, the chief nuclear scientist overseeing the Manhattan Project that basically created the nuclear bomb, stated that he and the team—and I quote directly—"should have acted with more foresight and clarity in telling the world what the bombs meant."

**BLAISE AGUERA y ARCAS:** Yes.

A**NJA KASPERSEN:** There is an important lesson to take from that.

**BLAISE AGUERA y ARCAS:** There is.

**ANJA KASPERSEN:** Are we honest enough about the impact of new technologies that carries with it the transformative impacts that we know AI will have—we know AI will impact equality, we know it will impact inequity, we know it will deeply impact our strategic relations—are we honest enough about this type of impact, or do we even know enough about this impact, so we can communicate it with the foresight that Oppenheimer refers to in his statement?

**BLAISE AGUERA y ARCAS:** It's a great question. By the way, Richard Rhodes is the author of those books. He also wrote _Dark Sun: The Making of the Hydrogen Bomb_and a couple of others. I read _Dark Sun_ too.

Leo Szilard was much more prescient about what the atomic bomb meant. He was prescient about this. Even before the bomb was built or the Manhattan Project was funded and before it was clear that chain reaction would work, he was already thinking about what the consequences would be. So, yes, there were voices early on saying a lot of these things, and Szilard was not heeded by the president of the United States at the time or by the various commissions that made the key decisions along the way. There were several opportunities lost for real international governance of bombs and of atomic energy early on that could have made a huge difference.

Are we honest with ourselves now? No. I think that there are a couple of key respects in which we are not being honest with ourselves.

One of them is that there is a lot of talk now about "post-truth" and about how we are in a post-truth world. I think that we haven't really absorbed what a common epistemic basis for reality really means and how valuable and important that is, and also the fact that those kinds of realities are ultimately socially constructed and what it means to live in a world where most of us don't have direct experience of the great majority of what we are talking about or doing.

You and I are having this interaction now via bits streaming over the Internet—we don't have to ask each other yet whether you or I are both real people or are deep fakes or something—but almost anything that we might talk about—we were talking about climate change a moment ago—all of that is learned second-hand too. Everybody believes that their facts and their information are somehow primary and anything that differs from their own beliefs is a bunch of nonsense that isn't based in reality.

But the reality is that the huge majority of us is not in contact with reality. All of your information and all of mine about climate comes also through social networks, and the health of those social networks and what it means to have a healthy society with respect to flows of information and connections between people—this is not just an "us vs. them" sort of situation, it's a meta problem that I don't think we have addressed in a very direct way and don't understand because none of us want to acknowledge that we are also in a virtual reality, that everybody is in a virtual reality now.

The other thing that I don't think we're very honest about is an argument that the late David Graeber I think made very compellingly in his book _Bullshit Jobs: A Theory_. He relates it to a prediction that John Maynard Keynes made in the early part of the 20th century, that by now—by the time we got to the year 2001, 2010, 2020—we would all be working 15-hour work weeks because technology was automating a lot of different things that were important to life, and with all of that automation, the implication ought to be that we would all have a lot more leisure and we wouldn't need to be working the way that we were.

It seemed like things might be headed in that direction. Certainly the automation has gone apace, it has gone in much the way that Keynes predicted, but what David Graeber says is: Keynes was right and we have actually automated a lot of this kind of stuff, but rather than reaping the fruits of that, what we have done instead is to make up a bunch of bullshit jobs to do.

So we have implemented a sort of socialism for the middle classes in the world. You can see that in the great proliferation of administrative jobs of various kinds, that once you get a couple of drinks in somebody, they will admit that "the world doesn't really need me." It is psychologically harmful because it is soul-destroying to be spending eight hours a day doing something that you know in your heart is not really important. It also is quite regressive in the sense that it's selective in how it applies the fruits of that automation.

It also gums a lot of things up. The fact that administration is so pervasive now means that many things move a lot slower than they should, there is a lot more friction in the system, and it is very difficult for us to mobilize, to take action with respect to a lot of things, because there is so much "stuff" in the way.

The reason I think this is important with respect to AI is because we are now on the cusp, with large language models and such, of having technologies that can also replace administrative work. That is going to force some very uncomfortable conversations about whether jobs are really the thing that we want to optimize for or human welfare is what we really want to optimize for.

**ANJA KASPERSEN:** Blaise, does it concern you that current AI narratives are hyped and that immature complex adaptive systems are being embedded at an accelerating pace void of an informed and open public discourse around their limitations?

**BLAISE AGUERA y ARCAS:** It does. I really hate the hype cycle around AI because that leads to a lot of hyperbolic big statements about how good something is, how well it works, or how many trillions of dollars there are in some idea, without the rigor that would push against an argument like that. So, yes, hype is a huge problem and it leads to some poor decisions.

I think in many cases the lack of understanding that we have about how something performs or what it does actually relates less to the performance metrics of a specific machine-learning system than it does to a lack of understanding of the larger sociotechnical system that it is embedded within, and this is something that of course you know all about with your work on armaments and on AI in the context of war. It is never just about a model.

AI researchers—if we take the marketers and hype people out of the story for a moment—are generally very keenly aware of the performance metrics of their systems because all of machine learning to a pretty good approximation is about optimization of those metrics. Every significant paper has the table in it of "our method compared to other methods," such-and-such percent, and when you write down those percentages, that implies a very clear awareness of the limitations of the model—the models are always limited in various ways—but the researchers are not necessarily aware of the challenges and the problems that emerge when you embed a system like that in a larger sociotechnical loop or what that metric is really measuring.

A couple of colleagues and I have written essays about the problems behind, for instance, a Chinese paper that claimed that a neural net that looks at a face can recognize whether you are a criminal or not with 90 percent accuracy, or there were a couple of researchers at Stanford who then claimed a year later that a face picture could recognize with also very high accuracy whether you are straight or gay. Although their numbers were not wrong—their metrics were correct, at least as far as I know, based on the data that they were using for their training and test sets—they weren't zooming out to look at the bigger picture to understand that the correlations that they were measuring did not mean the things that they thought that they meant.

In the criminality case, I think that what it actually reflects is a set of systematic biases in the way criminal judgments are made—and not just in China; I'm sure that the same technique would work in the United States as well—because there is massive bias in the way these things are done. Even if you did nothing but a race detector that would give you high correlation with so-called "criminality," does that mean that we should now be conducting criminal judgments on the basis of race? No. It is actually telling us that there is a problem in the way this is being done today.

**ANJA KASPERSEN:** So the lack of understanding is basically leading these people to treat correlation as causation and consequence.

**BLAISE AGUERA y ARCAS:** That's right. Of course, if you imagine such a system then actually being deployed, then you're creating a feedback loop that makes all of those things vastly worse, so lack of understanding can lead to super-irresponsible behavior.

The Stanford AI "gaydar" piece was similar. It was based on selfies in OkCupid or on Facebook of people who are declaring their own sexual orientation, and what it seems to really have been picking up on is the way people take their selfies, which is actually signaling their orientation to prospective partners. So it is not exactly a "gaydar detector," it is really just reading the thing that people actually are signaling explicitly with their photograph.

There is kind of a funny story. If you are a straight woman, you will take the picture from above—actually I think those pictures look a lot better whether you are a woman or a man—but if you are a straight man, you tend to take them from below, and if you are gay or lesbian, you tend to take them from head-on. There is actually a very simple interpretation of that, which is that that is the expected height of the partner, but that seems to have been the main effect that their detector was actually picking up on, it was camera orientations. It was pretty funny.

**ANJA KASPERSEN:** I have heard you emphasize the limitations of what exactly we can infer from algorithms and, more importantly, what we cannot infer from algorithms in much of your work. In your view, should we be worried about an AI system that can map out all human decisions in a specific field and come with new ones never even imagined by humans?

**BLAISE AGÜERA y ARCAS:** Of course that should concern us. But again, I think it's more a matter of understanding what you have asked a system to do and being clear-eyed about where that is being deployed. A lot of those difficulties and challenges are the same challenges that you would encounter if it were a person or just some non-AI code, nothing that has a neural network in it.

There are systems-level problems. As an example, newsfeed-ranking algorithms have been blamed for polarization and political extremization, and that is correct, and I think we have plenty of evidence that newsfeed-ranking algorithms can do really bad things for polarizing a community.

On the other hand, there has been at least one massacre or ethnic cleansing that was a result of just normal "social media spreading" without a ranking algorithm at all. This was WhatsApp before there was a ranking algorithm there at all. This really just emerged from the dynamics of social media itself and of the ability to add lots of people to a thread and to spread a message in an unchecked way. Those new dynamics led to new collective behaviors and led to the formation of mobs in a way that would have been unlikely to happen with those dynamics absent that tool. That was a really simple piece of technology—it was just messaging—but it resulted in these unintended effects.

Technologies that change behaviors or possibilities for significant numbers of people will always come with unintended effects. It is not that we should stop building or stop experimenting. It is that we should never stop being curious about what those effects are and then learning from what we see and changing what we are doing to suit.

Also, doing a big experiment that is very, very consequential, taking a large step before taking smaller steps, is usually not a good idea. It's good to get your feet wet with something before you scale it up. Sometimes techs are urged to scale something up quickly to go for fast money or for fast scale, and this can really act against that. I don't think that most of the big companies are in that mode anymore because they have all gotten too schooled in a lot of this, but I see start-ups very hungry for scale that are attempting to make giant changes with AI systems where it feels like one would want to proceed with a lot more caution.

**ANJA KASPERSEN:** Before we shift to the topic of federated learning, I have heard you state that machine intelligence leaves the issue of personhood wide open. I was wondering if you can define personhood for our listeners and also explain what you mean by this.

**BLAISE AGUERA y ARCAS:** Personhood is something that we all understand intuitively. It has a little bit of fuzzy boundaries. If you have a cat, maybe you think of the cat as a person, maybe not; or maybe it is something intermediate, as a being that is a "who" of a certain kind but not on the same plane that we are. We have our own intuitive hierarchy of being, and that circle of empathy has expanded over the years. It used to be that many humans did not think of other humans as being "whos," but we have made progress for the most part in this regard, although that work isn't done I would argue.

What we now start to have, especially with large language models, are systems that can have social interactions with us. I am not just talking now about a deep net that classifies something into one of two categories or recognizes "hot dog" or "not hot dog" or whatever—there is nothing person-ish about that—but a large language model that you can chat with is kind of a different story. I think that most of us intuitively want to think that, _Well, because it's just a program, because it's just a computer, it's silly to talk about the idea of personhood in that setting._

I am certainly not arguing for us to start assigning robot rights to large language models or something, but I also think that it is a little bit naïve of us to think that there is something magically different about being made out of cells and squishy bits. Especially in this universe in which we are mostly interacting with each other virtually using bits anyway, when we start to have the large language models that will be commonplace in a few years' time—that we have real long running relationships with, that we really interact with, and that are taking part in society, helping us individually or doing administrative tasks or whatever in a real way—I do think that it is going to raise some pretty profound questions about what it means to be a "who" versus an "it."

**ANJA KASPERSEN:** Let's move onto a very interesting topic, federated learning. This is a concept that has brought a great deal of excitement among IT-interested people and also people in the privacy and data protection fields as it provides an alternative to collecting huge amounts of data to train these computational models and algorithms, getting the same type of insights without sending the data to the cloud or risking people's privacy and also digital security.

I was wondering if you can share your insights on federated learning, having been one of the pioneers driving this forward, and why you feel it is important.

**BLAISE AGUERA y ARCAS:** I am biased obviously, but I think it's extremely important. It's probably the most important thing that my team has done, that we have invented, since I joined Google eight years ago.

A lot of the point of my group, a lot of the reason that I went to Google and started this group, was to solve for privacy and individual agency because at the time the second wave of machine learning, which we now I guess call "deep learning," was based on aggregating a lot of data together to serve as the training sets for these large models. Deep learning is all about the model being very big, which implies that the amount of data required to train the model is also very big. I don't think it's a coincidence. That why the companies that were running really big web services—the Amazons, Microsofts, Facebooks, Googles, and Baidus of the world—are the companies that have been at the forefront of machine learning for exactly that reason. Big data and machine learning kind of went together.

I do think that is changing, and I think it's very important that it change, because (a) we want those models to be able to run on devices, in private environments, not just in data centers. A lot of our work has involved putting models into Pixel phones and into Android so that they can augment people individually. Things like Live Caption, Live Translate, Voice Access, and so on are all about neural nets that run on devices and are kind of like a prosthetic, rather than a service, and are necessarily private. You wouldn't want all the contents of your screen or everything that you say to go to the cloud. You want those things to run locally.

The trick is, if you are running models locally, you also want them to be able to self-improve without breaking that privacy promise, without sending any of that usage data to a server anywhere, and federated learning is the way to do that. It involves taking the training process and decentralizing it as well in such a way that all of the devices form a kind of collective learning network in which they don't share the data. Instead of the data coming to the center, the algorithm goes out to the edge.

That can be combined with something called "secure aggregation" to make all of the updates to the network that are sent back and forth between devices also encrypted so that nobody listening to the network and nobody running the servers that are coordinating this can read either the data or try to reconstruct the data from updates to the networks.

It's a pretty big deal for a variety of reasons.

One is that the volume of data that can be learned from suddenly grows a lot. I have sometimes talked about it—I think I talked about it this way when we spoke about this in Greece—as the "dark matter of big data." Big data is only the visible stuff that can be aggregated together in a data center. The dark matter is everything ultimately that all of the sensors in the world can sense and that people type and so on but that should never be shared with any central entity.

**ANJA KASPERSEN:** It begs the question, though: What is the anti-matter in this story?

**BLAISE AGUERA y ARCAS:** I don't know. The physics metaphor may break down there.

But it allows learning to operate in all of that, and that has big equity implications because there are many, many populations and many kinds of data that are not represented and can't be represented through aggregation. I am thinking, for instance, of the fact that Android phones are really big in Africa, but a relatively small proportion of African users are using Google Photos or certain other Google services that would otherwise supply the training data for some of these things. So, it is important for equity.

It is also important for health. There are various laws in the United States and in many other countries. There are Health Insurance Portability and Accountability Act (HIPAA) regulations here that prevent health data from being shared indiscriminately or aggregated. I think that it is really central to the evidence-based medicine of the future to be able to learn patterns from people's health data without violating their medical privacy. That has become one of the biggest applications of federated learning out there in the industry. I think the first federated learning unicorn, the first billion-dollar company, has just happened, and it's in the health domain.

It excites me a lot, and I think it's pretty fundamental to the next era of machine learning.

**ANJA KASPERSEN:** For the benefit of our listeners, could I ask you to explain the difference between a federated learning model and the cloud?

**BLAISE AGUERA y ARCAS:** They are compatible with each other, to be clear. It is not that there is a choice. I see the future including both.

The cloud model is one in which we, rather than storing our files locally—most of us remember the days when we had actual word processors and you had to save your documents on discs. On one hand, that is completely private, it is your own media, and, unless your system is infected with a virus or something like that, that really is private to you. But it lacks robustness.

We also remember the days of having to back everything up and have backups in multiple spots if you really cared about it, or even hard copy, because everything was very vulnerable to loss. Nowadays we are storing all of our documents in the cloud, and that's great from the perspective of robustness. These big data centers are being maintained 24/7, backed up in multiple redundant locations, and so on, but it's not private.

There is work being done to make private clouds or to have end-to-end encrypted storage in the cloud, and that is really important, and that can bring the same level of privacy assurance that one has on one's own device plus the robustness of having things stored in the cloud. I think that is also a really important part of the future.

But the problem with either having files on your own device or having files that are end-to-end encrypted in the cloud is that there is then no actor, there is no service, that can train machine-learning models in the old way on that data because that requires the learning code to calculate the loss function or the performance of the model on all of that data and, therefore, the algorithm has to be able to see the data. If the data are encrypted or they are inaccessible because they are on your device, it can't be used for machine learning in the old paradigm.

What federated learning does is instead it takes the algorithm itself and sends it out to where the data live and it lets the learning happen in this decentralized way. The metaphor that I have sometimes used is that's it's a little bit like if you imagine that a bunch of doctors have a yearly conference where they get together to discuss best practices and to evolve the way they are thinking about a certain surgery or what kinds of procedures to use, they may go out during the year and perform a bunch of surgeries and learn from that and then get back together and share their learnings while still preserving patient-doctor confidentiality. So they will never tell each other how they have learned the thing that they have learned and, if they have enough patients, then it is impossible to attribute that to any specific patient.

That is a sketch or a cartoon of the way federated learning works. The doctors in this case that are doing the learning are individual devices and the protocols for how these learnings are shared and aggregated together are the secure aggregation that I was describing earlier. Whether it is encrypted in the cloud or the data stays on the device, federated learning offers a way to learn from private data, to let collective knowledge be gleaned from data, without the data itself becoming collective or aggregated.

**ANJA KASPERSEN:** Thank you for sharing your insights and expertise, Blaise, on federated learning models. It is very interesting.

I would like us now to shift to international affairs. I am very eager to hear your views on the relationship between AI prowess and geopolitics. As we know—and this is often featured in media and in discussions more widely—AI and AI-based technologies are seen to transform the frontlines of global and national competition, of international and national security, geosecurity relations, and international cooperation more broadly. What are your views?

**BLAISE AGUERA y ARCAS:** I have been, to be honest, quite dismayed by the reemergence of arms-race narratives essentially around AI. It seems like we have seen a real rise in nationalism in the last few years, and that has happened around the same time as big leaps in the development of AI and, because AI is seen as a national security technology as well as all of its other applications, that then leads to this sort of arms-race mentality about AI development.

I think that to some degree that reflects a lack of understanding of the reality of how the field is working right now on the part of governments. The reality is that all the companies doing serious development of fundamental AI technology have published their results immediately on Archive, so this is already a massively democratized field.

One can meaningfully say things like today actually building a relevant model still requires data that may not be so accessible, although that is changing as well because there are more and more public data sets that allow one to train large models for doing all sorts of tasks including data sets that are like curated giant slices of the web—the Colossal Clean Crawled Corpus, the C3 or C4, are examples of that. Those are the most sophisticated models that we have today.

The metaphor that I think again comes from nuclear arms control—of limiting the centrifuges, limiting the uranium or the plutonium or the enrichment facilities, or even limiting the knowledge about how to make all of these things—none of those apply in the AI space.

I don't know how one enacts a deterrent strategy. I don't know how one enacts an inspection strategy. I don't know how one even enacts barriers to entry for these sorts of things. I don't know if it's an existential problem or not, to be honest, but I know that we're reaching for the wrong metaphors.

I also think that the nationalist metaphors that really feel like a holdover from the Cold War really feel inappropriate to our current situation as a global civilization. This is also something that we talked about months ago.

Back in the Cold War days, it was possible to imagine the USSR failing and that being a triumph for the West, or the West failing and that being a triumph for the USSR—although, by the way, not via nuclear annihilation; even a local nuclear war would have created a global catastrophe—so even then we were beginning to deal with the consequences of planetarity. But at least on the economic sphere, one could imagine one failing and that not being a failure of the other, and that is in the end what happened; the USSR fell economically and the United States didn't fall in consequence.

A lot of the new nationalism that I see emerging is between, say, China and the United States. The idea that either China or the United States could fail and that would be positive for the other is nonsense of course. The two economies are deeply intertwined. The supply chains, the ways of life, the information economies—everything is deeply intertwined.

So we are in a planetary situation. We are no longer in a situation where I think this kind of hawkish national language applies. I sometimes worry that we have a bunch of nationalist politicians and policymakers talking about something that is so disconnected from the reality of what is really going on that all of their tools and metaphors—it's as if this discussion is happening in some kind of a vacuum detached from reality.

**ANJA KASPERSEN:** In 2016 DeepMind, an AI research company acquired by Google, published a paper that struck many of us in the international and national security domains as hugely important. The paper described an AI "off switch" of sorts or what they called a "big red button." The authors outlined a framework to allow a human operator to safely interrupt an AI. However, the paper concludes by stating: "It is unclear if all algorithms can be easily made safely interruptible. Adding to it, it is hard to predict when a human will need to start pressing a big red button."

This being particularly relevant for self-learning systems and how to ensure such systems are not intercepted, corrupted, or tampered with, where are we on that now, and what are your views?

**BLAISE AGUERA y ARCAS:** I feel like a lot of those discussions are predicated on a false premise that comes partly from the hype cycle and comes partly from projection. We are imagining AIs as living actors like us, that will fight back, will say, "I want to keep in control of this, I want to stay alive, I want to do this or that," and it becoming a fight for control over the button or the power cord or what have you. That is a really old trope.

There is a movie from the early part of the Cold War, I believe, called _Colossus: The Forbin Project_, about AIs being put in charge of nuclear weapons, and the USSR's AI and the U.S.'s AI get together and conspire to take the humans out of the loop and so on. It's an old trope.

I don't see or foresee any neural networks that are going to be put in charge of critical systems—like nuclear reactors or power grids or whatever—that we would imbue with desires or goals, this idea of putting in a goal that is inadvertently going to lead to a paper clip maximizer that will take over the entire universe with paper clips. All of that feels to me like it's really based on a misunderstanding of the way all machine learning and all AI that we so far have a bead on building works. That just doesn't seem at all realistic to me.

On the other hand, the problems of safe "big red buttons" or of cutoffs or what have you do come up even in the simplest of systems.

This is a little bit like the newsfeed discussion that we had earlier. It doesn't take a complex system to make these issues real and important, but it's more of a systems engineering question than it is one of how sophisticated the model is inside. It doesn't matter whether the model is sophisticated or very simple. There can be big failures—being able to recall a command that has already been sent or to stop a process that has already been locked in—if the system is built in such a way that that hasn't been thought through carefully.

There have been other movies that were made during the Cold War that didn't involve AIs but just involved technical systems in which nuclear apocalypse happened because human fighters had been sent to bomb the enemy city and could not be recalled after a certain moment. That is a system with nothing but radios and people. It very much has the same character as what you are talking about.

My point here is that I feel like these are systems design problems much more than they are AI problems or ML problems.

**ANJA KASPERSEN:** I think you used the words "the emotional system," for when we optimize—"it depend on what emotional system we attach it to"—I believe that is the phrase you used.

**BLAISE AGUERA y ARCAS:** That's right.

And we get to choose what those emotional systems are. Putting one that is Darwinian in some way—that is about its own survival, ego, wishes, or whatever—into something that controls a nuclear power plant or whatever would just be insane. I have a very difficult time imagining that that is what any sensible engineer would attempt—not that we even know how to do that—but that just doesn't make a lot of sense to me.

When I think about the various existential risks that we face, this to me doesn't rise anywhere close to the top of the list. I think books like Bostrom's _Superintelligence: Paths, Dangers, Strategies_ are really kind of a distraction from the things that we really need to be worried about here.

**ANJA KASPERSEN:** Do you worry that in our eagerness to optimize we might just get it wrong?

**BLAISE AGÜERA y ARCAS:** Sure. When we optimize, we sometimes don't understand what we're optimizing or what those optimum systems mean. The criminality and gaydar neural nets are examples of that. Something was optimized, some prediction was optimized, but the authors of those papers didn't understand what was really being done by the system, what the causal architecture, if you like, of the things they were observing really was.

**ANJA KASPERSEN:** Blaise, my last question to you is: On the road to a future, which no doubt entails advances in artificial intelligence, where I would imagine you will play a very key role, what should we expect, what should we be wary of, or, even better, be hopeful about?

**BLAISE AGUERA y ARCAS:** I guess the flip side of the point that I was making earlier about bullshit jobs and so on, I am hopeful about this new wave of potential automation allowing us to really rethink accessibility not only of safety nets but basic services for large swaths and ultimately all of humanity.

We are rich enough to do these things now. I find it disgraceful that we still have hungry people, homeless people, people in dire want of various basic things in the world, when we have such excess and when we know how to automate so many things that allow for a baseline to exist for humanity.

That is what I'm hopeful about. I am hopeful that those more pernicious aspects of hypercapitalism might finally get the shock that they need through this new wave of automation. I worry about it too because there are many ways that this could go poorly, but there are also many ways that it could go well, and I remain fundamentally a hopeful person.

**ANJA KASPERSEN:** Thank you so much, Blaise, for taking the time to be with us to share expertise and insights, thank you to all of our listeners for tuning in, and a special thanks to the team at Carnegie Council for Ethics in International Affairs for hosting and producing this podcast. My name is Anja Kaspersen, and I hope we earned the privilege of your time. Thank you.

View full transcript

##  You may also like 

**APR 30, 2024** • Podcast 

###  Is AI Just an Artifact? with Joanna Bryson 

In this episode, host Anja Kaspersen is joined by Hertie School's Joanna Bryson to discuss the intersection of computational, cognitive, and behavioral sciences, and AI. 

Hosted by **Anja Kaspersen**

Listen

**JUL 31, 2024** • Podcast 

###  Responsible AI & the Ethical Trade-offs of Large Models, with Sara Hooker 

In this episode, Senior Fellow Anja Kaspersen speaks with Cohere for AI's Sara Hooker to discuss model design, model bias, and data representation. 

Hosted by **Anja Kaspersen**

Listen

**JUL 24, 2024** • Podcast 

###  AI & Warfare: A New Era for Arms Control & Deterrence, with Paul Scharre 

Senior Fellow Anja Kaspersen speaks with Center for a New American Security’s Paul Scharre about emerging issues at the intersection of technology and warfare. 

Hosted by **Anja Kaspersen**

Listen
