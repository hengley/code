#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:00:50 2017

@author: kevinchangwang
"""
import numpy as np
from sklearn import svm 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import scipy.io

'''
Importing data
'''
print('Loading Data...')
data = scipy.io.loadmat('/home/kevinchangwang/Downloads/sp1s_aa_1000Hz.mat')
y_test = np.loadtxt('/home/kevinchangwang/Downloads/sp1s_aa_1000Hz_test.mat')
'''
Preprocessing the data
'''
print('Processing Data...')
x_train = data['x_train'].reshape(316,14000)
x_train = x_train.astype('float32')

x_test = data['x_test'].reshape(100,14000)
x_test = x_test.astype('float32')

x_total = np.concatenate((x_train, x_test), axis = 0)

y_train = data['y_train'].reshape(316)
y_train = y_train.astype('float32')

y_test = y_test.reshape(100)
y_test = y_test.astype('float32')

y_total = np.concatenate((y_train, y_test), axis = 0)

X_train, X_test, Y_train, Y_test = train_test_split(x_total, y_total, test_size = 0.3, random_state = 20)

clf = svm.SVC(kernel='poly', C = 1.0)
clf.fit(X_train, Y_train)

accuracy = clf.score(X_test, Y_test)
print(accuracy)