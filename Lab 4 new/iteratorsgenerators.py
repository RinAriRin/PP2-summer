#ex 1 Генерация квадратов чисел до N
a = int(input())

def squares(a):
    for i in range(a):
        if (i*i) <= a:
            yield i * i

for i in squares(a):
    print (i)
  
#ex 2 Генерация четных чисел от 0 до n
  a = int(input())

for i in range(0, a + 1, 2):
    if i < a - 1:
        print(i, end = ', ')
    else:
        print(i)

#ex 3 Генерация чисел, которые делятся на 3 и 4 в диапазоне от 0 до n
      a = int(input())

def div4and3(a):
    for i in range(a + 1):
        if (i % 3 == 0) and (i % 4 == 0):
            yield i

for i in div4and3(a):
    print(i)

#ex 4 Генерация квадратов чисел от a до b
a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(i * i)

#ex 5 Implement a generator that returns all numbers from (n) down to 0.

a = int(input())

for i in reversed(range(a + 1)):
    print(i)
