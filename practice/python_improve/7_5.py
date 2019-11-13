# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 21:30
# @File    : 7_5.py
# 让类支持比较操作

from functools import total_ordering
from abc import abstractmethod
from math import pi

@total_ordering
#修饰器推测出了__eq__ 和 __gt__
class Shape(object):
    @abstractmethod
    def area(self):
        pass

    def __lt__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape!')
        return self.area() < obj.area()

    def __eq__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape!')
        return self.area() == obj.area()

''' 
    def __le__(self, obj):
        return self < obj or self == obj

    def __gt__(self, obj):
        return not (self < obj or self == obj)
'''

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * pi


r1 = Rectangle(5, 3)
r2 = Rectangle(4,2)
c = Circle(2)

print c > r2 # r1.__lt__(r2)