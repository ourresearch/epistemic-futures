---
title: "TaskCluster migration: a “hello, world” for worker task creator"
person: selena-deckelmann
section: by
type: blog-post
year: 2015
date: 2015-06-02
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2015/06/02/taskcluster-migration-a-hello-world-for-worker-task-creator/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# TaskCluster migration: a “hello, world” for worker task creator

## Full text

On June 1, 2015, Morgan and Dustin presented an introduction to configuring and testing [TaskCluster](http://docs.taskcluster.net) worker tasks. [The session was recorded](https://vreplay.mozilla.com/replay/showRecordingExternal.html?key=7AvN2iczQYcI3lY). Their notes are also [available in an etherpad](https://etherpad.mozilla.org/taskcluster-hello-world).

The key tutorial information centered on how to set up jobs, test/run them locally and selecting appropriate worker types for jobs.

This past quarter Morgan has been working on Linux Docker images and TaskCluster workers for Firefox builds. Using that work as an example, Morgan showed how to set up new jobs with Docker images. She also touched on a couple issues that remain, like sharing sensitive or encrypted information on publicly available infrastructure.

A couple really nice things:

- You can run the whole configuration locally by copy and pasting a shell script that’s output by the TaskCluster tools

- There are a number of predefined workers you can use, so that you’re not creating everything from scratch

Dustin gave an overview of [task graphs using a specific example](https://tools.taskcluster.net/task-graph-inspector/#m_E90SLvQcOsLMl1Q-kqPA/). Looking through the docs, I think the best source of documentation other than this video is probably the [API documentation](http://docs.taskcluster.net/scheduler/api-docs/). The docs could use a little more narrative for context, as Dustin’s short talk about it demonstrated.

The talk closed with an invitation to help write new tasks, with pointers to the [Android work Dustin’s been doing](https://bugzilla.mozilla.org/show_bug.cgi?id=1118394).
