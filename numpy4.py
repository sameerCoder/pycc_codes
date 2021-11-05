# numpy class.


import numpy as np

a=np.array([1,2,3,4,5])
print(a)

a=np.array([1,2,3,4,5],ndmin=2)
print("ndmin:2",a)

a=np.array([1,2,3,4,5,6],ndmin=3)
print("ndmin:3",a)
