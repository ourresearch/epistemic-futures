---
title: "The FBI blunder on phone encryption, explained"
person: henry-farrell
section: by
type: blog-post
year: 2018
date: 2018-05-30
venue: "The Monkey Cage (The Washington Post)"
authors: "Henry Farrell"
source_url: https://goodauthority.org/news/the-fbi-blunder-on-phone-encryption-explained/
retrieved: 2026-08-13
content: full-text
notes: "Post from The Monkey Cage, retrieved from the Good Authority archive (goodauthority.org), which hosts the complete Monkey Cage back catalogue; themonkeycage.org itself is offline. Text spot-verified against Wayback captures of the original themonkeycage.org pages (100% word coverage on 3 checks). Legacy Textile link markup surviving the WordPress migration was converted to markdown links."
---

# The FBI blunder on phone encryption, explained

## Full text

Yale University Press

The FBI has been arguing for years that the approach of Apple and other companies that strongly encrypt phones is a big problem for law enforcement, which cannot get access to information it needs to catch criminals. Some days ago, these claims led to a big controversy when it turned out the FBI had been accidentally exaggerating the number of phones it couldn’t open for years. Susan Landau is a renowned cryptographer and the author of the recent book “[Listening In: Cybersecurity in an Insecure Age](https://amzn.to/2IXHxnd),” which looks at the argument between the FBI and the cryptographic community.  I asked her about her book and how to get law enforcement to a higher level of technological sophistication.

HF: The FBI has been claiming for years that it has thousands of encrypted phones that it can’t get access to and that might have vital information. Now it turns out that it has been massively overreporting the number of problem phones. How could this have happened?

SL: Records of the devices were in three different databases. The FBI wrote a program to tally the number of encrypted devices law enforcement couldn’t unlock. But the software apparently counted certain devices several times. It’s not news that the FBI has been having trouble with computer software. But given the importance the FBI has given to this issue, making an error of this magnitude is really hard to fathom. The Post [reported](https://www.washingtonpost.com/world/national-security/fbi-repeatedly-overstated-encryption-threat-figures-to-congress-public/2018/05/22/5b68ae90-5dce-11e8-a4a4-c070ef53f315_story.html?utm_term=.c31df080fa6d) that the FBI ultimately expects to find only one to two thousand locked devices it can’t open — rather than the 7,800 FBI Director Christopher Wray had [repeatedly](https://www.fbi.gov/news/speeches/raising-our-game-cyber-security-in-an-age-of-digital-transformation?) [spoken](https://www.documentcloud.org/documents/4404076-03-07-18-20-Bccs-20-Press-20-Version-282-29.html) of.

HF: Your book describes how the FBI and other law enforcement agencies claim that surely “smart people” can figure out some way to meet the demands of law enforcement while allowing people to use strong encryption to maintain their security and privacy. You and most other technical experts on cryptography are skeptical. Why?

SL: It’s flattering to be told you’re smart, but flattery doesn’t suddenly make an insoluble problem solvable. Law enforcement wants Silicon Valley to design encryption systems so that, when legally authorized, they can access encrypted communications and locked devices. That sounds reasonable until you look at the details of how an exceptional access system would work. My colleague [Matt Blaze](https://www.seas.upenn.edu/directory/profile.php?ID=8) has [likened](https://www.youtube.com/watch?v=zsjZ2r9Ygzw) this to arguing that if you can land a person on the moon, then you can land someone on the sun — and bring them back safely.

Complex systems go wrong in many ways. We build software out of different components. Often vulnerabilities occur at their interfaces (there are different assumptions about how each piece works, and these often fail to match). That problem was behind the recent [security failure](https://www.krackattacks.com/) of the [WPA protocol](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access), a critical mechanism for securing WiFi communications. The protocol had been used for 14 years and was believed to be secure (aspects had even been mathematically proved correct). But researchers discovered that interactions between different parts of the protocol enabled decrypting communications, allowing hackers to eavesdrop on user log-in credentials.

The problems with an exceptional access system are complexity and scale. Such a system would have to work across billions of devices, with varied architectures and security systems, and different ways of handling updates. The system should be flexibly designed to permit new technologies that weren’t previously considered — otherwise it would impinge on innovation, which would not be healthy for the U.S. Meanwhile, there’s authentication. Finally, there are [over 15,000](https://www.bjs.gov/content/pub/pdf/lpd13ppp.pdf) sheriff and police departments in the U.S. An exceptional access system should be able to securely authenticate all of them. And all that’s not considering the international issue, where phones cross borders and law enforcement abroad would seek the same access.

HF: Your book talks about some of the problems of “key escrow,” including how it would effectively rule out “forward secrecy.” What are key escrow and forward secrecy, and why should people be concerned about them?

SL: In the 1990s, the U.S. government introduced the Clipper chip, which had 80-bit cryptography and keys “escrowed” — stored — with two federal agencies. The system was a total market failure. U.S. businesses were not interested in encryption with the U.S. government holding the keys; neither were foreign companies or governments. And, in general, key escrow solutions are problematic from a security vantage point: Whoever holds the keys is a rich, ripe target.

Key escrow also prevents the use of forward secrecy, a security technique that employs a new key for each communication session. With forward secrecy, there’s no long-term key that, once discovered, can be used to decrypt past communications. Instead, the communication is destroyed at the end of the session. This would have been useful for [John Podesta](https://en.wikipedia.org/wiki/Podesta_emails) — and for [Sony executives](https://www.vanityfair.com/hollywood/2015/02/sony-hacking-seth-rogen-evan-goldberg).

In this context, it’s worth mentioning Apple’s solution for securing the iPhone, which doesn’t keep the encryption key on the phone — or at the company. It’s clever; there’s nothing for a hacker to steal. Instead an attacker has to try possible keys in order to get in. And Apple has designed the system to erase the phone’s data if there are 10 failed log-ins. That model is a great design for security. It also makes the phone useful for [second-factor authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication#Mobile-phone_two-step_authentication), the use of which strengthens the security of online accounts. The Android OS uses other ways of securing the device.

HF: You describe how other law enforcement agencies, such as the Manhattan District Attorney’s Office, have been able to hire people with real technical skill. What more could the FBI be doing to understand “the nitty-gritty details of how modern communication technologies work”?

SL: Let’s return to the software error that the FBI made when counting locked devices. The bureau has long [had](http://www.washingtonpost.com/wp-dyn/content/article/2006/08/17/AR2006081701485.html) a technology problem. Now there are savvy computer criminal investigators in law enforcement — just not enough of them. I’ve heard senior law-enforcement investigators from various computer crime divisions complain when communications metadata comes in different formats from different providers — an easy problem to fix from a technological vantage point — or question whether software has more than a single vulnerability to use for [lawful hacking](http://scholarlycommons.law.northwestern.edu/cgi/viewcontent.cgi?article=1209&context=njtip) (yes, many). The lack of technical expertise is really problematic. The Manhattan District Attorney’s Office estimates over 25 percent of its annual cases deal with digital evidence. In the digital age, technical understanding is needed at all levels of the bureau.

The FBI needs to change its view in what’s needed in investigative skills — and also needs to vastly increase sharing of technological capabilities between federal and state and local investigators, many of whose agencies are too small to develop skill in-house. Developing these capabilities is complicated — there’s lots of competition — and law enforcement will need help till it develops the expertise. But we don’t have a choice on this; even without encryption, law enforcement needs to be better at working with digital evidence.

This article is one in a series supported by the MacArthur Foundation Research Network on Opening Governance that seeks to work collaboratively to increase our understanding of how to design more effective and legitimate democratic institutions using new technologies and new methods. Neither the MacArthur Foundation nor the Network is responsible for the article’s specific content. Other posts can be found [here](https://www.washingtonpost.com/news/monkey-cage/wp/category/macarthur-network/?utm_term=.116dfa4a6263).
