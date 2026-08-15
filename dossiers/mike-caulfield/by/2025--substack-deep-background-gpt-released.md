---
title: "Deep Background GPT Released"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-06-16
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/deep-background-gpt-released
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Deep Background GPT Released

*The world's best AI fact-checking tool is now available to all as a completely free GPT*

## Full text

[](<https://substackcdn.com/image/fetch/$s_!MNI0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c45f0c7-caa6-45ec-a9ab-0753091a65cd_1024x1024.png>)

**Update:** People rightly asked me for an introduction for people who have never used SIFT Toolbox. Here it is — **I just released a (largely) non-hallucinating1 rigorous AI-based fact-checker that anyone can use for free**. And I don’t say that lightly: I literally [co-wrote the book](<https://press.uchicago.edu/ucp/books/book/chicago/V/bo207015182.html>) on using the internet to verify things. All you do is log into ChatGPT, click the link below, and put in a sentence or paragraph for it to fact check.   
  
<https://chatgpt.com/g/g-684fa334fb0c8191910d50a70baad796-deep-background-fact-checks-and-context?model=o3>  
  
When you get there you should see this or something similar:  

[](<https://substackcdn.com/image/fetch/$s_!RVYf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8182dc8-6171-4858-8a29-57b1fff8552c_872x561.png>)

If you don’t try clicking the link again — sometimes after logging in ChatGPT gets a bit lost.  
  
You can click on one of the example prompts if you don’t know what to ask it to check. After its initial check, type “another round”. Watch it double-check its check. When that’s done, type “context report” for a nice little summary. You’re done.

For instance, there’s a story in Education Week just out that says that playing chess can boost performance in other academic subjects. Is that true? First, make sure you are using o3:  

[](<https://substackcdn.com/image/fetch/$s_!pSoc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0332be4b-0aaf-4b8a-878d-d4e152f22ac1_712x328.png>)

  
**PLEASE NOTE: IF YOU DO NOT USE o3 AS YOUR MODEL, YOU WILL RADICALLY INCREASE THE GPTs ERROR RATE FROM SOMETHING VERY LOW TO SOMETHING SUBSTANTIAL. USE o3.**

Type it in the claim and submit:  

[](<https://substackcdn.com/image/fetch/$s_!H48m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f7c8ab7-a5dd-4c32-bb36-41e677718563_1074x229.png>)

  
It will generate a list of facts from common assumptions, and return clarifications and source links for them all:

[](<https://substackcdn.com/image/fetch/$s_!96sO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a21bbee-0a82-4ec0-9d13-ff5fb85fd340_1143x558.png>)

It will identify what it believes may be errors, and show the sources that seem to conflict with the claims:

[](<https://substackcdn.com/image/fetch/$s_!Pzqz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38825257-45b0-4e41-b56c-f936ac9de33c_1137x538.png>)

It will give you a corrections summary:

[](<https://substackcdn.com/image/fetch/$s_!0PVX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f65a95-a7df-4fd6-98db-fb56cfb9fe79_1087x309.png>)

I could go on — it gives you a lot:  

[](<https://substackcdn.com/image/fetch/$s_!J84B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f2f9125-f7b2-4d58-a4d5-47bdc8d67536_1060x616.png>)

Please note you don’t need to read all of this. If you want to scroll down to what a fact-checker might say, or just the “Revised Summary” you can. The core of this product is that I force it to “show its work” but it’s up to you how much you want to check that work. 

After you get this, type and submit the phrase “another round” which will try to “fact-check the fact-check” and see if it missed anything. It will let you know whether going deeper found stuff that changed the initial assessment — or just reinforced it:

[](<https://substackcdn.com/image/fetch/$s_!vaQi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F002581ea-6819-4005-8bc4-a4f65ad8522d_1121x610.png>)

Finally, type “context report” to get a nice succinct summary of what was found of note:

[](<https://substackcdn.com/image/fetch/$s_!70sz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10409006-0dff-47af-95c1-e9add2842ee8_705x512.png>)

Happy checking!

## Original Post

  
I should write more about this later. It’s taken four hours to whittle down a version of SIFT Toolbox that can fit into a GPT and still function correctly, but I think I have done it. I did this because GPTs now let you choose any model so it can run on o3.

What this means is you no longer need to download a prompt and put it in a project and give Claude $20 a month. It’s now free to all. You just need to go here:  
  
[https://chatgpt.com/g/g-684fa334fb0c8191910d50a70baad796-deep-background-fact-checks-and-context?model=o3](<https://chatgpt.com/g/g-684fa334fb0c8191910d50a70baad796-deep-background-fact-checks-and-context>)

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

That means, also, that you can send your friends, family, and students there as well. For free.

It is not the full SIFT Toolbox: I have tried to get it as close as I could, while paring it down by more than two-thirds (from about 3,300 words to 1,100). I needed to do that because of limits on ChatGPT instruction length. But I think it’s still the best fact-checker/contextualization tool on the AI market. If you hadn’t already used to Toolbox, I doubt you’d notice.  
  
One note — because I had to make difficult decisions I pulled *all* of the image analysis instructions out — it can still do OCR on screenshots but won’t source images anymore. It’s a text fact-checker. 

I am still mourning all the stuff I had to take out. I still vastly prefer its performance on Claude. But I think this is going to open it to a dramatically larger audience. It’s the start of a beautiful friendship. 

If there was ever a post to share and restack widely, this is it. 

Spread the word! 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

1

I should clarify this. First, non-hallucinating does not mean error free — it means free of a certain type of error where stuff is just made up, not where things are confused or misinterpreted. Second, I’ve added “largely” in front of this, because I can only certify that in my many many tests it has not hallucinated, but past performance is no guarantee of future results. Plus — the hallucination-reduced performance in only for o3, the model I designed this for. Output on GPT-4o is an absolute mess. The prompt has always had a warning that all items need to be checked.
