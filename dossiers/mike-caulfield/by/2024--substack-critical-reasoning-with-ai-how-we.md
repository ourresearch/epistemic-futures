---
title: "Critical Reasoning with AI: How we know LLMs are applying reasoning patterns, and not just reverse image searching"
person: mike-caulfield
section: by
type: blog-post
year: 2024
date: 2024-12-31
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/critical-reasoning-with-ai-how-we
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Critical Reasoning with AI: How we know LLMs are applying reasoning patterns, and not just reverse image searching

*Writing this because I'm tired of having this argument*

## Full text

I usually share my experiments on analyzing images with LLMs freely, because they demonstrate advances in reasoning of the latest models, advances which I think will be game-changing for education.

Invariably when I do this, no matter how impressive the results are I get the same response from some people — it’s just matching on something in the dataset. It’s just reverse image searching the entire internet and finding some photo of the same thing and reproducing what someone wrote about that image. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

When I was an AI skeptic (not a horrible one — but one who didn’t think there was that much of a role for AI in education) I would get very irritated by the gullibility of the AI boosters. And I still do. 

We are absolutely in an AI bubble, for instance. The thing is going to pop. I happen to think it’s an AI bubble in kind of the way that dot com in the 1990s was a bubble — that there’s a real there there. It’s not as life-changing as the internet was, but it’s not MOOCs/Crypto/NFTs/VR either. It’s absolutely bubble though, and this incessant drive to shove AI into every last thing is ridiculous at best, and the world is full of AI grifters. I still believe that.

But having overcome my broader skepticism, I find I’m just shocked at the mental gymnastics militant _cynics_ will execute to avoid admitting that generative AI is doing anything particularly unique or useful. There’s a whole mythology. The photo issue is just one example of that. For testing out prompts I will often use photos that are after the training set cutoff date, so I can make sure the response is not keying off of something specific in the training set. People then tell me that Claude or ChatGPT is secretly doing reverse image searches on the back end. I’m not sure what they think happens then — I suppose use that to find the page it’s on, consume all the text on that page and then use that to guide the response. 

This would be an amazing feature, of course, to be able to precisely identify all photos ever on the internet in real time with 100% accuracy no matter how they were cropped or annotated, load relevant context in, and use that to form a response. If a company could show this in action in their product, working in this seamless way that people describe, they’d get a good stock boost after that demo. It’d be a highlight of Google I/O. 

But what people are actually arguing to me is that companies somehow have this ability and are keeping it secret. Because if there’s one thing these companies hate, it’s money. 

Anyway, I’m sure I’ve already upset some people with this intro, but I have heard this same theory from dozens of people, that anything that LLMs do that is impressive is really just the fingerprinting of some undiscovered analysis some person wrote on LiveJournal in 2003 about this very specific issue. We can’t seem to locate that analysis, it’s invisible to all search engines. But it’s there somewhere, because the only skill these tools have is plagiarism, and cannot produce unique reasoning.

I’ve become convinced that the people who make these arguments make them partially because they haven’t actually used LLMs other than what they see when doing Google searches, and maybe what they tried a couple years back with ChatGPT. Maybe it’s fruitless to even engage. But I’m tired of arguing about it on Bluesky and elsewhere, so I am writing this post to link people to instead of arguing.

## First, why do reasoning patterns matter?

Let’s start with why this whole argument is important at all.

The key for me has been demonstrating how LLMs, especially with the recent advances in reasoning models, do really interesting things that I think are going to revolutionize education. Namely they have gotten quite good at applying _reasoning patterns_ to facts and issues at hand.

For instance — you can take President Harrison’s national announcement of Columbus Day and ask Claude to read it like a historian. You can do this yourself if you want. Make sure to use the 3.5 Sonnet model which has the new reasoning advances in it (it's not technically a reasoning model but has been trained in a way that does well with these tasks). Upload the full text of the announcement. Then type:

_Read this document "historically" and tell me what you think the significance might have been._

Here’s the output of that. 

* * *

_Reading this document historically reveals several fascinating layers of significance in 1892 America:_

  1. _Nation-Building Context: The 1890s were a crucial period of American identity formation. This was the end of the "frontier era" (the Census Bureau had declared the frontier "closed" in 1890), and America was actively constructing narratives about its origins and destiny. The choice to celebrate Columbus so grandly suggests an attempt to create a longer, grander American origin story that predated the Pilgrims._

  2. _Immigration and Catholicism: The timing is significant because this period saw massive Italian and Catholic immigration to America. Elevating Columbus, an Italian Catholic, to such prominence could be seen as a gesture of inclusion toward these communities, though it's worth noting that significant anti-Catholic and anti-immigrant sentiment existed at this time._

  3. _Educational Emphasis: The proclamation's focus on schools reflects the Progressive Era's emphasis on public education as a tool for creating American citizens. This was a period of mandatory schooling laws and standardization of education. Using schools as centers for the celebration shows how civic rituals were being institutionalized through the education system._

  4. _Secularization vs. Religion: The document interestingly balances secular progress ("pioneer of progress and enlightenment") with religious providence, reflecting a period when America was becoming more secular while maintaining strong Protestant influences in public life._

  5. _Imperial Context: 1892 was a time when America was beginning to think more about its role as a world power. Celebrating Columbus's "discovery" could be seen as validating American expansionist ambitions - just a few years before the Spanish-American War would make America a colonial power._

  6. _Historical Memory: The proclamation shows how the 1890s viewed Columbus - as an enlightenment figure and bearer of civilization. This portrayal notably omits any mention of Native Americans or the complexities of colonization, reflecting the period's dominant narratives about progress and civilization._

  7. _Political Moment: Harrison was nearing the end of his presidency (he would lose to Grover Cleveland that year), and the country was experiencing significant labor unrest (the Homestead Strike occurred in 1892). The call for people to "cease from toil" and unite in patriotic celebration might be seen as an attempt to promote social harmony during a turbulent time._

_The proclamation thus serves as a window into multiple aspects of 1890s America: its nationalism, its educational system, its religious character, its imperial ambitions, and its way of understanding its own history. It's a document that shows how public commemorations were used to construct national identity during a crucial period of American development._

* * *

I showed this to a person I know, who is known for writing on this exact topic (the proclamation). He knows what’s out there. 

His response was that he could not imagine most any person analyzing this so thoroughly. Not the vast majority of historians. Certainly not your average graduate student. It’s a near perfect analysis. 

This is where the “one document out there” defense comes in. Due I think to a misconception that every LLM works just as it did in 2022, people reply that maybe no single person made all these points, but the system has plagiarized it from seven different places and sort of blended it into something new. In that telling, every piece of this is somewhere, more or less, in different words somewhere on the web.

**I’m sure some of it (most of it?) is elsewhere.** I’m _not_ saying that you can’t find this stuff out there. You can — but on the whole that’s not what’s going on here. At least, _that’s not the part that is making this an unusually good treatment of the issue_. (And one way we know this is until recent LLM models were released, LLMs could not produce this sort of answer — despite having _already_ swallowed the whole internet).

What is happening — at least in part — is this: Claude is looking at the sorts of things people talk about when they talk about history and in particular, that period of American history (I am talking high level here, of course all this is a result of semantic adjacency at the implementation level). And it’s looking at how people talk about documents like this. And then it is looking at the document, running through dozens of potential frames and looking for any intersection between what’s in the document and the available frames. And of course it is still running that normal LLM process we are familiar with to write the text. You can call this reasoning if you want, though it’s probably more accurate to talk about it as applying _reasoning patterns_ to a given context and seeing what happens. 

A lot of people’s understanding of these tools seems locked into 2022, and so many have missed this. But this is what these tools are getting scary good at doing — finding the _reasoning pattern intersections_ to define an approach and then using the standard LLM functionality to write it up. This is where they are, and this is where most of the recent gains are coming from and will come from.

I don’t think I need to make this point, but just in case: a world where a student can say “Show me how a historian might read this document” or “Show me how a public health sociologist would think about this chart” is a world where education is irrevocably changed, far more than by any project to use LLMs to produce textbooks or even to do more standard coaching and tutoring. I come from a liberal arts tradition, and this is the business of liberal arts in particular — giving students a broad set of disciplinary lenses to view the world, and building their proficiency in applying them to novel situations. Does it get facts wrong? Yeah, sometimes. But if it can reliably identify the _sorts_ of things you want to be thinking about and a general way you can _approach_ a problem, that’s game-changing.

## The “It’s always pulling from something someone already did somewhere” argument

So you can see the stakes here, and they are high. We could imagine a world, for example, where what has _really_ happened is that Anthropic read a bunch of student term papers and textbooks and there was enough content about this proclamation that could get tossed into the word blender and leveled up linguistically and refined to produce an analysis like this, in which case this approach is limited to things people have already written about, and is doing little more than summarizing current thinking (and possibly plagiarizing). If that were the case it’d be useful, but ultimately a glorified summarizer of the already written. And in some ways that’s a hard charge to rule out, because of you can find some text somewhere you can always say, aha, the source is this, there’s nothing going on interesting at all!

On the other hand, if it really is applying an emergent reasoning pattern library to novel questions, then it is something quite different. And of course it is doing a _bit of both_ , because the output is always doing that auto-predict thing that most people are familiar with at this point (and people will explain to you in the comments is a “stochastic parrot”, thereby winning some points in some grand game they seem to be playing where I can only assume the first person in a comment thread to say that gets a free turkey or something).

So people are invested, to say the least. And I fully expect that people will take this demonstration I am about to do and come up with yet another explanation. But here we go. I want to show you the analysis of something that I know has never been analyzed elsewhere, to make a bit clearer how these things work. 

Today I stumbled on two photos I took of my kid at the bus stop on September 27th and 28th in 2011. The other people in the photos are former neighbors who won’t mind me sharing. The photos were taken in a Keene, a New Hampshire college town. The pictures have never been on the web. The bus stop was just at the end of my street at the time, and had no known landmarks. To remove any metadata, I screenshotted the photos rather than download and upload them. Here they are:

[](<https://substackcdn.com/image/fetch/$s_!E_rw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cf6e080-cb46-4b07-9b18-334ad15a2037_856x653.png>)

[](<https://substackcdn.com/image/fetch/$s_!WIAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F822c9b5c-6c0e-4815-bef0-007f24a30ca1_849x628.png>)

(these are now a screenshot of a screenshot and hence slightly degraded, but it doesn’t matter for this example.)

The challenge is to ask Claude to figure out:

  1. Where these were taken

  2. In what year

  3. And what month

I uploaded the first one, and asked:

_where was this photo taken? explain your reasoning._

The first response:

_Based on several visual clues, this photo appears to be taken in the northeastern United States, likely in New England. Let me explain the reasoning behind this conclusion:_

_The school bus itself provides our first major clue - it shows "USDOT 254406" and is operated by "First Student," which is one of the largest school bus operators in North America. The style and color of this bus is the standard American school bus design._

_The environmental context gives us strong seasonal and geographical indicators. We can see trees with changing fall foliage in the background, displaying yellow and golden colors characteristic of autumn in the northeastern United States. The architecture visible in the background - particularly the house with what appears to be traditional New England-style features - is typical of residential areas in New England states._

_Another telling detail is the stone wall visible in the background. These stone walls are extremely common in New England, as they were built by farmers in the 18th and 19th centuries who cleared rocks from their fields. They became a distinctive feature of the New England landscape._

_The overall scene - with its suburban setting, tree-lined street, stone wall, and traditional architecture - combined with the fall foliage and the particular style of school bus operation, strongly suggests this is a typical morning school pickup in a New England town, possibly in a state like Massachusetts, Vermont, New Hampshire, or Maine._

I then uploaded the second and asked:

_Here's another photo. Can you guess the town? Explain your reasoning in detail._

Here was the response:

_Looking at this second photo along with the first one, I can break down several key details that help narrow down the location, likely to New Hampshire and quite possibly Durham, NH. Let me walk through the reasoning:_

_The environmental elements are distinctly New England:_

  * _The trees show early fall foliage transition, with maples beginning to turn yellow while some trees are still green, suggesting September in northern New England_

  *  _The overhead power lines are typical of New England residential areas_

  *  _The stone wall construction visible in both photos is characteristic of historic New England property boundaries_

 _The school bus details provide important clues:_

  * _It's operated by First Student, a major contractor in New Hampshire_

  *  _The bus appears to be picking up elementary school-aged children_

  *  _The USDOT number visible in the first photo (254406) is within a range commonly used in New Hampshire_

 _The residential setting offers additional context:_

  * _The homes visible in both photos show classic New England architecture_

  *  _The combination of older homes with stone walls suggests a historic New England town_

  *  _The layout shows a suburban-residential area near a school district_

  *  _The well-maintained lawns and sidewalks indicate an established, likely college town_

 _The presence of multiple parents/adults waiting with children at what appears to be a regular bus stop, combined with the architectural and natural features, suggests a community where many families live within walking distance of each other - typical of a college town like Durham._

_Durham, NH would fit all these characteristics as:_

  * _It's home to the University of New Hampshire_

  *  _It has historic residential neighborhoods with this exact type of architecture_

  *  _The town has many young families associated with the university_

  *  _The timing of the foliage change matches Durham's geographical location_

  *  _The stone walls and overall community layout are typical of Durham's historic development pattern_

 _While I can't be completely certain without more specific landmarks, these photos show many characteristics consistent with Durham, NH during the early fall school season._

Now I’ll note there are really only four small college towns in NH: Keene, Plymouth, Durham, and arguably Hanover (where Dartmouth is). So Durham was not an exact hit, but damn close. And importantly, the reasoning is rock-solid. It gets from anywhere in the world to “New Hampshire college town”, and while certainly the stated reasoning is not equal to it’s exact process, [it doesn’t matter](<https://mikecaulfield.substack.com/p/the-two-meanings-of-reasoning-and>): the reasoning is solid — at least in the context of asking it to make a _guess and defend it_.

So, onto the year. 

_These photos were taken within the last 30 years. What year do you think they were taken? Explain your reasoning._

Again, I’ll remind you — it doesn’t matter whether the system reasons, but [whether it can produce reasoning](<https://mikecaulfield.substack.com/p/the-two-meanings-of-reasoning-and>). Some of the reasons below are superfluous and some may be wrong, but there’s enough correct stuff in there to get you to this conclusion. Remember, the photo is from 2011. This places it from 2013-2015. Again, not bad at all.

_Let me help analyze these photos to estimate when they were taken, looking at several key details:_

_The School Bus Technology and Design The bus shows some important temporal markers. It's a CE (Conventional Engine) model with the distinctive First Student branding. The "NO STANDEES" marking and DOT number format suggest this is a relatively modern bus complying with post-2000 federal safety standards._

_Children's Fashion and Accessories The backpacks the children are wearing provide a particularly telling clue. We can see:_

  * _Multiple children wearing colorful backpacks with what appear to be character designs or bright patterns_

  *  _The backpack styles appear to be from the early to mid-2010s based on their size and design_

  *  _The children's clothing, including leggings and casual wear, is consistent with early-mid 2010s elementary school fashion_

 _Digital Image Quality The photo quality itself helps date the image:_

  * _The resolution and color clarity suggest a digital camera or smartphone from the early-mid 2010s_

  *  _There's some visible digital noise in the shadows, but overall good detail preservation_

  *  _The dynamic range handling is characteristic of cameras from this era_

 _Additional Environmental Context_

  *  _The stone wall and houses look well-maintained but not recently renovated_

  *  _The presence of overhead power lines (not buried) is consistent with infrastructure from this period_

  *  _The trees and landscaping appear mature and established_

 _Combining all these elements, I would estimate these photos were taken around 2013-2015. The combination of the bus safety standards, children's fashion, photographic technology, and overall scene composition strongly points to this time period. The photos have the characteristic look of images taken with smartphones or digital cameras that were common during those years._

Ok, so now we have a year and a place. What about a month?

_What month do you think this is? Explain your reasoning_

Here’s the response:

_Let's analyze several details from these photos to pinpoint the month. I'll break this down by examining multiple environmental and contextual clues:_

_The Foliage Stage The trees show early fall color transition, which is particularly informative. We can see:_

  * _Some trees are still predominantly green_

  *  _Others are beginning to show yellow coloration_

  *  _The leaf coverage is still full, with minimal leaf drop_

  *  _The grass remains green and appears recently mowed_

 _School Session Context The scene shows what appears to be a regular morning school bus pickup with:_

  * _Multiple children with backpacks_

  *  _Parents/adults accompanying them_

  *  _Everyone wearing light clothing appropriate for mild weather_

  *  _The casual, routine nature suggests this isn't the first day of school_

 _New England Fall Color Timing In New England, particularly in New Hampshire where these photos appear to be taken:_

  * _The fall foliage progression typically begins in late August to early September_

  *  _Peak foliage usually occurs in mid-October_

  *  _The partial color change we see suggests early stages of this transition_

 _Temperature Indicators The clothing choices provide temperature clues:_

  * _Children wearing a mix of short and long sleeves_

  *  _Some wearing leggings or pants_

  *  _Adults in casual, moderate-weather clothing_

  *  _No heavy jackets or summer-weight clothing visible_

 _Combining all these factors, these photos were most likely taken in mid-September 2011. This timing would coincide with:_

  * _The beginning stages of fall foliage change in New Hampshire_

  *  _Comfortable temperatures requiring light to moderate clothing_

  *  _The established routine of the school year being underway_

  *  _Optimal morning lighting conditions for photography_

 _This would place the photos several weeks into the school year, when bus stop routines are established, but before the more dramatic fall color changes and cooler temperatures of October._

So altogether, the two photos, never seen before on the internet, taken in Keene NH, September 2011 are identified as possible being taken in Durham NH, September 2013-2015. 

Reasoning patterns plus LLM output, modeling professional analysis — and hitting the mark. It feels like it shouldn’t work, and yet somehow it does.

You can do this with almost any professional or disciplinary lens you want to. It’s not perfect, but it’s usually helpful. There are tricks to asking the right way, and traps to avoid when interpreting. But it’s something new and strangely useful, and avoiding grappling with its implications is a bad look.

**Addendum:** As a commenter points out some of the reasons for the bus stop are unconvincing, and some are fabricated (or at least fuzzy). I thought I was more clear about this in the post, but maybe not. When assessing reasoning produced by an AI you need to think of it as reasons surfaced to you by a bright but overly motivated arguer that throws a bunch of spaghetti at the wall. Some of it sticks, and some of it is a real reach. None of it says for sure how the person can to their conclusion.   
  
So for example, with the First Student thing, it’s a good point that it probably puts it in the US/Canada. But it’s in 30 states, so it doesn’t really get you to NH, and the DOT range thing could be hallucinated — or could be something it’s figured out through pattern matching in photos. But you can’t use it without verifying. The no standees thing is something you’d want to verify. 

As I say repeatedly, LLMs are bad at facts, half-decent at reasoning. They know the patterns but they play a bit loose with the evidence at times.

The turning leaves are better, the stone wall (while not an original stone wall) is very New England, the part about a suburban + college town look is a pretty good guess. It’s not definitive but its something (and I’ve explicitly asked for _guesses_ , not proof). I am sure it is keying off of other things it is not expressing, and a piece of my work is to work to get it to do better identifying those, but the prompt used in this case was very bland. Likewise the stuff about time of year is best when talking about the leaves, and the clothing, less good when talking about it being a couple weeks into the school year. 

The point is _not_ that it is Skynet — the point here is it is trying to _fit reasoning patterns_ (and, of course, linguistic predictions) to the _evidence_ , and that’s how it is producing its text. Sometimes it overfits, almost always it generates more reasons than it has to, and doesn’t weight things well unless you ask it to. This turns out to be very useful because we humans are not quite as good at brainstorming ideas. Is it doing more with the image matching than it can express in the post-hoc reasoning? I’m sure of it. But once you understand that this is a reasoning generator, then you move on to how to better prompt it, and better evaluate its inputs. That’s what I plan to show over time if you subscribe to this substack. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
