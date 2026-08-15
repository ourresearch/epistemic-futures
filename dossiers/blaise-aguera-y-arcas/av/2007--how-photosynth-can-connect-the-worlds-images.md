---
title: "How PhotoSynth can connect the world's images"
person: blaise-aguera-y-arcas
section: by
type: talk-transcript
year: 2007
venue: "TED2007"
source_url: https://www.youtube.com/watch?v=M-8k8GEGZPM
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 9
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# How PhotoSynth can connect the world's images

*Speakers (inferred):* speaker_0=Audience, speaker_1=Blaise Aguera Y Arcas, speaker_2=Host

## Transcript
**Audience** [00:00]: [instrumental music] [applause]

**Blaise Aguera Y Arcas** [00:25]: What I'm gonna show you first, uh, as quickly as I can is, uh, is some, some foundational work, some, some new technology that, uh, that we brought to Microsoft as part of an acquisition, uh, almost exactly a year ago. Uh, this is Seadragon, and it's an environment in which you can either locally or remotely interact with vast amounts of, uh, of visual data. We're looking at many, many gigabytes of, uh, of, of digital photos here and kind of seam- seamlessly and, uh, continuously zooming and panning through the thing, rearranging it in any way we want. And, um, it doesn't matter how much information we're looking at, how big these collections are, or how big the images are. And the most of them are ordinary, uh, digital camera photos, but this one, for example, is a scan from the Library of Congress, and it's in the, in the 300-megapixel range.

**Audience** [01:07]: [laughs]

**Blaise Aguera Y Arcas** [01:07]: Uh, it doesn't, doesn't make any difference because the only thing that, that ought to limit the performance of a system like this one is the number of pixels on your screen at any given moment. Uh, it's also a very flexible architecture. Uh, this is an entire book, so this is an example of non, uh, non-image data. Uh, this is, uh, Bleak House by Dickens.

**Audience** [01:24]: [laughs]

**Blaise Aguera Y Arcas** [01:24]: Every, every column is, uh, is a chapter. And, uh, to prove to you that it's, that it's really text and not an image, we can do something like so, uh, to really show that this is, uh, a real representation of the text. It's not a picture. Uh, maybe this is a kind of an artificial way to read an e-book. I wouldn't recommend it.

**Audience** [01:40]: [laughs]

**Blaise Aguera Y Arcas** [01:40]: Uh, this is a more realistic case. This is an issue of The Guardian. Every, uh, large image is the beginning of a section, and this really gives you the, the, the joy and the good experience of reading, uh, the real paper version of, um, of a magazine or, or newspaper, uh, which is an inherently multi-scale kind of medium. We've also done a little something with the corner of, uh, of this particular issue of The Guardian. We've, uh, made up a fake ad that's very high resolution, uh, much higher than you'd be able to get in an ordinary ad. And we've embedded extra content. You gotta see the features of this car. You can see it here or, uh, other models, uh, or even technical specifications.

**Audience** [02:15]: [laughs]

**Blaise Aguera Y Arcas** [02:15]: And, uh, and this, this really, this really gets at some of these ideas about, uh, really doing away with, uh, with those limits on, on screen real estate. We hope that this means, uh, no more, no more pop-ups. No other kind of rubbish like that should be necessary.

**Audience** [02:26]: [laughs]

**Blaise Aguera Y Arcas** [02:26]: Um, of course, mapping is one of those really obvious applications for technology like this. And, and this one I, I really won't spend any time on except to say that we have things to contribute to this field as well. Um, but, uh, those are all the roads in the, in the US superimposed on top of a, of a NASA, um, geospatial image. So let's pull up, uh, now something else. So this is actually live on the, live on the web now. You can go check it out. This is a project called Photosynth, which really marries, uh, two different technologies. One of them is Seadragon, and the other is, uh, some very beautiful computer vision research done by, uh, Noah Snavely, a graduate student at the University of Washington co-advised by, uh, Steve Seitz at UW and Rick Szeliski at Microsoft Research, a very nice, uh, collaboration. Uh, and so this is, this is live on the web. It's powered by Seadragon. You can see that when we kind of do these sorts of views, where we can, we can, we can dive through images and have this kind of multi-resolution experience. Um, but, but the spatial arrangement of the images here is actually meaningful. The computer vision algorithms have registered these images together so that they correspond to the real space in which these, uh, these shots, all taken, uh, near Grassy Lakes in the Canadian Rockies, um, all these shots were taken. So you see elements here of, um, of stabilized slideshow or panoramic, uh, panoramic imaging. Um, and, uh, these things have all been related, related spatially. I'm not sure if I have, uh, if I have time to show you any other environments. There are some that are much more spatial. But I'd like to jump straight to, um, to one of Noah's original data sets, and this is from an early prototype of Photosynth that we first got working in the summer, uh, to show you what I think is really the, the punchline behind, uh, this, this technology, the Photosynth technology. And it's not necessarily so apparent from looking at the environments that we've put up on the website. We, um, we had to worry about the lawyers and so on. This is a reconstruction of Notre Dame Cathedral that was done entirely computationally from images scraped from Flickr. You just type Notre Dame into Flickr, and, uh, you get some pictures of guys in T-shirts and of the campus and so on. And, uh, each of these orange cones represents an image that was, uh, that was discovered to belong to this model. Um, and so these are all, these are all Flickr images, and they've all been related, um, spatially in this way, and we can just navigate in this very simple way.

**Audience** [04:32]: [laughs] [applause]

**Blaise Aguera Y Arcas** [04:38]: Thank you. You know, I never, I never thought that I'd end up working at Microsoft, and it's very, it's very gratifying [laughs] to have this kind of, this kind of reception here. Um-

**Audience** [04:51]: [laughs]

**Blaise Aguera Y Arcas** [04:51]: But, uh, so, so this is, uh, I guess you can see this is a very... This is, this is lots of different types of cameras. It's everything from cell phone cameras to professional SLRs. Uh, a quite a large number that have been registered together into this environment. If I can find some of the sort of weird ones, um, there, uh, so many of them are occluded by faces and, and so on. Um, there's, uh, somewhere in here, there's actually a, a, there, there are a series of photographs. Here we go. This is actually a poster of Notre Dame that registered correctly.

**Audience** [05:20]: [laughs]

**Blaise Aguera Y Arcas** [05:20]: Okay, so if we, uh, you know, we can, we can dive in from the poster to a physical view of this, of this environment. So what, what the point here really is, is that we can do things with the social environment. Uh, this is, this is now, uh, taking data from everybody, from the entire collective memory of, of, uh, visually of what the Earth looks like, and, uh, link all of that together. All of those photos become linked together, and they make something emergent that's greater than the sum of the parts. You have a, a model that emerges of the entire Earth. Think of this as, as the long tail to Stephen Lawler's, uh, virtual Earth work. Uh, and this is something that grows in complexity as people use it, and whose benefits become greater to the users as they, as they use it. Their own photos are getting tagged with metadata that somebody else entered. Uh, if, if somebody bothered to, um, to tag all of these saints and say who they all are, then, then my photo of Notre Dame Cathedral suddenly gets enriched with all that data. And I can use it as an entry point to dive into that space, into that metaverse, using everybody else's photos and, and do a kind of a cross-modal and, um, and, uh, and cross-user, uh, social experience that way. Uh, and of course, a, a by-product of all of that is immensely rich virtual models of, of every interesting part of the Earth, um, collected, uh, not just from, uh, from overhead flights and from satellite images and so on, but from the collective memory. Thank you so much.

**Host** [06:41]: [applause] Just wait, wait one sec. I've got one question for you. So do I, do I understand this, do I understand this right? That what, what your software is going to allow is that at some point, really within the next few years, all the pictures that are shared by anyone across the world are gonna basically link together.

**Blaise Aguera Y Arcas** [07:07]: Yes. What this is really doing is discovering, it's creating hyperlinks, if you will, between, between images. Uh, and it's doing that based on the content inside the images. And that gets really exciting when you think about the richness of the semantic information that a lot of those images have. Like, when you do a web search for images, right, you type in phrases, and the text on the webpage is, uh, is carrying a lot of information about what that picture is of. Now, what if that picture links to all of your pictures? Then the amount of semantic interconnection and the amount of richness that comes out of that is really huge. It's a classic network effect.

**Host** [07:35]: Blaze, that is truly incredible. Congratulations.

**Blaise Aguera Y Arcas** [07:37]: Thanks so much.

**Host** [07:37]: Yeah. [applause] [upbeat music]

