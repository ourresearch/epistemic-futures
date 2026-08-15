---
title: "Course Signals and Analytics"
person: mike-caulfield
section: by
type: blog-post
year: 2012
date: 2012-08-24
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2012/08/24/course-signals-and-analytics/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Course Signals and Analytics

## Full text

I have been looking a little more closely at the Course Signals research since I mentioned it in my Post-Content LMS whitepaper, and it’s — well, it’s a more complex story than I first thought.

First, there’s this [interesting finding](<http://www.itap.purdue.edu/learning/research/pdf/Arnold_Pistilli-Purdue_University_Course_Signals-2012.pdf>):

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2012/10/www-itap_-purdue-edu-learning-research-pdf-arnold_pistilli-purdue_university_course_signals-2012-pdf.png>)

The graph says that those students from the 2009 cohort who have at least one course with CS persist to year 2 at a 1.3% higher rate than those without such courses. That’s good stuff, especially with the balance in the numbers between these compared groups. The earlier 2007 cohort data possibly overstates the impact due to an adoption bias, but the 2009 data is showing impact as it nears scale.

All fine and good. But the graph also says that students that have  _one_ course with CS persist at a 1%  _lower_ rate than their non-CS counterparts.

(Yes, lower).

Can you find an explanation for this? Sure. There might be a lot of remedial classes using CS. There might be high-retention majors not using it. But it’s an odd fact, and deserves picking at. If you are building a causal argument, you like to see a nice clean dose-response effect. J-curves exist, of course, but are generally an indication that the story is more complex and multi-factored than we want to admit.

Here’s the second thing — look at the non-CS 2 year retention rate in 2007.

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2012/10/www-itap_-purdue-edu-learning-research-pdf-arnold_pistilli-purdue_university_course_signals-2012-pdf2_.png>)

It’s 73%. Now compare it to the non-CS 2 year retention rate in 2009. It’s **82%**. That’s a huge 9% gain in a short span of time that has nothing to do with analytics in the narrow sense, and one that actually dwarfs the cross-sectional differences we were just looking at. And it means that, in general, longitudinal comparisons of classes before and after CS adoption are likely suspect — there are massive things afoot at Purdue that are increasing student retention semester over semester, and it shouldn’t be a surprise if your 2010 course with CS demonstrates better outcomes than your 2008 course without it, because, on average, classes in 2010 are likely doing better all around.

Do I think this means Course Signals is snakeoil? Far from it. If I had to bet money, I’d say CS is having some impact, and that when the numbers and research firms up that impact will be demonstrably positive. But what these numbers remind me is that we get too focused on the wrong questions when it comes to things like analytics. Assuming I’m not missing a broad student demographic change, it’s very clear that the culture around this tool has had more impact than the tool itself.

In other words, we are far to early in this enterprise to peel apart how much success at Purdue was the tool, and how much success was the conversations around the tool, and how much success had nothing to do with the tool. Until we can peel apart those impacts more precisely, quoting x% increase or y% decrease around tool adoption as a way to compare products is meaningless.

What is not meaningless is this — it’s clear that this retention effort that involved analytics and other measures succeeded. It’s likely the technology played a strong positive role in that, and it’s possible that some of that role was indirect. It’s possible to move the needle on this. What affordances did the particular implementation offer, and how might we learn from them in our own initiative? In what ways did analytics change the culture of the classroom and institution, and do our own technology decisions support those types of shifts? How does our own technology hinder (or actively work against) these types of shifts? How do we change that?

In other words, technology matters, but it matters most at its intersection with culture, and that intersection needs to be the focus. Of course, you have to look at bugginess, stability, security, must-have features and other issues. But past a certain baseline level of functionality, tools are about culture. Choose tools that foster the right culture, and discard those that don’t. That’s your one line technology plan. It won’t lead you astray.

**Update:** Incidentally, there’s an interesting potential confounder in the “2 or more” category, and I can’t tell if it is controlled for skimming the paper. Briefly — which student is like to have had two or more classes with CS — a student that dropped out after one semester? Or a student that stayed for two semesters? Obviously the two semester student — they have taken more courses, so they are likely to have taken more CS courses as well.

That would distort the data, quite a bit.

I’ve only skimmed this, but I can’t see where that is controlled for. Can someone help? (Again, I’ve only skimmed, I may be missing something obvious).

**Additional Update:** There’s a second issue too, less important, maybe. But at Keene, taking a low number of classes (say 3) is correlated with less persistence than taking a high number of classes (say 5). So again, the student that is more likely to persist may also be more likely to end up with more CS classes — they will take 10 classes in a year, whereas the low-persist students will take 6. If 15% of each student’s classes are CS, the low persist student will get one CS class, whereas the high persist student is as likely to get 2 as to get one. Again, just thinking out loud, but worth a look.
