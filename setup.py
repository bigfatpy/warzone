from setuptools import setup, find_packages


setup(name='warzone',
      packages=find_packages(),
      version=open("version", "r").read().strip())
