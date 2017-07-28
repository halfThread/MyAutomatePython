#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: commaList.py
@time: 2017/7/12 9:46
"""


def comma_list(items):
    ret = ''
    for item in items[:-1]:
        ret += item + ", "
    return ret + " and " + items[-1]


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_list(spam))
