# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 21:15
# @File    : 7_4.py
# 创建可管理的对象属性

from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            return ValueError('Wrong type!')
        self.radius = float(value)

    def getArea(self):
        return  self.radius ** 2 * pi

    R = property(getRadius, setRadius)

c = Circle(3.2)
c.R = 4.5
print c.R

