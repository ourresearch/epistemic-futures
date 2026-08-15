---
title: "Wrap-up meetings provide feedback that teams need to improve"
person: selena-deckelmann
section: by
type: blog-post
year: 2011
date: 2011-02-23
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2011/02/23/wrap-up-meetings-provide-feedback-that-teams-need-to-improve/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Wrap-up meetings provide feedback that teams need to improve

## Full text

(originally posted on [tech emma](http://tech.myemma.com/wrapup-meetings-feedback-teams-improve/))

Nobody likes admit­ting mis­takes. [Except this guy](http://www.techdirt.com/articles/20070515/021134.shtml#c230).

Getting peo­ple to go to a post-mortem meet­ing is easy. Getting peo­ple to par­tic­i­pate with­out a sense of impend­ing doom is hard. Most peo­ple don’t want to be there. They show up ready to fight or make excuses, with a pit in their stom­ach as they wait to talk about what went wrong.

So, how do you fix that pit-in-the-stomach feeling? We’ve worked on this a bit at Emma, and here’s my formula:

- Set high-level, achiev­able goals and have meet­ings even when things go right.

- Focus on how every­one will work together to make things bet­ter in the future, not what went wrong.

- Get every­one to participate.

- Share with the whole com­pany what the group learned.

Now might be a good time to tell you that I wrote about some changes to our inter­nal down­time process last week ([read that post here](http://tech.myemma.com/better-planning-for-maintenance-window/)); today I’d like to fol­low up with details about our ver­sion of a post-mortem meeting.

### Set high-level, achiev­able goals and meet about success

A main­te­nance win­dow here is con­sid­ered a suc­cess when we make our changes, recover from any fail­ures with­out impact­ing pro­duc­tion and end on time.

As a group, we decided what’s okay to include in the win­dow, and stripped out some riskier changes. Those included tasks that were hard to esti­mate time for, or ones that would push against the amount of time we allo­cated for test­ing. At this point, going into each win­dow, we have a clear list of tasks, and we can assess suc­cess or fail­ure of each task after the change.

In that first win­dow in January, we com­pleted the following:

- Upgraded our PostgreSQL databases

- Recovered 5% of the disk space on our largest data­base cluster

- Fixed a long-standing main­te­nance issue with par­ent tables on our largest database

We decided to have a meet­ing after the win­dow — regard­less of whether the change suc­ceeded or failed.

### Talk about what went well (aka Why I decided to call these meet­ings “wrap-ups”)

I always hated call­ing these dis­cus­sions “post-mortems.” I get why tech peo­ple want to com­pare the process to a med­ical pro­ce­dure, and [I love a good zom­bie movie](http://www.imdb.com/title/tt0451954/), but it sets the wrong tone. I decided to call them “wrap-ups,” to help make it clear that we’re there to reflect on the project, not find blame.

And here’s what we try to do in each wrap-up:

- Spend time talk­ing about how things went well, and why

- Focus on how to improve future projects

- Distill what we learned

Documenting how the team man­ages main­te­nance win­dows makes the great work peo­ple were already doing vis­i­ble. We also open up the meet­ings so non-IT folks at Emma can con­tribute and make them better.

### Conduct the dis­cus­sion for 100% participation

After a main­te­nance win­dow, we com­mu­ni­cate the out­come to the rest of our col­leagues. Then, I sched­ule a 30-minute meet­ing with a sim­ple agenda. We go over what hap­pened dur­ing the main­te­nance win­dow to:

- Discuss what went right

- Discuss what went wrong

- And deter­mine what we could do to make things bet­ter next time

In our most recent wrap-up, seven peo­ple attended, and I requested at least one com­ment from each per­son on the agenda bul­let points.

### What we learned

In just 30 min­utes, we came up with plenty of things that the group felt good about doing well and a set of clear changes to make in the future.

Here are some of the things peo­ple liked:

- Creating a cus­tom error mes­sage for the main­te­nance window

- Having a phone bridge and using Campfire through­out the win­dow to communicate

- Using a wiki page to orga­nize tasks and each task’s owner dur­ing the main­te­nance window

- Using the change win­dow to test out new Linux ser­vice scripts for the sys­tem admin­is­tra­tion team

This was our first main­te­nance win­dow where we used both [Campfire](http://campfirenow.com/) and a phone bridge at the same time for the whole team. We chose Campfire because any­one new who joined could eas­ily see what con­ver­sa­tion had already taken place. We used the phone bridge to make it sim­ple to type com­mands and stay in touch at the same time.

In the past, we’d used email and [RT tick­ets](bestpractical.com/rt/) to doc­u­ment what was hap­pen­ing in the main­te­nance win­dow. Everyone loved hav­ing a wiki page to ref­er­ence and update instead. The wiki just had a bet­ter UI than email or a ticket, and pro­vided a bet­ter experience.

Finally, the sys­tems admin­is­tra­tion team used the win­dow to test out new ser­vice start/stop scripts for a series of cus­tom appli­ca­tions. This is the type of thing that can go un-exercised when you rarely have down­times or main­te­nance win­dows. The team was smart to seize the opportunity!

We also thought a few things didn’t go so well:

- We didn’t give our cus­tomers enough of a heads-up.

- Steps for the changes should have num­bers, not just times asso­ci­ated with them.

- Our test­ing took quite a while because the change affected all the data­bases at the same time, and tests only looked at one data­base at a time.

There may have been other things that peo­ple thought we could have done bet­ter, but we kept the list short and action­able. We’ll change the process slightly in the future to inform cus­tomers bet­ter, add num­bers to all the steps and test data­bases concurrently.

Beyond this cur­rent win­dow, I also asked every­one to imag­ine how we might do things dif­fer­ently or bet­ter dur­ing other downtimes.

A few ideas included:

- Trying out video con­fer­enc­ing dur­ing the main­te­nance, like [Tokbox,](http://www.tokbox.com/) to help make com­mu­ni­ca­tion even better

- Pulling in more helpers for test­ing — for train­ing, and mak­ing the work­load lighter for the QA team

- Using Salesforce to com­mu­ni­cate upcom­ing changes internally

My favorite sug­ges­tion, though, was:

- Playing “[Point of no return](http://www.youtube.com/watch?v=ksHsh4r8tJA)” when we know every­thing worked

Feel free to com­ment below — I’d love to hear how you man­age your meet­ings, and what you’ve learned.
