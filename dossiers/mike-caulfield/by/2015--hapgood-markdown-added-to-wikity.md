---
title: "Markdown added to Wikity"
person: mike-caulfield
section: by
type: blog-post
year: 2015
date: 2015-12-26
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2015/12/26/markdown-added-to-wikity/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Markdown added to Wikity

## Full text

Markdown support has been added to Wikity (more specifically GitHub-flavored Markdown). I’ve done this for some very good reasons, and I’ve also done this a bit differently than most implementations, and I thought I’d explain why.

First, a brief description of what Markdown is, for the uninitiated. Markdown is a markup format produced in 2004-ish by Jon Gruber with some input from Aaron Swartz. The idea of Markdown was to create a markup syntax that balanced human-readability with machine readability. Like wiki markup before it, it drew heavily from conventions of a format called setext which was used in Usenet newsgroups and email communications.

Here’s a comparison of what markup looks like in HTML and Markdown:

text using Markdown syntax | the corresponding HTML produced by a Markdown processor |   
---|---|---  
      
    
    Heading
    =======
    
    Sub-heading
    -----------
     
    ### Another deeper heading
     
    Paragraphs are separated
    by a blank line.
    
    Leave 2 spaces at the end of a line to do a  
    line break
    
    Text attributes *italic*, **bold**, 
    `monospace`, ~~strikethrough~~ .
    
    Shopping list:
    
      * apples
      * oranges
      * pears
    
    Numbered list:
    
      1. apples
      2. oranges
      3. pears
    
    The rain---not the reign---in
    Spain.
    
    A [link](http://example.com).
    

| <h1>Heading</h1> <h2>Sub-heading</h2> <h3>Another deeper heading</h3> <p>Paragraphs are separated  
by a blank line.</p> <p>Leave 2 spaces at the end of a line to do a<br />  
line break</p> <p>Text attributes <em>italic</em>, <strong>bold</strong>,  
<code>monospace</code>, <s>strikethrough</s>.</p> <p>Shopping list:</p> <ul>  
<li>apples</li>  
<li>oranges</li>  
<li>pears</li>  
</ul> <p>Numbered list:</p> <ol>  
<li>apples</li>  
<li>oranges</li>  
<li>pears</li>  
</ol> <p>The rain&mdash;not the  
reign&mdash;in Spain.</p> <p>A <a href=“[http://example.com&#8221](<http://example.com&#8221>);>link</a>.</p> |   
  
## Why Markdown and Reusability Go Together

“So what?”, you might think. “Markdown is moderately easier to read and work with than HTML but _I use an HTML editor_ so I don’t ever see that HTML gobbledygook!”

Well, we’ve set it up so you can use the HTML editor side by side in Wikity next to Markdown. So you don’t need to change a thing. But I’d like you to consider a couple reasons why you might try working in Markdown.

**Markdown keeps you honest.** Visual editors pander to people who want to control how something looks rather than what it means. But in our multi-device world you can’t really control how something looks. When you do silly things like declare the size of a heading in absolute terms, you create a reusability mess that adversely effects everyone down the line.

Now it’s true, the WordPress editor has gotten very good at saving people from their worst instincts, but then there’s the copy problem…

**Markdown solves the copy/paste problem.** When you copy text from another website into your WordPress editor kittens die.  _Lots_ of kittens. Even if the text you pasted in looks good to you in your browser it looks horrible in someone else’s, and it’s probably uneditable to boot.

What happens is this. The website you go to has a databased version of your text. It looks at your browser, your platform, your screen size and the surrounding template and encodes that all into a set of HTML probably keyed to a specific style sheet served up separately. Now you go and copy that text into a new context that has to serve multiple browsers and platforms and screen sizes from a template that works entirely differently and uses its own, different style sheet.

What you’ve done is coded the use context into the content, and that is very bad.

With Markdown, you copy and paste the text in, and then quickly add the semantic markup, indicating links, blockquotes, italics, etc. Your text comes over clean.

**Markdown is friendly to the mobile composer.** I’ll be honest: I think mobile devices are the wrong devices for composing things. But I know I’m in the minority here.

Now if you’ve ever tried to blockquote or bold text with a mobile device, or tweak which words in a phrase should be part of a link you’ll have realized that a big problem with text editing on these devices is that 30 years of WYSIWYG development has assumed that there is a mouse attached to your machine.

Markdown solves this problem by making all formatting text-based. If you can type on your phone you can format.

**Markdown will make you faster at everything.** Add this to the “hard-to-learn but easy-to-use” category. There is a small learning curve with Markdown. However, because Markdown allows you to compose and format without periodically breaking concentration to look for the tool bar, grab the mouse, select text and find the right button it will make you faster in everything you do. There’s a reason that programmers, the laziest people on the planet, have gravitated to Markdown for documentation and composition.

**Special bonus for teachers: keep students focused on the content.** I’ll just add this in here, from personal experience. I have been teaching with various site making tools for more than a decade and there’s a definite balance to be struck with student design on projects that are not about student design.

I think, for example, that your history or stats class will enjoy being able to choose a WordPress template for their page, a background image, maybe a custom header, etc. These things build a sense of ownership with a site.

But I’ve also seen projects with Google Sites and other tools go awry, where a certain group gets so fixated on the issue that they can’t get the picture to float-left just the right way or get the blockquote in a certain section to just the right size that they forget they are supposed to be doing history or stats or sociology.

In fact, I’d argue that part of technical literacy these days is understanding in a multi-device accessibility-focused world that this pixel-level focus is a sign of technical illiteracy, and we must do our best to get students to understand the separation between content and styling that makes the modern communications ecosystem possible.

**There are more reasons, but damn this post is long.** I was going to go into a long discourse (diatribe?) on the history of WYSIWYG and how it killed text reusability, but this post is too long already.

## Final Note

We did the implementation differently than JetPack, becuase JetPack has different goals.

JetPack lets you type in Markdown which is then converted to HTML which then gets saved. This is because the assumption in blogging engines is that once you post you will likely never edit that page again, so there’s no benefit in maintaining Markdown editability relative to the cost of the system having to interpret Markdown each time a viewer looks at your page.

Needless to say, we see things differently. The primary use to us of Markdown is as a storage format, so that when someone forks your page they get a nice clean Markdown version of it (if that’s the way you wrote it) that they can easily edit and update.

So we hacked in a module called Parsedown, and rolled our own wrapper for it.

What this means is if someone writes Markdown-based pages you should be able to fork those pages. Ideally, what I’d like to see is that a few communities that emerge on Wikity might make community rules which either require or forbid the use of Markdown for materials that they produce.

There is a Markdown Cheatsheet [here](<https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet>), and of course you can go get an account on Wikity [here](<http://wikity.cc/>). The join code for the moment is “peloton”, but if it changes you can always reach me via Twitter (@holden).
