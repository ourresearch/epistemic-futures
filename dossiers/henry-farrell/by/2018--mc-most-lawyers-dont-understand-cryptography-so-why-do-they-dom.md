---
title: "Most lawyers don’t understand cryptography. So why do they dominate tech policy debates?"
person: henry-farrell
section: by
type: blog-post
year: 2018
date: 2018-03-15
venue: "The Monkey Cage (The Washington Post)"
authors: "Henry Farrell"
source_url: https://goodauthority.org/news/most-lawyers-dont-understand-cryptography-so-why-do-they-dominate-tech-policy-debates/
retrieved: 2026-08-13
content: full-text
notes: "Post from The Monkey Cage, retrieved from the Good Authority archive (goodauthority.org), which hosts the complete Monkey Cage back catalogue; themonkeycage.org itself is offline. Text spot-verified against Wayback captures of the original themonkeycage.org pages (100% word coverage on 3 checks). Legacy Textile link markup surviving the WordPress migration was converted to markdown links."
---

# Most lawyers don’t understand cryptography. So why do they dominate tech policy debates?

## Full text

Fort Meade gate next to the National Security Agency. (Jose Luis Magana/AP)

On Wednesday, the Trump administration appointed the renowned computer science professor Ed Felten to the Privacy and Civil Liberties Oversight Board (PCLOB). This is the first time that a [nonlawyer has been appointed to the board](https://www.lawfareblog.com/white-house-pclob-nominations-pleasant-surprise), even though it has oversight responsibilities for a variety of complex technological issues.

The bias toward lawyers reflects a more general problem in the U.S. government. Lawyers dominate debates over privacy and technology policy, and people who have a deep understanding of the technological questions surrounding complex questions, such as cryptography, are often shut out of the argument.

Some days ago, I interviewed Timothy Edgar, who served as the intelligence community’s first officer on civil liberties and is the author of the book “[Beyond Snowden: Privacy, Mass Surveillance, and the Struggle to Reform the NSA](https://www.amazon.com/Beyond-Snowden-Privacy-Surveillance-Struggle-ebook/dp/B01NAXEPQS/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=),” about the reasons government policymaking isn’t as open to technological expertise as it ought to be.

The U.S. policy debate over surveillance mostly overlooks the ways in which cryptography could assure the privacy of data collected by the NSA and other entities. What broad benefits does cryptography offer?

When people think about cryptography, they mostly think about encrypting data and communications, like emails or instant messages, but modern cryptography offers many more capabilities. Today’s debate over surveillance ignores some of the ways these capabilities might allow the public to have the best of both worlds: robust intelligence collection with ironclad, mathematically rigorous privacy guarantees.

The problem is that many of these capabilities are counterintuitive. They seem like magic to those who are not aware of how cryptography has advanced over the past two decades. Because policymakers may not be aware of these advances, they view intelligence collection and privacy as a zero-sum game: more of one necessarily requires less of the other — but that’s a false trade-off.

Which specific techniques have cryptographers developed that could be applied to collected data?

Probably the most promising technology for ensuring the privacy of data that intelligence agencies are collecting is called [encrypted search](https://cs.brown.edu/~seny/pubs/metacrypt.pdf), something that my colleague at Brown, Prof. Seny Kamara, has helped pioneer. Imagine a large database that an intelligence agency like the NSA would like to query. The vast, vast majority of the data is irrelevant: It belongs to people that intelligence analysts should not be able to monitor. Of course, the agency could formulate queries and submit them to whoever owns the database, perhaps a telecommunications company or a digital services provider. But what if the agency is worried that its queries will reveal too much about its sensitive operations, and is not willing to take the chance that this information will leak?

Without encrypted search, the scenario I just outlined is a classic trade-off. Of course, the intelligence agency could simply forgo its queries, but if the stakes are too high — maybe the agency is trying to prevent a devastating terrorist attack — it could decide instead to engage in a highly intrusive intelligence practice called bulk collection. Bulk collection means the agency collects the entire database, including all the irrelevant information, hopefully with legal or policy safeguards to prevent abuse. Following the Snowden revelations in 2013, bulk collection of domestic data [was reformed](https://www.lawfareblog.com/lawfare-podcast-timothy-edgar-mass-surveillance-after-snowden), but it remains an option when the NSA collects data outside the United States, even if that data includes communications with Americans.

Encrypted search allows us to do much better than this. The entire database is encrypted in a way that allows the intelligence agency to pose specific queries, which are also encrypted. Policymakers can decide what kinds of queries are appropriate. There are mathematically rigorous guarantees that ensure 1) the intelligence agency may only pose permissible queries, 2) the agency only receives the answers to those queries and does not receive any other data, and 3) the company will not learn what queries the agency has posed, offering the agency security for its operations.

Why is it that lawyers, rather than technologists, seem to dominate U.S. policy debates over technically complex subjects like surveillance and cryptography?

Lawyers have been dominating debates in the United States since at least the days when the French writer Alexis de Tocqueville wrote “[Democracy in America](https://read.amazon.com/kp/embed?asin=B008H4LC6W&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_MYOQAb5TC4W53&tag=thewaspos09-20)” in 1831. De Tocqueville describes lawyers as [occupying a place in American society](http://scholarship.law.marquette.edu/cgi/viewcontent.cgi?article=2503&context=mulr) similar to the aristocracies of Europe. If we examine just how many members of Congress, senior government officials and even business leaders are drawn from the legal profession today, it appears that little has changed in this regard in the subsequent two centuries. Lawyers tend to be verbal and overconfident. Computer scientists are more prone to be reserved and even introverted.

The failure of lawyers and technologists to communicate well led the NSA to [make some serious mistakes](https://fas.org/irp/congress/2013_hr/092613edgar.pdf) in the domestic bulk collection programs it was running until 2015, when they were reformed in the aftermath of the Snowden revelations. It has also, unfortunately, impeded the deployment of technologically based alternatives to intrusive intelligence programs.

Is this changing, and if it is changing, is it changing for the better or the worse?

I certainly hope it is. In 2015, a committee of the National Research Council that was asked to look at using technology as an alternative to bulk collection [issued a report](https://www.nap.edu/catalog/19414/bulk-collection-of-signals-intelligence-technical-options) that offered some helpful recommendations. Unfortunately, the report did not adequately address some of the more promising technology that can offer us the best of both worlds. With the surveillance debate continuing to mature, I think the time is ripe for policymakers, lawyers and computer scientists to look again at ways we can use advances in cryptography to ensure robust intelligence collection with rock-solid privacy guarantees.

This article is one in a series supported by the MacArthur Foundation Research Network on Opening Governance that seeks to work collaboratively to increase our understanding of how to design more effective and legitimate democratic institutions using new technologies and new methods. Neither the MacArthur Foundation nor the Network is responsible for the article’s specific content. Other posts can be found [here](https://www.washingtonpost.com/news/monkey-cage/wp/category/macarthur-network/?utm_term=.116dfa4a6263).
