---
title: "Create a diff tool in ChatGPT o1 with a few short sentences"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-02-17
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/create-a-diff-tool-in-chatgpt-o1
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Create a diff tool in ChatGPT o1 with a few short sentences

*A short little hack if you want to compare text files*

## Full text

There’s lots of diff tools for text online, but I got curious if I could single-command a diff processor into existence in ChatGPT’s o1. 

So I did.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

The text to build it is:
    
    
    **Canvas** On canvas build an interactive javascript page that takes in two text areas. One has initial text. One has revised text. When a button is pressed the page uses a javascript library to do a visual word level diff.

It will make you one of these:

[](<https://substackcdn.com/image/fetch/$s_!S4m9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F210af994-eac1-4f7e-a859-9b84715f30f9_1825x980.png>)Screenshot of diff tool it creates

If you need some text to compare you can use this:

**Original**
    
    
    The first song to feature a distorted guitar was "Rocket 88" by Ike Turner and the Kings of Rhythm, released in 1951. The distorted guitar was played by Willie Kizart. 
    
    The distortion was achieved by using a faulty tube amp that Kizart damaged during transport. The damaged speaker cone gave the guitar its unique buzzing sound. Other early examples of distorted guitar: 
    
    "Rock Awhile" by Goree Carter (1949)
    "Boogie in the Park" by Joe Hill Louis (1950)
    "The Things That I Used to Do" by Guitar Slim (1953)
    "Maybellene" by Chuck Berry (1955) 
    
    Guitarists began experimenting with distortion in the 1940s. They eventually started to deliberately damage amplifiers and speakers to achieve the desired effect. 

**Revised**
    
    
    While "Rocket 88" by Ike Turner and the Kings of Rhythm, released in March 1951, is widely recognized for its distorted guitar, some sources suggest it may not have been the absolute first.  The distorted guitar on "Rocket 88" was indeed played by Willie Kizart. 
    
    The distinctive distortion in "Rocket 88" is attributed to a damaged amplifier. As the story goes, the band's amplifier was damaged during transport, possibly affecting the speaker cone or a tube. This accidental damage resulted in the guitar's unique, buzzing, distorted sound. Other early examples of recordings featuring distorted guitar, which may predate "Rocket 88", include: 
    
    "Rock Awhile" by Goree Carter (1949) 
    "Boogie in the Park" by Joe Hill Louis (1950)
    "The Things That I Used to Do" by Guitar Slim (1953) 
    "Maybellene" by Chuck Berry (1955) 
    
    Guitarists' experimentation with achieving distortion effects reportedly began in the 1940s. Early methods to create distortion included deliberately damaging amplifiers and speakers or overdriving tube amplifiers. "Rocket 88" is nonetheless considered a pivotal recording in popularizing and bringing the sound of guitar distortion to a wider audience in rock and roll music.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
