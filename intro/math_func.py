print( min(1 , 2 , 3) ) #1
print( max(1 , 2 , 3) ) #3

print( max([1 , 2 , 3 , 5]) ) #5
print( max([1 , 2 , 3 , 5] , [10 , 20]) ) #[10, 20]

x = abs(-7.25)

print(x) #7.25

x = pow(4 , 3) #Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

print(x) #64

# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

x = math.pi #The math.pi constant, returns the value of PI (3.14...):
print(x) #3.141592653589793

#Return factorial of a number
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))

print( math.factorial(2009) )

print( math.sqrt(36) )

print( math.log10(3) )
print( math.log(3) )
print( math.log2(3) )