"""-------------numpy-----------"""
#%% numpy

import numpy as np
from numpy.core.fromnumeric import ravel

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

# %% indexing and slicing
import numpy as np
array = np.array([1,2,3,4,5,6,7]) # vector dimension=1

print(array[0])
print(array[0:4])
print(array[0:-2])
print(array[:-2])
print(array[::-2])
print(array[::3])
print(array[1:5:2])

reverse_array=array[::-1]
print(reverse_array)
print("---------------------------------------")

array1=np.array([[1,2,3,4,5],[4,5,6,7,8]])
print(array1)
print(array1[1,1])

print(array1[:,1])

print(array1[1,1:4])


# %% # shape manipulation
print("---------------------------------------")

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
#flatten
print(array)
a=array.ravel()
array2=a.reshape(3,3)
print(a)
print(array2)
arrayT=array2.T
print(arrayT)


print(a)
a.resize((3,3))
print(a)


# %%stacking arrays

array1=np.array([[1,2],[3,4]])
array2=np.array([[-1,-2],[-3,-4]])

print("array 1 :",array1,"\n array2 : ",array2)

#vertical
array3=np.vstack((array1,array2))
print(array3)
#horizontal
array4=np.hstack((array1,array2))
print(array4)


#convert and copy

liste = [1,2,3,4]
array = np.array(liste)
liste2=list(array)

a =np.array([1,2,3]) #memory
b=a
c=a
b[0]=5
print(a)

d=np.array([1,2,3])
e=d.copy()
f=d.copy()


# %%

"""-----------pandas------------"""