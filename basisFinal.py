# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:05:03 2019

@author: Vishal
"""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from scipy.interpolate import interpolate
import numpy as np
from math import pi

x = np.linspace(0,1,100)
X = np.linspace(0,1,10)
noise = np.random.normal(scale= 0.25, size=X.shape)
y = np.sin(2*pi*X)+noise
z = np.sin(2*pi*x)


n = len(x)                          #the number of data
mean = sum(x*z)/n                   #note this correction
sigma = sum(z*(x-mean)**2)/n        #note this correction

def gaus(y,a,x0,sigma):
    return a*exp(-(y-x0)**2/(2*sigma**2))

popt,pcov = curve_fit(gaus,x,z,p0=[1,mean,sigma])

xNew = np.linspace(min(X), max(X), 100)
tck = interpolate.splrep(X, y)
y_smooth = interpolate.splev(xNew, tck)


plt.fill_between(X, gaus(X,*popt), color='pink', alpha='0.5')

plt.plot(x,z, color = 'r')
plt.scatter(X, y, color = 'green')
plt.plot(X,gaus(X,*popt))
plt.show()