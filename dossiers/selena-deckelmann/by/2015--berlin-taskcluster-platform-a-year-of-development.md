---
title: "[berlin] TaskCluster Platform: A Year of Development"
person: selena-deckelmann
section: by
type: blog-post
year: 2015
date: 2015-10-05
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2015/10/05/berlin-taskcluster-platform-a-year-of-development/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# [berlin] TaskCluster Platform: A Year of Development

## Full text

*Back in September, the TaskCluster Platform team held a workweek in Berlin to discuss upcoming feature development, focus on platform stability and monitoring and plan for the coming quarter’s work related to Release Engineering and supporting Firefox Release. These posts are documenting the many discussions we had there.*

Jonas kicked off our workweek with a brief look back on the previous year of development.

### Prototype to Production

In the last year, TaskCluster went from an idea with a few tasks running to running all of FirefoxOS aka B2G continuous integration, which is about 40 tasks per minute in the current environment.

Architecture-wise, not a lot of major changes were made. We went from CloudAMQP to [Pulse](https://pulse.mozilla.org/) (in-house RabbitMQ). And shortly, Pulse itself will be [moving it’s backend to CloudAMQP](https://docs.google.com/document/d/1F207nMJUXXxyDNuJuoPDfFzK39RSy0gOqrYMR-21AcQ/edit)! We introduced [task statuses](http://docs.taskcluster.net/queue/api-docs/#status), and then simplified them.

On the implementation side, however, a lot changed. We added many features and addressed a ton of docker worker bugs. We killed Postgres and added Azure Table Storage. We rewrote the provisioner almost entirely, and moved to ES6. We learned a lot about babel-node.

We introduced the first alternative to the Docker worker, the Generic worker. We for the first time had Release Engineering create a worker, the Buildbot Bridge.

We have several new users of TaskCluster! Brian Anderson from Rust created a system for testing all Cargo packages for breakage against release versions. We’ve had a number of external contributors create builds for FirefoxOS devices. We’ve had a few Github-based projects jump on [taskcluster-github](http://github.com/taskcluster/taskcluster-github).

### Features that go beyond BuildBot

One of the goals of creating TaskCluster was to not just get feature parity, but go beyond and support exciting, transformative features to make developer use of the CI system easier and fun.

Some of the features include:

- [Interactive sessions](http://docs.taskcluster.net/workers/docker-worker/#features-interactive) 

- Live logging (mentioned in our [createArtifact() docs](http://docs.taskcluster.net/queue/api-docs/#createArtifact) and visible in the [task-inspector](http://tools.taskcluster.net/task-inspector/) for a task) 

- Public-first [task statuses](http://docs.taskcluster.net/queue/api-docs/#status) 

- [Easy Indexing](http://docs.taskcluster.net/services/index/) 

- Storage in S3 (see [createArtifact()](http://docs.taskcluster.net/queue/api-docs/#createArtifact) documentation) 

- Public first, [reference-style APIs](http://docs.taskcluster.net) 

- Support for [remote device lab workers](https://github.com/taskcluster/testdroid-proxy/blob/master/README.md)

### Features coming in the near future to support Release

Release is a special use case that we need to support in order to take on Firefox production worload. The focus of development work in Q4 and beyond includes:

- Secrets handling to support Release and ops workflows. In Q4, we should see secrets.taskcluster.net go into production and UI for roles-based management.

- Scheduling support for coalescing, SETA and cache locality. In Q4, we’re focusing on an external data solution to support coalescing and SETA.

- Private data hosting. In Q4, we’ll be using a roles-based solution to support these.
