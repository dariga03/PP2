a = "Hello World" #str
print(type(a))

b = 20 #int
print(type(b))

c = 20.5 #float
print(type(c))	

d = 1j	#complex
print(type(d))

e = ["apple", "banana", "cherry"]  #list
print(type(e))

f = ("apple", "banana", "cherry")	#tuple	
print(type(f))

g = range(6)	#range	
print(type(g))

h = {"name" : "John", "age" : 36}	#dict
print(type(h))

l = {"apple", "banana", "cherry"}	#set	
print(type(l))

m = frozenset({"apple", "banana", "cherry"})	#frozenset	
print(type(m))

n = True	#bool	
print(type(n))

o = b"Hello"	#bytes	
print(type(o))

p = bytearray(5)	#bytearray	
print(type(p))

q = memoryview(bytes(5))	#memoryview	
print(type(q))

r = None #none
print(type(r))
