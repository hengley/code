# -*- coding: utf-8 -*-
# @Time    : 2018/5/1 11:54
# @File    : ClimbStairs.py

'''
假设你正在爬楼梯。需要 n 步你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
'''


# 递归
def climb_stairs(n):
    if n == 0 or n == 1 or n == 2:
        return n
    else:
        total = climb_stairs(n - 1) + climb_stairs(n - 2)
    return total


# 压缩法
def climb_stairs2(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a + b
    return a


# 动态规划
def climb_stairs3(n):
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
    return res[n - 1]
