#Write a Python program to convert a given camel case string to snake case.

import re 

string = input() 
x = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string).lower() 
print(x)
 
 
"""
def snake(str): 
 return str.group("g1")+ "_" + str.group("g2").lower() 
 
txt = input() 
x = "((.)([A-Z][a-z]+))+" 
 
print(re.sub(x, snake, txt))
"""


