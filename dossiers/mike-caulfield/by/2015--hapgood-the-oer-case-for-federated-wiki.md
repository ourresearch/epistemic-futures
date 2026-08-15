---
title: "The OER Case for Federated Wiki"
person: mike-caulfield
section: by
type: blog-post
year: 2015
date: 2015-05-05
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2015/05/05/the-oer-case-for-federated-wiki/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# The OER Case for Federated Wiki

## Full text

I talk a lot about the open pedagogy case for federated wiki, but not much about the OER/OCW case for it. That doesn’t mean it isn’t a good fit for the problems one hits in open materials reuse.

Here’s how you currently reuse something in WordPress, for example. It’s a pretty horrific process.

  1. Log into the WordPress source site
  2. Open the file, go to the text editor.
  3. Select all the text, cntrl-c copy it.
  4. Go log into your target WordPress site
  5. Create a new page and name it.
  6. Go into the text editor, and paste the text in.
  7. Save Draft.
  8. Go back to the source site. Right click on the images in the post and download them.
  9. Go back to the target site. Open the Media Gallery and upload the images you just downloaded.
  10. Go through you new post on the target site, and replace the links pointing to the old images with links pointing to the images you just uploaded.
  11. Preview the site, do any final cleanup. Resize images if necessary. Check to make sure you didn’t pull in any weird styles that didn’t transfer (_Damn you mso-!_)
  12. Save and post. You’re done!
  13. Oh wait, you’re not done. Go to the source post and copy the URL. Try to find the author’s name on the page and remember it.
  14. Go to the bottom of your new “target” page and add attribution “Original Text by Jane Doe”. Select Jane Doe and paste in the hyperlink. Test the link.
  15. Now you’re REALLY done!

It’s about an five to ten minute process per page, depending on the number of images that have to be ported.

Of course, that’s assuming you have login rights to both sites. If you don’t, replace steps one and two with trying to copy it from the actual post, attempting to paste it in the *visual* editor to preserve formatting, go through the same steps, except spend an extra five to ten minutes cleanup on step eleven.

It’s weird to me how fish-can’t-see-the-water we are about this. We’re in 2015, and we take this 15 step process to copy a page from one site to another as a given.

Conversely, once you see how absurd this process is, you can’t *unsee* it. All these philosophical questions about why people don’t reuse stuff more become a little ridiculous. There are many psychological, social, and institutional reasons why people don’t reuse stuff. But they are all academic questions until we solve the simpler problem: our software sucks at reuse. Like, if you had an evil plan to stop reuse and remix you would build exactly the software we have now. If you wanted to really slow down remix, you would build the World Wide Web as we know it now.

Conversely, here’s what the steps are in federated wiki to copy a page from one site to another:

  1. Open your federated wiki site.
  2. Drag the page from the source site to the target site and drop it.
  3. Press the fork button. You’re done!

And keep in mind you don’t need to have the front-end of your site look like federated wiki. All that matters is you have federated wiki on the backend. Here’s a short video showing how two sites with different web-facing appearance still allow the easy transfer of pages:

You’ll notice that most of the length of this video is explanation. The actual transfer of the three pages transferred here is from 1:45 in the video to 2:30. It’s about 15 seconds a page to copy, complete with images. While the question of why people don’t remix and reuse more is interesting to me from a theoretical standpoint, I think it pales in comparision to this question: **what would happen if we dropped reuse time from 10 minutes to fifteen seconds?**

How is this possible? Mostly, it’s the elegance of federated wiki’s data model.

  * **Data Files not Databases.** Traditional sites store the real represenation of a page in a database somewhere, then render it into a display format on demand. The database takes a clean-ish copy and dirties it up with display formatting, You grab that formatting and try to clean it up to put it back in the database. Federated wiki, however, is based on data files, and when we pull that link from one federated wiki driven site to another federated wiki grabs the JSON file, not the rendered HTML.
  * **JSON not HTML.** HTML renders data in a display format. A YouTube video, for example, specifies an IFRAME as a device along with width, height and other display data. This hurts remixability, because our two sites may handle YouTube videos in different ways (width of player is a persistent problem). JSON feeds the new site the data (play a YouTube video with this ID, etc) but let’s the new site handle the render.
  * **Images Embedded.** This is a simple thing, and the scalability of it has a few problems, but for most cases it’s a brilliant solution. Federated Wiki’s JSON stores images not as a link to an external file, but as JSON data stored in the page. This means when you copy the page you bring the images with it too. If you’ve ever struggled with this problem in another platform you know how huge this is: there’s a reason half the pages from 10 years ago display broken images now – they were never properly copied.
  * **Plugin Architecture.** ~~Federated Wiki ’s plugin architecture works much like Alan Kay’s vision of how the web should have worked.~~ The display/interaction engine of federated wiki looks at each JSON “item” and tries to find the appropriate plugin to handle it. Right now these are mainly core plugins, which everyone has, but it’s trivial to build new plugins for things like multiple choice questions, student feedback, and the like. If you copy a site using a new-fangled plugin you don’t have, the page on your site will let you know that, and direct you to where you can download the plugin. Ultimately, this means we can go beyond copying WordPress style pages and actually fork in tools and assessments with the smae ease.
  * **History follows the Page.** As anyone who has reused content created and revised by multiple people knows, attribution is not trivial. It consumes a lot of time, and the process is extremely prone to error. Federated wiki stores the revision history of a page with the page. As such, your edit history is always with you and you don’t need to spend any time maintaining attribution. If the view of history in the federated wiki editor is not sufficient to your needs, you can hit the JSON “Journal” of the page and display contribution history any way you want.

We could probably say more on this, but this should do for now.
