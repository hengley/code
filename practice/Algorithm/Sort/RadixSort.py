# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 17:35
# @File    : RadixSort.py
# detail

import math
from Algorithm.Sort.generateArrayHelper import generateArray

'''
基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。
有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序，最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。
基数排序基于分别排序，分别收集，所以其是稳定的排序算法。
'''


def radix_sort(lists, radix = 10):
    k = int(math.log(max(lists), radix))
    bucket = [[] for b in range(radix)]
    for i in range(k + 1):
        for j in lists:
            bucket[j / (radix ** i) % radix].append(j)
        del lists[:]
        for l in bucket:
            lists += l
            del l[:]
    return lists


new_lists = radix_sort(generateArray(10))
print(new_lists)