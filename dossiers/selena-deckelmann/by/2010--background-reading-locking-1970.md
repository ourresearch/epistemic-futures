---
title: "Background reading: Locking (1970)"
person: selena-deckelmann
section: by
type: blog-post
year: 2010
date: 2010-09-03
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2010/09/03/background-reading-locking-1970/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Background reading: Locking (1970)

## Full text

I’ve been reading some old papers about locking and MVCC in preparation for writing about MVCC in PostgreSQL, and for giving a talk at [CouchCamp](http://www.couch.io/couchcamp) next week!

I just finished “[Locking](http://icanhaz.com/locking)“, by Jim Gray. He discusses semaphores, and makes the argument for implementing a locking scheduler to handle errors and deadlocks (which he calls interlocks, or a “deadly embrace” – a term I’m sad we’ve stopped using). 

An example from the start of the paper illustrates the power of MVCC: 

> The classic example is an accounting file. Processes reading the file may share it

concurrently. However, a process requesting write access to the file blocks until all processes currently reading have released the file.

A lovely thing about Postgres’ MVCC is that readers (SELECT) don’t require this type of lock, and most writers don’t block readers. For SELECT, the only statements that will block it are those that make changes to tables which move all rows physically around (VACUUM FULL, CLUSTER, REINDEX, TRUNCATE), or make changes to table structure (ALTER TABLE, DROP TABLE).

Have a look at the [explicit locking docs](http://www.postgresql.org/docs/current/static/explicit-locking.html) for more detail on the lock modes automatically used by PostgreSQL.
