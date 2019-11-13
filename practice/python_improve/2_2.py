from random import randint

g = {x: randint(60,100) for x in 'xyzabc'}

g_sorted = sorted(g.items(), key = lambda x: x[1])

print g_sorted