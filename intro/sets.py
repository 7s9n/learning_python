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

odds = {1 , 3 , 5 , 7 , 9}
evens = {0 , 2 , 4 , 6 , 8}
primes = {2 , 3 , 5 , 7}

union = odds.union(evens)
print(union)

intersect = odds.intersection(evens)

print(intersect) #set()

intersect = evens.intersection(primes)
print(intersect) #{2}

setA = {i for i in range(1 , 10)}
setB = {1 , 2 , 3 , 10 , 11 , 12}

diff = setA.difference(setB)
print(diff) #{4, 5, 6, 7, 8, 9}

diff = setB.difference(setA)
print(diff) #{10, 11, 12}

diff = setA.symmetric_difference(setB)
print(diff) #{4, 5, 6, 7, 8, 9, 10, 11, 12}

setA.update(setB) #Update a set with the union of itself and others.
print(setA) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

print(setB) #{1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)
print(setA) #{1, 2, 3, 10, 11, 12}

setA = {1 , 2 , 3 , 4}
setB = {4 , 5 , 6 , 1}
setA.difference_update(setB) #Remove all elements of another set from this set.
print(setA) #{2, 3}

setA.symmetric_difference_update(setB) #Update a set with the symmetric difference of itself and another.
print(setA) #{1, 2, 3, 4, 5, 6}

setA = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8}
setB = {1 , 2 , 3}
setC = {9 , 10 , 11}
print( setA.issubset(setB) ) #False
print( setB.issubset(setA) ) #True

print( setA.issuperset(setB) ) #True
print( setB.issuperset(setA) ) #False

print( setA.isdisjoint(setB) ) #False Return True if two sets have a null intersection.
print( setB.isdisjoint(setC) ) #True


setA = {1 , 2 , 3}
setB = setA

setB.add(0)

print(setA) #{0, 1, 2, 3}
print(setB) #{0, 1, 2, 3}

setA = {1 , 2 , 3}
setB = setA.copy()

setB.add(0)

print(setA) #{1, 2, 3}
print(setB) #{0, 1, 2, 3}

setA = {1 , 2 , 3}
setB = set(setA)

setB.add(0)

print(setA) #{1, 2, 3}
print(setB) #{0, 1, 2, 3}


a = frozenset([1 , 2 , 2]) #Build an (immutable) unordered collection of unique elements.

print(a) #frozenset({1, 2})

