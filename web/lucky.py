#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: lucky.py.py
@time: 2017/8/29 14:36
"""
import webbrowser

import bs4
import requests


def func():
    print('Baiduing...')
    res = requests.get('http://www.baidu.com/s?wd=敏感词过滤')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # print(soup.prettify())
    linkElems = soup.select('h3 a')
    numOpen = min(2, len(linkElems))
    for i in range(numOpen):
        webbrowser.open(linkElems[i].get('href'))


if __name__ == '__main__':
    func()
