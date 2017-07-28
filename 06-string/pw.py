#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: pw.py
@time: 2017/7/12 10:24
"""
import sys

import pyperclip as pyperclip

if __name__ == '__main__':
    PASSWORD = {'email': 'F234sdewrew',
                'blog': 'sesdfedadfew',
                'loggage': '12321234'}
    if len(sys.argv) < 2:
        print('Usage: python pw.py [account] - copy account password')
        sys.exit()

    account = sys.argv[1]

    if account in PASSWORD:
        pyperclip.copy(PASSWORD[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)
