#Write a Python program to count the number of lines in a text file.

import os

path = input("Enter filename:\n")

if not os.access(path, os.R_OK):
    print("Wrong path")
    exit()

