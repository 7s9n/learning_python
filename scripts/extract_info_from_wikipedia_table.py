import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json

url = 'https://en.wikipedia.org/wiki/List_of_ID3v1_Genres'
response = requests.get(url)
soup = BeautifulSoup(response.content , 'html.parser')
tables = soup.find_all('table',{'class':'wikitable'})

res = {}
for table in tables:
    td_list = table.find_all('td')
    td_list = list(zip(td_list , td_list[1:]))
    for td in td_list[::2]: #jump in intervals of 2
        res[int(td[0].string)] = td[1].text.strip()


out_file = Path('list_of_id3v1_genres.json')
with out_file.open('w') as fw:
    json.dump(res , fw , indent=2)
