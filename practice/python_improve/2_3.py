from collections import OrderedDict
from time import time
from random import randint

d = OrderedDict()

players = list('abcdefgh')

start = time()

for i in xrange(len(players)):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start
    d[p] = (i+1, end - start)

print
print '-' *20

for k in d:
    print k, d[k]