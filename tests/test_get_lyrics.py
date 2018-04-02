from darklyrics import get_lyrics, LyricsNotFound
import pytest

from darklyrics.darklyrics import get_songs


def test_not_found():
    with pytest.raises(LyricsNotFound):
        get_lyrics('fakesong', 'fakeartist')


def test_song_only():
    lyric = get_lyrics('your familiar face')
    assert 'but love is meaningless' in lyric.lower()


def test_get_songs():
    songs = get_songs("katatonia")
    assert 'Criminal' in songs


def test_integration():
    lyric = get_lyrics('steelheart', 'she\'s gone')
    assert 'i\'m to blame,' in lyric.lower()
