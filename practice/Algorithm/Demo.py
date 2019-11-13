# -*- coding: utf-8 -*-
# @Time    : 2018/4/6 14:00
# @File    : Demo.py

from Algorithm.Sort.generateArrayHelper import generateArray


class SortAlgorithm(object):
    def __init__(self, lists):
        self.lists = lists

    def selection_sort(self):
        for j in range(len(self.lists)):
            # 寻找最小值
            min_num = j
            for i in range(j+1, len(self.lists)):
                if self.lists[i] < self.lists[min_num]:
                    min_num = i
            self.lists[min_num], self.lists[j] = self.lists[j], self.lists[min_num]
        return self.lists

    '''
    首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。
    1、选取一个划分元素（partition element，有时又称为pivot）；

    2、重排列表将其划分为三个部分：left（小于划分元素pivot的部分）、划分元素pivot、right（大于划分元素pivot的部分），此时，划分元素pivot已经在列表的最终位置上；

    3、分别对left和right两个部分进行递归排序。
    '''
    def quick_sort(self, left, right):
        if left <= right:
            return self.lists
        low = left
        high = right
        pivot = self.lists[left]
        while left < right:
            while left < right and self.lists[right] <= pivot:
                right -= 1
            self.lists[left] = self.lists[right]

            while left < right and self.lists[left] <= pivot:
                left += 1
            self.lists[right] = self.lists[left]
        self.lists[right] = pivot
        self.quick_sort(pivot, low, left - 1)
        self.quick_sort(pivot, left + 1, high)

        return







if __name__ == '__main__':
    sort = SortAlgorithm(lists=generateArray(10))
    sort_list = sort.selection_sort()
    print(sort_list)
