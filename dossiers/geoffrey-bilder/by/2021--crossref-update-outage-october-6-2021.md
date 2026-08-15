---
title: "Update on the outage of October 6, 2021"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2021
date: 2021-10-27
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/update-on-the-outage-of-october-6-2021/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/sen6x-c2c16."
---

# Update on the outage of October 6, 2021

## Full text

**5 minute read.**

## Update on the outage of October 6, 2021

In [my blog post on October 6th](https://doi.org/10.64000/e3xe5-wae58), I promised an update on what caused the outage and what we are doing to avoid it happening again. This is that update.

Crossref hosts its services in a hybrid environment. Our original services are all hosted in a data center in Massachusetts, but we host new services with a cloud provider. We also have a few R&D systems hosted with Hetzner.

We know an organisation our size has no business running its own data center, and we have been slowly moving services out of the data center and into the cloud.

For example, over the past nine months, we have moved our authentication service and our [REST APIs](https://api.crossref.org) to the cloud.

And, we are working on moving the other existing services too. For example, we are in the midst of moving [Event Data](https://www.crossref.org/services/event-data/) and, our next target, after Event Data, is the content registration system.

All new services are deployed to the cloud by default.

While moving services out of the data center, we have also been trying to shore up the data center to ensure it continues to function during the transition. One of the weaknesses we identified in the data center was that the same provider managed both our primary network connection *and* our backup connection (albeit- on entirely different physical networks). We understood that we really needed a separate provider to ensure adequate redundancy, and we had already had a third network drop installed from a different provider. But, unfortunately, it had not yet been activated and connected.

Meanwhile, our original network provider for the first two connections informed us months ago that they would be doing some major work on our *backup* connection. However, they assured us that it would not affect the primary connection- something we confirmed with them repeatedly since we knew our replacement backup connection was not yet active.

But, the change our provider made *did* affect *both* the backup (as intended) and the primary (not intended). They were as surprised as we were, which kind of underscores why we want two separate providers as well as two separate network connections.

So both our primary and secondary networks went down while we had not yet activated our replacement secondary network.

Also, our only *local* infrastructure team member was in surgery at the time (He is fine. It was routine. Thanks for asking).

This meant we had to send a local developer to the data center, but the data center’s authentication process had changed since the last time said developer had visited (pre-pandemic). So, yeah, it took us a long time to even get into the data center.

By then, our infrastructure team member was out of surgery and on the phone with our network provider, who realized their mistake and reverted everything. This whole process (getting network connectivity restored, not the surgery) took almost two hours.

Unfortunately, the outage didn’t just affect services hosted in the data center. It also affected our cloud-hosted systems. This is because all of our requests were still routed to the data center first, after which those destined for the cloud were split out and redirected. This routing made sense when the bulk of our requests were for services hosted in the data center. But, within the past month, that calculus had shifted. Most of our requests now are for cloud-based services. We were scheduled to switch to routing traffic through our cloud provider first, and had this been in place, many of our services would have continued running during the data center outage.

It is very tempting to stop this explanation here and leave people with the impression that:

* The root cause of the outage was the unpredicted interaction between the maintenance on our backup line and the functionality of our primary line;
* Our slowness to respond was exclusively down to one of the two members of our infrastructure staff being (*cough*) indisposed at the time.

But the whole event uncovered several other issues as well.

Namely:

* Even if one of our three lines had stayed active, the routers in the data center would not have cut over to the redundant working system because we had misconfigured them and we had not tested them;
* We did not keep current documentation on the changing security processes for accessing the data center;
* Our alerting system does not support the kind of escalation logic, and coverage-scheduling that would have allowed us to automatically detect when our primary data center administrator didn’t respond (being in surgery and all) and redirect alerts and warnings to secondary responders; and
* We need to accelerate our move out of the data center.

What are we doing to address these issues?

* Completing the installation of the backup connection with a second provider;
* Scheduling a test of our router’s cutover processes where we will actually pull the plug on our primary connection to ensure that failover is working as intended. We will give users ample warning before conducting this test;
* Revising our emergency contact procedures and updating our documentation for navigating our data center’s security process;
* Replacing our alerting system with one that gives us better control over escalation rules; and
* Adding a third FTE to the infrastructure team to help us accelerate our move to the cloud and to implement infrastructure management best practices.

October 6th, 2021, was a bad day. But we’ve learned from it. So if we have a bad day in the future, it will at least be different.
