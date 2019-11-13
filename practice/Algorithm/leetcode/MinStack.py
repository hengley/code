# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 23:34
# @File    : MinStack.py


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        return self.stack.append((x, x if not self.stack else min(self.getMin(), x)))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

