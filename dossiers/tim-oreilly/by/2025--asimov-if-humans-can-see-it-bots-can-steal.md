---
title: "If Humans Can See It, Bots Can Steal It"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-11-06
venue: "Asimov’s Addendum"
authors: "Isobel Moure, Ilan Strauss, Tim O'Reilly"
source_url: https://asimovaddendum.substack.com/p/if-humans-can-see-it-bots-can-steal
retrieved: 2026-08-13
content: full-text
notes: "Subtitle: “New architectures for content in the age of AI”. Asimov’s Addendum, the Substack of Tim O’Reilly and Ilan Strauss on AI commercialization risks and governance; published CC BY 4.0. Retrieved from the free public post page."
---

# If Humans Can See It, Bots Can Steal It

## Full text

[](<https://substackcdn.com/image/fetch/$s_!3ez2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11119185-5333-45f7-884c-2143343d4789_2560x1778.png>)Source: [Hanna Barakat & Archival Images of AI + AIxDESIGN](<https://betterimagesofai.org>)

I (Isobel) had the pleasure of presenting our AI Disclosures Project [research](<https://www.ssrc.org/programs/ai-disclosures-project/research/>) on AI access violations and attribution as part of a workshop at the [FIPP World Media Congress](<https://fippcongress.com/>) last week in Madrid. The attendees were mainly publishers who shared the same concern: _what is the world of publishing going to look like in the new age of generative AI_? There was an urgency in the air as publishers’ existing business model is under attack from AI chatbots and their scrapers.  
  
Many of the vendors at the conference purported to have the answer – for a fee. Cut costs using this AI drafting tool, use AI-generated keywords to optimize SEO (or [GEO](<https://en.wikipedia.org/wiki/Generative_engine_optimization>)?), track bots on your website, embed a proprietary chatbot on your site trained on your own data, the list goes on.

An executive from OpenAI got on the main stage and reassured anxious audience members unequivocally that ChatGPT would not circumvent paywalls. Of course, even a simple test can show you that this isn’t true. ChatGPT seemed to be somewhat respectful to mainstream publishers – when I probed it to summarize an article from _The Information_(a completely paywalled outlet), [it only used secondary sources](<https://chatgpt.com/share/690233e3-17ac-8002-a855-49905a629633>) that had quoted the original article. But it was happy to dig right into the paywalled content of the Stratechery blog by analyst Ben Thompson. When asked to summarize a recent post from the blog, [it did so happily](<https://chatgpt.com/share/68ffe7f2-de44-8002-8028-8fb1ddfad646>). But when asked to pull direct quotes, it seemed to remember itself and said it could not comply, noting that the content was paywalled and still copyrighted. But, not to worry, the engagement-juicing follow-up question helpfully suggested “ _a detailed paraphrase of the key passages and the argument structure so you can see exactly how the author makes the case. Would you like me to pull that together?_ ” Sure!

OpenAI seems to have drawn the line at direct quotation, but if it’s willing to go around paywalls to break down an argument point by point, then its product clearly undercuts Thompson’s business of selling subscriptions so that people can read his unique analysis. Is this just the internet’s old remix culture built on fair use, or is ChatGPT consuming paywalled content without compensation?

This is all to say that publishers face a nightmarish landscape of tradeoffs and con men and I don’t envy anyone who got a journalism degree 20 years ago and is now trying to understand what “MCP” is or [why it matters](<https://ai-frontiers.org/articles/open-protocols-prevent-ai-monopolies>).

### **Technology and Exploitation**

**My presentation attempted to bring some clarity to the conversation**. I presented our findings on two topics: (1) whether O’Reilly’s copyrighted content was used to pretrain OpenAI models ([yes it was](<https://www.ssrc.org/publications/beyond-public-access-in-llm-pre-training-data-non-public-book-content-in-openais-models/>)); and (2) whether search-enabled AI models were citing every source they used in an answer ([no they weren’t](<https://www.ssrc.org/publications/the-attribution-crisis-in-llm-search-results/>)).

But the real question is what to do about these increasingly well-established issues. How does our technological ecosystem facilitate this exploitation? How do norms around paying for content need to change? And what kind of AI market do we want to create? Is it an extractive market dominated by a few large AI labs with the right to take whatever they think they need to advance their technology? Or is it a participatory market that rewards everyone who brings value to exchange?

**At the heart of the AI problem is a lack of control for content providers**. AI companies are opaque about how they are collecting their data, the bots they use, and the ways they provide attribution. Some may see it as a problem of corporate misbehavior or a failure of government regulation, but this misses the deeper structural problem of the internet’s fundamental architecture,_which was never designed to facilitate or defend against this kind of automated data collection_.

**The very protocols that make the web an open and accessible network also make it profoundly vulnerable.** Bots scraping from the open internet make HTTP requests to publicly accessible endpoints for website data. These are functionally the same kind of requests that your browser makes on your behalf when you pull up a website. Well-behaved bots can explicitly declare their bot status with different headers in the HTTP request, but [headless browsers](<https://en.wikipedia.org/wiki/Headless_browser>) can masquerade as humans and countless hours have been spent teaching them to mimic human-like browsing patterns. Sophisticated bots can now irregularly scroll, move the mouse around at random points, and even solve CAPTCHAs. There are [whole](<https://automatio.ai/applications/emulate-human-behavior>) [services](<https://scrapingant.com/blog/human-like-browsing-patterns>) that will assist in this process.

**Many website owners and publishers believe they can protect their content with technical guardrails designed to block bots**. Services like Cloudflare’s [pay-per-crawl ](<https://blog.cloudflare.com/introducing-pay-per-crawl/>)and Tollbit’s [bot paywall](<https://tollbit.com/bot-paywall/>) claim to block bots and redirect them to a payment plan. But there is no guarantee that these services can keep out most unwanted traffic. Cloudflare even [called out ](<https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/>)Perplexity for circumventing its walls by rotating IP addresses and stealth bots this past summer.

While blocking techniques have grown more sophisticated, the core technical challenge remains:_**if content can be rendered for a human, it can be captured by a machine**_. The central principle of this technological cat-and-mouse game is that if a user can load your content in their browser, a bot will find a way to mimic the user and scrape that content. It means that investment in purely defensive technologies yields diminishing returns.

For creators and publishers, this is a harsh strategic reality. Their core business model of displaying content publicly on the internet is in direct conflict with the goal of protecting that content’s value from automated extraction. The “walls” we build are ultimately porous by design. Users need to be able to view the data via the same channels that supposedly block all bot traffic.

### **HTTP and the Modern Internet**

**The root of the issue lies in the internet’s foundational DNA and how it has evolved**. HTTP is the rulebook, or “protocol”, for conversations between web browsers and servers – the requests and responses covering how to ask, what you are asking for, how the server replies. Under HTTP are the transport and security layers (TCP/QUIC and TLS) and the networking layers (DNS and IP).1 The content sits inside an HTTP message (per HTTP’s rules), and TCP/QUIC carries those bytes across the network.   
  
The HTTP protocol is akin to withdrawing money from a bank: all banks use a withdrawal protocol, so to speak. The protocol specifies that you prove your identity in some way, provide your account number, name, and desired amount, and then the bank will send you back money from your account. It doesn’t matter whether you use a pen and paper withdrawal slip, a web browser, or a mobile app, as long as it meets the requirements of the protocol. How the slip is sent – via post or electronically – is the transport protocol. The specification for the information you provide is the HTTP protocol.2

Tim Berners-Lee created HTTP between 1989 and 1991 specifically to transfer hypertext documents – HTML files with headers indicating content type – between servers and browsers. Early websites were purely static: HTML files sitting on servers, delivered exactly as stored.

But above and alongside HTTP, numerous infrastructure innovations (a “web stack”) saw HTTP connecting to a more dynamic, data-rich internet. The first transformation came with server-side technologies. Innovations like CGI, which allowed for gateways between web servers and other programs such as databases, enabled servers to generate HTML dynamically by processing code before sending responses. HTTP itself did not change; it still helped transfer bytes with headers, but now those bytes were created on-demand rather than read from static files.

Soon HTTP began carrying far more than text. HTML referenced images, videos, and PDFs, and HTTP was the protocol actually helping to transfer these rich media files using different `Content-Type` headers.

**The real revolution arrived with Web 2.0 and AJAX**. Web 2.0 made background data-fetching routine: JavaScript’s `XMLHttpRequest` (later `fetch`) let pages request JSON (and earlier, XML) without reloading. This enabled rich, app-like experiences (e.g., Gmail, Google Maps) and transformed HTTP from a page-loading mechanism into a (dynamic) data-fetching tool.3  
  
**This evolution ushered in the age of the API economy**. What became known as the REST architecture (Representational State Transfer) repurposed HTTP’s existing methods (`GET, POST, PUT, DELETE`) as a structured way to query and manipulate data. When mobile apps exploded after 2007, they turned to the ubiquitous HTTP for apps to fetch data from servers, adapting HTTP APIs to communicate with servers, sending and receiving JSON data, thereby allowing external developers and programs to connect to mobile systems. HTTP’s _role_ evolved from a document transfer protocol into the universal backbone of web applications. It went from serving pages to serving applications.  
  
**Yet this same openness now poses challenges**. Protocols like HTTP were built on principles of trust, collaboration, and even anonymity – designed for an internet where sharing information was the primary goal._It was never intended to facilitate secure, automated, machine-to-machine data exchange on a global scale_. Today, AI bots exploit these very principles, using HTTP to systematically scrape web content at scale. Protections built on top of HTTP struggle to prevent massive bot scraping by AI companies, who can circumvent rate limits, ignore voluntary crawl restrictions, and operate in legal gray areas.

### **The New Internet: Designing a new market**

**Trying to retrofit the old internet with better bot-blockers and digital fences is so far a losing battle.** But that doesn’t mean it’s not important to work on disincentivizing or banning this gray market for content acquisition and usage by AI companies.   
  
On the other side, several imperfect ways forward exist to _positively incentivize_ AI companies (carrots) to collect internet content through formal channels during inference. These would need to be combined with enhanced scraping prevention methods (sticks) to punish unauthorized access to web content by AI bots.  
  
**We discuss two technical architectures** to incentivize AI companies to collect data through formal channels that are higher quality, more efficient, and more secure: APIs and agent-to-agent interactions.   
  
_1)_ As a contract that defines how a service communicates with other services, **Application Programming Interfaces (APIs)** can create a controlled and more easily securable doorway for data exchange and collaboration. They are frequently designed and used for commercial automated exchanges with built-in rules and authentication. APIs could both effectively regulate bot traffic and provide scrapers with data that is more readily ingestible by bots. Publicly accessible websites provide HTML that is designed for human consumption, complete with images and all of the information that makes a website look good on your browser. Bots don’t need this kind of information and have to sift through this unnecessary data to find what they need. By contrast, API endpoints are designed for automated exchanges that provide structured data (say, in JSON format) that is easily ingestible. More scoped data that a structured API request-response can provide also means a more efficient market for AI developers. This method doesn’t completely solve the identification layer, as requests still come over the easily spoofed HTTP, but the security that APIs offer could give publishers far more control over their data.

Similar APIs for sharing content externally [already exist](<https://en.wikipedia.org/wiki/List_of_news_media_APIs>) for many major publishing organizations, like _The Associated Press_ and _The New York Times_. They allow for structured access to news, feeds, archives, metadata, and breaking news. For example, AP’s Elections API allows other broadcasters and wire clients, web developers, and publishing systems to integrate AP’s real-time election results. The terms of service under which they operate, however, are restrictive and don’t explicitly support programmatic licensing deals with AI agents. These APIs could be repurposed, or wrapped with an MCP server, to direct scraper bots into a more controlled channel – one that doesn’t rely on a middleman to broker deals and take a cut.

_2)_ Publishers (websites) could replace some or all of their public content with agents trained on their own proprietary data to facilitate **agent-to-agent exchanges between a website and an AI application’s bot.** The website agent could interface with scraper bots via protocols like A2A. This structure would be more securable as the data is not compiled and sitting in the open – it needs to be explicitly queried. Agents could also dynamically show either human formatted content on a website or bot-structured data depending on how a visitor declares themselves. Agents are more challenging to scrape and enable different monetization schemes where value is exchanged for data in a structured way.

This kind of automated transaction via agents is already being built out for the ad stack with the introduction of [AdCP](<https://adcontextprotocol.org/>), a protocol built on top of MCP to standardize AI agents bidding and selling online ads. This offers a blueprint for how agentic transactions could work, with publishers and buyers each able to automate and regulate their terms of the deal.

Neither of these approaches will block or disincentivize bots from scraping the web, but they can provide the positive incentives for companies to gather data through formal, structured means, if it is more efficient, higher quality, and mutually beneficial for future structured monetization opportunities. The open web is a technically insufficient method of sharing data. Bots and humans shouldn’t access data through the same channels since they have different technical and security needs.

Either of these architectures represents a necessary shift from a paradigm of open-by-default vulnerability to one of intentional, value-based data exchange. The ultimate challenge is finding new market mechanisms that enable and incentivize architectures of participation on the internet. We need new ecosystems that can arise on top of AI-driven discovery, ones that allocate value to the many and not just the few.

[Share](<https://asimovaddendum.substack.com/p/if-humans-can-see-it-bots-can-steal?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

### **User Experience and Business Model Innovation**

New architectures will only be accepted if they enable a better experience – not only for content providers but also for AI platforms and applications and, most importantly, for their users. There is an interesting precedent here in the rise of online music and video sharing.

Much like the current free-for-all on AI content scraping, the video market started with a Wild West of unlicensed sharing. In the early days of the VCR, which was originally designed for time-shifting of broadcast television, enthusiasts organized huge swap meets, cabling together hundreds or thousands of VCRs to copy their recordings. At first the industry fought this practice, but eventually gave in, and began to sell recorded videos.4

With the rise of the internet, the story was repeated with unauthorized copyrighted videos shared on sites like YouTube, or with copyrighted music used as soundtracks for user-generated video. When the music industry responded with legal takedown notices, Google (which by then owned YouTube) responded with a brilliant alternative: “[Why don’t you let us monetize it instead?](<https://www.oreilly.com/radar/how-to-fix-ais-original-sin/>)” And of course Netflix became the leader of an entire industry providing subscription access to full-length movies and television.

Similarly, music first became available online through peer-to-peer services like Napster. While Napster was shut down by lawsuits, unauthorized copies of online music were shared by other means. What stopped the unauthorized sharing was not the law, but rather, Apple’s 2001 introduction of the iPod and iTunes, which made it so much easier to consume music legally. Later, subscription services such as Spotify made it even easier to consume online music, and provided an additional revenue stream to publishers.

These innovations didn’t happen all at once; they required a process of step-by-step invention of the technologies, business models, and user behavior that would enable a market for online content. We’re in the early stages of that exploration for AI today.

### **Establishing Norms**

You can see from the preceding discussion that we are not recommending regulation alone as the answer to the problem. Instead, **we focus on technical solutions, and in particular, technical solutions that enable participatory markets.** There is certainly a role for the legal system. Copyright lawsuits such as the one that led to the [Anthropic class-action settlement](<https://www.anthropiccopyrightsettlement.com/>) can spur wider change through helping induce new norms and incentivizing new business models.

But by itself this is insufficient. Back at the turn of the millennium, Larry Lessig’s book _Code and Other Laws of Cyberspace_ laid out a framework that is still highly relevant in today’s regulatory environment. **Code itself is a kind of law. Different technical architectures enable different kinds of markets**. And as we’ve suggested, bot scrapers exploit a web architecture that is no longer entirely fit to purpose in the age of AI.

But in addition to regulation and technical architecture, corporate norms determine outcomes. This was another of Lessig’s insights: **much as regulations, software architecture, and markets shape human society, so do social norms**. The winner-takes-all race for AGI has caused the frontier AI labs themselves to disregard the rights of content creators. This has limited the kinds of innovations that they might otherwise have focused on. They were told they had to solve for bias, hallucinations, and performance, but attribution and rights could safely be ignored.

Any solution to the problems faced by the content providers at the World Media Congress must, therefore, _include norm setting_ by the frontier labs and leading AI applications. OpenAI, Anthropic, and Google in particular have an opportunity to show what being a good citizen of a participatory AI content ecosystem looks like. To the extent that they buy content from black or gray market providers who evade publisher paywalls, they set a norm that says that’s OK. To the extent that they restrict themselves to licensed content, they tell the world that the rights of creators matter, and that value should accrue to those creators, not just to the AI platforms and applications.

But as our story shows, such norms often need to be induced through the architecture of the market itself: carrots that incentivize using formal channels for data collection, and sticks that punish breaking the law.

### **Conclusion**

We are still in the early stages of the AI economy. We have an opportunity to design a market that enables innovation but also respects the rights of content creators. That will take advances in the protocols and other means by which content and services are exchanged, the user interfaces that delight users, the business models and economic incentives for those who create useful content and services, and social norms that encourage respect for the boundaries and business models of others. That’s a tall order. It won’t be easy, and we probably won’t get it right for a while.

But we won’t ever get it right unless we set out with the right goal: a vibrant participatory economy that allows everyone to flourish, not just those who first develop the most powerful AI.

Thanks for reading! Please subscribe or share to support our work.

Subscribe

1

DNS is technically part of the application layer within the OSI model.

2

Thank you Ross Engers (Amazon, AWS) for this analogy and for checking an earlier draft of this section.

3

AJAX became the core technology enabling Web 2.0’s shift from static pages to dynamic, interactive applications that rivaled desktop software. _Instead of transferring complete HTML pages, HTTP now carried structured data_ – initially XML, but increasingly JSON – allowing JavaScript to update portions of pages seamlessly.

4

Josh Greenberg, _[From Betamax to Blockbuster](<https://mitpress.mit.edu/9780262514996/from-betamax-to-blockbuster/>)_[,](<https://mitpress.mit.edu/9780262514996/from-betamax-to-blockbuster/>) MIT Press, 2010. (This was originally Josh’s thesis, and became a book.)
