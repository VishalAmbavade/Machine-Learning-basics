import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
import sys

lamd=0.001

def generateX(k,m,d):
	A=np.ones((d,1), float)
	for i in range(1,m+1):
		temp=k**i
		A=np.hstack((A,temp))
	return A

while(1):
	m=int(input("Enter degree(-1 for e2xit): "))

	if(m==-1):
		sys.exit()
	else:
		d=int(input("Enter the size of data points: "))
		x=np.linspace(0,1,d)
		noise=np.random.normal(0,1,d)
		t=np.sin(2*np.pi*x) + noise


		k=np.zeros((d,1), float)
		l=np.zeros((d,1),float)
		for i in range(0,d):
			k[i][0]=x[i]
			l[i][0]=t[i]
		X=generateX(k,m,d)

		#a=inv(np.dot(np.transpose(X),X))
		#b=np.dot(np.transpose(X),l)
		#W=np.dot(a,b)
		a=np.dot(np.transpose(X),l)
		b=inv(np.dot(np.transpose(X),X) + lamd*(np.identity(m+1)))
		W=np.dot(b,a)
		print(W)

		x_1=np.linspace(0,1,100)
		f=np.zeros((100,1), float)
		for i in range(0,100):
			f[i][0]=x_1[i]
		X_1=generateX(f,m,100)
		Y=np.dot(X_1,W)

		for i in range(m):
			e=W[i]*(x**i)
			plt.plot(x,e)
		plt.show()