# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 21:08
# @File    : 4_2.py
# Python 2 and Python 3 读写文本, 读写入文本中的数据都是字节，读写数据时都需要编码。

# Python 2
f = open('py2.txt','w')
s = u"你好"
f.write(s.encode('utf8'))
f.close()
f = open('py2.txt','r')
t = f.read()
print t.decode('utf8')

 # Python 3
f = open('py3.txt', 'wt', encoding='utf8')
f.write('Hello, world!')
f.close()
f = open('py3.txt', 'rt', encoding='utf8')

print f.read()