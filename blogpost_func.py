import re
import requests
import subprocess
import os

def addImage(filename):
    print("Enter the blog post image: (leave it blank if you don't want an image)")
    imagePath = input().lstrip().rstrip() # either a url or a local file


    # for wsl 

    imagePath.replace("C:\\", "/mnt/c/")
    imagePath.replace("\\","/")
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

