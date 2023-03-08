#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

path = input("Enter the path: ")
if os.access():
    

    if os.access(path, os.R_OK):
        print("readable, ", end = "")
    else:
        print("unreadable, ", end = "")

    