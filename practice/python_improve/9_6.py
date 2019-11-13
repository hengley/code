# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 23:40
# @File    : 9_6.py
# 如何在一个for语句中迭代多个可迭代对象
from random import randint
chinese = [randint(60, 100) for _ in xrange(10)]
english = [randint(60, 100) for _ in xrange(10)]
math = [randint(60, 100) for _ in xrange(10)]

total = []
for c, e, m in zip(chinese, english, math):
    total.append(c + e + m)
print(total)

from itertools import chain
count = 0
for s in chain(chinese, math, english):
    if s > 90:
        count += 1
print count