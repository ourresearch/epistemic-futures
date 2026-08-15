---
title: "Mashup-ageddon is a Massive Blackboard Fail"
person: mike-caulfield
section: by
type: blog-post
year: 2015
date: 2015-06-09
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2015/06/09/mashup-ageddon-is-a-massive-blackboard-fail/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Mashup-ageddon is a Massive Blackboard Fail

## Full text

I used to think the main problem with Blackboard was that it applied an enterprise solution to a consumer software problem. I increasingly think the main problem is that it’s just  _lousy_ enterprise software.

Case in point: today we learned that _all_ of the YouTube videos that all of our professors had embedded in Blackboard using their embedded video function (bizarrely named the “mashup” function) don’t work anymore. Every student in every Bb class is clicking on the YouTube videos their professor has embedded using “Mashups” and seeing this message as they frantically try to watch them before class:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/mashup.png>)

_“ We are unable to display the mashup content. This happens if the system detects an invalid URL. Remove the mashup item and try again to resolve the issue.”_

Right off the bat, there are some problems with even _the error message_. After the student stops wondering what the Intro to Genetics class video has to do with “mashups” (a musical form popularized by the hit show Glee) they have two other messages to decipher. First they are told the the system has detected and invalid URL, which is useless information to them. Then they are told to remove the mashup item, which they actually can’t do, and even if they could it doesn’t get them what they need, which is to see the video.

I want to repeat — this is happening right now in every class _across the world_ with every video that any instructor embedded using the Blackboard YouTube tool. Professors are spending thousands of person-hours fielding emails from students unable to play videos or to understand the error message trying to produces.

Now, you might ask next, why is this happening at all? Blackboard will likely tell you “It’s YouTube! They pulled the API we used! We’re scrambling to react!”

So is that true? Yes, but not in the way you think. The API that was pulled has been deprecated for a little over a year.

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/api.png>)

At that time Google notified people support for the YouTube v2.0 API would be pulled on April 20, 2015, and that developers should migrate to the 3.0 spec.

So what happened on April 20, 2015? Well, YouTube published a deprecation plan, saying hey — we were serious. We’re going to start shutting down the API piece by piece, and your stuff will stop working around the end of May:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/06/api2.png>)

So what did Blackboard do in the 14 months since they learned that the API would break? Apparently nothing. Nada. Zilch.

They didn’t even fix the ERROR message. Let that sink in. They couldn’t be bothered to update the error message. That message could give you a link to the video you could click, saving the student a crisis and thousands of professors a flood of emails about broken videos. But they don’t care enough to do this.

This is really par for the course with Blackboard. It really is.

Is there any other industry where this would be tolerated?

Anyway, if you hear that Mashup-ageddon was “caused by a YouTube change”, politely decline to accept that answer. And if you’re considering purchasing Blackboard, you might ask them for an explanation of how this sort of thing continues to happen.

For my encore, I would love to detail their inability to keep our hosted Blackboard server up, even during finals week, with a server failure issue that they have not been able to fix despite working on it for over four months. But I have to go manually re-embed several hundred YouTube videos that are not working for our students. So I’ll have to write that post next week. Stay tuned!
