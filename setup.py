# -*- coding: utf-8 -*-
from setuptools import setup
import os
import re


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('./dodecahedron/__meta__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='Dodecahedron',
    description="A Flask boilerplate implementation.",
    packages=[
        'dodecahedron',
        'dodecahedron.tests',
        'dodecahedron.models',
        'dodecahedron.views',
    ],
    scripts=[
        "bin/manage.py",
        "bin/wsgi.py",
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Flask',
        'Intended Audience :: Developers',
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    install_requires=read('dependencies.txt'),
    license="MIT",
    zip_safe=False,
)
