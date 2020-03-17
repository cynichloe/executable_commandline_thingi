#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from setuptools import setup, find_packages

requires = [
    'click',
]

extras_require = {
    'dev': [
        'coverage',
        'flake8',
        'pytest >= 3.6',
        'pytest-cov',
        'sphinx',
    ],
    'docs': [
        'sphinx',
    ]
}

version = '1'

setup(
    name='Fangi',
    version=version,
    description="Fangi's dummy executable",
    # long_description=readme,
    author='author fangi',
    author_email='fangsu.qmul@gmail.com',
    # url='https://github.com/projectmesa/mesa',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_require=extras_require,
    keywords='keywords fangi',
    license='None',
    zip_safe=False,
    entry_points='''
        [console_scripts]
        fangi=click_group:cli
    ''',
)
