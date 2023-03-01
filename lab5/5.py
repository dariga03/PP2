#Write a Python program that matches a string that has an followed by anything, ending in .'a''b'
 
import re 

string = input()  
x = re.match('a.*?b$', string) 
 
print(x)