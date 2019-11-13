# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 23:10
# @File    : SymmetricTree.py


'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return

    def isSymmetrical(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outSymmetrical = self.isSymmetrical(left.left, right.right)
            inSymmetrical = self.isSymmetrical(left.right, right.left)
            return outSymmetrical and inSymmetrical
        else:
            return False
