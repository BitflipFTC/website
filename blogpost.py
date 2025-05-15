#!/usr/bin/python3
import subprocess
from datetime import datetime

#Get the name of the blog post
print("Enter the blog post name: ")
nameString = input()

#Get the image of the blog post
print("Enter the blog post image: ")
urlString = input()

#Get the text of the blog post
print("Press enter to edit blog contents")
dummyLine = input(); open('temp.txt', mode='w').write(''); subprocess.run('vim temp.txt', shell=True)
blogPostText=open('temp.txt').read()

#Create the new blog post
baseText = open('blogbase.html').read()
baseText = baseText.replace('replace-this-url', urlString)
baseText = baseText.replace('replace-this-header', nameString)
baseText = baseText.replace('replace-this-text', blogPostText.replace("\n", '<br>'))
currentDate = datetime.now().strftime('%B %-d %Y')
fileName = "blog/" + nameString + " On " + currentDate + ".html"
open(fileName, mode='w').write(baseText)

#Update the blog.html file to have the new post
currentBlogPage = open('blog.html').read()
recrusiveText = '<div>And more coming soon...</div>'
formatedOutputCard = "<div class='blog-card'>" + "<img src='" + urlString + "'>" + "<a href='" + fileName + "'>" + nameString + " On " + currentDate + "</a> </div>" + recrusiveText
currentBlogPage = currentBlogPage.replace('<div>And more coming soon...</div>', formatedOutputCard)
open('blog.html', mode='w').write(currentBlogPage)