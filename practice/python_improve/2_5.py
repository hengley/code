#-*- coding:utf-8 –*-

#猜数字游戏
from random import randint
from collections import deque

history = deque([], 5)
N = randint(0, 100)

def guess(k):
    if k == N:
        print "Right!"
        return True
    if k < N:
        print '%s is less than N' %k
    else:
        print '%s is bigger than N' %k
    return False

while True:
    line = raw_input("请输入一个0~100之间的数：")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h':
        print list(history)

