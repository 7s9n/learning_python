#Arithmetic operations

#Addition:          3 + 2
#Subtraction:       3 - 2
#Multiplication:    3 * 2
#Division:          3 / 2
#Floor Division:    3 // 2
#Exponent:          3 ** 2
#Modulus:           3 % 2

#code snippets
print(f"classic division {17 / 3}") # classic division returns a float

print(f"floor division {17 // 3}") # floor division discards the fractional part

print(17 % 3) # the % operator returns the remainder of the division

#With Python, it is possible to use the ** operator to calculate powers

print(5 ** 2) # 5 squared
print (2 ** 7) # 2 to the power of 7

x = 5
y = 10

#Assignment operators
x = y #The left operand gets set to the value of the expression on the right
x += y #same as x = x + y
x -= y #same as x = x - y
x *= y #same as x = x * y
x**= y #same as x = x ** y
x /= y #same as x = x / y
x //=y #same as x = x // y
x %= y #same as x = x % y

#casting
x = '100'
y = '200'

print(x + y) #will print 100200

x = int(x)
y = int(y)

print(x + y) #will print 300

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2