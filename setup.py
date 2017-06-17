#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python2 setup.py install\'')
    print()

sys.path.insert(0, 'mail_check')
import release

if __name__ == "__main__":
    setup(
        name = release.name,
        version = release.__version__,
        author = release.__author__,
        author_email = release.__email__,
        description = release.__description__,
        url='https://github.com/saketharsh/mail-check',
        keywords='Terminal based mail-checker written purely in python2',
        packages = ['mail_check'],
        license = 'MIT License',
        entry_points = {
            'console_scripts': [
            'mail_check = mail_check.mail:main'
            ]
        },        
        test_suite = 'nose.collector',
        tests_require = ['nose>=0.10.1']
    )

