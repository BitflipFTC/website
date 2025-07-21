#!/bin/python3

import frontmatter
import os
from blogpost_func import selBlog, pushChanges
import re

filePath = selBlog()
blogFileName = filePath.split("/").pop()
print("deleting: " + blogFileName )

blogFrontmatter = frontmatter.load(filePath)
imageExists = (blogFrontmatter["image"] != "")
if (imageExists):
    print("There is an image.")
    imgFileName = blogFileName.replace(".md",".png")
    print("deleting: " + imgFileName)
else:
    print("There is no image.")

print("Are you sure you want to delete these file(s)?")
ans = input()
input2 = re.sub(r'^[Yy][Ee]?[Ss]?$', '', ans)

if not(input2):
    os.remove(filePath)
    if(imageExists):
        os.remove("src/assets/blog-images/" + imgFileName)

    print("All files were deleted.")
else:
    print("No files were deleted")

pushChanges()