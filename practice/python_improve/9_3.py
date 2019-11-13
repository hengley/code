# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 23:16
# @File    : 9_3.py
# 如何定义参数可变的装饰器

from functools import wraps
import time
import logging

def warn(timeout):
    timeout = [timeout]
    def decortaor(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s": %s > %s' %(func.__name__, used, timeout[0])
                logging.warn(msg)
            return res

        def setTimeout(k):
            # python 3 (nonlocal timeout)
            timeout[0] = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decortaor

from random import randint
@warn(1.5)
def test():
    print 'In test'
    while randint(0, 1):
        time.sleep(0.5)

for _ in range(10):
    test()

test.setTimeout(1)
for _ in range(10):
    test()