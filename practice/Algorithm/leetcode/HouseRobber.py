# -*- coding: utf-8 -*-
# @Time    : 2018/5/5 21:12
# @File    : HouseRobber.py

'''

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = = 2 + 9 + 1 = 12 。

f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max(f(k-2) + nums[k], f(k))
'''


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last, now = 0, 0
    for num in nums:
        last, now = now, max(last + num, now)
    return now


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    ll = [0 for i in range(n)]
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums)
    else:
        ll[0] = nums[0]
        ll[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        ll[i] = max(ll[i-2] + nums[i], ll[i-1])

    return ll[-1]
