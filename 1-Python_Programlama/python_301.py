#%% numpy

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,45,15])

print(array)
print(array.shape)

a=array.reshape(3,5)

print(a)

print("shape : ",a.shape)
print("dimension : ",a.ndim)
print("data type: ",a.dtype.name)
print("size : ", a.size)
print("type : ",type(a))

array1=np.array([[1,2,3,4],[5,6,7,8],[9,3,8,7]])
print(array1)

zeros=np.zeros((3,4))
print(zeros)

zeros[0,0]=5
print(zeros)

print(np.ones((3,4)))
print(np.empty((2,3)))

a=np.arange(10,50,5)
print(a)

a=np.linspace(10,50,20)
print(a)
# %% numpy basic operations

a=np.array([1,2,3])
b=np.array([4,5,6])
print("a: ",a ,"\n b: ",b)
print("a+b: ",a+b)
print("a-b: ",a-b)
print("a**2 : ",a**2)

print(np.sin(a))

print(a<2)
#element wise product
print("a*b: ",a*b)

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])

#matrix product
print("b.T :" ,b.T)
print("a.dot(b) : ",a.dot(b.T))

print("np.axp(a) : ", np.exp(a))


c= np.random.random((5,5))
print(c)
print(c.sum())
print(c.max())
print(c.min())

print(c.sum(axis=0))
print(c.sum(axis=1))

print(np.sqrt(c))
print(np.square(c))

# %%
