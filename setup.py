# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name='threatbutt',
    version='1.0.4',
    provides=['threatbutt'],
    author='c0wl',
    url='https://github.com/ivanlei/threatbutt',
    setup_requires='setuptools',
    license='Apache License v 2.0',
    author_email='ivanlei@yelp.com',
    description='Defense in derpth - maximum protection from hacker threats like 4Chan and Reddit.',
    packages=find_packages(),
    install_requires=[
        'argparse==1.3.0',
        'requests==2.6.2'
    ],
    entry_points={
        'console_scripts': [
            'threatbutt=threatbutt.threatbutt:main',
        ],
    },
)
