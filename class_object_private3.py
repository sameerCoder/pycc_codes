
class C(object): 
       def __init__(self): 
              self.c = 21
  
              # d is private instance variable  
              self.__d = 42
              
class D(C): 
       def __init__(self): 
              self.e = 84
              #C.__init__(self)

              
object1 = D() 

print("object1.e:",object1.e )
print("object1.c:",object1.c )
# produces an error as d is private instance variable
print(object1.d )
print(D.d )
