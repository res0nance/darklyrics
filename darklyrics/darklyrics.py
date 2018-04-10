# coding: utf-8
import requests
from bs4 import BeautifulSoup

__BASE_URL__ = 'http://www.darklyrics.com/'


class LyricsNotFound(Exception):
    def __init__(self):
        super(LyricsNotFound, self).__init__()


def get_search_url(song, artist):
    url = __BASE_URL__ + 'search?q=' + artist + '+' + song
    return url


def get_artist_url(artist):
    artist = artist.lower().replace(' ', '').replace(u'æ', u'e')
    return __BASE_URL__ + artist[0] + '/' + artist + '.html'


def get_lyric_url(song, artist):
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


def process_lyric(lyric):
    lyric = lyric[:lyric.find('<h3>')]  # remove tail
    # Set linebreaks
    lyric = lyric.replace('<br/>', '')
    # Remove italic
    lyric = lyric.replace('</i>', '')
    lyric = lyric.replace('<i>', '')
    # Remove trailing divs
    lyric = lyric.split('<div')[0]
    result = ''
    split_lyric = lyric.splitlines()
    for line_number in range(len(split_lyric) - 1):
        line = split_lyric[line_number].rstrip()
        next_line = split_lyric[line_number + 1].rstrip()
        last_line = split_lyric[max(line_number - 1, 0)].rstrip()
        # Remove duplicate blank lines
        if line is not '' or (line is '' and next_line is '' and last_line is not ''):
            result = result + '\n' + line
    return result


def get_lyrics(song, artist=''):
    lyric_url = get_lyric_url(song, artist)
    index = lyric_url.find('#')
    song_number = int(lyric_url[index + 1:])
    album_url = lyric_url[:index]

    response = requests.get(__BASE_URL__ + album_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    lyrics_div = soup.find('div', class_='lyrics')
    lyrics = lyrics_div.prettify().split('</h3>')  # split into separate lyrics
    lyric = lyrics[song_number]
    return process_lyric(lyric)


def get_songs(artist):
    url = get_artist_url(artist)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if 'not Found' in soup.title.string:
        raise LyricsNotFound()
    links = soup.find_all('a')
    result = []
    for link in links:
        if 'html#' in link.attrs['href']:
            result.append(link.text)
    return result


def get_albums(artist):
    """A way to scrape all lyrics for an artist saving a lot of requests."""
    url = get_artist_url(artist)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if 'not Found' in soup.title.string:
        raise LyricsNotFound()
    album_headlines = soup.find_all('h2')
    result = []
    for line in album_headlines:
        result.append(line.text.split('"')[1])
    return result


def get_all_lyrics(artist):
    albums = get_albums(artist)
    result = ''
    for album in albums:
        album = album.lower().replace(' ', '').replace("'", "").replace(u'æ', u'e')
        url = __BASE_URL__ + 'lyrics/' + artist.lower().replace(' ', '') + '/' + album + '.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        lyrics_div = soup.find('div', class_='lyrics')
        try:
            lyrics = lyrics_div.prettify().split('</h3>')  # split into separate lyrics
            for lyric in lyrics:
                result += process_lyric(lyric)
        except AttributeError:
            pass
    return result
