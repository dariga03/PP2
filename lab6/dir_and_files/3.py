#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

path = input("Enter the path:\n")

if not os.access(path, os.R_OK):
    print("Wrong path")
    exit()

print("Path exists:")

basename = os.path.basename(path)
dir_portion = os.path.dirname(path)

print(f"Directory portion: {dir_portion}")
print(f"filename: {basename}")