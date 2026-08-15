---
title: "Learning Python the hard way: __init__.py needed for packages (as opposed to modules)"
person: selena-deckelmann
section: by
type: blog-post
year: 2011
date: 2011-02-09
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2011/02/09/learning-python-the-hard-way-__init__-py-needed-for-packages-as-opposed-to-modules/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Learning Python the hard way: __init__.py needed for packages (as opposed to modules)

## Full text

Just ran into this today, and wanted to get it down so I never forget: 

Modules are not packages! 🙂

From the docs, a *Module* is: 

> 
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

And a *Package* is:

> 
Packages are a way of structuring Python’s module namespace by using “dotted module names”.

When you create a module and you want other scripts to be able to reference it, you need an __init__.py in the directory containing the modules in order for Python to treat a directory as containing a package.

The error manifests as “ImportError: No module named XXXX”. 

All I had to do was touch __init__.py and things worked. I’m sure there are other things I’m going to learn today, but that was a silly one that I didn’t expect, and wasn’t mentioned in the Modules documentation, but [is mentioned in Packages](http://docs.python.org/tutorial/modules.html#packages).
