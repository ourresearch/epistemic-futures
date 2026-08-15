---
title: "Four Tips for Better Prompting"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-06-30
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/four-tips-for-better-prompting
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Four Tips for Better Prompting

*A generalizable and durable approach to investigating an issue with an LLM.*

## Full text

[](<https://substackcdn.com/image/fetch/$s_!pYJ3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b2fb73f-8efa-47f5-9b07-5f592000c4c0_1222x689.png>)Chart of tips described below

## Avoiding the information smoothie 

Before we introduce the tips, it’s worth asking what we are trying to accomplish.

The main focus of these tips is to encourage students to “avoid the information smoothie” effect when doing research on a subject. “Information smoothie” is a term I use to talk about the standard LLM response that when asked a question takes a variety of sources and blends them all up into a sort of milkshake. You get an opinionated and often sourceless response, one that often sounds quite authoritative.

This can be fine. The other day, I was trying to figure out how to choose the right-sized drill bit to pre-drill a wall for screws into a stud. I asked Google and got a great response. 

[](<https://substackcdn.com/image/fetch/$s_!UtBE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31692e7c-550e-437d-a84e-e13048371b8d_1190x458.png>)

For me this response — that you choose a bit that is as big as the shaft of the screw without the threads — was good enough for me to start drilling. That’s partially because the minute I saw it I realized I had looked this up before and found this exact answer, and partially because my sense of this issue is that this is an issue where there is a well-documented one-right-way answer replicated across the entire web. Also the TV I was putting up was less than 10 pounds and going into the exercise room where if it ever does fall down at most I’m out a $150 TV.

Those three things together — a recognition that this accorded with previous knowledge, a “one-right-way” sort of question, and low stakes — led me to value my time more than additional research and I started drilling. 

Academics have a hard time realizing this, but most information needs in life are like this, and that’s the reason people _like_ the information smoothie. A few years ago I made a call to my followers to share their most recent five internet searches with me. I then put them altogether, removed navigational and consumer queries (e.g. typing Amazon to get to Amazon.com or asking where you can stream a particular show) and analyzed them. Most of them were pretty low stakes questions with fairly agreed on answers. I am not particularly worried that people are getting the answer to what is “6-7 and why are kids doing it” from an LLM.

Habits are tricky things though, because what is a good impulse in one situation is not great in another. Our students bring a habit of consuming the instant response into areas where a more engaged approach is necessary. They worry that this is making them cognitively lazy and hurting their retention of information. They are correct to worry.

The solution is to treat researching with an LLM differently than asking Google if Tom Holland and Zendaya are still together. This means engaging with the LLM as a tool for investigation. These four tips are meant to put the student in the driver’s seat of the experience, tapping into the ability of an LLM to sort and summarize information while avoiding treating it as an Oracle of Truth. 

[](<https://substackcdn.com/image/fetch/$s_!pYJ3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b2fb73f-8efa-47f5-9b07-5f592000c4c0_1222x689.png>)

##  1\. Treat the first response as a draft

The companies selling LLMs often present what you’re doing with them as “having a conversation”. The LLM listens to you. It answers, and you listen to it. Back and forth, right?

Reject that. 

Here’s how I want you to think of what you’re doing with an LLM when doing a deeper investigation. You are providing the software with guidance to produce a answer for you on a subject, issue, or question of your choice. 

Do those things sound very similar? This first step will help you understand the difference. 

Let’s say that you are trying to better understand the American Revolution for a class. You type in “Were the British Responsible for the Boston Massacre?” The answer comes back. _The British created the conditions for the massacre, but the event was not planned or intentional._

[](<https://substackcdn.com/image/fetch/$s_!L1Gq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f9c33b0-939f-4861-9bd8-e6d524c059ff_990x747.png>)

Traditional approaches to teaching prompting often try to get the user engaged by encouraging them to a) read the whole response, and b) push back. So you do “But weren’t the colonists provoking them?”

Now you get another summary: _The colonists provoked the immediate situation but the presence created the larger crisis._

[](<https://substackcdn.com/image/fetch/$s_!5h_h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5184e00f-5f63-4370-be0b-3a1779787c3e_992x652.png>)

You push back again and get yet another response, not contradictory but with yet another focus and slightly different implication. The experience over time is disorienting. A final pronouncement on each question comes through, you read it diligently, you push back, a new revised final pronouncement comes through. You push back, and get yet another final pronouncement. 

As this process proceeds, you feel disoriented. Which is odd, because each round of this seems to be encouraging you to see the question as settled and closed. The further you get into the conversation the more mushy the LLM seems to get. It vacillates between different positions with little indication that the system recognizes it is shifting. You start to feel like you are wandering a bit lost through the topic. You can’t tell if you are seeing the same answer over and over in slightly different words or a genuinely shifted “opinion”. 

[](<https://substackcdn.com/image/fetch/$s_!iUQL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88701e09-8ba1-42af-b79f-5c9a9caf8b8d_990x728.png>)

Worse, days later you try and remember the facts involved and you can’t recall any of them. Or if you do, when asked where the information came from you have no idea. It’s not for lack of reading; after a half-dozen back and forths you’ve read a book chapters worth of text. It’s just… not particularly sticky.

Your problem here is simple. You’re using this software to get its “opinion” and it does not in fact have an opinion. You’re pushing back on a toaster. 

What does the “drafting” approach look like? Start instead with this:

> analyze: the british were responsible for the boston massacre

Then here’s my weird advice: don’t waste your time reading the reponse. This first response isn’t for you. It’s the LLM exploring the space. It’s the LLM talking to itself, using its little predictive text trick to surface issues. Skim the response at most. It’s a draft and you don’t need to read robot drafts. 

## 2\. Focus on the follow-up

Now that the LLM has done its one-minute writing exercise to limber up, we get specific with what we want out of our report. Remember, we’ve barely read anything here, we are saving our attention for better output than the dreck we are initially served by it. 

In the follow-ups we do two things. 

  * We ask for evidence or expert perspectives, and 

  * We ask for sources

If we want to learn something here, and not just drink the information smoothie then we’ve got to make sure that what we get back from the LLM is not blended up. We want the evidence it surfaces to be enumerated and its sources to be checkable. 

There are a wide variety of follow-ups that can get you the right slice of what you want, but I suggest two basic “starter” follow-ups for students. Choose either:

  * Give me the evidence for and against ______ with links to reputable sources, or

  * What do a variety of experts think about this issue? Provide links to the relevant sources.1

### Evidence For and Against

Let’s start with the simpler one:

> Give me the evidence for and against the british being responsible with links to reputable sources

Note that our focus on the follow-up move encourages you to choose the sources you want. Here I say “reputable” sources. But I could also say “scholarly sources” or “primary sources”. You choose, depending on what you need, but you have to _use your words_ and be _clear about what you want_. 

Here’s the [result of that](<https://chatgpt.com/share/e/6a42db82-b060-832f-b7df-482b049a53a6>). (Screenshot below is just the start. I’m using the basic version of ChatGPT here, without the “Pro” level).

[](<https://substackcdn.com/image/fetch/$s_!enF0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2642cd82-8cbc-4453-9086-cc816c88d887_996x531.png>)Some evidence for culpability

[](<https://substackcdn.com/image/fetch/$s_!b2Jc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49ff10e0-41a1-46b6-98a0-f6f1cb25b889_1014x443.png>)Some evidence against

In this case we get some of the same information we got in our back and forth, but here it is set up not as a ping-ponging opinion but as a set of facts that largely support British culpability but have some elements in tension. (Note that because we asked for reputable, it is pulling from the Park Service and Library of Congress pages on the event, but we could of course asked for something else, either scholarly work or primary sources). 

If you click the link and look at the conversation you’ll see it does end with a summary “decision” of course, but instead of engaging with an imaginary conversational companion you are engaging with the facts of the case. 

Note: I try to slim down these follow-ups so that they are memorable, but if you keep them in a snippets file you can level them up: “Give me the evidence for and against the british being responsible with links to reputable sources, rating the strength of each piece of evidence and the reputation of the source on this topic".

### Variety of Perspectives

The perspectives follow-up is a bit more complex, and often will give you a wider view of the issue:

> What do a variety of experts think about this issue of British culpability? Provide links to the relevant sources.

Plug this in and the response you’ll get will be quite different from the back and forth. The response I got, [shared here](<https://chatgpt.com/share/e/6a42d31c-eda4-832c-815b-127e7a73cd10>), talks about how legal scholars see it and how the colonist insurgents of the time saw it. But it also brought in wider perspectives. It talks about how propaganda scholars stress the public memory of the event was shaped by propaganda around it which is difficult to disentangle. And it mentions two scholars: 

  * [Hiller Zobel](<https://www.jstor.org/stable/1339722?utm_source=chatgpt.com&seq=1>), whose controversial 1970 book on the massacre emphasized the “radical recklessness” and “institutional impotence” of the colonists, claiming that failures of local governance led to the situation.

  * [Serena Zabin](<https://serenazabin.com/book/?utm_source=chatgpt.com>), whose more recent work stresses that seeing the soldiers as separate from the colonists is a mistake; the soldiers had many relationships in the community, and sometimes had worked together for the good of the town. Her work reminds us to understand this not as an invading army but as a group of soldiers firing on people who had become their _neighbors_. 

A bunch of these perspectives seem a bit to the side of our question. And that’s exactly the point. This particular follow-up helps us zoom out and think more broadly than a yes or no. It invites us to consider what aspects of this we care about. We are looking at history supposedly to find a yes or no, but why? For Zobel, in the chaos of 1970, it’s a cautionary tale about what happens when law and order declines. For Zabin writing in the 2010s, it is about how the community is fractured when the authorities who are also neighbors break neighborly bonds through violence. 

### These are base follow-ups, but you can extend

Once students build the habit of using these prompts they can modify them. A favorite modification of mine to the perspectives prompt is the “changed over time” lens:

> What do a variety of experts think about this issue of British culpability, and **how has expert opinion shifted over time (if it has)**? Provide links to the relevant sources.

This gets you something that puts the [experts in the context of history](<https://chatgpt.com/share/e/6a42dfa9-5e90-832e-a68c-20d7212a913b>) as well. Is it perfect? No, not at all. I noticed a number of little weird errors of summary and maybe you did too. But you can think of it as a mostly accurate map that can be used with a bit of caution to begin exploring the issue. 

Come up with your own modifications of these prompts, but keep the focus on exploring evidence and expert opinion, not talking to a chatbot, and you’ll be more engaged in the construction of your understanding and end up asking more interesting questions as well.

## 3\. Specify your output format

So I got excited when I saw the responses form the last round and jumped in. But you don’t have to.

If the sort of response that you got back in the previous turn felt either overwhelming or underwhelming, I’ll tell you a secret:

**You still don’t have to read it.**

You really don’t. If you start reading that response and it feels too much or too little or not the right format, _put it back in the oven and finish baking it_.

In particular, clarify how you want the information presented. Here’s a couple of ideas for that. 

### Give me the short summary

Maybe you’ll get to all that text about seven different experts or 15 different pieces of evidence but you need to get oriented first. 

Ask for a short summary:

> Summarize the above, 150 words, bullet points and links

### I changed my mind on sources

Don’t like the sources you got back? Ask for what you want:

> Keep the Park Service links and the Library of Congress links, but add links to relevant primary sources

### Put it in a table

Sometimes having evidence or persepectives in a table format can help you process them. Try something like this:

> Give me the evidence for and against culpability in a table along with sources and an initial weighting of the strength of the evidence

Or for the perspectives approach:

> Give this to me in a table that notes perpectives with associated scholars, works/primary sources, dates

### Dumb it down or smarten it up

I think many people can spot a too simple response and ask for it at a higher level. And it’s pretty straightforward to do that:

> Give me the above, but please write it at college senior level

The harder thing I find for people to do is to ask for it at a lower reading level if it is a bit above your head. It feels like a failure — I should be able to read this response, right? I should plow through!

I think this is well-intentioned but foolish. The truth is you’re going to be able to spot errors the LLM makes much more easily if it is talking at a level you can comprehend. Look at a response that is slightly above your head and you can’t help but feel it must be authoritative. Have it take at what ever level your 2 a.m. brain is capable of processing, and maybe you notice a couple cracks in its facade.

> Keep the format by explain this to me like I’m in high school please

Sometimes the smartest thing you can do is dumb it down, and not get wowed by the illusion of chatbot expertise.

### Get creative with formats

You can ask for anything. 

> Give me an annotated bibilography on this issue with links

or

> Present the expert perspectives on a browsable, zoomable historical timeline with links to major works

In general, the more creative your format, the more likely it is you’ll have to do a round or two of “debugging” making sure that it is formatted in a legible, accessible way. You may also see as you develop it that you have gaps needing filling. In the timeline below the big early 20th century gap, made visible by the timeline format, prompted me to ask to have that period of scholarship filled in.

[](<https://substackcdn.com/image/fetch/$s_!8k-C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2544fba1-530a-4bab-9267-8b7f82b2c0fa_1350x801.png>)Sources timeline

## 4\. Verify at the source

Do not lose sight of this: what you are getting back in these responses is a _map, not an answer_. It is a linked gloss and summary of the knowledge and thoughts of others. 

And the map is not perfect.

For one thing, especially if you are using the cheap or free versions of these tools, they are going to get some things wrong. Note the timeline in the section above, where every publication date is “January 1”, a formatting error resulting in false precision. Also Schlesinger date is off by a year (it should be 1918) and the Miller work cited as being from 1942 is actually from July 1943.

You know how I found that out? About the Miller date?

Hours and hours of research, and a deep background in historiography gained in graduate school under the tutelage of …

Nah, I’m just kidding. I majored in literature and linguistics for God’s sake. 

The way I found out was _[I clicked the link](<https://archive.org/details/in.ernet.dli.2015.212021/page/n1/mode/2up>)_.

[](<https://substackcdn.com/image/fetch/$s_!BFFn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0cfc14c-0f08-495c-9c5e-4f118cdb43d1_541x330.png>)

That led me to a public domain copy of the book, the third page of which is the copyright statement above.

Whenever I show something like this, I can always hear a certain part of my audience spinning up. “What! An error! And you have to check the date! How is this saving you any work at all!”

My friends, I say this with love in my heart: the totality of my labor here was _clicking a link._

And as long as I can deploy this arcane knowledge of “clicking links” and “checking things” I get a decent map of a space — whether timeline, table, or text — that forms a starting point for my exploration. The rest is up to me, but it always has been.

Of course, this checking is possible because we approach it as a knowledge map from the start. We ask for links, sources, and evidence in formats that are easy to verify. I think just as importantly, the output formats we ask for help remind us that it is a map, not an answer, and keep us engaged in the process instead of nodding our head and saying “You’re so right, Mr. Chatbot”. This is important not only for the checking of dates, but for encouraging us to go deeper and explore what’s out there, both on our map and off.

## The secret ingredient of AI information literacy is information literacy

There’s an interesting contradiction at the heart of the debate around LLMs right now, where two critiques are being advanced simultaneously:

  1. LLMs promote inappropriate levels _cognitive offloading_ , where students let the machine do the thinking for them, resulting in them never mastering important parts of what they are supposed to be studying. 

  2. It’s ridiculous to claim the reason people get bad results from using an LLM is that they are using it improperly. LLMs should produce perfect results even for people who use them poorly or not be used at all. Spending time showing people how to use these systems effectively is shilling for the companies.

I think the first point has merit. And I can see why people think that it leads to the second point. But it has never made sense to me. 

It’s certainly the case that the design of LLM interfaces is suboptimal. I’ve argued consistently that the chatbot interface is a bad model for these products when it comes to deeper work. It’s great for “Hey what drill bit do I use” but bad for “How do I think about this complex event?” Companies can and should do better. 

But the opposite of cognitive offloading is not “Only use products that are 100% accurate and truthful” whatever that could possibly mean.2 And it certainly isn’t “You should never learn how to better use your tools.”

I’ve struggled with this a bit, how people can hold both these views, and eventually came to a bit of a realization. I think a lot of people think that training around these tools is technology and platform specific, like showing people how to fix that problem you get in MS Word when you move an image.

[](<https://substackcdn.com/image/fetch/$s_!Ed29!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0b41cf5-265e-4a23-9f4b-2df3df77bd0f_583x285.png>)

In this view what we are teaching students when we teach them AI information literacy is how to fix a product’s errors. There’s only one place in life that learning to fix MS Word image errors will benefit you and that’s in MS Word. Obviously, that’s not a good use of instruction time. 

But I hope you can see this is not the case with AI information literacy properly conceived. The method here, to the extent you can call it a method, is not based in the product but in the nature of knowledge itself. It's about understanding first passes at things not as definitive answers, but as iterative drafts. It's about thinking through the sort of evidence you need to evaluate something and the sorts of sources appropriate to a task. It's about a conception of "what the experts say" not as some uniform voice, but as an ongoing discourse that evolves over time. And it's about seeing even informal explanations of things as summaries of information that came from somewhere, have a history, and could benefit from making that history visible.

All of this, but practiced in the specific context that students are doing much of their exploration already.

Is it work? Yeah, it’s work. But if this isn’t _our_ work as educator sand students, I’m not sure what is.

1

One is not really better than the other. In some situations the sort of question you are asking is one where there might be a variety of experts in discourse about it, and thinking about those expert perspectives on it is interesting. On other issues the “evidence for and against” framing might feel like a better fit. If you’re unsure, just pick one. 

2

It’s a meaningless statement, for reasons having to do with the context-boundedness of “accuracy” but that’s too much for this post.
