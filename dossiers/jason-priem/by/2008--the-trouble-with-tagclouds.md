---
title: "The trouble with tagclouds"
person: jason-priem
section: by
type: blog-post
year: 2008
date: 2008-09
venue: "jasonpriem.org (personal blog)"
authors: "Jason Priem"
source_url: https://web.archive.org/web/20120723001757/http://jasonpriem.org/2008/09/the-trouble-with-tagclouds/
retrieved: 2026-08-13
content: full-text
notes: "Personal blog, defunct; retrieved from the Internet Archive Wayback Machine. Original URL: http://jasonpriem.org/2008/09/the-trouble-with-tagclouds/"
---

# The trouble with tagclouds

## Full text

![](http://jasonpriem.com/wp-content/uploads/2008/09/tagcloud3-300x188.png "A tagcloud of this very post.  How meta.")Tag clouds, those darlings of early web 2.0, have been seeing something of a backlash lately. [Zeldman](http://www.zeldman.com/) was [suggesting](http://www.zeldman.com/daily/0405d.shtml) that tag clouds were the new [mullets](http://en.wikipedia.org/wiki/Mullet_%28haircut%29) back in 2005; more lately, ReadWriteWeb wondered if tagclouds were [dead altogether.](http://www.readwriteweb.com/archives/tag_clouds_rip.php) The main complaint in both cases wasn’t that tag clouds were just no good, but that they’d become trendy and thus overused.  Later criticism has argued that the increasingly common practice of using tag clouds for navigation is [fundamentally flawed](http://www.zeldman.com/daily/0505a.shtml).

But the problems of tag clouds–and their close cousin, [word clouds](http://www.joelamantia.com/blog/archives/tag_clouds/text_clouds_a_new_form_of_tag_cloud.html)–go deeper, to their usefulness as a visualization method.  These aren’t problems with how the method is used or misused, but with the idea itself.

[Moritz Stefaner](http://well-formed-data.net/archives/42/tag-maps-update) points out (and presents his own solution for) several problems with the format:

- tag clouds give a great picture of the “big head” of tags: the most frequently used tags that change little over time; they overlook, though, the “long tail”–where many of the interesting tags are located.
- tag clouds don’t show change over time.  Chirag Mehta has created a tag cloud with a time slider, which helps with this.  But as Stefaner points out, animating tag clouds doesn’t work very well, as the changing size of the cloud moves the words around so they’re hard to follow.
- Finally, tag clouds don’t show the relationships between tags (pretty much everyone who criticizes tag clouds mentions this one).

The IBM [Many Eyes](http://services.alphaworks.ibm.com/manyeyes/page/Tag_Cloud.html) site has one of the best tag cloud (actually this does word clouds, too) tools I’ve seen, allowing users to get lots of data from each tag while keeping the interface clean and simple.  They make a great point about an inherent limitation of the tool: the size and shape of the words themselves isn’t controlled for.  So, long words seem more dominant than short ones, and words with lots of ascenders and descenders (the vertical strokes of letters like ‘b’ or ‘p’) tend to dominate as well.  This can subtly alter the overall gist that tag clouds are supposed to deliver.

The academic community has noted shortcomings of the technique, as well. [Hearst and Rosner (2008)](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4438863) observe that the alphabetical layout of the cloud may lead to a sort of “false clustering” effect, as users misinterpret words because of surrounding tags.  [Renninger and Shumar (2007)](http://portal.acm.org/citation.cfm?id=1240624.1240775) found that tag cloud quadrants have different rates of recall, a fact which most tag cloud designs ignore.  In fact, their findings suggest that a simple list of tags, ordered by frequency, may deliver a more accurate overall impression than a tag cloud.  Several researchers have sought to improve shortcomings in tag cloud presentation with packing and sorting algorithms that manage whitespace and cluster relevant concepts ([Kaser and Lemire, 2007](http://arxiv.org/abs/cs.DS/0703109); [Seifert, Kump, Kienreich, Granitzer, and Granitzer, 2008](http://csdl2.computer.org/persagen/DLAbsToc.jsp?resourcePath=/dl/proceedings/&toc=comp/proceedings/iv/2008/3268/00/3268toc.xml&DOI=10.1109/IV.2008.89)).

Now, this isn’t to say that tag clouds have no value; in fact, I think they have great potential. It’s just that we need to know when tag clouds and word clouds are appropriate, know their shortcomings, and (this is the fun part) try to find ways to make them better. Most of the sources cited above have set about doing just that. In my next post, I’ll discuss a few of these “next-generation tag cloud” concepts; in particular, I’ll be examining methods of using word clouds to compare different versions of a text.
