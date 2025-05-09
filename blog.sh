#!/usr/bin/bash
while [ "true" = "true" ]
do
    echo "Creating new blog post. Enter the name of the blog post"
    read -r fileName
    echo "Set name to $fileName"

    echo "Enter the name of the image to use as a header. If the image is the wrong resultion, or aspect ratio, or"
    echo "if you get the URL wrong, it will be hard to fix, so be carefull."
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
    baseString="${baseString//replace-this-text/$textToUse}"
    baseString="${baseString//replace-this-url/$imageUrl}"
    baseString="${baseString//
    /"<br><br>"}"

    echo "$baseString" > "blog/${fileName}.html"

    printf "\n\n\n=============\n"
    echo "Pushing this update"
    ./testing.sh
    printf "=============\n\n\n"

    echo "Would you like to continue yes/Yes/YES/y/Y ?"
    read -r continue
    if [ $continue = "yes" ] ||  [ $continue = "Yes" ] || [ $continue = "YES" ] || [ $continue = "y" ] || [ $continue = "Y" ]; then
        echo "Continueing" 
    else
        exit
    fi

done