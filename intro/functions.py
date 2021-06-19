# def sayHello() -> None:
#     print('Hello')

# def sayHello(name: str):
#     print(f'Hello {name}')

#Python does not support function overloading. 
# When we define multiple functions with the same name,the later one always overrides the prior and thus, 
# in the namespace, there will always be a single entry against each function name.

# sayHello() error
# sayHello(name='Hussein')

# def sum(n: int) -> int:
#     if n & 1 != 0: #n % 2 != 0 , if is odd
#         return ((n + 1) // 2) * n
#     return (n // 2) * (n + 1)

# print( sum(10) )

# def fun()-> None:
#     pass

# print(fun()) #None
# print(fun) #address of the function in the memory

#Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

# def say_hi(name: str='Hussein') -> None:
#     print(f'Hi {name}')

# say_hi() #Hi Hussein
# say_hi('Hussein Sarea') #Hi Hussein Sarea

#Keyword Arguments
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

# def format_full_name(first:str , second:str)-> str:
#     return f'{first} {second}'

# print( format_full_name('Hussein', 'Sarea') )
# print( format_full_name('Sarea', 'Hussein') )
# print( format_full_name(second='Sarea', first='Hussein') )

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

# def sum(*args: int) -> int:
#     #args is of type tuple ()
#     ans = 0
#     for num in args:
#         ans += num
#     return ans

# print( sum(1 , 2) ) # 3
# print( sum(1 , 2 , 3 , 9 , 20) ) # 35
# print( sum() ) #0

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:




# def get_mean(*values : int) -> float:
#     ans = 0
#     for value in values:
#         ans += value
#     return ans / len(values)

# def print_student_info(*args , **kwargs) -> None:
#     print(args)
#     print(kwargs)

# courses = ['English' , 'Arabic' , 'Math' , 'Physics']
# info = {'name':'Hussein' , 'age':22}
# print_student_info(*courses , **info)

month_days = [0 , 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]

def is_leap(year:int)-> bool:
    """ Return True for leap year , False otherwise. """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# print( is_leap(2021) )

# def days_in_month(year: int , month: int) -> int:
#     """ Return number of days in that month of that year. """
#     if not 1 <= month <= 12:
#         raise ValueError
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month]
    
# print(days_in_month(month=6 , year=2021))

#Recursion
# def print_to(n:int) ->int:
#     if n > 1:
#         print_to(n - 1)
#     print(n)
# print_to(10)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

#Syntax
#lambda arguments : expression
#The expression is executed and the result is returned:

# sum_two = lambda x , y : x + y
# print( sum_two(1 , 2) ) #3

# add_10 = lambda x : x + 10 #Add 10 to argument x, and return the result:
# print( add_10(10) ) #20

# def myFun(n:int) -> int:
#     return lambda x : x * n

# doubler = myFun(2)
# print( doubler(8) )

if __name__ == '__main__':
    # print_student_info('English' , 'Arabic' , 'Math' , 'Physics' , name='Hussein' , age=15)
    # print( get_mean(100 , 99) )
    pass