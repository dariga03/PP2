#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

path = input("Enter the path to be deleted:\n")

if not os.access(path, os.F_OK):
    print("Wrong path")
    exit()
if not os.access(path, os.X_OK):
    print("Path is not available")
    exit()

