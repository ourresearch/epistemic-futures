---
title: "Tagging Motel Noir"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-06-20
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/tagging-motel-noir
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Tagging Motel Noir

*An example of how LLM projects find depth, and how people find curiosity*

## Full text

As you all know, I’ve been working on this [plot.fyi](<https://plot.fyi/>) project for a while, my film discovery tool. But the point of the project is really a point about education. When you engage in making something real and substantial with an LLM you end up deepening your understanding and appreciation of the world. That seems an important point for education.

Here’s an example. I’ve gotten interested in film noir recently, so I went through and tagged my database with film noir tags. I had that initial pass include both classic film noir (before 1960s) and so-called neo-noir (after the 1960s). Because I do this as an investigation and discovery effort, I tell the tagger to be pretty loose with what qualifies as film noir. I get this this set of 1200 films from my database. And again, purpose animates this set. I’m interested in finding new connections, so we allow films outside classic noir if they fit on a number of dimensions, but not all.

[All Film Noir](<https://plot.fyi/q?s=%3Dfilter%20with%3Ais_film_noir&v=card&p=Q700736>)

[](<https://substackcdn.com/image/fetch/$s_!AhED!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6d79c32-347f-4373-aa6d-3e8c1cb17c3c_1474x1012.png>)

The definition is of noir we use for tagging is pretty simple, because there is already a cultural understanding of it the LLM can access. So we don’t have to say anything more than “tag anything that is film noir or seems film noir adjacent.” (When doing tagging, it is best to cast a broad net then prune if necessary). 

And so I started watching some of these films, using the recommendation engine. I ended up watching a set of John Dahl films, including the 1989 film [Kill Me Again](<https://plot.fyi/s/Q1503911?v=card>). And I started thinking about how there was a particular subset of noir that I enjoyed a lot that wasn’t the noir of cops and gangsters, and wasn’t even the noir of the large city. And it wasn’t the professional class anxiety noir of something like Basic Instinct or Fatal Attraction. Instead it was the noir of the drifter who gets a dubious opportunity, the small time crook or day laborer who finds a suitcase full of cash, the person who arrives in a small town fleeing a past that eventually catches up to them anyway. For whatever reason, the term that occurred to me was “motel noir” which didn’t encompass everything but for me captured the feel of it, or at least a core of it.

## Writing the definition

I wrote out as best I could in a rambling way my definition for the LLM and asked it to find a selection of things in the vault that the definition would exclude, and things it wouldn’t. So you go back and forth with the LLM. _Fatal Attraction_ is rightly out, but what about _Body Heat_?

Well, that’s an interesting question! _[Body Heat](<http://low-rent lawyer Ned Racine>)_ feels to me on the border, but in. But that blows up my definition, because William Hurt in that is a lawyer, which is professional class. It feels like it should still be included though, so why is that? 

I think it’s the fact that he is a low-rent lawyer reaching up. He’s imagining for a moment he might have access to a world that is clearly not made for him. And this forms a fundamentally different structure than the professional class anxiety noir I’m looking to exclude, where the character has a substantial life to protect, and the noir is less about escaping that life than protecting their family, their status, and so on from an outside force disrupting it. I mentioned this in the back and forth of constructing the definition, and had the LLM hit me with more examples of what that would include, and exclude. That led to more questions, more tinkering with the definition, and so on.

It went on this way for about an hour. Tightening and loosening the definition and seeing what that would do to the selection. I did about 40 minutes in Claude, and then I did a thing that I’ve been doing lately which is porting it over into ChatGPT to do another round and finish it up. (ChatGPT is just a bit less convulted in its language right now than Claude).

I provide the definition below so you can see what a detailed tag might look like. Most of my tags are not this! They are a paragraph at most. But for something of special interest where the category is self-constructed, this is what you might want to do. If you scroll past this next section, I show what it produced. 

# The Definition

## Motel noir is the noir of escape velocity.

Its protagonists occupy the broad lower middle of society: laborers, small proprietors, salesmen, mechanics, deputies, bartenders, bookmakers, motel owners, drifters, and their spouses or partners. They possess enough stake in the world to imagine a better life, but not enough power, wealth, or institutional protection to secure it. Motel noir is a genre of ordinary people confronting extraordinary opportunities.

## Conditions

A film is motel noir when all four conditions are present.

### 1: Station

The central figures live by their labor or by a single small enterprise. They are neither destitute nor securely established. They have something to lose and something to gain.

What matters is not occupation but position. Motel noir concerns people seeking a larger life, not people defending an established one.

### 2: Independence

The protagonist acts outside organized structures of power.

They are not members of a criminal organization, and they do not operate principally through corporations, governments, courts, hospitals, universities, or other major institutions. The central scheme is freelance: a murder, affair, theft, fraud, blackmail, windfall, or improvised opportunity pursued by individuals.

An organized criminal group may appear as an external force. What matters is that the protagonist does not belong to it.

### 3: Escape Velocity

The plot turns on an attempt to enter a life otherwise unavailable to the protagonist.

The object may be money, property, status, freedom, security, a business, a desired lover, or an entire social world. The desired prize is typically life-changing for the protagonist but insignificant to society at large.

The opportunity may be legal or criminal. The attempt to seize it destabilizes the protagonist’s world.

### 4: Setting

The story takes place outside a major metropolis.

Small towns, rural districts, borderlands, highways, deserts, mountains, industrial backwaters, and isolated communities qualify. Motels, diners, gas stations, bars, roadside businesses, and car lots are common but not required.

A major metropolis does not.

## Confirmatory Markers

None are required, but their presence increases confidence.

• A drifter, traveler, or newcomer arrives from elsewhere.  
• A proprietor, proprietor’s spouse, and outsider form the central triangle.  
• A windfall is found, stolen, inherited, or fought over.  
• A desired lover represents entry into another life.  
• The highway delivers opportunity and then delivers consequences.  
• Individuals compete over money, desire, or escape without institutional protection.  
• The protagonist mistakes a temporary opportunity for a permanent solution.

## Exclusions

### 1: Organized-Crime Noir

The protagonist is a member, employee, or subordinate of a criminal organization, and that organization constitutes the film’s primary social world.

### 2: Professional-Class Noir

The central figures are securely established members of a professional, managerial, or ownership class. The drama concerns preserving, defending, or exploiting an already elevated position rather than escaping the limits of an ordinary one.

### 3: Rural-Poverty Noir

The protagonists possess no meaningful stake to leverage. The story concerns subsistence, survival, or generational deprivation rather than aspiration.

### 4: Institutional Noir

The decisive action occurs through institutions rather than through freelance schemes undertaken by individuals.

## Boundary Cases

  * A professional-class figure who descends into a small-place, freelance world may qualify if the film’s social logic is motel noir rather than professional noir.

  * A protagonist who steals, finds, or inherits money belonging to an organization remains eligible if the organization functions as an external force rather than the protagonist’s world.

  * Outlaw couples, folk heroes, and legendary criminals may satisfy the formal criteria while remaining peripheral to the category. Motel noir is most centrally concerned with ordinary people reaching beyond their station, not with the creation of public myth.

# OK, that was the prompt. What did I do with it?

Once you have the prompt, you put it in a markdown file and ask the LLM to read it and apply that definition to everything we’ve tagged film noir. If it meets the definition (on a more sure than not basis), tag it is_motel_noir. When you do that, you get this, a set of 112 films, just under 10% of the noir in the database.

[Motel Noir Set](<https://plot.fyi/q?s=%3Dfilms-with%20a%3Ais_motel_noir&v=card&p=Q20026847>)

[](<https://substackcdn.com/image/fetch/$s_!T3ZN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2bbe1ec-c1a7-46e0-80ee-b5a575d2d778_1597x985.png>)

(Note that I don’t describe how to set up a tagging architecture here; for that you’ll have to read previous posts).

There’s a bunch of stuff here I’ve seen and loved, and in the 112 films there is much much more that I haven’t. Which is the point! I have a whole world of film out there waiting for me, and one which I will be watching with this lens of class anxiety and escape velocity. 

Life is good.

# IANAFS: I Am Not A Film Scholar

Maybe I worry about this bit too much, but I write things like this and I hear the voice of a random academic in my head saying “Well this is garbage, you’ve basically recreated ‘country noir’” (I haven’t) or saying I’ve missed some crucial thing.

Maybe. Probably, in fact! 

But if you’re the person who has arrived to tell me that in an aggressive way in the comments, you’re missing the point of this whole exercise.

_I chose this project because I do not have expertise here_. Every time I would do a project inside my expertise people would rightly point out that I could only learn from it because I had expertise already. So I decided to learn more about film, something that I had sort of forgotten I liked after 15 years of watching TV shows over films. 

Is my categorization scheme going to be published in a highly-rated film journal? No. But that’s not the point for me and that’s not the point for 99.9% of the students we teach about film. The point is whether we can use the resources at our disposal to engage with our world with a bit more intentionality, curiosity, and appreciation. 

I don’t think that I will become a scholar here, but I’m having a blast watching these films, and as I go through them I’m reading about the history and nature of noir, the relationship between gender and class anxiety in the 1990s, and dozens of other things. That’s made my life better, and that’s a better result than most “educational software” has provided me previously. I think it would be a neat experience for our students as well.
