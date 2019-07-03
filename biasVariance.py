# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:35:14 2019

@author: Vishal
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

x = np.linspace(-1, 1, 100)
sinCurve = np.sin(pi * x)

plt.plot(x, sinCurve)

x_val = []
y_val = []

temp_x = np.linspace(-1, 1, 100)
def hypo1(p1, p2):
    mean = (p1[1] + p2[1]) / 2
    slope = 0
    y_1 = slope * temp_x + mean  
    plt.plot(temp_x, y_1, color = 'k', alpha = 0.2)
    bias1 = np.mean((y_1 - sinCurve)**2)
    bias1 = np.mean(bias1)
    var1 = np.mean((y_1 - bias1)**2)
    return bias1, var1
    
#print("Bias1: ", np.mean((temp_x - sinCurve)**2))
    

temp = []
temp_x2 = np.linspace(-1, 1, 100)
def hypo2(p1, p2, slope):    
    c = p1[1] - (p1[0] * slope)
    y_2 = slope * temp_x2 + c
    axes = plt.gca()
    axes.set_ylim([-1, 1])
    plt.plot(x, sinCurve, color = 'r')
    plt.plot(temp_x2, y_2, color = 'k', alpha = 0.2)  
    bias2 = np.mean((y_2 - sinCurve)**2)
    bias2 = np.mean(bias2)
    var2 = np.mean((y_2 - bias2)**2)
    return bias2, var2
    #print("Bias2: ", np.mean((y_2 - sinCurve)**2))

  
"""def calcBias(temp_x, y_1):
    print(temp_x)"""

data = []

for i in range(100):
    x1 = np.random.choice(x)
    y1 = np.sin(pi * x1) 
    x2 = np.random.choice(x)
    y2  = np.sin(pi * x2)
    data.append([[x1, y1], [x2, y2]])
    
#print(data[1][1][1])
    
for point in (data):
    p1 = point[0]
    p2 = point[1]
    b1, v1 = hypo1(p1, p2)
    
print("Bias1: ", b1)
print("Variance: ",  v1)
plt.show()

#slopes = []
for point in (data):
    p1 = point[0]
    p2 = point[1]
    #print(p1)
    slope = ((p2[1] - p1[1]) / (p2[0] - p1[0]))
    #print(p1)
    #slopes.append(slope)
    b2, v2 = hypo2(p1, p2, slope)
    
print("Bias2: ", b2)
print("Variance2: ", v2)
    
#print(slopes)
plt.show()


"""for i in range(data):
    #xaxis ie time is along the row , for ith b we use h0[:,i]
    bias_h0[i] = (np.mean(h0[:,i])-np.sin(np.pi*x[i]))**2
    bias_h1[i] = (np.mean(h1[:,i])-np.sin(np.pi*x[i]))**2
    var_h0[i] = np.mean((h0[:,i] - np.mean(h0[:,i]) )**2)
    var_h1[i] = np.mean((h1[:,i] - np.mean(h1[:,i]) )**2)
    
"""    
    
    #x1_temp.append(data1)
    #y1 = np.sin(pi*data1)
    #y1_temp.append(y1)
    
    #plt.scatter(x1_temp, y1_temp)
    #print(x1, y1)
    #plt.scatter(x1, y1)

#print(x1_temp)    
"""x2_temp = []
y2_temp = []
    
for i in range(50):
    data2 = np.random.uniform(0, 1, 2)
    x2_temp.append(data2)
    y2 = np.sin(pi*data2)
    y2_temp.append(y2)
    
    plt.scatter(x2_temp, y2_temp)"""
   

#plt.scatter(X, sinCurve)
#plt.show()