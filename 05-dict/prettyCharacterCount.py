#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: prettyCharacterCount.py
@time: 2017/7/12 10:08
"""
import pprint


def func():
    message = 'It was a bright cold day in April, and the ' \
              'clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    pprint.pprint(count)


if __name__ == '__main__':
    func()
