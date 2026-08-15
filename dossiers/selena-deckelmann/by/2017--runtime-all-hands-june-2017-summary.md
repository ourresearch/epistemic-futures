---
title: "Runtime All-Hands June 2017 Summary"
person: selena-deckelmann
section: by
type: blog-post
year: 2017
date: 2017-07-03
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2017/07/03/runtime-all-hands-june-2017-summary/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Runtime All-Hands June 2017 Summary

## Full text

All of Mozilla met in San Francisco last week for a work week. Unlike the last few All-Hands, we spent the week mostly informally and not in meetings — hacking in rooms together on near-term work.

The Runtime engineering team was focused on landing patches for Quantum Flow, Quantum DOM and Quantum Networking efforts. We had exciting changes related to Speedometer v2, both in improving how we measure and landing key patches. The Security Engineering team invited the Tor Project to join and deep dive into the Android version of the browser (based on Fennec, and called [OrFox](https://guardianproject.info/apps/orfox/)). The rest of the Runtime team was landing patches, reconnecting with colleagues across the org, and making exciting, measurable progress toward a great launch of Firefox 57.

I asked several team leads to send me their highlights from the week. I’ve summarized this below. If I missed something that was important to you, please get in touch.

**Project Quantum highlights**

“Watching my laptop race HTTP network queries against the disk cache and seeing that it was choosing the right transactions to have the network actually be faster.” -Patrick McManus

- QF team fixed [26 Quantum Flow](https://bugzilla.mozilla.org/buglist.cgi?list_id=13657462&columnlist=bug_id,opendate,changeddate,cf_last_resolved,bug_status,component,resolution,reporter,assigned_to,status_whiteboard,short_desc&status_whiteboard_type=allwordssubstr&chfieldto=Now&chfield=cf_last_resolved&query_format=advanced&chfieldfrom=2017-06-23&status_whiteboard=%5Bqf:&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED) bugs since last Friday, June 23

- Landed (preffed off, going to do a pref experiment for rollout) [budget-based background tab throttling](https://bugzilla.mozilla.org/show_bug.cgi?id=1362322) ([meta bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1302270))

- Joel Maher and his “army of automation” has helped correct Speedometer reporting.

- Got a bunch of people from different teams in a room and figured out the easiest/best architecture for supporting the moz-page-thumbs protocol in e10s (i.e. the protocol that supports everything you see when you open a new tab). Same, for nsITraceableListener support (which is must for 57: needed to support the NoScript addon).

- Incremental table sweeping bug fixes landed that should reduce GC pause times.

- [Byte code cache landed](https://bugzilla.mozilla.org/show_bug.cgi?id=900784) and is on for 5% of Nightly population — this project was in progress for more than a year.

- We [now have a name for almost every runnable](https://bugzilla.mozilla.org/show_bug.cgi?id=1372405) in Firefox.

**Security/Privacy Highlights**

“At Mozilla all hands this week. They are excited to work with us.” –[Mike Perry](https://lists.torproject.org/pipermail/tor-project/2017-June/001225.html), Tor Project

- Tor Browser for Android was updated during the workweek to be based on Firefox 52 (from 45). The update is in QA now.

- Patch written (and being rewritten) for constant blinding in the JIT.

- A [patch for integrating Tor into Focus was hacked up][8] for discussion.

- Got the TLS Canary (tool for testing changes to our crypto stack on Alexa-top-100 websites) running in TaskCluster.

- Had first successful use of OneCRL administrative workflow

**Other Runtime Highlights**

“The culture of focusing on performance is in effect! Performance was a big part of every discussion and review.” -Andrew Overholt

- “Making my first interoperable handshake and encrypted data for Mozilla’s IETF QUIC.” -Patrick McManus

- [JavaScript classes][9] are done and fully optimized.

- [GeckoView example now being tested][9] in automation.

- Added security certificate information to GeckoView for use in PWA and Custom Tabs.

- Taught a bunch of people how to profile at the two Quantum Flow profiler office hours sessions.

Thanks everyone for a productive week!
