---
title: "The Gender Question"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2024
venue: "Aspen Ideas Festival"
source_url: https://www.youtube.com/watch?v=O7_DZtKdW9w
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 57
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# The Gender Question

*Speakers (inferred):* speaker_0=Antonia Hylton, speaker_1=Dan Savage, speaker_2=Lucy Sante, speaker_3=Blaise Aguera Y Arcas, speaker_4=Audience

## Transcript
**Antonia Hylton** [00:00]: All right, everyone. I think we're ready to get started. My name is Antonia Hylton, and I'm a correspondent for NBC and MSNBC. I'm also the host of our podcast, South Lake and Grapevine, and the author of a book called Madness. It is an honor to be here with all of you. I'm really excited for this conversation. It's still Pride Month, and yeah. [clapping] It's a party. It's a celebration, I think. But it's also a time for reflection, and I think we all know we're in a really critical moment in which the lives, uh, and experiences of LGBTQ Americans, but especially transgender and non-binary Americans, they are hyper-visible, and with that visibility comes a backlash, a debate, and sometimes peril. And so I couldn't be happier to have this group here convened for a conversation, and I don't wanna waste a moment. So I'm gonna jump in and introduce you to them. First, right next to me, we have Blaise Aguera y Arcas, a vice president and fellow at Google Research, leading a team working on AI, large language models, smart devices, technology, ethics, and privacy. He is also the author of the books Who Are We Now?, and Ubi Sunt?, and essays about the relationship between art and technology, and on physiognomy and bias in AI. Lucy Sante is a writer and artist. Her many books include Nineteen Reservoirs, Maybe the People Would Be the Times, and The Other Paris. She began her gender transition in twenty twenty-one, which she chronicled in her latest book, I Heard Her Call My Name. And last but not least, we have Dan Savage, a writer, advice columnist, and activist. He has been writing Savage Love, his syndicated sex and relationship advice column, since nineteen ninety-one. Is that right? [laughing] So we have to start here. The Supreme Court just announced that they would hear a case on gender affirmation care for minors in response to a law in Tennessee that has sought to make that form of healthcare illegal. What's all of your gut reaction? What are you anticipating? And anyone can start.

**Dan Savage** [02:21]: Nothing good-

**Lucy Sante** [02:22]: Yeah. Yeah

**Dan Savage** [02:23]: ... from this Supreme Court as constituted. Um, it is... I agree, it is a shame and a, a scandal that you have state governments in red states inserting themselves into the private medical decisions that parents and kids, in consultation with their doctors, are making in the best interests of those child, those children. We, uh, I live in Seattle. We're already seeing in the blue states, uh, gender medicine refugees, people who've left red states where they're being either stigmatized or attacked, as happened in Texas, where they declared any parent who would provide gender medicine to their child is a- abusive and should be investigated by Department of Children and Family Services. And so it has real consequences. Um, we used to say, like fifty years ago, forty years ago, when I first came out as gay, that all gay people were refugees because we had to flee our families, and even if we only moved to the other side of town, we were refugees. But for the most... You know, we fled from small places to bigger places to be safe. And now you see that, um, is true for the straight, usually straight, opposite sex, cisgender parents of trans kids because of this sort of legislation, and it's not gonna end well at this Supreme Court.

**Lucy Sante** [03:46]: Uh, not for the first time in American history, we have a physical fact that's being judged as if it were a moral decision. You don't choose to be trans. You are trans. And, you know, tell people this, you can't back it up because there's been no research, and there's been no research because there's been no funding. Um, the... it, it's just, um, kids are going to... There's been this moment of opening, this great awakening among the younger generation, which has made it possible for senior citizens like myself to also stop being... suppressing their gender. Um, and, um, people are panicking. They're overestimating numbers, all this stuff, and we're gonna, we're gonna be crushed probably. And, uh, if, uh, the new administration may try to apply this to the nation as a whole, um, the fact is that these transgender medicines for the youg- the youth are all completely reversible. If they did decide they, they made a mistake, they can revert back to their birth gender in a matter of months. So it's a fake panic on top of everything else.

**Blaise Aguera Y Arcas** [05:05]: Um, well, I guess [clears throat] for my part, and I, I feel the least, uh, qualified on this panel to say anything to this for a couple of reasons. Um, one is that, you know, I, I thank you for the super kind introductions. I also wanna make sure that I'm disclaiming that, you know, I'm, I'm not speaking as a Google vice president here. Um, you know, the, the book that I guess is the reason that I'm on this panel, uh, Who Are We Now?, is one that, one that I wrote, um, you know, very much on my, on my own time and with my own, uh, with my own resources and, uh, you know, is definitely not, not, like, the company line. Um, also-

**Antonia Hylton** [05:40]: We don't want the company line. [laughs]

**Blaise Aguera Y Arcas** [05:41]: So I have no intention-

**Antonia Hylton** [05:42]: We won't miss it. [laughs]

**Blaise Aguera Y Arcas** [05:43]: I have no intention to give the company line here. But, but also, you know, I, I... The book, the book was also not a piece of advocacy. Uh, you know, I, I have my own political opinions. I, I did wanna be upfront about those in the book because, you know, I, I think it's hard to, um, it's hard to even- talk about, uh, sensitive issues these days without having some kind of positionality statement, and I didn't wanna try and hide. Uh, at the same time, the point of the book was really to do a kind of, uh, forensic analysis of what is going on with identity and, you know, including gender and sexuality and so on, uh, widely among Americans, and not to make it a piece of advocacy from my own perspective. Um, personally, I am no more a fan of this Supreme Court or of this moment than anybody else on the stage, I think. Um, but, um, uh, you know, another thing that I'm seeing that I, I think is causing this, this, you know, this current moment is this extreme polarization that is taking place, not only in the US, but really all over the world, which I have a feeling, uh, is due to urbanization. Basically, as people have been concentrating in cities and cities, um, sort of progress faster culturally, the, the, the rate of cultural evolution is much faster in, in, in, you know, the, as, as, uh, population densities increase, that's led to a kind of pulling apart of the cities and the countryside. Um, and, uh, and as the cities become denser, the, you know, it's, it's almost like a tidal force that, that pulls us further and further apart. And the, and the trouble is that in American politics especially, um, there's a, a great over-weighting of rural interests because, uh, when we look at, at bodies like the Senate, you know, they're, they're, uh, they're apportioned by land area more so than by population. Same with congressional districts. So even as we pull apart, and even as more and more people end up in cities, the sort of political imbalance between rural and urban grows as well.

**Antonia Hylton** [07:36]: I wanna come back to some of what you mentioned there in terms of trends and demographic change here. But Lucy, I, I wanna hear some of your story.

**Lucy Sante** [07:45]: Mm.

**Antonia Hylton** [07:46]: Tell me about your... You, you wrote all about your transition back in twenty twenty-one.

**Lucy Sante** [07:52]: Mm-hmm.

**Antonia Hylton** [07:53]: What has it been like for you to tell your story in this specific political moment?

**Lucy Sante** [08:00]: Um, well, it was a weird feat of timing. You know, uh, uh, of, of course, um, so the, uh, the term of art in among transgender people, my egg cracked. That's not a metaphor I invented. Um, a person who is transgender but hiding it, um, is known as an egg. When they can't stand it any longer, their egg is set to crack. And mine cracked after some fifty-five years of suppression. Um, I was sixty-six when I came out, and, um, it happened very quickly. [clapping] Thank you. It-- A-after, after the, the glacial procession of decades, it happened like a lightning flash. Um, and it had to do... You can read it, about, all about it in my book. Uh, it had to do with, uh, artificial intelligence actually, with an app called Face App-

**Antonia Hylton** [08:58]: Yes

**Lucy Sante** [08:59]: ... where I was able to see myself as a woman. And it just un-- [snaps finger] the dam broke. And, uh, within two weeks, I had come out to my immediate circle. Yeah, like forty people. Um, and, and nobody-- I didn't lose anybody, by the way. Um, some people were startled. Some people had suspicions confirmed. Either way, everybody was cool. Um, and ever since, I've been, um, public about it, partly 'cause I'm a writer, and I feel that as a wr-- it doesn't apply to all writers, but as a writer, I've always felt that I'm not a politician, I'm not an organizer, I'm not a celebrity, but I have a responsibility to be a public witness. And in this case, I'm being a witness to my own transformation. And so yes, I've been explai-- my book came out in mid-February, well, since mid-January. I've been interviewed on average about four times a week, um, sometimes more than that. Um, so I, um, I'm kind of incapable of repeating myself, so it never comes out quite the same way. So I'm not bored. I hope you're not. [laughing] Um, in any event, um, I feel at home in my own skin for the first time in my life. I'd always been hiding. I'd always been [clapping] crawling, um, just, you know, un- uh, kind of ashamed of being myself. Um, hated looking at pictures of myself. And now I just, well, this is me. Um, it's kinda lonely, you know, because I... Well, for one thing, given my age, I live in a cisgender heterosexual world for the most part. I have gay friends, you know, plenty, but, um, the transgender people I know tend to be under the age of thirty, and that's a whole other generation. Um, I have a twenty-four-year-old son myself, who, as I enjoy saying, as straight as a highway in Texas. [laughing] But he understands. Uh, the only problem he ever had was trying to figure out how not to call me Dad all the time. So, you know, he can call me Dad. Um, in any event, um, I'm just-- Uh, it's-- Transitioning has made me brutally honest, um, incapable of dissimulation because of these layers of, of deception and contradiction and hiding. I was my own Stasi, you know? I was my own secret police for so long, and having that removed, I've been, you know, I've been carrying a piano on my back, my-- a grand piano on my back my entire life, and now I'm not, and it's incredible. Um, and I can only wish for everybody to have a similar experience to the one I had. But it's not given to all.

**Dan Savage** [12:10]: Whenever anybody says that the gay experience and the trans experience have nothing in common and attempt to divide trans people and gay people, I always point to that.

**Lucy Sante** [12:17]: Mm.

**Dan Savage** [12:18]: That you're perceived to be someone that you know or always knew or eventually come to know you were not, and being able to let go of-- to, to, to step into who you actually are-

**Lucy Sante** [12:26]: Yeah

**Dan Savage** [12:26]: ... which can be very upsetting and traumatic because you can lose people, and the stakes feel very high. That's what trans people and gay people share.

**Lucy Sante** [12:33]: Yes.

**Dan Savage** [12:34]: Like the essential core of the coming out-

**Lucy Sante** [12:36]: Right

**Dan Savage** [12:37]: ... risk. Um, I wanted to jump back for a second and talk about gender-affirming care and what we mean when we use affirming care, 'cause it gets demagogued by the right to mean that any kid... that affirmation means that that kid is immediately provided with puberty blockers and surgical interventions if wanted. And that's not what affirmation, I think, means when people talk about gender-affirming care. Um, sometimes people, even on the left, will mistake what you mean by gender-affirming care for the provision of puberty blockers and surgeries. It means affirming the kid in their exploration of what it is that they are and coming to understand themselves and providing that kid with what they need. That's what the decisions families are making. When you talk about the state inserting itself into the decision the parents, the kid, and their doctors are making, it's not the state inserting itself into a decision that is always puberty blockers. It's the state inserting itself into the choice-

**Lucy Sante** [13:29]: Mm

**Dan Savage** [13:29]: ... about whether that's right or not for this particular kid. And in this polarized time, I feel like we end up using different buzzwords, and there's what we mean by gender-affirming care, there's what they mean by youth gender medicine or whatever the right wing's, uh, term of art is. And I think it's really important to assert that ideally, and in its best practice, what gender-affirming care means is listening to that kid. It doesn't mean a certain prescription or a certain intervention. It means allowing the kid to LGBTQIA+++. The Q stands for questioning. And one of the things a kid can question is your sexual orientation. Another thing is a gender identity. And asking the question doesn't predetermine the answer. And that's happened.

**Antonia Hylton** [14:12]: Well, the other misconception, right, is that this all can happen really rapidly. I spend a lot of time in states like Texas, Tennessee, and Oklahoma, and in evangelical churches reporting. And I will have people tell me, "I heard that a kid down the street decided to be trans, and then the school nurse gave them puberty blockers, and then the next week..." I, I'm not, I'm not saying that to make you laugh. I'm actually... This is a, a real thing that many Americans think, that a kid can go to the local twenty-four-hour clinic and then get all of these services. That's not the reality on the ground. What is it actually like?

**Lucy Sante** [14:51]: Um, well, it's-- for most people, it's extremely difficult. I mean, the, uh... Many people, um, I happen to have been refer-- I live in the Hudson Valley of New York State, which is a very friendly area to trans people. But, um, if you're out there in a red state, um, if there's still a Planned Parenthood somewhere in your area, you can go there. Otherwise, you might all have to do, do it, you know, online or something. It's, it's tough. Um, you are, um, going to be questioned variously. Um, I didn't have to go through this because I was already sixty-six years old. But if you're a thirteen, fourteen-year-old kid, um, many people assume that you don't know your own mind. And by the way, that's a subproblem here, is people not respecting, uh, the fact that thirteen-year-olds can know very well who they are, and furthermore, that parents cannot design their own children. It's a big mistake made in other areas than merely gender identification. Um, but in any case, um, the process is going to be bureaucratic. It's gonna take time. It's, um, it's gonna be sinuous. It's gonna be, um, it's gonna have to be renewed, um, and it's gonna have a, a lot of checkup, checkpoints and checkups. Um, and, you know, and of course, surgery is never, ever performed on people under the age of eighteen. That's important to say because, you know, the, the, the urban legends on that one are profuse.

**Antonia Hylton** [16:35]: Blaze, what are you seeing at the data level, the, in research when it comes to that kind of mis- and disinfor- disinformation-

**Dan Savage** [16:44]: Mm

**Antonia Hylton** [16:44]: ... when it comes to the questions that people are asking, what Americans are searching for with understanding?

**Dan Savage** [16:50]: Well, um, [clears throat] I think there are a couple of factors that are worth pulling apart. Uh, one of them has to do with age and, uh, changes in definition of what, of what trans means, because it's not the same thing for, uh, you know, for, for young people and for people of our, of our age. Um, it, uh, and, and, you know, it used to be the case, um, I, I mean, I, I hope it's not offensive, like I, I refer to this as like the, the Priscilla Queen of the Desert phenomenon. But, you know, when, when, when we were coming up, um, trans tended to mean, uh, that there had to be surgery involved, and it almost always was, um, was transitions to female. And, um, among young people, those, uh, the, the, the ratios have reversed. So it's, it's much, it's actually quite a bit more common now to transition in the other direction. Uh, it's also no longer binary. So, you know, trans nowadays means not identifying with, um, with your sex assigned at birth, doesn't necessarily mean identifying with the other sex. Uh, and, uh, you know, so there's a big middle that has opened up as well. Um, and, uh, you know, so between it being less, um, less medicalized, um, and, uh, more expansive, uh, you know, the, the fact that, that there are actually so many more young trans people doesn't even necessarily mean what a lot of older people assume it means, if that, if that makes sense, because the definitions have shifted too.

**Antonia Hylton** [18:18]: I'm curious here in the audience if anyone feels confident enough to, to shout it out. What's your best guess as to the percentage of Americans who actually identify as trans or non-binary? Do you know?

**Blaise Aguera Y Arcas** [18:33]: Nobody's gonna be brave enough to say [laughs] what they think.

**Audience** [18:36]: Ten percent.

**Dan Savage** [18:36]: Yeah, two.

**Audience** [18:37]: Three percent.

**Antonia Hylton** [18:38]: Okay. Some of you are close, but everyone actually is overestimating. It's, according to numerous studies and polls, actually more like point five to just under two percent. Uh, some polls show that Americans think that up to twenty percent of their fellow Americans are, are trans. I'm curious for you, where do you think some of that... When you talk about the polarization, um, and also just the way in which a minority group can be weaponized politically, you know, how we got to this moment and, and why that can be reflected in, in the polling in this way?

**Blaise Aguera Y Arcas** [19:14]: Well, um, first of all, when people are answering that question, I think many of them are making a political statement of one kind or another, uh, as opposed to saying what they actually believe. Um-

**Antonia Hylton** [19:23]: Mm.

**Blaise Aguera Y Arcas** [19:23]: But, you know, for what it's worth, I asked thousands of randomly selected Americans, you know, how, you know, what, what they thought the percentage of trans people was, and the majority of them said well under one percent. Uh, you know, sometimes it w- you know, they, they wanted to say, like, point oh oh one percent or something like this. That was, that was a m- a more typical number. And, um, the thing is, like, when, when you actually break the data down, uh, just giving a number, giving a percentage, you know, whether it's point five or two or whatever, it doesn't tell the story at all because it varies so much by age and by density. So, uh, it's much higher in the city, uh, and it's much higher among the young. Uh, if you look at people assigned female at birth, uh, in the city, uh, and, you know, under the age of twenty-one, that number is upward of seven percent and maybe as high as fourteen. Uh, on the other hand, when you look at people of our age, it's extremely low, uh, even in the city, let alone in the countryside. In the countryside it really is, you know, uh, you know, right for, for, you know, for people over fifty, say, you know, point oh something. So, uh, you know, and, and the thing is, of course, when you give an estimate, you're, you're doing it on the basis of who you know and also who you think you know 'cause there are a lot of uncracked eggs out there-

**Antonia Hylton** [20:38]: Mm-hmm

**Blaise Aguera Y Arcas** [20:38]: ... especially in the places where, you know, where, where it's, where it's not accepted, and there's a feedback loop in the lack of acceptance. So, you know, as a result, uh, you know, it, it can be rational. It can be, uh, it, it can be an observ- you know, a real observation when you say, "Well, it doesn't seem like anybody is trans," because, you know, you're maybe older living in the countryside. You don't see anybody, uh, who at least to your knowledge, uh, is, is trans.

**Dan Savage** [21:01]: But you do see in the newspaper that thirty percent of Gen Z identifies as queer.

**Blaise Aguera Y Arcas** [21:05]: Right.

**Dan Savage** [21:06]: And for a lot of people, that instantly becomes thirty percent or twenty percent of everybody is trans.

**Blaise Aguera Y Arcas** [21:12]: Right.

**Dan Savage** [21:12]: Um, can I ask a question?

**Antonia Hylton** [21:14]: Please.

**Dan Savage** [21:14]: You described the hurdles, that it's not a frictionless process-

**Blaise Aguera Y Arcas** [21:18]: Mm

**Dan Savage** [21:18]: ... to access trans care. Um, in response to your question about the myth that it's a frictionless process and you can just go and get whatever you want whenever you want it, do you think that process should be frictionless? Are you saying that the hurdles that you had to clear to access care even as an adult, um, were an injustice and they should be wiped away? 'Cause that is what some people argue, that we should make these treatments available without any gatekeeping at all.

**Blaise Aguera Y Arcas** [21:42]: Mm-hmm.

**Dan Savage** [21:42]: And people... A thirteen-year-old knows who they are, and if the thirteen-year-old wants to block puberty-

**Blaise Aguera Y Arcas** [21:48]: Mm-hmm

**Dan Savage** [21:48]: ... or get top surgery, which has happened, it's not a myth. Like, we don't wanna hand the right wing a stick to beat us with by saying this never happens. It's extremely rare, but it has happened.

**Blaise Aguera Y Arcas** [22:00]: Mm-hmm.

**Dan Savage** [22:00]: And they can point to these cases where young people who may have benefited from it, and it happened for all the right reasons, and there's no regret, did get surgery as minors. But I'm-

**Blaise Aguera Y Arcas** [22:10]: Mm

**Dan Savage** [22:10]: ... I'm curious where you come down on that because I see both arguments being made, that we don't need to worry about anybody being rushed along because the process is, has so many roadblocks-

**Blaise Aguera Y Arcas** [22:20]: Mm-hmm

**Dan Savage** [22:21]: ... and hurdles. But I also see people saying, "And that should be not how it is. It should be a frictionless process where there are no hurdles." And I'm curious where you come down on that.

**Lucy Sante** [22:30]: Uh, you know, I'm gonna take a middle course, [laughs] the coward's way out. Um, I don't think it should be automatic. Um, I think some personality assessment has to be done. Um, I think that yes, and there are probably cases in which, um, affecting this kind of ideation is actually a symptom of something else, you know? Um, so I don't think it should be entirely frictionless, but on the other hand, it shouldn't be torturous either. It should be regarded, um, the same way any kind of medical inter-intervention is regarded, really. I mean, it is a medical intervention and, um, I'll tell you, uh, my m- the process I'm going through in getting hearing aids right now is not frictionless.

**Antonia Hylton** [23:18]: [laughs]

**Lucy Sante** [23:18]: You know? Um, by the way, go- going back to the statistics question, I read a fascinating interview in the, it was in The Guardian about five years ago, and, um, it was, um, a trans person on the, uh, neurological spectrum in addition, uh, who noted that, um, that people, um, on this, the autism spectrum, uh, generally self-identified as trans at a rate that was at two or three times higher than the norm. And this person pointed out it's not because, um, uh, it's not because people on the neurological spectrum are more likely to be trans. It's because people on that spectrum are incapable of lying.

**Dan Savage** [24:07]: Ha. [laughs]

**Lucy Sante** [24:08]: So, you know, factor in all the people out there, especially people my age, older, and, you know, four or five decades younger who have been lying to themselves as I intend, I intended to take this to my grave. There are a lot of others

**Antonia Hylton** [24:26]: On that point, what do you say to the many Americans and elected leaders who argue that some of this is a social contagion? Kids are seeing it on TikTok, on Twitter, on Instagram, and that is turning them-

**Lucy Sante** [24:41]: Mm

**Antonia Hylton** [24:42]: ... trans in some way.

**Lucy Sante** [24:44]: Uh, so reducing it to the matter of a fad. You know, I mean, I tend to see it as a gradual opening, and all these cultural manifestations since my own teenage years, The Cockettes, and then David Bowie, and then, uh, the Rocky Horror Picture Show, on and on and on. One thing after another over the decades. Um, and uh, for me, actually, it was, um, being a professor at a college and seeing the wave kind of reach the shore and then break, which happened about 10, 15 years ago. F- the first time I started getting non-binary students. Um, but the social contagion, all I would say is, well, if that's the case, give it five years, you know? Because fads don't last much longer than that. If people are still wanting to be trans five years from now, it's gonna mean it's a real thing. I mean, u- unfortunately, uh, a lot of pe- for a lot of people, the matter is so urgent, they don't have five years to wait.

**Dan Savage** [25:53]: What is socially contagious is the permission structure that now exists for people to question the received sex assignment at birth.

**Lucy Sante** [26:02]: Mm.

**Dan Savage** [26:02]: Right? And [clears throat] what is socially contagious, I think, is not more and more people just, like deciding they're trans, but more and more people deciding they fall somewhere under this much larger trans umbrella that Blaise talks about, where they're not getting blockers or surgeries or hormones, but they are identifying as non-binary or agender. Um, and that, that does seem to me to have a social component because of the social permission structure. In the same way that, like they said, when, you know, I'm super gay and super old, um, and my parents believed that gay was something you caught, that gay was contagious, that we were recruited. Now they-

**Lucy Sante** [26:39]: Mm

**Dan Savage** [26:39]: ... have resurrected groomer as the slur. Um, and what was contagious was courage. What was contagious was bravery.

**Lucy Sante** [26:45]: Mm.

**Dan Savage** [26:45]: Um, and what was contagious was the example of the life a- authentically lived out, even at great cost. And people saw, people who were closeted, saw other people living that life and decided that that was better even at whatever cost. And I think that's what is socially contagious. That's what we mean by that. Um, that permission structure is giving some people the courage to identify as trans and to medically transition, but it's giving a whole lot of people the courage to identify as all sorts of things that would also get slapped with the trans label that then people read when they see those numbers as all of these people are getting puberty blockers, all these people are getting surgeries.

**Lucy Sante** [27:24]: Mm.

**Dan Savage** [27:24]: When a lot of these people are just getting haircuts and identifying as non-binary. [laughs]

**Blaise Aguera Y Arcas** [27:31]: Spicy. [laughs]

**Lucy Sante** [27:33]: [laughs]

**Blaise Aguera Y Arcas** [27:33]: Well, to, to, to build a little bit on, on both of your points. Uh, this, um, originally, social contagion was a term used by social scientists to, to talk about the way ideas, um, move around social networks, which is a thing. Um, but of course, that word contagion and, you know, Kenji Yoshino, the, the legal scholar, you know, wrote a, a great article about this a number of years ago. Um, you know, also it communicates a sense of this being a disease which has this, uh, you know, sort of semiotic alliance with the idea of, of being gay, being a illness, or now being trans, being an illness. Um, and that's really unfortunate because, you know, it, it, it feeds into all these narratives about, about grooming or, or about, uh, you know, if you're, you know, gay parents and you have a kid, the ki- you know, the kid might catch gay from you or something like this. Um, so that's obviously-

**Dan Savage** [28:21]: Social contagion is real. Like, so-

**Blaise Aguera Y Arcas** [28:22]: But this is the thing, right?

**Dan Savage** [28:25]: As a... So- sorry, interrupt you.

**Blaise Aguera Y Arcas** [28:26]: Exa- no, exactly. I, so although, although, um, that, that sort of negative connotation is really ugly, uh, some, some of the response from people on the left when they say, "Well, you know, there is no such thing as social contagion," I don't subscribe to that idea either. Uh, the entire, um, concept of culture and cultural evolution relies on ideas being transmitted through social networks and on that building over time. There is no social level or cultural evolution without social contagion. I tried to sort of rebrand it in my book, you know, social transmission, uh, to give it a little bit of a less, um, toxic name. But, you know, that's actually really important. That's how progress happens. Uh, I also think that, that being essentialist about it, which is a position that a lot of the left gets pushed into by trying to push back against the social contagion idea and saying that, "Well, everybody is a certain way," and, uh, you know, and there's no su- there's, there's no, you know, you are what you are, and that's it. That's the end of the story. I don't think that that's the case either. Uh, we've seen, uh, definitions of trans change. Uh, that's social, and as those definitions change, as you point out, you know, different people are in or outside of that envelope. Uh, some people are very, very inflexible about some aspect of their identity. It's gonna be the way it is no matter what the circumstances. Many other people are more flexible, are more or less unhappy if they're wedged into, you know, some, some place where they don't necessarily, uh, fit. Um, and some people, you know, come out l- you know, later in life, and some people never.

**Lucy Sante** [29:53]: Mm.

**Blaise Aguera Y Arcas** [29:54]: Some people would have been extraordinarily unhappy the entire time, some less so. There's, you know, I, I, I guess I wanna push back against the false binary between the binary and the non-binary, if that makes any sense.

**Lucy Sante** [30:05]: Yeah, yeah, yeah.

**Dan Savage** [30:06]: Yeah.

**Lucy Sante** [30:07]: Um, but-

**Dan Savage** [30:07]: That does seem... Sorry.

**Lucy Sante** [30:08]: Sorry.

**Dan Savage** [30:08]: I interrupted. Go ahead.

**Lucy Sante** [30:09]: I was just gonna say that, you know, um, it strikes many people who are not, you know, who have never felt... It's, it's a hard thing to conceptualize for people who are cis and do not have... Although I do think there's a lot of blurring of boundaries anyway. But, um, the fact is that, um- It-- There are plenty of societies in the world that make allowances for the two-spirit, et cetera. Um, so we know that trans people have always been around. The thing is, in the West, there has been this extremely strong taboo, um, such a taboo that it, it seemed unthinkable, um, un- you know, for-- until very recently, and even among parts of the population even now. And why this taboo? And, you know, I mean, this is just m-m-my notion, but I think it's because, uh, it makes nonsense of male supremacy. Male supremacy cannot exist if you have traitors, if you have blurred boundaries. It has to be, uh, uh, an absolute system, and it's encoded into these kinship patterns. And as, you know, social mobilities happen, uh, vertically and horizontally, kinship patterns get broken, and that's what permits this kind of taboo breaking to occur.

**Antonia Hylton** [31:39]: And does this idea of transmission and contagion... I mean, uh, I-- sometimes I'm surprised at the fact that we don't often hear that applied to what we see happening in political theater, which is the overestimation, the use of children especially in these communities as a kind of cudgel. Um, and, you know, I, I'm curious if from your standpoint, but really from all three of you, how you see that. Does that framework apply on the opposite end of the political spectrum?

**Blaise Aguera Y Arcas** [32:09]: Well, um, so to, to, to give a, a kind of data-driven example from, uh, not, not from, not from trans, uh, but, but from just, uh, same-sex attraction and being gay. Uh, when, when I ask people of many, many ages, um, "Are you exclusively same-sex?" I actually don't ask, "Are you exclusively?" I ask, you know, "What," you know, "How do you identify, and are you sexually attracted to men, sexually attracted to women, romantically attracted to men, romantically attracted to women?" If you then plot the fraction of people across all ages who are exclusively same-sex attracted, both sexually and romantically, you find that that is actually a very, uh, stable five percent or so across all ages. On the other hand, if you ask, um, "Are you lesbian or are you gay?" You get really different curves.

**Lucy Sante** [32:55]: Mm.

**Blaise Aguera Y Arcas** [32:56]: Uh, so you know, it's, uh, that, that, that curve, you know, settles down to... Well, actually, it goes even lower than the five percent among, among the, among the oldest respondents. Um, but, you know, lesbian, for example, at age eighteen, nineteen, goes up to thirty percent. So this is way higher than exclusive same-sex attraction. Well, it used to mean that, you know, I mean, for a lot of, for a lot of older people, you know, you don't say you're lesbian unless you are exclusively same-sex attracted.

**Lucy Sante** [33:21]: Mm.

**Blaise Aguera Y Arcas** [33:21]: Uh, and, and if there was any play, any give, uh, or, you know, any, any degree to which you are, you know, a little bit bi or a little bit flexible, you would, you would not apply that label, partly because of the high social cost of doing so. That social cost has obviously gone down a lot, especially in the cities for young people. So much so that, uh, you know, that even, even people who, um, uh, who are mainly, uh, opposite sex attracted, uh, are still, uh, identifying, uh, sometimes as, as lesbian. So, you know, this is why I say, you know, uh, is this social transmission? Is it not social transmission? Well, obviously, there is social transmission in the sense that, that those labels have come to mean a different thing because of, because of how people talk about it and who they interact with. Uh, does that mean that lesbianism is catching? I mean, uh, I, I think that's a trick question, if that, if that makes sense.

**Antonia Hylton** [34:13]: What do you see, Dan? I mean, as someone who's seen this and written about this, and, um, you also are part of the media, y-you and I. I mean-

**Dan Savage** [34:23]: Well, you talk about these things and write about these things, and the people who read them or encounter them begin to understand that there's more things possible for them, um, more ways in which they could identify, including, and I've met some myself, um, opposite sex attracted, assigned female at birth persons who identify as lesbians, and it's kind of a cultural tribal signal of allegiance and almost, um, a wish casting that they would rather have been lesbians. Um-

**Antonia Hylton** [34:51]: [chuckles]

**Dan Savage** [34:52]: And I find that really fascinating. I'm old. I like words to mean things. Um-

**Antonia Hylton** [34:59]: [chuckles]

**Dan Savage** [34:59]: And so when I meet people who use a word like that, and increasingly the word you see being used is sapphic, um, a-as opposed to lesbian, and what... And their own personal, uh, boutique definition, bespoke definition of the word doesn't mean what the word means. I wanna get pedantic with them and start arguing with them, um, but I don't, because whatever. I also-- But I do think that we have this problem on the left, where the, the right will weaponize a concept like social contagion, and the left's pivot is not social transmission, not to try to str- which is brilliant, try to strip the, the word that has a negative connotation out of it and just re-roll it out. But to say, "That's not a thing. That doesn't happen." Just like we wanna say because they wanna weaponize or demagogue around, um, minors getting surgery, but then we'll say that that never happens. Well, it does happen. It has happened. And so we have to be careful on the left not to shift-- allow the right to basically herd us into taking these indefensible positions that will be easily demagogued about, including in front of the Supreme Court when this case comes up around youth gender medicine, which I would hope that they would declare these laws unconstitutional and get the state out of, um, the relationship between individuals and their doctors. But we've already seen that the Supreme Court is gonna come down on... where they'll come down on the side of it's people like that with Dobbs, and I'm really concerned.

**Lucy Sante** [36:28]: Mm-hmm.

**Dan Savage** [36:28]: And I get, as a lefty, I don't like to see lefties Set traps for themselves around things like arguing social contagion doesn't exist, when we acknowledge that it exists when it comes to suicide clusters, when it comes to gun violence-

**Lucy Sante** [36:43]: Mm

**Dan Savage** [36:43]: ... when it comes to all sorts of other things, including things that are harmless. Charm bracelets were socially contagious-

**Lucy Sante** [36:50]: [laughs]

**Dan Savage** [36:50]: ... among girls for a while, and nobody had a moral panic about that. And so we can't-- We don't wanna make arguments that can be so easily-

**Lucy Sante** [36:58]: Mm

**Dan Savage** [36:59]: ... debunked, disproved.

**Antonia Hylton** [37:00]: So I have to ask then, how do you talk to people about the reality that while it is a small, small fraction, that there are detransitioners? There are people who regret, who make changes.

**Dan Savage** [37:13]: I have a friend who was a lesbian for 10 years.

**Lucy Sante** [37:16]: Hmm.

**Dan Savage** [37:17]: And that's fine. That... And I don't doubt that she was a lesbian when she was lesbian identified and with women, um, sexual orientation often for women can be more fluid than for males. For males, it tends to be a little more, uh, icy [laughs] than fluid. But yeah, there are some people who have detransitioned. Um, some people have said they detransitioned because the social pressure of being trans was too great, um, or they couldn't pass, and it invited violence, it, and they couldn't handle it. But, uh, not that anyone should have to handle violence, but, um, there are other people who've detransitioned who are like, "I, I made a mistake." And I think with something as ephemeral and hard to pin down and understand as gender identity, 'cause there isn't a test for it, that that is a-an error that a person could make. Which is why I don't think when I read Andrew Long Chu's piece in The New York-

**Lucy Sante** [38:14]: Mm

**Dan Savage** [38:14]: ... in New York Magazine about why it should be, the process should be frictionless, and anybody who asks-

**Lucy Sante** [38:18]: Mm

**Dan Savage** [38:18]: ... should receive. And I actually think that we should m-be m-merging j-the idea of gender affirming care and the idea of consistent, persistent, insistent, which used to be the standard-

**Lucy Sante** [38:30]: Mm

**Dan Savage** [38:30]: ... for providing transitions to youth, was like that it was persistent and consistent and insistent. And you can s-allow a kid to sit with their questions and, um, affirm them in the asking of the questions and the seeking of the answers without rushing to the answer of puberty blockers. And the people who argue that they detransition not because of social pressure or fear of violence or stigma or family pressure, but because it wasn't who they actually were, when you listen to what those people say, they say they were affirmed too quickly, that the process for them was too frictionless, and they needed to have more time. They needed some pushback. I have a friend who's n- who was non-binary, um, and he, he now identifies as he again, called me angrily one day, and we had this conversation because what he needed when he identified as non-binary was for someone to say, "Are you sure?"

**Lucy Sante** [39:27]: Hmm.

**Antonia Hylton** [39:27]: Hmm.

**Dan Savage** [39:27]: Whereas instead everybody said, "Right on, sister."

**Lucy Sante** [39:30]: [laughs]

**Dan Savage** [39:30]: Right? Everybody was like, "You go, and I love you and support you." And I said it, too. And he's like, "I needed pushback at that moment 'cause it actually wasn't right," and it was a source for him, even though there was no medical component, of a lot of pain, and it wasn't true. And it was only... You know, sometimes it's through the process of going through something that you figure out who you are. Just like when you write. You figure out what you think by writing.

**Lucy Sante** [39:52]: Yeah.

**Dan Savage** [39:52]: You sometimes don't know what you think before you start. And I think that can apply to transitioning, too, and we have to allow for detransitioning as part, as a trans experience.

**Lucy Sante** [40:02]: Mm-hmm.

**Dan Savage** [40:03]: And not pit detransitioners against transitioning or tran- people who have transitioned. And there may be lessons in what a detransitioner has gone through or knows that would benefit people around making their own mind up with certainty who are pondering transition.

**Antonia Hylton** [40:22]: Lucy-

**Lucy Sante** [40:22]: There-

**Antonia Hylton** [40:22]: ... do you think that's possible?

**Lucy Sante** [40:24]: Well, I was just gonna say, I mean, and frankly, uh, there are going to be seekers, there are going to be tourists. You know, just think of religion. Think of people who've converted multiple times. This-

**Dan Savage** [40:35]: Religion is so socially contagious-

**Lucy Sante** [40:37]: Yeah

**Dan Savage** [40:38]: ... if you were to label it that way.

**Lucy Sante** [40:38]: Bingo, yeah. Um, so yeah. There's, um, you know, and I mean, it's been said that all, you know, the, um, I mean, the line is in my book, but I didn't make it up, um, that all trans people have the same story, and yet all trans stories, no tr- two trans stories are quite alike. Um, everybody comes to their own conclusion their own way, and it's rife with contradictions. Um, and, um, probably there'll be changes over time. You know, it's, um, uh... I'm lucky enough that my own personality was already established before I transitioned so that I only had to do a little bit of work, and the rest was all momentum. Uh, but, um, it's invariable that, um, especially if you accept the fact that male and female are not monolithic duality, um, you know, a-after that, it's all gray area.

**Blaise Aguera Y Arcas** [41:42]: I, I would, I would add that, you know, the, m- it's, it's frustrating to me to see the left fall back into essentialism-

**Lucy Sante** [41:50]: Mm-hmm

**Blaise Aguera Y Arcas** [41:50]: ... in order to, uh... And I, and I, i-ik- I can see why it happened. It happened because, you know, a lot of people's experiences are, you know, "I've always been this way, and I finally... You know, it's not a lifestyle choice, and I finally, you know, my, you know, my, my shell cracked. I had a chance to, you know-

**Lucy Sante** [42:04]: Mm-hmm

**Blaise Aguera Y Arcas** [42:05]: ... show the world what I am." And that is obviously an experience many people have had. But it is also true that language is not immutable. It changes over time. And people are not immutable. They change over time.

**Lucy Sante** [42:16]: Mm-hmm.

**Blaise Aguera Y Arcas** [42:17]: Uh, you know, to deny the idea that people can change is to deny the idea of their own agency, which is exactly what we're supposed to be fighting [laughs] for. Uh, to deny the idea that language changes over time is to, is to, uh, pretend that culture doesn't evolve. All language changes. So here I have a bit of a disagreement with you, Dan. Like, you know, you say, like, "This is what this word means." Well, that just shows you're old. [laughs]

**Dan Savage** [42:39]: I, I-

**Antonia Hylton** [42:39]: [laughs]

**Blaise Aguera Y Arcas** [42:40]: Like, you know, the... Every, every word changes over time, and it's okay for us to fight about it and argue about it because that's part of that process-

**Dan Savage** [42:47]: It feels like the meaning-

**Blaise Aguera Y Arcas** [42:47]: ... of change and pushback against the change

**Dan Savage** [42:48]: ... that it's change, it needs, that meaning, that change needs to be earned through argument.

**Lucy Sante** [42:52]: Hmm.

**Blaise Aguera Y Arcas** [42:53]: Yeah.

**Dan Savage** [42:53]: Not by-

**Lucy Sante** [42:54]: Yeah

**Dan Savage** [42:54]: ... diktat.

**Blaise Aguera Y Arcas** [42:55]: Sure. And, and, and nobody is, nobody is actually in a position to dictate it unless, except in France, I guess they have like a language board.

**Antonia Hylton** [43:01]: [laughs]

**Dan Savage** [43:01]: Can't even trust it.

**Blaise Aguera Y Arcas** [43:02]: Yeah.

**Antonia Hylton** [43:04]: I wanna leave a few minutes for some people here in the audience to ask questions. But before we go to them, I just wanna ask all of you what you think the future holds, if you feel optimistic right now, if you are fearful of where the trends are taking us. What's on your mind looking ahead?

**Lucy Sante** [43:22]: Well, we're the, we're the current folk devils, and we're extremely vulnerable as a minority. Um, we don't have a legal foundation. We don't have, uh, corporate support. You know, we're, we're out there naked in the world, so we can be squashed very easily, and it's happening already in various countries. Um, and it could very well happen here, uh, especially depending on the results in the next election. So I am scared, yes.

**Dan Savage** [44:00]: The left-wing m-- The right-wing myth is we can never risk any progress because society will collapse. The left-wing myth is there's never been progress, right? That we're just as racist, sexist, homophobic, transphobic, um, uh, this culture, society as we've ever been. We on the left, I think, always should point to the ways in which we made progress and the right's predictions of doom did not come to pass to prove that whatever they're predicting doom about right now is they're wrong about this, too. Um, marriage equality turned nine or ten [laughs] just now. Um, and they predicted people would be marrying kids, and people would be marrying animals. And when they undid Don't Ask, Don't Tell, they predicted that five hundred thousand people would quit active service military. Two quit active service military. Um, they were wrong what they said about gay people serving in the military, about gay people marrying and having kids. They're wrong now about what they're saying about trans people existing in the world, too. Um, and we, trans people are going through it right now, going through the fire. Um, in some ways, I see echoes of what trans people are... I mean, literally in, like some of the demagoguery around bathrooms and, um, grooming and recruiting is, it's just what they were saying about gay men forty years ago, fifty years ago. They're saying about trans people now. They're just taking their hatred off the shelf and reinject it into the culture. But I see this as a moment of great peril, but also great opportunity for trans people and gender non-conforming people because all of the attacks on gay people and gay marriage invited the argument about who we were and what we meant, and we won that argument, and I think trans people are gonna win this argument. But it's gonna... Two thousand and four was really fucking ugly. The fourteen anti-gay marriage amendments in fourteen states that, uh, cost John Kerry the election, that got George Bush back into office for four more insanely incompetent years. Um, that night, uh, my husband and I sat there with our son, and we cried 'cause we thought we were gonna have to leave the country, and we couldn't have predicted that ten years later we would have marriage equality.

**Blaise Aguera Y Arcas** [46:00]: Hmm.

**Dan Savage** [46:00]: And so we can't predict right now when it's darkest what ten years later I think trans people are gonna have or where they're gonna be, and we shouldn't succumb to pessimism.

**Blaise Aguera Y Arcas** [46:09]: I, I couldn't agree more. [audience applauding] Um, I, I think that, um, uh, especially on the left, fear has taken hold, uh, and pessimism.

**Dan Savage** [46:20]: Hmm.

**Blaise Aguera Y Arcas** [46:20]: And, uh, I think that, you know, there are certainly plenty of reasons to be anxious. Uh, you know, I, I mean, when I, when I was growing up, when we were growing up, we grew up in the shadow of the Cold War when, you know, nuclear apocalypse was imminent for real, right? We narrowly averted it, uh, you know, a few times. Um, I think that zooming out is very, very helpful and looking at, you know, what the last couple of centuries have looked like. Uh, and when you do that, you realize that things are better now than they have ever been by a large, large factor. In nineteen hundred, life expectancy on Earth was thirty-five. And these things are really easy to forget, and I think that one of the reasons for that, Han-Hans Rosling pointed this out in a, in a, in, in his last book that he, you know, he kind of wrote on his deathbed. Um, good news tends to happen incrementally. Progress is incremental.

**Dan Savage** [47:11]: Hmm.

**Blaise Aguera Y Arcas** [47:11]: And we are wired to notice changes. So, you know, no news story has ever been written saying, you know, "One point six percent fewer cases of river blindness in India last year," right? Whereas, you know, a school bus, uh, you know, full of kids, uh, kidnapped by Boko Haram, that's news, right? So it's snakes and ladders. The, you know, the uphill is slow, the downhill is fast, but it does tend upward over time despite the setbacks. So I, I'm fundamentally an optimist.

**Antonia Hylton** [47:40]: Thank you. Thank you to all of you. We have just a couple moments. Um, now is the time to raise your hand if you have a question. I know there are some people coming around with microphones. Right here in the front.

**Lucy Sante** [47:50]: Um, there's been research about the overlap between autism and Asperger's. Uh, sorry. Uh, there's been a, a lot in the literature on, uh, the overlap between neurodiversity, mainly autism, Asperger's, and transgender and, and vice versa, just more than the averages and everything. And, uh, I was wondering what, uh, your opinions are in the sense that if this is true, um, shouldn't the transgender specialists and psychologists and autism specialists be trained in the other as well? I think it's a false syllogism. Um, I, I quoted, just earlier on this dais, I quoted this story in, uh, The Guardian about five years ago, and it was an interview between, um, cisgender heterosexual father and his transgender son who was on the autism spectrum. And it's that, that, you know, the son said, "Yeah, the rates are for transness among people on the autism spectrum are at least twice as high, if not three times, as the general population." Is that because people on the spectrum are more likely to be trans? No. It's because they can't lie to themselves.

**speaker_5** [49:13]: Is one just happens what I do. I'm not a professional, but at differentbrains.org where we advocate for neurodiversity, many of our interns and the people we speak to are neurodiverse-

**Antonia Hylton** [49:26]: Can you reply?

**speaker_5** [49:26]: -on the autism spectrum, Asperger's, and the-

**Antonia Hylton** [49:34]: I think she didn't like his view.

**speaker_5** [49:35]: I apologize. I was just saying in what I do with, uh, differentbrains.org, we're a not-for-profit that advocates for neurodiversity. And we have found amongst our interns and amongst th-the literature that, um, there, there is an increased incidence in both ways. In other words, if you interview a hundred transgender individuals, more of them will be on the spectrum, not meaning deeply autistic, but Asperger's and high functioning autism, uh, than, than, you know, regular population and vice versa. So the only point I was making and why I wanted to bring it up was I think it would behoove everybody to get some training in both, to train the autism professionals and psychologists and so forth, uh, in transgender and the transgender specialists, if you will, in, um, autism. That was the, the only point I was making.

**Antonia Hylton** [50:41]: Thank you.

**Dan Savage** [50:41]: Totally agree.

**Antonia Hylton** [50:42]: We have only a little bit time a l- left, and I wanna make sure we have-

**Dan Savage** [50:44]: One more

**Antonia Hylton** [50:44]: ... at least one other person, if that's okay. Give him one second.

**Audience** [50:48]: Yeah. Thank you so much. Hi, I'm Bryonna Barrett. I'm a playwright. I mostly write plays about gender identity in ways that are comedic and kind of sneak people into compassion that they weren't expecting to walk away with when they see a play, hopefully. Um, and I guess I, I, I feel like the, the modern conversation around gender and transgender identity and non-binary identity ends up in this place where we're talking about how to justify ourselves to other people, and I, I, I, I'm left wanting to hear more, I guess, about how we, how we create a community where people don't feel like they need to justify themselves so much. This idea of this sort of bioessentialism, "I was born this way," it has to be this persistent identity. Like, I don't... I mean, I, I remember during, you know, the, the George Bush election how th-this, this, this, um, demagoguery around this idea of i-is it, is it a choice or are you born with it? And for some reason, we got so caught up in this idea that you had to prove it was real, and that something can't be a choice that is also real. Like, I, I, I don't understand why there's not more discussion around like, "Yeah, maybe it's a choice. Who cares? Maybe you're doing it to get along with your friends, and who cares?" There's a million identities that, that, that children and adults alike take on to find community and to find people that understand them and, and, uh, s-so what? Maybe it's a choice. Maybe we change our minds later. Maybe it's a mistake. Nobody's questioning everyone else who gets plastic surgery or any kind of other medical intervention that they... didn't work out the way they hoped and changed their mind about later. Nobody questions a woman who, you know, gives birth and then says, "Eh, I kinda wish I didn't." You know? Like, there's a lot of i- unchangeable choices we make based on notions we have at one point in our lives or another and like, why, why not just stand behind the banner of like, choice is cool? Like, it, it... if it's a choice, fine, and we have the right to make it.

**Dan Savage** [52:50]: We can stand behind the banner that choice is cool and everyone has a right to make their own choice, and also acknowledge that for most people, particularly around their sexual orientation, they don't experience it as a choice. Like particularly gay men of my generation, you chose straight desperately-

**Audience** [53:04]: [laughs]

**Dan Savage** [53:04]: -and proved to yourself that it wasn't a choice. You didn't choose gay. Um, as for the, the point you began with, like we shouldn't have to justify ourselves, you're absolutely right, we shouldn't have to, but we're going to have to. Because when you're a tiny minority and you're invisible and spread randomly through the population, it's going to be hardwired into the experience of being a part of that minority that you're gonna be in negotiation with the majority whether you like it or not, and always. And so, yeah, we shouldn't have to justify ourselves. Welcome to being, you know- A human ... four percent of the population, five percent of the population, and existing in a culture where the person that you are has been stigmatized and marginalized for thousands of years. Uh, we're gonna have to justify ourselves. We're really good at it. It's why we're winning the argument, at least now we have. We've made progress, and I don't think we should stop. And yeah, like [laughs] as to whether it's a choice or not, like Mormonism is a choice. You would... Like everybody who says it's a choice are the same people who are out there proselytizing around the religion, and it shouldn't... It doesn't matter if it's a choice. But it also is true of most people's lived experience of their sexual orientation, that it was unchosen. I also think that your question gets at two really deep philosophical issues about what is reality and what is free will that are really not simple. Uh, you know, you- Talk about zooming out. [laughs]

**Antonia Hylton** [54:33]: [laughs]

**Dan Savage** [54:34]: Well, well, I mean, uh, you know, all... it's all... it's just atoms out there, you know? So, you know, is this a chair or not, you know, is, is not a statement about like a ph- a physical reality. It's, it's, it's about a, it's about a perception and a history. Uh, you know, the... it was manufactured as a chair. You know, if we make neural nets that generate pictures of chairs, you can, you know, sort of transition smoothly from something that looks like a chair to something that doesn't, and everybody will have a different idea about exactly where that, where that shift took place. What's reality? You know, so I, I, I, I don't think that... I don't think these questions have, have, um, Boolean answers, and I think that anybody who wants to claim that this is, you know, physical or biological reality is, is actually not understanding the nature of reality. And not all choices are exactly the same. You can choose to identify as gay or lesbian or bi, and it can... you can realize later that that's not who you are anymore, or it's not... whatever. Like, different choices have different stakes or potential consequences, as we've seen with detransitioners. If like the consequence or stakes was an orchiectomy, you can't walk that back very easily. And so that's a choice you're gonna wanna, I think, have some friction in that process so that if you do make that choice, and it's the right choice for you, that it is the right choice for you. Um, and that requires more thought than just, "I'm non-binary now." Like, we have to be able, on the left, to recognize stakes and consequences being different for different groups.

**Antonia Hylton** [56:06]: Thank you, Dan, Lucy, Blaise. It's really been such a, a joy and an honor to get to know the three of you and to spend some time with you today. And thank you to all of you for being part of this conversation. [clapping] [outro music]

