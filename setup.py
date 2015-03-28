#!/usr/bin/env python
import codecs
import os
import re
from setuptools import setup, find_packages


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts), encoding='utf8').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='best-trees',
    description='Utility for getting the best N trees from a BEAST treelog',
    long_description=read('README.md'),
    version=find_version('best_trees/__init__.py'),
    packages=find_packages(),
    author='Jonathan Chang',
    author_email='jonathan.chang@ucla.edu',
    url='https://github.com/jonchang/best-trees',
    license='AGPLv3',
    install_requires=[
        'argh>=0.26.1'
    ],
    include_package_data=True,
    entry_points={
      'console_scripts':[
          'best_trees = best_trees:main'
      ]
   }
)

