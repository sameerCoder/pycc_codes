# data hiding oops concept.
class MyClass(object): 
    # Hidden member of MyClass 
    __hiddenVariable = 0 # private attribute
    stream="cse" # public attribute
    # A member method that changes  
    # __hiddenVariable  
    def add(self, increment): 
        self.__hiddenVariable += increment 
        print ("self.__hiddenVariable :",self.__hiddenVariable)
        
# Driver code 
myObject = MyClass()      
myObject.add(2) 
myObject.add(5)
myobject2=MyClass()
myobject2.add(10)
print("MYClass.stream:",MyClass.stream) # with class name also we can call variable.
print("myobject.stream:",myObject.stream)

# Below line causes an error as __hiddenVariable is private attribute.
print ("MYClass.__hiddenVariable :",MyClass.__hiddenVariable) 
