---
title: "Setting up a PDXAPI instance"
person: selena-deckelmann
section: by
type: blog-post
year: 2010
date: 2010-06-03
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2010/06/03/setting-up-a-pdxapi-instance/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Setting up a PDXAPI instance

## Full text

Today I spent a little time setting up a PDXAPI instance of the CivicApps data. There are a few different tools out there for grabbing the data and loading it up, and so I’m documenting the basic steps here for setting up a spatial SQLite using @lokkju’s python projects.


hg clone https://pyspatialite.googlecode.com/hg/ pyspatialite

cd pyspatialite
mv setup.cfg.OSX setup.cfg
python setup.py build
sudo python setup.py install

cd ..
cd pyod

hg clone https://pyod.googlecode.com/hg/ pyod

# unsatisfied dependency!
sudo easy_install pyyaml

pypython fetcher.py

This creates a 1 GB sqlite database called ‘test.sqlite’.

Next, I’ll be testing out loading this into a CouchDB instance and maybe playing with Max Ogden’s initial PostGIS export.
