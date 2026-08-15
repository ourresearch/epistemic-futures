---
title: "The Universal JSON Canvas and Ben\u2019s Five Star Plugin"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-07-11
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/07/11/the-universal-json-canvas-and-bens-five-star-plugin/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# The Universal JSON Canvas and Ben’s Five Star Plugin

## Full text

I’ve borrowed Jon Udell’s term (“universal canvas”) for talking about SFW. In this video I talk about a plugin my brother Ben wrote for SFW earlier this week, and try to show what that means in semi-mechanical terms. 

One of the things I think it starts to show is how much of a construction kit SFW is. As Jon Udell noted when discussing the concept of the universal canvas ([in 2006](<http://www.infoworld.com/d/developer-world/we-need-universal-canvas-doesnt-suck-130>)!!), most of days are spent in a world _semi-structured data_ , yet most of the products we have access to either have no affordances for structured data at all, or are engineered to a level of precision appropriate to accounting systems. 

Over-engineering data collection is not just a waste of resources. It’s a dangerous practice where data is concerned Most times we start collecting data or sharing it, we’re not even really certain what we want to collect — yet modern practice forces us to design tables and subroutines before we collect *anything*. How the heck can [lead users](<http://en.wikipedia.org/wiki/Lead_user>) move things forward in such an environment? 

In practice, of course, no one moves forward at all. Most information that could help us is never logged anywhere, or it is logged in inaccessible, unparseable formats such as Word XML. We it comes to data, we have access to pea-shooters and inter-continental missiles, and little in-between.

A better approach is to create semi-structured data environments that rely more on conventions and culturally adopted techniques to add meaning to data. The data won’t be perfect, but because convention is more fluid than backend schemas, practice can evolve. Despite what a database admin will tell you, the biggest problem we face is not lack of data consistency. The biggest problem we face is the amount of information captured in no way at all. Using flexible JSON documents with front-end plugins starts to address that issue — and we know from history it’s a lot easier to clean up data we have retrospectively than capture data after the fact. 

In the example I show here — how would we know that the fivestar plug-in is showing your overall movie rating, and not, for instance, the rough quality of cinematography in the film? Convention. We agree that the first rating is always your overall rating. We agree that unseen films should be rated as “0”. 

As that convention solidifies, it gets encoded in a template. Now the template generates these objects with template-determined IDs. So now we don’t need to look for the first “fivestar” to get the rating — we look for object ‘bd3b3ea18244c038’, which is what the template called that top fivestar interface. We walk through the sitemaps in the neighborhood and find all pages named “Pulp Fiction” and average their values, exclusive of the zeros we decided would mean “not rated”.

Is this more laborious than a join? More error-prone than a SQL Stored Procedure? Well, yeah. You’re never going to get a scientific level of precision from this. 

But you don’t need it. If your process to find the best movies misses a film because you filled it out pre-template and it didn’t have the right object ID you will still receive more films in your search results than if you had entered no films at all. Those are the problems we tend to have in life and work, and it’s time for a process and software approach that addresses them.
