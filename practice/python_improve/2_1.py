from random import randint
from collections import Counter

data = [randint(0, 20) for _ in xrange(30)]

c = dict.fromkeys(data, 0)

for x in data:
    c[x] += 1

c2 = Counter(data)

print c2.most_common(3)