---
title: "Reclaim Hackathon"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-07-23
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/07/23/reclaim-hackathon/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Reclaim Hackathon

## Full text

[Kin](<http://kinlane.wordpress.com/2014/07/23/reclaim-your-domain-la-hackathon-wrap-up/>) and [Audrey](<http://hackeducation.com/2014/07/22/reclaim-your-domain-hackathon/>) have already written up pretty extensive summaries about the Reclaim event in Los Angeles. I won’t add much.

Everything was wonderful, and I hope I don’t upset people by choosing one thing over another. But there were a few things for me that stood out.

**Seeing the Domain of One ’s Own development trajectory**. I’ve seen this at different points, but the user experience they have for the students at this point is pretty impressive.

**JSON API directories.** So I really like JSON, as does Kin. But at dinner on Friday he was proposing that the future was that the same way that we query a company for its APIs we would be able to query a person. I’d honestly never thought of this before. This is not an idea like OAuth, where I delegate some power/data exchange between entities. This is me making a call to the authoritative Mike Caulfield API directory and saying, hey how do I set up a videochat? Or where does Mike post his music? And pulling back from that an API call directly to my stuff. This plugged into the work he demonstrated the next day, where he is painstakingly finding all his services he uses, straight down to Expedia, and logging their APIs. I like the idea of hosted lifebits best, but in the meantime this idea of at least owning a directory of your APIs to stuff in other places is intriguing.

**Evangelism Know-how.** I worked for a while at a Services-Oriented Architecture obsessed company as an interface programmer (dynamically building indexes to historical newspaper archives using Javascript and Perl off of API-returned XML). I’m newer to GitHub, but have submitted a couple pull requests through it already. So I didn’t really need Kin’s presentation on APIs or GitHub. But I sat and watched it because I wanted to learn how he did presentations. And the thing I constantly forget? Keep it simple. People aren’t offended getting a bit of education about what they already know, and the people for whom it’s new need you to take smaller steps. As an example, Kin took the time to show how JSON can be styled into most anything. On the other hand, I’ve been running around calling SFW a Universal JSON Canvas without realizing people don’t understand why delivering JSON is radically different (and more empowering) than delivering HTML (or worse, HTML + site chrome).

**Known.** I saw known in Portland, so it wasn’t new to me. But it was neat to see the reaction to it here. As Audrey points out, much of day two was getting on Known.

**Smallest Federated Wiki.** Based on some feedback, I’ve made a decision about how I am going to present SFW from now on. I am astounded by the possibilities of SFW at scale, but you get into unresolvable disagreements about what a heavily federated future would look like. Why? Because we don’t have any idea. I believe that for the class of documents we use most days that stressing out about whether you have the the best version of a document will seem as quaint as stressing out about the number of results Google returns on a search term (remember when we used to look at the number of results and freak out a bit?). But I could be absolutely and totally wrong. And I am certain to be wrong in a lot of *instances* — it may be for your use case that federation is a really really bad idea. Federation isn’t great for policy docs, tax forms, or anything that needs to be authoritative, for instance.

So my newer approach is to start from the document angle. Start with the idea that we need a general tool to store our data, our processes, our grocery lists, our iterated thoughts. Anything that is not part of the lifestream stuff that WordPress does well. The stuff we’re now dropping into Google Docs and emails we send to ourselves. The “lightly-structured data” that Jon Udell rightly claims makes up most of our day. What would that tool have to look like?

  * It’d have to be general purpose, not single purpose (more like Google Docs than Remember the Milk)
  * It’d have to support networked documents
  * It’d have to support pages as collections of sequenced data, not visual markup
  * It’d have to have an extensible data format and functionality via plugins
  * It’d have to have some way to move your data through a social network
  * It’d have to allow the cloning and refactoring of data across multiple sites
  * It’d have to have rich versioning and rollback capability
  * It’d have to be able to serve data to other applications (in SFW, done through JSON output)
  * It’d have to have a robust flexible core that established interoperability protocols while allowing substantial customization (e.g. you can change what it does without breaking its communication with other sites).

Of those, the idea of a document as a collection of JSON data is pretty important, and the idea of federation as a “document-centered network” is amazing in its implications. But I don’t need to race there. I can just start by talking about the need for a general use, personal tool like this, and let the networking needs emerge from that. At some point it will turn out that you can replace things like wikis with things like this or not, but ultimately there’s a lot of value you get before that.
