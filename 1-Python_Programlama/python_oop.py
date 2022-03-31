
import numpy as np
import pandas as pd


array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[-1,:])

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array.reshape(3,3))

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

print(np.hstack((array1,array2)))

print(np.linspace(10,15,5))


dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1[dataFrame1.AGE > 60] 