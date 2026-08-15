---
title: "Uncovering the impact of software"
person: jason-priem
section: by
type: blog-post
year: 2013
date: 2013-01-18
venue: "Impactstory blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/github/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.impactstory.org."
---

# Uncovering the impact of software

## Full text

\
Academics — and others — increasingly write software.  And we [increasingly](http://www.gamesindustry.biz/articles/2013-01-17-github-sees-3-millionth-member-account) host it on [GitHub](https://github.com/).  How can we uncover the impact our software has made, learn from it, and [communicate this](http://blog.impactstory.org/2013/01/11/comment/) to people who evaluate our work?

![Screen Shot 2013-01-18 at 5.56.20 AM](http://impactstory.files.wordpress.com/2013/01/screen-shot-2013-01-18-at-5-56-20-am.png?resize=242%2C48)

GitHub itself gets us off to a great start.  GitHub users can “[star](https://github.com/blog/1204-notifications-stars)” repositories they like, and GitHub displays how many people have *forked* a given software project — started a new project based on the code.  Both are valuable metrics of interest, and great places to start qualitatively exploring *who* is interested in the project and what they’ve used it for.

What about impact beyond GitHub?  GitHub repositories are discussed on Twitter and Facebook.  For example, the GitHub link to the popular jquery library has been [tweeted 556 times and liked on Facebook 24 times](http://impactstory.org/item/url/https://github.com/jquery/jquery) (and received 18k stars and almost 3k forks).

Is that a lot?  Yes!  It is one of the [runaway successes](http://www.moretechtips.net/2012/08/most-forked-github-repositories.html) on GitHub.

**How much attention does an average GitHub project receive?** We want to know, to give [reference points](http://blog.impactstory.org/2012/09/11/31342582590/) for the impact numbers we report.  Archive.org to the rescue! Archive.org posted a list of [all GitHub repositories active in December 2012](http://archive.org/details/archiveteam-github-repository-index-201212).  We just wanted a random sample of these, so we wrote some [quick code](https://github.com/total-impact/total-impact-core/blob/master/extras/build_refsets/get_refsets.py#L93) to pull random repos from this list, grouped by year the repo was created on GitHub.

[Here is our reference set](http://impactstory.org/collection/s2dfrg) of 100 random GitHub repositories created in 2011.  Based on this, we’ve calculated that receiving 3 stars puts you in the top 20% of all GitHub repos created in 2011, and 7 stars puts you in the top 10%.  Only a few of the 100 repositories were tweeted, so getting a tweet puts you in the top 15% of repositories.

You can see this reference set in action on [this example](http://impactstory.org/item/url/https://github.com/ropensci/rfishbase), [rfishbase](https://github.com/ropensci/rfishbase), a GitHub repository by rOpenSci that provides an R interface to the fishbase.org database:

[![Screen Shot 2013-01-18 at 5.31.49 AM](http://impactstory.files.wordpress.com/2013/01/screen-shot-2013-01-18-at-5-31-49-am.png?w=362&resize=362%2C224)](http://impactstory.files.wordpress.com/2013/01/screen-shot-2013-01-18-at-5-31-49-am.png)

So at this point we’ve got recognition within GitHub and social media mentions, but what about **contribution to the academic literature?**  Have other people used the software in research?

Software use has been frustratingly hard to track for academic software developers, because there are poor standards and norms for citing software as a standalone product in reference lists, and citation databases rarely index these citations even when they exist.  Luckily, publishers and others are beginning to build interfaces that let us query for URLs mentioned within full text of research papers… all of a sudden, we can discover attribution links to software packages that are hidden in not only in reference lists, but also methods sections and acknowledgements!  For example, the [GitHub url for a crowdsourced repo on an E Coli outbreak](https://github.com/ehec-outbreak-crowdsourced/BGI-data-analysis) has been mentioned in the full text of [two PLOS papers](http://www.plosone.org/search/advanced?queryTerm=&unformattedQuery=everything:%22https%3A%2F%2Fgithub.com%2Fehec-outbreak-crowdsourced%2FBGI-data-analysis%22), as discovered [on ImpactStory](http://impactstory.org/item/url/https://github.com/ehec-outbreak-crowdsourced/BGI-data-analysis):

[![Screen Shot 2013-01-18 at 4.45.11 AM](http://impactstory.files.wordpress.com/2013/01/screen-shot-2013-01-18-at-4-45-11-am.png?w=628&resize=628%2C229)](http://impactstory.files.wordpress.com/2013/01/screen-shot-2013-01-18-at-4-45-11-am.png)

There is still a lot of work for us all to do.  How can we tell the difference between 10  labmates starring a software repo and 10 unknown admirers?  How can we pull in second-order impact, to understand how important the software has been to the research paper, and how impactful the research paper was?

Early days, but we are on the way.  Type in your [github username](http://impactstory.org/create) and see what we find!
