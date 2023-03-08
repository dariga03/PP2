#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

string = input()
upper = 0
lower = 0

for i in string:
    if 65 <= ord(i) <= 90:
        upper += 1
    if 97 <= ord(i) <= 122:
        lower += 1


print(f"{upper} upper case letters")
print(f"{lower} lower case letters")

