---
title: "Current Design of the Federated Classroom Wiki as of Today"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-03-05
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/03/05/current-design-of-the-federated-classroom-wiki-as-of-today/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Current Design of the Federated Classroom Wiki as of Today

## Full text

I’m realizing some of the design description of the Federated Classroom Wiki on Hapgood is out of date. So here is how it is currently working (or soon to work based on some scheduled coding). This is the process you would use as a user.

**Setup**

  1. **Install!** Your institution installs Dokuwiki on a server, on a PaaS, or other vehicle. Wherever you want with whoever you want. (You can do any step here as an individual as well, just dealing with institutional case here).
  2. **Extend!** Your institution installs the two custom plugins I’ve written (federation and clone) and the freely available gitbacked plugin
  3. **Federate!** You go to the federation GitHub site (e.g. <https://github.com/timmmmyboy/federated-wiki>, though you can make others). You fork it, add your self-named folder to it (ex. UofUT, UVU, NIU, UMW, whatever), then issue a pull request to accept that change. You point this new folder to your dokuwiki pages folder (via gitbacked). There’s some finessing here that Tim will show in a screencast soon, but what you’ll end up with after Tim’s magic is done is a system where your changes to your wiki will flow into the subfolder. Then all pages from all federated wikis will flow into a special subfolder/namespace of your wiki called alternate. This will be searchable by people with editing permissions (although you can set permissions up any way you want, really).

**Use**

  1. **Search!** Now you are about to write a syllabus, or assign your students to write an article. You think — wouldn’t it be nice to just tweak a syllabus, or give my students an article to *extend*? You go and search the :alternate: namespace for federation content you can use. You find some great articles your students can improve, and a syllabus that is a good starting point.
  2. **Clone!** You clone the articles and the syllabus to your public wiki/course namespace. The revision record follows the documents so that attribution is taken care of.
  3. **Edit!** You tweak the documents to your own needs. You write additional documents.
  4. **Feed Forward!** Here’s the neat part — because you are federated, feed forward isn’t actually a step. All the changes you make feed back into the federation as alternate versions of the documents you cloned. The person whose docs you cloned gets a message in their revisions history that you cloned it, and is automatically pointed to your revisions to see if they are useful. Your other original docs you made also flow back to the federation. The next person who searches will see your alt-versions and new documents, and maybe end up cloning those. Lather, Rinse, Repeat.

There are possibly classroom systems which already do similar things, though I’ve never seen them do this well. The fundamental difference here is the structure that makes it possible. This is not a service that everyone has to agree on to be a part of. It’s a federation — you have absolute control over who is in your community and what they can do and where your instance lives and how it’s branded. You are self-governing, an island. But on the back-end the architecture creates a system of sharing by default that gives you the benefits of working with a community without having to make institutional or individual compromises. The contract is simple– all this stuff will flow to you if you let your stuff flow back. Think of it sort of like torrenting — you get your download speed by letting others download from you.

There’s lots of reasons I’ve come to feel that this point is crucial for the expansion of higher ed collaboration, but that’s another post.
