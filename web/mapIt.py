#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: mapIt.py.py
@time: 2017/8/29 13:47
"""
import sys
import webbrowser

import pyperclip

if __name__ == '__main__':
    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    webbrowser.open('https://cn.bing.com/ditu/Default.aspx?q=' + address)
