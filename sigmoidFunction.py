# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:36:56 2019

@author: Vishal
"""

import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return(1 / (1 + np.exp(-x)))


#x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 100)

#plt.plot(x, sigmoid(x), 'r')
plt.plot(y, sigmoid(y), 'b')

#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
#plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))
