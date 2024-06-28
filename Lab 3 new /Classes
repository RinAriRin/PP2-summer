#ex 1 Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class class1:
    def getstring(self):
        self.s = input()

    def printstring(self):
        print(self.s.upper())

a = class1()
a.getstring()
a.printstring()

#ex 2 Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def areas(self):
        print(0)

class Square(Shape):
    def __init__ (self, length):
        self.length = length
    def area(self):
        print(pow(self.length,2))
 
l = int(input())

Area = Square(l)
Area.area()

#ex 3 Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Shape():
    def areas(self):
        print(0)

class rectangle(Shape):
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
 
l = int(input())
w = int(input())

rect = rectangle(l, w)
print(rect.area())

#ex 4 Write the definition of a Point class. Objects from this class should have a
#a method show to display the coordinates of the point
#a method move to change these coordinates
#a method dist that computes the distance between 2 points

class Point():

    def show(self, x, y):
        self.x = x
        self.y = y
        print(x, y)
        
    def move(self, x, y, x1, y1):
        self.x1 = x1 + x
        self.y1 = y1 + y
        print(x1, y1)

    def dist(self, x, y, x1, y1):
        print(((x1 - x)**2  + (y1 - y)**2) ** 0.5)

x, y = map(int,input().split())
x1, y1 = map(int,input().split())

distance = Point()
distance.show(x, y)
distance.move(x, y, x1, y1)
distance.dist(x, y, x1, y1)

#ex 5 Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
#class Account:
#   pass
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, income):
        def __init__ (self, income):
            self.newcome = income
        self.balance += income

    def withdraw(self, outcome):
        def __init__(self, outcome):
            self.outcome = outcome
        if self.balance >= outcome:
            self.balance -= outcome
        else:
            self.balance = 0

    def show(self):
        print(self.balance)


a = BankAccount("Amina", 5000)
a.deposit(100)
a.withdraw(1500)
a.show()

#ex 6 Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
list1 = [3, 58, 346, 17, 19, 23, 21]

is_prime = list(filter(lambda i: all(i%j!=0 for j in range(2, i//2)), list1))

print(is_prime)



