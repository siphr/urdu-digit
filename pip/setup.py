#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="urdu_digit",
    version="0.0.17",
    keywords=["urdu", "numeric", "digit", "converter"],
    description="English to Urdu numeric digit converter.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-urdu-digit-211001.html',
        'Source': 'https://github.com/siphr/urdu-digit',
        'Tracker': 'https://github.com/siphr/urdu-digit/issues',
    },
    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['urdu_digit'],
    platforms="any",
    install_requires=[]
)
