import pytest

from darklyrics import get_lyrics, LyricsNotFound
from darklyrics.darklyrics import get_songs, get_all_lyrics, get_albums


def test_not_found():
    with pytest.raises(LyricsNotFound):
        get_lyrics('fakesong', 'fakeartist')
        get_albums('fakeartist')


def test_song_only():
    lyric = get_lyrics('your familiar face')
    assert 'but love is meaningless' in lyric.lower()


def test_get_songs():
    songs = get_songs("katatonia")
    assert 'Criminals' in songs


def test_get_all_songs():
    lyrics = get_all_lyrics('in vain')
    assert 'Before it was torn by hands of man' in lyrics


def test_integration():
    lyric = get_lyrics('steelheart', 'she\'s gone')
    assert 'i\'m to blame,' in lyric.lower()


def test_get_albums():
    albums = get_albums('shadows fall')
    assert 'Retribution' in albums
