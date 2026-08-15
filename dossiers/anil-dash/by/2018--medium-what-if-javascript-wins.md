---
title: "What if JavaScript wins?"
person: anil-dash
section: by
type: essay
year: 2018
date: 2018-05-15
venue: "Medium"
authors: "Anil Dash"
source_url: https://medium.com/@anildash/what-if-javascript-wins-84898e5341a
retrieved: 2026-08-13
content: full-text
notes: "Medium blocks non-browser clients; recovered from the Wayback Machine snapshot 20250829214450 (https://web.archive.org/web/20250829214450id_/https://medium.com/@anildash/what-if-javascript-wins-84898e5341a). Medium UI chrome stripped."
---

# What if JavaScript wins?

## Full text

## JavaScript is now part of the toolkit of most working developers. What if network effects push it into being the first-ever truly dominant programming language?

May 15, 2018

### Around a decade ago, a big part of coding culture changed.

What had often been a solitary pursuit, or one where collaboration happened with a defined set of colleagues within a company or open source project, burst open into a much more intrinsically social experience. Everything from how we share code to how we find answers to how we discover new technologies became far more linked to the attitudes and actions of other programmers.

In short, the people who make software got networked just like their computers had been in the preceding decades.

## The Networks

The impact of network effects on coding culture has manifested itself in many ways, but some of the most visible are worth examining:

  * For knowledge about coding issues, and answers to common questions, [Stack Overflow](<https://stackoverflow.com/>) rose and quickly became a dominant source of reliable information about programming. (Requisite disclaimer: I’m on the board of Stack Overflow, though my experience here is based on being a coder who just relies on it for useful answers.) Though the [barriers to participation](<https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change/>) in the Stack Overflow community are well-known, there’s no doubt that its enabling of a network of knowledge around coding answers amplified the discoverability of programming information, and accelerated the idea of social signal being a strong component of technology adoption. A framework or toolkit that has its own, actively answered tag on Stack Overflow is much more likely to get new adopters.
  * A similar pattern followed for collaborating around code: [GitHub](<https://github.com/>) rose a decade ago as a powerful platform for sharing each commit to a project. Though its value was presented as being about popularizing the then-nascent distributed version control tool Git, the social value of GitHub has extended to being a signal of the value or reliability of software hosted on the platform. Counting the number of stars or forks or watchers on a project acts as a proxy for how much the code can be trusted. GitHub has real barriers, like the difficulty of learning git or the obtuseness of organizing around _changes_ to a project, rather than the project itself, and all of these factors can make it difficult for some users to participate in the network. But despite those barriers, social signals on GitHub deeply shape the adoption of tools and technologies by developers.
  * Finally, there are the networked information sources for news and discussion, primary among them being [Hacker News](<https://news.ycombinator.com/>). Though it’s notoriously the most hostile of these large, networked coder communities, it inarguably helps promote and elevate new technologies and new ideas around how to create software. Hacker News’ amplification of tools often helps them reach critical mass in adoption, and discussion of a product is another form of social signal that many in the coding world use to judge a particular platform. To a lesser degree, more product-focused communities like [Product Hunt](<https://www.producthunt.com/>) also fulfill some of this function. (And Product Hunt does this while being far more welcoming.)

In each of these cases, if we look past the flaws of the communities that enable them, we see a deeper pattern: software being evaluated based on its social success and social merits, rather than just some ostensibly “objective” technical merit.

Technology has always existed in a social context, and evaluations of the risk or reliability of a tech platform have always relied on social indicators. But the _acceleration_ of these patterns, and the extending of the social networks around code to include the _majority_ of working coders, means that institutional indicators (like “which company funds its development?”) now come second to community-based signals.

Similarly, top-down indications of technical maturity like documentation (often an artifact of outside investment in making a technology accessible to a new audience) are complemented, or even eclipsed, by bottoms-up indicators like how many people have bookmarked a framework, or how many people answer comments about a toolkit. Even purely social factors like the number of participants in a Gitter or Slack chat room about a project, or the number of people who follow a project on social media, are all weighed when we look at new technology.

## Then There’s The Law

Though nearly everything he shares on social media these days makes me want to smash my head into my desk, longtime software blogger Jeff Atwood has had a number of valuable insights over the years. Perhaps none was more prescient than the insight captured in his [eponymous law](<https://blog.codinghorror.com/the-principle-of-least-power/>):

> [A]ny application that _can_ be written in JavaScript, _will_ eventually be written in JavaScript.

Jeff’s inspiration lay in the insightful “[principle of least power](<https://www.w3.org/DesignIssues/Principles.html>)” as articulated by Tim Berners-Lee, father of the web. But especially back when Jeff wrote that blog post, JavaScript was still considered something of a toy (for example, Node.js wouldn’t be invented for another 2 years), and the idea of everything being ported to the language seemed a bit absurd. Naturally, the internet being the internet, almost a dozen years later, there’s an [entire community](<https://www.reddit.com/r/atwoodslaw/>) dedicated to documenting things being ported to, or rewritten in, JavaScript.

But Atwood’s law speaks to the ability to re-implement nearly any other code in JavaScript. Given that any Turing-complete language should be able to implement functionality written in other languages, that makes this observation amusing, but not particularly revelatory about what kinds of behaviors might emerge as a result. Atwood’s law says nothing about _adoption_ of JavaScript, just its potential to express ideas implemented in other languages.

## But What If JavaScript Is A Network?

There are a lot of things that are considered “JavaScript” these days. There’s the open language described in the ECMAscript standard. There are adjacent languages like TypeScript that offer niceties to coders in exchange for compatibility with the JavaScript ecosystem. There are environments like Node. There’s the power of instant access to years of coding effort through package management tools like npm. There is a nearly-infinite amount of infrastructure around the language, and even more infrastructure _using_ the language to provide build tools or automation for other languages. And then there’s the ubiquity of JavaScript being interpreted within the web browsers on billions of devices around the world.

This breadth of contexts accounts for the popularity and dominance of JavaScript. Indeed, the most recent [Stack Overflow survey of developers](<https://insights.stackoverflow.com/survey/2018/#technology>) lists nearly 70% of them claiming JavaScript as one of the languages they use. (As above, some of the obstacles for participation in the Stack Overflow community can skew this kind of survey, so we should be mindful of those distortive effects, but the overall trend here is clear even if we account for those concerns.) And the percentage of coders using JavaScript keeps _increasing_ , increasing by about 15% in just the last few years, even as other languages like Python keep growing as well.

What this suggests is that JavaScript may be reaching escape velocity as a _network_ , and as an ecosystem of related technologies. To be clear, there’s no winner-takes-all here — domain-specific languages will always have their uniquely valuable areas of focus. But for general-purpose coding? Everything from spreadsheet macros to Internet of Things hardware seems to default to having JavaScript be one of the primary ways to make things programmable.

It’s impossible to say if this idea of evaluating a programming language as a social network is a valid way to judge the technology. But every indication is that the feedback loop around the JavaScript ecosystem is _increasing_ in strength. Though most “serious” developer tools are insistently polyglot (and indeed, every indication is that most working coders do make use of more than one language in their work), it may make sense for forward-looking platforms to disproportionately invest in JavaScript for their futures.

Press enter or click to view image in full size

## Glitch ❤ JavaScript

Of course, I work on Glitch all day long, so you know our team has got an opinion on this. Don’t worry: [Glitch](<https://glitch.com/>) can run code in almost any common language. We’ve got Python and PHP and Ruby projects happily running in the community.

But we’ve chosen JavaScript (and Node) as our primary platform for Glitch, the one we feature in our work. There are lots of reasons for this (I mean, have you _seen_ the [full-stack debugging](</glitch/tackling-the-biggest-pain-points-in-web-development-57d64afe19dc>) that Glitch lets you do?!) but one of them is that we’re a small team and we want to make sure we’re betting on the technology that will provide the most value for our community. And we think our investment in the JavaScript ecosystem will only become _more_ valuable over time.

We also look at the network value of apps, libraries, modules, and code snippets that live in the Glitch ecosystem, and we think focusing our attention will yield dividends as we start to build more tooling for coders and apply newer developments in machine learning to help make coding easier. Picking a domain helps ensure that the things we create are valuable and applicable and immediately useful, instead of diffuse efforts to serve all languages without really picking one to be great at.

Now, this isn’t carved in stone. If Haskell comes out of nowhere and gets baked into a billion browsers and they start teaching it to kids in grade school, Glitch is gonna be there. And there are definitely folks on the Glitch team who wish we could offer as great an experience on other languages as we do on JavaScript. But with trends where they are right now, we wanted to explain our rationale behind making a bigger bet on JavaScript and on Node, rather than just saying “we’re language-agnostic”. There’s theory, and thought, and a little bit of history, and a pretty good amount of data, and all of those signals indicate that something special is going on here.

The truth is, we’ve never seen one open language become a nearly-universal programming language for coders. We don’t know what kind of benefits might accrue if the majority of coding effort starts to happen in one language, unless there’s a particular reason to use a domain-specific language that insists we do otherwise.

We just might be on the precipice of an era in coding that’s unprecedented, where we might actually see something _new_ in the patterns of adoption and usage of an entire programming language. That potential has us excited, and waiting with bated breath to see how the whole ecosystem plays out. But even more than that, we’re excited that all of these developments will allow the Glitch community to make apps that are even more expressive and meaningful, while being even easier to realize in code.

We can’t wait to see what you create!
