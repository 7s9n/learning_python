import json

json_string = '''
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL"

    }
  ]
}
'''

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
            "emails":["test123@gmail.com"],
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

data = json.loads(people_string)

print(data)
