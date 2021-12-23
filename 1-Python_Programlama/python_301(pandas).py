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

print(dataFrame1.columns)
print(dataFrame1.info())

print(dataFrame1.dtypes)

print('\n\n',dataFrame1.describe())