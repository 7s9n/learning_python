from collections import Counter , namedtuple , OrderedDict , defaultdict , deque

# c = Counter()  #Create empty counter
# print(c)

# c[1] = 5 #add element to the counter 1 is the key and 5 is the value
# print(c) #Counter({1: 5})
# del c[1]

# str = 'abbbacdcc'
# cnt = Counter(str) #Create counter With sequence of item
# print(cnt) #Counter({'b': 3, 'c': 3, 'a': 2, 'd': 1})

# freq = {'a':5 , 'b':9 , 'c':8}
# cnt = Counter(freq) #Create counter with dictionary
# print(cnt) #Counter({'b': 9, 'c': 8, 'a': 5})

# with keyword arguments 
# cnt = Counter(a=5 , b= 66 , c=10)
# print(cnt) #Counter({'b': 66, 'c': 10, 'a': 5})

# cnt = Counter([1 , 2 , 3 , 4 , 1])
# print(cnt) #Counter({1: 2, 2: 1, 3: 1, 4: 1})
# print(cnt.keys()) #dict_keys([1, 2, 3, 4])
# print(cnt.values()) #dict_values([2, 1, 1, 1])
# print(cnt.items()) #dict_items([(1, 2), (2, 1), (3, 1), (4, 1)])
# print(list(cnt.elements())) #[1, 1, 2, 3, 4] Iterator over elements repeating each as many times as its count.
# print(cnt.most_common()) #[(1, 2), (2, 1), (3, 1), (4, 1)] List the n most common elements and their counts from the most common to the least. If n is None, then list all element counts.
# print(cnt.most_common(2)) #[(1, 2), (2, 1)]
# print(cnt.most_common(1)[0][1]) #2

# if 1 in cnt:
#     print('Yes')

# point_2d = namedtuple('Point' , ['x' , 'y'])

# p = point_2d(x= 10 , y=5) # or point_2d(10 , 5)

# print(p.x) #10
# print(p.y) #5
# print(p[0] + p[1]) #15

# An OrderedDict is also a sub-class of dictionary but unlike dictionary, 
# it remembers the order in which the keys were inserted. 
#Note: from python 3 notmal dict and OrderedDict are the same

# ordered_dic = OrderedDict() #Create empty OrderedDict
# print(ordered_dic) #OrderedDict()

# print("This is a Dict:\n") 
# d = {} 
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
    
# for key, value in d.items(): 
#     print(key, value) 
    
# print("\nThis is an Ordered Dict:\n") 
# od = OrderedDict()  
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4


# for key, value in od.items(): 
#     print(key, value)

# print(od)#OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# A DefaultDict is also a sub-class to dictionary. 
# It is used to provide some default values for the key that does not exist and never raises a KeyError.
# default_factory is a function that provides the default value for the dictionary created. 
# If this parameter is absent then the KeyError is raised.
# DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.


# nums = [1 , 2 , 1 , 3 , 4 , 2 , 3 , 1]
# d = defaultdict(int) #Create defaultdict 

# for num in nums:
#     # The default value is 0 , so there is no need to enter the key first. 
#     d[num] += 1 

# print(d) #defaultdict(<class 'int'>, {1: 3, 2: 2, 3: 2, 4: 1})

# d = defaultdict(list) #default is empty list

# d['a'] = 1
# d['b'] = 6
# d['n'].append(1)
# print(d['c']) #[]
# print(d) #defaultdict(<class 'list'>, {'a': 1, 'b': 6, 'n': [1], 'c': []})

# Defining a dict 
# d = defaultdict(list) 
    
# for i in range(5): 
#     d[i].append(i) 
        
# print("Dictionary with values as list:") 
# print(d) #defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
# d[1].append(2)
# print(d) #defaultdict(<class 'list'>, {0: [0], 1: [1, 2], 2: [2], 3: [3], 4: [4]})

dq = deque()
dq.append(1)
print(dq) #deque([1])
dq.append(2)
dq.append(3)
print(dq) #deque([1, 2, 3])

print(dq[2]) #3

dq.appendleft(0)
print(dq) #deque([0, 1, 2, 3])

dq.pop() #remove last element
print(dq) #deque([0, 1, 2])

dq.popleft() #remove first element
print(dq) #deque([1, 2])

dq.extend([3 , 4 , 5])
print(dq) #deque([1, 2, 3, 4, 5])

dq.extendleft([0 , -1])
print(dq) #deque([-1, 0, 1, 2, 3, 4, 5])

dq.insert(0 , -2)
print(dq) #deque([-2, -1, 0, 1, 2, 3, 4, 5])

dq.rotate(3)
print(dq) #deque([3, 4, 5, -2, -1, 0, 1, 2])

dq.rotate(-3)
print(dq) #deque([-2, -1, 0, 1, 2, 3, 4, 5])

dq.remove(-2)
print(dq) #deque([-1, 0, 1, 2, 3, 4, 5])