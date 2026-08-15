---
title: "Tier-1 status for Linux 64 Debug build jobs on March 14, 2016"
person: selena-deckelmann
section: by
type: blog-post
year: 2016
date: 2016-03-08
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2016/03/08/tier-1-status-for-linux-64-debug-build-jobs-on-march-14-2016/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Tier-1 status for Linux 64 Debug build jobs on March 14, 2016

## Full text

*I sent this to dev-planning, dev-platform, sheriffs and tools-taskcluster today. I added a little more context for a non-Mozilla audience.*

The time has come! We are planning to switch to [Tier-1 on Treeherder](https://wiki.mozilla.org/Sheriffing/Job_Visibility_Policy) for TaskCluster [Linux 64 Debug](https://treeherder.mozilla.org/#/jobs?repo=mozilla-central&filter-searchStr=linux%20x64%20debug) build jobs on March 14. At the same time, we will hide the Buildbot build jobs, but continue running them. This means that these jobs will become what Sheriffs use to determine the health of patches and our trees.

On March 21, we plan to switch the Linux 64 Debug tests to Tier-1 and hide the related Buildbot test jobs.

After about 30 days, we plan to disable and remove all Buildbot jobs related to Linux Debug.

Background:

We’ve been running Linux 64 Debug builds and tests using TaskCluster side-by-side with Buildbot jobs since February 18th. Some of the project work that was done to green up the tests is documented [here](https://public.etherpad-mozilla.org/p/buildbot-to-taskcluster-migration).

The new tests are running in Docker-ized environments, and the Docker images we use are defined in-tree and publicly accessible.

This work was the culmination of many months of effort, with Joel Maher, Dustin Mitchell and Armen Zambrano primarily focused on test migration this quarter. Thank you to everyone who responded to NEEDINFOs, emails and pings on IRC to help with untangling busted test runs.

On performance, we’re taking a 14% hit across all the new test jobs vs. the old jobs in Buildbot. We ran two large-scale tests to help determine where slowness might still be lurking, and were able to find and fix many issues. There are a handful of jobs remaining that seem significantly slower, while others are significantly faster. We decided that it was more important to deprecate the old jobs and start exclusively maintaining the new jobs now, rather than wait to resolve the remaining performance issues. Over time we hope to address issues with the owners of the affected test suites.
