---
title: "The LMS in Historical Perspective"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-09-16
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/09/16/the-lms-in-historical-perspective/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# The LMS in Historical Perspective

## Full text

Is it ironic that I’m posting on this topic partially to avoid the mundane process of setting up Blackboard trainings for a bit longer? Probably not.

In any case, Jared Stein [has a post up](<http://jaredstein.org/2014/09/i-fought-the-lms-my-first-10-years-with-learning-managment-systems/#comment-1774>) about the LMS and his personal perspective on why it turned out the way it did, and the crux of the narrative is that the LMS won out initially because frankly there was a bunch of stuff that the web was not making easy at the time. And the primary force for adoption of the LMS was not administration, but faculty, who really wanted management tools.

I’m too young on this side of higher education to confirm or deny that account as the ground truth, but it jives with my experience as well. My first encounter with Blackboard was on a educational simulation project we were looking to sell to Old Dominion University in 2000/ early 2001. Cognitive Arts wanted to sell a kickass (technical term) learning sim we had made to Old Dominion to run, something we had spent several millions of dollars developing, and which had had great results (I’m trying to remember if it was our macroecon product or our Java 101 product). Anyway, word came back from the sales team — they are interested, but they want it to run in Blackboard. Since I was usually the “Somebody figure out what X is” person on the team, it fell to me to figure out if we could integrate it.

I ultimately learned we could wrap our web hosted software in a frame (it was 2000, deal with it) and exchange some very rudimentary data with Bb. I think it might have just been a completion flag, and I forget how we hacked it.(Other places we had wrapped things as big AICC objects, but I’m not sure that was the method here). Ultimately the whole deal turned out to be a sales mirage, so I thanked sales for another ill-spent 65-hour week chasing after phantom commissions for them, and called it a day.

But here’s the thing. As I remember, it wasn’t an institutional rule that it had to fit into Bb. It was a faculty concern that they pushed up to us. Faculty thought our stuff was cool, but they didn’t want to be in two places. They wanted to manage it from Blackboard, and wanted it to be available to the students from Blackboard so that the course felt coherent rather than two seperate, unconnected bits.

My second exposure to the LMS was getting to know the guys who built Prometheus, which at the time was billed as the first “community source” LMS. (Actually, now that I think of it, it was my first LMS exposure, since I remember meeting them in Washington D.C. when Bill Clinton was still President).

I had co-built the enrollment and user managment functions in our Cognitive Arts’ home-brew LMS (let’s admit it, if you enroll users, its an LMS whether it’s a syndication hub or a simulation). And when I looked under the hood of Prometheus (which was written in ColdFusion, the same language as our product) I went right over to my boss and argued we port our stuff to Prometheus and ditch our home-brew. It was just elegant and extensible. It looked beautiful. It was ridiculously easy to write extensions to it.

Here was a platform that encouraged you to build on top of it. And a community that was truly engaged with the possibilities extending it.

Of course, Prometheus was eventually bought by Blackboard. If you’ve heard of Building Blocks in Blackboard, it’s basically a port of what Prometheus was doing with extensibility, but done in a way that makes it unattractive to end-users to build in it. So yay.

A number of years later I asked a person I knew who worked at Prometheus why Prometheus failed. Did Blackboard crush them?

His answer was interesting. No, it wasn’t Blackboard at all. It was the educational institutions. With the slow, resource-intensive and state-mandated RFP processes, the interminable faculty commitees, and the way that even after the deal was signed the institution would delay payment and implementation as long as possible (or suddenly throw it into an unanticipated ‘final review’) it was just not possible to grow a stable business. The process institutions followed was supposed to ensure equitable access to contracts, but what it did was made it impossible for any company not sitting on a pile of cash to stay in business. (I’m extrapolating a bit here, but not much).

So ironically, if you want to know what built the world of the One True LMS, look not at capitalism, but anti-corruption law, faculty governance, and state budgeting. Fun, huh? Counter to most of the rest of my world-view, but from what I’ve seen on the inside, entirely true.

When I got to Keene State in 2004, Blackboard was entrenched, but the stories I heard were really the same. There had been a faculty push to get something in place, and the Blackboard advocates had won. But what we started finding as 2004 rolled into 2005 and 2006 was that the external web was accelerating making all sorts of open connection possible, all sorts of reuse possible, and Blackboard was supporting none of it. They decided they had solved the LMS problem, once and for all, and started to look at more lucrative aspects of university business.

The standard joke about Blackboard by 2007 was that they were spending millions of dollars trying to get your university’s keycard production business (actually true) but couldn’t figure out a way for you to add a simple YouTube video without writing a javascript-based hack.

By 2008, when Blackboard announced, hey, we’re so Web 2.0, I was writing rather high-minded [screeds like this](<http://hapgood.us/2008/05/31/a-short-explanation-from-a-terminal-smasher/>):

> [W]hile Blackboard was busy trying to leverage their foothold in the University to get into the business of [dining hall management](<http://www.blackboard.com/docs/CS/Bb_Whitepaper_NTE.pdf>), [video surveillance](<http://www.blackboard.com/products/Commerce_Suite/Video_Surveillance>), and [door access control](<http://www.blackboard.com/clientcollateral/Bb_Transaction_System_Datasheet_Wireless%20Door%20Access.pdf>), this little thing called Web 2.0 happened. And suddenly the technology Blackboard had for learning began to look — well, old. Junky. Very 1999.
> 
> So while Bb spent their efforts trying to become the single sign-on point for your institution, professors, frustrated with the kludginess of the actual *learning* part of Bb’s suite, started looking elsewhere for solutions.
> 
> Their first discovery was that they could do everything they were doing in Blackboard for free, and much more easily.
> 
> But the second discovery was the kicker. These Web 2.0 tools they adopted encouraged them to share their stuff with the world, instead of locking it away in a password protected course. And suddenly, they got a taste of open education. And it didn’t stop there. The tools they adopted had a true web DNA, and played well with other tools in a loosely coupled mode. So suddenly, they got a taste of what it was like to build your own custom learning environment.

The tone is a bit overstated and obnoxious, but I stand by the 2008 analysis. Somewhere in the mid-aughts, the customer of Blackboard moved from being the faculty member (who they had aggressively courted initially) to the administration. And, as Scott Leslie points out, [incumbency’s a bitch](<http://jaredstein.org/2014/09/i-fought-the-lms-my-first-10-years-with-learning-managment-systems/#comment-1774>). They became a barrier to serious, important movements — the social web, open education. By the time I was working for the OpenCourseWare Consortium it had passed ridiculousness into something akin to a crime against humanity. Again and again I’d talk to people who wanted to open up their instructional materials to the world only to learn that the company they had paid a quarter of a million dollars to host those materials had no way to let them do that.

[Side note: Insert argument here about whether all classes really need “educational materials” which is about as intelligent as arguing about whether all classes need students to buy novels.]

I’m interested where Jared takes the history from there. But what he has described so far fits my recollection. We fought the LMS, the LMS won, and then the LMS just sat there for a number of years asking us if we would like to upgrade to the alumni fundraising product. What happened next was… well, back to setting up Blackboard training [sigh]. But I’ll reply with more when Part II of Jared’s series comes out.
