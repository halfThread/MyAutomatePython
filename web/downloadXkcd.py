#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: downloadXkcd.py
@time: 2017/8/29 16:24
"""
import os

import bs4
import requests


def func():
    url = 'https://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)
    while not url.endswith('#'):  # 第一页url后带#号
        print("Downloading page %s...." % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print("Could not find comic image.")
        else:
            comicUrl = comicElem[0].get('src')
            print('Downloading images %s' % comicUrl)
            res = requests.get(str('http:' + comicUrl))
            res.raise_for_status()

            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')


if __name__ == '__main__':
    func()
