''' JavaScript Object Notation '''
import json

people_string = '''
{
    "People": [
        {
            "name":"Hussein Sarea",
            "phone":"737660509",
            "emails":["zzzsssx0@gmail.com"],
            "has_licence":true
        },
        {
            "name":"Moataz Sarea",
            "phone":"737660509",
            "emails":["test123@gmail.com" , "test13@gmx.com"],
            "has_licence":false
        },
        {
            "name":"Ekram Sarea",
            "phone":"737660509",
            "emails":null,
            "has_licence":false
        }
    ]
}
'''
#loads converts json to a python onject
data = json.loads(people_string)

# print(type(data))
# print(data)

# print(type(data['People']))

# print( type( data['People'][0] ) )
# print( type( data['People'][0]['name'] ) )

# for person in data['People']:
#     print(person)

for person in data['People']:
    del person['phone']

#json.dumps() convert the data to a json string.
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

new_string = json.dumps(data , indent=2) #json.dumps(data , indent=2 , sort_keys=True)

print(new_string)
