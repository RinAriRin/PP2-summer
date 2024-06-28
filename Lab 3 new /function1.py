#ex 1 
a = int(input())

def ounce(a : int):
    b = a * 28.3495231
    return b 

print(ounce(a))

#ex 2 
F = int(input())

def calculate(a : int):
    C = (5/9) * (a - 32)
    return C 

print(calculate(F))

# ex 3 
heads = 35
legs = 94

def solve(heads, legs):
    rabbits = (legs/2) - heads
    chickens = heads - rabbits
    print(rabbits, " ", chickens)


solve(heads, legs)

# ex 4 
def isPrime(n):
    prime = []
    for i in range(a):
        for j in range(2, (int(i)//2)+1):    
            if n % j == 0:
                prime.append(i)
    print (prime)
            
answer = []
a = str(input()).split()
isPrime(a)

"""
import math

def return_primes(arr):
    return list(filter(lambda x : is_prime(x), arr))

def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

print(return_primes([10,21,3,8,9,11,44,62,100,19]))
"""

# ex 5 
from itertools import permutations  
def permutation(str): 
    a = permutations(str) 
    for x in a: 
        for y in x: 
            print(y, end = "") 
        print (" ")

str = input()
permutation(str)

#ex 6 
text = input()
def s_reverse(text): 
    return ' '.join(text.split()[::-1])

result = s_reverse(text)
print(result)

#ex 7  
nums = list(map(int, input().split()))
def has_33(nums):
    for i in range (len(nums)-1):
        if (nums[i] == 3 and nums[i+1]==3 ):
            return True     
        else:
            return False

if has_33(nums):
    print('True')
else:
    print('False')

#ex 8 
nums = list(map(int, input().split()))
def has_007(nums):
    for i in range (len(nums)-1):
        if (nums[i] == 0 and nums[i+1]==0 and nums[i+2]==7 ):
            return True
             
        else:
            return False

if has_007(nums):
    print('True')
else:
    print('False')

#ex 9
r = int(input())

def radius(a : float) :
    pi = 3.14159
    v = 4/3 * pi * pow(a, 3)
    print (v)

radius(r)

#ex 10
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

numbers = list(map(int, input().split()))
print(unique_list(numbers)) 

#ex 11
word = input()
def palindrome(word):
    if word == word[::-1]:
        print('Yes')
        
    else:
        print('No')
        

palindrome(word)

#ex12
def histogram(a):
    for n in a:
        res = ''
        size = n
        while( size > 0 ):
          res += '*'
          size = size - 1
        print(res)

histogram([4, 9, 7])

#ex 13
import random
num = random.randint(1, 20)
def guess_the_number(guess):
    cnt = 0

    while num > 0:
        cnt+=1
        if guess == num:
            print("Good job, " + a + "! You guessed my number in "+str(cnt)+" guesses!")
            break
        else:
            if guess < num:
                print("Your guess is too low.")
                print("Take a guess.")
                guess = int(input())
               
            elif guess > num:
                print("Your guess is too high.")
                print("Take a guess.")
                guess = int(input())

print ('Hello! What is your name?')
a = input()
print('Well, '+a+', I am thinking of a number between 1 and 20.')
print ('Take a guess.')
guess = int(input())

guess_the_number(guess)





