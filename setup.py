#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import shutil
import sys
from io import open

from setuptools import find_packages, setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('django_select2_admin_filters')


setup(
    name='django-select2-admin-filters',
    version=version,
    license='MIT',
    description='A simple extension to Django app to render filters in django admin panel as autocomplete widget.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Bartłomiej Żmudziński',
    author_email='zmudzinski.bartek@gmail.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=["django>=2.2"],
    python_requires=">=3.5",
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
    ],
    project_urls={
        'Source': 'https://github.com/the-bit-by-bit/django-select2-admin-filters',
    },
)