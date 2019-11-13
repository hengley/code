# -*- coding: utf-8 -*-
# @Time    : 2017/12/3 23:19
# @File    : 4_1.py
# 将多个小字符拼接成一个大字符

pj = ["<123>","<sad>","<wqe>","<23>","<fs>"]

# 拼接的字符比较少的时候可以用，字符多的时候会造成浪费
s = ''
for x in pj:
    s += x

# 字符多的时候
bz = ''.join(pj)

print bz

