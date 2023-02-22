#Реализуйте генератор, вызываемый для получения квадрата всех чисел от (a) до (b). 
#Протестируйте его с помощью цикла "for" и распечатайте каждое из полученных значений.squares

A = int(input())
B = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = A
    return self

  def __next__(self):
    if ((self.a >= A) and (self.a <= B)):
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x * x)