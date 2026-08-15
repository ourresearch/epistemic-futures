---
title: "NHIN Direct: Open Healthcare Records and Government as a Platform"
person: tim-oreilly
section: by
type: blog-post
year: 2010
date: 2010-03-11
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/2010/03/nhin-direct-open-healthcare-an.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# NHIN Direct: Open Healthcare Records and Government as a Platform

## Full text

In my advocacy around [Government 2.0](http://gov2events.com), I've been focused on the idea that [government should act like a platform provider rather than a complete solution provider](http://opengovernment.labs.oreilly.com/). That is, government should lay down rules of the road, create core functionality that others can build on, and then let the private sector compete to flesh out the offerings. 

[](http://www.gov2expo.com) You'd never think it from the right-wing media hysteria around the administration's health care initiatives, but some of the best thinking about minimal government intervention is happening right now in healthcare. I met yesterday morning with [Dr. David Blumenthal](http://healthit.hhs.gov/blog/onc/), the National Coordinator for healthcare policy, and I was struck by how he is focused on the idea of the least possible government intervention in the market. "We have to do as little as we have to do in order to have a strong probability to succeed," he told me. 

You might ask, "What is it that you have to do?" That is laid out in the 2009 Stimulus bill. Among many other things, the Stimulus allocates a large pot of money (some $20 billion) in direct payments to hospitals, medical practices, and other health care delivery organizations if they implement ["meaningful use"](http://www.cms.hhs.gov/apps/media/press/factsheet.asp?Counter=3564) of electronic health records. The idea is to jumpstart the adoption of electronic medical records, which have been demonstrated to have a big impact on lowering cost and improving patient care. (Here's a [Markle Foundation report (pdf)](http://www.markle.org/downloadable_assets/20090430_meaningful_use.pdf) that gives more detail on Meaningful Use.) No specific systems are mandated to achieve that meaningful use; that is left for the market to supply. 

There is also substantial funding for Blumenthal's office, the Office of the National Coordinator, or ONC. (This office was created by the Bush administration, but didn't receive substantial funding prior to the Recovery Act.) But rather than building a massive, centralized system for electronic health records, ONC's goal is to define the rules of the road for interchange of patient records. In internet-style, the expectation is that common protocols and file formats will allow vendors to compete on a level playing field to build the actual applications. But they aren't just writing paper standards; they are creating building blocks that actually implement those standards. (The internet analogy would be software like Bind, which implements the DNS protocol, and the root domain name servers, which for many years were funded by the US government.) 

I was swept from my meeting with Dr. Blumenthal into a planning meeting for [NHIN Direct](http://nhindirect.org/), an open system for interchange of patient records between physicians (and ultimately patients themselves), where I heard much the same message, which was [summarized so eloquently](http://geekdoctor.blogspot.com/2010/03/introducing-nhin-direct.html) by [Dr. John Halamka](http://twitter.com/jhalamka) on his blog yesterday morning: 

> The NHIN Direct effort philosophy is expressed in design rules 
> 
> The golden standards rule of "rough consensus, working code" will be applied to this effort. 
> 
> Discuss disagreements in terms of goals and outcomes, not in terms of specific technical implementations. 
> 
> The NHIN Direct project will adhere to the following design principles agreed to by the HIT Standards Committee from the feedback provided to the Implementation Workgroup 
> 
> Keep it simple; think big, but start small; recommend standards as minimal as possible to support the business goal and then build as you go. 
> 
> Don’t let “perfect” be the enemy of “good enough”; go for the 80% that everyone can agree on; get everyone to send the basics (medications, problem list, allergies, labs) before focusing on the more obscure. 
> 
> Keep the implementation cost as low as possible; eliminate any royalties or other expenses associated with the use of standards. 
> 
> Design for the little guy so that all participants can adopt the standard and not just the best resourced. 
> 
> Do not try to create a one size fits all standard, it will be too heavy for the simple use cases. 
> 
> Separate content standards from transmission standards; i.e., if CCD is the html, what is the https? 
> 
> Create publicly available controlled vocabularies & code sets that are easily accessible / downloadable 
> 
> Leverage the web for transport whenever possible to decrease complexity & the implementers’ learning curve (“health internet”). 
> 
> Create Implementation Guides that are human readable, have working examples, and include testing tools. 

That should be music to the ears of any Internet developer, and should raise some serious doubts in the minds of any of you who have been swallowing the idea that somehow the Federal government wants to take over the medical system. There's some fresh thinking going on here, influenced by the best practices of open standards and rapid internet development, about how government can use interoperability to stimulate market activity to improve the medical system. 

NHIN Direct is only one of several projects that implement core functionality for interchange of electronic medical records. It is focused on simple use cases like exchange of medical records from a primary care physician to a specialist, or from one primary care physician to another, or from a physician to his patient. Other projects, like [HHS Connect](http://www.hhs.gov/news/press/2009pres/04/20090406a.html) are focused on the much more complex problem of records interchange between large health providers such as the VA, the Department of Defense, and large hospital systems. This project demonstrates how interoperability can be used to reduce development costs by cooperation between agencies with overlapping missions. 

This is health reform in the trenches of technology, where there are enormous opportunities for cost savings and better care. There's really good thinking going on here. So don't believe what you read in the paper. 

Fellow Radar blogger [Brian Ahier](http://radar.oreilly.com/bahier/), who works as a health IT evangelist for a rural Oregon health cooperative, told me the following story last night, which illustrates how he counters the misunderstandings about electronic health records that he encounters in his daily work. 

> Trying to help rural providers in adoption of electronic health records has its own unique challenges. Many of these physicians practice in what is commonly called "fly over country." And the residents in these rural communities tend to lean conservative. Bringing up the subject of digitizing his office, the country doctor says, "I don't want all of my patients' information put into this government database. I'm not going to be part of the government takeover of our health system." I try to explain that the information is not stored in some giant government database. He certainly doesn't want to hear about a federated architecture for health information exchange or standards and protocols for secure messaging. But when asked how clinical information gets to the emergency room for a doctor who is treating one of his patients, he says, "My nurse sends it by fax." 
> 
> So when I start to explain that his office can still keep the entire patient record, but sharing that data can be more securely and efficiently handled digitally, a light bulb seems to go on. When we talk about patient online access to their records and I draw the analogy to accessing your bank account over the Internet, we begin to turn a corner. We can leave the larger debate of health reform behind. It isn't long before he starts to agree that it might just be possible for health IT to improve quality, patient safety and clinical outcomes while eventually lowering costs. Overcoming some of the fears based on false assumptions is the first battle, and now we can start to look at some of the serious technical barriers ahead in this journey.
