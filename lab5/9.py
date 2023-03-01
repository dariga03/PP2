#Write a Python program to insert spaces between words starting with capital letters.

import re

string = input() 
print(re.sub(r"(\w)([A-Z])", r"\1 \2", string)) 