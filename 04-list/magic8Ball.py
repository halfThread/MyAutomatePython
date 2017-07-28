#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: magic8Ball.py.py
@time: 2017/7/12 9:39
"""
import random


def func():
    message = ['It is certain',
               'It is decidedly so',
               'Reply hazy try again',
               'Ask again later',
               'Concentrate and ask again',
               'My reply is no',
               'Outlook not so good',
               'Very doubtful']
    print(message[random.randint(0, len(message) - 1)])


if __name__ == '__main__':
    func()
