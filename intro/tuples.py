#Tuple: ordered , immutable , allows duplicate elements
# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.

# mytuple = (1) #this is not recognized as a tuple
# print(type(mytuple))
# mytuple = (1, ) # this is now recognized as a tuple. we just added a comma ,
# print(type(mytuple))

# mytuple = tuple([1 , 2 , 3])

# print(mytuple) #(1, 2, 3)

#Access Tuple Items
#We can access tuple items by referring to the index number, inside square brackets:

# print(mytuple[0]) #1
# print(mytuple[-1]) #3 Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.






# mytuple[0] = 10 #gives error tuple is immutable

# for i in mytuple:
#     print(i , end=' ')
# print()

# target = 66
# if target in mytuple:
#     print(f'Yes {target} exists in mytuple.')
# else:
#     print(f'No {target} doesn\'t exist in mytuple.')

# mytuple = ("Hussein" , 22 , True)
# print(mytuple) # ('Hussein', 22, True)

#Tuple Methods
# Python has two built-in methods that you can use on tuples.

# print(mytuple.count('Hussein')) #1
# print( mytuple.index(True) ) #2
# print( mytuple.index(False) ) # this will raise an error tuple.index(x): x not in tuple

# mylist = list(mytuple) #Convert mytuple to list
# print(mylist) #['Hussein', 22, True]

# mytuple = tuple(mylist) #Convert mylist to tuple
# print( mytuple ) #('Hussein', 22, True)

#Change Tuple Values
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

#Add tuple to a tuple.
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

#Unpacking a Tuple

# fruit = ('Banana' , 'Apple' , 'Orange') #Packing a tuple.

# (banana , apple , orange) = fruit #Unpacking a tuple

# print(banana)
# print(apple)
# print(orange)

#Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.

#Using Asterisk*
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green) #apple
# print(yellow) #banana
# print(red) #['cherry', 'strawberry', 'raspberry']

# delete the tuple completely:
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


#Loop Through a Tuple
# thistuple = ("apple", "banana", "cherry")

# for x in thistuple:
#   print(x)

# for i in range(len(thistuple)):
#     print(thistuple[i])

# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i += 1

# Join Two Tuples
# To join two or more tuples you can use the + operator:

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3) #('a', 'b', 'c', 1, 2, 3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)