---
title: "Project Spotlight: CollectiveVoice"
person: "nick-vincent"
section: "by"
type: "blog-post"
year: 2024
date: "2024-02-02"
venue: "Metagov News"
authors: "Val Elefante, Nick Vincent, Skylar Karzhevsky"
source_url: "https://metagov.substack.com/p/metagov-project-spotlight-collectivevoice"
retrieved: "2026-08-13"
content: "full-text"
notes: "Substack byline shows Val Elefante; the piece is signed at the end by Val Elefante, Nick Vincent, and Skylar Karzhevsky, and is listed as his own writing on his CV."
---

# Project Spotlight: CollectiveVoice

## Full text

Welcome to another Metagov Project Spotlight.

This spotlight features a case study we conducted with our new community self-governance application, CollectiveVoice. The study is a follow-up to Shauna Gordon-McKeon’s guest blog post on the Open Collective blog titled “Govern your Collective with Metagov Gateway”. In that post, Shauna detailed how she worked closely with two Open Collective communities to help them set up unique, collective governance policies across different platforms using Metagov’s tools.

### Metagov Refresher

If you’re here and don’t already know who, or remember what, Metagov is: Metagov is a laboratory for digital governance, with a mission to cultivate tools, practices, and communities that enable self-governance in the digital age.

For many communities today, online platforms play a key role in how they communicate and coordinate. Additionally, the platforms that communities use have effects on how they are able to self-govern themselves. Many platforms, in fact, are designed in ways that undermine self-governance. In particular, communities using platforms that perpetuate the admin-user model, also described as "implicit feudalism," face a common but critical issue:

-

Admin-user models grant administrators disproportionate power over users by opening the potential for an admin to exploit key technical infrastructure or systems in ways that may be known or unknown to users.

Metagov’s tools give communities ways to prevent, respond to, and hold accountable this typically absolute admin power. This is done by introducing governance practices into the operation of shared digital infrastructure. Communities can automatically link executive administrative actions with collective decision-making processes, including juries, term limits, deliberative assemblies, consensus, and more—making transparency possible and accountability automatic.

And while, in principle, this intervention enables and expands much-needed governance capabilities, particularly when using admin/user-modeled platforms, it hasn’t always been very easy to write and maintain the policies (programs or scripts) necessary to link and automate these governance practices. Since Shauna’s initial blog in 2021, we have worked on improving these tools to make them easier to use and understand for online communities. CollectiveVoice is one example of this work and brings us one step closer to governance-enabled models of online platforms. We are excited to share the latest developments in this work with you here.

Keep up to date with CollectiveVoice and other news about Metagov’s projects, research, and community by subscribing.

Subscribe

### Introducing CollectiveVoice

CollectiveVoice is an application that enables open collective communities to choose from a more diverse set of governance processes to make decisions about shared finances (powered by PolicyKit and the Metagov Gateway). In case you’ve found this blog but haven’t heard of Open Collective, Open Collective is a platform for transparent money management for organizations such as co-ops, nonprofits, mutual aid groups, and open-source software groups.

On Open Collective, admins have decision-making power to approve or reject submitted expenses, while non-admin members do not. For communities with decentralized or democratic governance as a pillar, these types of technological restrictions can be misaligned with community values and work against operations.

For example, administrators can find themselves in a position where they may need to make decisions without all the necessary information or on behalf of other group members—perhaps without ever being explicitly granted that authority. For administrators, this can lead to micromanagement, duplication of work, slowdowns, and burnout. For non-admin community members, this can lead to mistrust, overdependence, bias, and exclusion.

Over the past few months, we conducted 15 interviews with leaders and stewards of self-governing communities to learn more about the challenges they face conducting governance over shared finances. We spoke with representatives from a variety of Open Collective communities, including mutual aid groups, open source software projects, social justice organizations, co-living communities, and more based across the U.S. and Europe. We wanted to know what decision-making procedures and digital tools they were already using and what types of features would be most supportive of their working processes and structures.

### Key Takeaways from Interviews

From these interviews, we learned that

-

communities are distributed across several digital tools and platforms, and

-

communities need context-aware decision-making procedures based on expense types

Communities expressed the need to be able to define qualities for specific types of expenses, say, based on expense amount, title/description, or tag in Open Collective, and then match that expense type to a specific voting template or policy that gets sent to a digital tool of the community’s choice, typically a platform where the majority of the community gathers to communicate.

This is the type of automated governance interoperability that CollectiveVoice is able to support by embracing decentralization and modularity. CollectiveVoice embraces decentralization by using Metagov Gateway to connect existing platforms (i.e., Open Collective, Slack, Discord, GitHub, etc.) and modularity by using PolicyKit to write platform- and integration-specific policies that bi-directionally expand the set of governance features available to a set of linked platforms and tools.

To illustrate this automated governance interoperability in concrete terms, consider the following example, where CollectiveVoice deploys different decision-making procedures based on the type of expense submitted to Open Collective:

Example: A community wants to establish unique decision-making policies for two types of expenses:

-

Small, recurring, and essential expenses: Submitting these types of expenses triggers a quick and easy “peer-approval” process requiring the approval of the expense from any one other person in the community, and

-

Larger, one-off, and nonessential expenses: Submitting these types of expenses triggers a larger, four-person jury deliberation.

-

In both cases, the results of a decision-making procedure are sent back to Open Collective and trigger the approval or rejection of a submitted expense.

The image below represents how CollectiveVoice handles these two different expense policies by watching for Open Collective expense submissions, triggering the appropriate decision-making procedure on the community’s linked Slack (the platform we focused on for this pilot), and sending results from Slack back to Open Collective to either approve or reject the submitted expense.

Graphic created by our UX designer, Julija Rukanskaite

In this demo video, you’ll see that we’ve built CollectiveVoice to accommodate a wide variety of different expense types that communities may want to account for and enable the creation of different policies that pair with those expense types. Down the line, we want to expand the types of voting templates available by default. If you have a policy you’d like to try, please get in touch with us!

Another insight from our interviews was the need from communities for the following additional features from tools for collectively self-governing funds:

-

Transparency over shared money

-

Easy, low-bar participation

-

Community knowledge of rules and policies

-

Social capacity building and education

-

Ability to experiment

### Pilot Program with MAMAS

In May 2023, we onboarded a mutual aid group called MAMAS (Mutual Aid Medford & Somerville) to CollectiveVoice. MAMAS distributes groceries to their local community, with costs for groceries averaging around $7,500 per month. Members buy groceries for distribution and submit their receipts to MAMAS’ Open Collective for reimbursement.

A representative from MAMAS used CollectiveVoice’s no-code UX to set up a custom policy for making decisions about grocery expense reimbursements. They configured an emoji-voting process in their Slack workspace, which allowed more members of their community (including non-admins of Open Collective) to participate in the decision-making over expense reimbursement. Each time an expense reimbursement was posted to Open Collective, the decision-making processes would be triggered by sending a post to their Slack with information about the request and the option to approve (up-vote) or reject (down-vote) the request. The policy set a threshold of upvotes necessary for an expense to be approved and trigged the automatic approval of the reimbursement request on Open Collective if that threshold was reached. Otherwise, if the threshold was not met (or there had been downvotes), then the expense was automatically rejected in Open Collective.

After three months, we caught up with Skyler Karzhevsky, one of the lead organizers of MAMAS, for feedback on how CollectiveVoice had changed their expense reimbursement decision-making processes. Although the policy was quite simple, it still managed to accomplish some of the key goals we were targeting, including distributing workload among leadership, increasing transparency, democratizing decision-making, boosting collective responsibility and participation, and spurring creativity in governance.

Graphic created by Julija Rukanskaite.

### Conclusion and Further Research

Our pilot with MAMAS demonstrated the capacity for our tool to support communities with cross-platform self-governance, but there is more work to be done.

One driving question we are continuing to explore is: how does resource allocation look different in a community under different financial governance models or decision-making structures? There are many diverse governance processes a community could choose from when designing their governance models. See the table below for some of the possibilities.

Graphic created by Leijie Wang from the paper “Pika: Empowering Non-Programmers to Author Executable Governance Policies in Online Communities.”

We’d love to work with you to implement and trial these processes. Currently, CollectiveVoice only works for Slack, but if you use another communication platform, please reach out. We are actively seeking support to improve integrations with Discord, GitHub, and other platforms.

If you would like to try out CollectiveVoice or contribute to its development, please reach out to us at val@metagov.org. You can also reach out to our team in the #metagov-gateway channel of the Metagov Slack.

Thanks for reading, and I hope to hear from you and your collectives soon!

Val Elefante, Nick Vincent, and Skylar Karzhevsky

Special thanks to the rest of the CollectiveVoice team (Amy Zhang, Leijie Wang, Julija Rukanskaite, Cent Hosten, and Josh Tan), MAMAs organizers and community, and Open Collective for all your support.

More links and information about Collective Voice:

-

Val Elefante and Nick Vincent presented CollectiveVoice as part of Sociocracy for All’s Power, Purpose, and Pay Conference in September 2023.

-

CollectiveVoice is an app built out of a larger project called PolicyKit, which was featured in a recent New_Public newsletter.

-

PolicyKit’s website is currently getting a makeover; stay tuned👀–but for now visit PolicyKit.org or the PolicyKit Github to learn more and contribute.

-

Similar projects to CollectiveVoice on our radars include Papertree and FundDrupal.
