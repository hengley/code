# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 23:48
# @File    : InsertSort.py
# detail

from Algorithm.Sort.generateArrayHelper import generateArray

'''
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。
插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素， 但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。
在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
'''


def insert_sort(lists, start, gap):
    for index in range(start + gap, len(lists), gap):
        # 记录大循环走到了第几个元素的值
        currentValue = lists[index]
        # 当前位置的左边gap个位置
        previus_num = index
        # 当前元素的左边的紧靠的元素比它大,要把左边的元素一个一个的往右移gap位,给当前这个值插入到左边挪gap个位置出来
        while previus_num >= gap and lists[previus_num - gap] > currentValue:
            # 左边位置的值向右移动gap位
            lists[previus_num] = lists[previus_num - gap]
            previus_num -= gap
        # 已经找到了左边排序好的列表里不小于current_val的元素的位置,把current_val放在这里
        lists[previus_num] = currentValue
    return lists


new_lists = insert_sort(generateArray(10), 0, 1)
print(new_lists)


def insert_sort2(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists
