# pandas reading a text file.


import pandas as pd

df=pd.read_csv("pandastest.txt",delim_whitespace=True)
#print(df.head())
print(df.head())
print(df['class'][0:3])
    
print(df['class'])

newsubsetdf=df['class']
newsubsetdf.to_csv("onlyclassdata.txt",index=None)
