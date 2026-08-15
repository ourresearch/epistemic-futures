---
title: "A Web service for random GitHub usernames, via Google BigQuery, R, and CouchDB"
person: jason-priem
section: by
type: blog-post
year: 2012
date: 2012-07
venue: "jasonpriem.org (personal blog)"
authors: "Jason Priem"
source_url: https://web.archive.org/web/20141012235459/http://jasonpriem.org/2012/07/a-web-service-for-random-github-usernames-via-google-bigquery-r-and-couchdb/
retrieved: 2026-08-13
content: full-text
notes: "Personal blog, defunct; retrieved from the Internet Archive Wayback Machine. Original URL: http://jasonpriem.org/2012/07/a-web-service-for-random-github-usernames-via-google-bigquery-r-and-couchdb/"
---

# A Web service for random GitHub usernames, via Google BigQuery, R, and CouchDB

## Full text

In the course of building some much-needed testing infrastructure for [total-impact](http://total-impact.org), I found I needed a source of random GitHub usernames. A [forum post](https://groups.google.com/forum/?fromgroups#!topic/scraperwiki/lv__20X4hHQ) directed me to the very cool [GitHub Archive](https://github.com/igrigorik/githubarchive.org/blob/master/bigquery/schema.js) project, which pushes its extensive collection of GitHub data to [Google BigQuery](http://https://bigquery.cloud.google.com/ "https://bigquery.cloud.google.com/"). BigQuery in turn lets you write SQL-style queries on ginormous datasets like this one. After a quick BigQuery signup and look at the [schema](https://github.com/igrigorik/githubarchive.org/blob/master/bigquery/schema.js), I had  a list of  One Million Usernames. Sweet.

Unfortunately, BigQuery isn’t really setup to do lots of fast lookups on the same query (update: [Or Is It?](http://jasonpriem.org/2012/07/a-web-service-for-random-github-usernames-via-google-bigquery-r-and-couchdb/#comment-26974)), which is what I needed. It does, though, let you download CSV, which I did. From, there the list of names went into R ([here’s the code](https://github.com/total-impact/total-impact-core/blob/18b33449cf2084afb7327b5e3d81f7936e146a75/extras/github_ids_to_couchdb.R)), where I got rid of  duplicates and (with the help of [this great post](http://digitheadslabnotebook.blogspot.com/2010/10/couchdb-and-r.html)) uploaded the usernames to [Cloudant](http://https://cloudant.com/), a cloud-based CouchDB service. Since CouchDB communicates entirely over HTTP, this essentially gives the dataset a [RESTful API](http://en.wikipedia.org/wiki/Representational_state_transfer) for free.

Once the data was in Couch, writing [a thin Python wrapper](https://github.com/total-impact/total-impact-core/blob/18b33449cf2084afb7327b5e3d81f7936e146a75/totalimpact/fakes.py#L323) around the HTTP call was a piece of cake; essentially, all you have to do is query Couch’s `all_docs` endpoint looking for the document id nearest to a randomly-generated string. All in all, a lovely afternoon’s work and a great example of how open APIs, cloud-based services, and open-source software can make slinging big data easy enough that even a grad student can do it :)
