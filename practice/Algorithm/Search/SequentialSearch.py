# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 22:54
# @File    : SequentialSearch.py
# detail

'''
无序表查找:
也就是数据不排序的线性查找，遍历数据元素。
算法分析：最好情况是在第一个位置就找到了，此为O(1)；最坏情况在最后一个位置才找到，此为O(n)；所以平均查找次数为(n+1)/2。 最终时间复杂度为O(n)
'''

def sequential_search(lists, target):
    for i in lists:
        if i == target:
            return True
        else:
            return False


'''
二分查找
'''
# def binary_search(lists, target):
#     start = 0
#     end = len(lists) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if lists[mid] > target:
#             end = mid - 1
#         elif lists[mid] < target:
#             start = mid + 1
#         elif lists[mid] == target:
#             print mid
#             return True
#     print '没有该数字！'
#     return False


# 针对有序查找表的二分查找算法
# 时间复杂度O(log(n))

def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low <= high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印折半的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


if __name__ == '__main__':
    LIST = [1, 5, 6, 9]
    result = binary_search(LIST, 0)
    print(result)

'''
插值查找算法核心: value = (target - lists[start]) / (lists[end] - lists[start])
               mid = start + int((end - start) * (target - lists[start]) / (lists[end] - lists[start]))
                
'''