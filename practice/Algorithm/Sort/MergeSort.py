# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 21:52
# @File    : MergeSort.py
# detail

from Algorithm.Sort.generateArrayHelper import generateArray

'''
归并（Merge）排序法是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的。
然后再把有序子序列合并为整体有序序列。归并过程：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；
否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。
归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。
'''


def merge(left, right):
    result = []
    i, j = 0, 0
    while len(left) > i and  len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    if len(lists) <=1:
        return lists
    middle = len(lists)//2
    left = lists[:middle]
    right = lists[middle:]
    return merge(merge_sort(left), merge_sort(right))


new_lists = merge_sort(generateArray(0))
print (new_lists)

