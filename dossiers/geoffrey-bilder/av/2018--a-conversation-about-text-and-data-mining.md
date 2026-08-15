---
title: "A conversation about text and data mining"
person: geoffrey-bilder
section: by
type: talk-transcript
year: 2018
venue: "OpenMinTeD (Data Services Workshop, Lausanne)"
source_url: https://www.youtube.com/watch?v=p_DgAkZy1k4
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 10
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# A conversation about text and data mining

*Speakers (inferred):* speaker_0=Geoffrey Bilder, speaker_1=Panelist

## Transcript
**Geoffrey Bilder** [00:00]: [gentle music] I think the thing that I found, uh, most interesting when I started doing research is that the very word, uh, or the phrase text data mining is almost designed to mislead people. Uh, if you think about, um, diamond mining, uh, what are you doing? You're looking through dirt to try and find diamonds, right? Uh, if you're gold mining, you're looking through dirt, you're trying to find gold. What are you doing if you're looking for, you know, when you're doing text mining? Are you... What... First of all, what is it that you're looking through, and is it that you're trying to find text? Um, so right offhand, the sort of the parallelism, uh, i- it breaks down, and I think that that's been one of the confusions of, uh, of the phrase text data mining. The other being that it conflates two different things, uh, which is text mining, uh, which is a, a, a method of information extraction, um, and the data mining, which is the actual process of, of, of making sense of whatever you've extracted from the text. Um, uh, text mining, uh, makes sense. If you consider text to be the dirt and data to be the stuff you're trying to pull out of the text, right? Um, that kind of... that almost works. Text, uh, you know, and that is effectively what you're doing. You're trying to convert something that's designed for humans, uh, to, uh, consume and turn it into data that's designed for machines, uh, to consume. After that, there are normal data analysis processes that you perform on the data that you've extracted. But the fact that those two things are so, uh, closely coupled, you know, in the phrase, um, when they're actually two separate processes is, is, is very confusing to people.

**Panelist** [01:45]: So it is slightly confusing. There are many different steps in it. I think the, the most important one at the beginning, and that's what most people refer to, is the extract- extraction of information out of text, ideally less structured text particularly. So, uh, we do have often structured information in terms of metadata about many things that we're processing, and then we have very loosely structured or unstructured information. And I think that text and data mining particularly targets non-structured source, which is the dirt, and tries to extract the meaningful information out of it. So yes, so I think I completely agree with Jeffrey. Well, I think, I mean, access to the data is, is a big issue. So, uh, from a publishing perspective, there is quite a lot that you can do. So we're, we're having a big growth in scientific output. That is what I'm gonna talk today about as well. But, um, the way we need to deal to publish all of this content or to actually process all of this content is going to fundamentally have to change. And a part of that is that we do need the help of right, the right tools to assist the people that are dealing with this content. So today we have something that we call a, a process assistant. So we can do a lot around the process to help automate, find the right things, but we have very little we can do about the content itself. So I do think that the really big part will be that if we can get machines to understand the content of papers and be able to give you the right information at the right moment, that's gonna change fundamentally how we actually deal with publishing and with processing, with reviewing papers. And to do that, you do need access to all of this data and to all of these publish- published papers as an example, because only like that you can learn and create these type of tools.

**Geoffrey Bilder** [03:43]: So, um, I'd, I'd push that further in the process, and I'd point out, and I'm certainly not the first to point this out, uh, is that we are doing something, uh, rather peculiar here. Uh, if you think of the fact that lots of papers are written based on data, and then somebody is taking tools to turn this narrative back into data, uh, you have to ask, "Why aren't we making the data available in the first place?" And I think that that's one of the first things that I think, and it, you know, this conference in particular is probably talking about, which is, um, if we can make the data available in parallel with the narrative, then it's entirely possible that a lot of the, uh, the text and data mining, uh, might not, um, might not be needed in the future. Um, and, uh, I think that there's another point. If we accomplish that, um, obviously that will only occur, that will only happen for papers on an ongoing basis. So we still have this huge collection of information that's sort of, um, uh, uh, that's i- in narrative form at the moment that people want to, um, uh, retrieve it in, in, in some sort of a data form. And this is I think the other critical, um, bit of the process that a lot of people gloss over, and that is that, um, one of the, the interesting things about the process of text mining, that is taking text and turning it into data, is that it is, um, is actually helping you in a legal sense as well because text, which is subject to copyright and which may have all sorts of restrictions on it, um, is, uh, diff... You know, once you've actually extracted data from it, data is not subject to those kind, same kinds of restrictions. And so the process of actually turning, uh, that text into data is also a process of making it more usable and more reusable. Um, and I think that that's, that's something that isn't, uh, talked about enough. Uh, uh, again, it's sort of assumed that, um, that, that it's sort of one big process and that all of the same legal, uh, uh, things that apply to the text apply to the data that's extracted from it. And it's not, and that's not clear... That's not true at all. Um, and I think that bears more investigation.

**Panelist** [06:02]: I mean, um, so I agree with it partially, but I do think that even if we would have access to the data, we wouldn't have to get this information out of the text. The next step would be that we would need to make sense out of this data, which would be a very similar process to, to text mining. So, uh-

**Geoffrey Bilder** [06:19]: I, I, I completely agree, Wim, but the thing that I find circular there, right, is that we are saying effectively that there is more data in the text than in just the data, right? We've added something there, um, in narrative form, which means that it's not processable, and now we're trying to get that extra data, right? Uh, we're trying to effectively try and figure out what it is that the person has said in the narrative that interprets the, the, the raw data. I hate that phrase, but, um, whatever the, the, the paper was based on. And again, I think that you've got a, a group of people who would argue that, um, one of the things we may, uh, have better luck with is not, uh... is, is if we put that in narrative form, then also put it in some sort of machine-readable form rather than try and reverse engineer it, right?

**Panelist** [07:10]: Exactly.

**Geoffrey Bilder** [07:10]: So if there's some way that we can start embedding more semantic information in the paper, uh, to, to, to, um, to, to, to make that extra data that's being added, uh, uh, evidence, then that might also be an approach.

**Panelist** [07:24]: Exactly. So we still need a format that represents what the paper today represents.

**Geoffrey Bilder** [07:29]: Right.

**Panelist** [07:29]: But it doesn't have to be, uh, written in humanly read-readable text, but it should at least have on top of that-

**Geoffrey Bilder** [07:37]: Right

**Panelist** [07:37]: ... a better machine-readable, uh, semantic explanation of what it actually says.

**Geoffrey Bilder** [07:42]: Right.

**Panelist** [07:42]: But I think the, the opportunities that something like this has goes far beyond what we can actually imagine, uh, in terms of solutions that can be found. I mean, it's pretty much a tool that accelerates the work of scientists, because it can bring the right content to these people at the right time, and really be a great tool to make much bigger discoveries than what we're talking today.

**Geoffrey Bilder** [08:07]: And I think this illustrates, uh, an aspect of a lot of the things that at least I work on, um, and that is that infrastructure, and I consider the, you know, the, the, the, the requirements for doing text and data mining on a large scale require fundamental changes in infrastructure. Um, infrastructure... Building infrastructure is generally a faith-based activity, and what I mean by that is that the problem with infrastructure is it's not useful until it's big enough to be useful. So everybody who's participating in it in the early days is doing so based on possibly scant evidence, but a firm belief that eventually it will become useful. So for instance, a DOI system, when there were two publishers implementing DOIs, was not useful to anybody. It only became useful when a critical mass of, um, of people were adopting DOIs. Uh, same thing applies to physical infrastructure such as lighting or phones or whatever. Phones aren't useful if only two people have them. They only become useful if you have a lot of people have them. Text and data mining, I think, is probably under... has a similar property, which is that until we have enough data, uh, text mined, and enough data to analyze, um, the true benefits of the, the sort of the network effects that come from that won't be evident. So I, you know, I agree, uh, it's, it's actually really hard to predict, uh, what will come of it, largely because, um, because it's sort of a generative process, a network effect. [outro music]

