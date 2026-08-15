---
title: "Google Bets Big on HTML 5: News from Google I/O"
person: tim-oreilly
section: by
type: blog-post
year: 2009
date: 2009-05-27
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2009/05/google-bets-big-on-html-5.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Google Bets Big on HTML 5: News from Google I/O

## Full text

"Never underestimate the web," says Google VP of Engineering [Vic Gundotra](http://www.google.com/corporate/execs.html#gundotra) in his keynote at [Google I/O](http://code.google.com/events/io/schedule.html) this morning. He goes on to tell the story of a meeting he remembers when he was VP of Platform Evangelism at Microsoft five years ago. "We believed that web apps would never rival desktop apps. There was this small company called [Keyhole](http://en.wikipedia.org/wiki/Keyhole,_Inc), which made this most fantastic geo-visualization software for Windows. This was the kind of software we always used to prove to ourselves that there were things that could _never_ be done on the web." A few months later, Google acquired Keyhole, and shortly thereafter released Google Maps with satellite view. 

"We knew then that the web had won," he said. "What was once thought impossible is now commonplace."

Google doesn't want to repeat that mistake, and as a result, he said, "we're betting big on HTML 5." 

Vic pointed out that the rate of browser innovation is accelerating, with new browser releases nearly every other month. The slide below, from early in Vic's talk, shows the progress towards the level of UI functionality found in desktop apps through adoption of HTML 5 features in browsers. This looks like one of Clayton Christensen's classic "[disruptive innovation vs sustaining innovation](http://www.12manage.com/methods_christensen_disruptive_innovation.html)" graphs. It's also fascinating to see how mobile browsers are in the forefront of the innovation. 

[](http://radar.oreilly.com/upload/2009/05/browser_innovation.png)

While the entire [HTML 5](http://en.wikipedia.org/wiki/HTML_5) standard is years or more from adoption, there are many powerful features available in browsers today. In fact, five key next-generation features are already available in the latest (sometimes experimental) browser builds from Firefox, Opera, Safari, and Google Chrome. (Microsoft has announced that it will support HTML 5, and as Vic noted, "We eagerly await evidence of that.") Here's Vic's HTML 5 scorecard:

[](http://radar.oreilly.com/upload/2009/05/html5.png)

  1. The [canvas](http://www.whatwg.org/specs/web-apps/current-work/multipage/the-canvas-element.html#the-canvas-element) element provides a straightforward and powerful way to draw arbitrary graphics on a web page using Javascript. Sample applications demoed at the show include [a simple drawing area](http://htmlfive.appspot.com/static/draw.html) and [a simple game](http://htmlfive.appspot.com/static/gifter.html). But to see the real power of the Canvas element, take a look at Mozilla's [BeSpin](https://bespin.mozilla.com/). Bespin is an extensible code editor with an interface so rich that it's hard to believe it was written entirely in Javascript and HTML.

  2. The [video](http://www.whatwg.org/specs/web-apps/current-work/multipage/video.html#video) element aims to make it as easy to embed video on a web page as it is to embed images today. No plugins, no mismatched codecs. See for example, this [simple video editor running in Safari](http://htmlfive.appspot.com/static/video.html). And check out the page source for [this YouTube demo](http://www.youtube.com/html5). (As a special bonus, the video is demonstrating the power of O3D, an open source 3D rendering API for the browser.)

  3. The [geolocation APIs](http://dev.w3.org/geo/api/spec-source.html) make location, whether generated via GPS, cell-tower triangulation or wi-fi databases (what [Skyhook calls hybrid positioning](http://www.skyhookwireless.com/howitworks/)) available to any HTML 5-compatible browser-based app. At the conference, Google shows off [your current location to any Google map](http://0.gfe4.serve.steveblock.da.borg.google.com/maps), and announces the availability of [Google Latitude](http://www.google.com/latitude/intro.html) for the iPhone. (It will be available shortly after Apple releases OS 3.) What's really impressive about Latitude on the phone is that it's a web app, with all the platform independence that implies, not a platform-dependent phone application.

  4. [AppCache and Database](http://www.whatwg.org/specs/web-apps/current-work/multipage/offline.html#appcache) make it easy to build offline apps. The killer demo is one that [Vic first showed](http://fora.tv/2009/04/03/A_Conversation_with_Vic_Gundotra) at [Web 2.0 Expo San Francisco](http://web2expo.com) a few months ago: offline gmail on an Android phone. But Vic also shows off [a simple "stickies" app running in Safari](http://htmlfive.appspot.com/). 

(I love the language that Vic uses: "You can even store the application itself offline and rehydrate it on demand.")

  5. [Web workers](http://www.whatwg.org/specs/web-workers/current-work/) is a mechanism for spinning off background threads to do processing that would otherwise slow the browser to a crawl. For a convincing demo, take a look at a web page [calculating primes without web workers](http://htmlfive.appspot.com/static/primes-bad.html). As the demo says, "Click 'Go!' to hose your browser." Then check out [the version with web workers](http://htmlfive.appspot.com/static/primes-good.html). Primes start appearing, with no hit to browser performance. Even more impressive is a [demo of video motion tracking](http://htmlfive.appspot.com/static/tracker1.html), using Javascript in the browser.

During his keynote, Vic was joined on stage by Jay Sullivan, VP of Mobile at Mozilla and Michael Abbot, the SVP in charge of application software and services at Palm. Both showed their own commitment to working with HTML 5. Jay expressed Mozilla's commitment to keeping the web open: "Anything should be hackable; anything should be scriptable. We need to get out of plugin prison." Javascript rendering in Firefox 3.5 is 10x faster than in Firefox 2, with support for video, offline storage, web workers, and geolocation. 

Michael showed how Palm's WebOS relies on HTML 5. "You as a developer don't need to leave your prior knowledge at the door to develop for the phone." He demonstrates the power of CSS transformations to provide UI effects; he shows how the calendar app is drawn with Canvas, how bookmarks and history are kept in an HTML 5 database. Michael emphasized the importance of standardization, but also suggested that we need new extensions to HTML 5, for example, to support events from the accelerometer in the phone. Palm has had to run out ahead of the standards in this area. 

If you're like me, you had no idea there was so much HTML 5 already in play. When I checked in with my editors at O'Reilly, the general consensus was that HTML 5 isn't going to be ready till 2010. Sitepoint, another leading publisher on web technology, recently [sent out a poll to their experts](http://www.sitepoint.com/newsletter/viewissue.php?id=3&issue=241) and came to the same conclusion. Yet Google, Mozilla, and Palm gave us all a big whack upside the head this morning. As Shakespeare said, "The hot blood leaps over the cold decree." The technology is here even if the standards committees haven't caught up. Developers are taking notice of these new features, and aren't waiting for formal approval. That's as it should be. As Dave Clark described the philosophy of the [IETF](http://en.wikipedia.org/wiki/IETF) with regard to internet standardization, "We reject: kings, presidents, and voting. We believe in: rough consensus and running code." 

Support by four major browsers adds up to "rough consensus" in my book. We're seeing running code at Google I/O, and I'd imagine the 4000 developers in attendance will soon be producing a lot more. So I think we're off to the races. As Vic said to me in an interview yesterday morning, "The web has not seen this level of transformation, this level of acceleration, in the past ten years." 

Vic ends the HTML 5 portion of his keynote with hints of an announcement tomorrow: "Don't be late for the keynote tomorrow morning." 

**Additional Resources**

Here is a convenient list of [the HTML 5 demo apps shown in the keynote this morning](http://htmlfive.appspot.com/). Be sure to look at the page source for each of the applications. 

[New developer features in Firefox 3.5](https://developer.mozilla.org/en/Firefox_3.5_for_developers)

To learn more about these HTML 5 features, check out these tutorials from the Opera, Mozilla, Palm, and Google teams (plus a few others): 

Canvas: [HTML 5 Canvas: The Basics](http://dev.opera.com/articles/view/html-5-canvas-the-basics/)   
[Painting with HTML 5 Canvas](http://dev.opera.com/articles/view/html5-canvas-painting/)

Video: [A Call for Video on the Web](http://dev.opera.com/articles/view/a-call-for-video-on-the-web-opera-vid/)  
[HTML 5 Video Examples](http://www.bluishcoder.co.nz/2008/10/html-5-video-element-examples.html)

Geolocation: [Track User Geolocation with Javascript](http://www.webmonkey.com/tutorial/Track_User_Geolocation_With_JavaScript)

Web cache and database: [Palm WebOS HTML 5 DataBase Storage](http://www.weboshelp.net/webos-tutorials/156-palm-webos-html5-database-storage-tutorial)   
[HTML 5 Features in Latest iPhone Applications](http://ajaxian.com/archives/html5-features-in-latest-iphone-application-cache-and-database)   
[Gmail for Mobile: Using AppCache to Launch Offline](http://google-code-updates.blogspot.com/2009/04/gmail-for-mobile-html5-series-using.html)

Web workers: [Using DOM Workers](https://developer.mozilla.org/En/Using_DOM_workers)
