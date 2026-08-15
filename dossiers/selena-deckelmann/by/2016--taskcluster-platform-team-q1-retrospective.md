---
title: "TaskCluster Platform Team: Q1 retrospective"
person: selena-deckelmann
section: by
type: blog-post
year: 2016
date: 2016-05-11
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2016/05/11/taskcluster-platform-team-q1-retrospective/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# TaskCluster Platform Team: Q1 retrospective

## Full text

TaskCluster Platform team did a lot of foundational work in Q1, to set the stage for some aggressive goals in Q2 around landing new OS support and migrating as fast as we can out of Buildbot.

The two big categories of work we had were “Moving Forward” — things that move TaskCluster forward in terms of developing our team and adding cool features, and “Paying debt” — upgrading infra, improving security, cleaning up code, improving existing interfaces and spinning out code into separate libraries where we can.

As you’ll see, there’s quite a lot of maintenance that goes into our services at this point. There’s probably some overlap of features in the “paying debt” section. Despite a little bit of fuzzyness in the definitions, I think this is an interesting way to examine our work, and a way for us to prioritize features that eliminate certain classes of unpleasant debt paying work. I’m planning to do a similar retrospective for Q2 in July.

I’m quite proud of the foundational work we did on taskcluster-worker, and it’s already paying off in rapid progress with OS X support on hardware in Q2. We’re making fairly good progress on Windows in AWS as well, but we had to pay down years of technical debt around Windows configuration to get our builds running in TaskCluster. Making a choice on our monitoring systems was also a huge win, paying off in much better dashboarding and attention to metrics across services. We’re also excited to have shipped the “Big Graph Scheduler”, which enables cross-graph dependencies and arbitrarily large task graphs (previous graphs were limited to about 1300 tasks). Our team also grew by 2 people – we added Dustin Mitchell, who will continue to do all kinds of work around our systems, focus on security-related issues and will ship a new intree configuration in Q2, and Eli Perelman, who will focus on front end concerns.

The TaskCluster Platform team put the following list together at the start of Q2.

Moving forward:

- Kicked off and made excellent progress on the taskcluster-worker, a new worker with more robust abstractions and our path forward for worker support on hardware and AWS (the OS X worker implementation currently in testing uses this)

- Shipped task.dependencies in the queue and will be shipping the rest of the “big graph scheduler” changes just in time to support some massive release promotion graphs

- Deployed the first sketch for monitoring dashboard

- Shipped login v3 (welcome, dustin!)

- Rewrote and tested a new method for mirroring data between AWS regions (cloud-mirror)

- Researched a monitoring solution and made a plan for Q2 rollout of signalFX

- Prototyped and deployed aggregation service: statsum (and client for node.js)

- Contributed to upstream open source tools and libraries in golang and node ecosystem

- Brought bstack and rthijssen up to speed, brought Dustin onboard!

- Working with both GSoC and Outreachy, and Mozilla’s University recruiting to bring five interns into our team in Q2/Q3

Paying debt:

- Shipped better error messages related to schema violations

- Rolled out formalization of error messages: {code: “…”, message: “…”, details: {…}}

- Sentry integration — you see an 5xx error with an incidentId, we see it too!

- Automatic creation of sentry projects, and rotation of credentials

- go-got — simple HTTP client for go with automatic retries

- queue.listArtifacts now takes a continuationToken for paging

- queue.listTaskGroup refactored for correctness (also returns more information)

- Pre-compilation of queue, index and aws-provisioner with babel-compile (no longer using babel-node)

- One-click loaners, (related work by armenzg and jmaher to make loaners awesome: instructions + special start mode) 

- Various UI improvements to tools.taskcluster.net (react.js upgrade, favicons, auth tools, login-flow, status, previous taskIds, more)

- Upgrade libraries for taskcluster-index (new config loader, component loader)

- Fixed stateless-dns case-sensitivity (livelogs works with DNS resolvers from Germans ISPs too)

- Further greening of travis for our repositories

- Better error messages for insufficient scope errors

- Upgraded heroku stack for events.taskcluster.net (pulse -> websocket bridge)

- Various fixes to automatic retries in go code (httpbackoff, proxy in docker-worker, taskcluster-client-go)

- Moved towards shrinkwrapping all of the node services (integrity checks for packages)

- Added worker level timestamps to task logs

- Added metrics for docker/task image download and load times

- Added artifact expiration error handling and saner default values in docker-worker

- Made a version jump from docker 1.6 to 1.10 in production (included version upgrades of packages and kernel, refactoring of some existing logic)

- Improved taskcluster and treeherder integration (retrigger errors, prep for offloading resultset creation to TH)

- Rolling out temp credential support in docker-worker

- Added mach support for downloading task image for local development

- Client support for temp credentials in go and java client

- JSON schema cleanups 

- CI cleanup (all green) and turning off circle CI

- Enhancements to jsonschema2go

- Windows build work by rob and pete for getting windows builds migrated off Buildbot

- Added stability levels to APIs
