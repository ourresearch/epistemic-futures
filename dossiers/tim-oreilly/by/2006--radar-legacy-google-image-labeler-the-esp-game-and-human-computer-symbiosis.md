---
title: "Google Image Labeler, the ESP Game, and Human-Computer Symbiosis"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-09-03
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/09/more_on_google_image_labeler.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Google Image Labeler, the ESP Game, and Human-Computer Symbiosis

## Full text

In comments on my previous entry, Stephen Rondeau pointed out that [Google Image Labeler](http://images.google.com/imagelabeler/) appears to be based on the [ESP Game](http://www.espgame.org) developed by Professor [Luis von Ahn](http://www.cs.cmu.edu/~biglou/research.html) of CMU. An anonymous commenter pointed to the video of [Luis von Ahn's tech talk at Google](http://video.google.com/videoplay?docid=-8246463980976635143) on July 26, 2006.

The tech talk was fascinating, both because there was no hint in it that Google was about to announce something based on von Ahn's work -- the talk is all about his previously published games -- and for the actual thought-provoking content, which gives a lot of background on the design of this kind of game, and in general, the idea of harnessing humans to work as program components via games.

Luis started out his talk by looking at Captchas. Most of this was familiar material, although he has a great definition of a Captcha: "A program that can generate and grade tests that most humans can pass, but that current computer programs cannot pass." (This is an interesting variation on the Turing test, in which humans generate and grade tests that most humans can pass, but current computer programs cannot pass. Is there another variation in the future, in which computers generate and grade tests that computers can pass, but humans cannot pass?)

At about 7 minutes into the talk, he makes a staggering assertion about the amount of time spent on casual games: in 2003, 9 billion hours were spent playing solitaire. By comparison, it took only 7 million human hours (6.8 hours of solitaire) to build the Empire State Building, and only 20 million human hours (less than a day of solitaire) to build the Panama Canal. He then states his thesis, "human computation":

> "We're going to consider the human brain as an extremely advanced processor that can solve problems that computers cannot yet solve. Even more, we're going to consider all humanity as an extremely advanced and large scale distributed processing unit that can solve large scale problems that computers cannot yet solve. I claim that the relationship between humans and computers is extremely parasitic.... What I want to advocate for in this talk is a symbiotic relationship, a symbiosis in which humans solve some problems, computers solve others, and together we work to create a better world."

At that point, the audience dissolves in laughter, as the image he's projecting on the screen is [the symbolic waterfall of the Matrix](http://www.calwhite.com/pix/matrix%20001.jpg).

Getting serious again, he talks about how games can be used to harness some of this unused processing power, and goes specifically into how they can be used for labeling images. First, he describes the ESP Game. Two players are paired up, and given the same image to label. When they agree on an label, they are given a new image. Their goal is to type as many possible labels as quickly as possible till the two players find a match. 

Evidence shows that people find this activity to be fun. He says that people have played as long as 15 hours at a stretch, that many people play over 20 hours a week, and that over three years 75,000 players have agreed on over 15 million labels for images. But so far, what he's done is fairly small-scale. (When I logged in to the ESP Game this morning, there were 179 simultaneous players.) With 5000 simultaneous players -- a number found on many popular online gaming sites, he claims it would take about 2 months to label all images on Google images.

He talks also about some of the things he does to make the game fun, a lot of it eerily reminiscent of Kathy Sierra's insights on [Creating Passionate Users](http://headrush.typepad.com/). And I have to say, comparing the ESP Game against Google Image Labeler, I wonder if Google hasn't missed some important points in von Ahn's work. While his implementation is MUCH slower, it's more fun, with sound effects, scoring feedback, and other game features making it much more engaging. He even identifies the partner by login name. (He talks about how people love to play because they feel a really good connection to their partner when they agree on a word. He shows some amazing quotes describing how passionate players are about the game.)

He also talks about how to prevent cheating: They give people test images that have already been labeled, and only store their guesses when it's clear that they are playing fair. And once you have enough images labeled, you can get additional labels by prohibiting labels that have already been used. And of course, you can even implement one player versions of the game, and zero-player versions (in which you get additional matches by re-running the sessions from different player combinations that used the same image.)

But the ESP Game is only one instance of a general class of game that Luis calls "games with a purpose", i.e. games that "run a computation in people's brains rather than in silicon processors." Some of the other games he talked about include:

  * [peekaboom](http://www.peekaboom.org) \- a game for locating objects in images. One player is given an image and a word (the pairing is output from the ESP game); the player clicks on the image, and highlights a small bit to be shown to the other player, who has to guess the word. In the first 4 months, 27 players identified objects in 2.1 million images. The top player has 3.3 million points. (From what I can tell, players get about 100 points per correct answer, plus various bonuses.) Luis points out that once this game generates a large enough data set, it could perhaps be used for training computer vision programs. 
  * [verbosity](http://www.cs.cmu.edu/~biglou/Verbosity.pdf) (pdf). This game collects common-sense facts ("Milk is white", "Milk goes with cereal.") A player is given a word, and fills in a phrase to describe it. The other player is given the word, and has to guess the same descriptive phrase. Luis points out that there have been many AI research projects attempting to build common sense databases like this, but that they haven't figure out to make them fun. (He doesn't mention [Cyc](http://www.cyc.com/) by name, but that's clearly what he has in mind.)

Luis describes peekaboom and verbosity as "asymmetric verification games": Input is given to player 1, whose output is sent to player 2, who has to guess the input given only player 1's output. Once he guesses, this verifies the connection between the output and the input. This is in contrast to the ESP Game, which is a symmetric verification game. But symmetric games work only when there is a constrained list of possible outputs.

All in all, a fascinating talk on a trend that I believe is going to be one of the _most_ important any of us will face. As the symbiosis between humans and computers becomes deeper, and at a larger scale, we're going to see problems that were formerly construed as "hard AI" suddenly broken, not because computers themselves have become intelligent, but because humans and computers have gotten better at working together. We're only at the early stages of harnessing collective intelligence, and we're going to see more and more breakthroughs as creative computer scientists find new areas that they can tackle with [bionic software](http://radar.oreilly.com/tag/bionic).
