#!/bin/python3

import re 
import os
import subprocess

print("Write a image: ![Alt text](Path to image)")

input_ = "![Alt text](C:\\Users\\griffin\\Downloads\\europawall.jpg)"
print (input_)
inputImage = input_.replace("C:\\","/mnt/c/").replace("\\","/")

print("Updated input is: " + inputImage)

#  /!\[.+\]?\((C:\\).+\)/gm