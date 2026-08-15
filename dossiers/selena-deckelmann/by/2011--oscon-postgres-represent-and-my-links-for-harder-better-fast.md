---
title: "OSCON: Postgres represent! And my links for Harder, Better, Faster, Stronger talk"
person: selena-deckelmann
section: by
type: blog-post
year: 2011
date: 2011-07-23
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2011/07/23/oscon-postgres-represent-and-my-links-for-harder-better-faster-stronger-talk/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# OSCON: Postgres represent! And my links for Harder, Better, Faster, Stronger talk

## Full text

I’m giving a couple talks at OSCON this year. The first is on Tuesday, 10:40am room C123: [Harder, Better, Faster, Stronger: Postgres 9.1](http://www.oscon.com/oscon2011/public/schedule/detail/19275). The other is [Mistakes were Made](http://www.oscon.com/oscon2011/public/schedule/detail/18777), Wednesday at 1:40pm in room D136.

My colleague Robert Treat is giving a [Pro PostgreSQL](http://www.oscon.com/oscon2011/public/schedule/detail/19206) workshop Wednesday at 1:40pm too, room 204. He’s also giving a [Scalability Patterns](http://www.oscon.com/oscon2011/public/schedule/detail/19196) talk at 4:20pm Tuesday. I’m sure his talks will be awesome. 🙂

And here are the [rest of the talks tagged with PostgreSQL](http://www.oscon.com/oscon2011/public/schedule/tag/postgresql).

Also remember — there’s a [PgDay tomorrow](http://calagator.org/events/1250460814) at the Oregon Convention Center!

I’m pushing my examples for my 9.1 talk [into a github repo](https://github.com/selenamarie/pg91demo). It should be populated with whatever I decide to use for the talk by Monday evening.

Building 9.1 for me on Mac OS X (leopard!) involved the following:

git tag -l | grep REL9_1

git checkout REL9_1_BETA2

./configure --with-perl --with-python --prefix=/opt/pg91beta2 --with-readline

make

make install

Normal caveats apply – you need X Code of a reasonably recent version, and a bunch of support libraries to make this happen. I haven’t rebuilt from scratch on OS X in a long time, but now I realize that maybe I aught to go through the pain and document this again.

But I digress!

I have a long list of resources for this talk and wanted to share. Probably in the slides for the talk, I’ll provide shortlinks so that people can pull them up and read instead of listening to me 😀

Here’s my links:

- [Latest build of documentation for 9.1](http://developer.postgresql.org/)

- [Heikki’s slides about replication](http://www.pgcon.org/2010/schedule/attachments/149_PGCon2010-Built-in-Replication.pdf) 

- [pg_basebackup](http://www.postgresql.org/docs/9.1/static/app-pgbasebackup.html)

- [Common Table Expressions](http://developer.postgresql.org/pgdocs/postgres/queries-with.html#QUERIES-WITH-MODIFYING)

- [Writeable CTE Examples](http://www.depesz.com/index.php/2011/03/16/waiting-for-9-1-writable-cte/)

- [Upserting with Writeable CTEs](http://xzilla.net/blog/2011/Mar/Upserting-via-Writeable-CTE.html)

- [Per column collation support examples](http://www.depesz.com/index.php/2011/03/04/waiting-for-9-1-per-column-collation-support/)

- [Review of Postgres Extensions effects and usage for end users](http://facility9.com/2011/03/postgresql-extensions/)

- [Dimitri’s talk from last year about his work on Extensions](http://wiki.postgresql.org/images/0/00/PGDay2010-Extensions.pdf)

- [David Wheeler’s talk (tomorrow!) on building extensions](http://wiki.postgresql.org/wiki/PDXPUGDay2011#Building_and_Distributing_PostgreSQL_Extensions_Without_Learning_C_.28David_E._Wheeler.29)

- [User-level overview of KNN Indexing](http://wiki.postgresql.org/wiki/What's_new_in_PostgreSQL_9.1#K-Nearest-Neighbor_Indexing) 

- [Developer overview of KNN Indexes](http://www.sai.msu.su/~megera/postgres/talks/pgday-2010.pdf)

- [Unlogged tables overview with example performance test from depesz](http://www.depesz.com/index.php/2011/01/03/waiting-for-9-1-unlogged-tables/)

- [Robert Haas’ analysis of features and differences between temporary tables and ulogged tables](http://rhaas.blogspot.com/2010/05/global-temporary-and-unlogged-tables.html)

- [SSI wiki page](http://wiki.postgresql.org/wiki/SSI)

- [My notes from Kevin Grittner’s talk on SSI](http://www.chesnok.com/daily/2011/03/24/raw-notes-from-kevin-grittners-talk-on-ssi/)

- [Postgres 9.1 docs on synchronous replication](http://developer.postgresql.org/pgdocs/postgres/warm-standby.html#SYNCHRONOUS-REPLICATION )

- [Wiki page for synchronous replication](http://wiki.postgresql.org/wiki/What%27s_new_in_PostgreSQL_9.1#Synchronous_replication_and_other_replication_features)

- [Developer wiki page about synchronous replication implementation](http://wiki.postgresql.org/wiki/Synchronous_replication )

- [Josh Berkus’ Magical Mystery Tour of 9.1 features](http://www.pgexperts.com/document.html?id=50) 

And if you’re wondering about the title, I took it from an great Daft Punk song that fans have created some epic videos of:
