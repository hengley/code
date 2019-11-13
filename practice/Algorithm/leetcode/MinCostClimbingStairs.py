# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 23:53
# @File    : MinCostClimbingStairs.py


def minCostClimbingStairs1(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    # if n == 2:
    #     return min(cost[0], cost[1])
    dp = [0]*n
    for i in range(2, n):
        dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
    return dp[-1]


def minCostClimbingStairs2(cost):
    n = len(cost)
    dp = [0]*n
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])


def minCostClimbingStairs3(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    min_cost1, min_cost2 = cost[0], cost[1]
    for c in cost[2:]:
        min_cost1, min_cost2 = min_cost2, min(min_cost1, min_cost2) + c
    return min(min_cost1, min_cost2)
