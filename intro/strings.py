#Besides numbers, Python can also manipulate strings, 
# which can be expressed in several ways. 
# They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. 
# \ can be used to escape quotes:

txt = 'Hello this is a string'
#txt = "Hello this is a string"
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
