---
title: "[workweek] tc-worker workweek recap"
person: selena-deckelmann
section: by
type: blog-post
year: 2016
date: 2016-03-11
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2016/03/11/workweek-tc-worker-workweek-recap/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# [workweek] tc-worker workweek recap

## Full text

## Sprint recap

We spent this week sprinting on the tc-worker, engines and plugins. We merged 19 pull requests and had many productive discussions!

### tc-worker core

We implemented the task loop! This basic loop should start when the worker is invoked. It spins up a task claimer and manager responsible for claiming as many tasks up to it’s available capacity and running them to completion. You can find details in [in this commit](https://github.com/taskcluster/taskcluster-worker/commit/6510a6c2ab9d83c88403eb473b28efcdf89b3914#diff-f64c7e5420debf6d23a76b241e871afeR16). We’re still working on some high level documentation.

We did some cleanups to make it easier to download and get started with builds. We fixed up packages related to generating go types from json schemas, and the types now conform to the linting rules

We also implemented the webhookserver. The package provides implementations of the WebHookServer interface which allows attachment and detachment of web-hooks to an internet exposed server. This will support both the livelog and interactive features. Work is detailed in [PR 37](https://github.com/taskcluster/taskcluster-worker/pull/37).

### engine: hello, world

Greg created a proof of concept and [pushed a successful task](https://tools.taskcluster.net/task-inspector/#a6NTsF9yQvC2cdIp1qTNrg/) to emit a hello, world artifact. Greg will be writing up something to describe this process next week.

### plugin: environment variables

Wander landed this plugin this week to support environment variable setting. The work is described in [PR 39](https://github.com/taskcluster/taskcluster-worker/pull/39).

### plugin: artifact uploads

This plugin will support artifact uploads for all engines to S3 and is based on generic-worker code. This work is started in [PR 55](https://github.com/taskcluster/taskcluster-worker/pull/55).

## TaskCluster design principles

We discussed as a team the ideas behind the design of TaskCluster. The umbrella principle we try to stick to is: Getting Things Built. We felt it was important to say that first because it helps us remember that we’re here to provide features to users, not just design systems. The four key design principles were distilled to:

- Self-service

- Robustness

- Enable rapid change

- Community friendliness

One surprising connection (to me) we made was that our privacy and security features are driven by community friendliness.

We plan to add our ideas about this to a TaskCluster “about” page.

## TaskCluster code review

We discussed our process for code review, and how we’d like to do them in the future. We covered issues around when to do architecture reviews and how to get “pre-reviews” for ideas done with colleagues who will be doing our reviews. We made an [outline of ideas](https://public.etherpad-mozilla.org/p/taskcluster-code-review) and will be giving them a permanent home on our [docs site](http://docs.taskcluster.net).

## Q2 Planning

We made a first pass at our [2016q2 goals](https://public.etherpad-mozilla.org/p/taskcluster-2016q2). The main theme is to add OS X engine support to taskcluster-worker, continue work on refactoring intree config and build out our monitoring system beyond InfluxDB. Further refinements to our plan will come in a couple weeks, as we close out Q1 and get a better understanding of work related to the Buildbot to TaskCluster migration.
