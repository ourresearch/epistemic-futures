---
title: "My Postgres Performance Checklist"
person: selena-deckelmann
section: by
type: blog-post
year: 2011
date: 2011-09-22
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2011/09/22/my-postgres-performance-checklist/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# My Postgres Performance Checklist

## Full text

I am asked fairly frequently to give a health assessment of Postgres databases. Below is the process I’ve used and continue to refine. 

The list isn’t exhaustive, but it covers the main issues a DBA needs to address.

- **Run boxinfo.pl on a system**

Fetch the script from [http://bucardo.org/wiki/Boxinfo](http://bucardo.org/wiki/Boxinfo). Run as the postgres user on the system (or a user that has access to the postgres config).

- **Check network.**

What is the network configuration of the system? What is the network topology between database and application servers? Any errors?

- **Check hardware.**

How many disks? What is the RAID level? What is the SLA for disk replacement? How many spares? What is the SLA for providing data to the application? Can we meet that with the hardware we have?

- **Check operating system.**

IO scheduler set to ‘noop’ or ‘deadline’, swappiness set to 0 (http://www.pythian.com/news/1913/what-exactly-is-swappiness/)

- **Check filesystems.**

Which filesystem is being used? What parameters are used with the filesystem? Typical things: noatime, ‘tune2fs -m 0 /dev/sdXY‘ (get rid of root reserved space on database partition), readahead – set to at least 1MB, 8MB might be better.

- **Check partitions.**

What are the partition sizes? Are the /, pg_xlog and pgdata directories separated? Are they of sufficient size for production, SLAs, error management, backups?

- **Check Postgres.**

What is the read/write mix of the application? What is our available memory? What is the anticipated transpactions per second? Where are stats being written (tmpfs)?

- **Check connection pooler.**

Which connection pooler is being used? Which system is it running on? Where will clients connect from? Which connection style (single statement, single transaction, multi-transaction)?

- **Backups, disaster recovery, HA**

Big issues. Must be tailored to each situation.

What’s your checklist for analyzing a system?
