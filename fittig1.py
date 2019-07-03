import matplotlib.pyplot as plt
from numpy.linalg import inv
from math import pi
import numpy as np
import scipy.interpolate as interpolate

degree = 2
x = np.linspace(0,1,100)
X = np.linspace(0,1,10)
noise = np.random.normal(scale=1.0, size=X.shape)
y = np.sin(2*pi*X)+noise
z = np.sin(2*pi*x)



print(X.shape[0])
b = np.empty([X.shape[0], 0])
print(b.shape)
X.resize(len(X),1)
for i in range(degree+1):
    b = np.concatenate((b,np.power(X,i)),axis=1)
w = inv(b.T.dot(b)).dot(b.T).dot(y.T)
p = np.matmul(w,b.T)
print(w)

xnew = np.linspace(min(X),max(X),100)
tck = interpolate.splrep(X,p)
y_smooth = interpolate.splev(xnew,tck)


plt.scatter(X, y, color = 'red', label = 'data points')
plt.plot(x, z, color = 'blue', label = 'sine curve')
plt.plot(xnew, y_smooth, color = 'red', label = 'fittig curve')
plt.legend(loc = 0)
plt.show()
