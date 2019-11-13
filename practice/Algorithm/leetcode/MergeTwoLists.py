# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 15:16
# @File    : MergeTwoLists.py


'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def merge_two_lists(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_two_lists(l1.next, l2)
    return l1 or l2
