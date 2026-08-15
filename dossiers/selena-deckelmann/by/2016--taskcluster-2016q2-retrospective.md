---
title: "TaskCluster 2016Q2 Retrospective"
person: selena-deckelmann
section: by
type: blog-post
year: 2016
date: 2016-08-03
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2016/08/03/taskcluster-2016q2-retrospective/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# TaskCluster 2016Q2 Retrospective

## Full text

The TaskCluster Platform team worked very hard in Q2 to support the migration off Buildbot, bring new projects into our CI system and look forward with experiments that might enable fully-automated VM deployment on hardware in the future.

We also brought on 5 interns. For a team of 8 engineers and one manager, this was a tremendous team accomplishment. We are also working closely with interns on the Engineering Productivity and Release Engineering teams, resulting in a much higher communication volume than in months past.

We continued our work with RelOps to land Windows builds, and those are available in pushes to Try. This means people can use “one click loaners” for Windows builds as well as Linux (through the Inspect Task link for jobs)! Work on Windows tests is proceeding.

We also created try pushes for Mac OS X tests, and integrated them with the Mac OS X cross-compiled builds. This also meant deep diving into the cross-compiled builds to green them up in Q3 after some compiler changes.

A big part of the work for our team and for RelEng was preparing to implement a new kind of signing process. Aki and Jonas spent a good deal of time on this, as did many other people across PlatformOps. What came out of that work was a detailed specification for TaskCluster changes and for a new service from RelEng. We expect to see prototypes of these ideas by the end of August, and the major blocking changes to the workers and provisioner to be complete then too.

This all leads to being able to ship Linux Nightlies directly from TaskCluster by the end of Q3. We’re optimistic that this is possible, with the knowledge that there are still a few unknowns and a lot has to come together at the right time.

Much of the work on TaskCluster is like building a 747 in-flight. The microservices architecture enables us to ship small changes quickly and without much pre-arranged coordination. As time as gone on, we have consolidated some services (the scheduler is deprecated in favor of the “big graph” scheduling done directly in the queue), separated others (we’ve moved Treeherder-specific services into its own component, and are working to deprecate mozilla-taskcluster in favor of a taskcluster-hg component), and refactored key parts of our systems (intree scheduling last quarter was an important change for usability going forward). This kind of change is starting to slow down as the software and the team adapts and matures.

I can’t wait to see what this team accomplishes in Q3!

Below is the team’s partial list of accomplishments and changes. Please drop by #taskcluster or drop an email to our tools-taskcluster lists.mozilla.org mailing list with questions or comments!

#### Things we did this quarter:

- initial investigation and timing data around using sccache for linux builds

- released update for sccache to allow working in a more modern python environment

- created taskcluster managed s3 buckets with appropriate policies

- tested linux builds with patched version of sccache

- tested docker-worker on packet.net for on hardware testing

- worked with jmaher on talos testing with docker-worker on releng hardware

- created livelog plugin for taskcluster-worker (just requires tests now)

- added reclaim logic to taskcluster-worker

- converted gecko and gaia in-tree tasks to use new v2 treeherder routes

- Updated gaia-taskcluster to allow github repos to use new taskcluster-treeherder reporting

- move docs, schemas, references to https

- refactor documentation site into tutorial / manual / reference

- add READMEs to reference docs

- switch from a * certificate to a SAN certificate for taskcluster.net

- increase accessibility of AWS provisioner by separating bar-graph stuff from workerType configuration

- use roles for workerTypes in the AWS provisioner, instead of directly specifying scopes

- allow non-employees to login with Okta, improve authentication experience

- named temporary credentials

- use npm shrinkwrap everywhere

- enable coalescing

- reduce the artifact retention time for try jobs (to reduce S3 usage)

- support retriggering via the treeherder API

- document azure-entities

- start using queue dependencies (big-graph-scheduler)

- worked with NSS team to have tasks scheduled and displayed within treeherder

- Improve information within docker-worker live logs to include environment information (ip address, instance type, etc)

- added hg fingerprint verification to decision task

- Responded and deployed patches to security incidents discovered in q2 

- taskcluster-stats-collector running with signalfx

- most major services using signalfx and sentry via new monitoring library taskcluster-lib-monitor

- Experimented with QEMU/KVM and libvirt for powering a taskcluster-worker engine

- QEMU/KVM engine for taskcluster-worker

- Implemented Task Group Inspector

- Organized efforts around front-end tooling

- Re-wrote and generalized the build process for taskcluster-tools and future front-end sites

- Created the Migration Dashboard

- Organized efforts with contractors to redesign and improve the UX of the taskcluster-tools site

- First Windows tasks in production – NSS builds running on Windows 2012 R2 

- Windows Firefox desktop builds running in production (currently shown on staging treeherder)

- new features in generic worker (worker type metadata, retaining task users/directories, managing secrets in secrets store, custom drive for user directories, installing as a startup item rather than service, improved syscall integration for logins and executing processes as different users)

- many firefox desktop build fixes including fixes to python build scripts, mozconfigs, mozharness scripts and configs

- CI cleanup https://travis-ci.org/taskcluster

- support for relative definitions in jsonschema2go

- schema/references cleanup

#### Paying down technical debt

- Fixed numerous issues/requests within mozilla-taskcluster

- properly schedule and retrigger tasks using new task dependency system

- add more supported repositories

- Align job state between treeherder and taskcluster better (i.e cancels)

- Add support for additional platform collection labels (pgo/asan/etc)

- fixed retriggering of github tasks in treeherder 

- Reduced space usage on workers using docker-worker by removing temporary images 

- fixed issues with gaia decision task that prevented it from running since March 30th.

- Improved robustness of image creation image

- Fixed all linter issues for taskcluster-queue

- finished rolling out shrinkwrap to all of our services

- began trial of having travis publish our libraries (rolled out to 2 libraries now. talking to npm to fix a bug for a 3rd)

- turned on greenkeeper everywhere then turned it off again for the most part (it doesn’t work with shrinkwrap, etc)

- “modernized” (newer node, lib-loader, newest config, directory structure, etc) most of our major services

- fix a lot of subtle background bugs in tc-gh and improve logging

- shared eslint and babel configs created and used in most services/libraries

- instrumented taskcluster-queue with statistics and error reporting

- fixed issue where task dependency resolver would hang

- Improved error message rendering on taskcluster-tools

- Web notifications for one-click-loaner UI on taskcluster-tools

- Migrated stateless-dns server from tutum.co to docker cloud

- Moved provisioner off azure storage development account

- Moved our npm package to a single npm organization
