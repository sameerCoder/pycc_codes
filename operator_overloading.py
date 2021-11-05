# Polyphism

class Abc :

  def __init__ (self , a):

    self.a =a
   
  #def __str__(self):
    #return "Abc (%d,%d)" %(self.a, self.b)

  def __add__(self,other):

    return self.a + other.a 


obj1=Abc(1)
obj2=Abc(2)

obj3=Abc("Geeks")
obj4=Abc("For")

print(obj1+obj2)
print(obj3+obj4)



  
    
