# pandas dataframe.

import pandas as pd

data1=[[1,2,3],[11,22,33]]
data2=[[11,22,55],[111,'bb','cc']]
dataor={'data1':data1,'data2':data2}
data=pd.DataFrame(dataor)
print(data)

