# Numpy .

import numpy as np

a=np.array([[1,2],[3,4]])# 2 dimensional.

print(a)
print("a shape:",a.shape)
b=np.array([1,2,33,44,44,55],ndmin=2)
print(b)

print(b[0][1])

print("b shape:",b.shape)
print("b.size:",b.size)

c=np.arange(15).reshape(3,5)
print(c)
print("c shape:",c.shape)
print("c dimension:",c.ndim)

print("type of c :",type(c))
#cc=np.array([1,2,"hi",48.2])
#print(cc)

d=np.array([[12,32],[33,43]],dtype=complex)
print("d dtype complex :",d)

e=np.array([[32,56],[13,98]],dtype=float)
print("e dtype float :",e)

zeroarray=np.zeros((3,4))

print("Zero Array :",zeroarray)


onearray=np.ones((2,3,4),dtype=np.int16)
print("one array :",onearray)

rangevalue=np.arange(1000)
#print("rangevalue upto 999:",rangevalue)

print("reshape of 1000 values:",rangevalue.reshape(10,100))







    

















