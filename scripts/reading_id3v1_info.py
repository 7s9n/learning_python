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

def get_genre(index: int) ->str:
    with genres_file.open('r') as genres:
        data = json.load(genres)
    return data.get(str(index))

def extract_info(data , encoding='utf-8'):
    info = {
        'Tag': None,
        'Title': None,
        'Artist': None,
        'Album': None,
        'Year': None,
        'Comment': None,
        'Track': None,
        'Genre':None,
    }
    empty_field = b'\x00' * 30
    if data[:3] != b'TAG':
        raise TypeError('This function reads only id3v1')
    else:
        info['Tag'] = data[:3].decode(encoding , 'backslashreplace')
    if data[3:33] != empty_field:
        info['Title'] = data[3:33].decode(encoding , 'backslashreplace')
    if data[33:63] != empty_field:
        info['Artist'] = data[33:63].decode(encoding , 'backslashreplace')
    if data[63:93] != empty_field:
        info['Album'] = data[63:93].decode(encoding , 'backslashreplace')
    if data[93:97] != b'\x00'*4:
        info['Year'] = data[93:97].decode(encoding , 'backslashreplace')
    if data[97:127] != empty_field:
        if data[97:127][28] == 0:
            info['Track'] = data[97:127][29]
            info['Comment'] = data[97:126].decode(
            encoding , 'backslashreplace') if data[97:126] != empty_field[:29] else None
        else:
            info['Track'] = 0
            info['Comment'] = data[97:127].decode(
            encoding , 'backslashreplace') if data[97:127] != empty_field[:29] else None
    info['Genre'] = get_genre(data[127:128][0])
    return info

if __name__ == '__main__':
    mp3_file = Path(__file__).parent.parent.parent / 'Desktop' / 'music' / 'chilly.mp3'
    with mp3_file.open('rb') as rf:
        rf.seek(-128 , 2)
        data = rf.read()
        info = extract_info(data)
        for key , value in info.items():
            print(key , value)
