#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
	name='django-highway',
	version='0.1',
	description='',
	author='Allan Lei',
	author_email='allanlei@helveticode.com',
	url='https://www.github.com/allanlei/django-highway',
	keywords = 'django highway multitenant'.split(),
	license = 'BSD',
	packages=find_packages(),
	install_requires=[
        'Django>=1.4',
        'django-appconf>=0.5',
        'Werkzeug==0.8.3',
    ],
)