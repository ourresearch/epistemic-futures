---
title: "Database War Stories #6:  O'Reilly Research"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-05-02
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/05/database_war_stories_6_oreilly.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Database War Stories #6:  O'Reilly Research

## Full text

In building our Research data mart, which includes data on [book sales trends](http://radar.oreilly.com/archives/2006/04/state_of_the_computer_book_mar.html), [job postings](http://radar.oreilly.com/archives/2006/05/mysql_and_the_database_job_mar.html)), blog postings, and other data sources, Roger Magoulas has had to deal with a lot of very messy textual data, transforming it into something with enough structure to put it into a database. In this entry, he describes some of the problems, solutions, and the skills that are needed for dealing with unstructured data.

Roger wrote:

  * When integrating our research data mart with a legacy sales transaction system, I was asked to help tune a data mart with appx 3mm rows that joined to a few large dimensions; an aggregate query was not completing. I was able to tune the query down to completing in under 2 minutes by addressing the following common database problems: 
    * There were orphans in the data, i.e, there were rows with quantitative information that had no parent dimension data. For example an invoice might not have any customer data. To capture all the data, the query included outer joins that seemed to slow down processing. The fix: add 'unknown' parent rows and map all orphans to these rows. This step led the query completing in 7 minutes. The new 'unknown' parents also made it clear to anyone looking at the query results that data was missing so they could address correcting the data 

    * The data went back many years. I partitioned the data based on expected query requests into tranches (time based partitions) based on data in the last quarter, the year up to the last quarter and then by year before that. The query now completes in under 2 minutes. I wrote automated ETL code that updates the partitions every month to help keep performance consistent.

The lessons:  

    * the need to pay attention to how data is organized to address performance issues, to make the data understandable, to make queries reliable (i.e., getting consistent results), and to identify data quality issues.  

    * when you have a lot of data, partitioning, usually by time, can make the data usable. Be thoughtful about your partitions; you may find its best to make asymmetrical partitions that reflect how users most access the data. Also, if you don't write automated scripts to maintain your partitions, performance can deteriorate over time.

  * Finding usable information in large, unstructured data sets. This is a relatively new problem for business. Not too long ago, data warehouses tended to store structured operational data or clickstreams from web activity, with good keys and controlled data entry. Nowadays we're building data warehouses w/ jobs, blogs and other unstructured data that requires different techniques. To look for trends in unstructured data we need to use techniques similar to those used for effective search. Cleverness is a plus. 

For example, to determine if a job is technical, we look for our least two technical terms from a list of technical terms. Because technical terms can be a piece of a longer word, care must be taken when handling word boundaries. Technical terms may appear as part of e-mail addresses, so e-mail addresses are identified and skipped.

In our study to compare Gnome and KDE, we had to filter out jobs that referenced lawn gnomes and those placed by a recruiting firm with an e-mail domain of kde.com (e.g., name@kde.com). Some jobs mentioned both desktops, using the contraction gnome/kde. Manual inspection and iteration was required to create a reliable list of jobs for each Linux desktop.

Deduping large, mixed data sets like the job data can be difficult. One way to handle dupes is to use a single data set [as the master]; we often use Craigslist for the jobs data, where dupes can be more easily identified and are less likely to exist.

  * Anecdotally, in the blog data, we are finding that English technology terms are available in foreign language blogs. We're not sure yet how to handle these in our search and how often it occurs. However, it would be a nice turn of events for us if we can include int'l data and make inferences about geographic technology preferences 

It's a UTF-8 (or maybe UTF-16) world - a skill many are going to need to learn to handle increasingly int'l sources of data.

  * Regex and NLP are skills that are helpful and complementary for analyzing unstructured data. Need to learn when to apply tools appropriately. 

  * Sampling and probability are important tools for large data sets - many users don't understand (I wonder if the new [Chances Are](http://www.amazon.com/gp/product/0670034878) book will help lay people understand probability better. 

  * MySQL databases configured for transactions will perform slowly if used for business intelligence (and vice versa). I moved some queries from a transaction system to a data mart system and saw 30-50% faster performance. For a mart you want to use big buffers, big pages and process as much data as possible for each step (handle batches). Transaction systems are typically optimized to handle many small, unrelated data bits (handle one thing well at a time). My experience is that it's difficult to integrate transaction and analysis oriented tasks on the same box.

_**More entries in the database war stories series:[Second Life](http://radar.oreilly.com/archives/2006/04/web_20_and_databases_part_1_se.html), [Bloglines and Memeorandum](http://radar.oreilly.com/archives/2006/04/database_war_stories_2_bloglin.html), [Flickr](http://radar.oreilly.com/archives/2006/04/database_war_stories_3_flickr.html), [NASA World Wind](http://radar.oreilly.com/archives/2006/04/database_war_stories_4_nasa_wo.html), [Craigslist](http://radar.oreilly.com/archives/2006/04/database_war_stories_5_craigsl.html), [Google File System and BigTable](http://radar.oreilly.com/archives/2006/05/database_war_stories_7_google.html), [Findory and Amazon](http://radar.oreilly.com/archives/2006/05/database_war_stories_8_findory_1.html), [Brian Aker of MySQL Responds](http://radar.oreilly.com/archives/2006/05/brian_aker_of_mysql_responds.html)**_.
