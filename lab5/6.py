#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

string = input()
x = re.sub("[ ,.]", ":", string)
print(x)