#!/usr/bin/python3
import subprocess
from datetime import datetime
import os
import re
from blogpost_func import addImage, pushChanges

blogPath = "./src/pages/blogs/"

# Get the name of the new blog post
titleIsValid = False

while (not(titleIsValid)):
    print("Enter the blog post title / filename (only alphanumeric characters and spaces): ")
    nameString = input().rstrip().lstrip()
    nameString = re.sub(r'[^a-zA-Z0-9 ]', '', nameString)
    filename = nameString.replace(" ", "-").replace("	","").lower()
    print(f"Title: {nameString}")
    print(f"File name: {filename}")

    # If it already exists, dont overwrite
    if (os.path.exists("".join([blogPath,filename]))):
        print("Name already exists. You can delete it by using delete_blogpost.py, or choose a new name.")
    else:
        titleIsValid = True


print("Who is the author? (Format: John Doe)")
author = input().rstrip().lstrip()


# filename same for image and md, dont add md until writing actual file 
# if has tpps, use wget, then move. if no http get the local image, copy

# yay umlaut
if author == "Zoe Rzewnicki":
    author = 'Zoë Rzewnicki'

# Get the desc of the post
print("Enter the blog post description (try to keep it to one or two sentences): ")
desc = input()

#Get the image of the blog post
imageTuple = addImage(filename)

# Specific date for post ordering, current date for human viewing
currentDate = datetime.now().strftime('%B %-d, %Y')
specificDate = datetime.now().isoformat(sep="T", timespec="minutes")



#Create the new blog post frontmatter
blogContent = f"""---
layout: "../../layouts/blogLayout.astro"
title: "{nameString}"
desc: "{desc}"
date: "{currentDate}"
specificDate: "{specificDate}"
author: "{author}"
image: "{imageTuple[0] if imageTuple[0] else ''}"
imageAlt: "{imageTuple[1] if imageTuple[1] else ''}"
---
"""

#Make the text of the blog post
print("Press enter to edit blog contents")
dummyLine = input(); open('temp.md', mode='w').write(blogContent); subprocess.run(["code", "--wait", "temp.md"])
blogPostText=open('temp.md').read()

open("".join([blogPath,filename,".md"]), mode='w').write(blogPostText)

# Remove the input file
os.remove('temp.md')


# Process 


pushChanges()