#Encapsulation .
# Data Hiding Programme.

class datahidingdemo(object):
  __privatenum=3 # wch attribute
  _protectednum3=4 # wch attribute
  publicnum2=3 # wch attribute

  #class member variable ?
  # instance variable ?

  def displaynum(self):
    a=18
    self.__privatenum+=1
    # compound assignement .
    print ( "Number count : inside class function :",self.__privatenum)
numobj1=datahidingdemo()

numobj1.displaynum()

print ("num1.publicnum2",numobj1.publicnum2)
print ("num1._protectednum3",numobj1._protectednum3)
print ("num1.__privatenum",numobj1.__privatenum)
print ("num1._protectednum3",numobj1._protectednum3)
