#Write a Python program that matches a string that has an followed by zero or more 's.'a''b'

import re

string = input()
x = re.findall("ab*", string)
print(x)


"""string = input()

if re.search(r'a(b*)', string):
    print("Match found!")
else:
    print("Match not found.")"""
