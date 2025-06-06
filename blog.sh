#!/usr/bin/bash
while [ "true" = "true" ]
do
    echo "Creating new blog post. Enter the name of the blog post"
    read -r fileName
    echo "Set name to $fileName"

    echo "Enter the name of the image to use as a header. If the image is the wrong resultion, or aspect ratio, or"
    echo "if you get the URL wrong, it will be hard to fix, so be careful."
    read -r imageUrl
    echo "Set URL to $imageUrl"

    echo "" > "temp.txt"
    vim "temp.txt"


    #this is the main thing that this script does. it needs to auctually make the new file
    currentDate=$(date "+%B %-d, %Y")
    nameForHtml="$fileName On $currentDate"
    echo "Name of file being created is '$nameForHtml'"
    touch "blog/${fileName}.html"
    baseString=$(< "blogbase.html")

    textToUse=$(< "temp.txt")
    textToUse=$(sed ':a;N;$!ba;s/\n/<br>/g' temp.txt)


    baseString="${baseString//replace-this-text/$textToUse}"
    baseString="${baseString//replace-this-url/$imageUrl}"
    baseString="${baseString//replace-this-title/$fileName}"


    echo "$baseString" > "blog/${fileName}.html"


    #deal with putting the new data into blog.html
    currBlogText=$(< "blog.html")
    recursiveText="<div>And more coming soon...</div>"
    recursiveAddition="$recursiveText <a href='bitflip.club/blog/${fileName}.html'> $fileName </a>"

    # Escape slashes for use in sed
    currBlogText=$(< "blog.html")
    recursiveText="<div>And more coming soon...</div>"
    recursiveAddition="<div class='blog-card'>  <img src='${imageUrl}'> <a href='https://bitflip.club/blog/${fileName}.html'> $fileName </a> </div> $recursiveText"

    # Escape variables for use in sed
    escapedText=$(printf '%s\n' "$recursiveText" | sed 's/[&/\]/\\&/g')
    escapedAddition=$(printf '%s\n' "$recursiveAddition" | sed 's/[&/\]/\\&/g')

    # Perform the replacement
    currBlogText=$(echo "$currBlogText" | sed "s/$escapedText/$escapedAddition/")

    echo "$currBlogText"

    echo "$currBlogText" > "blog.html"


    #update the git repo
    printf "\n\n\n=============\n"
    echo "Pushing this update"
    ./push_blog.sh
    printf "=============\n\n\n"

    echo "Would you like to continue (make more posts)? yes/Yes/YES/y/Y"
    read -r continue
    if [ $continue = "yes" ] ||  [ $continue = "Yes" ] || [ $continue = "YES" ] || [ $continue = "y" ] || [ $continue = "Y" ]; then
        echo "Continueing" 
    else
        exit
    fi

done