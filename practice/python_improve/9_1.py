# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 22:20
# @File    : 9_1.py
# 如何使用修饰器

#装饰器
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

# 斐波那契数列:
@memo #相当于fibonacii = memo(fibonacii)
def fibonacii(n):
    if n <=1:
        return 1
    return fibonacii(n - 1) + fibonacii(n - 2)

# fibonacii = memo(fibonacii)
print fibonacii(20)

# 一共10个台阶的楼梯，从下到上，一次只能迈1-3步，不能后退，有多少种走法
@memo
def cilmb(n, steps):
    count = 0
    if n == 0:
        count = 1
    if n > 1:
        for step in steps:
            count += cilmb(n - step, steps)
    return count