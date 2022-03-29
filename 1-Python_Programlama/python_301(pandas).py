"""-----------pandas------------"""

import pandas as pd

dictionary ={"NAME" : ["ali","veli","kenan","hilal","onur","uğur"],
             "AGE": [19,22,23,25,26,28],
             "MAAS" : [100,150,200,250,340,220]}

#print(dictionary)

dataFrame1 = pd.DataFrame(dictionary)
#print(dataFrame1)

head = dataFrame1.head()
#print(head)

tail = dataFrame1.tail()
#print(tail)

#pandas basic method

#print(dataFrame1.columns)
#print(dataFrame1.info())

#print(dataFrame1.dtypes)

#print('\n\n',dataFrame1.describe()) 

#------indexing and slicing

#print(dataFrame1["NAME"])
#print(dataFrame1.AGE)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]
print(dataFrame1.yeni_feature)
print('////////////')

#print(dataFrame1.loc[:3, "NAME":"AGE"])

#print(dataFrame1.loc[::-1,:])


# -- filtering

filtre1 = dataFrame1.MAAS > 200

#print (type(filtre1))

filtelenmis = dataFrame1[filtre1]
#print(filtelenmis)
print('---------------------------')
print(dataFrame1[dataFrame1.AGE >= 26])

#-- List Comprehension

print(dataFrame1.MAAS.mean())

ort_maas = dataFrame1.MAAS.mean()

import numpy as np

print(np.mean(dataFrame1.MAAS))

dataFrame1["maas_sevyesi"] = ["yüksek" if ort_maas < x else "dusuk" for x in dataFrame1.MAAS]
print(dataFrame1)

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]
print(dataFrame1)

#-- concatenating data
dataFrame1.drop(["yeni_feature"],axis=1,inplace=True)
print (dataFrame1)

data1= dataFrame1.head()
data2= dataFrame1.tail()

print ('******************')

#vertical
print( pd.concat([data1,data2],axis=0))

#horizantal

print (pd.concat([dataFrame1.maas,dataFrame1.age],axis=1))

# -- transforming 

def multiply(age):
    return age*2

dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)
print(dataFrame1)