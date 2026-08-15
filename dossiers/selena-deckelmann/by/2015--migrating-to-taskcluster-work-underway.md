---
title: "Migrating to Taskcluster: work underway!"
person: selena-deckelmann
section: by
type: blog-post
year: 2015
date: 2015-05-29
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2015/05/29/migrating-to-taskcluster-work-underway/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Migrating to Taskcluster: work underway!

## Full text

Mozilla’s build and test infrastructure has relied on [Buildbot](http://wiki.mozilla.org/Buildbot) as the backbone of our systems [for many years](http://gregoryszorc.com/blog/2013/07/16/analysis-of-firefox's-build-automation/). Asking around, I heard that we started using Buildbot around 2008. The time has come for a change!

Many of the people working on migrating from [Buildbot](https://wiki.mozilla.org/ReleaseEngineering/Applications/Buildbot) to [Taskcluster](http://docs.taskcluster.net/) gathered all together for the first time to talk about migration this morning. ([A recording of the meeting is available](https://vreplay.mozilla.com/replay/showRecordingExternal.html?key=bhKVEns4kzkzdYH))

The goal of this work is to shut down Buildbot and identify a timeline. Our first goal post is to eliminate the Buildbot Scheduler by moving build production entirely into TaskCluster, and scheduling tests in TaskCluster.

Today, most FirefoxOS builds and tests are in Taskcluster. Nearly everything else for Firefox is driven by Buildbot.

Our current tracker bug is ‘[Buildbot -> TaskCluster transition](https://bugzilla.mozilla.org/show_bug.cgi?id=1141248)‘. At a high level, the big projects underway are:

- [Docker containers for desktop builds](https://bugzilla.mozilla.org/show_bug.cgi?id=1151508) – [Morgan Philips](http://linux-poetry.com/) shared [successful Linux64 builds](https://tools.taskcluster.net/task-inspector/#imXseNwETUi1R4lwpnkDRQ/0) at the start of the meeting! These containers are designed to be publicly shareable, and especially shareable with Firefox developers, so that getting an instance of our build environments for Linux is much easier.

- [Driving Android builds out of TaskCluster](https://bugzilla.mozilla.org/show_bug.cgi?id=1118394) – Dustin Mitchell is working on this and has test builds running already as he shaves yaks.

- [OS X cross-compliation](https://bugzilla.mozilla.org/show_bug.cgi?id=921040) – [Ted Mielczarek](https://twitter.com/tedmielczarek) will be building on the work of [Michael Shal](http://gittup.org/blog/), Chris Cooper and others. This will enable us to build Firefox in Linux containers. It won’t let us get away from using Mac Minis for tests, but it will free up hardware that previously was dedicated to builds.

- [Buildbot Bridge](https://bugzilla.mozilla.org/show_bug.cgi?id=1135192) – [Ben Hearsum](http://hearsum.ca/blog) is working on this. It will enable us to schedule a job in TaskCluster, but run the job in Buildbot infrastructure. This is helpful for allowing us to decommission the scheduler portion of Buildbot and helps everyone work on migrating task scheduling and configuration while we work on cross-platform worker support in parallel.

- [Signing workers](https://bugzilla.mozilla.org/show_bug.cgi?id=1149147) – Rail Aliiev worked on this, and [has set up signing workers in TaskCluster](http://rail.merail.ca/posts/taskcluster-first-impression.html) for [Funsize](http://rail.merail.ca/posts/funsize-hacking.html).

- [Generic worker](https://bugzilla.mozilla.org/show_bug.cgi?id=1147206) – [Pete Moore](http://petemoore.tumblr.com/) is working on this as a Q2 deliverable. This will enable us to provision Windows workers.

- Porting of Linux unit tests – [Andrew Halberstadt](http://ahal.ca/) will be focusing on this in the very near future.

We have quite a few things to figure out in the Windows and Mac OS X realm where we’re interacting with hardware, and some work is left to be done to support Windows in AWS. We’re planning to get more clarity on the work that needs to be done there next week.

The bugs identified seem tantalizingly close to describing most of the issues that remain in porting our builds. The plan is to have a timeline documented for builds to be fully migrated over by Whistler! We are also working on migrating tests, but for now believe the Buildbot Bridge will help us get tests out of the Buildbot scheduler, even if we continue to need Buildbot masters for a while. An interesting idea about using runner to manage hardware instead of the masters was raised during the meeting that we’ll be exploring further.

If you’re interested in learning more about TaskCluster and how to use it, Chris Cooper is running a training on Monday June 1 at 1:30pm PT.

Ping me on IRC, [Twitter](http://twitter.com/selenamarie) or email if you have questions!
