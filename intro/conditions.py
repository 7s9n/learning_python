#Comparisons
#Equal:             ==
#Not Equal:         !=
#Greater Than:      >
#Less Than:         <
#Greater or Equal:  >=
#Less or Equal:     <=
#Object Identity:   is

# x = 2
# y = 1
# z = 10

# if x < y or y < x:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

# if x < y and x < z:
#     print('x is smaller')
# elif y < z:
#     print('y is smaller')
# else:
#     print('z is smaller')

# if True:
#     print('Condition is True')

# if False:
#     print('Will never reach here')

# x = [1 , 2 , 3]
# y = [1 , 2 , 3]

# if x == y:
#     print('Yes , they have same data')
# else:
#     print('No , they don\'t')

# print(id(x))
# print(id(y))

# if x is y:
#     print('Yes , x and y refers to same memory location')
# else:
#     print('No')

# x = y

# print(id(x))
# print(id(y))

# if x is y:
#     print('Yes , x and y refers to same memory location')
# else:
#     print('No')


# if not False:
#     print('Then it\'s True')

# x = [1 , 2 , 9]
# target = 10
# if target in x:
#     print(f'{target} exists in x')
# else:
#     print(f'{target} doesn\'t exist in x')

#False values

#False
#None
#Zero of any numeric type
#Any empty sequence. for example '' , () , []
#Any empty mapping. for example {}

# if {}:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

#The following will return False:
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

#One more value, or object in this case, evaluates to False,
#and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

# class MyClass():
#     def __len__(self):
#         return 0
#
# my_object = MyClass()
#
# print( bool(my_object) )

bools = [True , True , False]

print(all(bools))
print(any(bools))

odds = [1 , 3 , 5 , 7 , 9]

is_odd = lambda n: n & 1 != 0

if all(is_odd(n) for n in odds):
    print('All number is odd')
else:
    print('There\'s even number in this list')

nums = [2 , 1 , 7 , 9]
if any(n % 2 == 0 for n in nums):
    print('Yes, there\'s at least one even number in this list')
