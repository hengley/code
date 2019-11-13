# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 23:25
# @File    : QuickSort.py
# detail

from Algorithm.Sort.generateArrayHelper import generateArray

'''
首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。
1、选取一个划分元素（partition element，有时又称为pivot）；

2、重排列表将其划分为三个部分：left（小于划分元素pivot的部分）、划分元素pivot、right（大于划分元素pivot的部分），此时，划分元素pivot已经在列表的最终位置上；

3、分别对left和right两个部分进行递归排序。
'''


# 第一种方法
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    pivot = lists[left]
    low = left
    high = right
    print(lists)
    while left < right:
        while left < right and lists[right] >= pivot:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] < pivot:
            left += 1
        lists[right] = lists[left]

    lists[right] = pivot
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


# new_lists = quick_sort(generateArray(10),0,len(generateArray(10)) - 1)
# print(new_lists)


# 第二种方法
def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq.pop()
    left, right = [], []
    for x in seq:
        if x > pivot:
            right.append(x)
        else:
            left.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)


# 第三种方法
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

# 第四种方法
quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])
