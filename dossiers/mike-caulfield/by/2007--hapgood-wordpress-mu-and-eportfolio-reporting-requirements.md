---
title: "WordPress MU and eportfolio reporting requirements"
person: mike-caulfield
section: by
type: blog-post
year: 2007
date: 2007-06-21
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2007/06/21/wordpress-mu-and-eportfolio-reporting-requirements/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# WordPress MU and eportfolio reporting requirements

## Full text

I had the good luck this week to stumble into a very helpful blogswarm. And since it’s best to make use of [their expertise](<http://bavatuesdays.com/the-motley-management-system/>) while they are still checking back here, let’s cut to the chase.

Here is the new thought, re: eportfolios and other WP projects needing data aggregation.

Append an optional process at the end of WordPress MU setup that pre-populates the category table with canonical terms.

So, for instance, the table could be pre-filled with specific performance indicators appropriate to educational eportfolios, organized around a standardized phrase, such as “Demonstration of Classroom Management Skills (NC 2.1.3)”. You upload the artifact and you or someone bigger than you tags it.

Now here’s the neat part. Since we have faith these terms are the same across MU instances, reports are simply a matter of writingÂ code that cycles through all the MU user tables and finds posts that are tagged with that term. Want a report of all users who have not met requirement _NC 2.1.3_? Easy.

Caveat: the people here with an intimate knowledge NCATE are still drawing up what the reporting requirements will look like. But then, there’s very little one can’t do with tagging and SQL. So I’m not worried yet.

So question…. does this make sense? Is anyone else using WP tagging in this way? Does anyone have NCATE reporting experience, and what can you tell me?

(Bill,Â I will eventually look into yourÂ [neat hack](<http://bavatuesdays.com/the-motley-management-system/#comment-13991>) in Drupal as well…]
