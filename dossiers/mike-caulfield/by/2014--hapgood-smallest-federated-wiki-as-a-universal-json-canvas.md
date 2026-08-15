---
title: "Smallest Federated Wiki as a Universal JSON Canvas"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-06-20
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/06/20/smallest-federated-wiki-as-a-universal-json-canvas/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Smallest Federated Wiki as a Universal JSON Canvas

## Full text

Watching Alan Kay talk today about early Xerox PARC days was enjoyable, but also reminded me how much good ideas need advocating. As Kay pointed out repeatedly, explaining truly new ways of doing things is hard.

People looked at the PARC stuff, and many saw a solution to this problem or that problem. But that wasn’t the point. If you walked away from PARC saying — wow, fonts! or if you walked out of the Mother of All Demos saying “I’ve been *looking* for a way to organize my grocery list” you didn’t really get it.

These technologies were not solutions to problems as much as a whole new way to think about solving problems.

Anyway, the reason that I keep hammering on about federated wiki is that I think it is one of those rarer meta-technologies. In the way it upends certain ways of thinking about the web it offers us the ability to get beyond our assumptions about how people and computers co-operate.

And yet I find myself cornered into explaining it as a new way to organize a shopping list. (And doing it).

However, I’m lucky to have a good co-analyst in this endeavor. Jon Udell [recently looked at Smallest Federated Wiki](<http://blog.jonudell.net/2014/06/12/how-thali-could-make-the-smallest-federated-wiki-even-smaller/>) and, I think, saw something like what I see. SFW borrows ideas from GitHub and re-blogging platforms (like Tumblr, for instance). But it does so NOT in the context of a specialized use, but as a _**universal canvas**_. What’s a universal canvas? The Jon Udell of today points to the [Jon Udell of 2006 to explain](<http://www.infoworld.com/d/developer-world/we-need-universal-canvas-doesnt-suck-130>):

> The most common workflows, by far, are mundane collaborations involving chunks of semi-structured data. Despite its warts, we continue to rely on e-mail with attachments as the standard enabler of these collaborations because it is a universal solvent. Our HR folks, for example, work for a different organizational unit than I do. Implementing a common collaboration system would require effort. Exploiting the e-mail common denominator requires none.
> 
> But while e-mail dissolves barriers to the exchange of data, we need another solvent to dissolve the barriers to collaborative use of that data. Applied in the right ways, that solvent creates what I like to call the “universal canvas” **—** an environment in which data and applications flow freely on the Web.

Jon, you’ll remember, literally [wrote the book on Internet groupware](<http://www.amazon.com/Practical-Internet-Groupware-Jon-Udell/dp/1565925378>). And he highlights a piece of this I don’t highlight nearly enough. SFW is a platform that allows you to apply a federated, mashup-friendly workflow to **ANYTHING**. Right now it’sthe *Smallest* Federated Wiki, and it only has a few plugins. But the plugin architecture is JSON-based and extensible.

A quick example. When I worked at Keene State we looked at using a Customer Relationship Management system to help us make sure we weren’t stepping on each other’s toes in dealing with faculty, and also to keep detailed notes on projects we were doing so that if someone had to step in when someone else was away on vacation they could.

But like so many collaborations, it fell apart. I did quite a bit of committee work and wanted my documents on faculty to keep track of nearly every email regarding decisions made, because having those emails at the ready is poitically important. Jenny, in Academic IT, on the other hand, wanted to track IT time more centrally and keep the “customer” record clean of intermittent communication. Becca, who worked in service learning, had about two hundred people off-campus she was working with that no one else wanted to see in the directory.

You’ll recognize this by now as a problem that a federated approach might be able to solve. But if SFW was just a wiki (and not a JSON canvas) you’d have to give up your structured data to use it, and that would hardly be worth the trade.

Here we don’t have to trade. You create a couple JSON plugins:

  * An email plugin that allows you to drag an email onto the Factory drop-area, and store the email in the page
  * An “customer card” plugin that allows you to enter structured data about your contacts, again as an item in the page’s story
  * A “meeting record” plugin that allows you to log future appointments and past meetings as structured, dated data. Maybe it can even accept a drag and drop from Outlook Calendar.
  * A “tickle-file” plugin that allows you to drop a “call next week” reminder on a customers page.

You build these, construct the proper view permissions and set it free. Everyone has their own site, but the records are connected across sites through naming conventions. Everyone has the power to organize their site the way they find most effective.

Better yet, since it’s a universal canvas, if we set up another federated wiki as a site for a project we are doing, we can just fork the pages on the people who are involved with that project over to our project wiki. And if we make notes on those pages in out project wiki, those notes can flow back to the CRM. Because it’s universal, see?

And all this flowing back and forth does not result in one bit of data loss. A page with that “customer card” plugin can get forked a dozen times through half a dozen projects and at the end of the line the JSON data is just as parseable as it was on day one.

“So now it’s a CRM?”

No, I know none of you are thinking that. You all realize the point is that this gives us a new way of thinking about how to think about problems. Not *just* CRM issues. *Even* CRM issues.

SFW isn’t really even a wiki to some extent. It’s more like a networked document.

I’m happy Jon sees this. I absolutely love my edtech friends and colleagues who, as Alan Levine put it, are committed to understanding SFW if only because of my excitement about it. But at some point you begin to doubt your own judgment… 😉

(Incidentally, Alan Kay also used to talk about a universal canvas, and claimed the most idiotic thing about the Internet was that your page of mixed-mode data didn’t arrive with the code you needed to interpret it. So the web became text with some hope-you-have-this-extension content. I’ll try and find that video.)
