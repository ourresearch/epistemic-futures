---
title: "Some Notes On Installing Federated Wiki On Windows"
person: mike-caulfield
section: by
type: blog-post
year: 2018
date: 2018-12-26
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2018/12/26/some-notes-on-installing-federated-wiki-on-windows/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Some Notes On Installing Federated Wiki On Windows

## Full text

It’s 2018, and I’ve still not found anything that helps me think as clearly as federated wiki. At the same time, running a web server of your own is still, in 2018, a royal pain. Case in point: recently a series of credit card breaches forced a series of changes in my credit card number (two breaches in one year, hooray). And that ended up wiping out my Digital Ocean account as it silently failed the monthly renewals. Personal cyberinfrastructure is a drag, man.

But such is life. So I recently started looking at whether I could do federated wiki just on my laptop and not deal with a remote server. It doesn’t get me into the federation, per se, but it allows all the other benefits of federated wiki — drag-and-drop refactoring, quick idea linking, iterative note-taking, true hypertext thinking. 

It turns out to be really easy (I mean as things go with this stuff). I’ll go into detail more below, but here are the steps:

  1. Download [Node.js for Windows](<https://nodejs.org/en/>). Install. 
  2. Open a command window and type: `npm install -g wiki`
  3. Launch via command window: wiki -p 80 –security_type friends –cookieSecret ‘REPLACE-THIS-SECRET’
  4. Navigate to localhost in a browser
  5. Click the lock to “claim” the wiki as owner
  6. Click the “wiki” link to take it out of read-only mode.
  7. Go forth and wiki…..

### Installation

**Step one:** Download [Node.js for Windows](<https://nodejs.org/en/>). Install.

**Step two:** Open a command window and type: `npm install -g wiki`

It’s installed!

###  Initial Startup

To start your wiki go to a command prompt and type: 
    
    
    wiki -p 80 --security_type friends --cookieSecret 'REPLACE-THIS-SECRET' 

You may need to give node some permissions. I won’t advise you on that. But you definitely don’t need to give public networks access to your server if you don’t want. 

Go to your localhost. You’ll get the start page. 

### Claiming your wiki

When you first visit your wiki it will be in **unclaimed, read-only mode,** and the bottom of the interface will look like this (though probably not have 47 pages):

When you click that lock icon, it will create a random username and go to unlocked position.

Once you do that you can click on the word “wiki” and now it will move out of read-only into edit mode:

You’ll know it’s in edit mode because you’ll see the edit history icons (sometimes colloquially referred to as ‘chiclets’) at the bottom.

**And — that’s it. You’re done. Wiki away.**

You’ll need to launch the server from a command window each time you want to use it, but if you’re familiar with Windows you can write a bat file and put it in your startup folder.

(Incidentally, this isn’t a tutorial on how to use federated wiki. I’m tired, frankly, of trying to sell it to people who want to know why it takes more than fifteen minutes to learn. I don’t teach people it anymore because people have weird expectations and it wastes too much of my time trying to get past them. But if you’re one of the people who has made the jump, you know this — I just want to help you do it locally on your laptop.)

### Optional stuff: Changing your name, importing or backing up files

You don’t need to know where files live on your computer, but sometimes it is useful. For instance, you might want to back up your pages, or reset a username. Here’s how you can do that.

In the single user mode we used above, wiki pages will be in a .wiki directory under your user directory. For instance, my directory is C:\Users\mcaulfield\\.wiki\pages. They are simple json files, and can be backed up and zipped. You can also drop json files from other wiki instances here, though you’ll have to delete the sitemap.json file to reindex (more on that below).

For ownership and indexing issues there is a status directory under the .wiki directory (e.g. C:\Users\mcaulfield\\.wiki\status). This has two important files in it. One is owner.json, which maintains login information (initially this will not be there — it’s written when you claim it). The other is your sitemap, which has a list of all pages and recent updates on them. Deleting the sitemap is useful when you want to regenerate it after manually uploading new files.

To change your username, you can edit the owner.json file. Change the name property. 

If something goes wrong and you want to reinitiate the claim process, you can delete the owner.json file. 

If you clear your cookies and hence loose your claim (i.e. are logged out), you can pull the secret from the json and enter it when prompted. It’s OK to change it to something simple and more password-like that you can remember.

The node files of your wiki installation will be in your AppData roaming directory under npm, e.g. C:\Users\mcaulfield\AppData\Roaming\npm\node_modules\wiki. There’s not an real reason to touch these files. 

### Running a personal desktop farm

This is only for federated wiki geeks, but it is completely possible to run a small personal desktop farm, where you can run multiple wiki sites in what are essentially separate notebooks. Just go into your hosts file (C:\Windows\System32\drivers\etc\hosts) and add localhost aliases:
    
    
    # localhost name resolution is handled within DNS itself.
    #	127.0.0.1       localhost
    #	::1             localhost
    	127.0.0.1       disinfo
    	127.0.0.1       journal
    	127.0.0.1       papersonwiki
    	127.0.0.1	sandbox
    	127.0.0.1	teachersguide
    	127.0.0.1	wikipediawomen
    	127.0.0.1	opioidcrisis
    	127.0.0.1	raceinamerica

Launch in farm mode (-f) and type these words into your browser omnibar. Each will maintain a separate wiki instance. If you want to be able to search across all instances, use the –autoseed flag. Note that you’ll have to go through the minimal claim process with each one (two clicks, shown above). 

### Pushing to a larger federation

If you want to push to a remote server, you can. There’s a couple ways to do this. 

First, there’s a flag in wiki that allows you to point to a different directory for pages. So you can point that to a mapped drive or Dropbox or whatever on your laptop, and then point a remote server to that same directory. 

Alternatively you could do a periodic rsync to the server. Windows 10 has bash native to it, so you can install that, reach your files through Bash for Windows’s /mnt/c/ mapping, and push them up that way. 

In each case, you probably want to delete the sitemap.json and sitemap.xml to trigger a regeneration.

Interestingly, you could also use this scheme (I think) for joint generation of a public wiki. 

IIRC, there is also a way to drag and drop json export files into wiki instances.

Finally, you can share files with people by zipping them up and emailing them or providing them as a zipped download. They in turn can drop them into their own federated wiki instance to work with. I’ve been thinking a lot about this model, which is very memex like — I make a notebook of my notes on something, post it up, you pull it into your machine. The provenance gets messy at scale, but among a group of people in a subfield that are being more descriptive in their practice than rhetorical this might work out fine. 

### It’s Good To Be Back

Using federated wiki again reminds me once again of what wiki means, in an etymological sense. It means quick. 

What all other non-federated wiki systems lack is not just federation. They lack quickness, largely because they are designed towards novices and trade away possibilities for fluid authorship in exchange for making the first 15 minutes of use easier. 

So while it may seem weird to run a federated wiki server on a laptop in a way that makes federation less available, if you’ve learned the method of multi-pane wiki it’s not really weird at all, because every note taking system you’ve used besides federated wiki is unbearably slow, clunky, and burdensome. Federated wiki, in the hands of someone that has mastered it, works at the speed of thought. And it does that whether your in the federation or not. So here’s to a very wiki New Year.
