import re
import requests


def get_playlist_videos_links(url: str) -> list:

    source_code = requests.get(url).text
    parser = re.compile(r"watch\?v=\S+?list=")
    playlist = re.findall(parser , source_code)
    domain = "https://www.youtube.com/"
    playlist = map( lambda x: domain + x.replace('\\u0026list=' , '') , playlist)

    return list(playlist)

url = "https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"

videos_links = get_playlist_videos_links(url)

for video_link in videos_links:
    print( video_link )
