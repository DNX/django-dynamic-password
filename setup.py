#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
]

setup(
    name="dynamic_password",
    version=__import__('dynamic_password').get_version(),
    url='https://bitbucket.org/DNX/django-dynamic-password/',
    download_url='http://bitbucket.org/DNX/django-dynamic-password/downloads',
    license='BSD License',
    description="Add dynamic password authentication to your web service",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Denis Darii',
    author_email='denis.darii@gmail.com',
    keywords='dynamic password authentication',
    packages=find_packages(),
    namespace_packages=['dynamic_password'],
    include_package_data=True,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.3',
    ],
)
