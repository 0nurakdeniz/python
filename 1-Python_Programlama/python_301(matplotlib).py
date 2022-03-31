
import pandas as pd

df = pd.read_csv("iris.csv")

#print(df.columns)

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

df1.plot(grid=True,linestyle=":")
plt.show()

plt.plot(setosa.Id,setosa.PetalLengthCm , color = "red", label = "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm , color = "green", label = "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm , color = "yellow", label = "virginica")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

#scatter plot