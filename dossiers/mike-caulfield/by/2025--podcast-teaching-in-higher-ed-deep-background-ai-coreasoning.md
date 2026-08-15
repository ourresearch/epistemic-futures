---
title: "Deep Background: Using AI as a Co-Reasoning Partner, with Mike Caulfield (Teaching in Higher Ed)"
person: mike-caulfield
section: by
type: interview
year: 2025
date: 2025-10-02
venue: "Teaching in Higher Ed podcast (host: Bonni Stachowiak)"
authors: "Mike Caulfield (interviewed by Bonni Stachowiak)"
source_url: https://teachinginhighered.com/podcast/deep-background-using-ai-as-a-co-reasoning-partner/
retrieved: 2026-08-13
content: full-text
notes: "Podcast transcript published by the show. ~48 min episode. Captured via r.jina.ai."
---

# Deep Background: Using AI as a Co-Reasoning Partner, with Mike Caulfield (Teaching in Higher Ed)

## Full text

Bonni Stachowiak [00:00:00]:

Today, on episode number 590 of the Teaching in Higher Ed podcast, Deep Background: Using AI as a Co-Reasoning Partner with Mike Caulfield. Production Credit: Produced by Innovate Learning, Maximizing Human Potential. Welcome to this episode of Teaching in Higher Ed. I’m Bonni Stachowiak and this is the space where we explore the art and science of being more effective at facilitating learning. We also share ways to improve our productivity approaches so we can have more peace in our lives and be even more present for our students. Listeners, you are in for such a treat today. We’re going to begin with a nod to the Sound of Music. We’re actually going to end with one too. And in between we are going to be hearing from Mike Caulfield about how he is using artificial intelligence as a co reasoning partner.

Bonni Stachowiak [00:01:09]:

He helps us think about the limits of artificial intelligence, the evolution of search and reasoning tools, and how to help learners develop how to scaffold their skills and competence through co-reasoning with AI. As you’ll hear in the episode, if you aren’t already familiar with Mike’s work, he is the creator of the SIFT methodology. He’s taught thousands of educators and students how to verify claims and sources through his workshops and teaching. His wonderful book, which we also have an episode about Verified, which he co authored with Sam Wineburg. Verified: How to Think Straight, Get Duped Less, and Make Better Decisions about what to Believe Online was published by the University of Chicago Press in November of 2023. Mike Caulfield, welcome back to teaching and Higher Ed.

Mike Caulfield [00:02:04]:

Glad to be here.

Bonni Stachowiak [00:02:06]:

Buckle up because I have been preparing for today’s conversation my entire life. I mean, I don’t want to exaggerate here, but I think I might be so we’re going to go back to watching musicals. In San Diego, they had this outdoor theater called the Starlight Opera, which sadly, they’ve been trying to bring it back for years now and sadly hasn’t happened yet. But when you’d go outdoor theater, I’d get to watch musicals like Oklahoma, South Pacific and Sound of Music. And every time an airplane would fly over to get into the San Diego airport, the entire stage would stop and freeze. The orchestra, the actors would all freeze. And so I’m gonna just start this conversation with a Sound of Music reference, if that’s okay with you.

Mike Caulfield [00:02:56]:

All right, let’s do it.

Bonni Stachowiak [00:02:57]:

All right, so it goes back to one of the Von Trapp kids, Brigitte and Maria is teaching the children how to sing. And at first the kids are protesting and These just doesn’t make sense. Brigitte says, “but it doesn’t mean anything. And Maria says, so we put in words, one word for every note.” And those listeners who are familiar with the Sound of Music know this is the precursor to the very famous song Do Re Mi. And listeners may be wondering, and possibly Mike may be wondering, what on earth does this have to do with AI And I don’t know if it’s just me, Mike, but in my mind, like I think about that all the time, that and I can’t even quite crystallize it into words. But when I try to wrap my head around what AI can do, there’s something predictive about that. Like it’s just matching.

Bonni Stachowiak [00:03:57]:

In this case, you know, she’s matching the songs up with words and then replacing the do ray me words that don’t mean a lot to the children with words that might mean something like them to do a deer. Oh, a deer means something to me. And it’s sort of, I don’t know, there’s something mathematical about that song in my mind and it’s says something about AI and maybe what it says is that I don’t really understand what AI can and can’t do. But I know you’ve been thinking a lot about what it can and can’t do. And I’d love for you to tell us about sort of your early experiences experimenting with the chat based large language models and what you discovered. Let’s start first, Mike, some of your early discoveries with what it couldn’t do. Because we are going to talk a lot about what you’re finding out it can do. Let’s just start with early experiments. Definitely it can’t do this.

Mike Caulfield [00:04:52]:

Oh well, I mean, so I mean a couple things there. The first thing is like early experiments. When I, when I first tried out LLMs, my, my early experience was that they were garbage, I think, which I think was a lot of people’s early experience too. At least if you care about things that you know that are verifiable, if you care about things that have some level of accuracy. This was before they started integrating the search features into it. And so you were really just sort of stuck with just that bare text prediction thing that happened. And it was impressive in a lot of ways. I’m not saying it wasn’t impressive, but for the sorts of things I care about, it didn’t really seem to do any of that.

Bonni Stachowiak [00:05:32]:

Any hysterical examples. I mean, of course many of us have heard about putting glue or rocks in your pizza. I mean, but anything for you that you’re like, it’s kind of funny.

Mike Caulfield [00:05:41]:

I tend not to like the sort of glue and rocks and pizzas examples because a lot of times those are examples that someone has figured out a way to construct something that makes it break. But in general, people don’t type into Google like how many rocks a day should I eat? Right? But people do type things into Google like where should I go to vote? You know, and things like that. And you know what you would find with AI at that, at that point the models is they would make a guess at where you should go to vote. And it wasn’t always correct. And sometimes it was where you should have gone to vote like four years ago, but your award had changed. Sometimes it was about give you regulations about voting that actually applied to another state about the level of ID you needed or something like that. And so it just was not very good at that stuff. So that was the first thing research, just a lot of stuff where direct information queries that have impact in people’s lives.

Mike Caulfield [00:06:40]:

It was getting wrong. I mean I think the other pieces of it. So at that point, to get onto something good at that point kind of talking about it in the stages of AI’s progression. One of the things I did notice eventually, especially, oh, I don’t know, maybe 20, 23, I guess it would be, might even be later than that, was that they actually could simulate reasoning fairly well. And I mean simulate. I don’t mean they reason, they don’t think we don’t, we don’t want a computer that thinks, by the way. It just be really clear. It’d be like really ethically problematic if we were directing things that can think to do things.

Mike Caulfield [00:07:20]:

But they, they can sort of simulate that and you can react to simulations. I mean this is not. Anybody in education knows that you can make a simulation. People are like that’s not real, that’s not the real thing. And they can react, but they could provide a simulation of an argument or something like that. And that was my first interest in them was, was thinking about, okay, well look, they’re not that great at factual matters, but they can sort of simulate the structure of an argument. And I think that could be useful in an educational sense. So that was my first sort of take on them.

Mike Caulfield [00:07:51]:

But obviously things have evolved since then.

Bonni Stachowiak [00:07:53]:

Yeah, that’s what I’d love to hear about next. So I’ve been having so much fun watching every video you’re putting out and reading everything. And what’s been really fun observing is just, I Sense really your curiosity starting to really get fueled and you’re making mentions of spending weekends and time when maybe it ought to have been downtime for you, but just you’re really getting into major experimentation mode. So tell us then about as you start to see. Gosh, it’s kind of this whole argumentation thing. I know that’s been big for you. You’ve actually influenced me a lot to want to learn more and recognize the importance of that, of just critical thinking and to be a good citizen in the. But tell us about these sort of experimentations where you may have entered a state of flow in terms of I really want to just test this thing.

Bonni Stachowiak [00:08:43]:

And what were some of the experiments that you were doing there?

Mike Caulfield [00:08:46]:

Yeah, so then the piece that really started to fuel my interest was when they added the search capability to these systems. And so the search capability is important in a number of ways. I mean, one is that maybe when you ask, where do I go to vote? It’s not giving you where you should go to vote. The year the model was trained, you’re actually going. It’s going and getting a search result and presenting you that information. So it’s important like that. But I think that the exciting thing about this is that I have worked teaching search for like a decade and a half and people romanticize search, but I have watched classroom after classroom of students struggle with is a skill. It takes a long time to learn that skill and.

Mike Caulfield [00:09:33]:

And most people don’t really master it. Right. And so the question I started to pursue was, okay, so we can kind of produce this simulation of reasoning over here. And I had been working with that, but. But it, it was getting things wrong. And then over here we have search. And the interesting question for me became, well, what if we could have it sort of simulate reasoning about search results? What would happen then? And what I found doing that is that when you have it simulate reasoning about search results, it actually does pretty good on factual matters. It actually acts like, I’m not going to say like a master fact checker or anything like that, but it does better than the average person at going through, walking through a set of search results and saying, okay, well here’s what we’re seeing over here.

Mike Caulfield [00:10:26]:

There’s a group of scientists that think this. There’s another group that think this. And really kind of giving you a summary of that, of that search process. And so those were the things I worked in with, something I now call deep background, this sort of super prompt that you can put into Claude this GPT that you can use on OpenAI. And in that I found that really interesting. And a piece of that that also interested me was that having people interact with this AI not as a thing with an opinion that you’re arguing with, which is just people’s natural inclination, but as something where you’re like, hey, go out, search the web for this information. Give me some summaries about how opinion breaks down on this. Who tends to think this? Who tends to think this? How does industry funded science compare to the non industry funded science and do these sorts of breakdowns.

Mike Caulfield [00:11:20]:

And it turned out to be really shockingly good at that in a way that even myself, I’m fairly known to be good at this stuff in that sort of manual way was finding that it was getting to some answers that I necessarily wouldn’t have gotten to.

Bonni Stachowiak [00:11:37]:

This is one of those times when I wish that this was a podcast that incorporated sort of theme music throughout because I feel like there needs to be a little commercial break. It’s not literally a commercial, but I want to give listeners the world’s fastest refresh on what Mike is very well known for and that is his sift fact checking model. Be. But I also want to tell you if you are not as familiar, go back and listen to those episodes because it goes into a lot more detail there. But let’s just do a quick recap. So S is stop. So one of the things that Mike mentions with this deep background, I’m finding myself really having fun to stop myself and then set it aside for when I have a chance to be at my computer on the big screen monitor and all the things and do that. So if I’ve got some sort of emotional, visceral, some kind of reaction, I’m gonna stop.

Bonni Stachowiak [00:12:23]:

And then I is investigate the source. F is to find trusted coverage and then T is to trace back to the original source. So my first question about this. What, what did you find? Or was there a harder part to get it to do for you? Like of those, those four letters, obviously the S is more. I think the S is more personally based. So you can’t like get it to control my feelings. But like, was there a part where you got like, gosh, it’s really not good at this, but how could I find a prompt that could get it to be better at this? Was there any of the sift that was particularly challenging or just all equally so for.

Mike Caulfield [00:13:01]:

So yeah, I haven’t thought of that. But so it’s, it’s excellent at the find trusted find better coverage. Right. It Does a really good job at finding sources. And I think that’s something that people don’t necessarily think about with these technologies is it’s not really. Everybody wants it to be like this sort of battle between, oh, we had search and now it’s getting replaced by A.I. or, or, oh, this is, this is horrible. A.I.

Mike Caulfield [00:13:27]:

is taking over search. And it, it really, the two things really work together, right? Like you, you do want to get eventually to sources. And one of the things I found is that with AI you can discover a broader set of more relevant sources if you know how the, how to prompt it. So it works really well with that. I think the place where it maybe struggles most is the trace. I’m much more, I can much more quickly, for example, if I’m looking at a, if I’m looking at a photograph and I’m trying to figure out where did this photograph come from, specifically who took this photograph, when and where, trying to find a very specific. And usually you do that by tracing it to an archive. And it hasn’t done as well with that.

Mike Caulfield [00:14:06]:

Right. I can, I mean, I think it can do better than a lot of untutored performance, but I can much more quickly trace something, you know, a historical photograph to the Getty Archive or something like that. And I think it’s part of the way that it approaches search in those cases. It’s still sort of sending out a wide net. It’s not great at visual recognition, but the trace piece I think has been a bit more challenging. But yeah, the investigate the source, the find better coverage, even the stop is a little bit easier because I think, I don’t know what your experience is, but my experience is a lot of people get keyword paralysis when they’re searching, right. So they see something online and they open up the search box and they’re like, I’m going to fact check this. And then they’re like keywords and they kind of just freeze.

Mike Caulfield [00:14:56]:

Like first keyword is coming into my head any moment now. Whereas in using AI, you can often feed the full claim in there, right? You can often just take the claim and put it in. And so I think there’s a little fluidity there. But the trace, the provenance is always a problem with AI. AI doesn’t naturally think in terms of provenance, in terms of how it got this piece of information. It’s a little bit of a bolt on afterthought. And so it’s probably not surprising that that’s the one place where I don’t think it’s up to par.

Bonni Stachowiak [00:15:26]:

When I first started learning about SIFT, I felt very insecure and scared and none of us enjoy looking. Like we somehow missed, you know, a huge part that other people got in their education. You know, that, like, it’s, it’s. It felt very vulnerable. But as soon as I started get shifting from teaching myself about it and just getting over myself and like, I would do some. Some YouTube videos and things just to show my, okay, I’m gonna learn out loud. You know, I’m just, I’m just gonna try this out and see what happens. I think that was good for me.

Bonni Stachowiak [00:15:59]:

But when I started teaching it to students, and still to this day, and you and I have exchanged over social media using the word magic, and I know neither one of us literally actually, like, believes in magic, but it feels like magic. Like, I, I’ve never experienced anything like that in my teaching.

Mike Caulfield [00:16:19]:

Oh, yeah. You know, the key. The key understanding there. And I think this is, this is what’s coming to me with the AI stuff as well as I think an opportunity. The key understanding from an education perspective is a lot of things that we were looking at and we were thinking were critical thinking problems with students turn out to be critical doing problems. Right? And just meaning that the students are thinking, but they just start. They see something online and they just start thinking, thinking, thinking. And it’s like an engine running without oil.

Mike Caulfield [00:16:52]:

You can kind of hear the gears grinding, and you’re like, slow down. Let’s. Let’s put the oil in first. Let’s. And then let’s get this done. But you’re just. They’re racing ahead to the thinking before the doing before the getting some basic information, getting, you know, understanding what the source is, understanding the information environment, what other people think. And once they did that first and then they came to the thinking, suddenly I’m looking at these things and like, I remember one time.

Mike Caulfield [00:17:17]:

So we did a bunch of educational research on this, right? And you pair the post test with the pre test, right? So we’re doing pretest post test. You pair the post test with the pretest and like, occasionally you mess something up. The whatever, right? And so I paired the post test with the pre tests early on. And I’m looking at them and I’m like, oh, I’ve munged this somehow because I’m looking at, I’m looking at. It’s in Excel, but I’m looking at just the cell that has the students pretest in it in their pretest answer. And looking at the post test Answer. I’m like, well, that’s obviously not the same student, right? This student here, like this student here doesn’t know what the heck they’re talking about. And this student over here, they sound like they’re in a graduate seminar, right? But I went through it and it’s paired up, right? It’s the same student.

Mike Caulfield [00:18:05]:

It’s the same student. And the difference again being that students had got into such a habit of just going out, just looking at something, just sort of. Just sort of doing. Doing. No, sort of work before the thinking. The work before the thinking. And I think that that’s a piece too that we’re trying to bring to AI as people use. AI is again, like, what is the, you know, it’s the doing piece, right? It’s the doing piece that I think we always fall down on.

Mike Caulfield [00:18:31]:

And I’m working on this issue of follow ups in my main thing right now with AI and AI search is to get people to not think of it as a single transaction where I put something in, I get something back, and that is the answer. And that’s what I’m seeing students doing right now. And I have a thing I’m developing with some, some others about follow ups and how to take some of these follow ups, like give me the evidence for and against this claim. Simple follow up. And what we’re finding is that if you ask the AI a question, even just throw in a claim, get a response from the AI, The AI says, oh no, this person is well known as the only person I’ve met Washington and Lincoln because of their age. And then you follow up and you say, what is the evidence for and against the claim? The AI runs through it and then it comes back with an answer that says no. It’s actually impossible for this person that voted for Washington. They lived in Connecticut.

Mike Caulfield [00:19:26]:

There was no popular vote in Connecticut in 1789, right? This is magic. This is magic to get students to think of these responses as not a single transaction, but as something where they’re trying to get the AI. They’re coaching the AI through a process that they have some idea about. Not to get a specific answer that they want, but to look at the sorts of sources that matter for the question. Like academic sources, how to sources. If you’re trying to figure out how to fix your sink, it’s not always academic sources or in this case just weigh the evidence for and against a claim and realize, oh no, actually the initial response the AI gave was wrong. And once you ask it to actually weigh the evidence it comes back with a correct answer. So this idea of this being an interaction, and I don’t even like the term conversation because I think that anthropomorphizes too much, but this idea of this being an interaction where you’re trying to get the.

Mike Caulfield [00:20:24]:

You’re kind of sending the AI up like this little drone above the information environment, and it’s kind of mapping out the territory for you so that before you kind of go trudging off into unknown woods, you know the lay of the land. And that was a very long answer, but that’s where I’m excited about it is this sort of interactive exploration piece and getting students to do that.

Bonni Stachowiak [00:20:46]:

All the words that you’re using are resonating so much and you actually anticipated. So it doesn’t matter if that was a long answer, which it didn’t feel long to me, but you anticipated where I was hoping we could go next. Because when I think about. Because I have been experimenting along the way with these custom GPTs that you’re building and incorporating them into to my AI workflows and things, but it has made me nervous because I have experienced so much of that magic where I use alternative grading, where if you get it wrong, I’m almost just giddy because it’s just like, if you get something wrong, that often is such a sign that you’re actually thinking critically. Because if you. If you get stuff right, it’s like the. All the research on retrieval practice, you know, if you’re getting it right, you could have just guessed and gotten it right anyway. But if you experience that friction.

Bonni Stachowiak [00:21:37]:

I don’t know if friction is the right word, but. But just so a common one. That’s one I’ll give. I’ll give students, here, here’s a list of. Of 7 things you can choose from. And I’ll. And I’ll just set it up in my instructional design workflow. I love, like the work of Mia Zamora and Alan Levine, where Mia’s come on the show before and talked about how do you structure a class that you’re teaching where you don’t know what the topic’s gonna be that week and just.

Bonni Stachowiak [00:22:02]:

Just leaving space for it. So I’ll just have this blank slide in my Google Slides and I’ll set it up a week ahead of time. Okay, you gotta go grab some latest stories and everything, but some of this stuff gets so heavy. And so I’ll literally have at the bottom, if this just feels too heavy for you, here’s a fun one. And you know about this from the last time you were on. Of course, a fun one is what’s the right way to put the toilet paper roll on?

Mike Caulfield [00:22:24]:

Yeah, right.

Bonni Stachowiak [00:22:25]:

But another fun one is a story from the Onion and it’ worker at Amazon just comes off. I don’t remember the exact thing, but a 4000 hour shift or something. I mean, it’s like, it’s absurd just even in the headline, let alone if you went to go read it. And that is often where they’ll. And I have them screencast themselves, so I can literally see their reactions. I’m like, okay, I got to investigate the source. Most of them have never heard of the Onion. So then they’ll go and look it up and they’ll be like, oh, this is satire.

Bonni Stachowiak [00:22:54]:

A decent chunk of them can’t go from there yet. So they’ll just be like, this is satire. So I guess, and I don’t mean to sound condescending, but this is going to sound condescending.

Mike Caulfield [00:23:05]:

But like, it’s, it’s like we found this too, you know that, that the first round that they do it.

Bonni Stachowiak [00:23:10]:

Yes.

Mike Caulfield [00:23:10]:

They’re not even used to thinking about what that means. Right. You know, and some people get that first round and they just slot into it and that’s great to see. But in the first round, very often they’re not used to thinking about what that means. And one of the things that we started doing was we started doing this expectations thing. And we talk about this in the book Verified, where instead of asking people whether something was true, we shifted to this question of, is this what I think it is?

Bonni Stachowiak [00:23:35]:

Yes. Yes.

Mike Caulfield [00:23:36]:

And trying to get students to even stop enough to develop an expectation of what they were looking at. Right. Because one of the things that really saves us is this sense of surprise. Right. And if we feel surprised, then we can ask, well, why am I surprised? But one of the things that often happens with students is because they’re not developing an expectation, they’re not feeling the surprise. And they don’t feel the surprise. They can’t really analyze the surprise. So thinking about just stepping through and even before they click it, just saying, hey, what sort of source do you think this is? Okay, well, I think it looks like a newspaper.

Mike Caulfield [00:24:11]:

Okay. Now you go through, now you look at it and it’s like, okay, it’s satire. Okay, well, what would be the difference between your expectation, you know, you thought it was a newspaper, you’re interpreting as newspaper. Now it’s satire. In what way? Right. In what way is that going to shift it it’s kind of like a Bayesian approach to thinking about how people think. And that, that piece, I think, kind of comes through in some of the stuff that we do later. But.

Mike Caulfield [00:24:37]:

But part of it is, yeah, slowing down even enough to develop an expectation or have. Have a. We call the fuzzy expectations. I. I don’t expect you to think, oh, well, this is probably a newspaper from the northeast of this one, but just a fuzzy. It feels like something newspapery. Yeah, that sort of thing, I think. But really interesting to watch students go through.

Mike Caulfield [00:24:59]:

What you said, though, has me thinking about another piece of this that I think is so important with AI. One of the key things that informed the way I think about AI in education was I wrote this, again, this sort of, whatever you want to call it, fact check or whatever, this deep background thing. And at some point I developed this thing in it where it went through the first pass, and then if you typed another round, it would go deeper into it. And it did what I wanted, which was another round says, okay, I’m going to take what I said in the first round. The elements going to take what it did in the first round. And then I’m going to look for sources that maybe question that and some sources that support it. And then I’m going to report back and say, okay, I tried to kind of hammer on this a little bit, and this is what I found, and it worked like I thought it would. But the thing that surprised me was the feeling I got when it would come back and say, actually, this second round has revealed some concerning information.

Mike Caulfield [00:25:58]:

And I realized, oh, that’s a piece of it. Right? That’s a piece of it. That’s a piece of what we’re missing with AI is the journey, right? It’s not just that the AI comes back with this answer. It’s not even just that we’re offloading things to AI, but searching for information is a journey, and we experience it as a journey and we process it as a journey. So even though I wasn’t doing that research and going out and looking at all these things, even the AI coming back and saying, hey, this is what I think it is. And then coming back and saying, oh, actually looking deeper, I found some concerning information. Like, there was something that was a relief to me there where, I don’t know, I just could process that better, you know, then it just. Even better maybe than it getting a perfect result the first time.

Mike Caulfield [00:26:46]:

Every time like that stuck with me. And it stuck with me because again, I think we’re set up to These investigations we do, we’re set up to process them as an intellectual journey and we short circuit that if we get something back that seems fully formed from the mouth of Zeus. So that piece really I think shifted my thinking about this. How can we get a lot of these benefits of AI but still preserve that feeling of a journey? I mean, I think it’s okay that AI looks at 100 different documents so that I don’t have to go through 100 different documents. I think that’s probably good. But at the same point having that sense of, of discovery and maybe I ask a good follow up that takes it in a different direction and it’s able to say, oh actually now that we go this direction. I do notice that all the sources that are saying this comet might be alien technology are very popular sources and all the science sources seem to be pretty clear it’s a comet. So that’s the sort of thing preserve that sense of journey in it.

Mike Caulfield [00:27:51]:

And I think that people do talk a lot about the cognitive offloading. I think that’s really important. But this is a very specific thing that I think is addressable in the way that we teach students to interact with these things and the way that we teach them to react. If suddenly they come up with something and the AI comes back with something that kind of contradicts what it said before. To see that as great, that’s discovery and make sure we preserve that feeling of discovery in the way that they interact with this technology.

Bonni Stachowiak [00:28:21]:

You were saying earlier and I’m gonna. Words matter. I mean, so you’re saying you don’t really like the use of the word conversation. You’d prefer the word use or it’s more precise to use the word interaction. Talk more then about these three co things that I’m hearing a lot of co reasoning, cognitive offloading. And then I think I saw you read perhaps this is fuzzy. I have a question mark in my notes. Being a cognitive apprentice, did I see you using that?

Mike Caulfield [00:28:50]:

Oh yeah, yeah, yeah. Okay. So three different things. And so co reasoning, I mean reasoning along. I don’t mean that the machine is reasoning, but I mean that you are going through a reasoning process. And this thing is, you know, the co pilot in, in an airplane is not necessarily the pilot. Right. They’re there, right? They’re there to assist the, the pilot.

Mike Caulfield [00:29:10]:

And that’s what I mean by the co reasoning piece. They’re here as, as someone to assist in that exploration that you’re doing. And it’s not, you’re not necessarily interested in Its, you know, its opinion. Right? I, I see this thing all the time where people start arguing with it and I don’t understand it. I don’t know. That’s not going to help you. I mean, one of two things is going to happen when you argue. It’s either going to capitulate, in which case you want, like, did I just bully the AI into agreeing with me? Or it’s going to dig in, in which case you’re like, why is it getting so stubborn? Like, you know, I know I’m right.

Mike Caulfield [00:29:45]:

Like, it doesn’t strike me as a particularly good interaction. On the other hand, the idea of CO reasoning is, look, we’re exploring the space together. The AI is good at some things. I can’t look at 800 sources in like 7 seconds. It summarizes half decently. I know it fails sometimes, but honestly, it summarizes about as good as people do. Your average person does. People don’t want to talk about that.

Mike Caulfield [00:30:10]:

But people mess up summary a lot too. But I want to be. One of the things I’ve been saying is, don’t be in the AI process, be above the AI process. Right? You are there and you’re trying to guide this sort of thing to help you with your explorations, but you’re there, right? You’re above it. And what I see when people start to argue with it, this conversation thing, is they’re in it and I see them sinking deeper and deeper in it. And I don’t think it’s for the stuff I look at. For certain stuff that may be what you want. Maybe you want to simulate a job interview, in that case.

Mike Caulfield [00:30:43]:

Yeah, back and forth, whatever, be in it. Like make it a simulation of something in life. But for the stuff where you’re exploring information, I want people to be above it. And that’s part of the CO reasoning idea. The apprentice piece is just that, the fact that they can model some of these things, like you can model scholarly writing, it can model, you can say, show me how a sociologist would approach this question. And it will do a pretty good job. Not perfect, but a pretty good job for a relatively standard question of showing you how a sociologist might go about thinking about something. We’ve never had that ability to get that on demand before.

Mike Caulfield [00:31:22]:

In general, you had to find a sociologist to demonstrate the thinking because we’re a society of written products. So you see the product, you see, like the paper that the sociologist writes. But you don’t see how a sociologist might go about thinking through an issue unless they’re in the classroom, watching a sociologist think through an issue. And so I think there’s some opportunities there. And that’s the cognitive apprentice idea. And then what was the third piece of that? I forgot?

Bonni Stachowiak [00:31:50]:

Cognitive offloading.

Mike Caulfield [00:31:52]:

Yeah. So offloading. So offloading is. This is, I think, this really big concern that. So if you think about our memories before Google, or if you think about our knowledge of a place before Google Maps, right? Before Google Maps, like, you move to a new place and actually you learned the layout of the place, right? And now after Google Maps, you move somewhere and you’re there three years and you still don’t quite know how this street connects to the street here, or when, you know, you get in your car and it just tells you to take these turns, right? And that’s probably fine for maps for the most part. Like, I don’t, I don’t think that that’s a huge loss. And I, you know, and I remember being in the car with the big map trying to figure out where you’re going, and it wasn’t safe doing that. Like, like there were some big issues with trying to read a paper map while you were, like, had half a hand on the wheel and half a half a hand trying to, you know, make it not blow up in your face.

Mike Caulfield [00:32:51]:

But a lot of learning involves us digging into details, mastering details. A lot of our way of thinking isn’t just about sort of doing reasoning without having any underlying knowledge that’s stored in our head. It has to do with stuff that’s stored in our head. So the worry with cognitive offloading in AI is, hey, if we give AI all these tasks to do and it kind of does all these things that seem. Seem menial and they seem kind of like a drag to do and boring, then we end up at the end of a process of looking at a question, and we actually don’t know any of the underlying facts because AI has handled that. We actually haven’t really sort of sat and struggled with the reasoning pattern because AI has handled that. And so we get to the end of this and we haven’t actually developed any skills that would allow us to approach the next question with more facility. And so that’s the piece of offload.

Mike Caulfield [00:33:49]:

I think it’s a big issue. But I do think one of the ways that we address that you come back to this is to think of these things as a journey where maybe AI is going off and doing this stuff, but it’s coming back, it’s explaining a little more what it did, and there’s Just a process where you’re going through it. And so the question ends up being not between, like, AI offloading, cognitive offloading with AI and nothing. The question becomes like, there’s this concept in education of scaffolding, which is, hey, maybe I’m not able to do the full thing yet, but if you could do the pieces I can’t do, then I can do the. Concentrate on the pieces I’m learning. And then at the end, I’ve learned some pieces. And then slowly we start to peel off the scaffolding. And then there’s this concept of offloading, and the two things are just the different sides of the same coin.

Mike Caulfield [00:34:41]:

And it comes down to, like, how do you structure it? And so what we want to do is we want to structure that interaction so that it’s scaffolding, so that it’s doing the sorts of pieces that we can’t maybe do for ourselves yet, but it’s encouraging us to do the pieces that we can. And slowly, over time, hopefully, that scaffolding comes down.

Bonni Stachowiak [00:34:59]:

I mentioned how intimidated I used to be early on when I started learning about this stuff. And then once I got hooked on the magic, just kind of. That all just falls away, because it really does. It really does. Just when you feel as concerned as I suspect that both of us are about our country and about what’s happening in the world, it really can feel like you’re doing the best work out there to help us.

Mike Caulfield [00:35:26]:

The information environment has gotten really hard to navigate, and most people throw up their hands and give up. And so I. I know this is debate about AI tools and so forth, but if we can teach people to use these tools to get contextualization of the things that matter, and if they can get good enough at it to help their family, their friends, their community better understand things that really matter to them. I’m not saying everyone has to feel this way, but for me, I feel like a moral imperative to do that, because maybe it’s just that’s my place in this, and different people have different places in it. And maybe the place that another faculty member has is actually, look, I’m going to be the place where there’s no way I. In this class and the students are going to. And that’s fine. But I think for me, my ability turns out to be how to show people to use technologies to increase their understanding, context, and awareness of issues in front of them.

Mike Caulfield [00:36:23]:

And this is now the technology we have. It’s an incredibly powerful technology, and I just think that it would be again for me, it would not be. I don’t think it would be a moral choice to say, well, no, just do it the other way, which we know has a lot of flaws and people struggle with. Don’t engage with this way, which can be quite powerful. Again, I want to be really clear. I’m not making a moral judgment on anybody that finds their place in this thing. But we absolutely do need a set of people that are working with this technology that figure out for people that want to use it to get quick context on these things, to better understand the issues that are popping up in their feed, to make sure that they’re not bamboozled by a bunch of stuff that’s, that’s just pushed out to them and spun in these ways that just, that just don’t stand up. I think we got to do that.

Mike Caulfield [00:37:16]:

That’s the tool they’re going to go to. That’s the tool that they’re going to use. So it doesn’t have to be everybody, but some of us do have to engage with this and show them how to use it effectively. Just. And if we don’t, I mean, I do think that’s on us.

Bonni Stachowiak [00:37:30]:

One thing that has really helped me draw hope in that I could have something to contribute to this work that you say we need to find our place in this thing is supporting you in your work. And you’ve actually made some explicit asks of people. So you’re talking to a decent chunk of people in higher education now. What would you like to ask us to support your work? And how could we do that, honestly?

Mike Caulfield [00:37:52]:

So I would love people to try the Claude super prompt at Deep Background, which is@checkplease.neocities.org you can get it and you can drop it in Claude or the GPT called Deep Background. I just like people to try it on things because the thing I struggle with most is if you’ve seen the stuff, act like it does when we set it up and we prompt it this way. And, and you’re like, that’s not my thing. That’s. That’s fine, that’s fine. But I do feel like a lot of the conversations and resistance I have are, are, are from people that maybe try to try, you know, typing in a few things like I did in, in 2023, 2022, and just getting horrible results back. And so I, I don’t know. I mean, I’m.

Mike Caulfield [00:38:37]:

I guess I’m not a good pitch person. I should be like, oh, you should subscribe to my substack. But I Don’t charge for my substack. I don’t. Whatever.

Bonni Stachowiak [00:38:44]:

That’s really good.

Mike Caulfield [00:38:45]:

I’d like you to try out some of the tools and just see if they resonate with you. See if they shift just a couple times, you know, and if it’s not your thing, it’s not your thing. But what I do find is for some people, it turns in the be, it turns into be their thing. I’d like people, if people could follow the substack. It’s free and I’ll be talking a little bit. I’ve gotten into AI mode, which is looking at how to use AI mode, which is the new Google tool, which you don’t have to sign up for a LLM. It’s not, you know, whatever. It’s just.

Mike Caulfield [00:39:13]:

It’s just a way. It’s just a new feature of Google. It’s not. It’s not the old thing. It’s not. AI summary is something new. I’ve been looking at ways to use that effectively and there should be some stuff out on that that I’m doing. And yeah, I just want people just take an hour to try these things and then see if it shifts what you think is possible.

Mike Caulfield [00:39:32]:

And if it doesn’t, that’s great. But if it does, then we can, we can move on and talk about, like, where we want to take this.

Bonni Stachowiak [00:39:39]:

This is the time in the show where we each get to share recommendations. And since I started with music, the Sound of Music, I’m going to end with music, although an entirely different. I came across a song by an artist who I wasn’t familiar with, Tom Misch. But the song features an artist that took me right back to my younger days, De La Soul. So the song is called It Runs Through Me by Tom Misch featuring De La Soul. Tom Misch is a English musician, producer, and this particular song is in the genre of neo soul and rhythm and blues. And it’s got some jazz, some bossa nova beats to it. It’s got some hip in the middle from De La Soul.

Bonni Stachowiak [00:40:24]:

It will play in the soundtrack of my mind many, many days in recent weeks. And then of course, just because, you know, your mind does this, but sometimes algorithms do this. I came across the Tom Misch Tiny Desk concert, which gave me even more enjoyment out of his songs and getting to see him perform in that context. And then the last two ones, I want to say I started thinking about De La Soul and so I graduated from high school in 1989, so no wonder that was a pivotal time.

Mike Caulfield [00:40:55]:

Yeah, yeah. Yeah, yeah.

Bonni Stachowiak [00:40:57]:

Which I didn’t know. I had to go back. Speaking of fact checking, I had because I was like, I have. Sometimes my timing will be off and I’ll think that something happened in a certain life time in my life, and I’m wrong. Oh, I was dead on. So, yeah, 1989, that’s when a big album of theirs came out. So there’s a wonderful song called Me, Myself and I. And then the magic number number.

Bonni Stachowiak [00:41:16]:

So those are my musical non AI. I love it because I do experiment with AI and then it’s just fun sometimes when you see something. No, only humans could do that. Only humans could generate this incredible kind of music. It was so fun. It was so, so fun. So those are my recommendations today.

Mike Caulfield [00:41:34]:

So for my recommendations, one thing I’ll say, just this is on my mind. This guy named on. On Substack, there’s a guy that writes a substack called Reasonable People, which for me was always one of the better blogs about thinking about misinformation in information and just like, what does it mean to be reasonable people? What does it mean to try to figure things out together and save Tom Stafford, the substacks. Reasonable People. And the reason I mention it is he just took a break from his position at University of Sheffield. He’s trying to figure out what he’s doing. And I do not want his writing to disappear. I want him to put time into that because it’s just valuable.

Mike Caulfield [00:42:16]:

So if you are a person that subscribes to Things on Substack to check out his blog, Reasonable People, and might give him a little encouragement as he’s trying to figure out what he does. The one other thing recently I’ve been playing this. I don’t know if we call it a sport. Yeah, it’s a sport. I’m sorry, Pétanque. Have you ever heard of Pétanque?

Bonni Stachowiak [00:42:36]:

No, never.

Mike Caulfield [00:42:37]:

Pétanque. Yeah, yeah, it’s kind of like bocce ball. Like you have these metal balls and you kind of go down to a Pétanque court and like, you throw them, you try to get them to the close to this thing called the jack or the cushion. And, you know, and then you walk over there and you throw that somewhere else and try to get the balls over. It’s. It’s completely an old man sport. And I think I’m just. I just want to get like.

Mike Caulfield [00:42:59]:

I think I’m prepping because I figure, you know, I’m getting. I’m getting older and I want to make sure I hit retirement with Some retirement skills. And so I’ve jumped early on the Pétanque thing, but I found it a pretty amusing sport because it is one of these sports where you kind of play against somebody, but there’s lots of time to talk. You spend a lot of time, you throw out a ball and then the other person looks and they’re like, oh, yeah, it’s gonna be hard getting around that. I think maybe you should hit that one that way and all this old guy stuff. And so, yeah, I become a Pétanque person, apparently, and see if you got a Pétanque club in your neighborhood and, you know, and you’ll meet a lot of people that are 80, but, you know, you’re gonna be 82, so, like, it’s time to face facts and get ready for your eventual retirement.

Bonni Stachowiak [00:43:48]:

But it sounds like if we meet people who are 80 there, we’re gonna want to be like them when we’re 80, for sure.

Mike Caulfield [00:43:53]:

Yeah. That’s the thing is I went. I went to it, and I’m like, yeah, you know, like, am I. Am I just going to be like, oh, look at all these old folks? And the answer is like, no, actually, I want to be like these old folks, you know, like, these old folks got it, got it, got it, got it down. Like, they come out every. You know. Oh, my gosh, they come out. There’s like.

Mike Caulfield [00:44:12]:

It’s like 40 of them that, like, will come out, like, in the morning and they’ll be playing Pétanque, you know, in the morning and some in the evening. There’s like a. There’s like a Pétanque WhatsApp. And they’re just, like, back and forth constantly on this and the other thing, and sharing their Pétanque videos. And how many times can I say Pétanque? If I was like, this sounds like me doing it for the algorithm, right? Trying to boost it. I’m like, Pétanque, you’re gonna cut of every sale?

Bonni Stachowiak [00:44:37]:

I don’t know what you’re selling, but.

Mike Caulfield [00:44:38]:

Yes, every sale, but yeah, check this out. The one other thing I’m gonna say about your intro, though, is I was in the Sound of Music as a kid, and I’m trying to remember which note I sang. I was the younger of the. The younger, younger boy in the Von Trapps. Which note is the younger boy in the Von Trapps singed?

Bonni Stachowiak [00:44:56]:

I don’t know. You mean which song is that? What you mean?

Mike Caulfield [00:45:00]:

Each of the kids has, like, a note, right?

Bonni Stachowiak [00:45:02]:

Yeah, I don’t know.

Mike Caulfield [00:45:03]:

Like. Yeah, I don’t know. Or I might have done far. I mean, I might have been far. A long, long way to go. And I was from New England. So like I said far. Exactly like that.

Bonni Stachowiak [00:45:13]:

This is cracking me up because I was trying to discipline myself because I was thinking, like, the Sound of Music maybe that didn’t quite land because I was like, I had, I had another thing where I was going to tell you it hallucinated. So it told me because I was wondering about this, but it doesn’t mean anything. So we put in words and it said that the, the. When I put that in chat GPT because I couldn’t remember which of the children said that line. It said Gret. Gretel. Gretel. Greta.

Bonni Stachowiak [00:45:37]:

Greta. The youngest one. You know, a predictive engine’s gonna go. Like, we see a lot of that name. So it must have been her. And it wasn’t her that said the line. But it doesn’t mean anything. So it’s so funny that you came full circle here with Sound of Music because.

Mike Caulfield [00:45:51]:

Oh, yeah, yeah, yeah. No, no. I, I, I, yeah, that, I, that was the, that was the beginning and I think the end of my acting career. I was just a tiny little kid, and of course I had a crush on Maria. Of course. It’s like, it’s like a fourth grader.

Bonni Stachowiak [00:46:05]:

Oh, see, I would have thought it would be the oldest Von Trapp sister, because there was a lot.

Mike Caulfield [00:46:09]:

Oh, that’s true.

Bonni Stachowiak [00:46:10]:

I am 16 going on.

Mike Caulfield [00:46:12]:

I don’t know. Maria, the Maria, they got, like. It was like community theater esque. And like, you know, in community theater, like, most of the people suck. And then there’s one person that’s, like, really good.

Bonni Stachowiak [00:46:22]:

Yes. And that would be Maria.

Mike Caulfield [00:46:24]:

Situation. Maria’s situation there. So.

Bonni Stachowiak [00:46:27]:

Well, we got to fact check sound music. We’ll get to fact check that. People will be writing in from all over the world. I love it. Mike, thank you so much for coming back on teaching in higher ed. I can’t wait for this to get out there and until the next time, too.

Mike Caulfield [00:46:40]:

All right, sounds good.

Bonni Stachowiak [00:46:44]:

Thanks once again to Mike Caulfield for joining me on today’s show episode and especially for wrapping us up there with another reference to the Sound of Music. I just so wish we had a picture of you at that age. All right, thanks to each of you for listening. Today’s episode was produced by me, Bonni Stachowiak. It was edited by the ever talented Andrew Kroeger podcast. Production support was provided by the amazing Sierra Priest. Would love to have you head over to teach in higher ed.com subscribe if you’ve yet to sign up for our weekly emails, you’ll receive the most recent show notes, links, and all those goodies, as well as some other things that don’t show up anywhere else but in those updates. Thanks so much for listening and I’ll see you next time on Teaching in Higher Ed.

Teaching in Higher Ed transcripts are created using a combination of an automated transcription service and human beings. This text likely will not represent the precise, word-for-word conversation that was had. The accuracy of the transcripts will vary. The authoritative record of the Teaching in Higher Ed podcasts is contained in the audio file.
