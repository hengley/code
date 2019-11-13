# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 20:43
# @File    : 7_1.py
# 派生内置不可变类型并修改实例化行为

class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        super(IntTuple, self).__init__(iterable)

t = IntTuple([1,-3,'ads',5,['x', 'r'],9])
print t