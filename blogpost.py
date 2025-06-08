#!/usr/bin/python3
import subprocess
from datetime import datetime
import os
import re
import requests

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
        print("Name already exists. try again\n")
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
print("Enter the blog post image: (leave it blank if you don't want an image)")
imagePath = input().lstrip().rstrip() # either a url or a local file
imageFinalPath = ""
imageAltText = ""

if (imagePath): #checks if it is blank
    isItAUrl = (re.match(r'^(http|https)://', imagePath))
    if (isItAUrl):
        response = requests.get(imagePath, stream=True)
        response.raise_for_status()

        with open("".join([filename,".png"]), 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        subprocess.run(f'mv {filename}.png ./src/assets/blog-images/', shell=True)
    else:
        subprocess.run(f"cp {imagePath} ./src/assets/blog-images/{filename}.png", shell=True)

    imageFinalPath = f'./src/assets/blog-images/{filename}.png'

    print(f'{os.path.exists(imageFinalPath)} is the validity of the image')

    print()
    print("Enter the alt text for the image (leave it empty if you don't want any)")
    imageAltText = input().lstrip().rstrip()



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
image: '{imageFinalPath if imageFinalPath else ""}'
imageAlt: '{imageAltText if imageAltText else ""}'
---
"""

#Make the text of the blog post
print("Press enter to edit blog contents")
dummyLine = input(); open('temp.md', mode='w').write(blogContent); subprocess.run('nano temp.md', shell=True)
blogPostText=open('temp.md').read()

open("".join([blogPath,filename,".md"]), mode='w').write(blogPostText)

# Remove the input file
os.remove('temp.md')

# Request pushing the changes
print("push changes?")
input1 = input()
input2 = re.sub(r'^[Yy][Ee]?[Ss]?$', '', input1)

if not(input2):
    subprocess.run("./push_blog.sh", shell=True)
else:
    print("ok. run    './push_blog.sh'     to push the changes!")