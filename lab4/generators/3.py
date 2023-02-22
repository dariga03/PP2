#Определите функцию с помощью генератора, который может итерировать числа, делимые на 3 и 4, между заданным диапазоном 0 и .n

N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    if (x % 3 == 0) & (x % 4 == 0):
        print(x)