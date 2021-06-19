from typing import List

#Lists: ordered , mutable , allows duplicate elements

#Create a List:



# mylist = [] #create empty list
# print( type(mylist) )

# mylist = list() #create empty list
# print( type(mylist) )

# nums = [1 , 2 , 3]

# item = nums[0] # first item in the list 1
# last_item = nums[-1]
# second_last_item = nums[-2]
# print(item)
# print(last_item)
# print( second_last_item )

# for i in range(4 , 11):
#     nums.append(i) #add numbers to the end of the list

# print(nums) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nums.insert(0 , -1) #Insert object before index.
# print(nums) #[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# items = [1 , 'Hussein' , True , False , 0.0 , 9.2]
# target = 1
# if target in items:
#     print(f'Yes {target} exists in the list.')
# else:
#     print(f'No {target} doesn\'t exist in the list.')

names = ['Hussein' , 'Rema' , 'Ekram']

#pop(index=last_index)
#Remove and return item at index (default last).
#Raises IndexError if list is empty or index is out of range.
# popped_value = names.pop()

# print(names) #['Hussein', 'Rema']
# print( popped_value ) #Ekram

# names.pop(0) # Hussein
# print( names ) #['Rema']

# fruits = ['Banana' , 'Apple']

# fruits.reverse() #reverse the actual list

# for i in reversed(fruits): #Return a reverse iterator over the values of the given sequence.
#     print(i)

# print(fruits)

# unsorted_list = [1 , 9 , 7 , 8 , 3 , 4 , 6 , 5 , 2]

# sorted_list = sorted(unsorted_list)
# print(sorted_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(unsorted_list) #[1, 9, 7, 8, 3, 4, 6, 5, 2]

# unsorted_list.sort() # sorts the actual list
# print(unsorted_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# first_list = [0] * 5 #create a list of 5 zeroes [0, 0, 0, 0, 0]
# second_list = [i for i in range(1 , 6)]

# new_list = first_list + second_list
# print(new_list) #[0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

# nums = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# odds = nums[::2] #starts from 0 and takes every second item.
# evens = nums[1::2] #starts from 1 and takes every second item.

# print(odds)
# print(evens)
# print(nums)

# reversed_nums = nums[::-1]
# print(reversed_nums)

# list_org = [1 , 2 , 3 , 4]
# list_cpy = list_org #this will not copy the actual data instead it coppies the reference in the memory.

# list_cpy[0] = None
# print(list_org)# [None, 2, 3, 4]
# print(list_cpy)# [None, 2, 3, 4]

# list_org = [1 , 2 , 3 , 4]
# list_cpy = list_org.copy()

# list_cpy[0] = None
# print(list_org)# [1, 2, 3, 4]
# print(list_cpy)# [None, 2, 3, 4]

# list_org = [1 , 2 , 3 , 4]
# list_cpy = list(list_org)

# list_cpy[0] = None
# print(list_org)# [1, 2, 3, 4]
# print(list_cpy)# [None, 2, 3, 4]

# list_org = [1 , 2 , 3 , 4]
# list_cpy = list_org[:]

# list_cpy[0] = None
# print(list_org)# [1, 2, 3, 4]
# print(list_cpy)# [None, 2, 3, 4]

# nums = list([1 , 2 , 3 , 4 , 5])
# squared = [i * i for i in nums]

# print(nums)
# print(squared)


dup = [1 , 2 , 3 , 1 , 1 , 5 , 1 , 2]

freq_of_1 = dup.count(1)
print(freq_of_1) #4

dummy = [0 , 0 , 5 , 5]

dup.extend(dummy) #Extend list by appending elements from the iterable.

dummy[0] = 1
print(dup)      #[1, 2, 3, 1, 1, 5, 1, 2, 0, 0, 5, 5]
print(dummy)    #[1, 0, 5, 5]

dup.clear() #Remove all items from list.

print(dup) #[]