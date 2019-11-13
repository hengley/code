# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 15:02
# @File    : KeyboardRow.py


def keyboard_row(words):
    ans = []
    key_set = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    for key in key_set:
        for word in words:
            w = set(word.lower())
            if w.issubset(key):
                ans.append(word)
    return ans