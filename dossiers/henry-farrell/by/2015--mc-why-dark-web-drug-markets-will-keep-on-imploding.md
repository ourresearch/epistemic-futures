---
title: "Why 'Dark Web' drug markets will keep on imploding"
person: henry-farrell
section: by
type: blog-post
year: 2015
date: 2015-03-19
venue: "The Monkey Cage (The Washington Post)"
authors: "Henry Farrell"
source_url: https://goodauthority.org/news/why-dark-web-drug-markets-will-keep-on-imploding/
retrieved: 2026-08-13
content: full-text
notes: "Post from The Monkey Cage, retrieved from the Good Authority archive (goodauthority.org), which hosts the complete Monkey Cage back catalogue; themonkeycage.org itself is offline. Text spot-verified against Wayback captures of the original themonkeycage.org pages (100% word coverage on 3 checks). Legacy Textile link markup surviving the WordPress migration was converted to markdown links. The Good Authority archive carries this post twice (duplicate import under slug 'why-dark-web-drug-markets-will-keep-on-imploding-2'); kept once."
---

# Why ‘Dark Web’ drug markets will keep on imploding

## Full text

(Daniel Acker/Bloomberg)

A couple of months after the conviction of Ross Ulbricht, the “Dread Pirate Roberts” behind the creation of the Silk Road online drug market, another online drug market, “Evolution” has imploded. Like the Silk Road, Evolution used “Tor Hidden Services,” to hide the true location of their Web site, providing the owners, and drug buyers and sellers with some degree of anonymity. But this Web site didn’t go down thanks to the feds. It went down because its owners took it down.

So what happened?

The anonymous owners of the Evolution drug market pulled what’s called an ‘exit scam.’ They pretended that the site was having technical difficulties, making it difficult for users of the market to withdraw funds. Then they pulled the site down and absconded with the money. Some people are [claiming](https://krebsonsecurity.com/2015/03/dark-webs-evolution-market-vanishes/comment-page-1/#comment-373010) that they made off with around $12 million – but it’s hard to be sure how much money they had (especially since the money they stole is Bitcoin, an artificial currency which has a wildly fluctuating exchange rate with regular currencies).

How did they get away with it?

If you want a detailed account of how drug markets work on the “Dark Web” (the archipelago of sites hidden behind Tor’s network), I’ve already written one [here](http://aeon.co/magazine/technology/on-the-high-seas-of-the-hidden-internet/) for Aeon magazine. But the principle is simple. Drug dealers and drug buyers are not noted for being particularly trustworthy people. They also want to avoid the attention of law enforcement. The “Dark Web” allows them to trade anonymously with each other. But it also means that it’s even harder for them to trust each other, exactly because the trade is anonymous (if you get ripped off by someone with an untraceable pseudonym, it’s hard to retaliate against them).

This has created a market for trustworthy intermediaries. Drug markets, such as Evolution and Silk Road and Agora (which is still in existence), provide an online site where buyers and sellers can meet each other. They also provide information (a little like eBay’s rating system) that allow buyers to evaluate the quality of sellers. But most importantly, they provide an escrow service, allowing buyers to put money into escrow, and only release it to sellers when they get their drugs through the mail. This doesn’t perfectly guarantee trustworthiness, and well-established sellers can demand that buyers ‘settle early’ as a condition of trade. But it certainly helps.

The obvious problem is that this only works if the owners of the drug market, who operate the escrow service, are themselves trustworthy. If they are not trustworthy, they can take all of the money in escrow and run. That’s what appears to have happened at Evolution.

Can online drug dealers avoid the problem of untrustworthy site owners?

In theory yes, but in practice it’s hard. It’s possible to use a different escrow system with Bitcoin called [Multi Party Signature](https://krebsonsecurity.com/2015/03/dark-webs-evolution-market-vanishes/comment-page-1/#comment-373010), which would prevent the market owners from taking the money and running, unless they colluded with either the buyers or the sellers. Evolution reportedly had some version of Multi Party Signature although it’s not clear how well it worked. However, this is much more complicated and tedious than ordinary escrow, and also carries other risks. It is publicly visible, and could serve as an enormous clue to law enforcement that a criminal transaction is taking place — there are few legitimate online transactions where people distrust each other so much that they have to rely on such a complicated system. People think of Bitcoin as a truly anonymous currency but it is not – all transactions are recorded on a publicly shared ‘blockchain’ making it possible to track many transactions with some luck and ingenuity. Using Multi Party Signature would help law enforcement identify dubious transactions.

So what happens next?

This is not the first online drug market to evaporate when the founders decided to split with the money of their outraged customers. But there’s some social scientific reason to suspect that it will not be the last. Consider the incentives of the people running the market. Drug dealers are not notable for altruism; they’re mostly in it for the money. The fundamental question they face is the following. Is it more profitable to keep running the market, and taking a steady percentage from the deals that everyone is making? Or is it more profitable to collapse the market and grab what they can? Basic game theory would suggest that their decision is going to depend on the ratio between long term expected profits (discounted over time) and the short term benefits of cheating. If they get a high enough long term payoff, they will stay honest and keep the market running. If the long term payoff is outweighed by the short term benefits of cheating, they’re going to take the money and run.

What I suspect is happening is that the perceived long run vs. short run tradeoffs are changing after the arrest and conviction of Ulbricht. Law enforcement authorities are using informants to penetrate the markets, and may have [exploited](http://www.slate.com/articles/technology/future_tense/2014/12/silk_road_2_0_arrests_operation_onymous_did_the_fbi_break_tor.single.html) short term vulnerabilities to de-anonymize users of the Tor network. This has consequences for the perceived value of building drug markets for the long haul. If you think that law enforcement has a good chance of breaking your site’s security, and perhaps catching you and convicting you, then you aren’t going to place a high value on long term profits, since there’s a very good chance that you won’t have any. If you’re rational and selfish, you’ll instead be more likely to get out while the going is good, taking as much money with you as you can.

This suggests that law enforcement’s job is somewhat easier than many think it is. To be effective, law enforcement agencies don’t have to break all the drug markets. They just have to break enough of them that other market owners believe that the risks are too high to be tolerable, so that they’re tempted to cheat their users and abscond with the proceeds. There may be other possible ways that drug market owners could try to insulate themselves (e.g. by operating from countries that are unlikely to extradite people to the United States or elsewhere), but it may be hard to do this (it’s surprisingly easy to get state protection in some countries if you are just ripping off the credit cards of rich Westerners, but rather harder if you are a self-avowed drug dealer).

As many researchers (myself included) have argued, online drug markets rely on quite fragile trust relations. As law enforcement authorities learn better how to disrupt trust, they can enormously increase the impact of their enforcement efforts.
