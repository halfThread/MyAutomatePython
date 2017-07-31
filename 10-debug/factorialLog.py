#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: factorialLog.py
@time: 2017/7/31 14:29
"""

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

logging.debug("Start to program")


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ',total is ' + str(total))
    return total
    logging.debug('End of factorial(%s%%)' % n)


print(factorial(5))
logging.debug('End of program')
