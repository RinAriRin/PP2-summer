#ex 1 Create a generator that generates the squares of numbers up to some number N.
a = int(input())

def squares(a):
    for i in range(a):
        if (i*i) <= a:
            yield i * i

for i in squares(a):
    print (i)
  
#ex 2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
  a = int(input())

for i in range(0, a + 1, 2):
    if i < a - 1:
        print(i, end = ', ')
    else:
        print(i)

#ex 3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
      a = int(input())

def div4and3(a):
    for i in range(a + 1):
        if (i % 3 == 0) and (i % 4 == 0):
            yield i

for i in div4and3(a):
    print(i)

#ex 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(i * i)

#ex 5 Implement a generator that returns all numbers from (n) down to 0.

a = int(input())

for i in reversed(range(a + 1)):
    print(i)
