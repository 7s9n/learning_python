from pathlib import Path

mp3_file = Path(__file__).parent.parent.parent / 'Desktop' / 'music' / 'chilly.mp3'


def create_id3v1_info(
    title = None ,
    artist = None ,
    album = None ,
    year = None ,
    comment = None,
    track = None ,
    genre = None,
    encoding = 'utf-8'
):
    empty_field = b'\x00' * 30
    id3v1 = {
        'title': empty_field,
        'artist': empty_field,
        'album': empty_field,
        'year': b'\x00' * 4,
        'comment' : empty_field,
        'genre': b'\xff',
    }
    if title:
        id3v1['title'] = bytes(title.ljust(30 , '\x00')[:30] , encoding=encoding)
    if artist:
        id3v1['artist'] = bytes(artist.ljust(30 , '\x00')[:30] , encoding=encoding)
    if album:
        id3v1['album'] = bytes(album.ljust(30 , '\x00')[:30] , encoding=encoding)
    if year:
        id3v1['year'] = bytes(year.ljust(4 , '\x00')[:4] , encoding=encoding)
    if comment:
        id3v1['comment'] = bytes(comment.ljust(30 , '\x00')[:30] , encoding=encoding)
    if genre in range(0 , 192):
        id3v1['genre'] = genre.to_bytes(1 , byteorder='big')

    return (
        b'TAG' +
        id3v1['title'] +
        id3v1['artist'] +
        id3v1['album'] +
        id3v1['year'] +
        id3v1['comment'] +
        id3v1['genre']
    )

def write_info(info):
    with mp3_file.open('r+b') as file_obj:
        try:
            file_obj.seek(-128, 2)
        except Exception:
            file_obj.seek(0, 0)
        file_obj.write(info)
    file_obj.close()
if __name__ == '__main__':
    info = create_id3v1_info(
        title='chilly' , artist='Hussein Sarea' ,
        album = '2002 - Disco Collection' ,
        year = '2021',
        comment = 'Hello world',
        genre=191,
        encoding='latin1'
    )
    write_info(info)
