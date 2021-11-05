# Pandas 1
import pandas as pd


Data =[1, 3, 4, 5, 6, 2, 9]  # Numeric data 
  
# Creating series with default index values 
s = pd.Series(Data)
print(type(s))
print("s:",s)
print("s[:5]",s[:5])
print("s.head(3):",s.head(3))
print("s.tail(2):",s.tail(2))


# predefined index values 
Index =['a', 'b', 'c', 'd', 'e', 'f', 'g']  
si=pd.Series(Data,Index)
print("si:",si)


# Creating series with predefined index values
si=pd.Series(Data)
print("Series with default index :",si)
print("Series with default index : with head()",si.head())
si = pd.Series(Data, Index)
print("si with own index:",si)




######################################################
# Program to Create Dictionary series 
dictionary ={'da':1, 'db':2, 'dc':3, 'dd':4, 'de':5}  
  
# Creating series of Dictionary type 
sd = pd.Series(dictionary)
print(sd.head(3))
print(sd.tail(2))
print(sd.shape)
print(sd)


