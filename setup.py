#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='PyEmail',
    version='0.1.0',
    author='SHAOFEI LI',
    author_email='SFL_9@outlook.com',
    description='PyEmail is a fast, powerful, and easy-to-use open-source Email tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SFL09/PyEmail',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    py_modules=['PyEmail'],
)
