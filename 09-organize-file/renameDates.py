#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: renameDates.py.py
@time: 2017/7/28 9:45
"""
import os
import re

import shutil


def func():
    # re.VERBOSE表示正则表达式里的空格将会被忽略掉
    # (.*)表示匹配任务字符0-无穷个,再加?表示为非懒惰模式
    # 正则表达式的分组，每遇到一个左括号加1，所以正则的分组为
    # r"""(1) (2(3)) - (4(5)) - (6(7)) (8) """
    date_pattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)

    for amerFilename in os.listdir('.'):
        mo = date_pattern.search(amerFilename)
        if mo is None:
            continue

        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

        euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
        shutil.move(amerFilename, euroFilename)


if __name__ == '__main__':
    func()
