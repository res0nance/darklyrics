# darklyrics
[![Build Status](https://travis-ci.org/res0nance/darklyrics.svg?branch=master)](https://travis-ci.org/res0nance/darklyrics)
[![Coverage Status](https://coveralls.io/repos/github/res0nance/darklyrics/badge.svg?branch=master)](https://coveralls.io/github/res0nance/darklyrics?branch=master)
[![PyPI version](https://badge.fury.io/py/darklyrics.svg)](https://badge.fury.io/py/darklyrics)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Python API for obtaining song lyrics from [darklyrics].

[darklyrics]: http://www.darklyrics.com/

## Description

[darklyrics] is an online database of lyrics for metal music.

This library scrapes the site for the lyrics and returns it. Kindly read the [disclaimer] to ensure that your use complies with it.

[disclaimer]: http://www.darklyrics.com/disclaim.html

## Installation

darklyrics is package freely available on [PyPI] and can easily be installed via pip.

```
pip install darklyrics
````

[PyPI]: https://pypi.python.org/pypi/darklyrics

## Support
Currently the following python versions are supported
- 2.7
- 3.4
- 3.5
- 3.6

## API
Currently only 4 API is supported `get_lyrics`. On success it returns lyrics on failure it will raise a `LyricsNotFound` exception.

```
import darklyrics

try:
    print(darklyrics.get_lyrics(song,artist))
    print(darklyrics.get_lyrics(song))
    print(darklyrics.get_songs(artist))
    print(darklyrics.get_albums(artist))
    print(darklyrics.get_all_lyrics(artist))
except darklyrics.LyricsNotFound:
    print('No lyrics found')
```