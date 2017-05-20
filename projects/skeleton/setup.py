try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Python Project',
    'author': 'Saurav',
    'url': 'url to get it at.',
    'download_url': 'where to download it',
    'author_email': 'saurav9878@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
    }

setup(**config)
