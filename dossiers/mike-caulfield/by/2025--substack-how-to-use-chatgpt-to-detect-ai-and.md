---
title: "How to use ChatGPT to detect AI (and otherwise digitally altered) photos"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-02-17
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/how-to-use-chatgpt-to-detect-ai-and
retrieved: 2026-08-13
content: full-text
notes: ""
---

# How to use ChatGPT to detect AI (and otherwise digitally altered) photos

*And a detour regarding why tools for amateurs unusually invested in making things better are useful*

## Full text

**NOTE: The technique here will probably exceed the tokens allowed on the free account — this technique works with the $20/month account or some of the academic contract accounts (e.g. CSU).**

One of the unfortunate trends in AI literacy regarding spotting fake photos is to tell students to “look for the clues”. When people first started saying things like “Count the fingers” I tried to explain to them that in two years AI would be producing hands just fine. Now genAI is producing hands just fine and we’ve trained a generation of students to believe that anything with five fingers is real. Not great, obviously.

The better approach is always provenance, if you can get it. Do you know where and when this photo was taken, and by whom? Is there a record of it? Who vouches for it? When looking at veracity in a world flooded with AI we need to be teaching provenance.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

That said, we don’t always have provenance. And while detecting the better and newer AI fakes will always be out of the reach of an amateur, I see a lot of people who are absolutely convinced by AI fakes. What to do about that?

## A brief detour: the antibodies are people

This next part of what I’m about to say has always been hard for people to comprehend, and I really don’t know why. It’s probably the most important idea in dealing with misinformation, and maybe one out of a thousand get it. I was recently in a conversation with misinformation researchers, and I think not a single one of _them_ got it.

The point of showing people how to identify fakes is not to prevent them from sharing fakes, but for them to prevent others from believing in them.

There’s an unfortunate metaphor people use where we supposedly want to “vaccinate” people against misinformation. This is based on the wrong belief that bad information is like a virus, and the only way to stop it is to boost the largest percentage of the population’s “immunity”. 

But that’s not how things really work. We mostly decide what to believe not through intense analysis of every claim that passes us by, but by looking at what people we believe to be “in the know” believe. And what actual research of actual people on the internet shows is that the biggest impacts on what spreads and doesn’t is whether influential people either support or debunk a claim.

We have to boost the antibodies in the information system, sure, but they aren’t some mystical bit of resistance in the minds of every individual. _The antibodies are people_. They are the folks that are willing to spend a little bit more time on a photo or claim they think to be wrong, to go read the fact-check or find the context, and then share that information with others. 

That’s why my most of my career has focused on one thing, from edublogs, to federated wiki, to SIFT, to my current work with AI — _give people unusually invested in improving the information environment the tools and skills to do so._ That’s it. That’s my career from 2007 (OER, open education) to now. It’s not about the mean ability of folks to discern this stuff. To make the information environment better you focus on the people with time and interest in making it better and help them, just as people looking to make the environment worse have empowered and platformed people with an unusually intense interest in doing that. 

_Give people unusually invested in improving the information environment the tools and skills to do so._ And maybe the financial support. But that’s the game, and for people confused why I’ve started working with AI, the reason is pretty simple — that’s where the powerful tools are right now, and I don’t believe in unilateral disarmament. 

## Building a very basic AI photo detector in ChatGPT 4o

So with that in mind, here’s a tool I want to give to the antibodies in the information system. Go into ChatGPT and paste the following into a 4o prompt (please make sure it is 4o):
    
    
    We are going to make a photographic manipulation test suite. When I upload a photo and say "check for digital alteration" you will write and run python code to check it for AI production, compositing, colorization, and other digital manipulations. Do the following, and always show the resulting image: Local Contrast Variation: Canny edge detection, Gabor filter (multiple) Reflections And Highlights Consistency: Noise Pattern analysis (FFT), Lighting consistency (gradient magnitude), reflection and highlights consistency. Check for colorization using B Channel (Color Consistency) check. Run Deep Learning-Based AI Detection, JPEG Compression Analysis, Patch-Based Anomaly Detection, Histogram Analysis, Saturation and Hue Irregularities When code executes successfully without error you will commit to memory that that method worked in this environment, and when code fails (i.e. errors out) you will commit to memory that that method failed and should not be used again. When done, answer whether the image was photoshopped, composited, digitally altered or blended, or AI-generated with a probability rating of low, medium, high, and explain your rating. Ready? If so, commit these instructions to memory and say "Upload a photo and say 'check for digital alteration'".

Now you can paste a photo in and ask for it to be checked for digital alteration, and it will run a very basic test suite of software tools on it, and give you output like this.

[](<https://substackcdn.com/image/fetch/$s_!gjxT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43650045-0ec7-4115-b634-caf562b93b10_920x767.png>)

[](<https://substackcdn.com/image/fetch/$s_!LR9D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b9bd19e-5559-4b20-8d13-ddefe98bc67d_810x582.png>)

[](<https://substackcdn.com/image/fetch/$s_!6U8x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd1090a4-f308-42ec-a50d-a798f77813c2_799x566.png>)

[](<https://substackcdn.com/image/fetch/$s_!FeGl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff291bfad-33ca-4d3a-90a2-8d62a721ced9_832x557.png>)

[](<https://substackcdn.com/image/fetch/$s_!YM3u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F338ea95e-5174-4c98-87a3-7eb044c008ff_835x538.png>)

[](<https://substackcdn.com/image/fetch/$s_!cH64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc22a5b2c-db45-42b9-99f6-5bc4afe1e2e2_845x654.png>)

[](<https://substackcdn.com/image/fetch/$s_!bhDR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a9e03bb-f8b7-47bf-939d-ef0ab745ee2d_839x676.png>)

This set of tools won’t capture some of the newer fakes, but it easily outperforms what most people can do “spotting” fakes, and has a considerably less false positive rate than I have observed with students and workshop participants. But my vision for this is that next time grandma shares AI slop or something a bit more polished you can run this through the detector and leave a comment that makes use of some of the evidence the tool produces, which will in turn increase your reputation as someone who knows a thing or two about AI photos and might be worth listening to. (It’s also maybe more helpful to tell a person that you ran something through analysis and show the results than to just post, “Oh, come on now!” no matter how good that may feel.)

If you want to try it on a photo I thought initially _might_ be AI, you can use this one (it isn’t):

[](<https://substackcdn.com/image/fetch/$s_!3Z8D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F380746ad-d0be-465e-8c5d-758d70eb61e0_1200x1600.jpeg>)

In my dream world, we combine this tool with a little mini-course in what these analyses mean (and don’t mean) why they work (and when the won’t). But the tool right now does some explanation, and you can prompt it for more if you want. And if a student takes a liking to it, maybe they go out and get a real test suite, one that can deal with the new generation of Mid-Journey stuff.

As always, ephemeral AI tools like this can get a bit flaky. No warranties are expressed or implied. If it doesn’t work, just try running it again, and if i still doesn’t work, tinker. 

It’s not a tool for everyone, but it’s a tool for the people that will make a difference. Try and get it to them — the antibodies — if you can.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
