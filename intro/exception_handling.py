# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# try:
#     x = 1 / 0
# except:
#     print("cannot divide by zero")
# finally:
#     print('This line will be executed regardless of the result of the try- and except blocks')

# try:
#     x = 1 / 2
#     print(f'{1} / {2}: {x}')
# except:
#     print("cannot divide by zero")
# finally:
#     print('This line will be executed regardless of the result of the try- and except blocks')

# try:
#     print(c)
# except NameError:
#     print('Variable c is not defined')
# except Exception:
#     print ('Other error')

# try:
#     print(x / 0)
# except NameError:
#     print('Variable c is not defined')
# except Exception:
#     print ('Other error')

#You can use the else keyword to define a block of code to be executed if no errors were raised:

# try:
#     print('Hello World')
# except:
#     print('Error occurred')
# else:
#     print('Everything is fine')

#The finally block, if specified, will be executed regardless if the try block raises an error or not.
#This can be useful to close objects and clean up resources:
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#     f = open('ex.txt' , 'r')
#     f.write('dsdsdksddwijfjfw')
# except Exception:
#     print('Somthing went wrong')
# finally:
#     try:
#         f.close()
#     except:
#         pass
#     finally:
#         print('Resources has been closed')

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

# x = -1
# if x < 0: #if x less than zero , Raise an error and stop the program
#     raise Exception('Sorry, no numbers below zero')


# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

# x = 'c'
#Raise a TypeError if x is not an integer:
# if not type(x) is int:
#     raise TypeError('Only integers are allowed')

# try:
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print(e) #division by zero

class ValueTooHigh(Exception):
    pass
class ValueTooSmall(Exception):
    def __init__(self , message , value):
        self.message = message
        self.value = value

def testValue(n:int):
    if n >= 5000:
        raise ValueTooHigh('Value is too high')
    if n <= 0:
        raise ValueTooSmall('value is too small' , n)

try:
    testValue(-50000)
except ValueTooHigh as e:
    print(e)
except ValueTooSmall as e:
    print(e.message)


# x = -1
# assert (x >= 0) , 'X is negative!'