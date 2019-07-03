# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:48:00 2019

@author: Vishal
"""

import numpy as np
import matplotlib.pyplot as plt

values=([0, 0], [1, 1])

print("Training input values without Bias: ", values)

test2 = [[-1]] * len(values)
values = np.concatenate((test2, values), axis = 1)  
print("\nTraining input values with bias in it\n",values)


m = 3     #number of elements in each row of inputs
n = 1 
weights = np.random.rand(m, n) * 0.1 - 0.5
print("\nInitial random weights: \n",weights)

final = ([[0],[1]])
print("\nTraining data target values are: ", final)

def updateWeights(weights, inputs, activation, targets):
    eta = 0.25
    weights += eta*np.dot(np.transpose(inputs), targets - activation)
    return weights

def  prediction (inputs, weights, targets):
    #representing Activation function with 'ack [[]]' variable
    ack = [[0]] * len(inputs)
    for i in range(0, len(inputs)):    
        for j in range(0,len(weights)):
            ack[i] += inputs[i][j] * weights[j]
        ack[i] = np.where(ack[i] > 0, 1, 0)
        #checking values with target
        if(targets[i] != ack[i]):
            weights = updateWeights(weights, inputs, ack[i], targets)
        print(ack[i])
    return weights

iterations = 2
for temp in range(0, iterations):
    print("\nIteration", temp + 1,"\n")
    weights = prediction(values, weights, final)
    
print("\nTrained Weights\n", weights)

def perceptronPredict(weights, newInput):
    activation = np.dot(newInput, weights)
    activation = np.where(activation > 0, 1, 0)
    print(activation)
    
xVal = [] 
yVal = []
for i in range(1, 3):
    xVal.append(values[0][i])
    yVal.append(values[1][i])
    
print(xVal, yVal)

plt.scatter(xVal, yVal)

"""newInput = ([-1.0, 1.786745, 2.94569],
            [-1.0, 7.023323, 1.9999])
perceptronPredict(weights, newInput)"""