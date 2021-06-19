#Sets: unordered , mutable , no duplictes

myset = {1 , 2 , 2}
print(myset) #{1, 2}

#create empty set
myset = set()
print(myset) #set()

myset = set("Hello")
print(myset) #{'o', 'H', 'l', 'e'}
myset = set([1 , 2 , 3 , 1])
print(myset) #{1, 2, 3}

myset = set()
nums = [1 , 1 , 5 , 6 , 2 , 4 , 5 , 2 , 1]
for i in nums:
    myset.add(i)

print(nums)
print(myset)

target = 1
if target in myset:
    print(f'{target} exists in myset')
else:
    print(f'{target} doesn\'t exist in myset')

# myset.remove(0) # error element doesn't exist in myset

myset.discard(0) #Remove an element from a set if it is a member , do nothing otherwise.

