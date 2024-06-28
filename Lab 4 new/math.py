#ex 1 Write a Python program to convert degree to radian.
import cmath
degree = int(input('Input degree: '))
radian = degree * (cmath.pi / 180)

print('Output radian:', round(radian, 6))

#ex 2 Write a Python program to calculate the area of a trapezoid.
#area of trapezoid 
height = int(input('Height: '))
base1 = int(input('Base, first value: '))
base2 = int(input('Base, second value: '))

area = 0.5 * height * (base1 + base2)

print('Expected Output:', area)

#ex 3 Write a Python program to calculate the area of regular polygon.
import math 
sides = int(input('Input number of sides: '))
length = int(input('Input the length of a side: '))

area = round(sides * (length**2) / 4 * math.tan(math.pi / sides))
print('The area of the polygon is:', area)

#ex 4 Write a Python program to calculate the area of a parallelogram.
base = float(input('Length of base: '))
height = float(input('Height of parallelogram: '))
area = base * height

print('Expected Output', area)
