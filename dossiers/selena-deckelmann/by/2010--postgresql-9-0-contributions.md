---
title: "PostgreSQL 9.0: contributions!"
person: selena-deckelmann
section: by
type: blog-post
year: 2010
date: 2010-09-21
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2010/09/21/postgresql-9-0-contributions/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# PostgreSQL 9.0: contributions!

## Full text

New releases are opportunities for reflection! 

As PostgreSQL grows, I would like to know how many people are contributing at any time. This is difficult to measure, given how many people contribute in ways not visible to the internet – advocating for PostgreSQL at work, sharing information about PostgreSQL offline in any way, or developing code related to PostgreSQL that isn’t shared directly back.

PostgreSQL developers have a habit of mentioning the people involved in the development of features in the commit logs. This includes people who discuss topics on the mailing list, who report bugs, provide test cases or send in patches. I spent a bit of time digging through the commit logs and pulling out unique names that are mentioned. This is a lossy process, as the log files are long, names are not always easy to spot, and I only spent 6 hours going through it.

I’ve made it through the 9.0 (16163 lines of logs) and 8.4 logs (21257 lines of logs) so far. 

Here’s some basic information about them: 

- 8.4 logs mention about **230** unique people (11 committers)

- 9.0 logs mention about **275** unique people (16 committers)

- 8.4 development contained 2293 commits with commits per author broken down below (click for a bigger version):

[](http://www.chesnok.com/daily/wp-content/uploads/2010/09/8.4commits.png)

- 9.0 development contained 1703 commits, and the commits per author broken down below (click for a bigger version):
[](http://www.chesnok.com/daily/wp-content/uploads/2010/09/9.0-commits.png)

I’m working on graphs about number of lines inserted or deleted by each author, but need more time to work out the information presentation. Some interesting trends emerge about what the role of each committer is – particularly that there are a couple people who seem to be “gardeners” of the code – removing a lot of lines, sometimes more than they are adding. With a project as old as ours (first commit in 1996!), this maintenance work is critical.

I also did some grepping for key words in the commit messages: 

word
times mentioned
 in 8.3
times mentioned
 in 8.4
times mentioned
 in 9.0

review
24
14
49

cute
29
26
25

tom lane
904
901
635

gripe
37
48
26

hot standby
0
5
48

replication
18
4
52

You’re welcome to explore our git repo at [git.postgresql.org](http://git.postgresql.org/gitweb?p=postgresql.git). Thanks to all the folks who worked on the git migration over the past few months, and finally made [our transition from CVS to git complete](http://blog.hagander.net/archives/175-PostgreSQL-now-on-git!.html) last night!
