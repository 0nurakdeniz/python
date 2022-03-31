
import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)

#print (df.Species.unique())

#print(df.info())

#print(df.describe())

setosa = df[df.Species =='Iris-setosa']
versicolor = df[df.Species == 'Iris-versicolor']
virginica = df[df.Species == 'Iris-virginica']


#print('setosa        :')
#print(setosa.describe())
#print('versicolor    :')
#print(versicolor.describe())
#print(virginica.describe())

import matplotlib.pyplot as plt
#line plot
df1= df.drop(["Id"],axis=1)
"""
df1.plot(grid=True,linestyle=":")
plt.show()

plt.plot(setosa.Id,setosa.PetalLengthCm , color = "red", label = "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm , color = "green", label = "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm , color = "yellow", label = "virginica")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()
"""
#scatter plot
"""
plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="setosa")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="yellow",label="virginica")

plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.legend()
plt.show()
"""

#histogram plot

"""
plt.hist(setosa.PetalLengthCm,bins=10)

plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("histogram plot")
plt.legend()
plt.show()

"""

#bar plot

import numpy as np


x = np.array([1,2,3,4,5,6,7])
y = 2*x+2

"""
plt.bar(x,y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("bar plot")
plt.legend()
plt.show()
"""

# subpolts

"""
#df1.plot(grid=True,linestyle=":",subplots=True)
#plt.show()

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalWidthCm,color="red",label="setosa")
plt.ylabel("setosa - PetalWidthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalWidthCm,color="green",label="setosa")
plt.ylabel("versicolor - PetalWidthCm")
plt.show()

"""