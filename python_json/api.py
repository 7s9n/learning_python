import requests , json

# {
#   "valid":true,
#   "number":"967737660509",
#   "local_format":"0737660509",
#   "international_format":"+967737660509",
#   "country_prefix":"+967",
#   "country_code":"YE",
#   "country_name":"Yemen (Republic of)",
#   "location":"",
#   "carrier":"MTN Yemen",
#   "line_type":"mobile"
# }
number = 772101999
url = f"http://apilayer.net/api/validate?access_key=02563d6311b069c95845d6f92822fbdf&number={number}&country_code=YE&format=1"


response = requests.request("GET", url)
data = response.json()


print(response.text)
# print(data['valid'])

# for key , value in data.items():
#     print(key , value)
