import pytest

from darklyrics import get_lyrics, LyricsNotFound, get_albums, get_songs, get_all_lyrics


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


def test_get_songs_fail():
    with pytest.raises(LyricsNotFound):
        get_songs("fakeartist")


def test_get_all_songs():
    lyrics = get_all_lyrics('in vain')
    assert 'Before it was torn by hands of man' in lyrics


def test_integration():
    lyric = get_lyrics('steelheart', 'she\'s gone')
    assert 'i\'m to blame,' in lyric.lower()


def test_get_albums():
    albums = get_albums('shadows fall')
    assert 'Retribution' in albums


def test_get_albums_fail():
    with pytest.raises(LyricsNotFound):
        get_albums("fakeartist")

def test_get_songs_album():
    """Check that a song from album is returned in the array"""
    arr = get_songs("kayo dot", "Choirs Of The Eye")
    assert 'Marathon' in arr

def test_get_songs_album_fail():
    """Check that an exception is thrown when artist doesn't exist"""
    with pytest.raises(LyricsNotFound):
        get_songs("fakeartist", "South Of Heaven")


def test_get_songs_album_fail2():
    """Check for songs not on album"""
    arr = get_songs("Slayer", "South Of Heaven")
    assert "Raining Blood" not in arr
