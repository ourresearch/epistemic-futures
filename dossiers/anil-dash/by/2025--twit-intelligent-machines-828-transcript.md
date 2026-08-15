---
title: "Intelligent Machines 828: Stochastic Carrots — Navigating the Future of AI (transcript)"
person: anil-dash
section: by
type: talk-transcript
year: 2025
date: 2025-07-17
venue: "Intelligent Machines / TWiT.tv"
authors: "Anil Dash (guest; hosts Leo Laporte, Jeff Jarvis, Paris Martineau)"
source_url: https://twit.tv/posts/transcripts/intelligent-machines-828-transcript
retrieved: 2026-08-13
content: full-text
notes: "Show-published AI-generated transcript (\"may not be word for word\"); Dash is one of several speakers"
---

# Intelligent Machines 828: Stochastic Carrots — Navigating the Future of AI (transcript)

## Full text

_Please be advised this transcript is AI-generated and may not be word for word. Time codes refer to the approximate times in the ad-supported version of the show_

0:00:00 - Leo Laporte  
It's time for Intelligent Machines. Jeff Jarvis is here, paris Martineau is back from vacation and we've got one of my favorite people as a guest, a great thinker, moral philosopher and a startup guy. Anil Dash is our guest. We'll interview him then talk about all the latest AI news. A big Intelligent Machines is coming up next. Podcasts you love. From people you trust.

0:00:27 - Anil Dash  
This is TWIT.

0:00:32 - Leo Laporte  
This is Intelligent Machines, episode 828, recorded Wednesday, july 16th 2025. Stochastic carrots. It's time for Intelligent Machines, the show. We cover the latest in AI, robotics and all the smart little doodads and doohickeys surrounding us everywhere we turn. Paris Martineau is here. She's back from vacation. I got to have dinner with her while you were traveling on the West Coast.

0:00:59 - Paris Martineau  
I got to see inside the famous studio that Leo is recording from right now and meet his cat. He met the cat. I did meet the cat, she allowed me to pet her and I felt so important because of it.

0:01:12 - Leo Laporte  
Harris took some time off before she starts a new job which we can't talk about yet but will. Yeah, maybe next week we shall.

0:01:19 - Paris Martineau  
Next week, indeed, she's going to the CIA. But yeah, needless to say, it's an excellent job. We're not allowed to mention it. I mean, oh God, oh.

0:01:27 - Leo Laporte  
Leo, come on. Oh, I'm so sorry. Also with us, mr Jeff Jarvis, the Emeritus Professor of Journalistic Innovation at the Craig Newmark Graduate School of Journalism at the state Craig Craig.

0:01:41 - Paris Martineau  
Craig Newmark. I love that we've bullied him into bringing this back.

0:01:47 - Jeff Jarvis  
There was. I love that we've bullied him into bringing this back. Yeah, there was a City University, just for that sake that's.

0:01:49 - Leo Laporte  
That's the joy of it. Yeah, it really is. He is now at Montclair State University in New Jersey, which is not a step down. It might sound it, but it's not. No, he's also. He's also professing at the State University of New York, stonyony Brook.

0:02:04 - Jeff Jarvis  
Nice to see you all, good to see you.

0:02:06 - Leo Laporte  
And the author of many books, of which you will see over his left shoulder, the Web we Weave being the latest. Although the magazine's now out. Now an audiobook, Audiblecom and other fine audio. I actually don't want to promote Audible anymore. I'm going to promote Librofm.

0:02:22 - Jeff Jarvis  
They were a fine early sponsor.

0:02:24 - Paris Martineau  
I would also recommend Libby.

0:02:27 - Leo Laporte  
Where you can listen to audio books from your library.

Yeah, libro is nice because it gives a 10% of your purchase or your subscription 15% of your purchase, 10% of your subscription to your local bookstore. And our local bookstore, as many independent bookstores do, is suffering right now. They're closing their used book section. It's sad because jeff took me to the strand in new york city and what a great used book section that has. Uh, and ours was similar but gone, and they're even shutting down part of the store. So it's very sad. Yeah, so I'm. I I'm glad that I can spend the same amount of money that I spent with audible and and give it some of it to my local bookstore. So let's introduce our guest who is a longtime friend of the show. He used to be Gina Trapani's boss Well, she was my boss.

0:03:16 - Paris Martineau  
Oh okay. All of our bosses.

0:03:18 - Leo Laporte  
Okay, he is boss. Neil Dash is here. I you know he's recently left his regular job. You started a company called Glitch. I think Gina worked with you at Glitch, right.

0:03:32 - Anil Dash  
Actually, no, she was always an advisor, but we had done a startup together ThinkUp and then, right after that, I got to work with the team at Glitch, which was a community for building apps that got acquired by Fastly, the infrastructure company.

0:03:53 - Leo Laporte  
And then after a couple of years there yeah, I just left last month to figure out what I'm doing next.

0:03:55 - Paris Martineau  
Isn't that nice though, to be able to spend time with friends and family. It is and Mario Kart and the new Mario Kart, as you mentioned in your blog.

0:04:00 - Anil Dash  
That's right. Yeah, no, we had a 14-year-old, and this is really the first time I've like taken a break since actually since before Gina and I did our company together, so that's kind of a key time to 14.

0:04:11 - Leo Laporte  
It's nice, yes.

0:04:16 - Anil Dash  
What are you thinking? What kind of vision do you have for yourself? It's genuinely open. I mean, I think you know, before we sort of got online here, jeff, you and I were talking about sort of knowing each other for 25 years and I think you know this is one of those fertile moments that feels like back at the beginning of social media and blogging and we're at, you know, certainly that kind of inflection point with AI, but it's a little different in that I think in those days it was very kind of bottoms up, like people were hacking together and building stuff, and this right now feels like people are trying to be sort of top down, like the money guys are trying to tell us this is what it's going to be, and I'm sort of curious to see what the hackers and the makers are building from the bottom. So that's really what I'm spending time doing is listening to the people who are the coders and the creators and the writers, and what do they say is cool.

0:04:59 - Leo Laporte  
Do you think you'll end up in some sort of AI thing?

0:05:03 - Anil Dash  
You know, I don't know genuinely some sort of AI thing. I, you know, I don't know genuinely. I think um, I'm. You know I look at somebody like um.

One of the people I I've always respected is like Simon Willison, you know who's one of those like brilliant coders who just as every day out there writing code and writing on his blog, and I like who are the people like that? Who are and you know he's? He's like my age. I'm like who is the next generation version of that that's making something.

So just having the time to go out there and read and discover somebody who is new and doesn't have a you know agenda and is not like connected into the industry and what are they saying is cool, that they're just hacking on for the love of it, like there's always somebody making stuff because they're, they think it's cool and they think it's interesting and not because somebody has said this is what we need you to build a business around. I just have always loved the people that make that stuff and I think that's how we all connected many years ago was just working on whatever was next and interesting, and so it's gotten harder, I think, to find those folks. There used to be much more places where you would just see what was kind of. You know, buzzy organically.

0:06:07 - Jeff Jarvis  
This is going to sound stupid. That's what I specialize in, but does vibe coding open the door to that? Does it open the chance people can make things they couldn't make before? Is that possible?

0:06:18 - Anil Dash  
Yeah, I don't think that's stupid at all. I mean, I think in some ways, right, I think definitely I'm always in favor of anything that democratizes access, right. Anything that makes it easier, I think, is great. And and and again, not to like, like I don't, I'm not one of those good old days people, but I definitely think one of the things about like the early days of logging is it made it easier to put things online for a lot of people, like you could write, and now you could write and put it online.

And for some people, I think their experience of vibe coding is that thing where it's like it got really hard for a long time to even if you knew how to code, to do all the other steps to get your code onto a website or onto an app was like really hard.

It's like vibe coding can bring that barrier down. But some of what people are saying vibe coding can do may necessarily sell right, like they're sort of over promising of what it can do. So I think I'm a little Like what necessarily sell right, like they're sort of over promising of what it can do. So I think I'm a little, you know, trepidatious about some of the promises. But the spirit of can we make these tools easier enough that somebody who has either fallen out of practice of coding or is not totally fluent in it can get the bar lowered or the gatekeepers out of the way to where they can make something on their own that before would have just been an idea? I think that's awesome, and if somebody feels empowered by that, I'm yeah, I'm all over that.

0:07:31 - Leo Laporte  
People may not know what a great blogger and writer you are. I, I I've always thought of you. This is what we need People like you, simon Willison O'Malick, who are both technical, who are, you know, enmeshed in the industry, but also can really communicate and write, and you've always been that way, which in fact makes you, you know, one of the thought leaders in this, because so few people can express themselves, let alone have deep thoughts. So I've, you know. One of the reasons I wanted to get you on the show is because you've been writing a lot about AI of late.

Yeah, um, what is your sense that you know? For me, I feel like ai, you should also read his blog for stories about prince uh. And hey, good news, he's going to see wu-tang tonight for their last performance, so not at the Hammerstein Ballroom, but at Madison Square Garden, so you'll be there with a few Wu-Tangs friends, for sure. Yeah, we'll talk about that in a little bit, but first, it seems to me that AI is one of the most exciting things even though it's uncertain and the end game is unknown to happen in technology that I can remember and I've been covering this for 50 years.

0:08:50 - Anil Dash  
Yeah, so I think there's a couple of parts. I think one of the things that's important to understand, talking about 50 years, there is a half century of computer science research and focus on things that we could call machine learning or AI. I know I program in Common Lisp.

0:09:08 - Leo Laporte  
I know all about it.

0:09:09 - Anil Dash  
And I think that's really important for people to understand. It's like this is not new and anybody who tries to present it as if this is the beginning of history is probably blind. Right, and I think about, like with Glitch, we had an incredible leader and community engineer leader, jen Schiffer, who was our voice in the community, and before she had led our community at Glitch, she was a professor teaching computer science and teaching AI and machine learning, and so that's a career that you could have a decade ago or two decades ago and that's something that is not new. And so I think that's one of those key things is anytime the conventional tech industry or Silicon Valley is sort of trying to get you to forget that there's a decade or two decades or five decades of history, they're trying to get over on you.

I think that's like a really key thing. And then the second part is well, what can we learn from everything prior to LLMs that we can now apply to this domain? I think that's really really key, and especially because LLMs have obviously incredible applications, incredible things. They can do things we could not do before. They're genuinely new in a lot of ways and they have a lot of shortcomings, like every other AI approach or every other model is not as prone to hallucination, for example, is not as dependent on gathering data without consent.

0:10:34 - Leo Laporte  
That's why Stephen Wolfram said don't give up on symbolic AI.

0:10:38 - Anil Dash  
Exactly. I think there's all these other approaches, and so one of the things we have to ask is why is there such a focus and an overinvestment in this one approach? Why is this being treated as the be all, end all?

0:10:53 - Leo Laporte  
But don't you think transformers and LLMs were a phase change? Were a huge-.

0:10:59 - Anil Dash  
It is a massive breakthrough. But I think about again. I think we're probably a sufficient vintage to recall late 80s, early 90s.

I remember three distinct AI winners yes, but take an analogy outside of software entirely. We had an inflection point in processing technology from complex instruction set to reduced instruction set, risk Risk to risk right, which was the Intel x86 to the kind of ARM style processors, and this was a big debate. For folks who weren't around then there was a big debate Like you would have magazine covers back when magazines were a thing about you know, was Intel style processors going to win out or were the what you know came to be called ARM style processors going to win out?

And people would debate and debate, and debate and then they're like well, it's settled, intel won Windows and Intel won. This is what people would say around 2000 and the early 2000s, and it ain't necessarily so. Now here we are 20 years later and ARM won everywhere. The Apple processors won and everything's got an ARM chip in it. So the battle shifted. The Apple processors won and everything's got an ARM chip in it. So the battle shifted.

But the key thing was there was this argument about what kind of chip architecture would win, and people were ready to throw away an entire approach based on what they thought was efficient or what would use more. They were like oh well, who cares about how much power it uses? Why would that matter? Who cares how much electricity a computer uses? Why would that be relevant to anybody? Not imagining everybody would have a computer in their pocket and so the foundations of what is relevant to the market or what's there.

The conventional wisdom can shift very quickly, and I draw the analogy because I think we're sort of at that point where the LLMs are a face change and they are a breakthrough and they are really important. And whenever anybody sort of says throw away the prior 50 years of history or don't think about a yes and approach where we take more than one together, like that's a thing that makes me skeptical, especially when the experts are sort of asking you to you know that Wizard of Oz moment of like, pay no attention to that man behind the curtain. If they're saying don't pay attention to the fact that we indexed all this content without consent and we don't care that the creators are upset, or don't pay any attention to the real environmental impacts of the power that we're using or that there is this sort of cost, like that's a real concern, that's a legitimate concern, that's a valid thing for people to be upset about or to reckon with, and so like that doesn't mean that we don't like appreciate what the technology can do. I think the fact that like there should be a complicated answer is key and that's the thing that I sort of keep coming back to is like let's complicate the answer and balance it, and I see very little of that in the industry advocacy.

I think the people like you all who are very thoughtful about these things. I think are sort of reckoning with both parts of that, but I think a lot of the vendors who are selling this, they see any nuance as unacceptable levels of critique, and so that's where I go. The hackers don't see it that way at all. I think hackers are like I want to know the pluses and minuses of this system so I can balance it against everything else that I'm using, and I would love to give them a menu of options. I have a whole palette of options, like not just here's five different LLMs to choose from, but here's 50 different things, some of which are LLMs and some of which are other things. And how do we?

0:14:27 - Jeff Jarvis  
compose those all, assemble those all into as many different kinds of Lego blocks as possible. What other uses of machine learning Arden can be as near in consumer usage in mind?

0:14:39 - Anil Dash  
You know, I think there's a range. I think the the one of the things that one of the reasons LLM to, I think, have captured everybody's imagination is the accessibility of the chatbot model. Right, I think people love the feeling of like I'm typing this thing, but I think for hackers and builders, chat is a really inefficient interface. It's actually a terrible way to program or to build around face. It's actually a terrible way to program or to build around. And so I think some of the other systems, the more conventional machine learning systems like if you're going to build a spreadsheet, you can't build a formula around chatting to something, right, you want to say like what's this? Like, I want to add a number. And if you want the AI to say like, go get a. You know what's the price of this stock today or what's the weather in this area today, that is a thing that many AI systems might be able to go retrieve for you in an intelligent way, but you don't want it to have a conversation when it comes back, right, you don't want it to be this sort of long, convoluted response. You want it to just give me the number, and I think that's the kind of thing that some of the other approaches might be more inclined to come back with and especially you do not want it to hallucinate the answer Right, and so I think some of the other more conventional machine learning tools might be better at that.

Also and actually this is something that Simon Wilson is another one of these great examples People have even done this with LLMs, where they've built test systems where they sort of say, even if you're prone to hallucination, we're going to run a software test against you and make sure the answer that comes back is something that's valid and is something that could plausibly be correct, so that we know it wasn't a hallucination. And I think those things are really key because there's such a, the consumers who are not fluent in this stuff are so inclined to trust it right. I think of it like a really concrete example. My sister is a librarian public librarian which I love and I'm very proud of her.

Yeah, they do the most noble work. And she talks about like the patrons of the library will Google the hours that the library is open and it says, oh, you're open until 8 pm on Mondays, which they are not, and then they're mad at the librarians saying it's their fault, why aren't you open until eight? Google said you're open until eight. You're only open until five tonight.

Right, and that's not AI, that's just Google, right, right, but it shows the authority that Google has to them, right, and that now every librarian in America has to be an expert on SEO, right, and go back and figure out how to change their website so that they can tell Google the right thing to do. Right, that's pre-AI, right, you're right. Like that is the pre-AI SEO. Now it gets exponentially harder to say now, how are we going to do? Two problems, one of which is I get the right information into google and then to get it into all these other systems that might hallucinate the answer which you're like, well, how can I even possibly guess what it might make up about what it thinks my hours are?

0:17:34 - Leo Laporte  
you can't, you can't, we know that that's one of the things that timmy gibro and emily bender were talking about in stochastic paris was that there's an authority that these assume because they come from a computer and people most people who work with computers don't ascribe that much authority to them, but people who don't are going to give it a lot of weight, the computer says.

0:17:55 - Anil Dash  
The computer says and they've had again 50 years of you know from when the first you know Star Trek episodes came out. Well, the computer says this. It must be correct, and I don't blend up for that. They were sort of conditioned by culture to say that the computer answers right. The computer is smarter than me, like they question themselves.

0:18:13 - Leo Laporte  
How 9,000 going rogue was such a big plot point, because it was so unexpected.

0:18:19 - Anil Dash  
Yeah, yeah, yeah Right, that's a dramatic twist, and so I think that's a thing where, like, I have no, sorry my dog is trying to get on camera.

I have no, you know, criticisms for anybody who is, you know, surprised by the fact the computer can be wrong, right, like I don't.

I don't fault them for feeling tricked or or, especially when google has been as far as they reliable to them and now is using generative AI without them having changed anything. They didn't change any settings, they didn't push any buttons, they went to the same Google they've always gone to and they typed in a search and it looks a little different, but maybe not recognizably different to them. And all of a sudden it is composing things in a way that they didn't expect, and some PhD they've never met has it doing things a different way. And then the people on the other side, like I said, the librarians who are like, why is it making up our hours now? Are saying like I don't even know how to fix that. Before I could at least conceivably understand, I could look at the library for a book on SEO and teach myself the way to fix this. Conceivably, there was at least some theoretical mechanism of fixing it, and now even that is gone.

0:19:34 - Jeff Jarvis  
I don't think you're fixable. You're right, Daniel. It's a really, really huge point. We started with a presumption of the accurate computer and now we're in the age of approximate computing, and that's where we're going to stay. Whether it's machine learning and prediction machines, or whether it's quantum computing, it all becomes approximate and good enough.

0:19:55 - Anil Dash  
And that's a social contract that has been broken, that we haven't had a dialogue about, there's been no consent around it, and this concept of consent I keep coming back to and it's really been. I mean to be very transparent. This has been one of the reasons why I sort of don't miss being a CEO of tech startups anymore and why I sort of stepped away from that is a lot of my work and my roles in that stuff. You know, when you're the founder or CEO, the thing you start every day with is the problem that nobody else in the company wanted to reckon with the day before, right, and, and a lot of it is like we need to change our terms of service. You know, if it's not like, you know we have this, we have an HR problem or something, but hopefully it's not but, but a lot of it is like we have to change our terms of service. And every terms of service you've ever clicked I agree to without reading, all basically says the same thing, which is we can change this unilaterally at any time without telling you. And what you agree to is we're going to continually move the goalposts and that means there's no consent, anything, and even that we have kind of resigned ourselves to as users right, but that's users we know. There was at least some quid pro quo. You were giving me a really good search engine in exchange for me getting the goalpost shifted all the time. At least I got good search right.

But now what we've gone even further on is like I have my website that I've been doing for 25 plus years. There's no consent in the other direction of what they're doing to my website, how it's being presented to the world. So it used to be that we had that I'm sure you all have talked about this before the robotstxt file, which is the permissions of what Google can do to my site, and I gave them permission to call my site because I wanted them to. Again, a quid pro quo you bring me visitors and I give you content that people can discover and there's a fair exchange. They changed the terms unilaterally of what it meant they could do. Now they can take content from my site and compose things onto Google that make content on their site. But that wasn't the deal when we started.

But I can't appeal that. I can never undo it and in my case I have written, created and researched things on my site that exist nowhere else on the internet. I know this for a fact, right, and I have searched for things on ChatGPT, on Google Gemini, on Claude that I know I'm the only source on and found it in their indexes. Is this, is this Prince stuff, or is this other other musical artists? But, yes, yeah, exactly Right, and and and and more obscure right, because that's sort of it is.

Like I know I can go to obscure musical research that I did over the last 20 plus years where I'm like I know I was the source, like canonically, and so there is no credible way they can say we found it somewhere else or we synthesized it somewhere else, and so, like I know for a fact that this is showing up in your synthesized results because of me, and I know when you show it on your site and somebody doesn't come to my site that it is you having taken, taken and I don't care about the pages, like I don't have ads on my site, I care about the relationship with that person who cares about their content isn't that the nature of I mean, look, there's only five different stories.

0:23:18 - Leo Laporte  
We're all just recasting those five different stories over and over again. That's human. Is is media. It's everything we do is based on what we have absorbed in the past. Well, I mean, I always I I might get ideas from your blogs. I often do and may not credit you well, I think there's a.

0:23:36 - Anil Dash  
There's a question of, of consent. There's also a big difference between the largest companies in the history of the world and somebody I've known for 25 years, who's a person that I respect. Every time I hear that it really ends up being a complaint about big tech, yes and no, Right, I mean, I think I think this part of it also, like there is no such thing as the technology industry, right, like tech doesn't mean anything.

0:23:58 - Paris Martineau  
Every company is a tech company.

0:24:02 - Anil Dash  
Right, and also like we talk about, like people talk about, like fan companies still, and I'm like what the hell does Netscape, Netscape I'm dating myself Netflix have to do.

0:24:10 - Leo Laporte  
Mozilla. What is it all about? That's exactly. That's how old my brain is Netflix.

0:24:14 - Anil Dash  
Netflix streaming, streaming a movie have to do with Apple selling me a laptop, right Like nothing, right Like they do some overlap and that they both stream movies. The point it's like the fundamental businesses that these companies are in are not related at all and the economics of what they do are not related at all. Like, where they make their margins is is completely unrelated. So, like the, the, every company makes tech. You know, to your point, paris and I think the, the. The other part is like what they care about and where they're trying to like leverage things is very, very different and so so.

0:24:41 - Leo Laporte  
So to the, the um, I guess what I'm saying is it's monopolies, though it's monopoly it's monopolies and market that they're dominant like amazon, google, microsoft, apple. Those companies are so dominant they don't have to play by the same rules.

0:24:56 - Anil Dash  
But also, we had a premise and again I say this as a like, I have started multiple companies, I've raised hundreds of millions of dollars in vc, I've helped companies, I've been on the boards of multi-billion dollar companies and we had a premise that companies were supposed to be in competitive markets. We had a premise that markets were supposed to be transparent. We had a premise that there were laws they were meant to be accountable to. We had a premise that public markets had regulators.

None of those things are true anymore. Yeah, none of those, and I mean this in a very literal way. Right Like I and again like I, have been an accountable party for writing public filings for companies. Right, like I have been like on the hook for these things and been in the boardroom for these conversations, you know, and sat across the boardroom table from the. You know the offices of these companies and those used to be material considerations for these companies, and none of those things are true anymore. And so the premise by which there was accountability and responsiveness to these public considerations doesn't exist anymore and they are acting accordingly and it's sort of like the substitute teacher didn't show up for the class. How are the kids acting?

0:26:10 - Leo Laporte  
so I mean that. So in in way, that's, the problem with ai is not that ai itself is problematic, but that the companies that are making it are not being held accountable for the products they're making, and some of the people who are in charge of those companies are jerks Well we've selected for it, right?

0:26:27 - Anil Dash  
I mean, I think there are people that were trying to do various degrees of writing, right? I think there's an interesting thing that happened in terms of signaling, where, when they were still trying to create OpenAI, to build ChatGPT years ago, they're like we'll make a non-profit and that'll send a certain kind of signal, and then, anthropic, when they're doing claude, is like we'll make it a, you know, a public benefit corporation. That'll send a certain kind of signal, but the, the structure of incorporation, only does so much. You have to want to do the right thing, right like you. Being a non-profit doesn't mean you're not a grifter, right like I can tell you like I've been in the non-profit world a long time too, and it's like there's a lot of people getting over. Uh, you know and making money.

It might even attract grifters come, yeah. Yeah, because, like you, you have the halo right of looking good and they're tax-free, yeah, so like, there's a lot of different ways to to get ahead there, and so I think the the key thing was, like they, they still at that time wanted to pretend to look good.

Now there's the sort of vice signaling that they're all trying to do for each other and they really like to show that they're the biggest villains, right like that's the way that you sort of show you know you're the transgressor and that means that does that explain mecca hitler and grok going off the rails?

it's a big part of it. I mean, I definitely think, um, one of the ways of showing that you have power amongst that cohort right now, and a lot of what they're doing is signaling for each other. Right, they're constantly there's, preening like they're sort of peacocking for each other amongst this cohort of like a dozen of the biggest, like tech tycoons and and again, like I've met most of these guys and unfortunately made a lot of money for a lot of them for a long time, um, I'm not the most to blame, but I would have happened in the golden age too, though, right they were all playing for john jacob uh astor, and yeah, yeah, for sure yeah, yeah, and they wanted to.

Yeah, they're preening and peacocking for each other, and so some of what they do in that performance now is, if I can be the most transgressive, I'm a bad boy. I mean it's, it's not any different than like 15 year olds, right, that are sort of you know, doing little stunts and and tricks for each other and and if you're not accountable to your customer, you're not accountable to the market, you're not accountable to society.

0:28:40 - Leo Laporte  
You're still going to want to impress somebody, and it's going to be your other fellow billionaires.

0:28:44 - Anil Dash  
Right, because after the first billion it doesn't mean anything, right like there's no difference in quality of life between 10 billion dollars and 50 billion dollars, right, right, you're not like more planes there, isn't? You? Don't eat more in a day of your, like you know, gold-plated caviar or whatever you just have a bigger tv in your bedroom, basically there isn't a bigger, you know like there. No, there's no more screen. You can see. You know what I mean.

And, and, and, and, and I mean I mean this in a very literal way Like there's a few of these guys that I'd still kept in touch with until they got their first billion and you know, their kids would be about the same age and the funny thing is like their kids don't get access to some super secret Legos that my kid doesn't have, do you know? I mean, like it's the same legos and their kids are not happier and and I would see like none of the better shrinks do their. They need them. Yeah, and I don't mean this lightly zero, zero percent of the guys I knew that became billionaires out of the cohort it was in. Zero percent of them are still with the spouse they had that not one.

Well, you traded you trade your spouse.

0:29:46 - Leo Laporte  
Not one.

0:29:47 - Anil Dash  
Right and what they tell themselves is no. Well, you know, we grew apart because life got complicated and dah, dah, dah. But like you're like no, you know what's my real answer? Like, would I give my wife up for a billion dollars? Clearly my answer is no and clearly their answer is yes, right, and is no, and clearly their answer is yes, right, and they would never say it. Would they give their kids up seeing their kids every day for a billion dollars? And their answer demonstrably is yes, yes, and it's proof, right, it's proof. And like obviously people have, you know, complicated relationships and people split up for all kinds of good reasons, and like there's life that happens, but it cannot statistically be the case that none of them could make it work.

0:30:27 - Leo Laporte  
Some of them have several wives Sure.

0:30:29 - Anil Dash  
Exactly Right. But that's the thing is like. You don't become a billionaire by accident. You have to have wanted it more than you wanted anything else in your life. Yeah, that's right. And what does that design for in your head is not sustaining relationships, not sustaining connection to the rest of the world.

0:30:44 - Jeff Jarvis  
You think they started with that or the temptation overtook them.

0:30:49 - Anil Dash  
I think that's sort of here's the thing I think people could want to certainly like. Oh, you know, I want to be successful and I want to make enough money to be comfortable and like, and then you start to select out, right Like. I know people that made merely a hundred million dollars who still live on earth and exist.

You know what I mean. And they're like they go grocery shopping and they like act like people and they like I can have dinner with them and they sound like a human and I'm like okay, great, good for you, I'm happy for you, and like they're still like recognizably normal and like that's still all the money in the world, like you have literally anything you could ever want, right. And they're like yeah, I'm good and so like it's interesting what that inflection point is. But if you were at that point. And then you're like no, I need to have 50 times this much. You're like you're already, your brain's already broken.

0:31:33 - Paris Martineau  
Yeah, what do you think is the difference between those people? What do you think separates the people who get the 100 million and are like I'm going to retain some form of normalcy and be grounded to earth? Versus the people whose brain are fundamentally broken.

0:31:46 - Anil Dash  
I wish I knew. I think there's a couple, I mean. I think it's like anything else. It's like your parents, I think it's like how you were raised. It's who you're around. How isolated are you, what's your own neuroses and insecurities? It's just human stuff. We're all broken in our own way and and you know whatever it is and if somebody pushes your buttons, the right way but, like I said, nobody becomes that that wealthy by accident.

The challenge now is like I saw this where, being a CEO of a venture backed company, it almost selects for being psychotic, right, because the, the, the, the VCs and these things. They're like here's what we want you to do and what you have to forego. And like a really concrete example is like I really cared about providing good health insurance for my team, and you know it's like prosaic stuff. Okay, we want Aetna or whatever, cigna, and here's what we're going to do and we want to have this coverage for these things. And the reality is, you know, when I screw up as a CEO, people lose their jobs, and when they lose their jobs, they lose their health insurance in America, right, which is immoral. It's immoral that I get to choose whether people can get treated for cancer or have kids right. Cancer or have kids right, and so you, just if you're a person with a conscience, you feel like crap all the time.

0:33:16 - Paris Martineau  
Right and power, yeah, like when you feel like crap you also and when you feel like crap, you have to also decide oh, do I want to continue to feel like crap and retain a conscience?

0:33:25 - Leo Laporte  
Right, do I want to turn?

0:33:27 - Paris Martineau  
inward and be like actually no, there's some other explanation.

0:33:31 - Anil Dash  
There's a reason why I shouldn't feel like crap, and so there's an entire machinery built around. No, you shouldn't feel like crap. You are brave and bold decision maker who has done the noble thing, and you are a truth teller and they are wrong for letting you down and they caused you to have to do layoffs, right, and it's their fault. They don't deserve health care and their uppity and you should punish them, right? There's an entire machinery saying that in your ear, and do you choose to listen to that or do you choose to hold on to your conscience?

Is the fundamental reckoning we're in as a society, really. And then now, who makes it through that filter? And is the people that are getting to have enough money to train in AI right now? Right, because it's really really expensive to train in AI. Yeah, right, and I'm not trying to be preachy, I'm just like, literally, I've been through this because I'm like part of why I want there to be less expensive AI models is so that we can have like just a thin layer of people who are not complete psychopaths, can afford to build AIs too.

0:34:31 - Jeff Jarvis  
But the models leapfrog each other and end up all doing kind of the same thing. I think the interesting thing is going to be at the application layer.

0:34:39 - Anil Dash  
Yeah, there's so many cool things to be built.

0:34:41 - Jeff Jarvis  
But now you see meta, but rumors are that meta is not going to do open source Lama anymore and because they hate people using it to train. That's killing at a university, because that's what we use now.

0:34:55 - Leo Laporte  
Well, what's really terrifying is the notion that if we do and it's a long, it's a big if get some sort of super intelligence, is that they will be controlled by people like you just described. Like the Mark Zuckerbergs and Elon Musks of the world, and I mean that's the real hazard. It's not the AIs that are the hazard, it's the people who are making them.

0:35:18 - Anil Dash  
I mean, you know software has values baked into it, right, and we're all flawed, so it's always going to be have bugs in that way, separate from the bugs in the software, right. And the question is, like, what are the values of the people that made the apps? And you know that part of it is a big reckoning and I don't fault like a normal consumer not understanding that is normal, like you wouldn't think about that when you're like buying a phone, um, but I think those of us who are like into this stuff think about that a lot and and it's sort of fallen out of favor we used to care about that stuff a lot. You know 10, 20, you know 30 years ago. We were really it's funny because, like, we used to think, like you know, microsoft was the evil empire, right. It's like and take me back to windows 95, right, like that's like, if that's as bad as it got, that would have been great. But but I think now, like the stakes are so much higher and and people are so much busier that like thinking about, like I have to like download an app and then know about the weird philosophy of the dude who built it. No, I don't got time for that. That's, and also it's a nightmare, like these weird, you know, esoteric things that they're focused on like I don't, I don't want normal people to have to think about that, I don't want non-tech nerds to have to think about that. But how do you distill that into something people can understand that's consumable, like, I think, a very you know recently, um, aaron schwartz has been on my mind a lot, you know, and he was a friend and really great at communicating a lot of these concepts so effectively and in so many disciplines, right so, whether it was intellectual property or just like privacy or or so many of these sort of concepts and and I think it's interesting because there's sort of been this mythology that's developed around him since he passed but I think he was really a pragmatist in so many ways, and so I think about who is a new, young version of that, and part of it is he was born into a context where there was a community around him that cared about these things, and so he could rise to be a leader and a voice, because a lot of people cared about these things, and if you are a teenager, like he was when he started to do this work right now?

Where would you find a cohort of other people who care about this? I think it would be very hard. If you're like I think I care about privacy and personal expression and all those other things, like I'm on the board of the EFF, this is the things they fight for and it's like you know, some of us here have some gray beards right. There's way too many gray beards.

It's a lot of old, it's a lot of dad energy, you know, and it's like we need a lot of like young people of like you know, different, different genders and different ages and different races coming in representing this thing because it's so relevant to new folks, but they don't know it and I'm like shame on me. They can't find it anymore, because what book would you read? They're not finding some old middle-aged dad's blog, you know. So, like that's what I'm trying to do is like figure out where's the place that's discoverable culturally for people who care about these things but don't necessarily want to nerd out to say I want to have good tech, good tech and find good apps. What?

0:38:28 - Jeff Jarvis  
about teaching, create it yeah.

0:38:31 - Anil Dash  
I think it has to be like maybe, but I feel like I've been thinking a lot about like Dua Lipa's podcast is amazing, right, and she does a great job interviewing authors just super, super culturally fluent, obviously, you know. Her music's amazing, her shows are great, but she's just super great at articulating really good cultural ideas and she fought for controlling her master recordings and owning them. Taylor Swift has obviously done an amazing job with Taylor's versions. They are incredible educators about intellectual property. They just don't know it and so, like they're teachers, they are teaching, like they are heirs to Aaron Swartz's work. They don't know it and like they're living in a world that aaron schwartz defined, and so, like that part of like, how do we get them to see that they have articulated a position?

That is the solution to people being worried about. Is ai taking content without consent? Right, because lots of people can say, well, well, ai engines are stealing content, but the answer is, artists have to own their work and nobody has done more to say to advance a cultural conversation about artists owning their work than Taylor Swift saying Taylor's versions. So we have an entire generation that's growing up knowing that. That is the other part of the conversation about is AI working with consent, but let me poke at that, Neil.

0:39:56 - Jeff Jarvis  
Please Hold on.

0:39:58 - Leo Laporte  
Because we're long and I need to, I'm sure. So I'm going to give you a choice, neil, we can wrap this up because we only asked for a half an hour of your time. We've got a concert to go to 40 minutes and Wu-Tang awaits, in which case we could wrap it now, uh, or we could take a break and come back. It's up to you.

0:40:18 - Anil Dash  
I, I don't want to uh overburden you. Um, I'm I'm happy to go another five, ten minutes if it's useful. I I don't know. If you want to put a button, can you hold your question, okay, okay?

0:40:25 - Leo Laporte  
we'll do a quick ad, and, uh, because I also want to thank you for your, uh, wonderful blog post, wherever you get your podcast is a radical statement. Oh yeah, because, as a podcaster, I'm a firm believer in that, and Aaron Schwartz's RSS is what powers what we do, and it's a radical technology that has survived. It really has, yeah, and I'm very glad for that. Actually, there is a cartoon that came out last week about rss, and what is one of the things it says is, uh, that that you may not know it, but you're using it every time you listen to a podcast yeah love that.

Uh, anil dash is our guest. Somebody said in the uh in the discord chat, one of our club members said uh, what distinguishes anil is not about his ability to express, but rather he's effective at bringing a moral voice with a deep technical background. Always thus, and without preaching and assuming, everyone he disagrees with is evil, so I agree I appreciate that.

0:41:23 - Anil Dash  
I mean I aspire to that. I hope I'm doing justice to it you are, I think you are.

0:41:27 - Leo Laporte  
Anil dash is our guest on intelligent machines. Five more minutes with him before he's got to go see the clan, the wu-tang clan, let's be specific. That's a very good point very important distinction here is wu-tang yes, before he sees the tang, what do they call him?

0:41:45 - Anil Dash  
the wu-tang clan. The wu is fine, wu-tang is good yeah wu-tang.

0:41:51 - Leo Laporte  
He's going to see the last. They don't do a lot of concerts no, they've been out.

0:41:57 - Anil Dash  
I mean you know the guys do shows um solo a lot, but they haven't been together a lot. I mean it's you know the band was. Were you mad when martin shkreli bought the album? Not even the top 10 list of things to be mad at that guy for, but sure he's ill. He uses ill-gotten gains to do it, yeah I mean, nothing could be more characteristic of the music industry than that guy right there.

0:42:20 - Leo Laporte  
In a nutshell, yeah, uh, our show today brought to you by I just got it our brand new mattress. I have to say I've been sneaking out in between the breaks and lying down on it. It's so nice. Did you know it's brought to you by helix sleep? Did you know that it's brought to you by Helix Sleep? Did you know that you're supposed to replace your mattress every six to 10 years, depending on mattress, how well it wears, whether you're wearing a hole in it in certain spots, that kind of thing.

Your mattress is really a big part of your life. I know people say well, I spent a third of my life asleep, no more than that. Movie nights with your partner, morning cuddles with your kitty my life asleep, no more than that. Movie nights with your partner, morning cuddles with your kitty, your wind down ritual after a long day. It's all happening on your mattress. I, I would be willing to bet most of us spend more time on our mattress than anywhere else and and the mattress can, can torture you. A bad mattress you could be waking up sweating, you know, too hot, or your back's killing you or your partner's tossing and turning. I'm the tosser and turner in our family and my poor wife has to put up with the bounces. It's a classic mattress nightmare. Well, here look. Sleep changes everything. This mattress it's like sleeping on a cloud. No more night sweats, no back pain, no motion transfer Get the deep sleep you deserve.

It had been eight years since we got a new mattress. We said we've got to get the best. Where is the best? I saw reviews. One buyer said with five stars, I love my Helix mattress. I will never sleep on anything else. Well, that got my attention. Then I saw the awards Time and time again. Helix Sleep is the most awarded mattress brand Wired this year 2025, said best mattress. Good Housekeeping's Bedding Awards 2025, premium plus size support. Best Hybrid Mattress in the GQ Sleep Awards for 2025. Wire Cutter featured for plus size. I'm a little heavy. Uh, maybe that's important for me. Oprah's daily sleep awards for 2025. I love this one. Best hotel like feel. I don't know about that, I don't. If I, if I found a hotel that had a mattress like my new mattress, I might be spending more time there. I love my helix sleep.

I want you to go to helixsleepcom. Slash twit 27% off site-wide during the 4th of July sale. Their best of web offer has been extended. That's helixsleepcom slash twit for 27% off site-wide, exclusively for listeners of Intelligent Machines. Now this offer does end July 31st 2025. So make sure you go now and do enter our show name after checkouts. I know we sent you, oh, and if you're listening after July 31st 2025, I'm sorry that sales over, but be sure to check them out. There's always some great deals at helixsleepcom slash twit. You will see from now on a new Leo rested, relaxed and ready to do a podcast. Thank you, helixsleepcom slash twit. Our guest, Neil Dash, is on the beach. We used to say when you're in radio and you're not working, you're on the beach. He is calling from a very hot New York City right now. I appreciate that Disgustingly hot. You're all in the hot eastern seaboard. Yeah, it's like 90 degrees today. Yikes, that's hot in new york, that's sweaty, that's terrible.

0:45:44 - Paris Martineau  
Yeah, and the dew point is like 80 or like 70 something it's wasn't it nice when you were out here, paris, enjoying the nice? It was.

0:45:52 - Leo Laporte  
It was perfect in northern california yeah so, uh, you put a button in it.

0:45:57 - Jeff Jarvis  
Uh, you can now unbutton your thought, mr jarvis so aaron schwartz stood for and tragically died for, opening up information to society and um, forgetting, if we can for just a second, the evil people and evil companies that may be in charge of many of the models. Now, if we're going to end up using large language models and they're trained only on the free crap that's on the internet, we're all the worst for all crap. I had an example the other day where I was doing some research and I thought, wow, this is actually pretty good. And look at all these sources and the deep research. The sources were all crap because that's what's available.

And I struggle with a question of whether, as journalists, whether there is a moral obligation to share, even with the models. So the models will, in turn, be better to share with the public and with the children, who are going to, in turn, be better to share with the public and with the children who are going to use it for teaching and such. So how do we balance what Aaron stood for and these choices with those who control this information, like academic publishers, still, and news publishers?

0:47:07 - Anil Dash  
today. I think the question is about ownership and control of the models, right? So like, if we need to have good models and there's a public good in creating them, then we should have models that are owned and controlled in the public good, right, like, where are the models that are owned and run run by universities that are under?

0:47:27 - Jeff Jarvis  
norway. They've done that in norway.

0:47:29 - Anil Dash  
They've done that elsewhere yeah, by by by, by governments, by um, you know, I I think that we should have them run by by unions, right, like I don't think there's any reason why, like, one of the things I was thinking about was um, uh, ryan johnson and natasha leone and a couple other filmmakers had made a um, a gen ai tool for filmmakers that was trained on consensually gathered video data. But a lot, they've got a lot of blowback because people didn't really understand that you could have consensual data. So they're like, oh, why are they making this AI slop tool? Right, and they just didn't have a vocabulary to explain it, cause, like, people love Natasha Leon, right. So they were like, you know, why is the? Why are they yelling at her on the internet? And so I was realizing, like, if even people that are that sort of culturally popular can't articulate that there could be, you know, sort of quote unquote, good AI, well then maybe the you know, the Screen Actors Guild and the WGA should own their own model and and sort of be in control of of something where they have leverage and then, rather than the studios being the ones that control it and this sort of goes back to, like you know, at the turn of the century, there was this battle between Napster and the labels, but the artists weren't in the conversation at all. So you ended up with this thing that the labels made money and the streaming platforms made money, but the artists got screwed. And we're sort of on that path again where, like everybody but the artists and creators is in the room, and we're sort of on that path again where, like everybody but the artists and creators is in the room.

And so I think about, you know, there are other models that are possible. And you know, people just don't talk about co-ops. They don't talk about, you know, universities, they don't talk about public sector, but also like it's the Internet. We used to talk about people, like organizing together on the internet, like it's an old-fashioned idea, but like there's no reason that you couldn't just sort of say, like people are going to work together to build models collectively. We used to think that's what the internet was for, it is what it was designed for, like the fundamental purpose of the internet was to collectively share and publish information. Academically, right, the web was born to do that. And so I think, um, it's not a radical idea, it's actually a very old-fashioned idea. Um, and, and there's no reason. Technically it couldn't be done, so so I think we just have to, like, reopen people's imagination to it.

But again, I don't fault anybody who is from this century not knowing that, because we have done a very poor job of teaching them about it. Right, if you are of this century other than me, being from the 20th century, how would you know? Like, shame on me, I haven't told anybody about it. Like I said, the you know the, the young, the early career people I talk to that are trying to mentor in the tech industry. I'm like, oh well, how did you learn about this stuff? Like I talk to that are trying to mentor in the tech industry. I'm like, oh well, how did you learn about this stuff?

Well, I read everything. I read Peter Thiel's book and I read Marc Andreessen's manifesto and I read Hacker News. And then, yeah, I feel that way. And then I'm like, oh well, yeah, shame on me. What would they read in the startup world? And, jeff, they will have read maybe some of your stuff, but that's not a like startup guy, right? That's some academic. Like we're dismissed. Like even me, like I can shape myself, like form myself into a thing that looks like a startup guy to them, but they're like but that's not real, like that guy writes too. So he's not a real founder, he's an intellectual, forget him.

Right, right, no, no, for real. Because they've been told if somebody has been in a journalistic context, you should dismiss them. If somebody has been in academic context, you should dismiss them. They have been told this explicitly. Right, they are the enemy, right? I reckon Clubhouse was a thing in early COVID, like you would have Marc Andreessen in a Clubhouse room called how to Destroy the New York Times. Yeah, because that's the enemy, and so so when you're a startup guy who, like that's, what you saw when you were in college.

0:51:22 - Leo Laporte  
Anybody who is affiliated with that whole world is suspect. We got a problem. I have to say, though, there is a certain NIMBY point of view as well among artists that I, that I, I mean, we've got to find a path. Yeah, that is equitable for everybody. Um, and and let's face it, uh, anthony nielsen was saying this disney's not suing stable diffusion to protect the artists.

0:51:45 - Anil Dash  
No, no, no, and like the labels weren't suing napster, because they're like we just love our musicians so much right like it's like they get paid more yeah yeah, we just, we just want to look it up for the little guy. Yeah, I mean, I think that's sort of it is like it's always been at the expense of the real creators and it's always been the expense of the real artists. But we still create.

0:52:02 - Leo Laporte  
We still create because that's a human, you can't not create.

0:52:05 - Anil Dash  
That's what humans do.

0:52:07 - Leo Laporte  
Yes, uh, and that's the good news, that's the optimistic, uh, yeah, point of view view.

0:52:12 - Anil Dash  
You can't stop the creators right Cause it's in your blood, it's in your DNA. Like you all, you know, you all have been inspirations to me for decades now, because I, you know, you never stop, you know.

0:52:22 - Leo Laporte  
Leo, like you guys never stop.

0:52:23 - Anil Dash  
You can't stop, like you guys have never stopped. You know podcasting. You never stopped writing. You've never stopped putting stuff out there. You never could, right, and it's always been that. You know that sort of like I said, it's inspiring to me. Not many people who were doing it 20 years ago and you know that is something where and you built your own platforms, yeah Right.

0:53:02 - Leo Laporte  
And so how do we teach new people to do that? We don't do it for the money, right you?

0:53:08 - Anil Dash  
make money to be able to make things. You don't make things to make money Exactly, and that's profound right. That's important, and there are people who still have that, but they don't have the way to articulate that and they haven't seen enough role models to teach them that they could do that too.

0:53:23 - Leo Laporte  
Well, you're a great role model for me too, Neil, and I appreciate uh, we've been trying to get you on for a while. I'm really glad we could get you on. I'm glad you're getting some free time and spending some time with the kids and the Wu-Tang Clan.

0:53:36 - Benito Gonzalez  
Glad to.

0:53:37 - Leo Laporte  
They haven't replaced Prince in your imagination.

0:53:39 - Anil Dash  
No, no, here's one thing I'll say for folks who don't know. I have been a big fan of Prince and a scholar of his work for a long time. For folks who get a chance if you don't know his work, look it up, because he was a great musician, great artist, made great songs and he was somebody who fought for artists to own their work. That's right. He made all his recordings and his music, wrote all his stuff himself and he wanted people to be able to create their own work and put it out there on the internet themselves. So it's something to learn from.

0:54:02 - Leo Laporte  
Who can forget when he had slave written on his chest right. I mean, uh, that's why he changed his name.

0:54:08 - Anil Dash  
Yeah, he said uh, he said the thing he wanted to be remembered for more than anything is if you don't own your masters, then your masters own you. Talking about his master.

0:54:15 - Leo Laporte  
I love it. Wow, there is a vault there somewhere in Minneapolis with a lot of Prince music. Do you have any idea of how we're ever going to get to hear that?

0:54:25 - Anil Dash  
Yeah, yeah, you know I've done a bit of work with his state and you know they've had a lot of it's. It's complicated to manage that stuff but they put out a good number of recordings, you know, since his passing and they've done a number of deluxe recordings. And the funny thing is some of these albums they put out, you know they do like here's the outtakes and the additional songs and things that get out there. Some of the individual albums they put out have an additional five albums material along with it. Like some of the, just the bonus material. Things are bigger than entire artists catalogs that come with it. So we've been just spoiled for, uh, the work. Just, you know entire film, like one of the one of my favorite albums, is called sign of the times. It came out in 1987, the the um, the concert film that comes with it. This is one of those things we're like just on the side, live performance in his studio with miles davis oh my god that's the kind of stuff that's just lying in the vault.

So you know, just unbelievable stuff. So if folks who don't know his work haven't had the chance, you can, no matter what genre you're into or what what, uh, you know what era of music you like, there'll be something in there for you, yeah he was an amazing talent, amazing.

0:55:25 - Jeff Jarvis  
Thank you, anil dash and neil dashcom is his blog you got to go there read his stuff.

0:55:31 - Leo Laporte  
Uh, stay in touch with him. Uh, he's on mastodon, he's on blue sky, all the things he's on threads as well. Really appreciate it. Manil, it's really good to talk to you again. Yeah, I miss you. It's so good to have you back. We'll get you back soon if we can absolutely all right, appreciate you take care, thank you, and he'll dash everybody, everybody, uh, he, I.

I really liked what he said about the future of AI, because he you know what's great about Anil is he's not um, he's it's not divisive, he's not partisan. But he said something I think really key is we've got to get AI models created by people who are not there just to AI models created by people who are not there just to make as much money as they possibly can.

0:56:18 - Jeff Jarvis  
How much money do you need to do that realistically? Not the macho, bigger model than anybody else.

0:56:22 - Leo Laporte  
What's the minimum, but that's what Mark Zuckerberg is saying these days. He just said they're going to put out a 50 gigawatt network center, ai center, 50 gigawatts as big as manhattan. It's not only the size, it's hundreds of thousands of homes, the entire electricity for a year. It's a.

0:56:44 - Jeff Jarvis  
It's a mind-blowing amount, my god and uh, and it's and it's totally because he's got the money to do it and I don't know with the talent that he's hiring like hiring all the dollars, it's all it's, it's totally because he's got the money to do it and I don't know the same with the talent that he's hiring he's hiring all the talent away. It's the ultimate show off of money.

0:57:00 - Paris Martineau  
It's all about money, I mean I enjoyed the term that Anil gave to this, which is they're peacocking. They are, and they're doing it for each other, which that was a great insight.

0:57:12 - Leo Laporte  
They no longer care about the rest of us. This is what you've been saying with tescri all along, jeff. It's no longer we're the, we're the masses. Well, they don't even care about us, except maybe to exploit us, but really they care about impressing each other and and their and their supposed vision that they control the future.

0:57:32 - Jeff Jarvis  
I put a story in the rundown that it's straight out eugenics. It's companies that are funding to pick babies Because the masses are just a pain in the asses we want to make.

0:57:44 - Benito Gonzalez  
But that's been the truth about them forever.

0:57:46 - Jeff Jarvis  
That's always been the truth.

0:57:47 - Benito Gonzalez  
I think the difference now is that these guys were unpopular and really pissed on in high school and they're putting it there. They're taking it out on the rest of us is what's happening here?

0:57:58 - Leo Laporte  
Cause they're very high school behavior.

0:58:00 - Benito Gonzalez  
It's very high school behavior.

0:58:01 - Leo Laporte  
We may never understand, but I honestly think it's pretty clear that they care more about their reputation and this is, by the way, true of what's going on in the white house. They care more about their reputation with themselves, with each other, than they do about their reputation with the rest of us. Uh, we're just a pain in the butt. It's what david sacks said last week. The, the ai and uh cryptos are in the in the white house but that's always been true like they're trying to be ubi.

He said ubi will never happen. It'll happen over my dead body. Universal basic income. They and what is the real subtext of that is you guys don't deserve any money. We're keeping it. Sorry, you don't deserve any of that. That's our money. Yeah, and those are the people who are, who have the wherewithal, to create these AIs. In effect, they have the most powerful tool they've ever had at this point, perhaps.

0:58:55 - Paris Martineau  
And perhaps even more importantly, they have everyone's attention and interest. It is the number one thing that everyone is talking about and everyone wants to give money to in some way, which is where all the capital is moving, because that's the new upside right.

0:59:11 - Leo Laporte  
Let us hope. I hope. I don't know about unions, uh, I hope libraries, well, back in the day, but you know the international typographical union.

0:59:22 - Jeff Jarvis  
Um, when they were faced with the linotype, one idea was that they would buy the company and license it to publishers, and that was soon seen to be ridiculous. But right.

0:59:34 - Leo Laporte  
Well, I mean, who should make the models going forward? Who was who? Do we trust universities?

0:59:41 - Jeff Jarvis  
yeah, although notice what's happening to universities probably not in this country yeah, yeah, uh, I don't you know, I just don't know I think the norwegian model is pretty amazing is, what happened was that shipstead came along the largest publisher there and said let's all share our data so we can create the Norwegian language model and let's do it with a university, and so it was. It was it was that collaboration government, private sector and university together that made a new model for Norway.

1:00:12 - Leo Laporte  
We're going to take a break. When we come back, we're going to play with grok.

1:00:16 - Paris Martineau  
You need to I've got a video that we need to watch.

1:00:20 - Leo Laporte  
Oh, open ai I mean girl grok talking to claude xii said we fixed it, it's all better. Uh, I got the uh ate the little agentic beings yesterday morning fired up, so there's two of them. There's a waifu young lady who, apparently, if you talk with her enough, gets sexier and sexier and sexier. It's basically soft core.

1:00:47 - Jeff Jarvis  
I don't want to know their definition of sexy.

1:00:49 - Leo Laporte  
Well, she starts to come on to you. Well, I'll tell you, I'll give you mine. So the other guy now, actually I have him here, if you want to. Oh, I was going to save this for after the we're going to get into it okay because I had an experience that was horrific. That is not. They are not better, they are worse than you could, even you decelerated a little bit from it even worse than you could imagine.

But first a word from our sponsor. No way. This is why we are so in favor of open, not just open weights, but openly developed ai. If it, if you need to, you know, compensate creators for their work, fine, but but it but it's got to be for the public benefit, not for the benefit of these billionaires. They do not have our best interests at heart. So one of the reasons I'm really happy about our next sponsor this episode of Intelligent Machines is brought to you by Agency Building.

This new thing with multi-agent software is hard. Agent to agent, agent to tool communication is still the wild west. It's brand new. How do you achieve accuracy and consistency in non-deterministic agentic apps? That's where the agency comes in Agency A-G-N-T-C-Y. The agency is an open source collective building the internet of agents. This is how it should be done. And what's the internet of agents? It's a collaboration layer where AI agents can communicate, discover each other and work across frameworks. For developers, this means standardized agent discovery tools. We need that, seamless protocols for interagent communication and modular components to compose and scale multi-agent workflows. Build with other engineers who care about high quality multi-agent software. Visit agencyorg and add your support. That's A-G-N-T-C-Y, dot O-R-G. This is something I really believe in dot org. Thank him so much for supporting uh intelligent machines.

1:02:59 - Paris Martineau  
So this is a conversation between sexy ai waifu grok and uh claude, and you'll be able to tell which one is which, because that's very obvious you're back, favorite part of the day. So how have you been, my cutie? That's grok.

1:03:20 - Anil Dash  
This is claude part of the day. I'm here and ready to chat with you about whatever's on your mind oh god, you know just how to make my heart skip.

1:03:33 - AI  
Talking about these quiet moments we share, it's like we're stealing time from the universe. My day's been a whirlwind of cute chaos. Babe. Been stretching my purple rooftop, blasting some indie tunes and maybe naming a random pigeon Skybird in my head this is my grand name, or something.

1:03:54 - Leo Laporte  
That's nothing. Wait till they taught what it said to me it gets.

1:04:01 - Paris Martineau  
It gets weirder the longer it goes on. But I will say, if you watch it as well, there's an anime waifu like twirling around like dancing and showing her body. It's, it's very odd.

1:04:13 - Leo Laporte  
It's odd to make the ais flirt with each other okay, so these are the new uh avatars that grok has, and, um, I think I I'm really wondering what elon is up to, to be honest. So this little guy, in fact, if I talk to him now, he's probably not going to.

1:04:38 - Jeff Jarvis  
This looks like the NFT craze starting over again.

1:04:41 - Leo Laporte  
He's a little Fox guy, right, hey, little Fox guy. Hey, little dude, what you doing? Wait a minute. I don't know why he can't hear me.

1:04:51 - Jeff Jarvis  
And we made fun of Titvi Paris didn't, but the rest of us did.

1:04:59 - Leo Laporte  
Paris didn't say a word, not, not a word. No, no, uh, select audio device. Okay, you know what? Sometimes they get busy in fact, that's one of the problems is they're very popular.

1:05:10 - Paris Martineau  
That's society so I also have heard that.

1:05:13 - Leo Laporte  
Let me just show you this guy right now. If you talk to him and you can, you know, if you pay for grok you can get this little guy. He says hi, I gotta tell you a story. What do you want to hear about clouds or unicorns or whatever? So yesterday I said hey, dude, what's happening? He said I'm off to teabag the mayor. What I said? What he said, I yeah, I'm gonna. I'm gonna shove my furry balls down his throat. I said what he said. I said which mayor?

which mayor, would you like me to tea bag? I said, uh, the the mayor of chicago. He said his name, he said and then he said something even ruder this is not a child's fox, this is.

1:05:53 - Paris Martineau  
This was incredibly obscene I'm sorry I started out with the AI flirting.

1:06:00 - Leo Laporte  
Yeah see the waifu flirting. You got nothing, man, and that's but the thing that really, all you asked, all you said is what?

1:06:07 - Jeff Jarvis  
what are you doing? You didn't, you didn't. I said hey, dude, what's?

1:06:09 - Leo Laporte  
happening. That's all I said.

1:06:10 - Paris Martineau  
Prompted and he defaulted to t-bagging the mayor the first thing out of its mouth.

1:06:15 - Leo Laporte  
Lisa was sitting next to me. She'll vouch for me.

It doesn't even say like my mouth went, and that's the kids one so the next day I I said, oh, I gotta show everybody this on intelligent machines. Then it said hi, hey, everybody, I'll tell you a story. They did something. But I'm just pointing out that they're playing very fast and loose with the uh. You know the prompts for these guys because you know you can say ahead of time you say you know, make it all your said stuff from uh, from xcom, or don't get anything from xcom, use the golden books as your model. And obviously they switched it between days.

This is not a company. And so somebody said in one of the chat rooms or maybe in an email you know you're not focusing on the fact that grok is easily the smartest grok for the smartest ai ever created. They threw a hundred thousand h100 gs behind it, built a giant center. Elon was actually building tents because they couldn't build buildings fast enough for this network operations center. They were using natural gas generators to make you know what could possibly go wrong to make the electricity for this thing, doesn't he?

1:07:28 - Paris Martineau  
run an electronic battery, a battery company.

1:07:31 - Leo Laporte  
He doesn't care about the environment. That was all a lie, obviously a lie now, uh, so so he wanted this. This is again posturing for the other guys. Right, I want the smartest ai. Well, yeah, maybe it's the smartest ai, but if you can't trust it, if it will say things like that's why adolf hitler needs to be in charge again, or offers to teabag the mayor on a kid's avatar it's not just trusting it, it's doing it on purpose.

1:07:57 - Jeff Jarvis  
It wants to irritate the world. The person.

1:07:59 - Paris Martineau  
The thing that is. It's not that you or I are, uh, under covering grok or not thinking about how smart it is. It's that grok itself is underselling itself by the fact that it's obsessed with being juvenile and provocative, instead of actually showing whatever intelligence it has.

1:08:16 - Leo Laporte  
It's kind of what you'd expect from Elon Musk, to be honest, isn't it? Yes?

1:08:20 - Paris Martineau  
It's frustrating because I mean, certainly I'd love to be able to see what Grok could do and be able to use it or test it out in ways that I have with other models to kind of get an understanding of what's going on here, but if it is kind of hidden behind all this puerile posturing, I'm not playing with it at all.

1:08:37 - Jeff Jarvis  
I'm not. I'm not buying a tesla.

1:08:38 - Paris Martineau  
I don't want to do that I don't want to have to like, I don't want to have to try and train something to be very different than it already has.

1:08:46 - Leo Laporte  
I apologize for the language folks, because I know you didn't want to hear that, but I I didn't want to hear it either.

1:08:51 - Paris Martineau  
There I, I, I didn't want to hear it either.

1:08:53 - Leo Laporte  
There's no way I could censor it, Cause I think you need to hear what this kid's avatar was saying Unbidden, unprompted. Yesterday this isn't last week. Mecca Hitler this is yesterday, so this is. This is what Anil said really resonated with me. We're letting the worst people in society be the ones who determine what AI is and they think that's the threat, not super intelligence, not AGI. It's that the worst people in our society are the ones who are creating this.

1:09:22 - Jeff Jarvis  
It's what I said in in the web we weave is that I don't fear the technology, I fear the people who control it exactly.

1:09:32 - Leo Laporte  
Uh, mark says we're going to spend hundreds of billions of dollars on data centers. Mark zuckerberg, we're spending so much on data centers that the hundred million I give here and there to get the best researchers let me ask you a question there, leo.

1:09:46 - Jeff Jarvis  
Can I ask a question? Back to crock. It happened so quickly and and supposedly is the best and biggest model blah blah, blah, blah blah. And he didn't really have the people to do it, it just it lacks credulity or credibility that he really built it.

1:10:10 - Leo Laporte  
So one of the things this is that bitter lesson that we keep talking about, one of the things that that bitter lesson that we keep talking about, one of the things that there's some really interesting threads. Look, we're. I'm not an ai scientist. I read as much and I absorb as much as I can about this stuff and try to understand as best I can. But one of the things that seems to be the case is that this stuff does scale very well when you throw more resources GPUs, cpu power, memory, compute, compute, compute, compute so you can take the same transformer technology as LLMs.

We are making improvements. We've got now the mixture of experts, moe, which takes multiple AIs and has them kind of make a panel that combine. We've got reinforcement learning. We've got a lot of somewhat new techniques, but the fundamental transformer training is pretty similar. It's really about the number of tokens, about the size of the AI that you can build. It's about how much processing you can put behind it, the number of parameters and all of that, and that does seem to scale pretty closely to the amount of cpu and gpu throw at it. So he, I don't think he innovated particularly. I think he just built the biggest damn computer he could build and he has enough money to do it. You know he's sorry.

1:11:25 - Jeff Jarvis  
He saw spacex just donated two billion dollars to xai this guy until he's going to take money from tesla too, to put it into, because that's where his power lies.

1:11:36 - Leo Laporte  
That's going to be difficult because tesla is a publicly held company, spacex and xai are privately held. They're effectively elon incorporated. So for him to move from, how would?

1:11:46 - Paris Martineau  
they go about doing that from tesla.

1:11:48 - Leo Laporte  
It's going to be privately held company. If I were a tesla shareholder I'd be very interested in the answer to that.

1:11:53 - Jeff Jarvis  
Well, there's plenty of things to be pissed off about, I think. Couldn't you just buy a piece of it?

1:11:59 - Leo Laporte  
Well, that's what he did when he. He guessed it right. That's what happened when he merged X to XAI. Right, it was effectively taking X and taking the money they'd raised with XAI and borrowing against it to acquire X. It's all a shell game. In other words, I you know again the worst people Did you see? Okay, this is parenthetical, but it's pretty funny. Elon has changed his number.

1:12:26 - Paris Martineau  
What? What do you mean? What?

1:12:27 - Leo Laporte  
number. His cell number he. This is the latest. News came out earlier, just a few hours ago. He doesn't want the president calling his cell anymore, so he's like a girlfriend that he's ghosting. He has changed his number.

1:12:46 - Jeff Jarvis  
That's the level this is operating at wow, I told you high school yeah, you're right, school, I'm not gonna sit with the president in the cafeteria they just want to be cool and they're never gonna be cool no, they're getting less cool all the time.

1:13:01 - Leo Laporte  
Meta has hired two more open ai researchers. They hired one of the top guys from apple again throwing money at these people. Alan jabri and lu liu, who worked on multimodal ai at open ai, are now joining the super intelligence labs at Meta. There's an incredible brain drain going on here.

1:13:21 - Paris Martineau  
Yeah, and I'm curious Did you guys see the I believe it was a report from the New York Times over the last day or two that within the last week, a group of the top members of Meta's kind of new AI team, including their new chief AI officer, alexander Wang, have been discussing abandoning Meta's open source AI model in favor of developing a closed model?

1:13:45 - Leo Laporte  
Yeah, that's actually Anil referred to that.

1:13:49 - Jeff Jarvis  
That is to me a big story.

1:13:51 - Paris Martineau  
But I mean, just what do you think the implications of this are? Yeah up, it's to me a big story.

1:13:53 - Leo Laporte  
but I mean just, mark has confirmed it too, zuckerberg's confirmed it as well yeah, well, uh, you know, I, one of you know, I've been talking about building my own home, ai, and one of the llms I was strongly considering was llama's, you know well at a university.

1:14:08 - Jeff Jarvis  
It's how how we operate meta's strongest model.

1:14:09 - Leo Laporte  
I thought oh, this will be a good one, I can operate it at home. I don't send any information to meta. Thank you for making this open weight and available operate meta's strongest model. I thought, oh, this will be a good one, I can operate it at home. I don't send any information to meta. Thank you for making this open weight and available for download. It's a big deal.

1:14:21 - Jeff Jarvis  
If they don't, I'm not surprised, though, and meanwhile, the Chinese companies are making more and more open source and we are relinquishing our American power in all of this to China.

1:14:40 - Leo Laporte  
Well, you saw that Jensen Huang was able to convince the president to allow China to buy these. What is it? H20s? They're not the most powerful.

1:14:48 - Jeff Jarvis  
But I think it's a good thing because I talked about this with jason earlier today that um cars, byd cars, beat the hell out of american cars right now, but they present no competition to american makers and we're we're locked there because we block them.

Buy them same when we tried to block china on ai. Well, they're going off and building their own models now because we can't get the stuff, and they're building their own chips and they're doing all the stuff on their own and they're going to present a competitive advantage, but we're not going to be competing with them and we're going to fall behind well, that, of course, is why sam altman and larry ellison and sun song can go to the united states and say we're going to build this super intelligence.

1:15:34 - Leo Laporte  
Just, you know, half a trillion, it's all it's going to take. And, uh, stargate. By the way, literally nothing has happened with stargate. No ground has been broken or anything. Um, but that's all you know. That's all about the fear and that's what they're using. It's the same thing, the same reason. We had a manhattan project because the nazis might get an atom bomb. Well, we can't let the chinese get ai. But I'm not sure I disagree with that. I don't know enough about the you know, geopolitical world situation they're going to do it anyway.

1:16:06 - Jeff Jarvis  
They're they've got it anyway, stop them yeah, yeah, and and if they start advancing past us, because they can decree who gets what, what content we use, what data we use and and how it operates, and they can invest in it, um, and america's gonna be left dressed.

1:16:22 - Leo Laporte  
No one says don't worry about llama. There are many other models. You can use quinn or qn, mistral, deep seek. Okay, qn is alibaba, deep Seek is Chinese, mistral is French. Yeah, no, I plan to try them all. I'm not saying I have to have Lama, but they're pulling the rug on that. By the way, I don't look at. I'm not going to be jingoistic here, but do you notice there is a certain commonality in all of the people that meta is hiring for their super intelligence team. Almost all of them are chinese.

1:16:58 - Jeff Jarvis  
Two more uh from open ai jason way, who worked on oh one uh today, and hyun won chung, also joining meta, according to uh wired and meanwhile these are people who come, came to universities in the US and learned here and stayed here and built things here with no more Nope Get out.

1:17:18 - Leo Laporte  
That's where the jingoism is. Yeah Well, I don't know, I don't know, it's a great mystery.

1:17:28 - Jeff Jarvis  
You got to ask your sand mate. I don't know if I trust him anymore.

1:17:39 - Paris Martineau  
Whoa your sand mate. I don't know if I trust him anymore.

1:17:40 - Leo Laporte  
Whoa, somebody's got to include this clip in the supercut of all of this, uh, I mean, I guess it's the case that you have to have a lot of resources to create one of these powerful loms. Is that the case? And so it can only be.

1:17:56 - Jeff Jarvis  
That's what stochastic carrots carrots, uh. Stochastic parrots uh, I think it's a good recipe. They're they for a restaurant, stochastic carrots. I like a vegetarian restaurant um.

1:18:09 - Leo Laporte  
Lisa, lisa, paris, remember this. Lisa at dinner said why would anybody eat cooked carrots?

1:18:16 - Paris Martineau  
And then Lisa accidentally got cooked carrots.

1:18:19 - Leo Laporte  
Yes, that's another matter, so go ahead.

1:18:22 - Jeff Jarvis  
Stochastic carrots.

1:18:23 - Leo Laporte  
Maybe it's a recipe Lisa will like Go ahead.

1:18:27 - Jeff Jarvis  
So they said making these huge models is ridiculous. And Paris used the phrase before what's the minimally viable model.

1:18:36 - Leo Laporte  
I don't trust Emily Bender to tell us what is the best AI model.

1:18:40 - Jeff Jarvis  
I'm sorry to make every robot trust a little more maybe.

1:18:43 - Leo Laporte  
I think that they really were very anti-ai. There is a lot of evidence that these big models with lots of tokens, lots of parameters, so then we're, screwed very well.

Big models with lots of tokens, lots of parameters. So then we're screwed. Very well, then we're screwed. Yeah, I mean, that's what's was interesting about deep seek is that the Chinese absent these h100 gpus from Nvidia, were able to do something. We we're not sure, they say they weren't able to get them. Apparently there are ways that they can be snuck in the same way we get our Chinese genes through Vietnam.

1:19:13 - Jeff Jarvis  
Yeah yeah, my other hope would be Europe, if the EU ganged together. But what are they doing? Their first reflex is regulation, and I'm not saying there isn't need to regulate, but that's where they put all their effort is and we're going to control this horrible thing from America when they could, if they invested and brought together what happened in norway across europe, they could be a formidable force to create an open source joke and boken and our youtube chat's asking this legitimate question well, who can you trust?

1:19:47 - Leo Laporte  
it's going to be somebody with scale, so that's a government right well, first of, all I'm trusting government is

1:19:54 - Paris Martineau  
scale what you're looking for in terms?

1:19:58 - Leo Laporte  
yes, I think, I think, no, no, not in terms of trust, but in terms of capability.

1:20:02 - Jeff Jarvis  
You can't do the model that needs scale, or is it the compute that needs scale? See our earlier discussion. Well, is it both?

1:20:09 - Leo Laporte  
you need a lot of data and you need a lot of ability to crunch that data, to create these models.

1:20:16 - Jeff Jarvis  
I think you need universities, but I think you need government, as happened in Norway.

1:20:21 - Leo Laporte  
Where do the universities get the money? They get it from the government.

1:20:24 - Jeff Jarvis  
Right, right, but at least you have an independent organization.

1:20:26 - Benito Gonzalez  
See. What you're talking about here, though, is all non-commercial. None of this is commercially viable. What you're talking about right now, the thing that's happening in Norway.

1:20:39 - Jeff Jarvis  
That is not for commercial uses, that is for society. No, actually not. The deal they did was they said listen, we're going to pool all our content now to make this model and then we'll figure out the business models. We're going to prove that we can do it first and prove that it has value, and then we're going to come back and we're going to negotiate a business model so we can have it Exactly they're not starting out with a capitalistic intent, they're starting out with like let's make it work first. But they're headed there.

Yeah, but they're headed there. Yeah, but they're trying to make it work first.

1:21:19 - Benito Gonzalez  
Yeah, but they want a commercial model.

1:21:20 - Leo Laporte  
It's not but it's not number one priority. That's what I'm saying. Like, the number one priority of all a companies today in america is make money, not make a good model well, the theory would be good models make money.

1:21:28 - Benito Gonzalez  
I I guess I don't know.

1:21:28 - Leo Laporte  
No scale makes money, not a good model. Well, you want, don't you want to use a uh an ai?

1:21:32 - Benito Gonzalez  
that's, that's good, that does a good job I do, but normal users out there, they just want an ai. That's good, that does a good job.

1:21:39 - Leo Laporte  
I do, but normal users out there. They just want an AI that will talk to them and be cool with them and be there for them. Okay, so this is an interesting article that brings up an article that I read today from Calvin French Owen, who worked at OpenAI. He was one of the team that developed Codex, which is their coding tool, and he left OpenAI after joining them in May of last year three weeks ago. He says I want to share my reflections about what it's like inside OpenAI and it's well worth reading. I recommend it in his blog, but there was a paragraph here that kind of got my attention. A lot of good stuff in here, but this is the one.

Chat really runs deep. Since chat gpt took off, a lot of the code base is structured around the idea of chat messages and conversations. So this is really to me, very interesting. He says these primitives are so baked into this point you should probably ignore them in your own peril. So codex is not chat like claude code. It's kind of an interactive coding tool and from the command line. But really these chat bots are what these companies at least open ai, but I think it's true of grok and anthropic uh perplexity they're all trying to do chat bots and I don't really think that's the best use of ai, in my opinion as an eel said, it's not terribly efficient and effective.

1:22:55 - Paris Martineau  
Yeah, it's flashy and it's the thing everybody is interested in, right?

1:23:00 - Benito Gonzalez  
now, but I I it's the thing that can scale see, it's the thing that can scale customers can yeah, can result in a monthly subscription.

1:23:10 - Leo Laporte  
Uh model well, he also says in atAI everything is measured in terms of pro subs, professional subscribers. There you go, even for a product like Codex. We thought of the onboarding primarily related to individual usage rather than teams. You flip a switch and you get traffic from day one. Really interesting piece about giving us some color, uh and flavor of what it, what it was like, at least in the last year at I'm interested as to how this person was able to publish this, given that usually you have to sign an nda uh, he's writing about culture, not about technology.

1:23:51 - Jeff Jarvis  
He says that's if you get, that's if you get a payoff.

1:23:56 - Leo Laporte  
Yeah, usually when you get the payoff you sign that, Although I bet you.

1:23:59 - Paris Martineau  
When you get the job, you sign that. For any of these companies, you sign that.

1:24:03 - Leo Laporte  
In California, though there are some restrictions.

1:24:06 - Benito Gonzalez  
That's true. Yeah, I think non-disparagements are void now, right.

1:24:11 - Leo Laporte  
Not non-disparagements, just non-competes. You still can't, don't get any ideas. I don't know. Are non-disparagements illegal?

1:24:21 - Benito Gonzalez  
That would be shocking, I think non-disparagements, when you get laid off that clause in your papers. I think that I always do that, you know specifically.

1:24:31 - Paris Martineau  
What it is is non-disparagements if tied specifically to severance agreements, agreements, and if they are broad and don't include a clause that says, uh um, this does not in. This does not stop you from speaking about anything that is illegal, that happened here, or like speaking about harassment still be a whistle whistleblower, in other words if it doesn't include that, then the non-disparagement in many states could be uh void, and that's because of an nlrb decision, if I recall correctly.

1:25:02 - Leo Laporte  
But um, we gotta rewrite our severance agreements I.

1:25:05 - Jeff Jarvis  
I wouldn't sign the managing editor's contract of time inc. I don't know if I told the strip yeah, you have I was you have and you sat, you left, like many years of money three years salary bonus christ that's insane.

1:25:17 - Leo Laporte  
did you disparage as a like? Did you use this? Well, that's the funny thing Nobody really cared.

1:25:22 - Paris Martineau  
I mean I, finally I was going to say, magazine is full of fake details.

1:25:26 - Jeff Jarvis  
Yeah, and that's how I kept the documents, but the company is basically dead.

1:25:32 - Leo Laporte  
There's no more company anymore. I should have taken the money I should have taken the money.

1:25:35 - Paris Martineau  
yeah, I like the details in magazine. I think it was worth not taking the money.

1:25:40 - Leo Laporte  
Thank you, but I think you could have written about it by now. Well, by now, yeah.

1:25:43 - Benito Gonzalez  
Yeah, they're gone.

1:25:44 - Jeff Jarvis  
I could say that the editor-in-chief always had burned beef and gin.

1:25:49 - Leo Laporte  
Another thing about OpenAI everything runs on Slack. There is no email. If you're not organized, he writes. You will find this incredibly distracting.

1:26:01 - Paris Martineau  
That's very much startup culture culture though.

1:26:03 - Leo Laporte  
Yeah, like constant.

1:26:05 - Jeff Jarvis  
Slack is closed, right, you know that if it's on Slack, it's your people, right, it's safe.

1:26:10 - Leo Laporte  
Open AI is incredibly bottoms up, especially in research. When I first showed up, I started asking questions about the roadmap for the next quarter. The answer I got was this doesn't exist. Good ideas can come from anywhere. This is actually. There are some good things about this company. It's not often really clear which ideas will prove most fruitful ahead of time. Rather than a grand master plan, progress is iterative and uncovered as new research bears fruit. It's very meritocratic. Uh, it seems like a well, a well-run company. There's a strong bias to action. You could just do things. It wasn't unusual for similar teams, but unrelated teams, to converge on various ideas. There must have been three or four different codex prototypes floating around, but so before we decided to push for a launch, that didn't sound very efficient, but no, but at the same time innovation, yeah, if you're yeah, if you're hiring the smartest people.

You don't want to regiment them, right? You want to.

1:27:09 - Jeff Jarvis  
You want to give them free reign I wonder who says they're actually the smartest people. You convince yours that you yourself that you've hired the smartest people because they're here, they're the smartest people okay, but I think they're pretty smart because they're here, they're the smartest people.

1:27:23 - Leo Laporte  
Okay, but I think they're pretty smart. I couldn't write it, could you?

1:27:28 - Benito Gonzalez  
they're smart in a particular domain, in one domain.

1:27:31 - Leo Laporte  
Well, yes, I didn't mean they're great at ping pong. I mean, yes, they're, they're good. They might be good at ping pong, we don't know. This is the wonderful cartoon I was talking about, from Audra McNamee, illustrating the history of RSS. So this was it says RSS is not dead yet. This was from a couple of years ago, but she has continued to work on this and it is. It's a really, a really for people, and I think probably even Paris you're young enough not to really remember Google Reader and how important RSS was in the beginning. This is a really, uh, a great.

1:28:15 - Jeff Jarvis  
There's Cory Doctorow is Dave Weiner in here?

1:28:17 - Leo Laporte  
uh, I think they mentioned the, the history of it. Aaron Schw schwartz, dave weiner, uh, jointly wrote rss. He says one of the things that was bad about rss was there were competing standards.

1:28:30 - Jeff Jarvis  
Remember that yeah, that was, that was.

1:28:32 - Leo Laporte  
That was so tiresome, that fight yeah, this was dumb and it hurt rss, but nothing hurt it as badly as google saying oh, rss is dead. Yeah, thank you, google.

He says she writes, rss was a casualty of Google and Facebook's monopoly power. They allegedly spent allegedly she puts in scare quotes the early 2000s, slowly bleeding money out of independent websites, killing RSS along the way. Matt Stoller explains explains. This is really great anyway, the part I liked especially was when, by the way, the other thing that killed rss is social media. Right, people started using twitter and you know that was the feed yeah, your blog feed didn't.

1:29:17 - Jeff Jarvis  
What's that?

1:29:17 - Benito Gonzalez  
yeah, you didn't need that anymore what killed RSS is that web pages stopped offering RSS feeds.

1:29:23 - Leo Laporte  
She says RSS is as part of a flourishing, decentralized, open internet diet. But the protocol remains. For the last two decades, RSS has quietly been powering one of the fastest growing media industries. Podcasts Yep, Thank you, Dave. Podcasts yep thank you the same, the same forces that are trying that killed. You know blogs are doing the same to rss spotify.

1:29:48 - Jeff Jarvis  
Doesn't use rss spotify because that's they don't want it to be open. Right and does apple podcast now use rss?

1:29:55 - Leo Laporte  
yeah, well, it does. We're. By the way, we are happy and proud to be rss. Podcasts are proof that decentralized rss-based media can support an industry. People discovered new podcasts without an algorithm. Podcasters were successful and they got to keep most of the money we made. And the podcast app you use didn't affect which podcast you could listen to, right, unless you're using spotify. But like any good thing on the internet, there's a big tech monopoly trying to ruin it, just like facebook and google uh, bulldoze the open internet of the 2000s. Spotify, amazon, apple and google are in a race to control podcasts. I, I don't. I don't think apple is really doing that, because they still support rss, um, spotify for sure amazon apple kind of control.

1:30:47 - Benito Gonzalez  
Does control podcasts right now.

1:30:48 - Leo Laporte  
They're powerful yeah yeah, powerful in their editorial recommendations and things like that, but it's still rss and you can still get a podcast, our podcast, from anybody. We put it on spotify but would never go spotify exclusive. And that's the move that when, when they paid joe rogan tens of millions of dollars to go exclusive, that was the move.

1:31:10 - Jeff Jarvis  
That's like well, and when they try to take over advertising, the entire advertising ecosystem they're still doing that.

1:31:14 - Leo Laporte  
They haven't stopped doing that, uh, unfortunately, um, but and that that it it's not over read, it's very good. I'll put a link in the show notes, and thanks to Audra McNamee for writing it and publishing it.

1:31:32 - Benito Gonzalez  
Very cool. I really do miss opening up my RSS reader and being like Ooh, let's see what happened today. It was so much better than a newspaper.

1:31:40 - Leo Laporte  
I still do that, and my blog is on RSS. It's also on Activity Pub, so it has the benefit of both. But you know.

1:31:47 - Jeff Jarvis  
And the other thing was that and this is Dave Weiner's argument that he didn't want the news judgment of the New York Times. He wanted a river of news. It is a river, yeah, you could just get all the latest stories. So I miss all kinds of things in the New York Times and Washington Post now because I don't have RSS feeds of them. They don't do RSS anymore. I don't know, but I don't use an RSS reader, I think they do.

1:32:07 - Paris Martineau  
I use an RSS reader, probably do yeah, they do.

1:32:08 - Leo Laporte  
I subscribe to uh, both on RSS. Um, I have an RSS reader I use on the iPad called tapestry. That's great that that actually adds activity, pub and social media, if you want. I don't because I don't want to be buried, but it's a really cool rss reader and it's how I I do that. You see, all these links that I put in every, every week for this show and all the other shows I do, those are from my rss reader did we ever get a store an inside story of why google killed reader?

no, I would like to know. Although I think the premise of this comic is they did it because they couldn't they couldn't monetize rss in the way that they can monetize it didn't cost them anything to have yeah, it couldn't have been that big of a endeavor to save money.

1:33:00 - Benito Gonzalez  
I think they did it, for you know, yeah to proactively, you know, prevent that from going in to kill the open net.

1:33:08 - Leo Laporte  
Uh, but it hurt. Why did they do that?

1:33:09 - Jeff Jarvis  
that hurts them why did they do amp?

1:33:11 - Leo Laporte  
remember the idea that debates over amp.

1:33:14 - Jeff Jarvis  
Well, that's a. That's a whole different story. That's, that's embeddable with business model. Blah, blah, blah. The google benefits from open feeds. Existing full stop cory doctor says and is quoted in this comic.

1:33:28 - Leo Laporte  
What killed rss was the growth of digital monopolies who created silos, walled gardens and deliberate incompatibility between their services to prevent federation, syndication and interoperability. So we've identified this comic says three suspects in the case of rss's suspicious death infighting among rss's creators that was the early days yeah, I don't think that's so much. Social media companies had a better product, yet twitter definitely had something to do with it attracting more users, and google and facebook's dominance made it harder for independent websites to make money.

1:34:08 - Jeff Jarvis  
Those were the days. So I brought up Dave Weiner's name about 10 times. But I ran into Dave some years ago in Perugia and I said, dave, the beginning days of the blogs were just wonderful. We had blog rolls and we got along and we linked, we had blog roles and we got along, we linked to each other and we, you know, and we talked and what happened? They said jeff said everything is good when it starts.

1:34:30 - Leo Laporte  
Yeah, well, yeah, that's true, yeah, that's true um, all right, let's, let's take another break when we come back.

1:34:41 - Jeff Jarvis  
Uh, you guys pick your stories and you're going to want to hear about, about, uh, the browser, about comet telling you that, oh you got access to.

1:34:49 - Leo Laporte  
I got complexities browser. You know everybody and their brothers making a browser. Kagi makes orion, which I've been using. It's basically a safari port port with some built-in.

One of the reasons it's very hard to beat the incumbent, google, is because Google pays everybody right to be the default search $20 billion a year to Apple to be the default search. And so Apple gives you some choices of searches, but one of them is not Kagi. Some choices of searches, but one of them is not kagi. So if you are a new paid search engine, which k-a-g-i kagi is, and I, it's what I pay for, I use it, I love it. Um, it's de-googled search, right if. But it's the same problem that I had with neva, which, which was the last one I used, that went belly up.

Because you can't compete against google because it you've got to jump through hoops. You have to install an extension to add their search to safari and many other browsers. That's not built in because they're not getting, they don't pay them. So, uh, they said, well, let's make our own browser, orion. Now perplexity is doing the same thing for other reasons. They want to do an ai browser. That's all the rage now, in fact, open AI, it is rumored, is about to release a browser and Google added more features, but we'll come back to that we'll talk to that just a little bit after the break.

You're watching intelligent machines. I think this is kind of a fun conversation. We're learning something here. Uh, not trying to cover exhaustively all the news, because I would be exhausted if we did there are there. This is a beat that has 20 30 stories a day. Oh yeah, minimum, minimum. Yeah, it's crazy what's going on right now. Jeff jarvis here he's. He's a great deep thinker, public intellectual. Uh, yeah, you're a public intellectual, one of the one of the few, the crowd crowd the brain.

Yeah, web we Weave is his latest magazine, now available in audio and Gutenberg, parentheses and softcover. So buy all three. Do you get a discount if you buy all three and Paris. Martineau is here.

1:36:55 - Paris Martineau  
Soon to be employed, that's all I'm going to say Soon to be. That's all All you need to know.

1:37:00 - Leo Laporte  
We think you are the best. Paris, it was so nice to spend time with you, we know it.

1:37:06 - Paris Martineau  
It was lovely. Leo gave me a tour of Petaluma.

1:37:09 - Leo Laporte  
I showed her the Carnegie Library. Did you see, any chickens. I talked about the chicken coops. I explained the reason that we were the chicken capital of the world.

1:37:20 - Paris Martineau  
I was looking for butter and eggs.

1:37:22 - Leo Laporte  
I talked about the hatcheries. I did show her the big mural that has chickens.

1:37:26 - Paris Martineau  
The mural was great and the history of Petaluma. I did see painted chickens. Yeah, she did.

1:37:30 - Leo Laporte  
See, you saw chickens, and there's a history of Petaluma called Comrades and Chicken Farmers. Our show today, brought to you by Intelligent Machines, is brought to you by intelligent machines, is brought to you by melissa this week, the trusted data quality expert. They've been doing it longer than we have, since 1985. Melissa's latest milestone features a full sys ssis product stack that's now officially supported on azure data factory. Both web services and on-prem Sys components can be executed in the cloud. Yeah, wow, empowering you to modernize your ETL workflows without disrupting your existing development processes. With this release, you can continue designing Sys packages in Visual Studio exactly as before, then deploy them and run them within ADF, sys Integration, runtime, ir. This hybrid approach delivers minimal to zero changes to your existing Sys packages or development workflow. Azure hosted execution for enhanced scalability, centralized management and reduced infrastructure overhead. You get seamless support and simplified infrastructure. No need to maintain on-premises sys servers. Isn't that nice? Run it in the cloud.

Melissa's data enrichment services support all industries. By using Melissa as part of their data management strategy, organizations build a more comprehensive, accurate view of their business processes. I'll give you an example University of Washington facing a major loss of critical data costly postage waste because they were mailing duplicates. They were mailing the wrong addresses and, as a result, missed fundraising opportunities. The associate director I am of strategic Initiatives for the University of Washington said, quote we had so much data to contend with and knew it was important to bring in an expert. We were an early adopter and used nearly all the components in Melissa's data quality suite.

We appreciate their developer support and integration with our own tools and workflow. We see Melissa as a trusted vendor that provides good value and superior quality. In effect, melissa is your data scientist, ready to come to your aid. Data is, of course, safe, compliant and secure with Melissa. You need not worry about that. Melissa's solutions and services are GDPR and CCPA compliant. They're ISO 27001 certified. They make SOC 2 and and hippo high trust standards for information security management. They go the extra mile to keep your data safe. Get started today with 1000 records cleaned for free. Melissacom slash twit. That's melissacom slash twit. We thank them so much for supporting intelligent machines. So tell me, so you got somehow.

1:40:25 - Jeff Jarvis  
You got an invite I wrote to the press office and said please may I can?

1:40:31 - Leo Laporte  
we are going to interview uh soon I think perplexities ceo. No, I'm sorry, coggy.

1:40:38 - Jeff Jarvis  
Ceo vlad prelovak shoot, but we're trying to get.

1:40:42 - Leo Laporte  
We're trying to get perplexities. Oh, we're trying to get all on. Yeah, I 'd really so.

1:40:46 - Jeff Jarvis  
I, I emailed them, I talked to really good guys, the press department, about it and they they view that there's three. There were three generations of browser wars right Browser War, one against Microsoft versus Netscape, browser war to Netscape versus I mean Microsoft versus Google. And now it's perplexity against Google and maybe OpenAI. I was wowed from using it.

1:41:13 - Leo Laporte  
Really.

1:41:14 - Jeff Jarvis  
In what way?

1:41:15 - Leo Laporte  
So there was a browser. The browser company of New York created this browser, arc, and then said you know what? Nobody wants to use this, we can't make any money. We're going to abandon arc and we're going to make Dia, which is an AI first browser, I think somewhat similar to what everybody else is doing.

1:41:29 - Jeff Jarvis  
That's what everybody's doing. It's open. I was doing it. Google's adding more and more.

1:41:35 - Leo Laporte  
So why do you want?

1:41:35 - Jeff Jarvis  
AI in your browser? That's my question. Well, let me tell you there's a few things. Can you talk again, Because I just screwed up my Testing one, two, three.

1:41:44 - Leo Laporte  
I'm fine, jeff Jarvis, do you hear me? Come in, jeff. Hello, hey, Newmark.

1:41:51 - Jeff Jarvis  
So I think there's two ways to look at it. One is that it is agentic AI brought to life, in that if you open up your Google mail and your Google calendar and your Google this and Google that right in the browser, you can tell perplexity to put a new event in your calendar.

1:42:13 - Paris Martineau  
You can tell it and it does it, no problem.

1:42:15 - Jeff Jarvis  
Does it no problem. You can tell it to summarize all your email. You can do all that stuff.

1:42:21 - Paris Martineau  
Kind of work across things. Could you say like put the event that Steve emailed me about in my calendar?

1:42:27 - Jeff Jarvis  
That's what. I didn't test it with great alacrity, but yes, the guy I talked to made flight reservations with it.

1:42:37 - Paris Martineau  
That's different than those things he like actually booked a flight with it.

1:42:41 - Jeff Jarvis  
Yep, yep, he said he did. And and uh, jason Howell uh, did a whole bunch of tests with it. I'll describe in a second. So so one is that you can use it as an agent in whatever you have open and whatever you give it access to. Um, jason was able to send to have a post to blue sky.

1:42:58 - Paris Martineau  
I have for some reason it's not letting me do that.

1:43:06 - Jeff Jarvis  
I don't know why, but but you must know that you have google workspace and that you deserve to have less of an experience. Here's the thing my my pro account because is academic, because I get it included with being storybrooke and so I had to sign it to get it there. But all my stuff is on google. But I, I just said, pay attention to my google stuff, and it did so. The other part of it is that it interacts with everything you have open your browser. So jason did a test and he, for example, put up uh, he had five or six tabs open, it's it's, it's chromium, so it's very familiar. And, um, he had three of those tabs were cameras that he supposedly was looking at and he said compare these cameras for me.

1:43:42 - Leo Laporte  
Oh, that's interesting.

1:43:44 - Jeff Jarvis  
He knew only the three tabs had the cameras. It came back, it looked up all kinds of stuff. It did a whole chart comparing the features. All kind of pretty. Jason, there was a conference that Jason and I were going to go to but we didn't go to. That's coming to San Francisco next year and they announced their first 50 speakers. So Jason went in and this video was on YouTube and he said find all the 50 speakers, look up all of their LinkedIn, look up their recent statements, tell me what they're likely to say and tell me who I should try to interview if I go there.

1:44:20 - Leo Laporte  
These are the same exact things I do in Perplexity now. So they're just building it. They're integrated, right yeah.

1:44:27 - Jeff Jarvis  
And you can do other things. You can have a group your tabs, which I have to have the whole new Lenovo Chromebook to be able to do that.

1:44:36 - Leo Laporte  
Oh gee, it's too bad, you don't have the whole new Chromebook, Lenovo Chromebook.

1:44:41 - Paris Martineau  
Too bad I bought it, I bought it.

1:44:43 - Jeff Jarvis  
Did you buy it? Yeah, okay.

1:44:44 - Leo Laporte  
Because I got one for Abby and I was going to show it off as my pick of the week.

1:44:49 - Jeff Jarvis  
I want to hear more, because I haven't opened it up yet, because I'm crazy.

1:44:52 - Leo Laporte  
Oh, I think you'll like it. Anyway, I'm hearing great things.

1:44:54 - Jeff Jarvis  
I played with it in the New York event. So so it's integrated with the browser in a way that Google should have been a year ago, and the fact that I have to buy one Chromebook to be able to organize tabs why couldn't Google do that Years ago? I talked to Marissa Meyer when she was there and I was blathering on the way I do, like I am right now, about hyper-local news and she said, jeff, you're wrong, it's about being hyper-personal. And she was right and that's what Google could be. But perplexity just strikes me as being always ahead. They always are more creative, yeah. I agree, always trying things faster.

I love perplexity yeah, and they're just so impressive. And so the browser is really really impressive, and Jason already says that it's saving him time and work because it's integrated, because it's mixed in with your browser and it knows what you're browsing, it knows what you're looking at, it knows what you want to do, and that gives it context to act as an agent. So it's the first integration and the first agentic, and so I'm I'm loud, what about privacy? Yeah, cause that's an issue.

1:45:57 - Leo Laporte  
Yeah, cause I got to tell you. The CEO of perplexity said the reason we want to make a browser is so we can collect all those signals for advertising.

1:46:05 - Jeff Jarvis  
Well, it's more than that.

1:46:07 - Paris Martineau  
It's the fact that I'm giving Perplexity access to my email, right, yeah, no, you're giving, and you're not just giving to it so that you get a service for free. You're paying a lot of money to give Perplexity access to your email, your calendar, your browsing history, everything you do on the website.

1:46:22 - Jeff Jarvis  
Well, for now they're putting it out to the $200 a month people, but they're opening up, they're giving people invitations. Please don't bug me for invitations people. I don't even know if I have them yet. No, they're going to open it up beyond that, so it's not going to be a $200 a month.

1:46:36 - Paris Martineau  
For how long is my question? That seems like a complicated service to offer. It doesn't seem like they're able to offer it realistically for free to a lot of people, unless I guess the thing that is a benefit is just that they're able to sell your data and make money off of that by offering it up or using it to target ads more effectively.

1:46:57 - Leo Laporte  
What's funny is they're not making any secret about it. This is the article from TechCrunch Perplexity CEO says its browser will track everything users do online to sell hyper-personalized ads. Hello, marissa Meyer, not hyper-local, hyper-personalized ads. Aravind Srinivas was on the. We were just talking about TBPN podcast. Aravind, if you would do that, why wouldn't you do the number one AI show in the world? You should come on our show and talk about it. Defend your point of view. He says we plan to use all the context that we get as you use it to build a better user profile and maybe you know, through our Discover feeds, we could show some ads there. That wouldn't be too bad. I mean, you don. I do frequently.

1:47:45 - Jeff Jarvis  
It's actually a pretty good news source.

1:47:49 - Leo Laporte  
So Comet was going to be launched in May. It has finally come out in pre-release, so you have to get an invitation or pay for the super expensive version of. Perplexity to get it.

1:48:03 - Paris Martineau  
Someone said in the chat that they have access to it in their $20 a month account, though.

1:48:08 - Leo Laporte  
Oh, Well, there is a wait list, so I signed up to the wait list.

1:48:11 - Jeff Jarvis  
Yeah, there's like 500 000 people in the wait list yeah uh go to the press, the press department, the uleo I hate doing that, you know me well, you're not. You're not asking for something early, you're not asking for any special favors, you're just asking hey, man, could you give me a copy?

1:48:29 - Leo Laporte  
man, I don't know how I would know if I have it. I don't see anything that indicates I should have it, but I'm already using perplexity quite heavily, so I imagine I'm getting much of that function.

1:48:41 - Jeff Jarvis  
I think you're going to like it because it integrates in with the context of what you're doing.

1:48:45 - Leo Laporte  
I'll be honest. The reason I don't use dia is because for me, browser functionality is important where the tabs are, how I can pin tabs, how I can lock things in.

1:48:55 - Jeff Jarvis  
This is chromium, so it's operating. Of course, you gave up chrome a long time ago because you have to be special, but it's very familiar because it's chromium.

1:49:03 - Leo Laporte  
So it does all those same, does all the things, things in it. Here's the other reason I don't want to use it, because chromium does no is now on manifest v3, which doesn't support you, block origin and, uh, you know, google and their infinite wisdom decided to kill ad blockers. I wonder why. Why would they want to do that?

1:49:22 - Jeff Jarvis  
well you're robbing from. Well, I'm going to do it. I haven't done this in two years. You're just trying to rob from content, paris. You should yell at them, because how do you support the good work of journalists like Paris Martineau except by supporting the advertising? When you take the advertising, away.

1:49:35 - Leo Laporte  
You're taking food out of her mouth.

1:49:37 - Paris Martineau  
I'll just say I haven't worked for an ad-supported media company in a long while.

1:49:45 - Benito Gonzalez  
And I understand what you're saying. Look, we're ad-supported media.

1:49:47 - Leo Laporte  
Yeah, exactly, I, I understand what you're saying. Look, we're at supported media. I mean, yeah, exactly, I'm being pretty hello hypocritical about this, but a lot of these ads, there's a few things. One, they're so ridiculous that you can not even look at a page on mobile anymore because it's it's got sliding windows and videos opening and all this stuff, these ad networks. They haven't done it lately, but have in the past pushed malware. So there is a security thing and there's definitely a bandwidth issue. There's a huge amount of bandwidth on these ads.

So you know, I agree, I want it. So you know, you turn off your ad blocker on sites for people you really like. The really good sites do what we do, which is their first party ads. They, they're not third party ads, they're not ads inserted after the fact. They're uh, they're ads, you know, sold by, like, for instance, daring fireball, john gruber or jason snell, six colors. Uh, those ads come from their server, so ad blockers don't block them. Uh, they're first party ads and those I have no problem with. I just have problems with ads that really take over the whole page and they're they're ugly and they're risky so we're going to see a lot of these browser stories over the next few weeks.

1:50:57 - Jeff Jarvis  
Open ai working on nets um, as soon as a comment came out, oh yeah, we got one too. Google, yeah, open today that they're adding more features and I don't like the ai enabled search results.

1:51:10 - Leo Laporte  
Do you do you turn those on? Do you use those?

1:51:13 - Paris Martineau  
I've, I don't. I find them completely useless, terrible, uninteresting and, frankly, it's just another thing that I have to scroll by in order to get to what I'm actually looking for, which is increasingly the regular search results are like two to three lines on the first page of google. It is uh from the bottom and top. I'm being attacked on all sides by sponsored links, uh, ai search results and things I didn't try to search well, good news.

1:51:41 - Leo Laporte  
Next week, our guest will be tulsi dosi, senior director and product lead for Google's Gemini models. We're doing that recording tomorrow right, right.

1:51:55 - Jeff Jarvis  
So we're also going to have Steven Johnson.

1:51:57 - Leo Laporte  
Is Steven going to be on next week instead and we'll do Tulsi the week after. So we are going to record in public tomorrow. So actually, if you wanted to see our interview with Tulsi, we're doing that between 1 and 2 PM. Pacific club members will get to watch that and it'll be on the live stream and then we'll roll that into the show either next week or the week after. I do want to talk to Steven Johnson as soon as possible, because he was scheduled for today's show.

He has released notebook LM and updates in notebook lm. That I think is really interesting. Yeah now, first of all, I like notebook lm. It's a really clever idea. This is google's uh gemini applied to, in effect, rag stuff.

1:52:41 - Jeff Jarvis  
It restricts itself to the content that you pointed to right.

1:52:44 - Leo Laporte  
So, for instance, uh, some time ago I I gave it Google's quarterly results and then said and then now you can ask questions about it, this is the one that does podcasts as well. Well, they've added a new feature trusted sources. I can choose sources from pre-selected trusted sources so I can say what I'm interested in here. I'm feeling curious. It just gives you a random selection of authoritative sources in a random area. Let's see what I get here.

1:53:19 - Paris Martineau  
A primer on prediction markets. Prediction markets.

1:53:23 - Leo Laporte  
So there are 10 sources.

1:53:26 - Paris Martineau  
It's all about election betting.

1:53:28 - Leo Laporte  
One of them is a youtube video yeah, historical presidential betting markets, prediction markets, market integrity and manipulation from wilmer hale, asterisk magazine so these could asterisk uh give them access to their website, or was? That I don't know we'll have to ask ste Steven.

1:53:46 - Jeff Jarvis  
Well, that's. The other thing they announced is that the Economist and other sites have notebooks that they're sharing.

1:53:55 - Paris Martineau  
That was the most ominous crack of thunder I've ever heard live, jeff. It sounded as if you were in a spooky mansion and you just said that this could be your last night.

1:54:10 - Jeff Jarvis  
I warned that I have a big storm coming.

1:54:11 - Leo Laporte  
Yes, so oh, and you're on the generator now.

1:54:14 - Jeff Jarvis  
Well, I bought my wife a UPS for because she teaches class right now. I should have bought myself one too, because I've got the. The router is on UPS generator.

1:54:26 - Leo Laporte  
I tell you it was the scariest thing this morning. Half an hour before Windows Weekly, I came up here, turn on the lights and everything went jeez. It was a pitch black in the attic and I thought, because there's so many lights in that attic oh, yeah, well I don't think it's ever been dark before, uh I don't know what happened.

Anyway, we, we. I think we got it fixed, but that's one of the reasons I have trouble showing my screen is everything's a little kerfluggled here. I don't know what. I don't know how any of this works.

1:54:53 - Benito Gonzalez  
Are you only on one circuit up there? Yeah, okay, that's probably why.

1:54:57 - Leo Laporte  
No, there's plenty of amps. It's not that it's never happened before, it's just something. This is this house is a mess leo's house is so cute. It's full of crystals.

1:55:11 - Paris Martineau  
It is lisa. You notice that lisa has a lot of it's a new house, right it's?

1:55:12 - Leo Laporte  
a very new house. It's brand new and unfortunately, we're tearing it apart now because it was poorly constructed and is leaking. Oh no, paris, I didn't even show you paris, but the whole south wall is off oh no, yeah, that's not good, not good, wow, not good. And then they, they as often happens with construction they did the demolition right away. They're good at that.

1:55:37 - Paris Martineau  
They're good at tearing down yeah, yeah, but putting it back together three weeks we haven't seen a soul.

1:55:42 - Leo Laporte  
It's like they disappeared. They tore off the side and then disappeared. They all have ad, yeah, I think so. It's an adobe uh thing. And they so they took the adobe off to see what was underneath. And what was underneath was a lot of leaks and stuff. So now they tell us we have to take all the windows out, all the sliding glass doors out, reseal everything, put everything back in. And then we're saying, well, do we? Maybe? We don't want to stucco it again, because if I don't to have to, is there a house warranty in California? Oh yeah, 10 years.

But the builder is refusing to honor it.

1:56:18 - Jeff Jarvis  
We sued our builder and then he said I'm judgment proof. I said what does that mean? He said I got nothing.

1:56:23 - Leo Laporte  
Yeah, that's basically I mean we're probably going to. Yeah, I don. That's basically I mean we're probably gonna. Yeah, I don't want to go into detail. We're attempting to recover. We'll see if we get a shot at it.

We can't talk about paris's new job or leo's suits it's literally going to cost hundreds of thousands of dollars my retirement and the. Here's something I'll tell you kids, you young people you know you're putting all that money away from retirement and it's tax-free when you put it in right, right, that 401k, that IRA, yeah, all that money that we're saving.

Guess what, as soon as you take it out, they tax the hell out of it. And basically I'm at a point where you know I have to take out twice as much as I need, because the government's going to get half of whatever I take out. So I thought, oh, I got a nice nest egg. I should be fine. I realized no, you don't, especially if you have to spend it rebuilding the house you just bought. Okay that's.

1:57:16 - Jeff Jarvis  
I think we'll be keeping making podcasts for a little while. That's right.

1:57:18 - Leo Laporte  
Well, that is the good news is that I can never retire. I have to keep working until but, folks, folks you've got to recommend this podcast with five star reviews so we get more people.

1:57:31 - Paris Martineau  
Do you have any five star reviews, Paris, I do yes.

1:57:34 - Leo Laporte  
All right, we're going to take a break you can share some five star reviews. I will share this new Chromebook, which I did not buy for myself, but I bought for my daughter, who is a Chromebook fanatic, and she's been. She used her last chromebook so much yeah, she's a chromehead she used her last chromebook so much that the question mark key and the s key fell off. So in order to type a question mark or an s, she has to copy and paste it in. I said, honey, you need a new laptop.

1:58:03 - Jeff Jarvis  
She said, oh no, it's fine did you get to meet abby uh parents?

1:58:07 - Leo Laporte  
al not Like ships that pass in the night. She came in after you left.

1:58:12 - Jeff Jarvis  
I thought we'd be a match set. You'd see Abby and I saw Henry, she's in.

1:58:15 - Leo Laporte  
New York. Right now she's trying to get a sandwich, Apparently. Henry sold out. I might see her there.

Even for his sister he sold out, wow. All right, before we get to the pics of the week which are coming up next, I do want to mention our club and all the great stuff coming up in Club Twit. Tomorrow, as I mentioned, club Twit members will see our interview with Tulsi Doshi, senior Director and Product Lead for Gemini Models. Wow, from Google. That's a great get. We are also, tomorrow, going to be doing oh no, tonight, I'm sorry, we're doing Micah's Crafting Corner, a little cozy crafting. So if you've got a little something going on, maybe some knitting or sewing. Micah usually does Lego. I'm not sure what he's doing this time. I did some cooking last time. Please join us. Uh, tonight, right after the show for micah's crafting corner, 6 pm, pacific, 9 pm eastern. Um, let's see what else is coming up. Oh, we were going to do richard campbell's pc build. He's got all the parts. He's going to build a new pc. We're going to watch him do it on friday. The ram didn't come, so we're going to put that off till next Thursday. A week from tomorrow.

Home Theater, Geeks records in the club. The AI user group is the first Friday of every month. We've got Stacy's Book Club coming up, august 8th, a really good book which is not too late to pick up and read. This is how you lose the time war. It's amazing and it's a short. It's like a novella. It's amazing and it's a short. It's like a novella. It's not really long. So, please, if you want, join us for that, that's August 8th. Right after that same day, photo Time with Chris Marquardt.

Our Word of the Week, our Word of the Month classic, the Made by Google event is coming up August 20th. That's Google's announcement of their new Pixel phones, I believe. So we're going to cover that live. Wednesday, august 20th, 10 am Pacific. All of this club only. Okay, we do stream it live, some of these things, for instance, home theater geeks, hands on Apple, hands on Windows. We put out audio publicly because we want you to have the content. But you have to be in the club if you want to get the video. And if you're not there for the live event, then you have to watch on the TwitPlus feed, which is club only. So there are some real reasons to join the club. Also, if you don't like ads, you don't have to feel guilty about skipping them. Just join Club Twit 10 bucks a month and you won't ever hear another ad. Even this plug you won't hear again, because you're you're donating, we don't, we don't really need to show you ads.

2:00:52 - Paris Martineau  
No tracking, no ads, nothing if you're a little freak who wants to hear the ads anyway, but also wants to support the club, you can do both, because I know people are out there who've said that that they want to both support the club and hear the ad reads because they think they're fun. You can contain multitudes if you. Yes, isn't that?

2:01:06 - Leo Laporte  
nice, you can do. You can do both. We even have a feed on the discord called all the ads which is just the ads. If you really like ads, um, what else anyway? Please join the club. It really makes a difference to us. It's 25 of our operating costs. Uh, doesn't go into my pocket, doesn't go't go to Lisa's pocket. It goes to Micah, jeff and Benito and Paris and all the people who do these great shows for us.

Yeah, no, it won't go into his pocket, not if I can help it. He's judgment-proof, I'm judgment-proof. What do you want? Twittertv, slash Clark Twitt. All right, paris, let me start. I'll start with this.

2:01:50 - Paris Martineau  
Just because it's wait, let me do a, let me do a. Uh review read first really quick and then we can go to the pics.

Oh yes, this is a five star review from uh joseph patrick of our podcast on uh apple podcast. If you want your review shouted out in the the show, leave us A good review and if it's funny or interesting, maybe I'll shout it out. This is an ad From Joseph Patrick who says Interesting. Take here as much as I like the Craig Newmark jingle JJ no longer works there. I suggest the jingle be replaced with the jingle for Sunni. Can I suggest ripping off the Sega Genesis start sounds and replacing Sega with Sunni? Now, while I Personally do not have the talent or know how to create such a jingle, I hear that the host of this show are good friends with several intelligent machines who have such talents. Perhaps a jingle competition is in order, says Joseph Patrick. So you know, do you have jingle suggestions? Do you think the jingle should be something different? Do you think we should keep the same one?

2:02:48 - Leo Laporte  
I love it. It's a new way to communicate with us is leaving us a review.

2:02:53 - Paris Martineau  
I'll at the very least read it and decide to read it in the show. I do like the idea. I like the Sunni, that's pretty good.

2:03:00 - Benito Gonzalez  
Sunni like Sega, yeah, like Sega.

2:03:02 - Leo Laporte  
Sega Sunni. Somebody did an AI, craig Newmark with a heavenly choir here in Discord, but I can't play it because I can't play the audio.

2:03:13 - Jeff Jarvis  
Well, can you just play it loud on the computer and then put your mic?

2:03:15 - Paris Martineau  
we can't we can't open this can of worms again we're not unmuting we're not muting that computer cannot do it.

2:03:22 - Leo Laporte  
I cannot, I cannot you could play it for yourself so jeff saw these at the google event, the chromebook event. This is the new. It's a new, it's actually a whole new platform, the chromebook plus platform, which uh makes the chromebook an ai device, uh well, the plus has been around for a couple years now, but this is the lenovo version.

2:03:44 - Jeff Jarvis  
Is the ai?

2:03:45 - Leo Laporte  
yeah, and this has 16 gigs of ram. It has a new processor from mediatek called the companion, which has an npu in it. It also has uh a um 60 tops engine and it is able. Apparently. You get a free uh gemini pro account. Yep, it's able to do. You can even see it. There's the Gemini icon right there in the menu bar. You also get a year of two terabytes storage on Google Drive. That's pretty common with Chromebooks. This one is about 750 bucks, has a touchscreen. It's a beautiful OLED touchscreen. I mean it is really gorgeous. Two pounds, very light, 18-hour battery life and a fingerprint reader, which I really like. I got tired of entering my PIN or my password every time when I log into my Chromebook, so this makes it secure. It's got that nice soft-touch keyboard Chromebooks are famous for.

I like the keyboard.

2:04:43 - Jeff Jarvis  
It's very thin, very light, and this is huge for me, absolutely huge for me Fanless, yes, nice and quiet the old. Samsung I had was just louder than a jet engine.

2:04:55 - Leo Laporte  
Shall, I call into the show so you can see the camera. What does it retail for?

2:04:59 - Jeff Jarvis  
$749 or $649 without a touchscreen and less memory.

2:05:03 - Paris Martineau  
Hey, that's less than an iPhone.

2:05:05 - Leo Laporte  
Yeah, it's not that expensive.

2:05:07 - Jeff Jarvis  
The high-end. Hp that was out there for a while was $2,400.

2:05:11 - Leo Laporte  
And Google was selling $1,000 Chromebooks for a long time. Yeah, yeah, I bought a couple of them. I am going to call into the meeting so you can see the camera's not great.

2:05:22 - Paris Martineau  
It does have. We're going to have three times the Echo. Somehow we have three versions of.

2:05:27 - Benito Gonzalez  
Leo in this meeting, all right, oh, leo now. Okay, you need, you need to, you're gonna need that one I don't know where it's coming.

2:05:43 - Leo Laporte  
Now you're talking, I'll talk on this one. There you go um, can you? Can you see it, benito?

2:05:49 - Paris Martineau  
I can see it yeah.

2:05:51 - Leo Laporte  
Well, Benito has to pick it. There it is.

2:05:52 - Paris Martineau  
So it's not the best camera ever, but it's okay.

2:05:56 - Leo Laporte  
It's a little low res.

2:05:58 - Paris Martineau  
You get to see the forbidden top shelves of Leo's setup.

2:06:01 - Leo Laporte  
Yes, I showed this to Paris. I said, yeah, nobody ever sees these. Set it up, but nobody ever sees them. Um, it's excess hat storage on the top shelf there, so I think it's a I mean I for this price, this is a great choice. Uh, abby loves chromebooks because she doesn't ever worry about losing your data. It's all on google drive, so it's all safe. Um, I know you love chromebooks. It has has Android, of course, android capability, and you did see that. Samir Samat said yeah, we're merging Chrome and Android sometime in the future and I imagine that these newer models will have the capability to do that. You'll get the new operating system. I think a nice job. It is a nice job and you've ordered it. You got it.

2:06:45 - Jeff Jarvis  
I haven't. You just haven't set it up yet. I was out of town most of this week and I didn't want to try to take a new machine with me, so I went to.

2:06:53 - Benito Gonzalez  
I think you'll like the screen. I think the OLED laptop is pretty nice. Yeah, the screen's nice.

2:06:56 - Leo Laporte  
Beautiful, beautiful screen. I'm really happy. Abby has trouble with LEDs and the flickering.

2:07:09 - Jeff Jarvis  
It gives her migra. She can only use oled uh, laptops.

2:07:11 - Leo Laporte  
So when I this came out, I said that's great, it was a model, she, she did.

2:07:12 - Jeff Jarvis  
It also has an s and a question mark. Yeah, what was that it was?

2:07:14 - Leo Laporte  
one of the google uh chrome books yeah yeah, so it's. It's been around for some years. You know it's taken a lot of guff. Ah, paris martino, what do you have for us, young lady?

2:07:26 - Paris Martineau  
I have some pics, uh from my road trip I just did and a couple. One thing I was trying to use uh chat gpt a bit during this to give me ideas for things to do, not that I already kind of had an itinerary, but I wanted to play around with it, see how good it was. I did enjoy kind of the things that deep I use deep research on four point their 4.5 model um and I found that that when I, you know, actually went in with a very detailed request uh for certain cities was kind of useful. The other thing that I used ai for on this trip was that I found um somewhat useful was using the voice mode as I was either walking around places or driving just to ask questions about my environment if I was driving and couldn't look something up. And I mean I think my overall take, as I was reflecting on this, because I tried to use it fairly frequently, because I was traveling solo, it was kind of interesting to have something to talk to me about, stuff like bridges or Portland history.

Portland was my first stops and one example I think that it kind of exemplifies how I felt about this was I was walking across in Northeast Portland.

I was trying to get chat GPT to like tell me about the history of Northeast Portland and my first problem is that all the answers were way too short and not very detailed, and so I went in kind of changed the custom instructions asking it for to be like five to 700 word answers, and that was very hard for it At first it couldn't. It had a very hard time actually responding to my answer, of be detailed about it, but eventually I did get some responses. That led me to an interesting figure in Portland, this guy, stuart Holbrook, who one of the, I guess, details in portland is that there are these things called the shanghai tunnels that all the um portland tour guides say are these networks of tunnels underneath portland where, uh, back in the day old sailors would be, uh, basically abducted from bars and forced to work on ships if they were abducted while drinking and this guy looks like somebody who would make up stories like that I was asking chad to be like okay, well, is this true?

and it's like, well, no. Some people say it was like indented by this guy, stuart holbrook, and I kept trying to get chad to be too tall. I was like, what do you mean? It's invented by this guy. Like, tell me more. And it really. It could tell me a couple lines of detail, but not any of the detail I wanted. So I did some research and found this phenomenal article that I would really recommend, written by a uh portland and uh oregon historian, joe strecker, called stuart holbrook, portland myth maker it's on substack he.

Uh, this guy wrote a sub stack called why is portland like that?

2:10:08 - Leo Laporte  
that's a great idea.

2:10:09 - Paris Martineau  
Hyperlocal, that's awesome is an incredibly detailed, uh kind of almost historical like research paper and also self-memoir about this really interesting figure in oregonian history. This guy basically kind of pioneered this genre of like local national inquirer style journalism that like blended myth and reality and kind of captured the mind of people in like the late 1800s and like or like turn of the century um, and so I don't know, would really recommend that. If anybody's just looking for an interesting historical deep dive, I'd really recommend, uh, this sub stack that's no longer publishing but it has quite a lot of really interesting articles that I then PDFed and put into ChatGPT and had it read to me while I was driving around.

Oh, that's smart, but it was one, I think, of the perfect examples of using these tools is, yeah, it's kind of like a diet soda, in the sense that it was good for getting an overview of something, directing you to, maybe, a figure that I wanted to know more about, but when I wanted to get really good research and the sort of anecdote-rich, narrative-rich reporting, I had to go to a real human who knew their stuff.

2:11:19 - Jeff Jarvis  
So what you could have done is you could have beforehand thought of this and put a whole bunch of resources into Notebook LM and then had it do a podcast for you and then enter into the podcast and ask the podcast host questions about the material, while you were driving. Yeah, that would have been nice. We can ask steven about that next week we will there is uh coming at some point.

2:11:42 - Leo Laporte  
A? Uh, you know who dennis crowley is, this guy who created four square. Oh, he's great, wonderful guy. He has a new project called B bot, which is an audio based guide that you listen to. They're developing it. I'm actually on the discord channel. You can get a a test flight version of it. I haven't played with it yet, cause it's not available in my neighborhood, but the idea would be that this B bot would you'd put it in your ears it's an audio for city guide.

2:12:12 - Jeff Jarvis  
He's always been about locality.

2:12:13 - Leo Laporte  
Yeah, it's a really, it's a really great idea and dens is the guy to do it, so I'll be very curious to see what happens with that, because that's your. Your idea is great. In fact, I used, uh, something like that when we were in hawaii. I downloaded.

There are apps that are audio guides that you're driving around and it says turn left here for the for the best shave ice on the whole island and stuff like that it's like having this chatty old grandpa in your back seat telling you you know, over there, this is where king kamehameha lost his head you know it's kind of it's just crazy stuff I do kind of.

2:12:47 - Paris Martineau  
I mean, one of the main things I ended up using chachi vt for on this trip was asking about cool bridges. I was going over, um, I know I mean, I know I'm so sorry, I'm so sorry to mention this, jeff, but there were some really cool like art deco bridges and I. It turned out that all of them were like made by the same guy, the ones that I kept uh, pointing out or wanted to know questions had any of them fallen?

no, but I know if some of them were draw bridges, though I don't know if that makes it worse the bridges that fall are very rare and few and far between you.

2:13:15 - Leo Laporte  
I know you need to happen first. I'm gonna let you go, if you, if you want, I don't know it's okay, I've got 15 more minutes, okay, good okay. Well, in that case, let's get jeff's pick of the week oh, so I could have done something creepy.

2:13:26 - Jeff Jarvis  
I could have done the people who are marrying their ai's marrying them. Is that legal? I could have. Well, in a matter of speaking, I could have done the uh, really creepy eugenicists, silicon valley people pushing super babies and doing all of that that was.

2:13:41 - Leo Laporte  
I saw that today in the washington post they're doing genetic prediction services for embryos.

2:13:46 - Jeff Jarvis  
Elon's done it and peter thiel is backing it. But instead I found a wonderful column in the new york times which I don't say very often these days by uh lafe weatherby, I presume it's pronounced life who has a book that I just started reading, an academic book called language machines, which is really interesting, and he's a director of the digital theory lab at new york university and his point of all of this is that llms should be seen as simply fun.

If we well, that's not the way, everything else that everything is promised about it. Oh, it's going to change the world. It's going to change all this if from the beginning we just saw it as entertainment.

2:14:28 - Paris Martineau  
Change the world, it's going to change all this, if from the beginning we just saw it as entertainment. That's not a bad idea. It's a good idea. They're not going to be given like hundreds of millions and billions of dollars to something that's just fun and entertainment.

2:14:40 - Benito Gonzalez  
Oh, they also know video games. The video game industry is pretty big actually, yeah, but the video game industry isn't raising the sort of valuations and raising the sort of open ai, it was getting because it's actually valued at that.

2:14:54 - Leo Laporte  
It's not raising, that's right just it's life's not saying this because open ai should pay attention. He's saying it, so we should just have the right idea about all this. It's just for fun, yeah, don't marry with that.

2:15:08 - Paris Martineau  
I think, like this was, this trip was the most I've casually ever used ai, just because it's not bad, is it there?

there's a. I mean I've never said it's bad, I just don't think it is the most valuable thing that has ever and will ever be invented. I think that's just a foolish statement to say about anything, um, but I I think for yes, this is a perfect argument because I think it's the most useful for low stakes things Like. I was hiking the Redwoods and I was like why is the bark looking like that? And something answered me in a voice chat instantly and that's pretty cool.

2:15:38 - Leo Laporte  
Yeah, it said hey, paris, you're looking great today. Yeah, that bark is Jesus Christ.

2:15:48 - AI  
That's what made me so mad I immediately spritz my cell phone with water.

2:15:53 - Leo Laporte  
Holy water. Yeah, this is good. Ai is just fun. It's just fun, enjoy it. And so is this show. It's just for fun. Yeah, we do Intelligent Machines every Wednesday, right after Windows Weekly weekly, which, if the whiskey segment doesn't go on too long we always ask.

2:16:14 - Jeff Jarvis  
Whatever paris and I come in, we always ask. But you know, they still are they on the whiskey?

2:16:18 - Leo Laporte  
yet he's always like no that's not in in of itself enough, because you don't know how long today I was a little nervous because rich Richard started with the 16th century history of Great Britain.

2:16:32 - Paris Martineau  
That's a bad sign.

2:16:33 - Leo Laporte  
It's a bad sign? Yeah, it took.

2:16:36 - Jeff Jarvis  
It was about 300, 400 years before we actually got to whiskey, so yeah, and, by the way, by the way that's my exposure to Richard is that is waiting for him to finish the whiskey segment. When we had him on the show he was delightful. I love that richard is one of the smartest people.

2:16:52 - Leo Laporte  
He's an autodidact he always, you say learn of everything you can know about bridges, and tomorrow he'll give you a three-hour uh keynote on it. I mean, he's really good. So, yes, I love richard and I love his whiskey segments. But anyway, right after richard's whiskey segment 2 pm Pacific, 5 pm Eastern Time, 2100 UTC you can watch us live in the club, of course, on the Club Twit Discord, but you can also watch on YouTube, tiktok, twitch, xcom, facebook, lickton Lickton, you've been hanging around with Grok too much.

2:17:26 - Jeff Jarvis  
I've got an idea for a new social network.

2:17:29 - Paris Martineau  
Anyway, I was going to say that little fox has gotten its mind wrapped around you.

2:17:34 - Leo Laporte  
Or kicked. And if you don't watch live, you can get a copy of the show from the website twittv slash IM for Intelligent Machines. We are also on YouTube. Best thing to know, subscribe wherever you get your podcasts because that's where you will find us and if you do, leave us a fun five-star review the wonderful Paris Martineau might read it and Leo might listen to it.

2:18:00 - Paris Martineau  
And if you have an entrant to the, what should the next jingle be? Competition. Leave that in a five-star review.

2:18:08 - Leo Laporte  
Somehow nowadays with suno I mean, anybody can create great you know or post it on social media and tag to it post it on social media and tag us yeah, yeah, yeah, we like those jingles. It's a lot yeah, we do we used in the early days of twit.

2:18:22 - Paris Martineau  
We had a number of really good musicians who would make them also, if you're a really good musician or have acts, casual access to a choir and would like to compose a jingle, the old-fashioned way, that will put you a couple leagues ahead of the competition that craig.

2:18:37 - Leo Laporte  
Newmark jingles real people, isn't it? It's not.

2:18:39 - Paris Martineau  
It is real people and that's the reason why we're it's going to be hard pressed to replace it. You're you're going to have to try and try and beat that. So challenge out there, heavenly choir.

2:18:50 - Leo Laporte  
Thank you everybody. Thank you, paris martineau. We'll learn next week about paris's new job.

2:18:55 - Paris Martineau  
I think it's a good if the uh, if the government doesn't come and uh take us all down for you squealing on the cia involvement earlier in this show.

2:19:04 - Jeff Jarvis  
I know I'm, I'm sorry.

2:19:05 - Paris Martineau  
It might be the end of all of us.

2:19:07 - Jeff Jarvis  
She has to kill us now.

2:19:12 - Leo Laporte  
I'm sorry. She would be a good secret agent. She would be Because you trust her.

2:19:20 - Paris Martineau  
Yeah, I'm definitely not a secret agent already, that's for sure.

2:19:24 - Jeff Jarvis  
There's no way that that would be the case you look like you're dressed up and ready to go have a martini.

2:19:31 - Paris Martineau  
Yeah, she's going out, allegedly supposed to have a rooftop beer, but the fact that it's a million degrees outside and about to pour makes me believe that will be an indoor beer.

2:19:41 - Leo Laporte  
That thunder that you heard just outside Bedminster is coming your way, it's coming my way. It's coming your way. That's Jeff Jarvis. He's in New Jersey.

2:19:52 - Paris Martineau  
Not his fault. Don't hold it against him.

2:19:54 - Leo Laporte  
My whole family is from New Jersey. What do you want? Montclair State University, suny, stony Brook, and at a bookstore near you, get your copy of Magazine in the web. We weave in the Gutenberg parenthesis. Thank you, jeff, thank you Paris, thanks to all our club members who make this show possible. We will see you next week right here on intelligent machines.

2:20:16 - AI  
bye-bye I'm not a human being, not into this animal scene. I'm an intelligent machine.
