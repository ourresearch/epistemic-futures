---
title: "Everyday Postgres: Specifying all your INSERT columns"
person: selena-deckelmann
section: by
type: blog-post
year: 2014
date: 2014-01-14
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2014/01/14/everyday-postgres-specifying-all-your-insert-columns/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Everyday Postgres: Specifying all your INSERT columns

## Full text

Postgres has so many convenient features, including the ability to *not* provide a list of columns to an INSERT.

For example:

CREATE TABLE temp_product_versions ( LIKE product_versions );
INSERT INTO temp_product_versions ( SELECT * from product_versions ); 

That’s pretty badass.

However, you may encounter trouble in paradise later if you use this kind of shortcut in production code.

See if you can spot the error in this code sample below.

Here’s the error message:

ERROR: column "is_rapid_beta" is of type boolean but expression is of type citext
LINE 10: repository
 ^
HINT: You will need to rewrite or cast the expression.
QUERY: INSERT INTO releases_recent
SELECT 'MetroFirefox',
 version,
 beta_number,
 build_id
 update_channel,
 platform,
 is_rapid,
 is_rapid_beta,
 repository
FROM releases_recent
 JOIN products
 ON products.product_name = 'MetroFirefox'
WHERE releases_recent.product_name = 'Firefox'
 AND major_version_sort(releases_recent.version)
 >= major_version_sort(products.rapid_release_version)
CONTEXT: PL/pgSQL function update_product_versions(integer) line 102 at SQL statement

And here’s the code (long!)

I’m sure quite a few of you found the problem right away. For the rest of us…

Here’s the error message you get if you specify the columns for the INSERT:

ERROR: INSERT has more target columns than expressions
LINE 10: repository
 ^
QUERY: INSERT INTO releases_recent (
 product_name,
 version,
 beta_number,
 build_id,
 update_channel,
 platform,
 is_rapid,
 is_rapid_beta,
 repository
)
SELECT 'MetroFirefox',
 version,
 beta_number,
 build_id
 update_channel,
 platform,
 is_rapid,
 is_rapid_beta,
 repository
FROM releases_recent
 JOIN products
 ON products.product_name = 'MetroFirefox'
WHERE releases_recent.product_name = 'Firefox'
 AND major_version_sort(releases_recent.version)
 >= major_version_sort(products.rapid_release_version)
CONTEXT: PL/pgSQL function update_product_versions(integer) line 112 at SQL statement

Now, it should be completely obvious. There’s a missing comma after build_id.

Implicit columns for INSERT are a convenient feature when you’re getting work done quickly, they are definitely not a best practice when writing production code. If you know of a linting tool for plpgsql that calls this kind of thing out, I’d love to hear about it and use it.
