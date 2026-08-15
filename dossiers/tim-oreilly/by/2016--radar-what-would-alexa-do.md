---
title: "What would Alexa do?"
person: tim-oreilly
section: by
type: blog-post
year: 2016
date: 2016-08-19
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/what-would-alexa-do/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# What would Alexa do?

## Full text

Every once in a while, a product comes along that changes everyone’s expectations of what’s possible in user interfaces. The Mac. The World Wide Web. The iPhone. Alexa belongs in that elite group of game changers. Siri didn’t make it over the hump, despite the buzz it created. Neither did Google Now or Cortana, despite their amazing capabilities and their progress in adoption. (Mary Meeker reports that [20% of Google searches on mobile are now done by voice](<https://techcrunch.com/2016/06/01/mary-meeker-internet-trends-2016/>), and Google Now cards are an essential part of every Android user’s experience.) But Alexa has done so many things right that everyone else has missed that it is, to my mind, the first winning product of the conversational era.

Let me talk you through a sample conversation to show you what I mean.

I’m standing in the kitchen cooking, hands dirty. “Alexa, play ‘Hamilton’.” (Yes, like everyone else who’s seen it, or even heard it once, I’m addicted!) “Playing songs from [the original cast recording of ‘Hamilton](<https://smile.amazon.com/Hamilton-Original-Broadway-Recording-Explicit/dp/B0135P6PZA/ref=sr_1_2?ie=UTF8&qid=1471480214&sr=8-2&keywords=hamilton>)’ …” “Alexa, louder.” “Alexa, set a timer for 30 minutes.” [Music volume goes way down but is still audible while Alexa replies.] “Setting a timer for 30 minutes.” [Volume comes back up] … “Alexa, what song is that?” [Again, volume goes down while Alexa replies, then returns to previous volume.] “’Guns and Ships,’ by Leslie Odom, Jr., Daveed Diggs, Christopher Jackson, Original Broadway Cast of ‘Hamilton’”… [Phone rings.] “Alexa, pause.” [Scramble to wash hands. Wish Alexa was also the interface to my phone!]  [End phone conversation.] “Alexa, resume.” “Alexa, how much time is left?” “About 9 minutes and 50 seconds left.”

What’s right about this:

1\. Alexa is always listening, so it’s hands-free. Once you get used to talking to the thin air and have a device wake up and respond, the idea of pawing at a screen feels as odd as a phone without a touchscreen did starting in 2007, when we got our first taste of multitouch on the iPhone. Touching a microphone icon to go into speech mode doesn’t cut it.

2\. Alexa can handle some degree of state with aplomb. I can “stack” multiple interactions, and have “her” guess with some accuracy which context a subsequent interaction belongs to. She knows that “pause” goes with the music,  and “how much time is left?” goes with the timer.

3\. I didn’t need to be taught many of the possible interactions. I just guessed that they might work, tried them, and discovered that they do. For example, I discovered that I could ask Alexa what was playing when I called up an elderly friend to whom I’d given an Echo to see how she liked it. She did, she said, except for the fact that she didn’t always know what music she was hearing. (Since she was afraid she wouldn’t know how to use it, I’d given her very simple instructions, like “Say ‘Alexa, play Mozart.'”) “Why don’t you try asking?” I said. “Say, ‘Alexa, what’s playing?'” Sure enough, Alexa came back with the exact name (and performers and conductor) of the classical piece she was listening to.

4\. The design nuance that the volume simply goes down and Alexa talks over it during an overlapping interaction is one of those “fit and finish” touches that are part of what makes a new UI paradigm (like the one represented by the original Mac or the iPhone) hum, and be a thing of beauty.

Let me contrast this with a similar interaction with Google on my phone.

First off, by default, Google isn’t listening on most phones. You have to touch the microphone icon to get it to switch to audio input. This is partly a power issue–unlike an Amazon Echo, the phone has battery life considerations–but it is also a privacy issue. I had a conversation with an Alphabet exec in which I made the point that Amazon had totally stolen a march on them with the Echo. He replied, “Can you imagine the blowback if it were Google that was always listening to you?” He had a point. But that’s how the future happens. Someone breaks the barrier, does the unthinkable, and then it becomes thinkable for everyone. I believe that we’re at that point with always-on listening agents.

At least on my Nexus 6P, Google has given me the option to enable always on-listening, even from the phone’s lock screen. Apple has done the same with Siri on the iPhone 6. But active listening isn’t yet on by default, and I suspect eventually it will be. (I first enjoyed this feature on my Moto X, and it made me truly love the phone. But that feature didn’t catch on sufficiently to make the phone a breakout success. And now that I’ve experienced voice interfaces done right on the Echo, I think I know why.)

So let’s assume I can wake up my phone hands-free simply by talking with it. Let’s replay that interaction, this time on my Nexus 6P.

“Ok, Google, play ‘Hamilton’.” “’Hamilton’ is a musical about the life of American fFounding father Alexander Hamilton, with music, lyrics and book by Lin-Manuel Miranda.” [Fail. Responds with the result of a Google search, despite the obvious “play” instruction. Doesn’t respond with “this is not in your library.” So I try again.] “Ok, Google, play Bob Dylan.” [Google Play opens, starts playing Bob Dylan from my library.] Good so far. “Ok Google, pause.” Nada. From now on, I’m expected to interact with the app by touching the screen. Have to hit the pause button.

But let me try other possible actions while the music plays. “Ok, Google, what song is playing?” “’Obviously 5 Believers’.” That’s promising! But once Google has answered my query about the song, Google Play Music is no longer in the foreground. Some other app or mode has answered my question. So I can’t even pause or skip the song with a single touch of the screen. I first have to navigate back to Google Play Music. But even when I do that, I don’t get to the control to pause or stop the song. Instead, I get a screen asking me to “Try Unlimited.” 

That’s just bad interaction design, putting the goals of the platform provider above my own. But even if that intervening screen weren’t there, you can see that the handoff model, where the conversational agent passes control to an old-school smartphone app, introduces needless complexity into the interface. The conversational agent needs to remain in the foreground, intercepting requests and routing them to the right app (and if necessary, translating them into the native language of the app so that the user doesn’t have to switch modes).

I touch “NO THANKS.” Now I can see and press the pause button.

But let’s go back to the sample interaction. The music is playing. Can I run the timer over it? “Ok, Google, set a timer for 10 minutes.” [Music stops entirely – a much less pleasing interaction than Alexa’s gentle muting – while the Clock opens, giving me the countdown timer from which I can see how much time is left, or, if I like, touches to stop or change the timer.] Music resumes playing, but now the Clock app is in the foreground.

And when I asked “Ok, Google, how much time is left?” the question was passed neither to Google Play, nor the Clock. Instead, Google read to me a search result about a calculation that the earth has 7.79 billion years left in [the habitable zone](<https://en.wikipedia.org/wiki/Circumstellar_habitable_zone>).

Let me be clear: the raw capabilities that Google brings to the table are far in excess of Alexa’s. I can ask Google questions that Alexa doesn’t have a hope of answering. “Ok, Google, how long will it take me to get to Palo Alto?” “Traffic is heavy so it will take you an hour and 10 minutes.” And because of its massive amount of stored data as well as real-time sensor data from my phone, and because of its unparalleled expertise in AI, I expect Google to be able to do many things that are impossible for Alexa.  But that’s precisely why Google should be studying Alexa’s voice UI and emulating it.

The user interaction flow between Google’s voice interface and its mobile apps is a disaster, as I’m lost in a maze of applications, each of which expects to have control, because the voice agent has never been given authority as conductor of the user experience. I’m forced to switch modes unnecessarily between voice and touch. And when the agent doesn’t know what to do, it often invokes clearly unrelated actions. (Alexa does this too occasionally, but far less often. It’s much better at saying “I don’t know how to answer the question you just asked.”)

In addition to creating a consistent voice-only interaction, Alexa’s creators have smartly partitioned the possibility space into domains, each with an understandable set of related tasks and questions that are within the capabilities of the agent. Unlike agents that take the model of “ask me anything” and often fail ungracefully (Siri), or trying to guess what I might want and surface that information unasked (Google Now), Amazon has done a brilliant job of information architecture. Let’s think deeply about music, and design for key interactions. OK, how about weather? How about a kitchen timer? What can we do to make the device more fun? (“Alexa, tell me a joke.”)  There’s real evidence of clear and consistent human design anticipation throughout the product.  This allows Alexa to appear more intelligent than she actually is.

Alexa’s creators demonstrate an essential insight for the era in which we’ll increasingly be designing interfaces with and for intelligent agents. Remember that your agent is essentially stupid, and use humans to put it in known situations where its limited abilities are sufficient, and users can easily learn about its capabilities.

Human-Computer Interaction takes big leaps every once in a while. The next generation of speech interfaces is one of those leaps. Humans are increasingly going to be interacting with devices that are able to listen to us and talk back (and increasingly, they are going to be able to see us as well, and to personalize their behavior based on who they recognize). And they are going to get better and better at processing a wide range of ways of expressing intention, rather than limiting us to a single defined action like a touch, click, or swipe.

Recent advice says that the hype about conversational interfaces is overdone. “[Bots are better without conversation](<https://medium.com/@tedlivingston/bots-are-better-without-conversation-fcf9e7634fc4#.hyxtyh6fi>),” says Ted Livingston of [Kik](<https://www.kik.com/>), a text-message based bot platform.

I don’t buy that. My experience with Alexa on the Amazon Echo convinces me otherwise. Of course, Alexa isn’t a chatbot. It’s a powerful voice-based service embodied in a special purpose device. It demonstrates that conversational interfaces can work, if they are designed right.

That leads me to the title of this piece: _What would Alexa do?_

Alexa gives us a taste of the future, in the way that Google did around the turn of the millennium. We were still early in both the big data era and the cloud era, and Google was seen as an outlier, a company with a specialized product that, while amazing, seemed outside the mainstream of the industry. Within a few years, it WAS the mainstream, having changed the rules of the game forever.

My work on what I called [Web 2.0](<http://www.oreilly.com/pub/a/web2/archive/what-is-web-20.html>) over a decade ago was an extended meditation on lessons to be learned from Google (and other pioneers of the emerging generation of web applications, platforms and services.) Eventually, these lessons were seen as required learning for every organization, which had to transform itself or die. In that “Oh sh*t” moment, Jeff Jarvis wrote a book called [What Would Google Do?](<https://www.amazon.com/What-Would-Google-Do-Reverse-Engineering/dp/0061709697>), whose cover copy advertised it as “an indispensable manual for survival and success in today’s Internet-driven marketplace.” That is, if you didn’t figure out how to do what Google does, you were screwed! I feel that way right now about Alexa.

If you’re making any kind of consumer gadget for the home–a TV, a music system, a thermostat, a security system, a Wi-Fi router, a dishwasher, or a washing machine–you should be asking yourself, “What would Alexa do?” If you’re an automotive executive planning to put a big touchscreen in your upcoming model instead of focusing on voice control, you should be asking yourself “What would Alexa do?” If you’re a software company, you should be imagining a future in which the devices used to interact with your software are increasingly conversational, and asking yourself “What would Alexa do?”  Heck, if you’re a restaurant or coffee shop with an app that lets people order and pay in advance, you should be asking “What would Alexa do?”

Fortunately, Amazon is a platform thinker, and so they’ve provided a neat set of affordances not just for Alexa users but for Alexa developers. App developers can add “skills” to Alexa using the [Alexa Skills Kit](<https://developer.amazon.com/appsandservices/solutions/alexa/alexa-skills-kit>)–for example, once you’ve added the Lyft skill, you can say, “Alexa, ask Lyft to call me a car.” And using the [Alexa Voice Service](<https://developer.amazon.com/alexa-voice-service>), developers can add voice commands to their own applications. ([Google also has a speech API](<https://cloud.google.com/speech/>), and [so does Microsoft](<https://www.microsoft.com/cognitive-services/en-us/speech-api>).)

Unfortunately, there’s no design API, so you’ll have to pay close attention to the way that Amazon has designed the Alexa interface, constantly asking yourself “What would Alexa do?” as you design your speech-enabled application. Designers who carry over too much baggage from the touch screen era, and don’t learn to think natively about speech interfaces, are likely to build poorly thought-out hybrid experiences like the one that keeps me from using speech as an effective interface to many of the functions of my Android phone.

I recently had the “What would Alexa do?” conversation with a senior technology leader at Facebook. I was pointing out that Facebook uses AI to curate my news feed, with the notion that by watching my behavior, it can guess what stories I most want to see. But I don’t always want to see the same thing, I noted, any more than I want a music player that only provides its own curated stream and doesn’t give me any choices.  It’s true that sometimes I want to listen to music that the service chooses for me, but often, I want to express some choice. So too with Facebook. Rather than trying to decide from all the possible posts from my friends which to show me, give me some affordances for expressing my intention.

An Alexa-like Facebook interface would let me say “Facebook, show me personal updates from my friends,” and the AI would go to work not trying to divine my taste, but in separating personal updates from links to news stories. At another time, I might say “Facebook, show me links about politics from my friends,” or “Facebook, show me funny videos.” This is AI put in service of my choices, not trying to replace my choices.

Right now, if I want Facebook to do any of those things, I can only do it by retraining the algorithm over a period of days, religiously avoiding favoriting or clicking on links of the type I don’t want to see while choosing only the type I do want. I can’t just switch back and forth!

What Alexa has shown us that rather than trying to boil the ocean with AI and conversational interfaces, what we need to do is to apply human design intelligence, break down the conversation into smaller domains where you can deliver satisfying results, and within those domains, spend a lot of time thinking through the “fit and finish” so that interfaces are intuitive, interactions are complete, and that what most people try to do “just works.”

_This piece was originally published on[LinkedIn](<https://www.linkedin.com/pulse/what-would-alexa-do-tim-o-reilly>)_ _._
