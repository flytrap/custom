# coding: utf8
# auto: flytrap
try:
    from setuptools import setup, find_packages

    PACKAGES = find_packages()
except ImportError:
    from distutils.core import setup

    PACKAGES = ['custom', 'custom.CustomCarry']

from custom.CustomCarry import __version__

NAME = 'custom'
VERSION = __version__

setup(name=NAME,
      version=VERSION,

      author='flytrap',
      author_email='hiddes@126.com',
      url='https://github.com/flytrap/custom',
      description='Custom self carry',

      packages=PACKAGES
      )
