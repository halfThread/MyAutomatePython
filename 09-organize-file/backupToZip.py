#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: backupToZip.py
@time: 2017/7/31 10:11
"""
import os
import zipfile


def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)

        for filename in filenames:
            # 跳过压缩包文件
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')


if __name__ == '__main__':
    backupToZip("D:\\temp")
