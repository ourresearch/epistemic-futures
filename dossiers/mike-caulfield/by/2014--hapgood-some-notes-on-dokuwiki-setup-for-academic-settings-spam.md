---
title: "Some Notes on DokuWiki Setup for Academic Settings: Spam"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-04-15
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/04/15/some-notes-on-dokuwiki-setup-for-academic-settings-spam/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Some Notes on DokuWiki Setup for Academic Settings: Spam

## Full text

Still working with DokuWiki as an educational platform for faculty here at WSU Vancouver. I’ve found a couple things that are worth mentioning, Thought I’d jot them down here. This post deals with spam prevention.

The idea that Dokuwiki wikis don’t get spammed as much as MediaWiki installs is true, but trivially so. You’ll get more than enough spam to clog up the series of tubes that is your website. You’re going to have to lock down the installation.

I’ve experiemented with a couple approaches to this. Here’s some things you _don ’t_ want to do:

  * The common “must confirm email” approach is not a long term winner. Plenty of spambots now happily confirm email, get user accounts, and live happily simulated lives on your wiki discussing the latest medical devices and weight-loss drugs available.
  * Corralling freshly registered users into a “non-editing” user type is also not a great idea. I registered 8 students in my class during class for a wiki project. They then waited while I fiddled around and bumped up their privileges. It’s hard to imagine that process scaling in an academic setting.
  * Similarly, deactivating registration and doing admin panel sign-ups manually is not a pleasant activity either.
  * LDAP then? Ugh. An EXCELLENT feature of DokuWiki. But not really a great option in academia for a pilot project. You’d have to coordinate with IT (which will lead to who knows what). Might be something to explore down the road, but not as you’re getting this off the ground.
  * Visual post CAPTCHAs? Yes, this is a great way to spark a multi-million dollar ADA/Section 508 lawsuit. Avoid.

So what do you do?

  * Set read permissions to “all”. Anyone can read.
  * Set edit to whatever your default confirmed registered user is.
  * This configuration is that everyone can read, but only registered users can edit.
  * Keep the registration link/functionality up.
  * Install the Captcha plugin. Under type, chose “question”
  * Make sure that registered users *don’t* have to do the CAPTCHA. In this configuration, since all non-registered can do is read, the only place the CAPTCHA will be is on the registration form.

This option will ask the student a plain text question of your choice when they register. If they get it right, registration proceeds. If not, it bumps them back.

Here’s where a bit of discretion comes into play. You can take one of two approaches:

  * Make the question a piece of cultural knowledge that students should know — e.g. the name of the dining commons.
  * Make the question “Access Code?” and have them supply an access code furnished by you or the prof.

As I went through “cultural knowledge” access codes, I started to realize how fraught that process was. I can maybe talk more about that later. I also realized what I really wanted was a semi-automated process for WSU staff and faculty not available to outsiders. I decided on the access code with a twist.

Here’s how it works. If you mail vc.wiki.access@gmail.com from a WSU email account, an autoresponder will send you back the code. If you mail it from a non-WSU account, you get nothing. I do this through setting up an autoresponder on that Gmail address with the code in it, but routing everything not from @xxxx.wsu.edu directly to deletion.

So there you go, that’s my setup. Maybe in a few days I’ll talk about my depressing struggle with various markdown plugins. Or requests… I’ll take requests too.
