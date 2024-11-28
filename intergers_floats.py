# Notes: This file contains examples of integers and floats in Python

num = 3 # int

print(type(num)) # int (integer)

num2 = 3.14 # float

print(type(num2)) # float (floating point number)

# Arithmetic operators

# Addition
print(3 + 2) # 5
# Subtraction
print(3 - 2) # 1
# Multiplication
print(3 * 2) # 6
# Division
print(3 / 2) # 1.5
# Floor division (rounds down)
print(3 // 2) # 1
# Exponent (power)
print(3 ** 2) # 3^2 = 9
# Modulus (remainder)
print(3 % 2) # 1

# Order of operations (PEMDAS) Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 2 + 1) # 7
print(3 * (2 + 1)) # 9

# Increment
num3 = 1  # num3 = 1
num3 += 1 # num3 = num3 + 1

print(num3) # 2

# Absolute value (always positive)  
print(abs(-3)) # 3    

# Round  (rounds to the nearest whole number)
print(round(3.75)) # 4

# Round to a specific decimal place
print(round(3.75, 1)) # 3.8

# Comparisons (return boolean values)   (Boolean: True or False)  (== equal, != not equal, > greater than, < less than, >= greater than or equal to, <= less than or equal to)

num4 = 3 # int
num5 = 2 # int


print(num4 == num5) # False   
print(num4 != num5) # True
print(num4 > num5) # True
print(num4 < num5) # False
print(num4 >= num5) # True
print(num4 <= num5) # False

# Casting (converting a variable from one data type to another)

num6 = '100' # string
num7 = '200' # string

print(num6 + num7) # 100200 (concatenation: string + string)

num8 = int(num6) # int
num9 = int(num7) # int

print(num8 + num9) # 300 (addition: int + int)





