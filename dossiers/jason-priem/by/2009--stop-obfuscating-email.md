---
title: "Obfuscate no more: why your email address should go au naturale"
person: jason-priem
section: by
type: blog-post
year: 2009
date: 2009-05
venue: "jasonpriem.org (personal blog)"
authors: "Jason Priem"
source_url: https://web.archive.org/web/20150111175201/http://jasonpriem.org/2009/05/stop-obfuscating-email/
retrieved: 2026-08-13
content: full-text
notes: "Personal blog, defunct; retrieved from the Internet Archive Wayback Machine. Original URL: http://jasonpriem.org/2009/05/stop-obfuscating-email/"
---

# Obfuscate no more: why your email address should go au naturale

## Full text

[![screenshot of the obfuscation decoder demo](http://jasonpriem.com/wp-content/uploads/2009/05/obfuscation-decoder.png "screenshot of the obfuscation decoder demo")](http://jasonpriem.com/wp-content/uploads/2009/05/obfuscation-decoder.png)I was recently redesigning my [homepage](http://jasonpriem.com), and I wanted to include my email address.  I knew that only n00b looz3rz display their addy in plain site for spambots to harvest, so I applied a little light obfuscation,  like they do on [php.net](http://www.php.net) and million other sites: “myname at jasonpriem dot com.”

“Take that, spammer scum!” I thought as I finished, basking in my newfound invulnerability to the v1@gr@-hawking vermin.  After all, if lots of people use [address munging](http://en.wikipedia.org/wiki/Address_munging), it must work, right?

Right?

Darn it, now I’ve got to start reading about it.  So I did.  And after a few hours of reading blogs and writing code, I am now an Expert With Advice (hey, this is the internet).  And the advice is this:

**Stop trying to obfuscate your email address.  Stop now.**

I’ve got two reasons (and for a few more, [some](http://floatingsun.net/articles/on-email-obfuscation/) [other](http://www.divineaphasia.com/words/email-obfuscation-is-silly.html) [folks](http://typewriting.org/2006/06/19/Email_Obfuscation_Helps_Spammers/#comment-4549) have blogged about this, too).  First, the more theoretical one:

### Spam is a problem for you–obfuscation makes it a problem for your users.

After all, they’re the ones who are going to have to do all the de-munging.  Are they always going to notice that they have to remove “.invalid” from the end?  Do they all know that the English “at” means “@”?   Do they have time to edit text in their address lines?   Address munging is fundamentally inelegant, because it intentionally works against clarity.

People have been making this argument for a very [long](http://www.interhack.net/pubs/munging-harmful/) [time](http://www.faqs.org/faqs/net-abuse-faq/munging-address/). It’s particularly relevant nowadays, though, because of the growing promise of the [semantic web](http://semanticweb.org/wiki/Main_Page).  We *want* data to be machine readable, because then we can do cool stuff with it.  [FOAF](http://en.wikipedia.org/wiki/FOAF_(software)) and the [hCard](http://microformats.org/wiki/hcard) microformat are pretty pointless if they don’t have real email addresses to work with.  “Hide the data from the machines” is a good strategy for fighting [Skynet](http://en.wikipedia.org/wiki/Skynet_(fictional)), but not for the future of the web.  Ok, reason two:

### Address munging just doesn’t work.

It can’t.  It’s [putting glasses on Superman](http://en.wikipedia.org/wiki/Mystery_Men#Cultural_references).  Although [in theory](http://tools.ietf.org/html/rfc2822) a valid email can be pretty hard to identify, [in practice](http://www.regular-expressions.info/email.html), emails addresses use a very limited vocabulary–and computers are good at identifying limited vocabularies.  Don’t forget, everyone has been using the same old \[at\] and “dot” tricks for *decades*–this is [security through obscurity](http://en.wikipedia.org/wiki/Security_through_obscurity) at its very worst.

But [don’t take my word for it](http://en.wikipedia.org/wiki/Reading_Rainbow#Show_details).  I took a couple hours and worked up a demo [email obfuscation decoder](http://jasonpriem.com/obfuscation-decoder/) that breaks the vast majority of text-based obfuscations; it’s also got an input field for you to test out your own munges (some other people have built [similar](http://dave78.com/misc/harv_test.html) [demos](http://www.openjs.com/scripts/regexp/email_decrypter.php), too).  It’s not perfect, but it correctly decodes most obfuscations–and remember that this is a novice programmer, working for an afternoon.  It’s that easy. Supporters of obfuscation argue that spammers will go after the low-hanging fruit; folks, text-based obfuscation *is* the low-hanging fruit.

Now, the Alert Reader has by this time noticed that I’ve limited my critique to text-based munging.  “What about more sophisticated methods,” the Alert Reader now asks?  “What about using an image, or CSS, or Javascript to hide addresses?”  Good questions, Alert Reader; you are very alert.  Alright, let’s take a quick look at these, too:

### Images

There’s not really much I can say about this one, save this: making content completely opaque to visually-impaired users simply shouldn’t be an option. And of course, spammers still can OCR your images.

### CSS

Obviously, something like  `foo@bar<span style=”display:none”>NULL</span>.com` is silly; the spambot can filter out “display:none” spans pretty easily, or even just discard everything in a span.  `<span class=’a’>foo</span><span class=’b’>bar</span>@“<span class=’c’>foo</span><span class=’d’>bar</span>.com` at least requires the bot to open your stylesheet to see which spans are hidden.  But remember, your server will happily dish out your easily-parsed css to anyone who asks for it; this is not a good place to hide secrets.

### Javascript

There are [too many](http://www.google.com/search?q=javascript+obfuscate+%22email%20address%22) js methods to cover in any detail here.  Some are better than [others](http://blog.macromates.com/2007/obfuscating-emails-revisited/); a few try to [degrade gracefully](http://pipwerks.com/journal/2009/02/01/obfuscating-email-addresses-revisited/) for users without Javascript support.  All of them, though, share the same weakness as CSS: everyone can read your Javascript.  And you certainly don’t need a browser to run it; there are [lots of JS interpreters](http://hublog.hubmed.org/archives/001847.html) that are more than happy to run on a spammer’s server.

Sure, you can get pretty clever with this technique (I particularly like the idea of decoding not on the onload event, but on a click event), but you can’t change the fact that ultimately the bad guys can do everything with your code that a browser does–and eventually, they will.

Now, I’ll admit that images, CSS, and Javascript approaches are more effective than text-based ones.  All of them (when done properly) require the spammer to pay for more bandwidth and/or processor cycles.  But they all also inconvenience some or all of your users, and none of them are compatible with the sementic web.  They all give you false sense of security, and they’re ugly, hackish solutions. True, some obfuscations have [performed well](http://techblog.tilllate.com/2008/07/20/ten-methods-to-obfuscate-e-mail-addresses-compared/) [empirically](http://www.cdt.org/speech/spam/030319spamreport.shtml)–but keep in mind that these (pretty informal) experiments are years old.  As more people have adopted these measures, be sure that more spammers are spending the time to counter them, as well.

Now, I can’t go so far as to condemn anyone who obfuscates an address; I get that spam is a pain, and filters aren’t perfect.  Sometimes an ugly, hackish solution is the only way.  But I’m suggesting that you think twice before you give in to the spammers and obfuscate, especially given the relative ineffectiveness of many commonly-used methods.  The Web reaches its full promise when information is made easier to find, not harder.
