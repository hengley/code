# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 15:21
# @File    : DeleteDuplicates.py


'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.val != current.next.val:
            current = current.next
        else:
            current.next = current.next.next
    return head


'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def delete_duplicates2(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head

    dummy = ListNode(0);  # 创建虚拟链表
    dummy.next = head

    pre = dummy  # 设置先前值
    cur = head   # 设置当前值
    while cur:
        if cur.next and cur.val == cur.next.val:
            # 循环直到当前值为最后的重复值
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            cur = cur.next
            pre.next = cur
        else:
            pre = pre.next
        cur = cur.next
    return dummy.next


def delete_duplicates3(head):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr:
        has_dup = False
        # Remove duplicates and leave the last of the duplicates.
        while curr.next and curr.next.next and curr.next.val == curr.next.next.val:
            curr.next = curr.next.next
            has_dup = True
        if has_dup:
            # Remove the last duplicate
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


def delete_duplicates4(head):
    """
    Time complexity: O(n). Space complexity: O(1), n is len(linked list).
    """
    prev = None
    curr = head
    while curr:
        found = False  # did we find node with duplicate value?
        # compare current node's value with next node's value
        while curr and curr.next and curr.val == curr.next.val:
            found = True
            curr = curr.next
        # after exiting the while loop curr is gonna point to the last
        # duplicate node, if there's one
        if found:
            curr = curr.next  # move curr pointer to the next unique node
            if prev != None:
                prev.next = curr  # skip all duplicates
            else:  # prev == None, 1st duplicate node is the 1st node in the list
                head = curr
        else:  # no duplicates were found
             prev, curr = curr, curr.next
    return head

