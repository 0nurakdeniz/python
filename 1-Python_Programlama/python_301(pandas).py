"""-----------pandas------------"""

import pandas as pd

dictionary ={"NAME" : ["ali","veli","kenan","hilal","onur","uğur"],
             "AGE": [19,22,23,25,26,28],
             "MAAS" : [100,150,200,250,340,220]}

#print(dictionary)

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1)