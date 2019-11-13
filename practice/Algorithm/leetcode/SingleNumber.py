# -*- coding: utf-8 -*-
# @Time    : 2018/5/1 0:00
# @File    : SingleNumber.py

from functools import reduce
import operator

'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''


def single_number1(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for key, val in dic.items():
        if val == 1:
            return key


def single_number2(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


def single_number3(nums):
    return 2 * sum(set(nums)) - sum(nums)


def single_number4(nums):
    return reduce(lambda x, y: x ^ y, nums)


def single_number5(nums):
    return reduce(operator.xor, nums)
