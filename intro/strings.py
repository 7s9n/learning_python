#Besides numbers, Python can also manipulate strings, 
# which can be expressed in several ways. 
# They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. 
# \ can be used to escape quotes:

#Strings: ordered , immutable , text representation
txt = 'Hello this is a string'
#txt = "Hello this is a string"
#txt[0] = 'A' # error cuz string is immutable 'str' object does not support item assignment

print(txt)

txt = 'I\'m Hussein.' # use \' to escape the single quote...

print(txt)

txt = "I'm Hussein." # ...or use double quotes instead

print(txt)

txt = '"Yes," they said.' 

print(txt) #will print "Yes," they said.

first_name = 'Hussein'
last_name = 'Sarea'

full_name = first_name + ' ' + last_name # concatenate two strings or more use +

full_name = f'{first_name} {last_name}' # ... or use f string
print(full_name)

print(full_name[0:2]) # characters from position 0 (included) to 2 (excluded) -> Hu

print(full_name[2:5]) # characters from position 2 (included) to 5 (excluded) -> sse

#Note how the start is always included, and the end always excluded. 
# This makes sure that s[:i] + s[i:] is always equal to s:
print(full_name[:5] + full_name[5:]) #Hussein Sarea

print(full_name[-2:]) # characters from the second-last (included) to the end

str = 'hussein loves c++ more than python.'
print(str.capitalize()) #make the first character have upper case and the rest lower case.
print(str.endswith('python.'))   #True
print(str.endswith('python'))    #False
print(str.startswith('hussein')) #True
print(str.startswith('Hussein')) #False
print(str.swapcase()) #Convert uppercase characters to lowercase and lowercase characters to uppercase.
print(str.title()) #words start with uppercased characters and all remaining cased characters have lower case.
print('2'.zfill(2)) #Pad a numeric string with zeros on the left, to fill a field of the given width. -> 02
print(str.upper()) #Return a copy of the string converted to uppercase.
print(str.lower()) #Return a copy of the string converted to lowercase.

str = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n'
print(str) #will print a,b,c,d,e,f,g,h,i,j,k,l,m,n

str = str.split(',') #Return a list of the words in the string, using sep as the delimiter string.

print(str) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

str = ' '.join(str)
print(str) #a b c d e f g h i j k l m n

from timeit import default_timer as timer
my_list = ['a'] * 100000

my_string = ''
#bad
start = timer()
for char in my_list:
    my_string += char
end = timer()
print(end - start)

#good
start = timer()
my_string = ''.join(my_list)
end = timer()
print(end - start)