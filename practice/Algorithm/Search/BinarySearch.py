# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 23:01
# @File    : BinarySearch.py
# detail

'''
二分查找(Binary Search):
算法核心：在查找表中不断取中间元素与查找值进行比较，以二分之一的倍率进行表范围的缩小。
'''
def binary_search(lists, target):
    start = 0
    end = len(lists) - 1
    while start <= end:
        mid = (start + end) // 2
        if lists[mid] > target:
            end = mid - 1
        elif lists[mid] < target:
            start = mid + 1
        else:
            return True
    return False

'''
插值查找算法核心：是将二分法中的1/2用公式 value = （target - lists[start]）/(lists[end] - lists[start])
            所以中间值 mid = start + int((end - start) * （target - lists[start]）/(lists[end] - lists[start]))
'''

'''
查找算法
'''

if __name__ == '__main__':
    print(binary_search([1,7,8,9], 5))
    a = int(0.5)
    print(a)