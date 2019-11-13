# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 17:21
# @File    : BubbleSort.py
# detail

from Algorithm.Sort.generateArrayHelper import generateArray

'''
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
'''


def bubble_sort(lists):
    for i in range(len(lists)):
        for j in range(len(lists) - 1, i, -1):
            if lists[j - 1] > lists[j]:
                lists[j - 1], lists[j] = lists[j], lists[j - 1]
    return lists


new_lists = bubble_sort(generateArray(10))
print(new_lists)
