---
title: "Simple Generative Ideas"
person: mike-caulfield
section: by
type: blog-post
year: 2015
date: 2015-04-25
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2015/04/25/simple-generative-ideas/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Simple Generative Ideas

## Full text

I’ve been explaining federated wiki to people for over a year now, sometimes sucessfully and sometimes not. But the thing I find the hardest to explain is the simple beauty of the system.

As exhibit A, this is something that happened today:

[](<https://mikecaulfield.wordpress.com/wp-content/uploads/2015/04/screenshot-2015-04-25-at-8-13-21-am.png>)

In case you can’t see that, this is what is going on. I’m creating a new template (look at my last post to understand the power of templates). But since the way you create a template is to just create a normal page but make the last word of the name “template” some thing interesting happens: you can create templates based on other templates.

Now since the IDs of the elements follow each template, that means that your second generation template inherits the abilities you coded for the first generation template, including all the bug-checking, cross-browser compatibility fixes, etc. You get all of that without writing a single line of code. So I can hammer out a basic template, write some handlers on the client side, then others can come and build a template based on my template and extend it, sometimes without even programming. Or they can drag and drop items from other templates, and since the IDs follow those items they might be able to mix and match their way to a new template.

Did Ward, Paul, and Nick plan any of this as they designed the code? No, not a bit. But every time a feature is requested the slow discussion begins — instead of a feature, is there a way to deliver this as a capability that extends the system as a whole? Is there a way to make this simpler? More generative? More in line with the way other things in federated wiki work?

So Ward is surprised as me that you can build templates out of templates. But we are both also not surprised, because this is how things go with software that’s been relentlessly refactored. There’s even a term for it: “Reverse bit-rot”.

A normal software process would have long ago decided to give Templates their own type and data model, soup them up with additional features, protections, tracking. The agile process says things should be constantly refactored down to a few simple and powerful ideas. It’s not as flashy, but you find you have killer features that you didn’t even intentionally write.
