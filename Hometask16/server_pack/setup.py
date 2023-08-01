from setuptools import setup, find_packages

setup(name='Async_Chat',
      version='0.0.1',
      description='Server package for chat',
      packages=find_packages(),
      author_email='kteranova@mail.ru',
      author='Ekaterina Eranova',
      install_requeres=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      url='https://github.com/Alesso4ka/AsyncChat_GB',
      )

