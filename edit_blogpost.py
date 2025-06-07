#!/usr/bin/python3

import frontmatter
import os
import subprocess
import re
from datetime import datetime

# List all files in blogs (list all blogs)
blogPath = "./src/pages/blogs/"
existingBlogs = os.listdir(blogPath)

# Remove the images dir
if "images" in existingBlogs: existingBlogs.remove("images")

postDic = {}

for post in (existingBlogs):
    print("\n" + post)
    postMatter = frontmatter.load(f'{blogPath}{post}')
    print(postMatter['specificDate'])
    postDic[post] = postMatter['specificDate']

print(postDic)

existingBlogs.sort(key=lambda filename: postDic[filename], reverse=True)

print(existingBlogs)


# Make a new array for the human readable names
fancyBlogNames = existingBlogs.copy()

# Make them human readable
for i, string in enumerate(fancyBlogNames):
    fancyBlogNames[i] = " ".join([f"{i}",string.replace("-"," ").replace(".md",""), "       ",postDic[f'{existingBlogs[i]}']])

# Print the names and ask for input
print(f"Current blogs in {blogPath}:\n\n{"\n".join(fancyBlogNames)}\n")
print("which blog do you want to edit? (you can ignore the .md and dashes, or just input the number of the target blog)")
filename = input()

# If it's not the number of one, find the name. if it is, use the file that it corresponds to
if(not(filename.isdigit())):
    filename = re.sub(r'[^a-zA-Z0-9 ]', '', filename).replace(" ", "-").replace("	","").lower().rstrip().lstrip() + ".md"
else:
    filename = existingBlogs[int(filename)]

filePath = "".join([blogPath, filename])
print(f"checking {filePath}")

# If it exists, edit. If no, don't
if os.path.exists(filePath):
    subprocess.run(f'nano {filePath}', shell=True)
else:
    print("File does not exist!")
    exit()

# Ask for changes
print("push changes?")
input1 = input()
input2 = re.sub(r'^[Yy][Ee]?[Ss]?$', '', input1)

if "" == input2:
    subprocess.run("./push_blog.sh")
else:
    print("ok. run    './push_blog.sh'     to push the changes!")