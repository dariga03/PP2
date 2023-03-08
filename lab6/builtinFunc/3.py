#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

string = input("Enter the string:\n")
str2 = string[::-1]
print(string == str2)

"""
a = str(input())

b = "".join(reversed(a))

if a == b:
    print('Palindrome')  
else:
    print('Not Palindrome')
"""    
