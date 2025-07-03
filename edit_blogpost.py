#!/usr/bin/python3

import frontmatter
import os
import subprocess
import re
from io import BytesIO
from datetime import datetime
import time
from blogpost_func import addImage
from blogpost_func import selBlog

filePath = selBlog()
print(f"checking {filePath}")

fpFront = frontmatter.load(filePath)
if (fpFront["image"] == ""):
    print ("No image in this blog post.")
else:
    print ("There is an image already in this blog post.")

print("Do you want to change the image? Y/y/yes")
input1img = input()
input2img = re.sub(r'^[Yy][Ee]?[Ss]?$', '', input1img)
imageDetailsTuple = tuple(())


# completely reorders the frontmatter in alphabetical order. probably fine.
if (not(input2img)):
    # deal with the image.
    fpFront["image"] = ""

    imageDetailsTuple = addImage(filename)
    fpFront["image"] = imageDetailsTuple[0]
    fpFront["imageAlt"] = imageDetailsTuple[1]

    updatedFile = BytesIO()
    frontmatter.dump(fpFront, updatedFile)

    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(updatedFile.getvalue().decode('utf-8'))
    print(f"Image frontmatter changes written to {filePath}")
else:
    print("Ok. Editing the blog post.")


print("press enter to continue...")
input()



# If it exists, edit. If no, don't
if os.path.exists(filePath):
    subprocess.run(["code", "--wait", filePath])
else:
    print("File does not exist!")
    exit()

# Ask for changes
print("push changes?")
input1 = input()
input2 = re.sub(r'^[Yy][Ee]?[Ss]?$', '', input1)

if not(input2):
    subprocess.run("./push_blog.sh")
else:
    print("ok. run    './push_blog.sh'     to push the changes!")