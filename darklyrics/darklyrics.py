from bs4 import BeautifulSoup
import requests

__BASE_URL__ = 'http://www.darklyrics.com/'

class LyricsNotFound(Exception):
    def __init__(self):
        super(LyricsNotFound,self).__init__()


def get_search_url(artist, song):
    url = __BASE_URL__ + 'search?q=' + artist + '+' + song
    return url

def get_lyric_url(artist, song):
    url = get_search_url(artist, song)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    sens = soup.find_all('div', class_='sen')
    for sen in sens:
        a = sen.find('a')
        if a:
            link = a.get('href')
            if link.find('#') != -1:
                return link
    raise LyricsNotFound()

def get_lyrics(artist, song):
    lyric_url = get_lyric_url(artist,song)
    index = lyric_url.find('#')
    song_number = int(lyric_url[index+1:])
    album_url = lyric_url[:index]

    response = requests.get(__BASE_URL__ + album_url)
    soup = BeautifulSoup(response.content,'html.parser')

    lyrics_div = soup.find('div', class_='lyrics')
    lyrics = lyrics_div.prettify().split('</h3>') # split into separate lyrics
    lyric = lyrics[song_number]
    lyric = lyric[:lyric.find('<h3>')] # remove tail
    lyric = lyric.replace('<br/>', '\n')
    return lyric
