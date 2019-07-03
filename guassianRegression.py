# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:17:37 2019

@author: Vishal
"""

"""import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

fig = plt.figure()

#plt.plot(x, np.sin(x), '-')
#plt.plot(x, np.cos(x), '--')


plt.plot(x, np.sin(x - 0), color='blue')
plt.plot(x, np.sin(x - 1), color='g')
plt.plot(x, np.sin(x - 2), color='0.75')
plt.plot(x, np.sin(x - 3), color='#FFDD44')
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3))
plt.plot(x, np.sin(x - 5), color='chartreuse')

y = np.linspace(0, 1, 100)

plt.plot(y, np.sin(y - 0.1), color = 'r')"""


import matplotlib.pyplot as plt
import numpy as np
import math
from math import pi

def gaussian(x, mu, sig):

    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

axes = plt.gca()
axes.set_ylim([0, 1])

x_values = np.linspace(-1, 1, 100)
axes.set_xlim([-1, 1])

mu = []
for i in range(11):
    a = i / 10
    mu.append(a)


for mu, sig in [(0, 1), (0.2, 1), (0.4, 1), (0.6, 1), (0.8, 1), (1, 1)]:
    plt.plot(x_values, gaussian(x_values, mu, sig))


plt.show()