#!/usr/bin/bash
while [ "true" = "true" ]
do
    echo "Creating new blog post. Enter the name of the blog post"
    read -r fileName
    echo "Set name to $fileName"

    echo "" > "temp.txt"
    vim "temp.txt"
    
    echo "Pushing this update"
    ./testing.sh
done