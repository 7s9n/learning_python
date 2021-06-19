#Tuple: ordered , immutable , allows duplicate elements
mytuple = (1) #this is not recognized as a tuple
print(type(mytuple))
mytuple = (1, ) # this is now recognized as a tuple. we just added a comma ,
print(type(mytuple))

mytuple = tuple([1 , 2 , 3])

# print(mytuple) #(1, 2, 3)

# print(mytuple[0]) #1
# print(mytuple[-1]) #3


# mytuple[0] = 10 #gives error tuple is immutable

# for i in mytuple:
#     print(i , end=' ')
# print()

# target = 66
# if target in mytuple:
#     print(f'Yes {target} exists in mytuple.')
# else:
#     print(f'No {target} doesn\'t exist in mytuple.')

mytuple = ("Hussein" , 22 , True)
print(mytuple) #('Hussein', 22, True)


