# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 18:45
# @File    : SelectSort.py
# detail

from Algorithm.Sort.generateArrayHelper import generateArray


# 首先在未排序序列中找到最小元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小元素，然后放到排序序列末尾。以此递归。
def select_sort(lists):
    for i in range(len(lists)):
        max_num = i
        for j in range(i + 1, len(lists)):
            if lists[max_num] < lists[j]:
                max_num = j
        lists[max_num], lists[i] = lists[i], lists[max_num]
    return lists


new_lists = select_sort(generateArray(10))
print(new_lists)
