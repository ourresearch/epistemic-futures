---
title: "[berkman] Open Source at Microsoft"
person: david-weinberger
section: by
type: blog-post
year: 2008
date: 2008-11-11
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2008/11/11/berkman-open-source-at-microsoft/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [berkman] Open Source at Microsoft

## Full text

Bryan Kirschner (Dir of Open Source Strategy) and Mario Madden (Open Source Licensing Counsel) at Microsoft are giving a Berkman Tuesday lunch talk on Open Source and Microsoft. [NOTE: I am live-blogging, typing too fast, missing things, getting things wrong, etc.]

They start with three framing positions: 1. Open source has changed the info-communications landscape. It’s “neither a fad nor a magic bullet” [missed the attribution] 2. It brings an opportunity for Microsoft, open source developers, and ICT customers. 3. It’s not any harder or easier to realize this potential, compared to other opportunities (e.g., cloud computing).

In 2004, Msft submitted two licenses to the Open Source Initiative. Now there are 500. There are at least 80,000 Open Source apps that run on Windows. Microsoft is virtualizing Linux on Windows and vice versa, and Silverlight is becoming Moonlight (= a Linux version).

Why is Msft doing this?

1. Motivation. What motivates OS developers? (From Karim Lakhani, who is in the room.) They’re motivated by creativity and learning, economic opportunity, and solving a problem.

2. Commercialization. Some of OS is money-driven, while some is community-driven. “At the end of the day, it’s about value-for-cost and solving a customer’s problem.”

There’s a “world of choice” these days. You use the best tool for the job. Mix and match. E.g., they want Windows to be a great platform for OS apps, including for PHP. So, Windows is working with Zen (commercial PHP company) and the PHP community. If your company wants single-sign-on; Msft has Active Directory that does that, including for php aps. Then, if you want to use cloud computing (Windows Azure), you can use it and it works with Active Directory. Then you could have OpenID and Ruby apps running on Linux. Then you might want to use virtualization to rapidly move apps across hardware, and you could then use OpenPegasus to do cross-platform systems management, contributing back to the Pegasus project. “At the application layer, it really makes sense to strive for openness.”

There’s a human relationship and emotions in the OS community, Bryan says. It’s inspirational. Microsoft wants to comingle, cooperate and co-exist.

Q: You touted collaboration with Novell. Many are not happy with that deal. Some people at Novell quit. The Linux kernel community would be a tougher community. They haven’t been happy about joining forces with you. Do you have any plans to bury the hatchet? E.g., Linus Torvalds is unhappy with Msft’s stance on patents…

A: I wouldn’t hold up Novell as a great example. Our customers, especially our large customers, like it a lot, though. It makes commercial sense, although it doesn’t necessarily make everyone feel happy.

A: [mario] The legal team’s job is to help the team navigate the shoals. We did the best we could in the Novell deal.

A: [bryan] We have an active partnership with Samba. Both sides are happy about this.

Q: I’m a European lawyer. Microsoft’s reaction to the European Court’s decision showed no sign of openness? How do you address the abuse that was found and the open attitude you’re expressing today?

A: [bryan] I’m not a lawyer. The question for me is how do you meet the needs of your customers? The overwhelming body of evidence leads you to openness. We will continue to develop .Net. But it’s not zero sum. We also have support php. The Windows media team wrote a plugin so Windows Media Player would work on Firefox. There have been 6 million downloads, so that’s great.

A: [karim] There’s a lag between court decisions and how the company thinks about it.

Q: My point was that you might have saved 500M euros if you had been more open…

Q: Once sw is fully developed, you’re half done. It still needs quality assurance. How do you assure open source software is of high quality? And how do you know it wasn’t stolen from an open source app?

A: [mario] When code is brought in, it’s up to the engineering groups to do the QA. Legally, OS software is just third party code. We brought in 500M lines of code last year. We scan it. A lot of it was Open Source.

A: [karim] Two studies have compared the quality of code from Open Source vs. commercial and found no difference, except perhaps OS is slightly higher quality because the QA is continuous.

A: [bryan] We’re a platinum sponsor of the Apache Foundation. They have overhead. It makes it easier to deal with them if they’re not under terrible financial stress.

A: [mario] When it comes to OS, we’re driven by business purposes. Can we decrease development costs?

Q: [me] What’s the business case that you see for contributing to OS, as well as enabling Windows to work well with OS? How much are you contributing?

A: [bryan] We contribute in three ways. 1. Product strategy. E.g., contribute to php to make it work better with SQL Server. 2. Does it actually make sense for your product to take an OS or hybrid strategy? E.g., Class server is curriculum management system. It competes with OS. It didn’t make sense to compete, so now it’s an OS product. 3. Having more developers creating more code is a good thing. It’s pie-expanding. E.g., we have XNA libraries for developing games. There are hundreds of XNA projects that are open source now.

Q: [me] Are 500 contributions a lot? Compared to the number of patents? Products?

A: We’ll measure success when every product group considers open source.

Q: [karim] IBM says they have 1,000 developers working on Linux, etc. Do you have any number you can point to that’s similar?

A: No.

Q: Has OS affected how stuff gets done inside?

A: Inside the company, we are not the Borg. Every product group has a lot of autonomy. Agile groups. You also have some 3-year-product-plan projects. Increasingly you’ll see a more blended model.

A: [mario] We have 30,000 developers. It’s hard to know, on the IP, what everyone is doing.

A: [bryan] You’ll see a company-wide statement from the company that we understand the world is heterogeneous, we respect the contributions open source has made, and we’re committed to greater openness. I’ll quote Heidegger: Fear is not knowing what to do. The Windows-Linux oppositional framework in 1998 took the public imagination. We formally responded with a site in 2007, so no one will accuse us of acting precipitously :)

Q: When will Steve Ballmer start putting out the OS msg? He has a reputation for being confrontational.

A: [bryan] He’s a strong, opinionated leader. But you’ve already seen Steve talk about the benefits of supporting open source. Inside Msft, the open source group always talks in terms of what makes sense for business.

Q: This has implications for DC policy positions. I.e., very strict IP enforcement.

A: [mario] We may disagree about strict IP; we support patent reform, for example. But we see our business as about IP. We’ll always support IP and IP rights.

Q: Chances are we’ll find out that the new Redmond Congressperson will be a former Microsoft manager. Since Msft employees have funded about a third of her campaign, when your lobbyists are calling her up, will you be asking to support Open Source?

A: [mario] Fascinating question, and I’m sure not going to comment :)

A: [bryan] We don’t want anyone fighting Open Source. We don’t think it makes business sense.

Q: [karim] If we’re back to big iron — Google is a server farm company — how do we think about the role of open source?

A: [bryan] It changes the dynamics. Clouds and server farms open up a lot more space.

[me[ What about OOXML vs. ODF? Why did you push OOXML as a doc format after we already had adopted ODF? Is that typical of what you mean by openness?

A: [bryan] Open doc formats are really important. I don’t see doc standards as a zero sum game. So being able to understand the doc through a published set of docs doesn’t seem exclusive to me.

Karim concludes the session by pointing out how contentious this topic would have been just five years. “The presence of Mario and Bryan here is a sign of success.” [Tags: berkman microsoft open_source ]
