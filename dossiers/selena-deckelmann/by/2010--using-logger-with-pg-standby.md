---
title: "Using logger with pg_standby"
person: selena-deckelmann
section: by
type: blog-post
year: 2010
date: 2010-08-29
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2010/08/29/using-logger-with-pg_standby/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Using logger with pg_standby

## Full text

Piping logs to syslog is pretty useful for automating log rotation and forwarding lots of different logs to a central log server. 

To that end, the command-line utility ‘logger’ is nice for piping output from utilities like pg_standby without having to add syslogging code to the utility itself. Another thing is that logger comes by default with modern packages of syslog.

Here’s an easy way to implement this: 

restore_command = 'pg_standby -d -s 2 -t /pgdata/trigger /shared/wal_archive/ %f %p %r 2>&1 | logger -p local3.info -t pgstandby'
