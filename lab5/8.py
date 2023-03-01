#Write a Python program to split a string at uppercase letters.

import re

string = input()
x = re.split("[A-Z]", string)
print(x)




"""
txt = "The rain in Spain"
x = re.split("\s[]", txt)
print(x)
"""