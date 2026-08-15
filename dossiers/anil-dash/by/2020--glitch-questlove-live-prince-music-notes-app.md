---
title: "I Built an App to Accompany Questlove’s DJ Set in 20 Minutes"
person: anil-dash
section: by
type: blog-post
year: 2020
date: 2020-04-20
venue: "Glitch blog (blog.glitch.com; formerly Fog Creek)"
authors: "Anil Dash"
source_url: https://blog.glitch.com/post/questlove-live-prince-music-notes-app/
retrieved: 2026-08-13
content: full-text
notes: "Company blog post authored by Dash as CEO"
---

# I Built an App to Accompany Questlove’s DJ Set in 20 Minutes

## Full text

One of the few bright spots in the otherwise deeply distressing environment of the current global quarantine is the rise of superb live-streamed entertainment by some of the world’s most talented artists. Perhaps the most joyous distractions are the live DJ sets and music battles going on, like [D-Nice](<https://www.instagram.com/dnice/>)’s already-legendary #ClubQuarantine.

As [Teddy Riley](<https://www.instagram.com/teddyriley1/>)’s unfortunately tech-challenged Instagram set showed this weekend, managing the technology for providing entertainment to thousands of people can be hard to do if you don’t have access to the trained professionals who usually handle such things. So when [Questlove](<https://www.instagram.com/questlove/>) decided to do a series of nightly DJ sets as a [tribute to Prince](<https://www.instagram.com/p/B_DcNpGlMTn/>), I got a little bit nervous when I had the wild idea at the last minute to accompany his set by providing live “liner notes” that would let listeners know what songs they were listening to and to provide additional commentary and context.

You see, in addition to being the co-founder of the legendary hip hop group The Roots, and the bandleader of The Tonight Show, Questlove is a super music nerd. So, even as they’re dancing and getting their groove on, listeners to his [DJ sets](<https://www.rollingstone.com/music/music-news/questlove-dj-set-slow-jam-coronavirus-quarantine-971280/>) are also often in learning mode—it’s one part turntables and one part Wikipedia.

What makes it especially complicated is that I decided Questlove’s livestream needed these annotations about five minutes before he began his set. Fortunately for me he got a slightly late start but, in all, I had about 20 minutes to pull together an app to provide notes to an audience that, at its peak, numbered in the tens of thousands of simultaneous listeners.

I was able to pull it off. Appropriately, I did it by remixing—since that’s how you can instantly make apps on Glitch. The end result was [a simple app](<https://quest-live.glitch.me/>) showing off nearly twelve hours of amazing live DJing.

I had a very clear idea of how I wanted to present live “liner notes” to the audience for the DJ set:

  * I needed a simple, responsive web page that would load quickly for lots of users.
  * The page should offer some basic context explaining what was happening, including a [donation link for Food Hub](<https://bit.ly/QuestloveYTFoodHub>), the charity Questlove was trying to support
  * Prominently featured up top would be an embedded YouTube video of the stream, so the audience could listen while they read. (Though live DJ sets are currently mostly associated with Instagram, Questlove streams on all the major platforms simultaneously, including Instagram, YouTube, Twitch and Twitter/Periscope, which worked great because YouTube is embeddable and I think it has the best sound.)
  * The key dynamic part of the site would be a live-updated list of notes under the stream, with the newest at the top so users didn’t have to scroll.
  * We’d need a basic admin interface for easily posting new notes to the stream, ideally supporting HTML for the content so I could do formatting and links, and supporting multiple authors in case I wanted to ask anyone else to help write notes.

I also quickly figured out what I _didn’t_ want to build:

  * No authentication or user management
  * I didn’t want to build or include a rich-text editor that might complicate things That was a pretty simple spec. I had expected to create some kind of data persistence, but surprisingly, time constraints and the actual experience meant that I didn’t end up actually having a database at all!

Having only about 20 minutes to get a basic version of the page running meant that I knew time was of the essence. I knew that dropping in a responsive page template would be the easy part, so I set about to find the simplest possible way to get the page to update. I knew about [socket.io](<https://socket.io/>) since it’s extremely popular, but had actually never used it in a project I was creating from scratch myself. (We’re pretty familiar with its feature set since Glitch enables live, real-time simultaneous code editing.)

I searched for “[socket io demo](<https://glitch.com/search?q=socket%20io%20demo>)” on Glitch and there were tons of example projects, but the very first one had really clean code that I could quickly understand. In the example, it was a simple chat page with the updating interface at the bottom, so I remixed the app (that’s the Glitch term for making your own copy of an app) and set about to customize it.

My first edits were pretty simple: I split off the chat submission form into its own view, which I put at _/write_ so it would be separate from the main message stream. (For these purposes, security through obscurity was good enough.) Then, I did some quick edits to simplify how the messages were displayed on the main view.

Next, I wanted to get the page looking decent. I wanted the lightest possible framework that would give me a responsive page, so I just grabbed [Skeleton](<http://getskeleton.com/>) even though I had only tinkered with it and not used it in production before. Instead of doing a full build process, I dropped in a CDN link to a hosted version of the styles, and copied & pasted most of their boilerplate demo in to be the scaffolding for this new page. I just barely customized the standard CSS to change some colors, and pretty soon the output of the app was looking like a real webpage.

From that point, we were off to the races. I think at the point when I dropped into the livestream, there were about six thousand people in Questlove’s Instagram live session alone, and many, many more on YouTube and Twitch and the other platforms.

He has 3.4 million followers on Twitter, and almost 2 million on Instagram, and between shares from him and other high-profile people like chef [Tom Colicchio](<https://twitter.com/tomcolicchio>) who dropped in, a couple million people saw the link, and at least a few tens of thousands checked out the live notes while watching the stream.

Just after launching, I sent the _/write_ link to my friend [iammisstlc](<https://twitter.com/iammisstlc>) so that she could add notes to the stream as well, and we were both instantly able to annotate the music as it played. The only slight downside was it was impossible to tell if any particular update came from me or her, but for most of the content, it didn’t matter, and we just added our name to the text if it was pertinent.

A short while into the stream, after about 10,000 people were watching and we had already written a few thousand words, I remembered that I had never built any kind of persistence or storage for all these updates. Uh oh.

This was… not my finest moment. But I decided to save the rendered HTML from my browser as a static HTML page and figure out how to put that up as an archive later. It was hardly an elegant solution, but trying to live-document an event while following an incredibly fast-moving conversation across Instagram and YouTube comments _and_ while doing research to make sure the information was accurate didn’t leave a lot of time to come up with something more appropriate.

As it turned out, this embarrassingly hacky solution worked pretty well! Though I certainly wouldn’t repeat that decision, given the time constraints, it ended up serving our needs and people were really happy for the resource while enjoying the show.

Over the course of three days of streams, Questlove played over twelve hours (!) of music, and we published over fifteen thousand words of commentary, all delivered as people watched. We were joined by fans, journalists, artists and enthusiasts from around the world, including almost a dozen different musicians who had actually performed on the songs being played.

Through the entire experience, the app held up just as I’d hoped. (At Glitch, we’d recently launched a [paid level](<https://glitch.com/pricing>) of the service, and since I’m a member, the app had no rate limits on the amount of traffic it could serve up.) Because you can pick a URL on Glitch just by typing something in, it was really easy to get a memorable URL and people were easily able to share it even in spaces like Instagram live comments, where links can often be difficult to share.

In all, though this little Socket + Skeleton app was a success, there were a few things I would have done differently, or that I’d improve if I ever did this again:

  * Definitely start more than 20 minutes before needing to go live with an app in front of thousands of people.
  * Do use existing frameworks like Socket.io and Skeleton, but design from the user experience forward, instead of just copying & pasting their default examples.
  * Explore persistence solutions so that content is automatically archived appropriately; there are tons of open source CMSes that could solve this kind of thing easily.
  * Examine whether any of the APIs from the big platforms would make it easier to bring over comments from their live chats — there were tons of gems being shared, and it would be fun to highlight standout conversations.
