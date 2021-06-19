from typing import List

#Lists: ordered , mutable , allows duplicate element

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

first_list = [0] * 5
second_list = [i for i in range(1 , 6)]

new_list = first_list + second_list
print(new_list)
