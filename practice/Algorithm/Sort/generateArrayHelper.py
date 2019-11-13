# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 19:57
# @File    : generateArrayHelper.py
# detail
import random


def generateArray(n):
    arr = [random.randint(0, 1000) for num in range(n)]
    return arr
