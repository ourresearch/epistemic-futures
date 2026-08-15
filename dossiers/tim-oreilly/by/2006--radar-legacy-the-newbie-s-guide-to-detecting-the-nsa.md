---
title: "The Newbie's Guide to Detecting the NSA"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-06-30
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/06/the_newbies_guide_to_detecting.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# The Newbie's Guide to Detecting the NSA

## Full text

Over on [Dave Farber's IP List](http://www.interesting-people.org), John Bartas pointed to a [blog entry on Wired about AT&T and the NSA wiretapping controversy](http://blog.wired.com/27BStroke6/index.blog?entry_id=1510938). The entry begins: "It's not surprising that an expert hired by EFF should produce an analysis that supports the group's case against AT&T. But last week's public court filing of a redacted statement by J. Scott Marcus is still worth reading for the obvious expertise of its author, and the cunning insights he draws from the AT&T spy documents." There's a great summary of the reasons to believe that:

  * "The AT&T documents are authentic. 
  * There may be dozens of surveillance rooms in AT&T offices around the country. 
  * The internet surveillance program covers domestic traffic, not just international traffic. 
  * The system is capable of looking at content, not just addresses."

But as [John Bartas wrote on IP](http://iplist.blogspot.com/2006/06/ip-newbies-guide-to-detecting-nsa.html), "The best part is at the end. Good old traceroute!":

> ... "With that in mind, here's the 27B Stroke 6 guide to detecting if your traffic is being funneled into the secret room on San Francisco's Folsom street.

> If you're a Windows user, fire up an MS-DOS command prompt. Now type tracert followed by the domain name of the website, e-mail host, VoIP switch, or whatever destination you're interested in. Watch as the program spits out your route, line by line. 
> 
> C:\> tracert nsa.gov  
>  1 2 ms 2 ms 2 ms 12.110.110.204  
>  [...]  
>  7 11 ms 14 ms 10 ms as-0-0.bbr2.SanJose1.Level3.net [64.159.0.218]  
>  8 13 12 19 ms ae-23-56.car3.SanJose1.Level3.net [4.68.123.173]  
>  9 18 ms 16 ms 16 ms 192.205.33.17  
>  10 88 ms 92 ms 91 ms tbr2-p012201.sffca.ip.att.net [12.123.13.186]  
>  11 88 ms 90 ms 88 ms tbr1-cl2.sl9mo.ip.att.net [12.122.10.41]  
>  12 89 ms 97 ms 89 ms tbr1-cl4.wswdc.ip.att.net [12.122.10.29]  
>  13 89 ms 88 ms 88 ms ar2-a3120s6.wswdc.ip.att.net [12.123.8.65]  
>  14 102 ms 93 ms 112 ms 12.127.209.214  
>  15 94 ms 94 ms 93 ms 12.110.110.13  
>  16 * * *  
>  17 * * *  
>  18 * * 
> 
> In the above example, my traffic is jumping from Level 3 Communications to AT&T's network in San Francisco, presumably over the OC-48 circuit that AT&T tapped on February 20th, 2003, according to the Klein docs. The magic string you're looking for is sffca.ip.att.net. If it's present immediately above or below a non-att.net entry, then -- by Klein's allegations -- your packets are being copied into room 641A, and from there, illegally, to the NSA. Of course, if Marcus is correct and AT&T has installed these secret rooms all around the country, then any att.net entry in your route is a bad sign.
