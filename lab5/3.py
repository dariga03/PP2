#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
string = input()
x = re.findall("[a-z]+_[a-z]+", string)
print(x)


"""import re
def find(txt):
        x = '^[a-z]+_[a-z]$'
        if re.search(x,  txt):
                return 'Found a match!'
        else:
                return('Not matched!')

print(find("dori_o"))
print(find("Dori_Alibekovna"))
print(find("darigA_ORAZBAI"))
print(find("a_b_c"))"""