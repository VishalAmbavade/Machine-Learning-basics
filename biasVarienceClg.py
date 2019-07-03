import numpy as np
import matplotlib.pyplot as plt
from math import pi


z = np.linspace(-1,1,100)
z1 = np.sin(pi*z)
plt.plot(z,z1)

dataset = []
y_values = []
for i in range(100):
    data = np.random.uniform(-1,1,2)
    y = np.sin(pi*data)
    dataset.append(data)
    y_values.append(y)
    plt.scatter(data,y)
    
#print(dataset)

#plt.show()

for i in range(100):
    if(i % 2 == 0):
        a = (sum(dataset[i])/2)
        print(a)
        
print(a.shape)
    
#print(a.shape)
    
    
#print(dataset[0])