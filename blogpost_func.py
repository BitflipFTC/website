import re
import requests
import subprocess
import os
import frontmatter

def addImage(filename):
    print("Enter the blog post image: (leave it blank if you don't want an image)")
    imagePath = input().lstrip().rstrip() # either a url or a local file


    # for wsl 

    imagePath = imagePath.replace("C:\\", "/mnt/c/").replace("\\","/")
    print(imagePath + " is the fixed WSL image path")
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
    
    return (imageFinalPath,imageAltText)

def selBlog():
    # List all files in blogs (list all blogs)
    blogPath = "./src/pages/blogs/"
    existingBlogs = os.listdir(blogPath)

    # Remove the images dir
    if "images" in existingBlogs: existingBlogs.remove("images")

    postDic = {}

    for post in (existingBlogs):
        print("\n" + post)
        postMatter = frontmatter.load(f'{blogPath}{post}')
        print(postMatter['date'])
        postDic[post] = postMatter['date']

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
    return filePath

def pushChanges():
    # Request pushing the changes
    print("push changes?")
    input1 = input()
    input2 = re.sub(r'^[Yy][Ee]?[Ss]?$', '', input1)
    
    if not(input2):
        subprocess.run("./push_blog.sh", shell=True)
    else:
        print("ok. run    './push_blog.sh'     to push the changes!")