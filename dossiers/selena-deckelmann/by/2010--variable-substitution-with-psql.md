---
title: "Variable substitution with psql"
person: selena-deckelmann
section: by
type: blog-post
year: 2010
date: 2010-08-30
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2010/08/30/variable-substitution-with-psql/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Variable substitution with psql

## Full text

**Updated:** Thanks @johto for s/:bar/:foo/. 🙂

A coworker asked about variable substitution with psql using \set, and so I looked into it a bit further.

You definitely can do things like this:

16:55 sdeckelmann@[local]:5432|postgres=> \set test 'select * from :foo limit 10;'

16:56 sdeckelmann@[local]:5432|postgres=> \set foo 'test'

16:56 sdeckelmann@[local]:5432|postgres=> :test

myint

-------

 1

 2

 3

 4

 5

 6

 7

 8

 9

 10

(10 rows)

But, what about something like this:

=> \set test 'select * from :var limit 10;'

=> :test mytable

Unfortunately, this isn’t supported. 

The best you could do is something pathological like:

=> \set s 'select * from '

=> \set pr ' limit 10;'

=> :s mytable :pr

=> :s test :pr

myint

-------

 1

 2

 3

 4

 5

 6

 7

 8

 9

 10

(10 rows)
