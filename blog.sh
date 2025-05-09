#!/usr/bin/bash
while [ "true" = "true" ]
do
    echo "Creating new blog post. Enter the name of the blog post"
    read -r fileName
    echo "Set name to $fileName"

    echo "" > "temp.txt"
    vim "temp.txt"

    git add .
    git commit -m "update for today's news"
    PAT=$(< gitkey.txt)
    echo $PAT
    git push https://Krabbenhoft:$PAT@github.com/BitflipFTC/website.git main




done