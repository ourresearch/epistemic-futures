---
title: "I Have a Research Question About MOOCs That Your Elite Institution Can Answer in Under an Hour"
person: mike-caulfield
section: by
type: blog-post
year: 2013
date: 2013-04-24
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2013/04/24/i-have-a-research-question-about-moocs-that-your-elite-institution-can-answer-in-under-an-hour/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# I Have a Research Question About MOOCs That Your Elite Institution Can Answer in Under an Hour

## Full text

I’ve been really curious about how much (and in what way) xMOOC students use forums. And I can’t find any good data on it. Not even a “per capita visits to forum” number.

This is pretty suboptimal for the field, since one of the main advantages of MOOCs often presented is the conversation they allow between students. Now, there is a question of whether these online conversations have any learning impact. But we haven’t even got to the basic question of whether the median xMOOC user uses the forums at all, outside a few brief scans. That seems insane to me.

Fortunately, if you work at an institution that offers a Coursera MOOC, you can answer that question pretty easily. What’s more, you can be the first to do it.

Here’s the data export procedure and SQL schema (thank you for the link, **[George Veletsianos](<https://twitter.com/veletsianos>)!)**:

[coursera_data_export_policies_and_sql_schema.17dec2012](<http://mikecaulfield.wordpress.com/wp-content/uploads/2013/04/coursera_data_export_policies_and_sql_schema-17dec2012.pdf>)

There are some unique challenges, due to the anonymization of user IDs on a per session basis. But post data is not anonymized, so you could get a metric like median posts per user, or percent of users who post. And on the reviewing the forums side, perhaps the percent of sessions involving a forum visit?

I’m not sure how hard it is to piece the database together from the download. But a competent SQL coder could use the document and database to get at these sorts of questions in a matter of minutes once the database is up and running and the document read. These are very simple sorts of SQL statements.

I don’t think these will answer any research questions definitively, but they will help us refine the questions that we ask in very helpful ways. And that, in turn, will help us improve education. I’ve seen a lot of institutions say they are doing Coursera courses as a charitable effort, to help improve education for all. Data is essential to that effort, so now is the time to see whether the rhetoric reflects reality.

Show me the data!
