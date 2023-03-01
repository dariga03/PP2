#Write a Python program that matches a string that has an followed by two to three .'a''b'

import re

string = input()
x = re.findall("ab{2,3}", string)
print(x)
