---
title: "Function with Anil Dash, ep. 4: Should Twitter Have an Edit Button?"
person: anil-dash
section: by
type: talk-transcript
year: 2018
date: 2018-11-19
venue: "Function with Anil Dash (Glitch / Vox Media)"
authors: "Anil Dash (host)"
source_url: https://glitch.com/culture/function-episode-4/
retrieved: 2026-08-13
content: full-text
notes: "Official episode page with full transcript; page is offline, recovered from the Wayback Machine snapshot 20190919203726 (https://web.archive.org/web/20190919203726id_/https://glitch.com/culture/function-episode-4/). Show notes and sponsor blocks precede the transcript."
---

# Function with Anil Dash, ep. 4: Should Twitter Have an Edit Button?

## Full text

### "How do you fan out a tweet to 50 or 60 million followers if someone can edit it every five minutes?" — Leslie Miley  
  
[](<https://itunes.apple.com/us/podcast/function-with-anil-dash/id1439658455?ls=1>)[](<https://www.google.com/podcasts?feed=aHR0cDovL2ZlZWRzLmZlZWRidXJuZXIuY29tL0Z1bmN0aW9uV2l0aEFuaWxEYXNo>)[](<https://www.stitcher.com/podcast/vox/function-with-anil-dash>)[](<https://open.spotify.com/show/61FfAOZJBJQbP7vfLoTuYB?si=9VICmm7DRDuiU-GfoNsj3Q>)

###  [](<https://overcast.fm/itunes1439658455/function-with-anil-dash>)[](<https://pca.st/gSE3>)[](<https://www.breaker.audio/function-with-anil-dash>)[](<https://feeds.feedburner.com/FunctionWithAnilDash>)

If you're an active Twitter user, you've probably made a typo or a mistake in a tweet before that you wish you could correct. You _could_ delete the tweet and just write another one, or Twitter could create a feature that users have adamantly requested for years -- an edit button. [Even Twitter's CEO Jack Dorsey has mulled over this feature](<https://www.usatoday.com/story/tech/2016/12/29/twitter-ceo-we-need-edit-button/95972118/>), and according to recent news, [it may just happen.](<https://thenextweb.com/twitter/2018/11/12/dorsey-says-twitter-is-thinking-about-an-edit-button-to-fix-typos-in-tweets/>)

Enabling a button to edit your tweets sounds like an easy thing to set up from a user standpoint, but like most technological features, implementing it comes with its own positives and negatives.

This week on Function, we look at this popular feature request from the expert and the user side. We talk with **Leslie Miley** , former engineering manager at Twitter, about the behind-the-scenes technical and ethical considerations that need to take place to carry out this feature from a product level.

We also talk to **Andy Carvin** , author, professor, and former social media editor at NPR. Andy knows firsthand how one misinformed tweet can have a dangerous ripple effect, and talks about how the possibility of editing that tweet may have caused even more damage.

**Guests**

**Other Links**

###  **Big thanks to[Microsoft Azure](<https://azure.microsoft.com>) for supporting the first season of Function.**  
[](<https://azure.microsoft.com>)

[**Function**](<https://glitch.com/function>) | [**About**](<https://glitch.com/culture/function-about/>)

* * *

## Transcript

**Anil Dash** : Welcome to Function, I'm Anil Dash. Today, we are gonna hit on a question that almost all of you have thought about at some point — you've certainly seen someone complain about if you are on Twitter — which is why doesn't Twitter let you edit your tweets?

The thing is, I've been ther. I've totally been that person where I tweet something and immediately think, "Oh man, I really gotta phrase that differently, or I wish I could just fix that typo" and I think everybody's had that feeling. I think for most of us that are regular people on Twitter that aren't celebrities, an edit button would let us fix if we had a typo or if we had a grammar mistake, something common.

But what about when the stakes are higher? How would an edit feature help an organization if they needed to get reliable information out to the world, like a news organization that's reporting during a time of crisis and they wanna be able to report the news responsibly?

_Newscaster: We have breaking news for you, it's coming out of Tucson Arizona. Several people have been shot. The Tucson Citizen newspaper is reporting that among those shooting victims is congresswoman Gabrielle Gifford..._

**AD** : [Back in 2011, Arizona congresswoman Gabby Giffords was shot during a mass shooting that left six people dead and several others injured](<https://en.wikipedia.org/wiki/2011_Tucson_shooting>), and the scene was chaos as you'd expect. There's first responders scrambling everywhere, trying to help the wounded. There's reporters that are rushing to the scene to try and get more information.

_Newscaster: And we understand that congresswoman Gabriel Giffords is among 12 people shot at a grocery store, just hours ago and that is, according to a democratic source. There are unconfirmed reports that there are fatalities and I should tell you, and it's disturbing news, that NPR is now reporting that the congresswoman, congresswoman Gabriel Giffords has in fact, died._

As we now know, Giffords was wounded that day, but she did not die in the shooting.

Andy Carvin was the social media editor for NPR at the time. And NPR had reported on air that Giffords had died, so Andy tweeted out the same information. And the thing is. Andy's tweet was only out for 25 minutes before he quickly issued a correction, another followup tweet that said there were conflicting reports on Giffords' condition. But the thing is, that 25 minutes is all the time it took for that inaccurate report to reverberate on Twitter and everywhere else across the internet.

Other news organizations like CNN and Fox News ran with the report and they all cited NPR as the source.

**Andy Carvin** : The NPR news twitter account at that point in time had around two million followers. By today's standards of some celebrity accounts, not particularly huge, but for them, it was one of the large news accounts on Twitter and so I think it's safe to say that the tweet reverberated much more broadly than the actual newscast did, because it was retweetable. It landed on people's desktops and they could click a button and ping-pong it further.

**AD** : [NPR eventually issued a correction and apology for the mistake on air and on Twitter.](<https://www.npr.org/sections/ombudsman/2011/01/11/132812196/nprs-giffords-mistake-re-learning-the-lesson-of-checking-sources>) But maybe an edit button would've stopped the tweet from reaching so many people with incorrect information. The incident happened almost eight years ago now, and Twitter has changed a lot since then. But one thing that hasn't changed is that there is still no edit button for tweets.

**AD** : Andy Carvin is a visiting professor at the [University of British Columbia School of Journalism](<https://journalism.ubc.ca/>) where he talks to students about how to create and navigate digital news and he joined us on Function to take me back to that tweet in 2011. We talked about how an edit button for tweets could possibly be used to report the news more responsibly and how he might want such a feature to work.

After my conversation with Andy, we'll hear from **Leslie Miley** who was formerly an engineering manager at Twitter and also someone who thought deeply about the impact that Twitter has on the world.

* * *

> #### "There wasn't a protocol for managing breaking news through social platforms at that point in time at NPR when it came to weekends." — Andy Carvin

* * *

**AD** : Andy Carvin, thank you for joining us on Function. Can you give people a little bit of background about what it is that you do and especially what you were doing a few years ago online?

**Andy Carvin** : Currently, I am a visiting professor at the University of British Columbia up in Vancouver where I'm teaching in the journalism school social media and visual storytelling. But I've spent the better part of the last ten to fifteen years working at different news organizations experimenting with ways to incorporate social platforms into the news gathering process. I found it and ran the social media team at NPR for a number of years. Most recently, I was senior editor-at-large at Now This News up in New York. So been playing in the social space for a while and been around with it for the many highs and lows of the whole thing.

**AD** : Right. So one of things that's really interesting is you've been in the thick of how do we report news on social media and how do we tell people what's happening in the world and I wanna go back to a moment several years ago now, when you were at NPR. It was in January of 2011, as almost everybody will recall, there was a really horrific shooting of Gabby Giffords who was then the [Arizona] congresswoman and NPR was one of the first outlets that was covering the story.

Can you give us a little bit of context about what it was like at NPR covering the story and what happened in the minutes after the news broke?

**AC** : Well, something a lot of people probably don't realize is that NPR, unlike a lot of news networks, isn't a 24/7 operation. There generally isn't a huge number of people working on the weekends apart from running the shows that happen on the weekends, so beyond that, it's a much smaller team than what you would expect on a typical weekday.

And on that particular day, Gabby Giffords was having a meetup essentially, at a local supermarket. It started around noon East Coast time and very quickly a gunman came, shot her and a number of other people. Multiple people died. It was an absolutely catastrophic situation.

Coincidentally, the wife of a local NPR news director was across the street at the time and called her husband and he was able to get there to the scene while Congresswoman Giffords was still there injured and hadn't been taken away in the ambulance yet. And so word quickly spread through the public radio system that this had happened and they went on air locally pretty quickly and we started reporting it somewhere around 1 p.m. East Coast time.

On that particular day I had a day off. It was a weekend and so I was sitting at a restaurant with my wife and a 4-year-old and a 2-year-old just relaxing and having no idea what was happening at that particular moment. Behind the scenes, as they were approaching the top of the hour for the next major newscast, a news director in Arizona called and said that they talked to someone in the Pima County sheriff's office confirming that congressman Giffords had passed away.

So the newscast staff scrambled to confirm that and just before — literally minutes before they had to go on air — a congressional report on Capitol Hill confirmed through one of her Congressional sources, that she had died as well. And so with those two sources in mind, they went on air and announced that she had passed away. This then was sent around as an email alert; it was the lead story on the NPR website. I wouldn't have known it was even happening except for the fact that I got the email alert. Knowing that NPR didn't have a social media staff running weekends at that point in time, I looked at the Twitter feed at NPR News and nothing — there weren't any recent updates as to what had happened. So I copy and pasted the latest headline which said that she had passed away and a link to it and sent it out, approximately 2:12 to 2:15 p.m., so almost 15 minutes after the news cast.

And having felt I'd done my part, I finished my lunch, put the kids in the car, got in with my wife, and started driving 20 minutes to get back home. In that 20 minute period, chaos broke out because all sorts of people in the news industry started contacting folks at NPR saying, "Why are you saying this? We've confirmed she's in surgery right now, she has not passed away."

And so NPR's news blogger at the time pretty quickly started posting updates on the blog saying that there were conflicting reports. But at this point, no one was running the Twitter feed because I'm in my car with my kids. And when I get home, I go back on Twitter and turn on the TV and look at all the at-replies I received from colleagues and peers in the industry saying that she's still alive. And so I sent out a tweet — it must've been 20 or 25 minutes after that original tweet — saying that there are conflicting reports about her status.

Because NPR only does live newscasts at the top of the hour on weekends, _another_ 25 minute would pass before anyone went on air to say that she was still alive. They didn't issue a correction, they just said that she was in surgery. There was no way of taking it back at this point.

Reuters, CNN, Fox, _The New York Times_ , so many news organizations, apart from a small number such as the AP, ran with the story saying that NPR had confirmed that she had died and some of them found additional sources claiming the same thing.

But then they started retracting it as they learned more about it. Because those news organizations were often doing minute-by-minute live coverage, rolling coverage, they were able to correct it quickly, but because of the structure of NPR and the hourly newscast and the fact that there weren't people in the newsroom to run a rolling live breaking newscast, the change in the reporting wasn't issued until an hour after that first report. It was a mess.

**AD** : How many people in an organization like that have the login for the public facing news account on their phone for Twitter or social media account?

**AC** : Well, let's see. This was early 2011 and we had a very small social media team, there were just three or four of us at the time and a number of producers had access to it, but they tended to be weekday producers. There wasn't a protocol for managing breaking news through social platforms at that point in time at NPR when it came to weekends.

If something like this had happened on a weekday, it would be a matter of a managing editor running down to one of our desks and say _get over here, we're starting to cover this story._ Afterwards, it became clear how NPR screwed this up. It turns out that the source that the local news director used, a person from the sheriff's office, and the source we used in Washington, DC from Congress, they both got the information from the same person who happened to be another law enforcement official locally. And so what NPR didn't know at the time is there weren't actually two sources, there were two people repeating the same thing they had heard from one source.

And if protocols had been followed and if they had contacted the executive producer of the newscast, who would've been home on weekend at that point, there's a very good chance this never have happened because there's normally a standard of three independent confirmations to report a death. So to say mistakes were made is a bit of an understatement.

**AD** : So this is interesting because I'm stuck on this moment being a time when a major media organization is still very casual about social media. It's just 2011 and it's interesting to think of how much this has changed since then, right. Where there would be much more of a mature process or a formal process even on the weekends probably.

**AC** : Oh very much so. The social media at the time was not considered part of the newsroom. We weren't even on the same floor as the newsroom. We were near the tech folks and the music team. So along with the process isolation, there was the physical isolation of our team not being fully integrated. Even though we had started doing social media back in 2007 and 2008, it took many, many years for the newsroom at large to realize that we had to be fully incorporated if this ever was gonna work effectively.

**AD** : And these days it feels like what journalists do has evolved to have more process around it and this is something you were early to learn, but others have followed in learning these lessons and then maybe the audience, the followers on social media are a little better understanding the first stories that come out might be fuzzy or inaccurate or something like that.

**AC** : In an ideal world, the Twitter audience would be more aware of that, but the reality is there is always going to be a percentage of the online public that's going to retweet and comment upon anything they see and in some ways, it's their retweeting of it and sharing it within their own networks that ends up being the most insidious part of it. But there are ways of trying to push back.

A number of years ago, I worked with the folks at [On The Media](<https://www.wnycstudios.org/shows/otm>) to produce what they called, I think, was [the news literacy consumer handbook.](<https://www.wnyc.org/story/breaking-news-consumers-handbook-pdf/>) And it was basically a top ten list of all the things you should know during a major breaking news story. For example, there's almost never two shooters during a shooting incident and a bunch of others that we worked on and wrote out. So everytime, there's a big story, it's always heartening to see NPR and other folks sharing that list, because it's just as relevant today as it was before.

But practices in news organizations still haven't changed in many ways, so if you turn on a cable news broadcast, you're gonna hear plenty of pundits saying, "I don't want to speculate, but..." _and then they go ahead and speculate._ And so you're seeing what plays out on social media is often mirroring exactly what's playing out live on TV.

What I've seen on so many occasions is the mistakes that get amplified are first shared via broadcast, whether it's TV, radio or cable. They get amplified by social and social is generally able to respond with a correction or at least a questioning of the facts faster than the people who are on air. Because you can look directly at the phone and have people saying _this is crazy, that's not true, check your sources again_ , whereas if you're on air talking away, you have to wait for your producer to talk in your ear and you may be checking your laptop to see what's on your Tweetdeck, but you're still processing a lot of information. So in some ways things are better, but at the same time, I think there's still a sizable number of people who will share pretty much anything they see or what they wanna believe.

**AD** : Right. So let me actually get into that point about the amplification and correction because this is a big part of this and part of why it's so insidious or so dangerous is the amplification. And one of the challenges...there is the old story about how a lie travels around the world before the truth even gets its shoes on even where it's not a lie but it's just merely something that's inaccurate or an error.

**AC** : Do you know what I love about that quote? It's been attributed to Winston Churchill, Mark Twain and half a dozen other people and a version of it can be traced all the way back to Jonathan Swift. And so even the quote gets misquoted and misattributed to people which I just find deliciously ironic.

**AD** : Right. Entirely appropriately misattributed, right?

**AC** : Yep.

**AD** : So to that point, we think about amplification, the knee-jerk reaction of people, especially outside of media or outside of tech, is "well if you know everybody's gonna amplify this and retweet it, shouldn't we be able to just go in and edit the tweet and update it and say this is the corrected information"? What are your feelings on that?

**AC** : Oh, absolutely. I've been begging Twitter for years going back to at least 2008 for some sort of mechanism to do this. I think in an ideal world, after I sent that tweet regarding congresswoman Giffords, there would've been a way for me to edit the tweet and the act of vetting it would be immediately replacing every retweet that went out. It would either @-reply or DM everyone who had shared it, and not only would it be corrected, but it would alert anyone who had helped amplify it. It wouldn't be just the ability to edit the tweet, there would also have to be a mechanism that alerts directly to people who might have contributed to amplifying it.

**AD** : So there's an interesting thing here, because one of the big issues around media manipulation and misinformation on social networks, not just Twitter but Facebook and the others, especially in the current political environment where we've seen these things be targeted, whether it's by groups within the US, here domestically or international efforts, is this ability to throw doubt on what's shared on these networks. The undermining of veracity, undermining of credibility as a big tactic. And we see sites that regularly will post a headline that they know to be false, wait for people to screenshot it at you and then amend it and say, "Oh, you know sorry, our bad" and other tactics like that.

If we look at that environment where there is almost the war on whether something can be known to be true or not, has a whole playbook around it.

Do you think that that idea of the editable tweet or the thing where you still alert everybody has retweeted something is gonna be relevant? Do you think people amplify something because they wanna share the correct information or because it reeifies their view of the world?

**AC** : Generally speaking, I wish it was more the former but we just have to be honest that for a lot of people they amplify things because they wanna look impressive around their friends that there's something that they believe to be true and they know their peers will feel the same, and so they end up pushing things along.

There is no technical mechanism that could ever be created that's going to get a small percentage of the public to do, what I consider their civic duty, to correct false information they would've shared. Whether it's for personal reasons, political reasons, cultural reasons...they have decided that they are either so mistrustful or want to sow that mistrust that it doesn't matter what the platforms do or third parties creating apps to try to make this easier. I don't see there being a solution that's going to get around these trolls.

So the best we can do is have tools that will alert the people — that would ideally alert everyone — but perhaps allow you to concentrate on the people in your network who you know have the most influence. Even while that's going on, it certainly doesn't hurt to send a DM or get on the phone with people you know who have large followers and tell them what you've just corrected so they go ahead and do the same thing.

So I think the solution still involves whoever first shared the misinformation accidentally, they have the responsibility to contact as many people as possible who can help make that correction, but even with the best editing and versioning tools that a platform can come up with, you will still have bad actors out there who are going to make a mess of things.

**AD** : That's an interesting point because the other thing that happens, and especially these days, but it might have even started back in 2011, is on Twitter — [the Twitter thread](<https://blog.twitter.com/official/en_us/topics/product/2017/nicethreads.html>). So somebody replies to a tweet with additional information; sometimes that's used for corrections now, right? So, if you say, "The sun has risen in the West," and somebody replies and says, "The sun has risen in the East," and it's part of the same thread, it might carry through. That user interface, or that choice in the app, wasn't there seven years ago, but it is there now. Is that a sufficient correction?

**AC** : I think it certainly helps if a news organization or an individual posts something that they find out to be incorrect. I think the responsible thing to do would be to reply to yourself in your own thread to correct it, and then perhaps even send out a separate tweet so there's something independently not getting buried within a thread. But having it in the thread, and then explaining how you made the mistake, which I think is key, is really important because if you are going to maintain trust with the public, or if you are going to attempt to regain that trust after you've made a mistake, you have to hold yourself accountable and be as transparent as possible. I always find it frustrating when a correction is made and then they just move on as if it was no big deal.

When I've made mistakes, I've tried to explain step-by-step how I got to that point, and hopefully by doing that — being sincere and trying to explain how we got to this point — helps reinforce the bonds of trust that I have with my online community.

**AD** : Let me ask you a slightly different question which is: what about deleting it? If something's been shared by an organization that they find out is erroneous, they find out is a mistake, should they just take it away? Take away that tweet, that Facebook post?

**AC** : This is one of the toughest questions, and I don't think there's a single solid answer. If you pull a bunch of news organizations, you're gonna find some who say in their standards and practices that you need to delete it; others will say that you keep it and use follow-up tweets to correct. On that particular day in 2011, for example, Reuters decided to delete their tweet; NPR did not. Or at that point in time, honestly, I did not because it was a weekend and there was no protocol for these sorts of things.

**AD** : Right.

**AC** : But a number of people called me out on that, and my response to them was, "We're already in a bit of a lose-lose situation because I posted this information, and it turns out to be horrifyingly incorrect; but because NPR gets pulled into politics so easily because of the small amount of federal funding it gets, that if I hit the delete button and got rid of it, some people would treat that as a cover-up, that we were trying to hide our error, and I can guarantee you that some member of Congress would end up calling one of the senior editors asking about the deleting and wanting a paper trail for how that decision was made.

**AD** : That's interesting because that's sort of specific to the organization, but there's this broader question about what deleting signifies, what replying or threading signifies, what editing would signify. Because you have on networks like Facebook and lots of other platforms, where you can edit sometimes for a little while, sometimes going forward, and then there's a little note that says that you did that. Is that enough accountability for making a change?

**AC** : You know, I think there's a stronger argument today when it comes to deleting a tweet because another thing that's changed over these last seven or eight years is the whole notion of [native retweets](<https://blog.twitter.com/official/en_us/a/2009/project-retweet-phase-one.html>). Back then, people would send out a tweet that would begin with the letters "RT" and would have the text following it. So, retweets that would go out would be amplified by individual user accounts under their own names. So, if I ended up deleting that NPR tweet, it would still exist in other forms based on people manually retweeting it. Today, at least, if a new organization chose to delete it, all of those native re-tweets would disappear along with it, but it still raises the issue of accountability and transparency, and I think every news organization has to decide, "Is it worth having that tweet continuing to pinball around the universe for a period of time while you are adding to the threat, correcting it, or do you start with a clean slate, delete it, and create a new thread?" I still don't think there's a right or wrong answer. I think there's a strong argument that could be made in both cases.

**AD** : It seems like there's something analogous in almost all of these networks. Like, you can't easily go into Instagram and replace a photo that you've already posted, right? So if you're saying, "My hair was out of place and I'd like to put a better photo in there," but keep it that same post with all the likes and the responses, do you think they should enable that?

**AC** : I think they probably should, especially in the case of platforms like Instagram; and some of my work over the years, one of the things my team would try to do is that if we saw a photo was being shared that we knew to be out of context or a hoax, we would watermark it in the most flagrant of ways to make it clear that anyone seeing the image...it's stamped right across it in large red all-cap letters "FAKE" or "DEBUNKED" and then have in the text explaining why this particular image has nothing to do with the news at hand. So, yeah, ideally if Instagram had either a method to replace the photo or to overlay it with some sort of watermark that acts as a correction, because you can edit the text, but not everyone is gonna read the text. So I think, at minimum, being able to watermark it with new text on top of it, or some sort of X or checkmark acknowledging something's been confirmed or debunked, would make new organizations' lives a lot easier.

**AD** : So, I'm curious here about a big takeaway. We started this conversation talking about that moment with Congresswoman Giffords, and it's been seven, almost eight years since then, and you spend time with students. You are the authority. You are the one that's teaching them about how to use these platforms. If you look at the responsibility of how to use these networks, you look at the gravity of sharing information, and what happens when something is shared out of context, or inaccurate information. What are the responsibilities of the platforms, and what are the responsibilities of us as individuals, or even as journalists or cultural creatives, for how we use these platforms?

VIDEO

**AC** : Starting with us as individuals, like I alluded to earlier, I truly believe that people who share information on social networks have a civic responsibility to get it right, and people need to understand the gravity of their own influence. Even if they only have 30 followers on Twitter or 30 friends on Facebook, and it's just their crowd of people that they hang out with at school, you still have a responsibility to make sure that what you're passing along to them is correct, because otherwise you become an enabler of misinformation, and an enabler of the spread of distrust in people in platforms and institutions.

I think in some ways what needs to happen is developing a cultural sense of responsibility that as you use social media, and as your network of people grows, you have to be self-reflective on the potential power you have to be a leader among your peers, in terms of sharing information, or how you can potentially become a problem in terms of sharing misinformation; and a lot of people are just gonna brush that idea off and say, "I don't care. I'm just talking to my buddies here." But the reason why this stuff gets around everywhere is because something that may feel like it's peer-to-peer at the beginning continues to expand and expand and expand until it's too late to put it back in the box. So, unless we can get as many people as possible who utilize these tools to recognize their social responsibility or their civic duty to be as factual as possible, I think we're gonna continue seeing plenty of people share stuff and then just move on, whether it's correct or not.

And you'll never get everyone to do it. There will always be a percentage of the population that just does not give a damn about what they just shared; but there are probably many more people somewhere in the middle that shared something, sincerely thought it was true; and if you made it easier for them to send a correction out, they would probably do it. That gets to the responsibility of the platforms, and what mechanisms they can create that allow people to amplify corrections and fact-checking among their own networks. Because it's very hard for the news industry, writ large, to convince the platforms, their engineers spending lots of time, in product development and making changes just for our industry. I think we need to be able to communicate to the platforms that this is a much larger cultural and societal problem, and we need to put tools in the hands of members of the general public, and find ways of educating them, and making it as seamless as possible for them to be even a little bit more responsible in how they use social media. It would make a big difference.

**AD** : Andy Carvin, thank you for joining us on Function, and for all your insights into how our social networks work.

**AC** : Thanks, Anil. I really appreciate it.

* * *

> #### "From a product perspective, I'm not sure that this is actually solvable." — Leslie Miley

* * *

**AD** : Okay, so clearly there's an argument to be made for Twitter to introduce a feature that lets us edit our tweets; in fact, it's one of the most requested features that people ask for; and Twitter's own CEO, Jack Dorsey, actually talked about the idea of editing tweets when the idea came up at the Power of 18 Conference in India:

**Jack Dorsey** : "People want to edit because they make mistakes on Twitter, and they want to quickly fix 'em; that's a lot more achievable than allowing people to edit any tweet all the way back in time because what happens with that if I say something, like I tweet something that you agree with and then you retweet that, and then I edit the tweet to something that you disagree with, you've retweeted now something that you disagree with, and that's what we need to prevent. There's a bunch of things that we could do to show a change log, and show how a tweet has been changed, and we're looking at all this stuff. So, we've been considering edit for quite some time."

**AD** : So, it sounds like letting people edit tweets could be complicated from the technical perspective, but extremely complicated from an ethical perspective.

I talked to Leslie Miley about this. Now, Leslie is a former Engineering Manager at Twitter, and he's also led engineering teams for Slack and for Google, and these days he's the Chief Technology Officer of the Obama Foundation.

I especially want to talk to Leslie because he's one of the entire tech industry's best thinkers about how to translate doing the right thing into the actual features we use, and he did a lot of that at Twitter working with their Trust teams or Safety teams around making sure people had a good experience, and really pushed hard for people to get what they wanted out of the platform without a lot of the attacks, and the stress and the harassment and the abuse that people often associate with Twitter.

Leslie, welcome to Function.

**Leslie Miley** : Anil, thank you for having me.

**AD** : So, we'll get into the nitty-gritty of the edit button first. I wanna back up a little bit. You spent some time at Twitter. When were you there? How did you end up at the company?

**LM** : It was a drunken night in San Francisco. No. They reached out to me, oddly enough; and while I had been a frequent user of the service, I'd never thought about working there. When I met some of the folks, Dick Costolo in particular, he's really a dynamic leader, and really just encouraged me to take a chance on coming into Twitter and see what I could make there. I didn't come there to do product, initially. I actually joined to do a function that could be best described as DevOps.

**AD** : DevOps is development operations, which is providing the infrastructure for your code to run your software.

**LM** : Yes. However, after about a year, I was approached to do a revamp of the mute button that Twitter had rolled-out a few months before; it had gone over really poorly. They had to essentially retract, take the feature back to it's original point, and then we were going to try again. It was really an interesting situation because no one wanted to do it, and I couldn't understand why; when I started asking people around the company why, they said, "Because anyone who ever tries to touch safety, security or abuse and harassment at Twitter ends up getting fired or quitting," and there was just this black hole of product feature work that no one wanted to do. I thought it was a great opportunity because it was hitting up on population groups that I cared about, generally women and people of color who are I think abused on Twitter more than most people. So, I took that on, and that's how I started getting involved in feature and product work at Twitter.

**AD** : All right. So, you were brought in by Dick Costolo who at the time was the CEO of Twitter, right?

**LM** : Yes.

**AD** : And you start to work on a mute button, which is one of the most maybe contentious features of that era of Twitter. You said they had to try to launch this thing twice.

**LM** : Launched it. It had a terrible response. Activists were up in arms; of course, they were tweeting and they were talking to the press. [I believe Dick actually apologized for this publicly.](<https://blog.twitter.com/official/en_us/a/2013/reverting-the-changes-to-block-functionality.html>)

**AD** : Never a good sign for your feature, if that's the way it starts.

**LM** : Never. I think he probably tweeted out an apology and rolled the feature back. Then, I was given an opportunity to put together a product team to go and fix it. And we fixed that. And in fixing that, we realized that we needed a function around safety and security, and started to build-out a team for that, and that was the team that in 2014-2015 was handling, that did "report a tweet". It was 21 steps to report a tweet for abuse or harassment or violent threat, and in our work we actually reduced that to six steps.

**AD** : So, that's a huge leap forward, and it gives a glimpse into what it takes to get something, as what feels to a user as simple as a block button or a report button or a mute button, takes a ton of work from a product team to be able to do this stuff.

What are some of the considerations that come up? How do you think about when a feature or a button is implemented in a platform like Twitter, the way it rolls out in terms of the number of users, the way it works around the world? What are all the big considerations that maybe an ordinary user doesn't know about?

**LM** : I wish I could answer that question from a 2015 perspective rather than a 2018 perspective because so much has changed since then, and maybe I'll give you an example when we changed the Report A Tweet function. So, first we had to dig into the current feature like, "What's going on here? Why is this so difficult?" and when I went through and counted the steps, it's like, "Why should it take 21 steps to report someone for tweeting out a death threat against you or someone you know?" And a credible death threat. When I asked around the company, the answer that I kept coming back with was that years earlier there were so many reports for tweets, for so many violations or perceived violations, that the user services team couldn't keep up with it. So they intentionally made it more difficult to report a tweet so they didn't have as many reports.

**AD** : Wow.

**LM** : So, therein lies, "How do you go and fix this?" and "What does this mean?" When we re-did the feature and rolled it out, I believe we rolled it out to 25% of our user base, which at the time was probably coming up on 300 million monthly active users. I may not be fully clear on this because it's been several years, but the number of reports that were received I think jumped 10x at a rollout of 25%, and it flooded User Services, they could not keep up, and we had to take a step back. So, that's why I said it's difficult to give you...I'd like to give you a 2015 perspective and not a 2018 perspective.

**AD** : Right.

**LM** : Because some of the points that you want to look at when you're doing a feature is: How is this going to impact how users interact with your service? How is this going to impact the things from latency in your product, things from how many reports your User Services team get, how fast they can respond to them, and even things as simple as how much do you let someone write in a text field for a report for a tweet? Because you don't want somebody to be able to put _War and Peace_ in there, but you also don't want to limit it to 140 characters. So, there was a lot of consideration that had to go into making, "Oh, how do you do the 'Report A Tweet' now?" How are we going to do this from a product perspective from iOS Android and Web.

One of the other considerations we had to make, and I think it was the right consideration at the time, was to go from a native experience for this particular feature to a web view because we realized that while it wasn't one of the most highly trafficked in the Twitter app, it was something that we could do from in a web view that would allow us to make changes both on Web Android and iOS all at the same time.

**AD** : Mm-hmm. And so to explain to folks what that means, what it meant is you shifted from that app that runs right on your iPhone or right on your Android phone into basically a form that worked as it would in a web browser, but lived with in the app and that let's you experiment a little bit more or work a little bit more quickly in getting out changes to users.

So that's a great glimpse into how it gets real complicated real quickly when you've got hundreds and millions of people on a platform. Now I wanna shift a little bit into...how do you decide this is the button we're gonna work on, this is the feature we're gonna work on, is that the sort of thing where a noral person on the team can say, "You know, I'd like to build an edit button on Twitter," or is that a top down, a CEO Jack Dorsey or a CEO Dick Costolo comes and says from on high, now it is time for us to all assemble around building an edit button?

**LM** : The somewhat simple answer to that question is yes. It actually happens in both ways.

**AD** : Okay.

**LM** : It's fascinating because in a lot of tech companies, everyone from an engineer, a solo engineer to the CEO can suggest a feature and in some cases, a lot of features come from both ends, right? They come from the engineer who just converted from their internship to the CEO who doesn't like something. And now these are not normal cases, but it does happen. Generally it comes from a product team that consists of a product manager, it consists of a UX person — a user experience person — it consists of an engineer, maybe a technical program manager...and we look at things like whether or not you're trying to move a particular number, a particular metric or you're trying to get more users, are you trying to better understand how people are using something right so you may want to what we call _instrument_ or add logins, so Anil, that's something you know a lot about. Add logins to a feature to understand how people are using it so that you can better modify the feature in the future.

So it really is up to the product team to set what we call OKRs or objectives and key results, and those should have metrics or numbers that we want to move in one direction or another like more engagement on this particular feature or more users, or less reports coming in, or in something like the "Report a Tweet" button, we really wanted to make it simpler and we were going to measure that by how fast people could actually complete the process, when in reality what we really should have been measuring, strangely enough, was the number of reports coming in.

**AD** : Okay, so let's wave our magic wands, and pretend that we have the power, the ability to cause somebody at Twitter or some product team at Twitter, to think about doing an edit button. And one of the reasons I ask this, I think there's a lot of people on Twitter that get frustrated, they have a typo, and they say, "Gosh, you can make a live realtime video streaming service on top of Twitter that works globally and yet you can't let me edit the text on this thing; that seems outrageous," right, so before we talk about whether it should be done, let's talk about if a company like Twitter, were to enable editing of tweets, of the core messages that make up the platform, what would some of the considerations be? What are some of the questions you have to answer at a tech level all of a sudden?

**LM** : The first question I would ask is, how do you fan out a tweet to 50 or 60 million followers if someone can edit it every five minutes or every one minute? The technical and...just the scale of something like that is _crazy_ , because if I were to tweet...well let's not use me, let's use somebody who I really like, say Barack Obama tweets something out...

**AD** : And he's got a 100 million followers or whatever it is right?

**LM** : ...a 100 million followers and he's just like, "Everyone go out and vote," and he spells "vote" wrong, which he wouldn't do right, but still... And then 10 minutes later, he realizes that he spells vote wrong, so he wants to edit that tweet and change it. Well that tweet has now been fanned out to, maybe not a 100 million people, but a lot of people, and there have been notifications there kicked off and there are retweets that get kicked off and there's comment tweets that get kicked off and then all of a sudden, he changes this. So what do you do then?

How do you handle that? And that's a product decision, and someone needs to map that out and said, "Okay so if that happens, how do we handle notifications, how do we handle alerts, how do we handle emails, how do we handle everything," right, and so that's just like a very small piece of it and I think that starts to underline a lot of the technical issues, and the technical issues of changing something in a realtime system and having it update in a reasonable amount of time across a network that spans the globe. it's not an easy thing to do.

It's not impossible. Trying to update a tweet, while it's still fanning out...I can't even _begin_ to think about just how...the technical challenges of doing that. The latency that you'd have to start considering when you literally have a tweet that was sent 10 minutes ago that still hasn't been fanned out to everyone and all of a sudden it's been changed, so the amount of churn in the system would be pretty interesting.

**AD** : Okay, so you get into some very very complicated problems and it's interesting because it seems to me, from a layperson's standpoint, sending a tweet kind of feels like sending an email, like, here's my message and it goes out there and maybe it's going to one recipient and maybe it's going to a couple of people I've cc'd, but it's out there and they got it in their inbox and we're all good and that's sort of how I imagine at a naïve level how Twitter works. But what if all of a sudden we're able to make changes and assuming we would just keep being able to edit that tweet forever, to me that feels a little bit more like Dropbox or Box, one of these services where it's syncing my files or like Google Drive, where it's syncing my files between different places, so they have to be kept in sync all of a sudden.

**LM** : I like that analogy because if you think about that and you think about — we will go back to the Barack Obama example, an account with a 100 million followers — try syncing with a 100 million followers, and then continue to do that, and then what happens with accounts that are managed by several people that you can tweet once from DC and once from Chicago within five minutes of each other. You and I both have watched these things with threaded tweets and subtweets and retweets and then you delete a tweet and then you have tweets that are just hanging out there without any context. From a product perspective, I'm not sure that this is actually solvable.

**AD** : Okay so that's a very hard technical challenge. Immediately people would start to say, "Or maybe you can cheat, maybe you could only edit your tweet for 10 seconds after you send it or maybe the change could only be less than five characters 'cause it has to be for typos instead of changing the meaning of it," so a lot of people suggested this like you constrain the problem and you limit the ways that you can edit or for how long you can edit. Does that reduce this technical complexity at all? Does that make it doable or is it sort of still the same kind of problem?

**LM** : I think it's the same kind of problem, and I think the testing this out at scale would be the issue. The problem with trying to constrain it is, now you're adding artificial constraints to, or constraints to a system that was never designed for it. And how do you even begin to map that out? How do you even begin to map that out from a resource consumption standpoint, because to do something like that is _extremely_ resource intensive. You now have a timer on every account, you have a timer on every tweet. I think constraining it doesn't make it simpler, constraining it just makes the number of potential fail points smaller.

**AD** : So I am convinced that this is a very very hard technical problem. Let me pretend as if money is no object and technical complexity is no concern, and that we're able to do it anyway. You and I are the new CEOs at Twitter and we're able to say, you know what, damn the torpedoes, we are gonna go and build an edit button, I don't care what the cost is or how hard the computer science is. Let me shift into what I think is a much harder more interesting question. Should this be done? Is this a good idea?

**LM** : I would not answer that question myself. I would get people in a room to help me walk through that, and given Twitter's history and text history, I would bring in a lot of women of color, I would bring in a lot of marginalized groups who have been abused, who have been harassed, who have been using Twitter from the very beginning, and I would say, let's start talking about what this really means. I would bring in journalists. I would bring in people who have done public policy and I would really start talking this through because this is not a product decision, given the scope, the region, the impact of Twitter, that I think Twitter should make in a silo. I think they have to involve people in something like this, outside of Twitter.

The impact of something like this is so great. To me, it has the potential to make how [the Myanmar government is using Facebook to foment genocidal mobs](<https://www.nytimes.com/2018/10/15/technology/myanmar-facebook-genocide.html>); i think it makes that pale in comparison. Because then you get people, unfortunately like heads of state, who could change whatever they wanted, whenever they wanted in a way that could cause confusion, in a way that could cause violence to erupt, and not on a small scale but potentially on a city or government or cross-border scale.

**AD** : Hugely potentially destabilizing to the global media ecosystem, global political ecosystem, if people all of a sudden are able to do and undo messages that they send on Twitter or are able to change things on the fly that there's this sort of, you can't trust the words in front of you on this platform.

**LM** : That's at a macro scale; let's just boil this down to something smaller. What about a death threat?

And in a death threat, I will bring up something that I had my finger in, which was when Chuck C. Johnson was banned. [Chuck C. Johnson as one of the most prolific trolls on Twitter, up until he was banned for a death threat against a civil rights advocate in 2015, from Twitter in 2015, early 2015, the tweet that got him banned was, "If somebody pays me enough, I can take out someone."](<https://www.washingtonpost.com/news/the-intersect/wp/2015/05/26/charles-johnson-one-of-the-internets-most-infamous-trolls-has-finally-been-banned-from-twitter/?utm_term=.4e658d3e0d02>) And when he said this, it was very clear what that meant. Imagine if he could go back and change one or two words so that it isn't such a threat, would he still be on Twitter?

And the threat is still real. Just because you change it, doesn't make it less real. And so I think that is another consideration at a more micro level than at a macro level.

**AD** : That's kind of terrifying — the idea that editing on Twitter opens us up to abusers, manipulators taking advantage of the fact that no longer do we know for sure a tweet is a tweet, to be able to really put out messages that they don't have to even be accountable for.

**LM** : And a way to target abuse in a way that is probably more frightening than just a tweet that hangs out there or a tweet that was deleted. Imagine the people you and I both know who have gotten terrible threats on Twitter, that they only see it four or five minutes and then the person changes it to something more innocuous. I mean, talk about gaslighting and triggering people! This is why it's like if you do this, you need to bring people from so many different places into the room to walk through this because it may not be a feature you want to do.

**AD** : That raises an interesting question too because I think then ordinary users that wanna be able to just edit a typo, a completely reasonable request, they start to say, they hear these concerns and what I see people say is then, "Oh well then you show that it was edited, you show the history and say oh this was the original version and this is what changed," and then like Wikipedia lets you do this. Or even if you go into Google Docs or Microsoft Word, you can see the past revisions, track changes on your document. Doesn't that solve this problem? If it was initially a death threat and then you edit it and now it seems more harmless and innocuous, can't you still go back to the history and see it? Does that solve the issue?

**LM** : It's hard to retract a lie. Once something is out there, people will run with it and we have seen this over and over again in the last two years, where misinformation is purposefully put out there, and I do think it's on purpose. And then it's retracted or updated or changed, but the lie has already spread. Given what I know and how I've seen Twitter evolve, particularly as an abusive platform or a platform for some abusers, this frightens me even more. And when I say it frightens me, it _really_ frightens me. It really frightens me because people all of a sudden don't have to be responsible for...even less responsible for what they say today.

You know because they can say, "Well that's not what I meant." Perfect example was...[what did Trump say about when he was talking to Putin and he had asked Putin a question and they said, and literally he changed one word and it changed the entire meaning, and that's what he went with?](<https://www.nytimes.com/2018/07/17/us/politics/donald-trump-putin.html>)

I think that's what we would be giving heads of state, that's what we would be giving CEOs of companies — we won't name any — that's what we would be giving people with millions and tens of millions of followers is an ability to not be responsible. And you have to think about that, and what is the potential impact — and this is something that, it's a conversation that's happening in tech every day now — which is, what is our responsibility?

To me, this is the crux of an edit button or any other feature that allows information to be changed, particularly information that's disseminated so quickly and at scale, is that what is our responsibility and are we being good stewards when we roll out features that could potentially allow a user, a head of state or a company to manipulate a country of people or a market?

**AD** : So Leslie Miley, I think that question about accountability, responsibility, what these platforms owe to the world in exchange for having connected us and also made billions of dollars doing it...I think that may be the question that we are all reckoning with every day and I thank you for joining us on Function to dig into it.

**LM** : Thank you for having me.

**AD** : So it's been almost a decade of people on Twitter saying, "I wish I could edit my tweets and I think both Andy and Leslie made a good argument for what are some of the reasons we might wanna do it and even the good benefits that we would have if news organizations for example being able to make sure that their tweets are accurate. But Leslie and I went deep into that conversation about the risks and about that bigger issue: can we trust anything we see online? And that risk seems like a reason to _not_ allow people to edit tweets. You know, I can see the debate, nobody's ever gonna resolve this until Twitter decides one way or the other, but if I'm sitting in their shoes, I have to feel like the danger of undermining people's already fragile trust, and the things they read online, might make me come down on the side of saying, you know what, if you tweeted it, you gotta stand behind it: it is what it is. There's not gonna be an edit button on Twitter.

That's it for this week at Function. Next week, we are gonna talk about YouTube...specifically the way the creators get caught up in copyright while trying to share their ideas or creations on YouTube. We're even gonna talk to a lawyer who's an expert on an intellectual property right and see what's even possible to do on YouTube.

Function is produced by Bridget Armstrong, our associate producer is Maurice Cherry, Nishat Kurwa is the executive producer of audio for the Vox Media Podcast Network. Our engineers are Srinivas Ramamurthy and Jarrett Floyd and thanks to Jelani Carter for your help this week. Our theme music was composed by Brandon McFarland and big thanks to the entire team at Glitch. [You can follow me on Twitter at @anildash](<https://twitter.com/anildash>), and of course you can always check out Function at [glitch.com/function](<https://glitch.com/function>). So please remember to subscribe to the show wherever you listen, and we'll be back next week with a brand new episode.
