from random import randint, sample

name = sample('abcdefg', randint(2,4))
g = {x: randint(1,4) for x in name}
s1 = g
s2 = g
s3 = g
j = reduce(lambda a,b: a&b, map(dict.viewkeys, [s1, s2, s3]))

print j