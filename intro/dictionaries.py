#Distionary: Key-Value pairs , unordered , mutable


mydict = {'name':'Hussein Sarea' , 'age':22}
print(mydict)

mydict = dict(name='Hussein' , age=22 , lang='C++')
print(mydict)

value = mydict['lang']
print(value) #c++

# value = mydict['city'] #raise error key doesn't exist
# print(value)

value = mydict.get('city')
print(value) #None

value = mydict.get('city' , 'Not exists')
print(value) #Not exists

value = mydict.pop('lang') #remove key-value pair (lang)
print(value) #C++
print(mydict) #{'name': 'Hussein', 'age': 22}

value = mydict.popitem() #Remove and return a (key, value) pair as a 2-tuple.
print(value) #('age', 22)

target_key = 'name'
if target_key in mydict:
    print(f'{target_key} exists in the dictionary')
else:
    print(f'{target_key} doesn\'t exist in the dictionary')

try:
    print(mydict['lang'])
except:
    print('Error') # will be printed

# new_dict = mydict.copy()
# new_dict['name'] = 'Hussein Sarea'
# print(mydict) #{'name': 'Hussein'}
# print(new_dict) #{'name': 'Hussein Sarea'}

new_dict = dict(mydict)
new_dict['name'] = 'Hussein Sarea'
print(mydict) #{'name': 'Hussein'}
print(new_dict) #{'name': 'Hussein Sarea'}

#counting the frequency of values in the list
nums = [1 , 2 , 1 , 3 , 2 , 7]
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq) #{1: 2, 2: 2, 3: 1, 7: 1}

#Loop Through a Distionary
for key in freq.keys():
    print(key)
print()
for value in freq.values():
    print(value)

for kv in freq.items():
    print(kv) #this will print each key-value pair as a tuple

for k , v in freq.items():
    print(f'{k} -> {v}')

for kv in freq:
    print(f'key-> {kv}')


mydict1 = {'name':'Hussein' , 'age': 20 , 'city':'sana\'a'}
mydict2 = dict(name='Hussein Sarea' , age=22 , lang= 'c++')

mydict1.update(mydict2)

print(mydict1) #{'name': 'Hussein Sarea', 'age': 22, 'city': "sana'a", 'lang': 'c++'}

mydict = {1:5 , 2:6 , 3:0}

print(mydict)

# mytuple = (1 , 1)
# mydict = {mytuple: 0}
# print(mydict) #{(1, 1): 0}
# mylist = [1 , 1]
# mydict = {mylist: 0} #error unhashable type: 'list'
# print(mydict) #error

del mydict , mydict1 , mydict2


## Can build up a dict by starting with the the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print (dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print (dict['a'])     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print dict['z']                  ## Throws KeyError
if 'z' in dict:
    print (dict['z'])     ## Avoid KeyError
    print (dict.get('z'))  ## None (instead of KeyError)

  ## By default, iterating over a dict iterates over its keys.
  ## Note that the keys are in a random order.
for key in dict:
    print (key)
## prints a g o

## Exactly the same as above
for key in dict.keys():
    print (key)

## Get the .keys() list:
print (dict.keys())  ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print (dict.values())  ## ['alpha', 'omega', 'gamma']

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print (key, dict[key])

## .items() is the dict expressed as (key, value) tuples
print( dict.items())  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items():
  print (k, '>', v)
## a > alpha    o > omega     g > gamma
