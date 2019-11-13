#coding: utf8
#对多种分隔符进行分割

import re

def mySplit(s, ds):
    res = [s]

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t

    return [x for x in res if x]

s = 'adf;sdf|sdfaf,asdfas\tasdf/adsffsd,afda'
#print mySplit(s, ';|\/,')
print re.split(r'[;|\t/,]+', s)



