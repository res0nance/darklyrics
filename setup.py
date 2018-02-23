from setuptools import setup

version = '0.1.3'

setup(name='darklyrics',
      version=version,
      description='Darklyrics API for song lyrics',
      long_description='This library scrapes the site darklyrics for the lyrics and returns it. Kindly read the disclaimer to ensure that your use complies with it.',
      license='MIT',
      author='Raihaan',
      author_email='raihaanhimself@gmail.com',
      url='http://github.com/res0nance/darklyrics',
      packages=['darklyrics'],
      setup_requires=['pytest-runner'],
      install_requires=['beautifulsoup4', 'requests'],
      tests_require=['pytest'],
      keywords='darklyrics lyric lyrics song api')