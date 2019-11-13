#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:14:01 2017

@author: kevinchangwang
"""
from __future__ import print_function
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, Flatten, MaxPooling2D
from keras.optimizers import SGD, RMSprop, Adam, Nadam
from keras.utils import np_utils
import scipy.io
import numpy as np
np.random.seed(1337)
from keras import backend as K
K.set_image_dim_ordering('th')
'''
Importing data
'''
print('Loading Data...')
data = scipy.io.loadmat('/home/kevinchangwang/Downloads/sp1s_aa_1000Hz.mat')
y_test = np.loadtxt('/home/kevinchangwang/Downloads/sp1s_aa_1000Hz_test.mat')
'''
Preprocessing the data
'''
#reshape the x variables to the correct input dimensions for LSTM and convert to float 32
print('Processing Data...')
x_train = data['x_train'].reshape((316,1,500,28))
x_train /= 250
#x_train = x_train + 1
x_train = x_train.astype('float32')

x_test = data['x_test'].reshape((100,1,500,28))
x_test /= 250
#x_test = x_test + 1
x_test = x_test.astype('float32')

#reshpe  y data to the correct dimensions and convert to float 32

y_train = data['y_train'].reshape(316)
tmp_train = []
for i in y_train:
    if i == 1:
        tmp_train.append(1)
    elif i == 0:
        tmp_train.append(-1)
y_train = np.array(tmp_train)
y_train = np_utils.to_categorical(y_train, 2)
y_train = y_train.astype('float32')

y_test = y_test.reshape(100)
tmp_test = []
for i in y_test:
    if i == 1:
        tmp_test.append(1)
    elif i == 0:
        tmp_test.append(-1)       
y_test = np.array(tmp_test)
y_test = np_utils.to_categorical(y_test, 2)
y_test = y_test.astype('float32')

'''
Build the model
'''
print('Building model ...')

activ = 'relu'

model = Sequential()
model.add(Conv2D(100, (7, 1), input_shape = (1, 500, 28), activation = activ ))
model.add(Dropout(0.3))
model.add(Conv2D(10, (5, 5), activation = activ))
model.add(Dropout(0.3))
model.add(Conv2D(5, (1, 1), activation = activ))
model.add(Dropout(0.3))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(120, activation = activ))
model.add(Dropout(0.3))
model.add(Dense(100, activation = activ))
model.add(Dropout(0.3))
model.add(Dense(2, activation = 'softmax'))

model.summary()

# Optimizer settings
optim = Nadam(lr = 0.001)

model.compile(loss = 'categorical_crossentropy', optimizer = optim, metrics = ['accuracy'])

'''
Fitting the model
'''
print('Fitting model ...')

model.fit(x_train, y_train, epochs=10, batch_size=10)

print('Calculating the score...')
score, acc = model.evaluate(x_test, y_test,
                            batch_size=1)
print('Test score:', score)
print('Test accuracy:', acc)



