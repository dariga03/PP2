"""
def myFun(x, y, z):
    return x * y * z

m = myFun(4, 5, 6)
print(m) 
"""





"""
def multi3(x, y, z):
    return x*y*z

a, b, c = int(input()), int(input()), int(input())
m = multi3(a, b, c) 
print(m)
"""





def mult(*args):
    result = 1
    for number in args: 
        result = result * number

    return result   

#print(mult(3,4,2,343,5))    

t = input().split()
print(t)
n = []
for i in t:
    n.append(int(i))  

print(n)          

