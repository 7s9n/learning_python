import requests

phone = input('Enter phone number: ')
message = input('Enter message: ')

#number must be in E.164 format : +967737660509

data = {'phone':phone , 'message':message , 'key':'textbelt'}
resp = requests.post( 'https://textbelt.com/text' , data=data)

print(resp.json())
