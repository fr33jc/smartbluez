#!/usr/bin/env python
from setuptools import setup, find_packages
import os.path


ETC = os.path.join(os.path.dirname(__file__), 'etc')

# with open(os.path.join(ETC, 'requirements.pip')) as f:
#     reqs = [l.strip() for l in f if '://' not in l]
reqs = []
reqs.append('distribute')

setup(
        name='smartbluez',
        version='0.1.0',
        author='fr33jc',
        author_email='fr33jc@gmail.com',
        packages=find_packages(exclude=['tests']),
        license='GPLv2',
        description='',
        platforms='POSIX',
        url='https://github.com/fr33jc/smartbluez',
        install_requires=reqs,
        )
