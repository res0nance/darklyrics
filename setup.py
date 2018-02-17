from setuptools import setup

version = 0.1

setup(name='darklyrics',
      version=version,
      description='Darklyrics API for song lyrics',
      long_description='Darklyrics API for song lyrics',
      license='MIT',
      author='Raihaan',
      author_email='raihaanhimself@gmail.com',
      url='http://github.com/res0nance/darklyrics',
      packages=['darklyrics'],
      install_requires=['beautifulsoup4', 'requests'],
      keywords='darklyrics lyric lyrics song api')