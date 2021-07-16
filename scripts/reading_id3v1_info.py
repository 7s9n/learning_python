"""
MP3 ID3 Tag 1.0 -- 128 bytes
(c) 1996, 1997 NamkraD (Eric Kemp)
Seek end of file, then -128, if first 3 bytes='TAG' then it has info layed
out as follows...

0..2 == 'TAG' (3 Bytes)
3..32 == Song Name (30 bytes)
33..62 == Artist (30 Bytes)
63..92 == Album Name (30 Bytes)
93..96 == Year (4 Bytes)
97..126 == Comment (30 Bytes)
127 == 1 Byte Song Genre Identifier
(get the listing of song Genre Types to know what byte = what)
"""
from pathlib import Path
import json


genres_file = Path('list_of_id3v1_genres.json')
def is_id3v1(header):
    return header == b'TAG'
def get_genre(index: int) ->str:
    with genres_file.open('r') as genres:
        data = json.load(genres)
    return data[str(index)]

def extract_info(file , encoding='utf-8'):
    info = {
        'Tag' : file.read(3),
        'Title' : file.read(30),
        'Artist' : file.read(30),
        'Album' : file.read(30),
        'Year' : file.read(4),
        'Comment' : file.read(30),
    }
    if not is_id3v1(info['Tag']):
        raise TypeError('This function supports only id3v1')
    track = 0
    if info['Comment'][28] == 0:
        track = info['Comment'][29]
        info['Comment'] = info['Comment'][:29]

    for key , value in info.items():
        info[key] = value.decode(encoding , 'backslashreplace')
    info['Genre'] = get_genre(index=file.read(1)[0])
    info['Track'] = track
    return info

mp3_file = Path(__file__).parent.parent.parent / 'Desktop' / 'music' / 'Rado0y & Jaguar.C & Meme-- Mshtaglk -2020.mp3'
tag_size = 128
with mp3_file.open('rb') as fr:
    fr.seek(-tag_size , 2)
    info = extract_info(fr)
    for key , value in info.items():
        print(key , value)
