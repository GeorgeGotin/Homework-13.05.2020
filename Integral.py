import random
import matplotlib.pyplot as plt
import numpy as np

class integral():
	def __init__(self,f,a=0,b=1,n=100):
		self.f=f
		self.a=a
		self.b=b
		self.n=n
	def rectangle(self,space='in', f=None,a=None,b=None,n=None):
		f=self.f if f == None else f
		a=self.a if a == None else a
		b=self.b if b == None else b
		n=self.n if n == None else n
		h=0 if space == 'in' else 1 if space == 'out' else None
		s=0
		i=(b-a)/n
		for j in range(n):
			s+=f(a+i*(j+h))
		return s*i
	
	def trapeze(self,f=None,a=None,b=None,n=None):
		f=self.f if f == None else f
		a=self.a if a == None else a
		b=self.b if b == None else b
		n=self.n if n == None else n
		s=0
		i=(b-a)/n
		for j in range(n):
			s+=(f(a+i*j)+f(a+i*(j+1)))/2
		return s*i
	
	def Monte_Carlo(self,f=None,a=None,b=None,n=None):
		f=self.f if f == None else f
		a=self.a if a == None else a
		b=self.b if b == None else b
		n=self.n if n == None else n
		s=0
		i=(b-a)/n
		h=max([f(i) for i in np.linspace(a,b,n)])
		xs=[]
		ys=[]
		for j in range(n):
			xs.append(random.uniform(a,b))
			ys.append(random.uniform(0,h))
			s+=1 if ys[-1] <= f(xs[-1]) else 0
		'''
		plt.plot(xs,ys,'o')												#to see distribution
		plt.plot(np.linspace(a,b,n),np.array([f(i) for i in np.linspace(a,b,n)]))
		plt.show()
		'''
		return ((b-a)*h)*s/n

def f1(x):
	return 2/(1 + x**2)

def f2(x):
	return 1/(1-x**2)**0.5 if x**2!=1 else 0 							#we just need it


a = integral(f2,-1,1,1000000)
print(a.rectangle('in'),a.rectangle('out'))
print(a.trapeze())
print(a.Monte_Carlo())


a.f=f1
intg = [a.rectangle,a.trapeze,a.Monte_Carlo]
n=np.array([10**i for i in range(7)])
fig = plt.figure()
a=[]
for j in range(3):
	a.append(fig.add_subplot(1,3,j+1))
	a[j].grid(axis='both')
	a[j].semilogx(n,[abs(intg[j](a=-1,b=1,n=i)-np.pi) for i in n])
plt.show()

