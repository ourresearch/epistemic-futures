---
title: "The Final Crontab: an introduction to crontabber"
person: selena-deckelmann
section: by
type: blog-post
year: 2014
date: 2014-05-06
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2014/05/06/the-final-crontab-an-introduction-to-crontabber/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# The Final Crontab: an introduction to crontabber

## Full text

I gave a talk at [Monitorama](http://monitorama.com) today about [crontabber](http://github.com/mozilla/crontabber). ([slides](https://speakerdeck.com/selenamarie/the-final-crontab))

My coworker tells me that I left out the part of “why you should care” about crontabber from my first few slides. So here’s a list:

- Retries jobs on failure automatically

- Dependency-aware, and won’t execute child jobs that depend on parents that have failed

- Nagios integration including support for WARNINGs and CRITICALs, and configurable escalation from WARNING to CRITICAL (e.g. 3 WARNINGS == CRITICAL). 

Those three are probably the top features sysadmins who are not happy with how cron is managing jobs wish they had.

Crontabber needs at least Python 2.6, Postgres 9.2, is FOSS and being used in production. We’ve used a version of the code since February 2013, and currently have the python module version you can install with pip install crontabber is currently running in our stage environment.

Let us know what you think!
