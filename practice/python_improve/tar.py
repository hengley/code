# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 21:36
# @File    : tar.py
# 将xml文件打包

import tarfile
import os

def tarXml(tfname):
    tf = tarfile.open(tfname, 'w:gz')
    for fname in os.listdir('.'):
        if fname.endswith('.xml'):
            tf.add(fname)
            os.remove(fname)
        tf.close()

        if not tf.members:
            os.remove(tfname)

tarXml('test.zip')