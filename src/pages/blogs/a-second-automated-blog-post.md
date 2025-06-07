---
layout: '../../layouts/blogLayout.astro'
title: 'A Second Automated Blog Post'
desc: 'Testing the automated deployment of blogs!'
date: 'June 6, 2025'
specificDate: '2025-06-06T18:00'
author: 'Griffin Rzewnicki'
---
# Automated Deployment of Blogs

---

## Why?
Automating the deployment of blogs is good for many reasons.
* It simplifies the blogging process, removing an extra step.
* It makes the commit process identical each time, cutting down on user error and making it easer to find the commits of blogs.
* It's cool.

Now that that's cleared up, on to the *how*.

---

## How?
This is done through two scripts:
* A python script, [blogpost.py](https://github.com/BitflipFTC/website/blob/main/blogpost.py), which creates the actual blogpost and handles the formatting
* A bash script, [push_blog.sh](https://github.com/BitflipFTC/website/blob/main/push_blog.sh), which uploads the changes to github by using a Personal Access Token (PAT).

---

And that's just about it. It's a simple thing to make, but it makes creating blogs significantly easier.
