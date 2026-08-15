---
title: "pushlog from last night, a brief look at Try"
person: selena-deckelmann
section: by
type: blog-post
year: 2015
date: 2015-05-28
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2015/05/28/pushlog-from-last-night-a-brief-look-at-try/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# pushlog from last night, a brief look at Try

## Full text

One of the mysterious and amazing parts of Mozilla’s Release Engineering infrastructure is the [Try server](https://wiki.mozilla.org/ReleaseEngineering/TryServer), or just “Try”. This is how Firefox and FirefoxOS developers can push changes to Mozilla’s large build and test system, made up of about 3000 servers at any time. There are a couple amazing things about this — one is that [anyone can request access to push to try](https://wiki.mozilla.org/ReleaseEngineering/TryServer#Try_Server), not just core developers or Mozilla employees. It is a publicly-available system and tool. Second is that a remarkable amount of control is offered over which builds to produce and which tests are run. Each Try run could consume 300+ hours of machine time if every posible build and test option is selected.

This blog post is a brain dump from a few days of noodling and a quick review of of the [pushlog](http://hg.mozilla.org/try/pushloghtml) for Try, which shows exactly the options developers are choosing for their Try runs.

To use Try, you need to include a string of configuration that looks something like this in your topmost hg commit:

try: -b do -p emulator,emulator-jb,emulator-kk,linux32_gecko,linux64_gecko,macosx64_gecko,win32_gecko -u all -t none

That’s a recommended string for B2G developers from the [Sheriff best practices](https://wiki.mozilla.org/Sheriffing/How:To:Recommended_Try_Practices) wiki page. If you’re interested in how this works, the [code for the try syntax parser itself is here](http://hg.mozilla.org/build/buildbotcustom/file/f03682d94ea7/try_parser.py).

You can include a Try configuration string in an empty commit, or as the last part of an existing commit message. What most developers tell me they do is have a an empty commit with the Try string in it, and they remove the extra commit before merging a patch. From all the feedback I’ve read and heard, I think that’s probably what we should document on the wiki page for Try, and maybe have a secondary page with “variants” for those that want to use more advanced tooling. KISS rule seems to apply here.

If you’re a regular user of Try, you might have heard of the [high scores](https://secure.pub.build.mozilla.org/builddata/reports/reportor/daily/highscores/highscores.html) tracker. What you might not know is that there is a JSON file behind this page and it contains quite a bit of history that’s used to generate that page. You can find it if you just replace ‘.html’ with ‘.json’.

Something about the 8-bit ambiance of this page that made me think of “texts from last night”. But in reality, Try is most busy during typical Pacific Time working hours.

The high scores page also made me curious about the actual Try strings that people were using. I pulled them all out and had a look at what config options were most common.

Of the 1262 pushes documented today in that file:

- 760 used ‘-b do’ meaning both Debug and Opt builds are made. I wonder whether this should just be the default, or we should have some clear recomendations about what developers should do here.

- 366 used ‘-p all’ meaning build on 28 platforms, and produce 28 binaries. Some people might intend this, but I wonder if some other default might be more helpful. 

- 456 used ‘-u all’ meaning that all the unit tests were run. 

- 1024 used ‘-t none’ reflecting the waning use of Talos tests. 

I’m still thinking about how to use this information. I have a few ideas:

- Change the defaults for a minimal try run

- Make some commonly-used aliases for things like “build on B2G platforms” or “tests that catch a lot of problems”

- Create a dashboard that shows TopN try syntax strings

- update the parser to include more of the options documented on various wiki pages as environment variables

If you’re a regular user of Try, what would you like to see changed? Ping me in #releng, email or [tweet](http://twitter.com/selenamarie) your thoughts!

And some background on me: I’ve been working with the Release Engineering team since April 1, 2015, and most of that time so far was spent on #[buildduty](https://wiki.mozilla.org/ReleaseEngineering/Buildduty), a topic I’m planning to write a few blog posts about. I’m also having a look at planning for the Task Cluster migration (away from BuildBot), monitoring and developer environments for releng tooling. I’m also working on a zine to share at Whistler of what is going on when you push to Try. Finally, I stood up a bot for reporting alerts through AWS SNS and to be able to file #buildduty related bugzilla bugs.

My goal right now is to find ways of communicating about and sharing the important work that Release Engineering is doing. Some of that is creating tracker bugs and having meetings to spread knowlege. Some of that is documenting our infrastructure and drawing pictures of how our systems interact. A lot of it is listening and learning from the engineers who build and ship Firefox to the world.
