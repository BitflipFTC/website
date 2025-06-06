#!/usr/bin/python3
import subprocess
from datetime import datetime
import os
import re


blogPath = "./src/pages/blogs/"

#Get the name of the blog post
titleIsValid = False

while (not(titleIsValid)):
    print("Enter the blog post title / filename (only alphanumeric characters and spaces): ")
    nameString = input()
    nameString = re.sub(r'[^a-zA-Z0-9 ]', '', nameString)
    filename = nameString.replace(" ", "-").replace("	","").lower() + ".md"
    print(f"Title: {nameString}")
    print(f"File name: {filename}")

    if (os.path.exists("".join([blogPath,filename]))):
        print("Name already exists. try again\n")
    else:
        titleIsValid = True


print("Who is the author? (Format: John Doe)")
author = input()

# Get the desc of the post
print("Enter the blog post description (try to keep it to one or two sentences): ")
desc = input()

#Get the image of the blog post
#print("Enter the blog post image: ")
#urlString = input()


currentDate = datetime.now().strftime('%B %-d, %Y')

#Create the new blog post
blogContent = f"""---
layout: '../../layouts/blogLayout.astro'
title: '{nameString}'
desc: '{desc}'
date: '{currentDate}'
author: '{author}'
---
"""

#Get the text of the blog post
print("Press enter to edit blog contents")
dummyLine = input(); open('temp.md', mode='w').write(blogContent); subprocess.run('nano temp.md', shell=True)
blogPostText=open('temp.md').read()

open("".join([blogPath,filename]), mode='w').write(blogPostText)

os.remove('temp.md')

os.execl("./push_blog.sh")