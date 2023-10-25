#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="libreria para cosas de quimica",
    entry_points={
        'console_scripts': [
            'chibi_alchemist=chibi_alchemist.cli:main',
        ],
    },
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_alchemist',
    name='chibi_alchemist',
    packages=find_packages(include=['chibi_alchemist', 'chibi_alchemist.*']),
    url='https://github.com/dem4ply/chibi_alchemist',
    version='0.0.1',
    zip_safe=False,
)
