# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 11:58
# @File    : AssignCookies.py


'''
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

注意：

你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干。

示例 1:

输入: [1,2,3], [1,1]

输出: 1

解释:
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
'''


def assign_cookie(child_lists, cookie_lists):
    '''
    贪心算法
    :param child_lists:
    :param cookie_lists:
    :return:
    '''
    child_lists.sort()
    cookie_lists.sort()

    child = 0
    cookie = 0

    while cookie < len(cookie_lists) and child < len(child_lists):
        if cookie_lists[cookie] > child_lists[child]:
            child += 1
        cookie += 1
    return child


def change(money_value, count, money):
    sum = 0
    dict = {}
    for i in range(len(money_value)):
        sum += money_value[i] * count[i]
    print(sum)
    if sum < money:
        return False
    for j in range(len(money_value) - 1, -1, -1):
        if money >= money_value[j]:
            n = money // money_value[j]
            if n > count[j]:
                n = count[j]
            money -= n * money_value[j]
            dict[money_value[j]] = n

    if money != 0:
        return '零钱不足'
    else:
        return dict


money_value = [1, 5, 10, 20, 50, 100]
count = [2, 0, 10, 5, 1, 1]
money = 273
data_type = change(money_value, count, money)
if isinstance(data_type, dict):
    for k, v in data_type.items():
        print('%d元：%d张' % (k, v))
else:
    print(data_type)
