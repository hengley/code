# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 13:03
# @File    : ReverseString.py


def reverse_string(s):
    return s[::-1]


def reverse_string2(s):
    n = len(s)
    if n < 2:
        return s
    l = reverse_string2(s[n // 2:])
    r = reverse_string2(s[:n // 2])
    res = l + r
    return res
