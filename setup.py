# -*- coding: utf-8 -*-

from setuptools import setup
import os
import re

version = '0.1'

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('./__meta__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='Dodecahedron',
    description="Magic Carpet server",
    # packages=[
    #     'Dodecahedron',
    # ],
    # scripts=[
    #     "bin/runserver.py",
    #     "bin/manage.py",
    # ],
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    install_requires=read('requirements.txt'),
    zip_safe=False,
)
