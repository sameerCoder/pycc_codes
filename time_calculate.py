import time

t1=time.time()
print(time.time())

def squ(number):
    print(number*number*number*number*number*number*number*number)


squ(3434444)
print("time took to run this code:",time.time()-t1)
