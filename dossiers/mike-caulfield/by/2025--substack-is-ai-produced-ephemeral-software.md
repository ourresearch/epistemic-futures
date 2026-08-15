---
title: "Is AI-Produced Ephemeral Software the Future of Novice Computing?"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-02-18
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/is-ai-produced-ephemeral-software
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Is AI-Produced Ephemeral Software the Future of Novice Computing?

*There are issues, but I think its a likely path*

## Full text

The last couple days I posted ephemeral software — software that potential users can use a text sent to ChatGPT to produce. So you need a text diff tool, you [plug this into the chatbox](<https://open.substack.com/pub/mikecaulfield/p/create-a-diff-tool-in-chatgpt-o1?r=hbr2&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true>) of the ChatGPT 4o model:
    
    
    Canvas On canvas build an interactive javascript page that takes in two text areas. One has initial text. One has revised text. When a button is pressed the page uses a javascript library to do a visual word level diff.

Need to analyze a photo and tell if it is AI, and you plug this into the 4o model — and get a [whole digital alteration detection suite](<https://open.substack.com/pub/mikecaulfield/p/how-to-use-chatgpt-to-detect-ai-and?r=hbr2&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true>):

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
    
    
    We are going to make a photographic manipulation test suite. When I upload a photo and say "check for digital alteration" you will write and run python code to check it for AI production, compositing, colorization, and other digital manipulations. Do the following, and always show the resulting image: Local Contrast Variation: Canny edge detection, Gabor filter (multiple) Reflections And Highlights Consistency: Noise Pattern analysis (FFT), Lighting consistency (gradient magnitude), reflection and highlights consistency. Check for colorization using B Channel (Color Consistency) check. Run Deep Learning-Based AI Detection, JPEG Compression Analysis, Patch-Based Anomaly Detection, Histogram Analysis, Saturation and Hue Irregularities When code executes successfully without error you will commit to memory that that method worked in this environment, and when code fails (i.e. errors out) you will commit to memory that that method failed and should not be used again. When done, answer whether the image was photoshopped, composited, digitally altered or blended, or AI-generated with a probability rating of low, medium, high, and explain your rating. Ready? If so, commit these instructions to memory and say "Upload a photo and say 'check for digital alteration'".

People ask what’s the point, and I think it’s the same point I’ve made a lot before. Programming is a powerful skill, but it’s confined to a few, and this means there isn’t a whole lot of end-user innovation. The ability to spin up simple programs that generate out of descriptions the size of a few text messages would be game-changing for a lot of people. Want to do a complicated text replace? Clean up junk HTML and replace it with markdown? Calculate the ideal projector screen size for a given lens and throw distance? Pull from a library of simple descriptive requests, plug them in, engage with a back and forth to massage them to your needs.

If novices (in programming, but often experts in their field) adopted ephemeral programming, efficiencies would eventually be built in. The code generated could be semi-ephemeral, left in a fully written but pre-compiled state for multiple uses until the system is given orders to rewrite it. The shareability already available with the canvases of 4o and Claude could be imbued with more functions, and made more findable. 

It’s exciting in a number of ways, but one is this — as programming has gotten more complex, it has become more inaccessible. In my youth a good portion of students sat in front of Apple IIe’s and learned to program biorhythm calculators and starcharts (it was the early 1980s but still really the 70s). My daughter took an AP computer class about 4 years back, and wrote a simulated card game — half the project was getting the Java development environment to compile the right dependencies. She went in excited about building things, and came out never wanting to touch code again. 

That stuff (IDE, dependencies, object-oriented design) is all important, but there’s just a lot of people who could at least start to engage with programming if the entry point was a bit easier. I think the ones that wanted to go further could work back to the other stuff. And I think a lot of people could get some benefit without even doing that. Seems to me like that’s enough to make it worth exploring. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
