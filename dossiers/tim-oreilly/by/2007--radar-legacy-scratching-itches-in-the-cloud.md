---
title: "Scratching itches in the cloud"
person: tim-oreilly
section: by
type: blog-post
year: 2007
date: 2007-08-04
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2007/08/scratching_itch.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Scratching itches in the cloud

## Full text

Sriram Krishnan has a great blog post entitled [Open source and scratching itches in the cloud](http://www.sriramkrishnan.com/blog/2007/08/open-source-and-scratching-itches-in.html) that takes off from my recent [post about hadoop](http://radar.oreilly.com/archives/2007/08/yahoos_bet_on_h.html). Sriram points out the difficulties of "scratching your own itch" with server-backed applications, for three reasons (with my comments in parentheses): 

  1. The inaccessibility of the back-end code, and the fact that that code is shared by many simultaneous users. (You can submit a bug report or feature request for either proprietary or open source code, and your success rate in getting your problem fixed depends more on the responsiveness of the development organization than on whether the code is open or closed source. What you get with open source is a second level of recourse: you can patch your own local version of the program, and if you feel strongly enough about the importance of your patches, you can fork the entire source tree and see if other people adopt your version. But when the user no longer has the choice of running a separate copy, due to the scale of the application and its data (see points 2 and 3), this recourse is gone, whether or not the code is open source.) 

  2. The fact that the value of the application relies on shared and collective data. (This has been my fundamental point about Web 2.0 from the beginning: that it represents an entirely new paradigm for potential lock-in. There's a kind of natural lock-in at work here, which I've elsewhere referred to as the ebay effect. I don't think we can fix that. If the biggest database is the best, it will continue to get bigger and better. But that doesn't mean that the owner of that database shouldn't be opening it up so that users can own their own data in that database. Ownership includes transparency (what data do you have about me?), my ability to correct it (think identity theft and credit scores -- but you need not go that far. For example, if Amazon has incorrect metadata about an O'Reilly book, you'd think that Amazon would trust us, as the publisher, to fix it.), and the ability to easily extract that data for archival purposes, re-usability, or mobility elsewhere. (Imagine, for instance, being able to move your "friends list" from LinkedIn to Facebook.) I agree with Dare Obasanjo when he says [just getting your own data out doesn't really solve the problem](http://www.25hoursaday.com/weblog/2007/08/03/Web20IsTheNewVendorLockin.aspx), but I wouldn't go as far as he does to say that vendors owe us the ability to export their entire database! Just because we might like it doesn't mean we deserve to get it.) 

  3. The fact that the application relies on a very large hardware platform. As Sriram points out, this issue may be going away with new commodity computing services like S3 and EC2 (what some people have started to refer to as "hardware as a service.") (But quite frankly, if we solve the open data problem, I think we get more "freedom" and benefit for users than solving either the hardware or software lock-in problem.)
