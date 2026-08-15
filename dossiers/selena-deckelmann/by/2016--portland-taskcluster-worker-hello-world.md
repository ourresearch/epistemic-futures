---
title: "[portland] taskcluster-worker Hello, World"
person: selena-deckelmann
section: by
type: blog-post
year: 2016
date: 2016-03-07
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2016/03/07/portland-taskcluster-worker-hello-world/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# [portland] taskcluster-worker Hello, World

## Full text

The [TaskCluster Platform](http://docs.taskcluster.net) team is in Portland this week, hacking on the [taskcluster-worker](https://github.com/taskcluster/taskcluster-worker).

Today, we all sync’d up on the current state of our worker, and what we’re going to hack on this week. We started with [the current docs](https://godoc.org/github.com/taskcluster/taskcluster-worker).

The reason why we’re investing so much time in the worker is two fold:

- The worker code previously lived in two code bases – docker-worker and generic-worker. We need to unify these code bases so that multiple engineers can work on it, and to help us maintain feature parity.

- We need to get a worker that supports Windows into production. For now, we’re using the generic-worker, but we’d like to switch over to taskcluster-worker in late Q2 or early Q3. This timeline lines up with when we expect the Windows migration from Buildbot to happen.

One of the things I asked this team to do was come up with some demos of the new worker. The first demo today was to [simply output a log and upload it](https://tools.taskcluster.net/task-inspector/#a6NTsF9yQvC2cdIp1qTNrg/) from Greg Arndt.

The rest of the team is getting their Go environments set up to run tests and get hacking on crucial plugins, like our environment variable handling and additional artifact uploading logic we need for our production workers.

We’re also taking the opportunity to sync up with our Windows environment guru. Our goal for Buildbot to TaskCluster migration this quarter is focused on Linux builds and tests. Next quarter, we’ll be finishing Linux and, I hope, landing Windows builds in TaskCluster. To do that, we have a lot of details to sort out with how we’ll build Windows AMIs and deploy them. It’s a very different model because we don’t have the same options with Docker as we have on Linux.
