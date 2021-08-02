import pickle
import dill
import bz2

class ExampleClass:
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)

obj = ExampleClass()

pickled_object = pickle.dumps(obj)  # Pickling the object

# print( pickled_object )

obj.a_dict = None

unpickled_object = pickle.loads(pickled_object)

print( unpickled_object )
print( unpickled_object.a_dict )

"""
Note: Newer versions of the protocol offer more features ,
and improvements but are limited to higher versions of the interpreter.
Be sure to consider this when choosing which protocol to use.
To identify the highest protocol that your interpreter supports,
you can check the value of the pickle.HIGHEST_PROTOCOL attribute.
"""
# print( pickle.HIGHEST_PROTOCOL )

"""
To choose a specific protocol,
you need to specify the protocol version when you invoke load(),
loads(), dump() or dumps(). If you don’t specify a protocol,
then your interpreter will use the default version specified
in the pickle.DEFAULT_PROTOCOL attribute.
"""

square = lambda x : x * x
# my_pickle = pickle.dumps(square) #ERROR Python pickle module can’t serialize a lambda function

my_pickle = dill.dumps(square)
# print( my_pickle )


# square = lambda x : x * x
# a = square(35)
# import math
# b = math.sqrt(484)
# dill.dump_session('test.pkl')
# exit()

# print( globals().items() )
#
# dill.load_session('test.pkl')
# globals().items()

"""
You can use __getstate__() to define what should be included in the pickling process.
This method allows you to specify what you want to pickle.
If you don’t override __getstate__(), then the default instance’s __dict__ will be used.

In the following example,
you’ll see how you can define a class with several attributes,
and exclude one attribute from serialization with __getstate()__:
"""

class foobar:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        self.excluded_attr = lambda x: x * x

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['excluded_attr']
        return attributes

hussein = foobar('Hussein' , 22)
moataz = foobar('Moataz' , 21)

# print(hussein.__dict__) #{'name': 'Hussein', 'age': 22, 'excluded_attr': <function foobar.__init__.<locals>.<lambda> at 0x000002CA9E679E50>}

hussein_pickled_string = pickle.dumps(hussein)
moataz_pickled_string = pickle.dumps(moataz)

print(hussein_pickled_string)
print(moataz_pickled_string)

my_new_instance = pickle.loads(hussein_pickled_string)
print(my_new_instance)
# print(my_new_instance.__dict__) #{'name': 'Hussein', 'age': 22}

"""
In this example,
you create an object with three attributes. Since one attribute is a lambda,
the object is unpicklable with the standard pickle module.

To address this issue,
you specify what to pickle with __getstate__().
You first clone the entire __dict__ of the instance to have all the attributes defined in the class,
and then you manually remove the unpicklable c attribute.

If you run this example and then deserialize the object,
then you’ll see that the new instance doesn’t contain the excluded_attr attribute:
"""

"""
But what if you wanted to do some additional initializations while unpickling,
say by adding the excluded c object back to the deserialized instance?
You can accomplish this with __setstate__():
"""

class foobar:
    def __init__(self):
        self.a = 35
        self.b = "test"
        self.c = lambda x: x * x

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.c = lambda x: x * x

my_foobar_instance = foobar()
my_pickle_string = pickle.dumps(my_foobar_instance)
my_new_instance = pickle.loads(my_pickle_string)
print(my_new_instance.__dict__)

"""
Compression of Pickled Objects
Although the pickle data format is a compact binary representation of an object structure,
you can still optimize your pickled string by compressing it with bzip2 or gzip.

To compress a pickled string with bzip2,
you can use the bz2 module provided in the standard library.

In the following example,
you’ll take a string, pickle it,
and then compress it using the bz2 library:
"""

my_string = """

    More subtly,
    slicing creates another reference to the same list (because lists are mutable),
    and then unreachable data can be garbage-collected, but generally this is done later.
    Deleting instead immediately modifies the list in-place
    (which is faster than creating a slice and then assigning it to the existing variable),
    and allows Python to immediately deallocate the deleted elements,
    instead of waiting for garbage collection.
    In some cases you do want 2 slices of the same list – though this is rare in basic programming,
    other than iterating once over a slice in a for loop – ,
    but it's rare that you'll want to make a slice of a whole list,
    then replace the original list variable with a slice (but not change the other slice!),
    as in the following funny-looking code:
"""

pickled = pickle.dumps( my_string )
compressed = bz2.compress(pickled)


print( len(my_string) )
print( len(pickled) )
print( len(compressed) )
"""
When using compression,
bear in mind that smaller files come at the cost of a slower process.
"""
