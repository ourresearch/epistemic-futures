---
title: "Context Aware Programming"
person: tim-oreilly
section: by
type: blog-post
year: 2013
date: 2013-07-05
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2013/07/context-aware-programming.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Context Aware Programming

## Full text

I’m increasingly realizing that many of my gripes about applications these days are triggered by their failure to understand my context in the way that they can and should. For example:

  * [Unruly apps on my Android phone](https://plus.google.com/+TimOReilly/posts/Lw5WY69Y7WD), like gmail or twitter, update messages in the background as soon as I wake up my phone, slowing the phone to a crawl and making me wait to get to the app I really want. This is particularly irritating when I’m trying to place a phone call or write a text, but it can get in the way in the most surprising places. (It’s not clear to me if this is the application writers’ fault, or due to a fundamental flaw in the Android OS.)
  * Accuweather for Android, otherwise a great app, lets you set up multiple locations, which seems like it would be very handy for frequent travelers, but it inexplicably defaults to whichever location you set up first, regardless of where you are. Not only does it ignore the location sensor in the phone, it doesn’t even bother to remember the last location I chose.
  * The WMATA app (Washington Metro transit app) I just downloaded lets you specify and save up to twelve bus stops for which it will report next bus arrival times. Why on earth doesn’t it just detect what bus stop you are actually standing at?
  * And it’s not just mobile apps. Tweetdeck for Mac lets you schedule tweets for later in the day or on future dates, yet it defaults to the date that you last used the feature rather than today’s date! How frustrating is it to set the time of the tweet for the afternoon, only to be told “Cannot schedule a tweet for the past”, because you didn’t manually update the date to today!

In each of these cases, programmers seemingly have failed to understand that devices have senses, and that consulting those senses is the first step in making the application more intelligent. It’s as if a human, on awaking, blundered down to breakfast without opening his or her eyes!

By contrast, consider how some modern apps have used context awareness to create brilliant, transformative user experiences:

  * Uber, recognizing both where you are and where the nearest driver is, gives you an estimated time of pickup, connects the two of you, and lets you track progress towards that pickup.
  * Square Register notices anyone running Square Wallet entering the store, and pops up their name, face, and stored payment credentials on the register, creating a delightful in-store checkout experience.
  * Apps like FourSquare and Yelp are like an augmentation that adds GPS as a human sixth sense, letting you find restaurants and other attractions nearby. Google Maps does all that and more. (Even Google Maps sometimes loses the plot, though. For example, yesterday afternoon, I was on my way to Mount Vernon. Despite the fact that I was in Virginia, a search unadorned with the state name gave me as a first result Mount Vernon WA, rather than Mount Vernon VA. I’ve never understood how an app that can, and does, suggest the correct street name nearby before I’ve finished typing the building number can sometimes go so wrong.)
  * Google Now, while still a work in progress, does an ambitious job of intuiting things you might want to know about your environment. It understands your schedule, your location, the weather, the time, and things you have asked Google to remember on your behalf. It sometimes suggests things that you don’t care about, but I’d far rather than than an idiot application that requires me to use keystrokes or screen taps to tell the app things that my phone already knows.

Just as the switch from the command line to the GUI required new UI skills and sensibilities, mobile and sensor-based programming creates new opportunities to innovate, to surprise and delight the user, or, in failing to use the new capabilities, the opportunity to create frustration and anger. The bar has been raised. Developers who fail to embrace context-aware programming will eventually be left behind.
