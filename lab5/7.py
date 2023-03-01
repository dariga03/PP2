#Write a python program to convert snake case string to camel case string.


import re

string = input() 
x = string.title().replace("_", "") 
print(x)

"""
def snake(str):
    x = r'_([a-z])'
    return re.sub(x, lambda y: y.group(1).upper(), str)

string = input()
camelString = snake(string)
print(camelString)
"""