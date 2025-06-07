#!/usr/bin/python3
import subprocess
from datetime import datetime
import os
import re


blogPath = "./src/pages/blogs/"

# Get the name of the new blog post
titleIsValid = False

while (not(titleIsValid)):
    print("Enter the blog post title / filename (only alphanumeric characters and spaces): ")
    nameString = input().rstrip().lstrip()
    nameString = re.sub(r'[^a-zA-Z0-9 ]', '', nameString)
    filename = nameString.replace(" ", "-").replace("	","").lower() + ".md"
    print(f"Title: {nameString}")
    print(f"File name: {filename}")

    # If it already exists, dont overwrite
    if (os.path.exists("".join([blogPath,filename]))):
        print("Name already exists. try again\n")
    else:
        titleIsValid = True


print("Who is the author? (Format: John Doe)")
author = input().rstrip().lstrip()

# yay umlaut
if author == "Zoe Rzewnicki":
    author = 'Zoë Rzewnicki'

# Get the desc of the post
print("Enter the blog post description (try to keep it to one or two sentences): ")
desc = input()

#Get the image of the blog post
#print("Enter the blog post image: ")
#urlString = input()

# Specific date for post ordering, current date for human viewing
currentDate = datetime.now().strftime('%B %-d, %Y')
specificDate = datetime.now().isoformat(sep="T", timespec="minutes")

#Create the new blog post frontmatter
blogContent = f"""---
layout: '../../layouts/blogLayout.astro'
title: '{nameString}'
desc: '{desc}'
date: '{currentDate}'
specificDate: '{specificDate}'
author: '{author}'
---
"""

#Make the text of the blog post
print("Press enter to edit blog contents")
dummyLine = input(); open('temp.md', mode='w').write(blogContent); subprocess.run('nano temp.md', shell=True)
blogPostText=open('temp.md').read()

open("".join([blogPath,filename]), mode='w').write(blogPostText)

# Remove the input file
os.remove('temp.md')


# Request pushing the changes
print("push changes?")
input1 = input()
input2 = re.sub(r'^[Yy][Ee]?[Ss]?$', '', input1)

if "" == input2:
    os.execl("./push_blog.sh")
else:
    print("ok. run    './push_blog.sh'     to push the changes!")