---
title: "Security and maintenance release for PostgreSQL: versions 9.1.3, 9.0.7, 8.4.11 and 8.3.18"
person: selena-deckelmann
section: by
type: blog-post
year: 2012
date: 2012-02-27
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2012/02/27/security-and-maintenance-release-for-postgresql-versions-9-1-3-9-0-7-8-4-11-and-8-3-18/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Security and maintenance release for PostgreSQL: versions 9.1.3, 9.0.7, 8.4.11 and 8.3.18

## Full text

Today, PostgreSQL Global Development Group [released new versions](http://www.postgresql.org/about/news/1377/) of all active branches. This includes three security bugfixes, two of which are pretty obscure and one that fixes a possible security issue with restoring un-sanitized output from pg_dump. Details about the security issues are included in the [release announcement](http://www.postgresql.org/about/news/1377/).

Some other bug and performance fixes in this minor release include: 

- Fix btree index corruption from insertions concurrent with vacuuming

- Avoid crashing when we have problems deleting table files post-commit

- Fix recently-introduced memory leak in processing of inet/cidr

- Fix postmaster to attempt restart after a hot-standby crash

[Upgrade](http://www.postgresql.org/download/) as soon as you can!
